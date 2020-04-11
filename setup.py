import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="whatthefuzz",
    version="0.1.0",
    description="Web fuzzer",
    url="https://github.com/javixeneize/wtfuzz",
    author="Javier Dominguez",
    packages=["whatthefuzz"],
    include_package_data=True,
    install_requires=["requests==2.22.0"]
)