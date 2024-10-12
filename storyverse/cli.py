# storyverse/cli.py

import os
import argparse
from .version_control import StoryVersionControl

def init(args):
    path = args.path or os.getcwd()
    svc = StoryVersionControl(path)
    print(f"Initialized empty StoryVerse repository in {path}")

def main():
    parser = argparse.ArgumentParser(description="StoryVerse - Version Control for Interactive Stories")
    subparsers = parser.add_subparsers()

    init_parser = subparsers.add_parser('init', help='Initialize a new StoryVerse repository')
    init_parser.add_argument('path', nargs='?', help='Path to initialize the repository')
    init_parser.set_defaults(func=init)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()