
## Getting Started

## Tools / Technology

The application is based on Django(4.0.4) monolithic architecture with use of forms, templates, custom template tags.

Application setup is managed by docker-compose

## Setup

In the Ubuntu OS, run
```bash
./scripts/build.sh
```
which will setup the project according to the configuration.

The server will be available at http://localhost:8000.
The admin will be available at http://localhost:8000/admin.
Landing Page: http://localhost:8000/
Login: http://localhost:8000/accounts/login/
Logout: http://localhost:8000/accounts/logout/
List a car: http://localhost:8000/car/sell/
Buy a car: http://localhost:8000/car/buy/<car_id>/


## Features

* Car Listing
* Car Buy(inquiry)
* Car Sell

## Useful commands

```
./scripts/build.sh - build the application
./scripts/app_logs.sh - To show the Django application logs
./scripts/app_shell.sh - To execute the Django commands
./scripts/app_lint.sh - Pylint checker
./scripts/code_coverage.sh - To check the code coverage for unittest
```
