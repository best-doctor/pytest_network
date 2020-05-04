
from setuptools import setup


def get_long_description(fname) -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name='pytest-network',
    version='0.0.1',
    author='Artem Lomonosov',
    author_email='mcproger7@gmail.com',
    maintainer='Artem Lomonosov',
    maintainer_email='mcproger7@gmail.com',
    license='MIT',
    url='https://github.com/best-doctor/pytest_network',
    description='A simple plugin to disable network on socket level.',
    long_description=get_long_description(),
    py_modules=['pytest_network'],
    install_requires=['pytest>=5.3.1'],
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'pytest11': [
            'network = pytest_network',
        ],
    },
)
