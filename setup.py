from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="boardify",
    version="0.1.0",
    description=" A web-based dashboard to analyzing your data with Python ",
    long_description=long_description,
    license="MIT",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    url="https://lucas-hild.de",
    packages=["boardify"],
    install_requires=[
        "flask"
    ],
)