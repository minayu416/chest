import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MythChest",
    version="0.0.1",
    author="minayu416",
    author_email="minayu416@gmail.com",
    description="Myth Chest for collecting function or object common-used and utility",
    long_description=long_description,
    url="https://github.com/minayu416/chest.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
