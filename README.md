# AI Prompt Audit Platform

## Overview

This project is a multi-tier application for managing users, prompts, AI models, and prompt execution history.

## Architecture

* Client Layer: HTML, JavaScript, CSS
* Service Layer: FastAPI
* Business Layer: Python
* Data Layer: PostgreSQL with psycopg2

## Features

* Create, retrieve, update, and delete users, prompts, AI models, and executions
* Search users by name and models by provider
* Filter prompts by user and executions by prompt
* View all records or individual records by ID

## Files

* src/service.py - FastAPI routes
* src/business.py - business logic
* src/db.py - database access
* project3-client/index.html - frontend
* project3-client/styles.css - frontend styling
* schema.sql - database schema
* requirements.txt - dependencies

## Prerequisites

* Python 3
* PostgreSQL
* pgAdmin 4
* pip

## Setup

1. Download or clone the repository
2. Create a PostgreSQL database named ai_prompt_audit
3. Run schema.sql to create the tables
4. Create a .env file inside src using .env.example as a guide
5. Install dependencies with pip install -r requirements.txt

## Running the Application

### Backend

Open a terminal in the src folder and run:
cd src
uvicorn service:app --reload

Open FastAPI docs:
http://127.0.0.1:8000/docs

### Frontend

Open a second terminal and run:
cd project3-client
python -m http.server 5500

Open in browser:
http://localhost:5500

Enter API address:
http://127.0.0.1:8000

Click Connect

## Testing

The system was tested for create, update, get all, get one, search, and delete operations across all entities.

## Author

Nishta Rawat
