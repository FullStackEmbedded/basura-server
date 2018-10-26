# basura-server
A prototype server application for FSE 2018 - Basura Trash System 
## Installing
      % sudo apt install python3 python3-pip python3-tk
      % sudo pip3 install virtualenv
      % virtualenv venv -p python3
      % source venv/bin/activate
      (venv) % cd basura-server
## Usage
### Instance initialization
      (venv) % pip install -r requirements.txt
      (venv) % ./manage.py migrate
      (venv) % ./manage.py createsuperuser
### Running the server
      (venv) % ./manage.py runserver
