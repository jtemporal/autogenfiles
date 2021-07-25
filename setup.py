from setuptools import setup

REPO_URL = 'http://github.com/jtemporal/autogenfiles'

with open('README.md') as fobj:
    long_description = fobj.read()

setup(
    author='Jessica Temporal',
    author_email='hello@jtemporal.com',
    description='Auto generate files based on a template',
    zip_safe=False,
    install_requires=[
        'click==8.0.1',
        'Jinja2==3.0.1'
    ],
    keywords='auto generate files, jinja, templates, cli',
    license='MIT',
    long_description=long_description,
    name='autogenfiles',
    packages=[
        'autogenfiles'
    ],
    entry_points={
        'console_scripts': [
            'autogenfiles = autogenfiles.autogenfiles:AutoGenFiles',
        ],
    },
    url=REPO_URL,
    python_requires='>=3.8.2',
    version='0.0.4',
)
