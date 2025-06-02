# This package
## Description
The page you are currently looking at is part of a very small python package called `homepage`. The package contains no code of its own, only the following elements:
- The markdown content that makes up the pages
- Deployment script for Github Actions
- `pyproject.toml` with dependencies

```{note}
Previously, this site was build using the [Sphinx](https://www.sphinx-doc.org/en/master/) and the [`myst_parser`](https://myst-parser.readthedocs.io/en/latest/intro.html). However, since Sphinx is really orientated towards Python package documentation, I've decided to move to solely [MySTmd](https://mystmd.org/) for website building.
```

## Do it yourself
If you want to use this package yourself to make your own website, then fork this package from the repo [here](https://github.com/IansGithubAcc/IansGithubAcc.github.io). The package and its dependencies can easily be installed using the following command from the root of your repo.
```
pip install -e .
```
Alternatively, you can also use [MySTmd](https://mystmd.org/) directly. Sadly, their automated github pages workflow did not work for me and I had to create the pipeline manually.

Now you got everything to build the website! Simply call `myst` or `python -m mystmd_py.main` to launch a local webserver.