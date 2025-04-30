NGO Website Project
===================

1. Project Description
----------------------
This is a Django 5.2 based web application for an NGO. The website provides information about the NGO's work, projects, media, blog, and allows users to volunteer and donate online. It integrates Razorpay for secure payment processing.

2. Features
-----------
- Informational pages: Home, About, Work, Projects, Media, Blog
- Volunteer signup form with file upload support for volunteer photos/documents
- Volunteer list page to view submitted applications
- Donation page with Razorpay payment gateway integration
- CSV report downloads for various programs (Women Health, Skill Development, Community Health)
- Uses SQLite database for data storage
- Static and media file handling configured

3. Prerequisites
----------------
- Python 3.x
- Django 5.2
- Razorpay account and API keys (test keys included in settings)
- Basic knowledge of Django and Python

4. Installation
---------------
1. Clone the repository
2. Create and activate a virtual environment (recommended)
3. Install dependencies:
   ```
   pip install django razorpay
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. (Optional) Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

5. Running the Project
----------------------
Start the development server with:
```
python manage.py runserver
```
Access the website at `http://127.0.0.1:8000/`

6. Folder Structure
-------------------
- NGOpro/: Django project settings and configuration
- NGOapp/: Main application containing models, views, forms, and URLs
- template/: HTML templates for various pages
- static/: Static files like images, CSS, and JavaScript
- media/: Uploaded media files (e.g., volunteer documents)
- manage.py: Django management script
- db.sqlite3: SQLite database file

7. Usage
--------
- Visit the home page to navigate the site
- Use the Volunteer Signup page (`/volunteer/`) to submit volunteer applications
- View submitted volunteers on the Volunteer List page (`/volunteers/`)
- Make donations via the Donate page (`/donate/`) using Razorpay payment gateway
- Download CSV reports for Women Health, Skill Development, and Community Health programs via respective links

8. Contact / Support
--------------------
For support or inquiries, please contact the project maintainer.

---
This README provides an overview and instructions to set up and run the NGO website project.
