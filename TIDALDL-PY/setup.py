from setuptools import setup, find_packages

setup(
    name = 'tidal-dl',
    version='1.0.0.3',
    license = "MIT Licence",
    description = "Tidal Music Download.",

    author = 'YaronH',
    author_email = "yaronhuang@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires=[],

    entry_points={'console_scripts': [
        'tidal-dl = tidal_dl:main', ]}
)