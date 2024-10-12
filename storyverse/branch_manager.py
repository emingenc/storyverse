from fs import open_fs
import os

class BranchManager:
    def __init__(self, root_path):
        self.fs = open_fs(os.path.join(root_path, 'refs', 'heads'))

    def create_branch(self, name, commit_hash):
        with self.fs.open(name, 'w') as f:
            f.write(commit_hash)

    def update_branch(self, name, new_commit_hash):
        self.create_branch(name, new_commit_hash)

    def get_branch(self, name):
        with self.fs.open(name, 'r') as f:
            return f.read().strip()