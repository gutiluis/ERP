```bash
.
├── .env.example
├── .github
│   └── workflows
│       └── test.yml
├── .gitignore
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── customers.py
│   │   ├── invoice.py
│   │   ├── payments.py
│   │   ├── products.py
│   │   └── user.py
│   └── routes
│       └── health.py
├── docker-compose.yml
├── Dockerfile
├── electron.vite.config.ts
├── eslint.config.mjs
├── package.json
├── postcss.config.js
├── README.md
├── requirements.txt
├── src
│   ├── main
│   │   ├── index.ts
│   │   ├── modules
│   │   └── tests
│   ├── preload
│   │   └── index.ts
│   └── renderer
│       ├── assets
│       ├── index.html
│       └── src
├── tailwind.config.js
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── setup_test_db.py
│   ├── test_connection.py
│   ├── test_customer.py
│   ├── test_invoice.py
│   ├── test_products.py
│   └── test_user.py
├── tsconfig.json
└── tsconfig.node.json
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

# GitHub Actions
team and repo oriented
production stability
runs in github servers
(CI) continuous integration / (CD) Continuous Deployment
automating workflows
code scanning workflows
pages workflows
building and publishing packages
deploying projects

# git pre-commit hook
if the hook fails the commit is blocked
automatically runs tools before commit






######### FRONTEND



# ESLint vs Vitest vs git pre-commit hook:
ESLint: syntax/style/formatting before or during dev. unused variables, wrong imports, bad patterns, formatting rules, possible bugs, code style consistency. runs local 
Vitest: testing behaviour when running tests. testing framework. Tests if the program works. runs local
git pre-commit runs local


# How to run eslint:


##############
# package.json with electron in the project:
as long as package.json has "out/main/index.js"
package.json defines the runtime entry
does not define typescript compiler options


###########################
############################
tsconfig.json # renderer bundler
tsconfig.node.json # main process node16 # electon main process runs in node
electron.vite.config.ts


the tsconfig.node.json file controls how typesscript compiles the electron main process

separation prevents typescript resolving modules incorrectly
path mismatches between node and vite
subtle runtime errors




#############################
# project environment and process
main process runs in node environment
has access to filesystems, OS
entry defined in main: out/main/index.js
compiled with tsc
executed directly by electron node
"moduleresolution": "node16" or "nodenext"
# renderer process execution environment
runs in chromium
built with vite
uses vite for testing
bundled before execution


##################################
# Electron for this project:
- Does not run the main source file directly as is an index.js file it runs the built output file

-


########################
# Frontend unit test with: VITEST
Files to test src/main/index.ts:
# to test src/main/index.ts. run from the root project
- npm install -D vitest
- touch src/main/index.test.ts

# Avoid record and playback testing tools, write a small set of UI integration tests. they resist changeability and obstruct abstractions
# use record-playback tools to generate fragments of scripts
# many more low-level unittests than high level through GUI
# use jasmine to test javascrip units UI
# 

# vite uses esbuild. handles ESM internally. transpiles typescript automatically
# as long as typescript is installed can run vitest for ts:
# as long as the parent has the package.json the child will run it
# as long as package.json has {"type": "module"}?????? runs without it too
# add type: module when running the files directly with node.js
# without type module node expects commonJS
# with type: module node expects ES modules
# can use the source file .ts and test file .js 
# best practise the source file .ts and test file .ts in vitest for consistency
# mix source and test file extensions for migrations from js to ts, gradual convertion, testing compiled output



########################

# tsconfig.json "target": "es2020" vs "target": "esnext"
target esnext vs target es2020 differs in compilation amount
target controls the output
# es2020
use es2020 while building a node library, 
publishing to npm, 
supporting old environment, 
not bundling
node backend
avoids new js features
old node versions
old browsers
# esnext
vite
modern browsers
vitest
frontend apps
newest js syntax possible
not downlevel modern features
assume a modern environment
#############


# tsconfig.json { "moduleresolution": "node16" } vs { "moduleresolution": "bundler" }
# node16, node, nodenext
node backend
running compiled js directly with node
node building cli tool
node server
node dist/index.js
express backend
modern node esm projects (enterprise service management)
node executes the js
compiled by tsc
# bundler
react app
anything bundled for the browser
vite
vitest
astro
sveltekit
next.js (new versions)
tests run by vitest
frontend ts is processed by vite
node is not directly executing typescript output
bundler executes/transforms the js

##########
# ESM enterprise service management VS ESR enterprise resource planning
complementary not competing



###########
# make typescript configuration file from CLI commands
# https://www.typescriptlang.org/docs/handbook/compiler-options.html
tsc --init # first make npm init -y


#############
javascript has two module systems
ES Modules (import)
Common JS (require, module.exports)

########
windowmanager module:
supports multiple windows
tray support
window state persistence remember size/position
deep linking
############
In Electron:
app is the application lifecycle controller
BrowserWindow is the window lifecycle controller

####
environment loader module in ts:
How it works:
Reads NODE_ENV (default: development)
Looks for .env.development or .env.production
Falls back to .env if specific file doesn’t exist
Loads variables into process.env (for main process)

###
test each module first for frontend with vite mock
