from setuptools import setup

setup(
   name='PiIO',
   version='1.0',
   description='PiIO IO library',
   author='K Lawson',
   author_email='keithl.online@gmail.com',
   packages=['PiIO'],  #same as name
   install_requires=['futures'] #external packages as dependencies
)
