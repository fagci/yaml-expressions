import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="yaml-expressions",
    version="0.2.1",
    author="Mikhail Yudin",
    author_email="fagci.nsk@gmail.com",
    description=("Jinja2 templates for yaml. Make dynamic rules and configs."),
    license="MIT",
    keywords="yaml jinja2 exptessions template",
    url="https://github.com/fagcinsk/yaml-expressions",
    packages=['yex'],
    install_requires=['pyyaml', 'jinja2'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
