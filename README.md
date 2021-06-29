# pra-request-tracker

## Basic Commands

### Running the app locally for development

To run the app locally, run the following command:

```bash
docker compose --file=local.yml up
```

This will spin up all the necessary services for running the application. It will also automatically restart the app when changes are made via volume mounts.

This will also capture your terminal with the logs for all the services running.

You can access the app at `localhost:8000`.

### Setting up an admin user

With the app running in a separate terminal, run the following:

```bash
docker compose --file=local.yml run django python manage.py createsuperuser
```

Follow the directions in your console to create the super user. Once you have filled out the information required and the console has output `Superuser created successfully.` you will now need to login to the web console. Once you log in the system will attempt to send you a verification email, which won't make it out of the local system. You'll need to switch to your other tab where you ran

```bash
docker compose --file=local.yml up
```

previously and look in the log stream and find the `django` service's output with the email, it will look something like this:

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

Alternatively you can run

```bash
docker compose --file=local.yml logs django
```

to view the logs for just the django service after you have successfully run the createsuperuser command.

### Creating any other type of user

Just do it through the website's UI and check for the email as described in the previous section. Follow the same process to confirm the email on the account.

### Running type checks 

```bash
docker compose --file=local.yml run django mypy pra_request_tracker
```

### Running unit tests

```bash
docker compose --file=local.yml run django coverage run -m pytest
docker compose --file=local.yml run django coverage html
open htmlcov/index.html
```

## Deploying the application

Deploy the application using the `production.yml` docker compose file.

TODO: test this out and fill in any more details if necessary.
