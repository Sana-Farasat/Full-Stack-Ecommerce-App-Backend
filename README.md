# Backend README.md

# StrideX Backend

A production-ready ecommerce REST API built with **FastAPI**, **SQLModel**, and **PostgreSQL**. It provides authentication, product management, categories, shopping cart, checkout, and order management.

---

# Features

* JWT Authentication
* User Registration
* User Login
* Categories API
* Products API
* Cart API
* Checkout API
* Orders API
* PostgreSQL Database
* SQLModel ORM
* Password Hashing
* CORS Support
* Interactive Swagger Documentation

---

# Tech Stack

* FastAPI
* SQLModel
* SQLAlchemy
* PostgreSQL
* Pydantic
* JWT
* pwdlib
* Uvicorn

---

# Folder Structure

```text
backend
│
├── app
│   ├── api
│   ├── core
│   ├── crud
│   ├── db
│   ├── dependencies
│   ├── models
│   ├── schemas
│   ├── main.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

# Requirements

Install

* Python 3.11+
* PostgreSQL

Verify Python

```bash
python --version
```

---

# Installation

Clone repository

```bash
git clone <backend-repository-url>
```

Move into backend

```bash
cd backend
```

Create virtual environment

Windows

```bash
python -m venv .venv
```

Activate

Command Prompt

```bash
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

Install all project dependencies:

```bash
uv sync
```

If you don't have a requirements file

```bash
pip install fastapi uvicorn sqlmodel sqlalchemy psycopg2-binary python-jose pwdlib python-dotenv python-multipart
```

---

# PostgreSQL Setup

Create a PostgreSQL database.

Example

```text
Database Name

stridex
```

---

# Environment Variables

Create

```text
.env
```

Add

```env
DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:5432/stridex

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Replace

* USERNAME
* PASSWORD
* DATABASE NAME
* SECRET KEY

with your own values.

---

# Run Development Server

```bash
uvicorn app.main:app --reload
```

Server

```text
http://127.0.0.1:8000
```

---

# Interactive API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Authentication

Authentication uses JWT Bearer Token.

Workflow

1. Register
2. Login
3. Receive Access Token
4. Send token in Authorization header

Example

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

# Available APIs

## Authentication

```text
POST /auth/register
POST /auth/login
```

---

## Categories

```text
GET /categories
GET /categories/{id}
```

---

## Products

```text
GET /products
GET /products/{slug}
```

---

## Cart

```text
GET /cart
POST /cart
PATCH /cart/{cart_id}
DELETE /cart/{cart_id}
DELETE /cart
```

---

## Orders

```text
POST /orders/checkout
GET /orders
```

---

# Database Models

* User
* Category
* Product
* Cart
* Order
* OrderItem

---

# CORS

Allowed Origins

```text
http://localhost:3000
http://127.0.0.1:3000
```

You can update these in

```text
app/main.py
```

---

# Running Tests

If you add tests later

```bash
pytest
```

---

# Deployment

Recommended platforms

* Render
* Railway
* Fly.io
* DigitalOcean
* VPS

Required Environment Variables

```text
DATABASE_URL
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
```

---

# Common Errors

## Database Connection Error

Check

* PostgreSQL is running
* DATABASE_URL is correct

---

## Invalid Token

Check

* SECRET_KEY
* Token expiration
* Authorization header

---

## CORS Error

Verify frontend URL is included in

```python
allow_origins
```

inside

```text
app/main.py
```

---

# Project Architecture

```text
Client (Next.js)
        │
        ▼
 FastAPI REST API
        │
        ▼
 SQLModel ORM
        │
        ▼
 PostgreSQL Database
```

---

# Author

Sana Farasat

---

# License

This project is intended for learning, portfolio, and demonstration purposes.
