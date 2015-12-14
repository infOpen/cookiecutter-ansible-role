# cookiecutter-ansible-role

Cookiecutter template for Ansible role

## Default variables

    {
        "ansible_role_dependencies": "",
        "ansible_role_description": "Ansible role description",
        "ansible_role_license": "MIT",
        "ansible_role_minimal_version": "1.9",
        "ansible_role_name": "role_name",
        "ansible_role_platforms": "",
        "ansible_role_repository": "ansible-role-{{ cookiecutter.ansible_role_name }}",
        "ansible_role_tags": "",
        "author_email": "foo@bar",
        "author_github_username": "foobar",
        "author_name": "Foo Bar",
        "company_name": "Foobar Inc.",
        "company_url": "http://foo.bar"
    }

## Additional information

### Role default variables

This part need to be completed manually

### Role dependencies and role tags

Use this pattern :

    dep1, dep2 and/or tag1, tag2

We do a split with the "," separator to build these lists.
An empty string will be changed to an empty array.

### Role platforms

Use this pattern :

    plaform:version1,version2;platform2:version1,version2

We do a split with the ";" separator between platform and "," separator
to build version list for each platform.

