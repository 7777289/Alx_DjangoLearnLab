# LibraryProject

This Django project demonstrates advanced user management and security features, including:

- Custom user model (`CustomUser`) with additional fields:
  - `date_of_birth`
  - `profile_photo`
- Custom user manager (`CustomUserManager`) for creating users and superusers using email
- Permissions and groups management
- CRUD functionality for `Book` model with custom permissions

## Project Structure

- `bookshelf/` — Contains models, views, and admin customization
- `LibraryProject/` — Root Django project configuration
- `README.md` — This file

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/7777289/Alx_DjangoLearnLab.git
   cd advanced_features_and_security/LibraryProject
