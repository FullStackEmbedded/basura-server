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
      (venv) % python manage.py runserver
This starts the development server for experimentation on `localhost`.
However, it won't allow any connections from external machines.
If you want to access the development server from another machine, first add the host name you want to use (e.g. `basura-server`) to the `ALLOWED_HOSTS` list in `settings.py`.
Then instruct the development server to listen on the appropriate interfaces for connections, e.g.:
    (venv) % python manage.py runserver 0.0.0.0:8000
