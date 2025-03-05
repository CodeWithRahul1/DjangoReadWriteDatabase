Django Dual Database (Read & Write) Setup

Overview

This Django project implements a dual-database setup where:

Write operations (User & Product Registration) are performed on write_db.

Read operations (User Authentication & Product Listing) are performed from read_db.

Data is replicated from write_db to read_db using Django signals.

Installation & Setup

1. Clone the Repository

git clone <repo_url>
cd <project_name>

2. Create & Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

Database Configuration

Modify settings.py to define multiple databases:

DATABASES = {
    'default': {},
    'write_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'write_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'read_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'read_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Running Migrations

python manage.py makemigrations users
python manage.py migrate --database=write_db
python manage.py migrate --database=read_db

API Endpoints

User Endpoints

Register a User (Writes to write_db)POST /api/auth/register/

Login a User (Reads from read_db)POST /api/auth/login/

Product Endpoints

Register a Product (Writes to write_db)POST /api/auth/product-register/

List Products (Reads from read_db)GET /api/auth/products/

Django Signals for Data Replication

We use Django signals to replicate user & product data from write_db to read_db.
Located in users/signals.py, this ensures that:

Newly registered users are copied to read_db.

Newly added products are copied to read_db.

Running the Server

python manage.py runserver

Author

Rahul

