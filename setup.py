from setuptools import setup

setup(
    name="wtfuzz",
    version="0.1.1",
    description="Web fuzzer",
    url="https://github.com/javixeneize/wtfuzz",
    author="Javier Dominguez",
    packages=["whatthefuzz"],
    include_package_data=True,
    install_requires=["requests==2.22.0"]
)