#!/bin/bash

# Define the root directory
ROOT_DIR="$(pwd)"

# Define directories to be created
DIRECTORIES=(
    "$ROOT_DIR/app/blueprints/main"
    "$ROOT_DIR/app/services"
    "$ROOT_DIR/app/models"
    "$ROOT_DIR/app/controllers"
    "$ROOT_DIR/app/config"
    "$ROOT_DIR/app/utils"
    "$ROOT_DIR/tests/unit"
    "$ROOT_DIR/tests/integration"
)

# Define files to be created with initial content
FILES=(
    "$ROOT_DIR/app/blueprints/main/__init__.py"
    "$ROOT_DIR/app/blueprints/main/routes.py"
    "$ROOT_DIR/app/services/example_service.py"
    "$ROOT_DIR/app/models/user.py"
    "$ROOT_DIR/app/controllers/user_controller.py"
    "$ROOT_DIR/app/config/__init__.py"
    "$ROOT_DIR/app/config/development.py"
    "$ROOT_DIR/app/config/production.py"
    "$ROOT_DIR/app/utils/helpers.py"
    "$ROOT_DIR/app/__init__.py"
    "$ROOT_DIR/app/wsgi.py"
    "$ROOT_DIR/tests/unit/test_example.py"
    "$ROOT_DIR/tests/integration/test_integration.py"
    "$ROOT_DIR/tests/conftest.py"
    "$ROOT_DIR/.env"
    "$ROOT_DIR/.gitignore"
    "$ROOT_DIR/Dockerfile"
    "$ROOT_DIR/requirements.txt"
    "$ROOT_DIR/README.md"
    "$ROOT_DIR/manage.py"
)

# Create directories
for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$dir"
    echo "Created directory: $dir"
done

# Create files
for file in "${FILES[@]}"; do
    touch "$file"
    echo "Created file: $file"
done

# Add basic content to specific files (optional)
echo "# Main application blueprint" > "$ROOT_DIR/app/blueprints/main/routes.py"
echo "# Example business logic service" > "$ROOT_DIR/app/services/example_service.py"
echo "# Example ORM model" > "$ROOT_DIR/app/models/user.py"
echo "# Example route handler" > "$ROOT_DIR/app/controllers/user_controller.py"
echo "# Configuration initialization" > "$ROOT_DIR/app/config/__init__.py"
echo "# Development-specific settings" > "$ROOT_DIR/app/config/development.py"
echo "# Production-specific settings" > "$ROOT_DIR/app/config/production.py"
echo "# Example utility function" > "$ROOT_DIR/app/utils/helpers.py"
echo "# Flask application factory" > "$ROOT_DIR/app/__init__.py"
echo "# WSGI entry point for the application" > "$ROOT_DIR/app/wsgi.py"
echo "# Example unit test" > "$ROOT_DIR/tests/unit/test_example.py"
echo "# Example integration test" > "$ROOT_DIR/tests/integration/test_integration.py"
echo "# Pytest fixtures and setup" > "$ROOT_DIR/tests/conftest.py"
echo "# Environment variables file (for development)" > "$ROOT_DIR/.env"
echo "# Git ignore rules" > "$ROOT_DIR/.gitignore"
echo "# Dockerfile for containerization" > "$ROOT_DIR/Dockerfile"
echo "# Python package dependencies" > "$ROOT_DIR/requirements.txt"
echo "# Project documentation" > "$ROOT_DIR/README.md"
echo "# Script for running and managing the app" > "$ROOT_DIR/manage.py"

echo "Project structure created successfully!"
