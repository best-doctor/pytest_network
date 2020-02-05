import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-network',
    version='0.0.1',
    author='Artem Lomonosov',
    author_email='mcproger7@gmail.com',
    maintainer='Artem Lomonosov',
    maintainer_email='mcproger7@gmail.com',
    license='MIT',
    url='https://github.com/best-doctor/pytest-network',
    description='A simple plugin to disable network on socket level.',
    long_description=read('README.md'),
    py_modules=['pytest_network'],
    install_requires=['pytest>=5.3.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'network = pytest_network',
        ],
    },
)
