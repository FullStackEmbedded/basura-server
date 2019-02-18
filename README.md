# basura-server
A prototype server application for FSE 2018 - Basura Trash System 

## Installing
      % sudo apt install python3 python3-pip python3-tk
      % sudo pip3 install virtualenv
      % cd basura-server
      % virtualenv venv -p python3
      % source venv/bin/activate

## Usage
### Instance initialization
      (venv) % pip install -r requirements.txt
      (venv) % python manage.py migrate
      (venv) % python manage.py createsuperuser

### Running the server
The following command activates the development server.
It is not meant for use in production; instead, the Django app should be deployed in a full-fledged web server.

This starts the development server for experimentation on `localhost`:

    (venv) % python manage.py runserver
However, it won't allow any connections from external machines.
If you want to access the development server from another machine, first add the host name you want to use (e.g. `basura-server`) to the `ALLOWED_HOSTS` list in `settings.py`.
Then instruct the development server to listen on the appropriate interfaces for connections, e.g.:
 
    (venv) % python manage.py runserver 0.0.0.0:8000

### Browsing the database
Database can be explored and modified not only through REST API, but also using a built-in administration page, available under http://localhost:8000/admin/

## Securing the system and proper deployment
If we were to deploy the Basura Trash System in a real environment, there is a certain set of steps required for the system to work safely.
1) The system gives read/write permissions to anyone without any authentication.
This could allow a malicious user corrupting the data stored in the basura-server using the very same REST API our software is using.
In order to prevent that, the REST framework should be configured to allow read-only access to the anonymous users.
Please look into [settings.py](settings.py) at the chunk starting from `REST_FRAMEWORK` to see recommended settings.
Proper authentication management would require distribution of authentication credentials across client applications (smartphone app).
Ideally, every user should have its own account in the system and then input the login credentials.
Once the superuser account is created, normal user accounts can be added using the server admin panel.
2) Here the server is run in a self-contained debugging environment.
This is fine for the demonstration and testing purposes, but proper deployment requires setting up a "production" environment.
This would involve couple of things like: enforcing HTTPS, regenerating secret keys, disabling debug mode.

More information available under:
https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
and
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
