#!/usr/bin/env python
from setuptools import setup,find_packages

setup(
    name = 'notifo-imap-listener',
    version = '0.4.2',
    py_modules = ['notifo-imap-listener'],
    data_files = [('.', ['config.ini.sample'])],

    author = 'Todd Eddy',
    author_email = 'vr@vrillusions.com',
    description = 'Listens for incoming mail and forwards it to notifo.',
    url = 'https://github.com/vrillusions/notifo-imap-listener',
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email",
        "Topic :: Internet",
        ],
)
