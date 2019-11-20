# RFID Security System CRUD

## Creating IAM user

Credentials are needed to manage stuff on AWS. Amazon, strongly discourages the usage of the root user credentials for security reasons, so a new user needs to be created with the **Identity Access Management** (IAM) service. Instructions to enable IAM and create a new user can [be found here](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

- In the **access type**, I chose `Programmatic access` which enables an **access key ID** and **secret access key**.

- In **permissions**, I clicked on *Attach existing policies directly*, then searched and chose `AmazonDynamoDBFullAaccess` so this user can only access dynamoDB.

- I skipped the **tags** section.

Once reviewed, a new user will be created. An **access key ID** and a **secret access key ID** will be generated, the **secret key will only be shown this one time**, so write it down and keep it safe and secret!

## Environment variables

The AWS SDK, `boto3`, needs some environment variables to run properly, so these should be set as following:

```bash
AWS_ACCESS_KEY_ID=[your-access-id]
AWS_SECRET_ACCESS_KEY=[your-secret-key]
AWS_DEFAULT_REGION=[your-closest-region]
```

In `AWS_DEFAULT_REGION`, I chose the value `us-east-2`.

Also, in order to not reveal the names of the dynamoDB tables used, l also set those up as environment variables:

```bash
USERS_TABLE_NAME=[your-users-table]
MACHINES_TABLE_NAME=[your-machines-table]
LOGS_TABLE_NAME=[your-logs-table]
```