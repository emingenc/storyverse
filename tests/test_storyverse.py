import unittest
from storyverse import StoryVersionControl
import tempfile
import shutil

class TestStoryVerse(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.svc = StoryVersionControl(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_add_story_content(self):
        content = "Once upon a time..."
        commit_hash = self.svc.add_story_content(content, "main", "Author1", "Initial commit")
        self.assertIsNotNone(commit_hash)

    def test_create_new_branch(self):
        content = "Once upon a time..."
        commit_hash = self.svc.add_story_content(content, "main", "Author1", "Initial commit")
        self.svc.create_new_branch("new_branch", commit_hash)
        timeline = self.svc.get_story_timeline("new_branch")
        self.assertEqual(len(timeline), 1)
        self.assertEqual(timeline[0]['content'], content)

if __name__ == '__main__':
    unittest.main()