from setuptools import setup

setup(
    name='generate-ssm-parameters',
    version='1.0',
    description='A script for creating AWS SSM Parameters in bulk from a CSV file.',
    url='',
    author='Travers Annan',
    license='',
    py_modules=['generate_ssm_parameters'],
    install_requires=[
        'click',
        'pandas',
        'tqdm',
        'boto3',
        'botocore'
    ],
    entry_points={
        'console_scripts':
            ['generate-ssm-parameters=generate_ssm_parameters:cli']
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ]
)
