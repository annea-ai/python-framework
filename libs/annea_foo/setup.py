from setuptools import setup

setup(
    name='annea_foo',
    version="0.1.0",
    author="horken7",
    author_email="johan.horken@annea.ai",
    description="An example python package",
    license="MIT",
    packages=['src'],
    install_requires=[
        'annea_bar',
        # add more packages if needed
    ],
)