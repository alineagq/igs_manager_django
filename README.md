# IGS Employee Manager

This project was developed according to rules established in [test_django](https://github.com/igs-software/teste_django) created by [IGS-Software](https://www.igs-software.com.br).

## How to develop

Run the following commands below:

    git clone git@github.com:alineagq/igs_manager_django.git
    cd igs_manager_django

> You'll be able to run your environment through Python Virtualenv or Dockerfile.

### Using Python Virtualenv

    python3 -m venv .venv
    source .venv/bin/activate #or ..venv\Scripts\activate (windows)
     pip install -r requirements.txt
     python manage.py makemigrations
     python manage.py migrate
     python manage.py createsuperuser
     python manage.py runserver 8000

### Using Docker

    docker-compose up -d
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser

