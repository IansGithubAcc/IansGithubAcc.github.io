# This `homepage` package
The website you are currently looking at has been generated via a very small python package called `homepage`. The only thing the package contains are the following ellements:
- Markdown contents
- Python dependencies to generate this html
- The generated static website
- A single module for easy building

If you want to use this package yourself to make your own website, then use the following commands.
```
git clone https://github.com/IansGithubAcc/IansGithubAcc.github.io.git
cd IansGithubAcc
pip install -e .
python -m homepage.build
```

The package has yet to be addapted for generic use. I may do this in the future and publish on PyPI.