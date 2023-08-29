from setuptools import setup, find_packages
setup(
    name = "bims",
    version = "1.0.0",
    description = "This is basic books inventary  management system.",
    author = "Prashik Dewtale",
    package_dir = {"": "bims"},
    packages=find_packages(where="bims"),
    license="MIT",
    classifiers = [
    "Programming Language :: Python :: 3",
    "Licence :: OSI Approved :: MIT Licence"
    "Operating System :: OS Independent",
    ]
    )
