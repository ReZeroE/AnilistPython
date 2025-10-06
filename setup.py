import os
from setuptools import setup, find_packages

setup(
    name="AnilistPython",
    version="1.0.0",
    author="Kevin L.",
    author_email="kevinliu@vt.edu",
    description="Anilist Python library (anilist.co APIv2 wrapper) to fetch anime, manga, and character information through the Anilist GraphQL API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ReZeroE/AnilistPython",
    project_urls={
        "Bug Tracker": "https://github.com/ReZeroE/AnilistPython/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    license="MIT",
    package_dir={"AnilistPython": "src"},
    packages= ["AnilistPython"],
    python_requires=">=3.8",
    install_requires=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")).read().splitlines(),
    include_package_data=True
)