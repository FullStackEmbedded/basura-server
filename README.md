# basura-server
A prototype server application for FSE 2018 - Basura Trash System 
## Installing
      % sudo apt install python3 python3-pip python3-tk
      % sudo pip install virtualenv
      % virtualenv venv
      % source venv/bin/activate
      (venv) % pip install -r basura-server/requirements.txt
## Usage
### Instance initialization
      (venv) % cd basura-server
      (venv) % ./manage.py migrate
      (venv) % ./manage.py createsuperuser
### Running the server
      (venv) % ./manage.py runserver