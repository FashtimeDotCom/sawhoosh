import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'repoze.tm2>=1.0b1', # default_commit_veto
    'sqlalchemy',
    'zope.sqlalchemy',
    'WebError',
    'whoosh',
    'pyramid_beaker',
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='sawhoosh',
      version='0.0',
      description='sawhoosh',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require = requires,
      test_suite="sawhoosh",
      entry_points = """\
      [paste.app_factory]
      main = sawhoosh:main
      """,
      paster_plugins=['pyramid'],
      )

