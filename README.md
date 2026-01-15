# Modern E-Commerce API (Django Rest Framework)

## A modern, scalable E-commerce REST API built with Django Rest Framework (DRF) as a team learning project.
**This project focuses on best practices in:**
- Django Rest Framework
- Git & GitHub collaboration
- Clean architecture
- PostgreSQL integration

**Real-world e-commerce features**
- Backend: Django, Django Rest Framework
- Database: PostgreSQL
- Authentication: JWT
- Environment Management
- Version Control: Git & GitHub

```
Project Structure
collaborative_ecommerce/
│
├── accounts/          # Authentication & user profiles
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── product/           # Products & categories
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── cart/              # Shopping cart logic
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── payment/           # Orders payments (future implementation)
├── static/
│
├── collaborative_ecommerce/  # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── .env.example       # Environment variables template
├── .gitignore
├── requirements.txt
└── manage.py
 ```

## Team Feature Assignment
### _Accounts Module_
1. Ephaste – User registration (buyer & seller)
2. Furaha – Login with jwt
3. Elyse – Buyer profile update
4. Immaculle – Seller profile update

### _Product Module_
1.  Faustin – Product category (Model + CRUD)
2.  Cedric – Create product
3.  Tresor – Update product
4.  Josue – Delete product
5.  Honore – List all products
6.  Theogene – Product detail view
7.  Arnold – Search products
8.  Frank – Filter by category & price

### _Cart & Orders_
1. Michelline – Add product to cart
2. Gad – View cart & update quantity
3. Joan – Checkout page
4. Sandrine – Place order & save order data
5. Joseph – Order history (buyer orders list)

## **Git Workflow Rules**
- Pull from main
- Create a feature branch with the pattern
> feature/"feature-name" 
- Work only on your feature
- Commit frequently with clear messages
- Open a Pull Request (PR) to main
- Wait for review before merge
- **No direct push to main !!!** 

**Typical work/push example**
```
git checkout main
git pull origin main
git checkout -b feature/product-create
# work... then when it comes to push 
git add .
git commit -m "Add product creation endpoint"
git push origin feature/product-create
```

## **Local Development Setup**
1. _Clone the project_
```
git clone <repository-url> 
cd collaborative_ecommerce
```
2. _Create virtual environment_
```
python -m venv venv 
source venv/bin/activate   # Linux/Mac 
venv\Scripts\activate      # Windows 
```
3️. _Install dependencies_
```
pip install -r requirements.txt
```

4. _PostgreSQL Configuration (IMPORTANT)_
**Create a local PostgreSQL database**
```
CREATE DATABASE ecommerce_db;
```

**Update .env**
_Copy .env.example → .env_
```
DEV_DB_NAME=db_name
DEV_DB_USER=db_user_name
DEV_DB_PASSWORD=password_example
```
_Update settings.py_

Replace SQLite with PostgreSQL
```
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':env("DEV_DB_NAME"),
        'USER':env("DEV_DB_USER"),
        'PASSWORD': env("DEV_DB_PASSWORD"),
        'HOST':'localhost',
        'PORT':5432
    }
}
```
_Run the Project_
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Feature Implementation Guidelines

1. Use DRF serializers
2. Use Class-based views APIView or ViewSets,etc
3. Validate inputs properly
4. Return meaningful HTTP status codes if applied
5. Keep logic inside services/models where possible

## Common Mistakes & Solutions
- Forgot to pull latest main
Always run:
> git pull origin main
- Pushed to wrong branch
> Reset and move commits to correct feature branch
- Migration conflicts
Run:
```
python manage.py makemigrations app_name
python manage.py migrate
```
- PostgreSQL connection error
Check:
> Database exists
> Credentials in .env
> PostgreSQL service is running

- Import errors
Ensure:
> App is added in INSTALLED_APPS
> Correct relative imports

### Final Notes

- Keep your feature small & focused
- Communicate with teammates
- Ask before changing shared files
- Write clean, readable code

Happy coding \
**_Django Cohort 2_**
