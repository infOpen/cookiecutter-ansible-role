# {{ cookiecutter.ansible_role_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }})

Install {{ cookiecutter.ansible_role_name }} package.

## Requirements

This role requires Ansible {{ cookiecutter.ansible_role_minimal_version }} or higher,
and platform requirements are listed in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

### Testing dependencies
- install [Vagrant](https://www.vagrantup.com)
- install [Vagrant serverspec plugin](https://github.com/jvoorhis/vagrant-serverspec)
    $ vagrant plugin install vagrant-serverspec
- install ruby dependencies
    $ bundle install

### Running tests

#### Run playbook and test

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

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

