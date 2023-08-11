from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
with open("requirements.txt" , "r", encoding='utf-8') as fh:
    requirements = fh.read()

setup(
    name='tool', 
    version = '0.0.1', 
    author = 'Eseban Barrios',
    author_email = 'esteban.barrios95@gmail.com', 
    description = 'accessing tools for quick access', 
    py_modules = ['tool', 'Eb_Main'], 
    packages = find_packages(), 
    install_requires = [requirements], 
    python_requires = '=3.11.3',
    classifiers=
        ['Programming Language :: Python :: 3.11.3', 
         "Operating System :: OS Independent",], 
    entry_points='''
        [console_scripts]
        ebTool=tool:cli
    '''
)