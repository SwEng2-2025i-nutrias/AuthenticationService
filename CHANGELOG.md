# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.1] - 2025-06-09

### Added
- `/auth/register` endpoint for user registration.
- `AuthService` implementation with password hashing using `argon2-cffi`.
- Local JSON repository (`LocalDBUserRepository`) to simulate a database.

### Changed
- Refactored the project structure to follow hexagonal architecture.

### Fixed
- Error handling when the request `Content-Type` is not `application/json`.

---

## [0.1.0] - 2025-06-09

### Added
- First working version of the authentication service.
