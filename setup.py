import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="infer-gender",
    version="0.1.0",
    description="Infers gender from an Indian first name or full name",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bnriiitb/infer-gender",
    author="Nagaraju Budigam",
    author_email="nagaraju.iith@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["infer_gender"],
    include_package_data=True,
    install_requires=["missingno", "pandas","numpy","matplotlib","scikit_learn","tensorflow","tensorflow_addons"],
    entry_points={
        "console_scripts": [
            "infer_gender=infer_gender.__main__:main",
        ]
    },
)