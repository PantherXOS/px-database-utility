import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.4'
PACKAGE_NAME = 'px-database-utility'
AUTHOR = 'Franz Geffke'
AUTHOR_EMAIL = 'franz@pantherx.org'
URL = 'https://git.pantherx.org/development/applications/px-database-utility'

LICENSE = ''
DESCRIPTION = 'Easily dump (backup), restore and list PostgreSQL databases.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
	'psycopg2'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'px-database-utility=px_database_utility.command_line:main',
            'px-db-util=px_database_utility.command_line:main'
        ],
    },
    packages=find_packages(),
    zip_safe=False
)
