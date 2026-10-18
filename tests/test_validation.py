"""Regression tests for failure conditions that could leak or break publication."""
import importlib.util
from pathlib import Path
import sys
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import validate

class PublicationValidationTests(unittest.TestCase):
    def test_private_key_rejected(self):
        self.assertTrue(validate.secret_findings('-----BEGIN PRIVATE KEY-----'))

    def test_github_token_rejected(self):
        self.assertTrue(validate.secret_findings('ghp_'+'x'*36))

    def test_plain_task_instructions_are_not_secrets(self):
        self.assertFalse(validate.secret_findings('Review permissions and never publish a PIN or token.'))

    def test_private_tree_rejected(self):
        self.assertTrue(validate.public_path_errors(Path('maintenance/evidence.json')))

    def test_database_and_source_rejected(self):
        for name in ('shop.db','credentials.pem','private.md','config.yml','app.cs','run.ps1'):
            with self.subTest(name=name):self.assertTrue(validate.public_path_errors(Path(name)))

    def test_valid_generated_asset_allowed(self):
        self.assertFalse(validate.public_path_errors(Path('assets/images/demo.png')))

    def test_dotfiles_rejected(self):
        self.assertTrue(validate.public_path_errors(Path('.git/config')))

    def test_encoded_traversal_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.build') as directory:
            site=Path(directory);current=site/'index.html'
            with self.assertRaisesRegex(ValueError,'escapes'):
                validate.resolve_reference(site,current,'/%2e%2e/credentials.pem','docpremiumpos.getseek.net')

    def test_file_scheme_rejected(self):
        with self.assertRaisesRegex(ValueError,'scheme'):
            validate.resolve_reference(ROOT,ROOT/'index.html','file:///F:/Premium_POS/README.md','docpremiumpos.getseek.net')

    def test_encoded_anchor_and_nested_path(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.build') as directory:
            site=Path(directory);(site/'guide').mkdir();(site/'reference').mkdir()
            target,fragment=validate.resolve_reference(site,site/'guide/index.html','../reference/index.html#some%20anchor','docpremiumpos.getseek.net')
            self.assertEqual(target,site/'reference/index.html');self.assertEqual(fragment,'some anchor')

    def test_html_parser_collects_anchor_and_asset(self):
        page=validate.HTMLPage('<h2 id="sale">Sale</h2><img src="demo.png" alt="Demo"><a href="#sale">Sale</a>')
        self.assertIn('sale',page.ids);self.assertIn(('img','src','demo.png'),page.refs)

    def test_fenced_shell_comment_is_not_a_second_heading(self):
        self.assertEqual(validate.heading_count('# Launch\n```powershell\n# Run from Software\n```\n'),1)

    def test_two_actual_h1s_are_detected(self):
        self.assertEqual(validate.heading_count('# One\n\n# Two\n'),2)

    def test_source_registry_consistency(self):
        errors,counts=validate.validate_source()
        self.assertEqual(errors,[]);self.assertEqual(counts['features'],22)

    def _check_bad_output(self,relative,addition,expected):
        with tempfile.TemporaryDirectory(dir=ROOT/'.build') as directory:
            site=Path(directory)/'site'
            shutil.copytree(ROOT/'.build/site',site)
            changed=site/relative;changed.parent.mkdir(parents=True,exist_ok=True)
            with changed.open('a',encoding='utf-8') as handle:handle.write(addition)
            errors,_=validate.validate_site(site)
            self.assertTrue(any(expected in error for error in errors),errors)

    def test_generated_broken_link_rejected(self):
        self._check_bad_output('index.html','<a href="missing-page/">Missing</a>','missing href target')

    def test_generated_broken_anchor_rejected(self):
        self._check_bad_output('index.html','<a href="#this-anchor-does-not-exist">Missing</a>','missing anchor')

    def test_generated_private_config_rejected(self):
        self._check_bad_output('cloudflared.yml','ingress: []','forbidden output file type')

    def test_modified_reviewed_asset_rejected(self):
        self._check_bad_output('assets/brand/premium-mark.svg','<!-- unexpected change -->','asset not copied intact')

    def test_candidate_failure_preserves_previous_local_artifact(self):
        # A fresh independent worktree fixture can build with this interpreter's
        # dependencies. It has no application inputs or shared preview process.
        with tempfile.TemporaryDirectory(dir=ROOT/'.build') as directory:
            fixture=Path(directory)
            for name in ('docs','maintenance','scripts'):
                shutil.copytree(ROOT/name,fixture/name,ignore=shutil.ignore_patterns('snapshots','__pycache__','private-review'))
            for name in ('zensical.toml','project.json','requirements.lock'):
                shutil.copyfile(ROOT/name,fixture/name)
            previous=fixture/'.build/site';previous.mkdir(parents=True)
            marker=previous/'index.html';marker.write_text('known-good-local-artifact',encoding='utf-8')
            with (fixture/'docs/index.md').open('a',encoding='utf-8') as handle:
                handle.write('\n<a href="missing-stage-target.html">Broken candidate</a>\n')
            result=subprocess.run([sys.executable,'-B',str(fixture/'scripts/manage.py'),'build'],cwd=fixture,capture_output=True,text=True,encoding='utf-8')
            self.assertNotEqual(result.returncode,0,result.stdout)
            self.assertIn('missing',result.stderr.lower()+result.stdout.lower())
            self.assertEqual(marker.read_text(encoding='utf-8'),'known-good-local-artifact')
            self.assertEqual(list((fixture/'.build').glob('candidate-*')),[])

if __name__=='__main__':unittest.main()
