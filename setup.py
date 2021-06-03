# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        return description
    except Exception:
        return '''
    Pyrandwalk is a tool for simulating random walks,
    calculate the probability of given state sequences and etc.
    Random walk is a representation of discrete-time,
    discrete-value Markov chain model using in stochastic processes..'''


setup(
    name='pyrandwalk',
    packages=['pyrandwalk'],
    version='1.0',
    description='Python Library for Random Walks',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sadra Sabouri',
    author_email='sabouri.sadra@gmail.com',
    url='https://github.com/sadrasabouri/pyrandwalk',
    download_url='https://github.com/sadrasabouri/pyrandwalk/tarball/v1.0',
    keywords="random-walk markov-chain stochastic-processes",
    project_urls={
        'Source': 'https://github.com/sadrasabouri/pyrandwalk',
    },
    install_requires=get_requires(),
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    license='MIT',
)
