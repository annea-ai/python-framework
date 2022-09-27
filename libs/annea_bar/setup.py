import os
import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text()

if 'CIRCLE_BUILD_NUM' in os.environ:
    version = f"0.1.{os.getenv('CIRCLE_BUILD_NUM')}"
else:
    version = '0.1.0'

setup(
    name='annea_bar',
    version=version,
    description="An example python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="horken7",
    author_email="Johan Larsson Hörkén <johan.horken@annea.ai>",
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[],
    url="https://github.com/annea-ai/python-framework/tree/master/libs/annea_bar"
)
