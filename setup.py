#!/usr/bin/env python

import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

setuptools.setup(
    name="chord_metadata_service",
    version="0.1.0",

    python_requires=">=3.6",
    install_requires=["chord_lib @ git+https://bitbucket.org/genap/chord_lib", "Django==2.2.6", "django-filter",
                      "djangorestframework", "psycopg2-binary", "requests"],

    author="Ksenia Zaytseva",

    description="An implementation of a variant store for the CHORD project.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=["chord_metadata_service"],
    include_package_data=True,

    url="https://github.com/c3g/chord_metadata_service",
    license="LGPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)