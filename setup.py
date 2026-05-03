from setuptools import setup, find_packages

setup(
    name="reconciliation-framework",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark>=3.4.0",
        "delta-spark>=2.4.0",
        "pyyaml>=6.0",
    ],
    python_requires=">=3.8",
)
