from setuptools import setup, find_packages

setup(
    name="toy_robot_package",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'toy_robot=toy_robot.__main__:main',
        ],
    }
)