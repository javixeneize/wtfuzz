from setuptools import setup

requirements = ['requests==2.22.0',
'behave==1.2.6']
setup(
    install_requires=requirements,
    author='Javier Dominguez',
    name='wtfuzz',
    packages=['src'],
    version='0.1',
    zip_safe=False,
)