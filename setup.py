try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python API for sentiment140',
    'author': 'Deepu Philip',
    'url': '',
    'download_url': '',
    'author_email': 'deepu.dtp@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['sentiment140'],
    'scripts': [],
    'name': 'sentiment140'
}

setup(**config)
