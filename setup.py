from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
   name='LinkedList',
   version='1.0',
   description='Linked List implementation',
   license=license,
   long_description=long_description,
   author='Mateusz Mazurkiewicz',
   author_email='m.mazurkiewicz91@gmail.com',
   url="https://github.com/MateuszMazurkiewicz/LinkedList",
   packages=["linked_list"], 
)