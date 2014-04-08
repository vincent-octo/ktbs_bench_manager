from setuptools import setup, find_packages


setup(
    name="ktbs_bench_manager",
    version="0.0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['rdflib==4.1.1',
                      'sutils'],

    dependency_links=['https://github.com/vincent-octo/sutils/tarball/master#egg=sutils'],

    extras_require={'tests': ['pytest']},

    # metadata for upload to PyPI
    author="Vincent",
    author_email="vincent-octo@users.noreply.github.com",
    description="kTBS bench manager",
    license="MIT",
    url="https://github.com/vincent-octo/ktbs_bench_manager",  # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
