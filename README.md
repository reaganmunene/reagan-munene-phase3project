# reagan-munene-phase3project
## PHASE 3 Independent project CLI and ORM Python Application

 This is a Python CLI application built using SQLAlchemy ORM. It allows users to interact with a SQLite database through a command-line Interface (CLI)

## Features

- **ORM Models:** The application defines two ORM models, `Parent` and `Child`, representing a one-to-many relationship between parents and their children.

- **CLI Commands:** Users can perform various operations on the database using CLI commands, including creating parent records, listing all parent records, and more.

- **Error Handling:** The application provides informative error messages for invalid user inputs and database operations.


## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/reaganmunene/reagan-munene-phase3project
    ```

2. Navigate to the project directory:

    ```bash
    cd reagan-munene-phase3project
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```


## Commands

- **create-parent:** Create a new parent record.
- **list-parents:** List all parent records in the database.

## Project Structure

- **cli.py:** Contains the CLI commands and entry point of the application.
- **database.py:** Defines the ORM models and database-related functions.
- **models.py:** Contains the ORM model definitions.

## Dependancies requirements

This project needs the following installed in your local environment for successful running of the application.

Install:
1. Sqlalchemy
2. A virtual environment dependancy
3. python3 on your machine

## Contributions
Contributions to the project are welcome!
