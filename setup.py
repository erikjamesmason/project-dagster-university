from setuptools import find_packages, setup

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=[
        "dagster==1.6.*",
        "dagster-cloud",
        "dagster-duckdb",
        "dagster-dbt",
        "dbt-duckdb",
        "geopandas",
        "kaleido",
        "pandas",
        "plotly",
        "shapely",
        "smart_open[s3]",
        "s3fs",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
