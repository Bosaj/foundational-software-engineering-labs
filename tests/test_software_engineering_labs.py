import os
import sys
import unittest

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
tp4_dir = os.path.join(repo_root, "POO Python", "pythonProject", "python TP4")
if tp4_dir not in sys.path:
    sys.path.insert(0, tp4_dir)


class TestFoundationalLabs(unittest.TestCase):
    def test_compte_oop_logic(self):
        try:
            from EX1 import Compte
            c = Compte("TestUser", 99999, 1000)
            self.assertEqual(c.balance, 1000)
            c.deposer(500)
            self.assertEqual(c.balance, 1500)
            c.retirer(200)
            self.assertEqual(c.balance, 1300)
        except Exception as e:
            self.fail(f"Compte class test failed: {e}")

    def test_curriculum_and_architecture_docs(self):
        docs_dir = os.path.join(repo_root, "docs")
        self.assertTrue(os.path.isdir(docs_dir))
        self.assertTrue(os.path.exists(os.path.join(docs_dir, "ARCHITECTURE.md")))
        self.assertTrue(os.path.exists(os.path.join(docs_dir, "CURRICULUM_MATRIX.md")))


if __name__ == "__main__":
    unittest.main()
