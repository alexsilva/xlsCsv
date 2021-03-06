from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.read().splitlines()
    setup(
        name='xlscsv',
        version='1.0',
        packages=[''],
        url='https://github.com/alexsilva/xlsCsv',
        license='MIT',
        author='alex',
        author_email='',
        description='Write similar xlsx files to csv format.',
        install_requires=requires
    )
