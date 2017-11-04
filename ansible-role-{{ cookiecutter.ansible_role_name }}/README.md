# {{ cookiecutter.ansible_role_name }}

[![Build Status](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.ansible_role_repository }})

Install {{ cookiecutter.ansible_role_name }} package.

## Requirements

This role requires Ansible {{ cookiecutter.ansible_role_minimal_version }} or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
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
