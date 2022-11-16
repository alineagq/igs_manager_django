# IGS Employee Manager

## Introduction

This project was developed according to rules established in [test_django](https://github.com/igs-software/teste_django) created by [IGS-Software](https://www.igs-software.com.br).

### Environment
- Python (3.10)
- Django
- Django Rest Framework
- Django Rest Swagger

### Database Diagram

![Database Diagram](/database.png "Database Diagram")

## How to develop

Run the following commands below:

```sh
git clone git@github.com:alineagq/igs_manager_django.git
cd igs_manager_django
```

> You'll be able to run your environment through Python Virtualenv or Dockerfile.

### Using Python Virtualenv

```sh
python3 -m venv .venv
source .venv/bin/activate #or ..venv\Scripts\activate (windows)
pip install -r requirements.txt
python igsmanager/manage.py makemigrations
python igsmanager/manage.py migrate
python igsmanager/manage.py createsuperuser
python igsmanager/manage.py runserver 8000
```
### Using Docker

```sh
docker-compose up -d
docker-compose exec web python igsmanager/manage.py makemigrations
docker-compose exec web python igsmanager/manage.py migrate
docker-compose exec web python igsmanager/manage.py createsuperuser
```

> If you use Python Virtualenv please change variable DATABASE HOST from ``` db``` to ``` localhost``` at ``` settings.py```

## API Documentation

- ``` http://localhost:8000/admin/ ```
- ``` http://localhost:8000/doc ```
- ``` http://localhost:8000/employee/ ```
- ``` http://localhost:8000/department/ ```
- ``` http://localhost:8000/employee/ ```
- ``` http://localhost:8000/department/<int:pk>/ ```
- ``` http://localhost:8000/employee/<int:pk>/ ```

> The API Documentation can be access through ``` http://localhost:8000/doc ``` 

## API example

### Request
```sh
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

### Body Response

```json 
[
  {
    "id": 2,
    "name": "Aline",
    "email": "alinequeirozagq@gmail.com",
    "department": "RH"
  },
  {
    "id": 3,
    "name": "Cejrie",
    "email": "cejrie@gmail.com",
    "department": "Tech"
  }
]
```
