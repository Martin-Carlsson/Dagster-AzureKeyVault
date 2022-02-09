"""Test Azure Key Vault"""
import os

from dagster_azure_key_vault.repositories.azure_key_vault_repo import (
    azure_key_vault_job,
)


def test_azure_key_vault():
    """
    Testing Azure Key Vault

    Set Environment Variables
        export AZURE_KEY_VAULT_URI=https://<vault_name>.vault.azure.net/
        export AZURE_TENANT_ID=11111111-1111-1111-1111-111111111111
        export AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_ID=11111111-1111-1111-1111-111111111111
        export AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_SECRET=AAAA~aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """

    azure_key_vault_uri = os.environ.get("AZURE_KEY_VAULT_URI")
    azure_tenant_id = os.environ.get("AZURE_TENANT_ID")
    azure_key_vault_service_principal_client_id = os.environ.get(
        "AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_ID"
    )
    azure_key_vault_service_principal_client_secret = os.environ.get(
        "AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_SECRET"
    )

    run_config = {
        "resources": {
            "key_management": {
                "config": {
                    "azure_key_vault_uri": azure_key_vault_uri,
                    "azure_tenant_id": azure_tenant_id,
                    "azure_key_vault_service_principal_client_id": azure_key_vault_service_principal_client_id,
                    "azure_key_vault_service_principal_client_secret": azure_key_vault_service_principal_client_secret,
                }
            }
        },
        "ops": {
            "get_secret_from_azure_key_vault": {
                "config": {"azure_key_vault_secret_name": "ForTestingKeyVault"}
            }
        },
    }

    result = azure_key_vault_job.execute_in_process(run_config=run_config)
    assert result.success

    assert result.output_for_node("get_secret_from_azure_key_vault") == "TestValidated"
