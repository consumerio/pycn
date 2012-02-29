import os
from setuptools import setup, find_packages
 
import cn_client
 
LONG_DESCRIPTION = open('README.rst').read()
 
setup(
    name='python-cn-client',
    version=cn_client.__version__,
    description="The official Python client for the Consumer Notebook API",
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
    keywords='python,rest,json',
    author=cn_client.__author__,
    author_email='pydanny@consumernotebook.com',
    url='http://github.com/consumernotebook/python-cn-client',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests==0.10.6'],
    zip_safe=False,
)