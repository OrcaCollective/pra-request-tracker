# pra-request-tracker

## Basic Commands

### Install

First, initialize the repository's local environment. To do this you probably want to create a virtual environment first:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then to install dependencies and initalize tooling:

```bash
make install
```

### Running the app locally for development

To run the app locally, run the following command:

```bash
make up
```

This will spin up all the necessary services for running the application. It will also automatically restart the app when changes are made via volume mounts.

To see the logs:

```bash
make logs
```

You can access the app at `localhost:8000`.

### Setting up an admin user

With the app running in a separate terminal, run the following:

```bash
make createsuperuser
```

Follow the directions in your console to create the super user. Once you have filled out the information required and the console has output `Superuser created successfully.` you will now need to login to the web console. Once you log in the system will attempt to send you a verification email, which won't make it out of the local system. You'll need to run `make logs` to see the logs.

In the log stream, find the `django` service's output with the email, it will look something like this:

```
django      | Content-Type: text/plain; charset="utf-8"
django      | MIME-Version: 1.0
django      | Content-Transfer-Encoding: 7bit
django      | Subject: [PRA Request Tracker] Please Confirm Your E-mail Address
django      | From: webmaster@localhost
django      | To: admin@example.com
django      | Date: Tue, 29 Jun 2021 17:35:16 -0000
django      | Message-ID: <162498811644.12.3635293736420768765@2190a548b587>
django      |
django      | Hello from PRA Request Tracker!
django      |
django      | You're receiving this e-mail because user admin has given your e-mail address to register an account on twitter.com/TechBlocSEA.
django      |
django      | To confirm this is correct, go to http://localhost:8000/accounts/confirm-email/MQ:1lyHdk:Td8HDxKa67J4uKIZdVlx6YsisvdjMS8Psjz95e94Yuw/
django      |
django      | Thank you for using PRA Request Tracker!
django      | twitter.com/TechBlocSEA
django      | ------------------------------------------------------------------------------
```

Copy the link into your browser to confirm the account. Then you'll be able to log into the account.

Access the django admin as usual by navigating to `localhost:8000/admin`.

### Creating any other type of user

Just do it through the website's UI and check for the email as described in the previous section. Follow the same process to confirm the email on the account.

### Running type checks

```bash
make types
```

### Running unit tests

```bash
make test
```

To view test coverage in your browser:

```bash
make coverage
```

### Linting

To lint all the files:

```bash
make lint
```

### Migrations

To create migrations based on model changes:

```bash
make makemigrations
```

Then to migrate your local environment:

```bash
make migrate
```

### If your local environment becomes unrecoverable

```bash
make freshstart
```

## Deploying the application

Deploy the application using the `production.yml` docker compose file.

TODO: test this out and fill in any more details if necessary.
