#!/usr/bin/env python
"""
responses
=========

A utility library for mocking out the `requests` Python library.

:copyright: (c) 2015 David Cramer
:license: Apache 2.0
"""

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

setup_requires = []

install_requires = [
    "requests>=2.30.0,<3.0",
    "urllib3>=2.0.0,<3.0",
    "pyyaml",
    "types-PyYAML",
    "typing_extensions; python_version < '3.8'",
]

tests_require = [
    "pytest>=7.0.0",
    "coverage >= 6.0.0",
    "pytest-cov",
    "pytest-asyncio",
    "pytest-httpserver",
    "flake8",
    "types-requests",
    "mypy",
    # for check of different parsers in recorder
    "tomli; python_version < '3.11'",
    "tomli-w",
]

if "test" in sys.argv:
    setup_requires.extend(tests_require)

extras_require = {"tests": tests_require}


class PyTest(TestCommand):
    """Designed to be run via `python setup.py test`"""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="responses",
    version="0.23.1",
    author="David Cramer",
    description="A utility library for mocking out the `requests` Python library.",
    url="https://github.com/getsentry/responses",
    project_urls={
        "Bug Tracker": "https://github.com/getsentry/responses/issues",
        "Changes": "https://github.com/getsentry/responses/blob/master/CHANGES",
        "Documentation": "https://github.com/getsentry/responses/blob/master/README.rst",
        "Source Code": "https://github.com/getsentry/responses",
    },
    license="Apache 2.0",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    packages=["responses"],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
    cmdclass={"test": PyTest},
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development",
    ],
)
