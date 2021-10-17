
## Running locally
- Initialize a python virtual environment by running `python3 -m venv <envName>`
- Start the python virtual environment by running `source <envName>/bin/activate`
- Install dependencies by running `pip install -r requirements.txt`
    or `python setup.py install`
- Create a sqlite3 database and migrate table by running `python manage.py migrate`
- Run server by running `python manage.py runserver`
- to exit python virtual environment run `deactivate`

## Running locally w/Docker
- Fill up `.env`
- Run application using docker-compose by running `docker-compose up --build`

## calling api
- to generate a new api key using curl run `curl -X GET http://localhost:8000/genkey`
- to get the latest quote using curl run `curl -H 'CUSTOM-TOKEN:<token_you_generated>' http://localhost:8000/api/v1/quotes`
- to update the latest quote using curl run `curl -H 'CUSTOM-TOKEN:<token_you_generated>' -X POST http://localhost:8000/api/v1/quotes`
