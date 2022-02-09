"""Repo for using Azure Key Valut"""

from dagster import job  # pylint: disable=all
from dagster import Field, JobDefinition, String, op, repository
from dagster_azure_key_vault.resources.azure_key_vault import azure_key_vault


@op(
    required_resource_keys={"key_management"},
    config_schema={
        "azure_key_vault_secret_name": Field(
            String, description="The name of the Azure Key Vault secret"
        )
    },
)
def get_secret_from_azure_key_vault(context) -> String:
    """Sends a secret name and retrive a secret
    Args:
        context (dagster object): The context provides access to system information
        like op configuration, loggers, resources, and the current run id
    """
    azure_key_vault_secret_name: str = context.op_config["azure_key_vault_secret_name"]

    azure_key_vault_secret: str = context.resources.key_management.get_secret(
        azure_key_vault_secret_name
    )

    context.log.info(f"azure_key_vault_secret_name: {azure_key_vault_secret_name}")
    context.log.info(f"azure_key_vault_secret: {azure_key_vault_secret}")

    return azure_key_vault_secret


@job(resource_defs={"key_management": azure_key_vault})
def azure_key_vault_job() -> None:
    """Executes the get_secret_from_azure_key_vault op"""
    get_secret_from_azure_key_vault()  # pylint: disable=no-value-for-parameter


@repository
def azure_key_vault_repo() -> JobDefinition:
    """A repository for Azure Key Vault
    Returns:
        job: azure_key_vault_job
    """
    return [azure_key_vault_job]
