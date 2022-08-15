import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "panda_object_creation_module",#module name
    version = "0.1",
    author = "Bruno Maximilian Voß",
    author_email = "bruno.m.voss@gmail.com",
    description = ("some small functions for easier object creation"),
    
    license = "MIT",
    keywords = "panda",
   
    packages=['panda_object_create'],#foldername
    
)
