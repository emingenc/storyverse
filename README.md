# StoryVerse

StoryVerse is a version control system for interactive, branching time-travel stories. It provides a Git-like approach to managing story content, allowing for immutable history, branching timelines, and easy version tracking.

## Installation

You can install StoryVerse using pip:

```bash
pip3 install storyverse
```

## Quick Start

To initialize a new StoryVerse repository:


```bash
storyverse init [path]
```

### Basic Usage

Here's a simple example of how to use StoryVerse:

```python
from storyverse import StoryVersionControl

# Initialize a new StoryVerse repository
svc = StoryVersionControl("/path/to/story/repo")

# Start a new story
initial_content = "Once upon a time in a galaxy far, far away..."
main_branch = svc.add_story_content(initial_content, "main", "Author1", "Initial commit")

# Add to the main storyline
next_content = "A young Jedi embarked on an epic journey..."
svc.add_story_content(next_content, "main", "Author1", "Add Jedi's journey")

# Create an alternate timeline
svc.create_new_branch("alternate_timeline", main_branch)
alternate_content = "Instead of a Jedi, a Sith Lord rose to power..."
svc.add_story_content(alternate_content, "alternate_timeline", "Author2", "Add Sith Lord storyline")

# View the main timeline
main_timeline = svc.get_story_timeline("main")
for entry in main_timeline:
    print(f"Content: {entry['content']}")
    print(f"Author: {entry['commit'].author}")
    print(f"Message: {entry['commit'].message}")
    print("---")

```

## Key Features

- **Immutable History**: Once a piece of content is committed, it cannot be altered or deleted.
- **Branching**: Create multiple storylines or timelines from any point in the story.
- **Version Control**: Keep track of all changes and versions of your story.
- **Author Attribution**: Each piece of content is associated with an author.
- **Commit Messages**: Add descriptive messages to each story commit.

## Advanced Usage

### Creating a New Branch

```python
svc.create_new_branch("new_branch_name", "commit_hash_to_branch_from")
```

### Viewing a Specific Branch's Timeline
    
```python
branch_timeline = svc.get_story_timeline("branch_name")
```

### Adding Multiple Story Segments
    
```python
    story_segments = [
    "In a world where magic flowed like water...",
    "A young apprentice discovered an ancient tome...",
    "The tome revealed secrets of forgotten spells..."
]

for segment in story_segments:
    svc.add_story_content(segment, "branch_name", "Author", f"Add segment: {segment[:20]}...")
```

### Command Line Interface

StoryVerse also provides a command-line interface for basic operations:

```bash
# Initialize a new repository
storyverse init [path]

# Add new content to a branch
storyverse add "Your story content" --branch main --author "Your Name" --message "Commit message"

# Create a new branch
storyverse branch new_branch_name --from commit_hash

# View timeline of a branch
storyverse timeline branch_name
```