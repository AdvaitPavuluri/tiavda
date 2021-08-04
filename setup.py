import setuptools
import subprocess
import os

tiavda_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in tiavda_version

assert os.path.isfile("tiavda/version.py")
with open("tiavda/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{tiavda_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tiavda",
    version=tiavda_version,
    author="Advait Pavuluri",
    author_email="advait.pavuluri@gmail.com",
    description="tiavda graphing util package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdvaitPavuluri/tiavda",
    packages=setuptools.find_packages(),
    package_data={"tiavda": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["tiavda = tiavda.main:main"]},
    install_requires=[
        "cryptography >= 3.4.4",
        "fabric >= 2.6.0",
        "paramiko >= 2.7.2",
        "requests >= 2.25.1",
        "apache-libcloud >= 3.3.1",
    ],
)