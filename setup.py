from setuptools import find_packages, setup

setup(
    name="dagster_dlt_sf_blob_storage",
    packages=find_packages(exclude=["dagster_dlt_sf_blob_storage_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-embedded-elt",
        "simple-salesforce>=1.12.4",
        "dlt[filesystem]>=0.3.5",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest", "ruff"]},
)
