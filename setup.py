from setuptools import setup
import os.path

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = 'mta_data'

requires = [
    'tributary>=0.1.4',
    'protobuf>=3.13.0',
    'httpx>=0.16.1 '  
]

requires_dev = [
    'flake8>=3.8.3',
    'pytest>=6.0.1',
    'autopep8>=1.5.4'
] + requires

setup(
    name=name,
    install_requires=requires,
    extras_require={
        'dev': requires_dev,
    }
)