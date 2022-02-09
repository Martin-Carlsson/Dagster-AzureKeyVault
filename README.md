# Dagster 🪢 Azure Key Vault

This repo is an examble of how to use Azure Key Vault as a Dagster [resource](https://docs.dagster.io/concepts/resources).

I am open sourcing this both to get feedback and learn ... and to save you for a lot of frustration (this took waaay to long for me to figure out)

If you have any questions, feedback, bugs, or improvements, create an issue - or contact me on the [Dagster Slack](https://dagster.com/), my name is `Martin Carlsson`, or directly on `martin@imus.dk`


**And don't forget to hit the ⭐️ button**

## Setup repo on your local machine

### Download repo

[Start by forking this repo](https://github.com/Martin-Carlsson/Dagster-AzureKeyVault/fork), hit the star icon ⭐️, and download the repo locally.

### Install development environment

Use [Remote development in Containers](https://code.visualstudio.com/docs/remote/containers-tutorial) or install requirements directly `pip install -r requirements.txt`

### Run `pytest`

**Set environment variables:**

```
export AZURE_KEY_VAULT_URI=
export AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_SECRET=
export AZURE_KEY_VAULT_SERVICE_PRINCIPAL_CLIENT_ID=
export AZURE_TENANT_ID=
```

**Execute pytest:**

Just run `pytest` in the terminal.

### Run Dagit

```
cd dagster_azure_key_vault
dagit
```

**Config:**

```
ops:
  get_secret_from_azure_key_vault:
    config:
      azure_key_vault_secret_name: "ForTestingKeyVault"
resources:
  key_management:
    config:
      azure_key_vault_service_principal_client_id:
      azure_key_vault_service_principal_client_secret:
      azure_key_vault_uri:
      azure_tenant_id:
```

## Setup and connect to Azure Key Vault

### Create an Azure Key Vault

[Create a key vault using the Azure portal](https://docs.microsoft.com/en-us/azure/key-vault/general/quick-create-portal#sign-in-to-azure)

### Create a secret

**Open Key Vaults in Azure portal:**

<img width="339" alt="image" src="https://user-images.githubusercontent.com/7769335/153219204-9e615ef1-8342-4721-b894-18d19ab0a4a4.png">

**Select the Key Vault you just created:**

<img width="537" alt="image" src="https://user-images.githubusercontent.com/7769335/153219622-afb3dc6a-d063-4814-9347-567f246bb72b.png">

**Copy Vault URI:**

_You will need it when connecting to Azure Key Vault from Dagster._

<img width="1199" alt="image" src="https://user-images.githubusercontent.com/7769335/153221248-3a11ab3d-13fe-4826-bf17-02e6745e6574.png">

**Click on Secrets:**

<img width="255" alt="image" src="https://user-images.githubusercontent.com/7769335/153219788-dd0e05af-2856-4e60-824b-192f707281e1.png">

**Click on +Generate/Import:**

<img width="137" alt="image" src="https://user-images.githubusercontent.com/7769335/153219852-37df7200-d178-4b34-906f-c387180ecb40.png">

**For testing create the following secret:**

- **Name:** ForTestingKeyVault
- **Value:** TestValidated

### Create Service Principal

_We will connect to Azure Key Vault via a Service Principal._

[Register an application with Azure AD and create a service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal)

**Give the Service Principal access to Azure Key Vault:**

[Give Service Principal access to Azure Key Vault](https://www.loom.com/share/f132c5526e0b48e6862c32013876facd)

### Create a new application secret for Service Principal

[Create a new application secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#option-2-create-a-new-application-secret)

