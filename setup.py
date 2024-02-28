# setup.py - responsible in creating the ML application as a package.

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='sgk',
author_email='gksrikanth11@gmail.com',
packages=find_packages(), # it will check, in how many folders do we have a file called "__init__.py". Since, it is found in src folder, the src is considered as package
#install_requires=['pandas', 'numpy', 'seaborn']
install_requires=get_requirements('requirements.txt')

)