# AuthenticationService

## Overview
The Authentication Service is responsible for managing user authentication and authorization across the SOFEA ecosystem. Its primary role is to ensure secure access by issuing and validating JWT tokens, which other services rely on to identify and authorize users.

The system exposes three main endpoints:
- `POST /auth/login`:  
  Allows a user to log in to the system using an `email` and `password`.  
  On successful authentication, a JWT token is returned along with basic user information.

- `POST /auth/register`:  
  Allows a user to create an account by providing their `name`, `email`, `password`, and `role`.  
  The password is securely hashed before being stored. On success, the user’s public information is returned.

- `GET /auth/validate-token`:  
  Enables other services to verify the validity of a JWT token sent in the `Authorization` header.  
  If valid and the user exists, the service responds with the user’s ID and a `valid: true` flag.

---
## ⚙️ System Architecture
This service follows a **Hexagonal Architecture (Ports and Adapters)** pattern. It is designed to isolate the core business logic from external concerns such as frameworks, databases, and communication protocols.

#### Key Architectural Components

- **Application Layer**:  
  Contains the core use cases and service interfaces. Business logic is implemented here, independent of frameworks or infrastructure.

- **Adapters (Input/Output)**:  
  - **Input Adapters**: Handle HTTP requests using Flask and expose routes via a REST API.
  - **Output Adapters**: Responsible for persistence, unique ID generation, password hashing, and JWT token handling. Examples include:
    - `LocalDBUserRepository`: In-memory user storage (can be replaced by a real DB implementation).
    - `Argon2CffiHasher`: Secure password hashing.
    - `UUIDIder`: Generates unique user identifiers.
    - `JWTHandler`: Encodes and decodes JWT tokens.

- **Service Communication**:  
  - The `validate-token` endpoint enables secure interaction with other microservices by providing a token validation mechanism.
  - Communication is designed to be stateless using JWT.

## 🚀 Setup and Usage

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SwEng2-2025i-nutrias/AuthenticationService.git
   cd AuthenticationService
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

> The API will run locally at:  
**http://127.0.0.1:5001**

---

### 📮 API Endpoints

#### 🔸 Create a User

#### 🔹 Register a User

- **POST** `/auth/register`
- **Body Example**:
  ```json
  {
    "email": "samuevarga@gmail.com",
    "password": "samuevarga",
    "name": "Samuel",
    "role": "farmer"
  }
    ```
- **Curl Command**:
    ```bash
  curl -X POST http://127.0.0.1:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email": "samuevarga@gmail.com", "password": "samuevarga", "name": "Samuel", "role": "farmer"}'
     ```

#### 🔹 Login a User

- **POST** `/auth/login`
- **Body Example**:
  ```json
  {
    "email": "samuevarga@gmail.com",
    "password": "samuevarga"
  }

    ```
- **Curl Command**:
  ```bash
  curl -X POST http://127.0.0.1:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "samuevarga@gmail.com", "password": "samuevarga"}'
  ```

#### 🔸 Validate a Token

- **GET** `/auth/validate-token`
- **Headers**
    - Authorization: Bearer <your_jwt_token>
- **Curl Command**:
  ```bash
  curl -X GET http://127.0.0.1:5000/auth/validate-token \
     -H "Authorization: Bearer <your_jwt_token>"
  ```

---

### 📘 API Documentation

Once the server is running, you can access the interactive API documentation via Swagger UI at:

👉 **http://127.0.0.1:5001/apidocs/**
