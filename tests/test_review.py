"""Negative controls for misleading review connections and incomplete choices."""
import copy
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import validate_review as review

class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.data=review.load('maintenance/code-review-index.json')
        self.workflows=review.load('maintenance/review-workflows.json')['workflows']
        self.decisions=review.load('maintenance/review-decisions.json')['findings']
        self.features=[f['id'] for f in review.load('maintenance/features.json')['features']]
        self.rules=review.load('maintenance/review-rules.json')['rules']
    def errors(self):return review.validate_records(self.data,self.workflows,self.decisions,self.features,self.rules)
    def test_rule_cannot_claim_runtime_acceptance(self):
        self.rules[0]['verification']='runtime verified'
        self.assertTrue(any('rule evidence' in e for e in self.errors()))
    def test_snapshot_consistent(self):self.assertEqual(self.errors(),[])
    def test_missing_command_coverage_rejected(self):
        next(w for w in self.workflows if w['commands'])['commands'].pop()
        self.assertTrue(any('coverage' in e for e in self.errors()))
    def test_unknown_handler_reference_rejected(self):
        self.data['commands'][0]['methods']=['M-unknown']
        self.assertTrue(any('unknown handler' in e for e in self.errors()))
    def test_source_line_drift_rejected(self):
        self.decisions[0]['sources'][0]['line']=999999
        self.assertTrue(any('line outside' in e for e in self.errors()))
    def test_source_digest_drift_rejected(self):
        self.decisions[0]['sources'][0]['sha256']='0'*64
        self.assertTrue(any('stale source' in e for e in self.errors()))
    def test_source_traversal_rejected(self):
        self.data['other_files'][0]['path']='Software/../../private.cs'
        self.assertTrue(any('unsafe source' in e for e in self.errors()))
    def test_unknown_fk_parent_rejected(self):
        next(t for t in self.data['schema']['tables'] if t['foreign_keys'])['foreign_keys'][0]['parent']='missing_table'
        self.assertTrue(any('foreign-key endpoint' in e for e in self.errors()))
    def test_choice_without_acceptance_rejected(self):
        self.decisions[0]['options'][0]['acceptance']=[]
        self.assertTrue(any('steps/checks' in e for e in self.errors()))
    def test_duplicate_command_assignment_rejected(self):
        self.workflows[0]['commands'].append(self.data['commands'][0]['name'])
        self.assertTrue(any('coverage' in e for e in self.errors()))

if __name__=='__main__':unittest.main()
