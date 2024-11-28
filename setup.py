from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the given file path.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters more cleanly
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="ML Project",
    version='0.0.1',
    author="Salah0Uddin",
    author_email="salahforkrh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
