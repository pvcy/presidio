import os.path
from os import path

import setuptools

__version__ = ""
parent_directory = os.path.abspath(os.path.join(path.abspath(path.dirname(__file__)), os.pardir))
with open(os.path.join(parent_directory, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

setuptools.setup(
    name="pvcy_presidio_analyzer",
    version=__version__,
    description="Presidio analyzer package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
#    url="https://github.com/Microsoft/presidio",
    url="https://github.com/pvcy/presidio",
    packages=[
        'presidio_analyzer',
        'presidio_analyzer.protobuf_models',
        'presidio_analyzer.predefined_recognizers',
        'presidio_analyzer.nlp_engine',
        'presidio_analyzer.recognizer_registry'
    ],
    package_dir={'pvcy_presidio_analyzer' : 'presidio_analyzer'},
#    trusted_host=['pypi.org'],
    tests_require=['pytest', 'flake8==3.7.9', 'pylint==2.3.1'],
    install_requires=[
        'cython==0.29.26',
        'spacy~=3.2',
        'regex==2019.12.17',
        'grpcio>=1.43.0',
        'protobuf>=3.19.1',
        'tldextract==2.2.1',
        'knack==0.6.2'],
    include_package_data=True,
    license='MIT',
    scripts=[
        'presidio_analyzer/presidio-analyzer',
        'presidio_analyzer/presidio-analyzer.bat',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
