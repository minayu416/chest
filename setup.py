import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chest",
    version="0.0.0",
    author="minayu416",
    author_email="minayu416@gmail.com",
    description="Chest for collecting function common-used and utility",
    long_description=long_description,
    url="https://github.com/minayu416/chest.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
