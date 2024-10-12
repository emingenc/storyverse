import hashlib
import json
from fs import open_fs

class Commit:
    def __init__(self, tree, parent, author, message):
        self.tree = tree
        self.parent = parent
        self.author = author
        self.message = message
        self.hash = self._calculate_hash()

    def _calculate_hash(self):
        commit_data = f"{self.tree}{self.parent}{self.author}{self.message}"
        return hashlib.sha1(commit_data.encode()).hexdigest()

    def serialize(self):
        return json.dumps({
            "tree": self.tree,
            "parent": self.parent,
            "author": self.author,
            "message": self.message
        })

class CommitStore:
    def __init__(self, root_path):
        self.fs = open_fs(root_path)

    def add_commit(self, commit):
        with self.fs.open(commit.hash, 'w') as f:
            f.write(commit.serialize())
        return commit.hash

    def get_commit(self, commit_hash):
        with self.fs.open(commit_hash, 'r') as f:
            data = json.loads(f.read())
        return Commit(data['tree'], data['parent'], data['author'], data['message'])