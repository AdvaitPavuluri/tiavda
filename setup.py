import setuptools

# Tutorial used: https://dzone.com/articles/executable-package-pip-install

setuptools.setup(
     name='tiavda',
     version='0.2',
     scripts=['scripts/tiavda_setup.sh'],
     author="Advait Pavuluri",
     author_email="advait.pavuluri@gmail.com",
     description="Utility package for graphing.",
     long_description="Advait's graphing Python util package.",
   long_description_content_type="text/markdown",
     url="https://github.com/AdvaitPavuluri/tiavda",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )