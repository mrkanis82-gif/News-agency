# News Agency
News Agency is a web application for managing a news agency. Users can create editors, newspapers, and topics to organize content.

## Functionality
- Users can create, update, and delete editors, newspapers, and topics
- Responsive sliding sidebar navigation (Bootstrap 5 Offcanvas)

## Authentication
- Custom login page (no admin access required)
- User registration only via terminal (`createsuperuser`) or by existing users

## Technology
- Django
- Bootstrap 5
- SQLite


## How to Run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a superuser: `python manage.py createsuperuser`
4. Run the server: `python manage.py runserver`
5. login using data of your superuser
6. You have access to all Functionality
