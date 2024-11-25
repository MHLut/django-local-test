# Django local test

A test project for local Django development, original by [@MHLut](https://github.com/MHLut).

This project is **not suitable for production** purposes!

## What is this for?

...

See also: [A simple approach to running Django Core locally](https://marijkeluttekes.dev/blog/articles/2024/01/25/a-simple-approach-to-running-django-core-locally/).

## Installation

Warning: These instructions are crude and not a tutorial: I assume you already know how to use the tools described.

### Requirements

* Technical knowledge of Git, GitHub, Python, Django, etc.
* Django fork per [Writing your first contribution for Django](https://docs.djangoproject.com/en/dev/intro/contributing/).
* [just](https://github.com/casey/just) (optional).
* [pre-commit](https://pre-commit.com/#install) (optional; for development only).

### Setup

1. Pick a directory in which to store the Django core and test projects side-by-side.
2. Clone your fork of Django core; the directory name should be `django`.
3. Clone the Django local test project.
4. Navigate to the local test project directory.
5. Copy the `.env` file from `.env.example`; adjust `.env` where needed.
6. Create a virtual environment and activate it.
7. Install the dependencies from `requirements.txt`.

The commands are something like this:

```sh
git clone <fork>
git clone git@github.com:MHLut/django-local-test.git
cd django-local-test
cp .env.example .env
python3 -m venv venv
pip install -r requirements.txt
```
