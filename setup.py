import setuptools

with open('README.md','r') as fh:
          long_description = fh.read()
          
setuptools.setup(
    name = 'tugas4',
    version = '0.0.1',
    author = 'dwi-agung',
    author_email = 'dwiagung212@gmail.com',
    description = 'simple repo for task',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = '',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3'
    ],
    install_requires = [
        'matplotlib', #==3.3.2
        'numpy',
        'pandas==1.1.4',
        'pydantic==1.6.1',
        'scikit-learn', #==0.23.2
        'seaborn==0.11.0',
    ],
    python_requires = '>=3.7'
)
          