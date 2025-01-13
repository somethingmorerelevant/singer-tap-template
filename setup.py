#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="tap-name",
    version="2.0.2",
    description="Singer.io tap for extracting data from the name API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="authorname",
    author_email="authorname@domain.com",
    url="https://singer.io",
    py_modules=["tap_name"],
    install_requires=[
        "singer-python>=5.13.0", 
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pylint",
            "ipdb",
            "pytest",  # For testing
        ]
    },
    entry_points={
        "console_scripts": [
            "tap-name=tap_name:main",  # Assuming 'main' is the entry point function in your module
        ],
    },
    packages=find_packages(exclude=["tests"]),
    package_data={"schemas": ["tap_name/schemas/*.json"]},
    include_package_data=True,
    project_urls={  # Additional URLs (if any)
        'Documentation': 'https://www.singer.io/tap/name',
    },
)
