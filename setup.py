import os
from setuptools import setup, find_packages
 
import pycn
 
LONG_DESCRIPTION = open('README.rst').read()
 
setup(
    name='pycn',
    version=pycn.__version__,
    description="A Python library for accessing the Consumer Notebook API.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='consumernotebook,python,rest,json',
    author=pycn.__author__,
    author_email='pydanny@consumernotebook.com',
    url='http://github.com/consumernotebook/pycn',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==0.10.6',
    ],
    zip_safe=False,
)