# Task Manager by Mohit

This is a simple Task Management web application built using Django with a Bootstrap frontend. The application allows users to create, edit, delete, and manage tasks, as well as update the task status across three stages: To Do, In Process, and Done.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Task Management**: Users can create, edit, delete tasks, and move them between different statuses (To Do, In Process, and Done).
- **Task Status Updates**: Move tasks between different stages of completion with ease.
- **Photo Upload**: Users can upload a photo for each task.
- **Responsive Design**: The app is fully responsive and styled using Bootstrap.
- **Dark Theme**: The app uses a dark theme with a modern UI.
- **Hover Effects**: Task cards have a glowing hover effect for a better user experience.
- **Navbar Hover Effect**: Mouse hover effects and icons on the navigation bar for better interaction.

## Tech Stack

- **Backend**: Django
- **Frontend**: Bootstrap 5.3
- **Database**: SQLite (default Django database)
- **CSS**: Custom styles for hover effects and glow effects on elements
- **Templates**: HTML with Django templating language

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- pip (Python package manager)

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Mohit940m/task-manager_Django.git
   cd task-manager
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. Run migrations to set up the database:

   ```bash
   python manage.py migrate

5. Create a superuser to access the admin panel (optional):

   ```bash
   python manage.py createsuperuser

6. Run the development server:

   ```bash
   python manage.py runserver

7. Open your browser and visit: http://127.0.0.1:8000/

Folder Structure

```php
project_root/
│
├── task_manager/            # Main Django project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── ...
├── tasks/                   # Main app folder
│   ├── templates/           # HTML templates
│   ├── static/              # Static files (CSS, JS, images)
│   ├── views.py             # Task-related views
│   ├── models.py            # Task model definitions
│   ├── forms.py             # Task form for creating/editing tasks
│   └── ...
├── manage.py                # Django project manager
└── README.md                # This file

