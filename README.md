# Django Health

## 🏥 Overview

Django Health is a sophisticated healthcare management system designed to streamline patient care and administrative operations in medical facilities. Built upon the robust Django framework and its powerful REST API capabilities, this platform creates a secure, efficient environment for managing the complex relationships between patients, doctors, and administrative staff.

The system employs a role-based architecture that carefully separates concerns while maintaining cohesive data flow throughout the application. With its PostgreSQL foundation, Django Health ensures data integrity and scalability to support growing healthcare organizations.

## ✨ Key Features

### User Management & Security

- **Custom User Model**: Uses email as the primary identifier instead of traditional usernames, providing a more intuitive authentication experience while supporting multiple role designations (patient, doctor, admin) through attribute flags.

- **Role-Based Access Control**: Implements comprehensive permission systems that ensure users only access information relevant to their role. Doctors can view their patients' records but not others', patients can only access their own information, and administrative staff have configurable access levels to system data.

- **JWT Authentication**: Employs JSON Web Token (JWT) authentication through Simple JWT integration, providing secure, stateless authentication that scales efficiently. Tokens include role information for rapid authorization checks without additional database queries.

### Healthcare Operations

- **Doctor Profiles**: Maintains detailed doctor records including specializations, availability schedules, credentials, and contact information. The system supports filtering doctors by specialty, location, and availability to facilitate patient-doctor matching.

- **Patient Records**: Manages comprehensive patient information including medical history, current medications, appointment records, and insurance details. The system maintains strict access controls while allowing authorized personnel to efficiently retrieve critical patient information.

- **Relationship Mapping**: Creates flexible associations between patients and doctors, supporting primary care relationships, specialist referrals, and temporary associations. The mapping system includes metadata such as relationship type, date established, and referral source.

### System Architecture

- **RESTful API Architecture**: Provides a comprehensive set of endpoints with consistent URL structures, appropriate HTTP verbs, and thoughtful response formatting. The API supports filtering, pagination, and various output formats to accommodate diverse client needs.

- **Admin Dashboard**: Features a customized Django admin interface with intuitive data organization, custom action buttons for common workflows, and integrated filtering and search capabilities. The dashboard includes role-specific views to streamline administrative tasks.

- **PostgreSQL Integration**: Leverages PostgreSQL's advanced features including JSON field storage for flexible metadata, robust transaction support for data integrity, and efficient indexing for query optimization. The database schema is designed for performance while maintaining logical data relationships.

## 🛠️ Technology Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| Backend Framework | Django 5.1.7 | Provides the core application structure, ORM, and security features |
| API Framework | Django REST Framework | Handles API routing, serialization, validation, and documentation |
| Database | PostgreSQL | Enterprise-grade relational database for reliable data storage |
| Authentication | Simple JWT | Token-based authentication system for secure API access |
| Programming Language | Python 3.11+ | Modern Python version with performance improvements and new features |
| Development Tools | Django Debug Toolbar | Performance profiling and debugging assistance during development |
| Testing Framework | pytest | Comprehensive testing framework for unit and integration tests |

## 📋 Installation Guide

### Prerequisites

Before beginning the installation process, ensure your environment meets these requirements:

- Python 3.11 or newer (Python 3.12 recommended for performance improvements)
- PostgreSQL 14+ database server with administrative access
- Virtual environment tool (venv, virtualenv, or conda)
- pip package manager (latest version)
- Git version control system

### Setup Process

#### 1. Clone and Configure Repository

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd django_health

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Database Configuration

Choose one of the following configuration methods based on your security preferences and deployment environment:

**Option A: Environment Variables (Recommended for Production)**

Create a `.env` file in the project root with the following variables:

```
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=1234

# Secret Key (Generate using: python -c "import secrets; print(secrets.token_urlsafe(50))")
SECRET_KEY=your_generated_secret_key

# Debug Mode (set to False in production)
DEBUG=False
```

**Option B: Direct Settings (Development Environment)**

Update the `settings.py` file with your database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=public'
        }
    }
}
```

#### 3. PostgreSQL Database Setup

Connect to PostgreSQL as the administrative user and set up the database:

```bash
# Connect to PostgreSQL as superuser
sudo -u postgres psql

# Execute the following SQL commands
CREATE DATABASE django_db;
CREATE USER django_user WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;
ALTER SCHEMA public OWNER TO django_user;
ALTER USER django_user CREATEDB;  # Needed for running tests
\q
```

#### 4. Application Initialization

Prepare and initialize the application:

```bash
# Generate database migrations for any model changes
python manage.py makemigrations

# Apply migrations to set up database structure
python manage.py migrate

# Create an administrative superuser
python manage.py createsuperuser
# Follow the prompts to create your admin account

# Collect static files (for production deployment)
python manage.py collectstatic

# Run the development server
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000) and the admin interface at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📚 API Documentation

### Authentication System

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|-------------|----------|
| `/api/auth/register/` | POST | Create new user account | User details (see example below) | User object with token |
| `/api/auth/login/` | POST | Authenticate user | `{"email": "user@example.com", "password": "yourpassword"}` | Access and refresh tokens |
| `/api/auth/token/refresh/` | POST | Refresh access token | `{"refresh": "refresh_token_value"}` | New access token |
| `/api/auth/logout/` | POST | Invalidate user tokens | `{"refresh": "refresh_token_value"}` | Success confirmation |

**User Registration Example:**

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "yourpassword",
    "is_patient": true,
    "is_doctor": false,
    "is_admin_staff": false,
    "phone_number": "+1234567890",  // Optional
    "address": "123 Main St, City, Country"  // Optional
}
```

### Core Resources

| Resource | Base URL | Methods | Description | Authentication Required |
|----------|----------|---------|-------------|-------------------------|
| Doctors | `/api/doctors/` | GET, POST, PUT, PATCH, DELETE | Manage doctor profiles and specializations | Yes |
| Patients | `/api/patients/` | GET, POST, PUT, PATCH, DELETE | Manage patient health records and information | Yes |
| Mappings | `/api/mappings/` | GET, POST, PUT, PATCH, DELETE | Control patient-doctor relationships | Yes |
| Appointments | `/api/appointments/` | GET, POST, PUT, PATCH, DELETE | Schedule and manage patient appointments | Yes |
| Medical Records | `/api/records/` | GET, POST, PUT, PATCH, DELETE | Access and update patient medical records | Yes |

### Filtering Examples

The API supports powerful filtering capabilities for efficient data retrieval:

```
# Find doctors by specialization
/api/doctors/?specialization=cardiology

# Find patients assigned to a specific doctor
/api/patients/?doctor_id=42

# Get appointments for a specific date range
/api/appointments/?start_date=2025-03-01&end_date=2025-03-31

# Find mappings created within a date range
/api/mappings/?created_after=2025-01-01&created_before=2025-03-01
```

## 🔧 Administrative Interface

The Django Health admin interface provides a comprehensive management dashboard tailored for healthcare administrators. Key features include:

- **Custom Admin Actions**: Perform bulk operations like assigning patients to doctors, scheduling appointments, and generating reports
- **Advanced Filtering**: Filter users by role, doctors by specialization, and appointments by status or date
- **Audit Logging**: Track changes to sensitive records with timestamp and user information
- **Export Capabilities**: Generate CSV or PDF exports of patient lists, appointment schedules, and other critical data

Access the admin interface at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) using your superuser credentials.

## 🤝 Contributing

We welcome contributions to enhance Django Health! Here's how you can contribute:

1. **Fork the Repository**: Create your own copy of the project
2. **Create a Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Implement Your Changes**: Add your improvements or fixes
4. **Run Tests**: Ensure all tests pass with your changes
5. **Commit Your Changes**: `git commit -m 'Add some amazing feature'`
6. **Push to Your Branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Submit your changes for review

Please follow these guidelines when contributing:
- Follow the coding style of the project
- Add or update tests to reflect your changes
- Update documentation for any modified functionality
- Reference any relevant issues in your pull request

For major changes, please open an issue first to discuss your proposed modifications.


## 🌟 Acknowledgements

- Django and Django REST Framework communities for their excellent documentation and support
- Contributors who have dedicated their time and expertise to improving this project
- Healthcare professionals who provided domain knowledge and requirements guidance

---


*Thank you for choosing Django Health for your healthcare management needs!*