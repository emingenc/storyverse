import os
from .content_store import ContentStore
from .commit_store import Commit, CommitStore
from .branch_manager import BranchManager

class StoryVersionControl:
    def __init__(self, root_path):
        self.content_store = ContentStore(os.path.join(root_path, 'objects'))
        self.commit_store = CommitStore(os.path.join(root_path, 'objects'))
        self.branch_manager = BranchManager(root_path)

    def add_story_content(self, content, branch_name, author, message):
        content_hash = self.content_store.add_content(content)
        parent_hash = self.branch_manager.get_branch(branch_name)
        new_commit = Commit(content_hash, parent_hash, author, message)
        commit_hash = self.commit_store.add_commit(new_commit)
        self.branch_manager.update_branch(branch_name, commit_hash)
        return commit_hash

    def create_new_branch(self, name, from_commit_hash):
        self.branch_manager.create_branch(name, from_commit_hash)

    def get_story_timeline(self, branch_name):
        timeline = []
        current_commit_hash = self.branch_manager.get_branch(branch_name)
        
        while current_commit_hash:
            commit = self.commit_store.get_commit(current_commit_hash)
            content = self.content_store.get_content(commit.tree)
            timeline.append({
                "commit": commit,
                "content": content
            })
            current_commit_hash = commit.parent
        
        return timeline[::-1]  # Reverse to get chronological order