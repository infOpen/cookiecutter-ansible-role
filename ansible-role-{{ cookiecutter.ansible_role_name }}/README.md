# {{ cookiecutter.ansible_role_name }}

[![CI](https://github.com/{{ cookiecutter.ansible_role_repository }}/workflows/CI/badge.svg)](https://github.com/{{ cookiecutter.ansible_role_repository }}/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.ansible_role_repository }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.ansible_role_repository }}/)
[![Python 3](https://pyup.io/repos/github/{{ cookiecutter.ansible_role_repository }}/python-3-shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.ansible_role_repository }}/)

Install {{ cookiecutter.ansible_role_name }} package.

## Requirements

This role requires Ansible {{ cookiecutter.ansible_role_minimal_version }} or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- CentOS 8
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies
{% if cookiecutter.ansible_role_dependencies -%}
{%- for dependency in cookiecutter.ansible_role_dependencies.split(',') %}
- {{ dependency | trim }}
{%- endfor %}
{% else %}
None
{%- endif %}

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: {{ cookiecutter.author_github_username }}.{{ cookiecutter.ansible_role_name }} }
```

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

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/{{ cookiecutter.ansible_role_repository }}&style=flat
