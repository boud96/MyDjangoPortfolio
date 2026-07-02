# My Django Portfolio

A dynamic, data-driven personal portfolio website built with Django. This project transforms a static HTML template into a fully functional CMS, allowing you to manage your work experience, education, skills, and projects directly through the Django Admin interface.

Based on the [Creative CV](https://templateflip.com/templates/creative-cv/) template by TemplateFlip.

## Features

*   **Dynamic Content Management**: Easily add, edit, or remove:
    *   **Personal Information**: Name, contact details, social media links.
    *   **Work Experience**: Job titles, companies, dates, and descriptions.
    *   **Education**: Degrees, schools, and dates.
    *   **Skills**: categorized technical skills with progress bars.
    *   **Projects/Portfolio**: Showcasing web development projects or photography with images and descriptions.
    *   **CV Upload**: Upload a PDF version of your CV for visitors to download.
*   **Multi-language Support**: Built-in support for English and Czech (or other languages) using `django-modeltranslation`.
*   **Rich Text Editing**: Uses Markdown for job and project descriptions.
*   **Optional Cloud Storage**: Can use AWS S3 for static and media file storage.
*   **Responsive Design**: Fully responsive layout based on Bootstrap.

## Tech Stack

*   **Backend**: Python 3, Django 5
*   **Database**: PostgreSQL
*   **Frontend**: HTML5, CSS3, Bootstrap 4, jQuery
*   **Storage**: Local filesystem for development, optional AWS S3 via `django-storages` and `boto3`
*   **Utilities**: `django-environ` for configuration, `django-modeltranslation` for i18n.

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

*   Python 3.10+
*   pip
*   virtualenv (recommended)

### Installation

1.  **Clone the repository**
    ```sh
    git clone https://github.com/your_username/MyDjangoPortfolio.git
    cd MyDjangoPortfolio
    ```

2.  **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the repository root or use the provided example:
    ```sh
    cp .env.example .env
    ```
    
    The example file is set up for local development with SQLite and local file storage:
    ```ini
    DJANGO_DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
    USE_S3=False
    ```

    For production, use real environment values and do not use the local placeholder `SECRET_KEY`:
    ```ini
    SECRET_KEY=your_real_secret_key
    DJANGO_DEBUG=False
    ALLOWED_HOSTS=example.com,www.example.com
    CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
    DATABASE_URL=postgres://user:password@host:5432/dbname

    # Enable only when this deployment should use AWS S3.
    USE_S3=True
    AWS_ACCESS_KEY_ID=your_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_STORAGE_BUCKET_NAME=your_bucket_name

    # Enable after HTTPS is correctly configured.
    SECURE_SSL_REDIRECT=True
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True
    SECURE_HSTS_SECONDS=0
    ```

    If the app runs behind a proxy that terminates HTTPS, such as Heroku or many load balancers, set `USE_X_FORWARDED_PROTO=True` after confirming the proxy controls the `X-Forwarded-Proto` header.

5.  **Apply Database Migrations**
    ```sh
    python manage.py migrate
    ```

6.  **Create a Superuser**
    Access the admin panel to manage your portfolio content.
    ```sh
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```sh
    python manage.py runserver
    ```

8.  **Visit the App**
    *   Portfolio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *   Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Deployment Checks

Before deploying, run:

```sh
python manage.py check
python manage.py check --deploy
```

The settings intentionally fail startup when `DJANGO_DEBUG=False` is combined with unsafe values such as a placeholder `SECRET_KEY`, missing `DATABASE_URL`, empty `ALLOWED_HOSTS`, wildcard hosts, or incomplete S3 credentials when `USE_S3=True`.

## Usage

1.  Log in to the **Admin Panel**.
2.  Navigate to the **Core** app section.
3.  Add a **Personal Info** record (mark it as `Active`).
4.  Populate **Jobs**, **Educations**, **Skills**, and **Projects**.
5.  The main page will automatically reflect the data entered.

## Project Structure

    MyDjangoPortfolio/
    ├── __cv_template/       # Original HTML template assets (reference)
    ├── core/                # Main application app
    │   ├── migrations/      # Database migrations
    │   ├── static/          # Static assets (CSS, JS, Images)
    │   ├── templates/       # Django HTML templates (index.html)
    │   ├── admin.py         # Admin panel configuration
    │   ├── models.py        # Database models (Job, Skill, Project, etc.)
    │   ├── translation.py   # Translation rules
    │   ├── urls.py          # App-level URL routing
    │   └── views.py         # Logic for rendering views
    ├── locale/              # Translation files (e.g., cs/LC_MESSAGES)
    ├── my_django_portfolio/ # Project configuration folder
    │   ├── settings.py      # Main Django settings
    │   ├── storage_backends.py # Custom storage configurations (S3)
    │   └── urls.py          # Project-level URL routing
    ├── .env.example         # Example environment variables
    ├── manage.py            # Django management script
    ├── Procfile             # Deployment commands
    └── requirements.txt     # Python dependencies

## Credits

*   **Design Template**: [Creative CV](https://templateflip.com/templates/creative-cv/) by TemplateFlip.
*   **Icons**: [Font Awesome](https://fontawesome.com/).

## License

The code is available under the MIT License. The design template "Creative CV" is subject to its own license terms (Free for personal/commercial use with attribution). See `LICENSE-free.txt` for template details.
