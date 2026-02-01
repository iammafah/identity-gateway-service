# Identity Gateway Service

A backend-first **identity and authentication gateway** built with **Flask**, using **Firebase Authentication** for secure user login and **PostgreSQL** for backend-owned user profiles.

Firebase is used strictly as an **external authentication provider**, while all user identity, profile data, roles, and business logic are fully managed by the backend.

---

## Stack
- Flask (REST API)
- Firebase Authentication (Email, Google, Facebook)
- Firebase Admin SDK (Token Verification)
- PostgreSQL
- Flask-SQLAlchemy

---

## What This Service Does
- Verifies Firebase ID tokens
- Creates and manages user profiles in PostgreSQL
- Acts as a centralized identity layer
- Keeps authentication provider replaceable
- Designed for production and scaling

---

## Architecture (High Level)

Client → Firebase Auth → Identity Gateway Service → PostgreSQL
