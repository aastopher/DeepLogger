import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EZ_Logger",
    version="0.0.1",
    author="Aaron Stopher",
    description="Easily configure, simple granular loggers for all your modules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aastopher/EZLogger",
    project_urls={
        "Bug Tracker": "https://github.com/aastopher/EZLogger/issues",
    },
    keywords=['python', 'logger', 'CLI','easy logging','easy logger'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
