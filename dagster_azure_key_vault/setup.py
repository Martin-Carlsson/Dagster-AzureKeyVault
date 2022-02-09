import setuptools

setuptools.setup(
    name="dagster_azure_key_vault",
    packages=setuptools.find_packages(exclude=["dagster_azure_key_vault_tests"]),
    install_requires=[
        "dagster",
        "dagit",
        "pytest",
    ],
)
