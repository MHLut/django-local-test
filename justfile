# Run the help command.
default: help

# List all available commands.
help:
	just -l

# Git pull current and Django repository.
pull:
    git pull
    cd ../django && git pull

# Create `venv` if one doesn't exist.
venv-create:
	test -d venv || python3 -m venv venv

# Activate `venv` and upgrade pip.
venv-upgrade-pip: venv-create
	. venv/bin/activate && pip install --no-cache-dir --upgrade pip

# Activate `venv` and install requirements.
venv-install: venv-upgrade-pip
	. venv/bin/activate && pip install -r requirements.txt

# Run Django management command.
manage *posargs='':
    . venv/bin/activate && python src/manage.py {{ posargs }}

# Activate the development server (`runserver`).
run:
	just manage runserver

# Pull code, requirements, translations, and run the server.
refresh: pull venv-install compilemessages run

# Run `show_urls` management command.
show_urls:
    just manage show_urls

# Run `makemessages` management command.
makemessages *posargs='':
    just manage makemessages --all --no-wrap --no-obsolete --ignore venv {{ posargs }}

# Run `compilemessages` management command.
compilemessages *posargs='':
    just manage compilemessages --ignore venv {{ posargs }}
