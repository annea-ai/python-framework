import os

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if 'CIRCLE_BUILD_NUM' in os.environ:
    version = f"0.1.{os.getenv('CIRCLE_BUILD_NUM')}"
else:
    version = '0.1.0'

setup(
    name='annea_foo',
    version=version,
    description="An example python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="horken7",
    author_email="Johan Larsson Hörkén <johan.horken@annea.ai>",
    license="MIT",
    packages=['src'],
    install_requires=[
        'annea_bar==0.1.0',
        # add more packages if needed
    ],
    url="https://github.com/annea-ai/python-framework/tree/master/libs/annea_foo"
)