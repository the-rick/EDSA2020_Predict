from setuptools import setup, find_packages

setup(
    name='metricsPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA metrics package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/the-rick/EDSA2020_Predict',
    author='AnalyseGroup16',
    author_email='tbndondo@gmail.com'
)