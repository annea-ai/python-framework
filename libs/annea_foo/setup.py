from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='annea_foo',
    version="0.1.2",
    description="An example python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="horken7",
    author_email="Johan Larsson Hörkén <johan.horken@annea.ai>",
    license="MIT",
    packages=['src'],
    install_requires=[
        'annea_bar',
        # add more packages if needed
    ],
    url="https://github.com/annea-ai/python-framework/tree/master/libs/annea_foo"
)