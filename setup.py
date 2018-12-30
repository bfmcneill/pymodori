from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pymodori',
    version='0.1.0',
    description='pomodoro app written in python 3',
    long_description=readme,
    author='Ben McNeill',
    author_email='ben@activeprogrammer.com',
    url='https://github.com/bfmcneill/pymodori',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
