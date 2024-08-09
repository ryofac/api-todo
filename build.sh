#!/usr/bin/env bash
# Exit on error
set -o errexit

# Enters the root
cd task_manager/

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements/production.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate