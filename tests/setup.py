from setuptools import setup, find_packages

setup(
    name="ghostdata",
    version="0.1",
    packages=find_packages(),
    install_requires=["pillow", "pypdf"],
    author="Oxde",
    description="GhostData: Securely remove metadata from images & PDFs",
    url="https://github.com/Oxde",
    license="AGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
