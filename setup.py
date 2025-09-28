from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e.'
def get_requirement(file_path:str):
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [requirement.replace('/n','') for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='project_0001',
version='',
author='FAKER_112',
author_email='',
packages=find_packages(),
install_requires=get_requirement('requirements.txt')

)