from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="TOpsPy",
    version="0.0.2",
    author="BijanSeif (Bijan Sayyafzadeh)",
    author_email="<b.sayyaf@yahoo.com>",
    description="OpenseesPy Functions",
    long_description_content_type="text/markdown",
    long_description=long_description ,
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



