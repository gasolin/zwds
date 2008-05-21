try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from pkg_resources import DistributionNotFound

import sys
import os
import glob

execfile(os.path.join('zwds', 'release.py'))

# setup params
# nose is used for test
required_modules = {}
extra_modules = {'nose':  ["nose>=0.9"]}

setup(
    name="zwds",
    version=version,
    author=author,
    author_email=email,
    download_url="http://code.google.com/p/zwds/downloads/list",
    license=license,
    keywords = "traditional, chinese",
    description=description,
    long_description=long_description,
    url=url,
    zip_safe=False,
    install_requires = required_modules,
    extras_require = extra_modules,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup", 'examples', 'apidocs']),
    entry_points = """
    """,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite = 'nose.collector',
    )

