
from setuptools import setup, find_packages

setup(
    name='readcraft',
    version='0.1.6',  
    author='Tasbi Tasbi',
    author_email='ttasbi@myseneca.ca',
    description='A command-line tool to generate README.md files using the Groq API.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tasbi03/ReadCraft',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",         
        "python-dotenv>=1.0.0",      
        "toml>=0.10.2",
    ],
    entry_points={
        'console_scripts': [
            'readcraft=readcraft.readme_generator:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    extras_require={
        "dev": ["pytest", "flake8"],
    },
)
