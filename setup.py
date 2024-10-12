from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="storyverse",
    version="0.1.1",
    author="Emin Genc",
    author_email="emingench@gmai.com",
    description="A version control system for interactive, branching time-travel stories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/storyverse",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fs>=2.4.13",
    ],
    entry_points={
        'console_scripts': [
            'storyverse=storyverse.cli:main',
        ],
    },
)