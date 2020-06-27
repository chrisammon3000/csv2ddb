# from setuptools import setup

# setup(
#     name='csv2ddb',
#     version='0.1',
#     py_modules=['app'],
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         app=app:cli
#     ''',

# )

from setuptools import setup

setup(
    name='csv2ddb',
    version='0.1',
    py_modules=['csv2ddb'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        csv2ddb=csv2ddb:cli
    ''',
)