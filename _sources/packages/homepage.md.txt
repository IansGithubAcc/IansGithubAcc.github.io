# This `homepage` package
The website you are currently looking at has been generated via a very small python package called `homepage`. The only thing the package contains are the following ellements:
- The markdown content that makes up the pages
- A single module for easy building
- The builded static website

If you want to use this package yourself to make your own website, then fork this package from the repo [here](https://github.com/IansGithubAcc/IansGithubAcc.github.io). The package and its dependencies can easily be installed using the following command from the root of your repo.
```
pip install -e .
```
Now you got everything to build the website! Simply call the following build in module from the root of your repo.
```
python -m homepage.build
```

```{note}
Usually, you would not store the documentation build on your repo. However since I'm using github pages to host my website, this is exactly what I do.
```