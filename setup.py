from setuptools import setup, find_packages

# Function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

setup(
    name='instant_nsr',
    version='0.1.0',
    description='Neural Surface reconstruction based on Instant-NGP.',
    url='https://github.com/Mirage-AI/era3d-instant-nsr-pl',  # Update with your project's URL
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
)