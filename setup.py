from setuptools import find_packages, setup
from typing import List

CONSTANT = "-e ."

# This function will return a list of requirement libraries
def get_requirements(filename: str)->List[str]:
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        result = [string.replace("\n", "") for string in requirements]

        if CONSTANT in result:
            result.remove(CONSTANT)

    return result

setup (
    name = 'student performance',
    version = '0.0.1',
    author = 'Ganesh Venu',
    email = 'ganeshvenu705@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)