import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='polign',
      version='1.0',
      description='polign',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Janusz Janowski',
      author_email='esentino@gmail.com',
      url='',
      keywords='python test poligon',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires
      )
