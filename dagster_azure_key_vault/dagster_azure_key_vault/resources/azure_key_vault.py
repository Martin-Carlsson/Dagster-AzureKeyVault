"""Resource for Azure Key Vault"""

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dagster import Field, String, resource


class AzureKeyVault:
    """Class that manages Azure Key Vault"""

    def __init__(
        self,
        azure_key_vault_uri: str,
        azure_tenant_id: str,
        azure_key_vault_service_principal_client_id: str,
        azure_key_vault_service_principal_client_secret: str,
    ) -> None:
        self.__vault_url = azure_key_vault_uri

        self.__credential = ClientSecretCredential(
            tenant_id=azure_tenant_id,
            client_id=azure_key_vault_service_principal_client_id,
            client_secret=azure_key_vault_service_principal_client_secret,
        )

        self.__client = SecretClient(
            vault_url=self.__vault_url, credential=self.__credential
        )

    def __str__(self):
        return self.__class__.__name__

    def get_secret(self, secret_name: str) -> str:
        """Connects to Azure Key Vault and returns a secret
        Args:
            secret_name (str): The secret name
        Returns:
            str: The secret
        """
        return self.__client.get_secret(secret_name).value

@resource(
    config_schema={
        "azure_key_vault_uri": Field(
            String, description="Vault URI | https://<vault_name>.vault.azure.net/"
        ),
        "azure_tenant_id": Field(
            String, description="Tenant ID | 11111111-1111-1111-1111-111111111111"
        ),
        "azure_key_vault_service_principal_client_id": Field(
            String,
            description="Service Principal Application (client) ID |"
            " 11111111-1111-1111-1111-111111111111",
        ),
        "azure_key_vault_service_principal_client_secret": Field(
            String,
            description="Service Principal client secret | AAAA~aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ),
    }
)
def azure_key_vault(context):
    """A resource that returns AzureKeyVault
    Args:
        context (resource_config): login credentials for Azure Key Vault
    Returns:
        class: AzureKeyVault
    """
    return AzureKeyVault(
        azure_key_vault_uri=context.resource_config["azure_key_vault_uri"],
        azure_tenant_id=context.resource_config["azure_tenant_id"],
        azure_key_vault_service_principal_client_id=context.resource_config[
            "azure_key_vault_service_principal_client_id"
        ],
        azure_key_vault_service_principal_client_secret=context.resource_config[
            "azure_key_vault_service_principal_client_secret"
        ],
    )
