# {{ cookiecutter.ansible_role_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }})

Install {{ cookiecutter.ansible_role_name }} package.

## Requirements

This role requires Ansible {{ cookiecutter.ansible_role_minimal_version }} or higher,
and platform requirements are listed in the metadata file.

## Testing

This role has some testing methods.

To use locally testing methods, you need to install Docker and/or Vagrant and Python requirements:

* Create and activate a virtualenv
* Install requirements

```
pip install -r requirements_dev.txt
```

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

### Default role variables

## Dependencies
{% if cookiecutter.ansible_role_dependencies -%}
{%- for dependency in cookiecutter.ansible_role_dependencies.split(',') %}
- {{ dependency | trim }}
{%- endfor %}
{% else %}
None
{%- endif %}

## Example Playbook

    - hosts: servers
      roles:
         - { role: {{ cookiecutter.author_github_username }}.{{ cookiecutter.ansible_role_name }} }

## License

{{ cookiecutter.ansible_role_license }}

## Author Information

{{ cookiecutter.author_name -}}
{%- if cookiecutter.company_name %} (for {{ cookiecutter.company_name }} company){% endif %}
{% if cookiecutter.company_url -%}
- {{ cookiecutter.company_url }}
{%- endif %}
{% if cookiecutter.author_email -%}
- {{ cookiecutter.author_email | replace('@', ' [at] ') }}
{%- endif %}

