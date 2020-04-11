import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="wtfuzz",
    version="0.0.1",
    description="Web fuzzer",
    url="https://github.com/javixeneize/wtfuzz",
    author="Javier Dominguez",
    packages=["wtfuzz"],
    include_package_data=True,
    install_requires=["requests==2.22.0"]
)