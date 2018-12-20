import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_to_json",
    version="0.0.3",
    author="ruturaj4",
    author_email="ruturajkvaidya@gmail.com",
    description="A simple csv to json coverter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ruturaj4/csv_to_json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
