import re

import setuptools

requirements = [
    "sqlalchemy-json",
    "python-decouple",
    "python-dotenv",
    "aiofiles",
    "aiohttp",
    "sqlalchemy",
    "pytz",
]


with open("LionX/version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "py-LionX"
author = "TeamLionX"
author_email = "teamlionz786@gmail.com"
description = "A Secure and Powerful Python-Telethon Based Library For Ultroid Userbot."
license_ = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/TeamLionX/Lion-X"
project_urls = {
    "Bug Tracker": "https://github.com/TeamLionX/Lion-X/issues",
    "Documentation": "https://teamlionx.github.io/LionX/",
    "Source Code": "https://github.com/TeamLionX/Lion-X",
}
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    project_urls=project_urls,
    license=license_,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">3.7, <3.11",
)
