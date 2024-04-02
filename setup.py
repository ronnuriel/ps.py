from setuptools import setup, find_packages

setup(
    name='Process Manager',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'click',
        'python_toolbox',  # Assuming 'caching' comes from here
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'newps=mypackage.ps:ps',  # Change the command name to 'newps'
        ],
    },
)
