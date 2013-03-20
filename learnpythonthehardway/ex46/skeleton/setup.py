#!/usr/bin/env python2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        "description" : "My Project",
        "author" : "zhulei",
        "url" : "URL to get it at.",
        "download_url" : "where to download it.",
        "author_email" : "uhziel@gmail.com",
        "version" : "0.1",
        "install_requires" : ["nose"],
        "packages" : ["NAME"],
        "scripts" : [],
        "name" : "projectname"
}

setup(**config)
