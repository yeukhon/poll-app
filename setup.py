import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'gunicorn',
    'psycopg2'
    ]

test_requires = [
    'requests',
    'nose',
    'mock'
]

setup(name='pollapp',
      version='0.0',
      description='pollapp',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pollapp',
      install_requires=requires,
      test_require=test_requires,
      entry_points="""\
      [paste.app_factory]
      main = pollapp:main
      [console_scripts]
      initialize_pollapp_db = pollapp.scripts.initializedb:main
      """,
      )
