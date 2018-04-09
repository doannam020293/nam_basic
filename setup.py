from setuptools import setup

setup(
    name='nam_basic',
    version='0.0.1',
    # description='a tool for helping people with a FACT night shift',
    # url='https://github.com/fact-project/shifthelper',
    # author='Dominik Neise, Maximilian Noethe, Sebastian Mueller',
    # author_email='neised@phys.ethz.ch',
    # license='MIT',
    # packages=[
    #     'shifthelper',
    #     'shifthelper.tools',
    #     'shifthelper.db_cloner',
    # ],
    # package_data={
    #     'shifthelper.db_cloner': ['logging.conf'],
    # },
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest>=3.0.0', 'freezegun'],
    install_requires=[
        'pandas',
        'numpy',
        'pymongo',
        'unidecode'
    ],
    # entry_points={'console_scripts': [
    #     'shifthelper = shifthelper.__main__:main',
    #     'shifthelper_db_cloner = shifthelper.db_cloner.__main__:main',
    # ]},
    # zip_safe=False,
)