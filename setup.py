from setuptools import setup

requirements = ['requests==2.22.0',]
setup(
    install_requires=requirements,
    author='Javier Dominguez',
    name='wtfuzz',
    packages=['wtfuzz'],
    version='0.1',
    zip_safe=False,
)