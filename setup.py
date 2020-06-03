from setuptools import setup

setup(
    name="whatthefuzz",
    version="version = 0.2.2",
    description="Web fuzzer",
    url="https://github.com/javixeneize/wtfuzz",
    author="Javier Dominguez",
    packages=["whatthefuzz"],
    include_package_data=True,
    install_requires=["requests>=2.22.0"]
)