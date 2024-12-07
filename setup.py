from setuptools import find_packages, setup
from typing import List

# HYPEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     This funcfion will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n", "") for req in requirements]

#         if HYPEN_E_DOT in requirements: 
#             requirements.remove(HYPEN_E_DOT)

#     return requirements
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e .")]

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Nayeon Kim',
author_email='lkim0731@gmail.com',
packages=find_packages(),
# install_requires=['pandas', 'numpy', 'seaborn']
install_requires=get_requirements('requirements.txt')

)

# pip install -r .\requirements.txt