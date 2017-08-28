from setuptools import setup

config = {
        'description': 'PROJECT DESCRIPTION',
        'author': 'Chris Heisel',
        'url': 'URL',
        'download_url': 'WHERE TO DOWNLOAD IT',
        'author_email': 'chris@heisel.org',
        'version': '0.0.1',
        'install_requires': [],
        'packages': ['pocket_curator'],
        'scripts': [],
        'name': 'pocket-curator'
}

# Add in any extra build steps for cython, etc.

setup(**config)
