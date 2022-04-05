from setuptools import setup, find_packages

import subprocess
import os

TopsPy_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

assert "." in TopsPy_version

assert os.path.isfile("topspy/version.py")
with open("topspy/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{TopsPy_version}\n")



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="TOpsPy",
    version=TopsPy_version,
    author="BijanSeif (Bijan Sayyafzadeh)",
    author_email="<b.sayyaf@yahoo.com>",
    description="OpenseesPy Functions",
    long_description_content_type="text/markdown",
    long_description=long_description ,
    package_data={
        "":["*.AT2","*.At2","*.at2"],
        # If any package contains *.txt or *.rst files, include them:
        #"": ["*.txt", "*.rst"],
        # And include any *.msg files found in the "hello" package, too:
        #"hello": ["*.msg"],
    },
    packages=find_packages(),
    install_requires=['openseespy', 'eseesminipy','numpy'],
    url="https://github.com/BijanSeif",
    keywords=['python', 'opensees', 'Modeling', 'Dynamic'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows'
    ],

)
