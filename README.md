# Chest Python Package

The chest box for collecting useful python function or objects that can be common used for different projects

# install guide

```
# pip install git+https://git@repo-address.git
pip install git+https://github.com/minayu416/chest.git
```

# Generate Sphinx Document

***Using Sphinx for wring document.***

```
sphinx-apidoc -f -o ./document .
sphinx-build -b singlehtml ./document ./document/_build
```