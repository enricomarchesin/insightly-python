from setuptools import setup, find_packages

setup(
    name='insightly-python',
    version='2.1.0',
    description='Insightly Python SDK',
    long_description=open('README.md').read(),
    author='Insightly',
    author_email='',
    url='https://github.com/Insightly/insightly-python',
    license='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
