import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="infer-gender",
    version="0.2.0.2",
    description="Infer gender from the Indian first name or full name",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bnriiitb/infer-gender",
    author="Nagaraju Budigam",
    author_email="nagaraju.iith@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["scikit_learn>0.22","tensorflow>2.3.0"],
    include_package_data=True,
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],

    # entry_points={
    #     "console_scripts": [
    #         "infer_gender=infer_gender.__main__:main",
    #     ]
    # },
)
