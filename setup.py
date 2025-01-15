from setuptools import setup, find_packages

setup(
    name="mzrandom",
    version="1.0.0",
    description="A comprehensive and high-entropy random number generator library.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author='Mohammad Zarghami',
    author_email='zamohammad1387@gmail.com',
    url="https://github.com/mohammadzarghami/mzrandom",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
