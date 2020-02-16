import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sudoku',
    version='0.0.1',
    description='play sudoku',
    long_description=long_description,
    author='Will Jenden',
    url='https://github.com/jenden/sudoku',
    packages=['sudoku'],
    test_suite='tests',
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    setup_requires=[
        'pytest-runner'
    ],
)
