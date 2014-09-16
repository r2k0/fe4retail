try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Le Chef',
    'author': 'Okkar Than',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lechef'],
    'scripts': [],
    'name': 'lechef'
}

setup(**config)
