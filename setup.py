from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='generate-ssm-parameters',
    version='0.1.2',
    description='A script for creating AWS SSM Parameters in bulk from a CSV file.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/travers-co/generate-ssm-parameters',
    author='Travers Annan',
    author_email="travers@curiousorbit.com",
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['generate_ssm_parameters'],
    install_requires=[
        "boto3 ~= 1.26.80",
        "botocore ~= 1.29.80",
        "click ~= 8.1.3",
        "pandas ~= 1.5.3",
        "tqdm ~= 4.64.1",
    ],
    entry_points={
        'console_scripts':
            ['generate-ssm-parameters=generate_ssm_parameters:cli']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
