# cookiecutter-ansible-role

[![Build Status](https://img.shields.io/travis/infOpen/cookiecutter-ansible-role/master.svg?label=travis_master)](https://travis-ci.org/infOpen/cookiecutter-ansible-role)
[![Build Status](https://img.shields.io/travis/infOpen/cookiecutter-ansible-role/develop.svg?label=travis_develop)](https://travis-ci.org/infOpen/cookiecutter-ansible-role)
[![Updates](https://pyup.io/repos/github/infOpen/cookiecutter-ansible-role/shield.svg)](https://pyup.io/repos/github/infOpen/cookiecutter-ansible-role/)
[![Python 3](https://pyup.io/repos/github/infOpen/cookiecutter-ansible-role/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/cookiecutter-ansible-role/)

Cookiecutter template for Ansible role

## Default variables

```json
{
    "ansible_role_name": "role_name",
    "ansible_role_dependencies": "",
    "ansible_role_description": "Ansible role to install and configure {{ cookiecutter.ansible_role_name }}",
    "ansible_role_license": "MIT",
    "ansible_role_minimal_version": "2.8",
    "ansible_role_github_branch": "master",
    "ansible_role_platforms": "Debian:stretch,buster;Ubuntu:focal,bionic;EL:7,8",
    "ansible_role_repository": "infOpen/ansible-role-{{ cookiecutter.ansible_role_name }}",
    "ansible_role_tags": "",
    "author_email": "foo@bar",
    "author_github_username": "foobar",
    "author_name": "Foo Bar",
    "company_name": "Foobar Inc.",
    "company_url": "http://foo.bar",
    "_copy_without_render": [
      "molecule/default/create.yml",
      "molecule/default/destroy.yml",
      "molecule/default/Dockerfile.j2"
    ]
}
```

## Additional information

### Role default variables

This part need to be completed manually.

### Role dependencies and role tags

Use this pattern:

```
dep1, dep2 and/or tag1, tag2
```

We do a split with the `,` separator to build these lists.
An empty string will be changed to an empty array.

### Role platforms

Use this pattern:

```
plaform:version1,version2;platform2:version1,version2
```

We do a split with the `;` separator between platform and `,` separator
to build version list for each platform.

## Run tests

Requirements: Docker and docker-compose installed

```
docker-compose up --build --force-recreate
```
