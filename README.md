# Dagster Azure Key Vault

## Setup and connect to Azure Key Vault

### Create an Azure Key Vault

[Create a key vault using the Azure portal](https://docs.microsoft.com/en-us/azure/key-vault/general/quick-create-portal#sign-in-to-azure)

### Create a secret

**Open Key Vaults in Azure portal:**

<img width="339" alt="image" src="https://user-images.githubusercontent.com/7769335/153219204-9e615ef1-8342-4721-b894-18d19ab0a4a4.png">

**Select the Key Vault you just created:**

<img width="537" alt="image" src="https://user-images.githubusercontent.com/7769335/153219622-afb3dc6a-d063-4814-9347-567f246bb72b.png">

**Click on Secrets:**

<img width="255" alt="image" src="https://user-images.githubusercontent.com/7769335/153219788-dd0e05af-2856-4e60-824b-192f707281e1.png">

**Click on +Generate/Import:**

<img width="137" alt="image" src="https://user-images.githubusercontent.com/7769335/153219852-37df7200-d178-4b34-906f-c387180ecb40.png">


**For testing create the following secret:**

- **Name:** ForTestingKeyVault
- **Value:** TestValidated
