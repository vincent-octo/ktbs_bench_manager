from setuptools import setup, find_packages


setup(
    name="ktbs_bench_manager",
    version="0.0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['rdflib==4.1.1',
                      'sutils'],

    dependency_links=['https://github.com/vincent-octo/sutils/tarball/master#egg=sutils',
                      'https://github.com/RDFLib/rdflib-sqlalchemy/tarball/master#egg=rdflib_sqlachemy'],

    extras_require={'tests': ['pytest', 'rdflib'],
                    'sql': ['rdflib-sqlachemy', 'psycopg2']},

    # metadata for upload to PyPI
    author="Vincent",
    author_email="vincent-octo@users.noreply.github.com",
    description="kTBS bench manager",
    license="MIT",
    url="https://github.com/vincent-octo/ktbs_bench_manager",  # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
