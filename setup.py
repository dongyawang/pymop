from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(
    name="pyop",
    version="0.1",
    author="Julian Blank",
    author_email="blankjul@egr.msu.edu",
    description="Optimization Test Problems",
    long_description=long_description,
    url="https://github.com/julesy89/pyop",
    license='MIT',
    keywords="optimization",
    packages=['pyop', 'pyop/problems'],
    install_requires=['numpy']
)
