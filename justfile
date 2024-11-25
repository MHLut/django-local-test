# Run the help command.
default: help

# List all available commands.
help:
	just -l

# Create venv if one doesn't exist.
venv-create:
	test -d venv || python3 -m venv venv

# Activate venv and upgrade pip.
venv-upgrade-pip: venv-create
	. venv/bin/activate && pip install --no-cache-dir --upgrade pip

# Activate venv and install requirements.
venv-install: venv-upgrade-pip
	. venv/bin/activate && pip install -r requirements.txt

# Activate the development runserver.
run:
	. venv/bin/activate && ./src/manage.py runserver

# Install requirements and activate the runserver.
refresh: venv-install run
