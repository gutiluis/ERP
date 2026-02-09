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

# colima docker. no docker destkop. everything is in colima
colima ssh

#
all requirements of the project go inside Dockerfile

#
docker compose automatically creates a private network
Network erp_software_system_default

# to test model uniqueness of sqlalchemy mapping:
from app.extensions import db
from app.models.customers import Customer
from sqlalchemy import text
db.session.execute(text('show create table table_of_a_model'))



#
user class is functioning
customer class is functioning
invoice class

#
how to know if its an imperative or declarative table column

#
relationship loading techniques

# there are declarative relationships and imperative relationships for mappings in sqlalchemy
# there are declarative annotated relationships mappings in sqlalchemy orm2.0


#
class Someclass(Base):
    ...
table creation is not business logic


#
src/main/index.ts → Electron main process
Responsible for creating windows, handling app lifecycle, IPC, menus, etc.
Runs in Node context (not browser).

src/preload/index.ts → Preload script
Runs in the browser context before the renderer loads.
Provides a safe bridge between renderer and main process (for IPC).

src/renderer/index.html -> UI frontend

#
electron.vite.config.ts from official documentation