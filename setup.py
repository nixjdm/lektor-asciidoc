from setuptools import setup

setup(
    name='lektor-asciidoc',
    version='0.1',
    author=u'A. Jesse Jiryu Davis',
    author_email='jesse@emptysquare.net',
    license='MIT',
    py_modules=['lektor_asciidoc'],
    install_requires=['Lektor'],
    tests_require=['pytest'],
    entry_points={
        'lektor.plugins': [
            'asciidoc = lektor_asciidoc:AsciiDocPlugin',
        ]
    }
)
