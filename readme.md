# Local setup


## Backend setup
* Install python (version>3.9)

Create virtualenv using 
* python -m venv venv

Install dependencies using 
* pip install -r requirements.txt

Activate the virtualenv using

In Linux :-
* ./venv/bin/activate

In Windows :-
* ./venv/scripts/activate

Create the .env file in the root directory and configure the .env file as per your database configuration.
See the file [here](.env.example) file


Start the local server using 
* uvicorn app:app --reload

## Frontend setup

* cd frontend
* Install node and npm
* node version = 20.1.1
* npm version = 8.3.1
* npm install
* npm start