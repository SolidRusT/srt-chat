from setuptools import setup, find_packages

setup(
    name='cli-client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'srt-core',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'cli-client=cli_client.main:cli',
        ],
    },
    author='Suparious',
    author_email='suparious@solidrust.net',
    description='A CLI client for srt-core',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SolidRusT/srt-chat',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
