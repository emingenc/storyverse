import hashlib
import os
from fs import open_fs

class ContentStore:
    def __init__(self, root_path):
        self.fs = open_fs(root_path)

    def add_content(self, content):
        content_hash = hashlib.sha1(content.encode()).hexdigest()
        with self.fs.open(content_hash, 'w') as f:
            f.write(content)
        return content_hash

    def get_content(self, content_hash):
        with self.fs.open(content_hash, 'r') as f:
            return f.read()