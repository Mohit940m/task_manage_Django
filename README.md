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

```
# Task Management Application

## Features Overview

### Task List
The main page displays tasks in three columns:
- **To Do**: Tasks that need to be completed.
- **In Process**: Tasks currently in progress.
- **Done**: Completed tasks.

### Task Actions
- **Create Task**: Create a new task using a form.
- **Edit Task**: Edit existing tasks.
- **Delete Task**: Delete a task.
- **Change Status**: Move tasks between To Do, In Process, and Done.
- **Photo Upload**: Add an image/photo to a task.

### Authentication
- **Register**: Create a new account.
- **Login**: Log into the app to access and manage your tasks.
- **Logout**: Securely log out from the application.

### Custom CSS and JS
This project includes custom hover effects and glow effects on task cards and navigation buttons.

#### Custom Hover and Glow Effects
- **Task Cards**: Task cards will have a glowing effect when hovered over, making them stand out.
- **Navbar Buttons**: Navigation buttons (Home, Login, Logout) will change color when hovered over.

### Dark Theme
The app uses a dark theme across all pages for a modern and sleek look.

### Custom Styles
All custom styles are placed in the static/css/styles.css file.

```css
/* styles.css */

body {
    background-color: #2c2c2c;
    color: #ffffff;
}

/* Card hover effect */
.card:hover {
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
}

/* Navbar hover effect */
.navbar .btn:hover {
    background-color: #007bff;
    color: #ffffff;
}
```

# Task Management Application

## Features Overview

### Task List
The main page displays tasks in three columns:
- **To Do**: Tasks that need to be completed.
- **In Process**: Tasks currently in progress.
- **Done**: Completed tasks.

### Task Actions
- **Create Task**: Create a new task using a form.
- **Edit Task**: Edit existing tasks.
- **Delete Task**: Delete a task.
- **Change Status**: Move tasks between To Do, In Process, and Done.
- **Photo Upload**: Add an image/photo to a task.

### Authentication
- **Register**: Create a new account.
- **Login**: Log into the app to access and manage your tasks.
- **Logout**: Securely log out from the application.

### Custom CSS and JS
This project includes custom hover effects and glow effects on task cards and navigation buttons.

#### Custom Hover and Glow Effects
- **Task Cards**: Task cards will have a glowing effect when hovered over, making them stand out.
- **Navbar Buttons**: Navigation buttons (Home, Login, Logout) will change color when hovered over.

## Future Enhancements
- Add real-time updates for task changes using WebSockets.
- Implement user roles (e.g., Admin, User) with different permissions.
- Add task deadlines and reminders.
- Integrate drag-and-drop functionality for easier task management.
- Add notifications for task updates.

## License
This project is open-source and free to use. Feel free to modify and improve the code for your own use!

---
End of Document


