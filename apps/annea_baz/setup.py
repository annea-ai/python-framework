import os
import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text()

if 'CIRCLE_BUILD_NUM' in os.environ:
    version = f"0.1.{os.getenv('CIRCLE_BUILD_NUM')}"
else:
    version = '0.1.0'


def lib_path(lib_name):
    if os.getenv('CIRCLECI'):
        path = f"/home/circleci/project/libs/{lib_name}#egg={lib_name}"
    elif os.getenv('PROJECT_DIR'):
        path = f"{os.getenv('PROJECT_DIR')}/libs/{lib_name}"
    else:
        path = pathlib.Path(f"{here}/../../libs/{lib_name}").resolve()
    full_path = f'{lib_name} @ file://localhost/{path}#egg={lib_name}'
    return full_path


setup(
    name='annea_baz',
    version=version,
    description="An example python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="horken7",
    author_email="Johan Larsson Hörkén <johan.horken@annea.ai>",
    license="MIT",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        lib_path('annea_foo'),
        lib_path('annea_bar'),
        # add more packages if needed
    ],
    entry_points={
        "console_scripts": [
            'annea_baz = annea_baz.main:main'
        ]
    },
    url="https://github.com/annea-ai/python-framework/tree/master/libs/annea_foo"
)
