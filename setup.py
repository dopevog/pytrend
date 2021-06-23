# Copyright 2021-Present Vedant Kothari
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='pytrend',
    version='0.3',
    packages=find_packages(),
    url='https://github.com/dopevog/pytrend',
    license='MIT License',
    author='Vedant Kothari',
    author_email='dopevog@gmail.com',
    description='Trend detection on stock time series data',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename="requirements.txt"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=', '.join([
        "trend detection", "stock analysis", "stock", "trend analysis",
        "stock trends", "financial trends"
    ]),
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/dopevog/pytrend/issues',
        'Source': 'https://github.com/dopevog/pytrend',
    },
)
