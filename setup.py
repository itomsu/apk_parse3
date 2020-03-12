import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apk_parse3",
    version="1.0.0",
    author="tomsu",
    author_email="itomsu@gmail.com",
    description="APK Parser for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itomsu/apk_parse3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires = [
        'future==0.16.0',
        'pyasn1==0.2.3',
        'cryptography==1.8.1'
    ]
)
