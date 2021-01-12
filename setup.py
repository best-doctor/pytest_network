
from setuptools import setup


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


package_name = 'pytest_network'

setup(
    name=package_name,
    version='0.0.2',
    author='Artem Lomonosov',
    author_email='mcproger7@gmail.com',
    maintainer='Artem Lomonosov',
    maintainer_email='mcproger7@gmail.com',
    license='MIT',
    url='https://github.com/best-doctor/pytest_network',
    description='A simple plugin to disable network on socket level.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    py_modules=[package_name],
    install_requires=['pytest>=5.3.1'],
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'pytest11': [
            'network = pytest_network',
        ],
    },
)
