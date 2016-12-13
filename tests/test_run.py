import json
import pytest
import re
import yaml

# Functions
# ==============================================================================


# Common checks
def common_tests(data, result):

    # General assert
    assert result.exit_code == 0
    assert result.exception is None

    # Structure assert
    assert_root_directory(data, result)
    assert_directories(result)
    assert_directories_with_main_file(result)
    assert_testing_files(result)
    assert_license_file(result)
    assert_readme_file(data, result)
    assert_meta_yaml_file(data, result)
    assert_travis_yaml_file(data, result)


# Check root project
def assert_root_directory(data, result):
    assert result.project.basename == data.get('ansible_role_name')
    assert result.project.isdir()


# Check directories
def assert_directories(result):

    # Root directories
    project_directories = ['defaults', 'files', 'handlers', 'meta',
                           'tasks', 'templates', 'tests', 'vars',
                           'vars/os_distribution', 'vars/os_family']

    # Check project directories
    for directory in project_directories:
        assert result.project.join(directory).isdir()


# Check directories with main.yml file
def assert_directories_with_main_file(result):

    # Root directories contains main.yml file
    directories_with_main_file = ['defaults', 'handlers', 'meta',
                                  'tasks', 'vars']

    # Check project directories with main.yml file
    for directory in directories_with_main_file:
        assert result.project.join(directory).isdir()
        assert result.project.join(directory + '/main.yml').isfile()


# Check test files
def assert_testing_files(result):

    # All files about tests
    test_files = [
        'tests/testing_deployment.yml',
        'testing_deployment.yml',
        '.travis.yml']

    # Check project directories with main.yml file
    for test_file in test_files:
        assert result.project.join(test_file).isfile()


# Check tasks/main.yml file
def assert_tasks_main_file(result):

    task_file = result.project.join('tasks/main.yml')
    task_lines = task_file.readlines(cr=False)

    assert task_file.isfile()
    assert "- 'role::foobar::init'" in task_lines
    assert (
        'include: "{{ role_path }}/tasks/manage_variables.yml"') in task_lines


# Check tasks/manage_variables.yml file
def assert_tasks_manage_vars_file(result):

    task_file = result.project.join('tasks/manage_variables.yml')
    task_lines = task_file.readlines(cr=False)

    assert task_file.isfile()
    assert "register: 'foobar_check_os_release_vars'" in task_lines
    assert (
        'path: "{{ role_path }}/vars/os_family/'
        '{{ ansible_os_family | lower }}.yml"') in task_lines


# Check license file
def assert_license_file(result):

    license_file = result.project.join('LICENSE')
    license_lines = license_file.readlines(cr=False)

    assert license_file.isfile()
    assert 'The MIT License (MIT)' in license_lines


# Check README file
def assert_readme_file(data, result):

    readme_file = result.project.join('README.md')
    readme_lines = readme_file.readlines(cr=False)

    # Regex used to check galaxy role name
    RE = re.compile('^\s*-\s*\{\s*role\s*:\s*%s\.%s\s*\}\s*$' % (
                data.get('author_github_username'),
                data.get('ansible_role_name')))
    print(dir(RE))

    assert readme_file.isfile()
    assert 'Install %s package.' % data.get('ansible_role_name') \
        in readme_lines
    assert len(filter(bool, (RE.match(line) for line in readme_lines)))


# Check meta/main.yml file
def assert_meta_yaml_file(data, result):

    meta_file = result.project.join('meta/main.yml')
    assert meta_file.isfile()

    # Test if yaml file is valid
    with open(str(meta_file.realpath()), 'r') as content:
        assert yaml.load(content)


# Check .travis.yml file
def assert_travis_yaml_file(data, result):

    travis_file = result.project.join('.travis.yml')
    assert travis_file.isfile()

    # Test if yaml file is valid
    with open(str(travis_file.realpath()), 'r') as content:
        assert yaml.load(content)


# Tests
# ==============================================================================

# Template test
@pytest.mark.parametrize('data_filename, role_name', [
    ('./cookiecutter.json', 'role_name'),
    ('./tests/test_01.json', 'test_01'),
    ('./tests/test_02.json', 'test_02'),
    ('./tests/test_03.json', 'test_03'),
    ('./tests/test_04.json', 'test_04')
])
def test_json_values(cookies, data_filename, role_name):

    # Load data file
    with open(data_filename) as data_file:
        data = json.load(data_file)

    # Create project
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == role_name
    common_tests(data, result)
