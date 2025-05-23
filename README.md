# RestHits

Simple REST application for exposing songs library data from a hypothetical radio station.
The project is a Django framework excercise, it's not a production-ready code by any means.

# Requirements
- Python 3.6+
- Django 3.0+
- PostgreSQL 13+
- Pytest lub unittest (DRF test cases are based on unittest)

# Useful commands (Linux/macOS)
* Initialize development environment: 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
* Setup initial data:
```
python3 manage.py setup_initial_data
```
* Run tests:
```
python3 manage.py test
```
* Run test server locally:
```
python3 manage.py runserver
```

# Note
This application is set up initially on PostgreSQL instance. Make sure you have your PostgreSQL environment set up accordingly to `./resthits/settings.py` file config.