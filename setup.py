import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'django-intellipages',
    version = '0.1',
    url = 'http://github.com/trilan/django-intellipages',
    license = 'BSD',
    description = (
        'This app provides one tiny but useful '
        'template filter for page navigation'),
    long_description = read('README.rst'),

    author = 'Mike Yumatov',
    author_email = 'yumatov@trilan.ru',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
