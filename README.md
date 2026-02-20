```bash
erp-backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── invoice.py
│   │   └── payment.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── health.py
│   └── main.py
├── migrations/          # later (Flask-Migrate)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env # no python venv in production
```

ERP Backend System:
A scalable and modular Enterprise Resource Planning (ERP) backend built with Python, SQLAlchemy, and SQL, containerized using Docker.
Designed for single-tenant deployment initially, with architecture prepared for future transition into a full multi-tenant SaaS platform.


Overview:
This ERP backend provides core business process management including:
-User & Role Management
-Inventory
-Sales & Procurement
-Finance
-HR Modules
-Reporting & Analytics
The system follows a modular, service-oriented architecture to ensure scalability, maintainability, and future SaaS extensibility.


Tech Stack:
-Language: Python 3.x
-ORM: SQLAlchemy
-Database: PostgreSQL / MySQL (configurable)
-Containerization: Docker & Docker Compose
-API Layer: REST (Flask / FastAPI – adjust if needed)
-Authentication: JWT-based authentication
-Migrations: Alembic

Features:
Authentication & Authorization
JWT-based authentication
Role-Based Access Control (RBAC)
Secure password hashing

Inventory Management:
Product management
Stock tracking
Warehouse support

Finance:
Invoice generation
Payment tracking
Financial reports

Sales & Procurement:
Sales orders
Purchase orders
Vendor management

Human Resources:
Employee management
Leave tracking
Payroll foundation (extendable)

Reporting:
Aggregated business metrics
Filterable reports
Export-ready data endpoints


Test Include:
Unit tests
Service layer tests
API integration tests

Security:
Password hashing using bcrypt
JWT access tokens
Input validation
ORM-based query protection against SQL injection
Docker container isolation

How to run eslint"
run lint