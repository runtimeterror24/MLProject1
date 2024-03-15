from setuptools import find_packages,setup
from typing import List


E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will reutrn list of requirements(packages)
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if E_DOT in requirement:
            requirement.remove(E_DOT)
            
    return requirement



setup(
name='MLPROJECT1',
version='0.0.1',
author='PriyankAcharekar24',
author_email='priyank.acharekar24@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)