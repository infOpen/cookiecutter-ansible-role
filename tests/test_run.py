import json
import subprocess
import yaml

#==============================================================================
# Functions
#==============================================================================

# Common checks
def common_tests(data, result):

    # General assert
    assert result.exit_code == 0
    assert result.exception is None

    # Structure assert
    project_root_tests(data, result)
    project_directories_tests(result)
    project_directories_with_main_file_tests(result)
    project_testing_files_tests(result)
    project_license_file_tests(result)
    project_readme_file_tests(data, result)
    project_meta_yaml_file_tests(data, result)
    project_travis_yaml_file_tests(data, result)

    # Execute serverspec tests for the role
    with result.project.as_cwd():
        subprocess.check_output(['bundle', 'install'])
        subprocess.check_output(['bundle', 'exec', 'rake'])


# Check root project
def project_root_tests(data, result):
    assert result.project.basename == data.get('ansible_role_name')
    assert result.project.isdir()


# Check directories
def project_directories_tests(result):

    # Root directories
    project_directories = [ 'defaults', 'files', 'handlers', 'meta',
                            'spec', 'tasks', 'templates', 'tests', 'vars' ]

    with result.project.as_cwd():
        subprocess.check_output(['pwd'])
        subprocess.check_output(['ls', '-lha'])
        subprocess.check_output(['ls', '-lha', '../'])

    # Check project directories
    for project_directory in project_directories:
        assert result.project.join(project_directory).isdir()


# Check directories
def project_directories_with_main_file_tests(result):

    # Root directories contains main.yml file
    project_directories_with_main_file = [ 'defaults', 'handlers', 'meta',
                                           'tasks', 'vars' ]

    # Check project directories with main.yml file
    for project_directory in project_directories_with_main_file:
        assert result.project.join(project_directory).isdir()
        assert result.project.join(project_directory + '/main.yml').isfile()


# Check test files
def project_testing_files_tests(result):

    # All files about tests
    test_files = [
        'Gemfile', 'Rakefile', 'spec/trusty_spec.rb', 'tests/ansible.cfg',
        'tests/inventory', 'tests/test_common.yml', 'tests/test_travis.yml',
        'tests/test_vagrant.yml', 'Vagrantfile', '.travis.yml' ]

    # Check project directories with main.yml file
    for test_file in test_files:
        assert result.project.join(test_file).isfile()


# Check license file
def project_license_file_tests(result):

    license_file = result.project.join('LICENSE')
    license_lines = license_file.readlines(cr=False)

    assert license_file.isfile()
    assert 'The MIT License (MIT)' in license_lines


# Check README file
def project_readme_file_tests(data, result):

    readme_file = result.project.join('README.md')
    readme_lines = readme_file.readlines(cr=False)

    assert readme_file.isfile()
    assert 'Install %s package.' % data.get('ansible_role_name') \
        in readme_lines
    assert any('role: %s.%s' % (data.get('author_github_username'),
        data.get('ansible_role_name')) \
        in line for line in readme_lines)


# Check meta/main.yml file
def project_meta_yaml_file_tests(data, result):

    meta_file = result.project.join('meta/main.yml')
    assert meta_file.isfile()

    # Test if yaml file is valid
    with open(str(meta_file.realpath()), 'r') as content:
        assert yaml.load(content)


# Check .travis.yml file
def project_travis_yaml_file_tests(data, result):

    travis_file = result.project.join('.travis.yml')
    assert travis_file.isfile()

    # Test if yaml file is valid
    with open(str(travis_file.realpath()), 'r') as content:
        assert yaml.load(content)


#==============================================================================
# Tests
#==============================================================================

# Template test with default values
def test_with_default_values(cookies):

    # Load data file
    with open('./cookiecutter.json') as data_file:
        data = json.load(data_file)

    # Create project
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == 'role_name'
    common_tests(data, result)


# Tests about values from test_01.json file
def test_json_01(cookies):

    # Load data file
    with open('./tests/test_01.json') as data_file:
        data = json.load(data_file)

    # Build template with json data
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == 'test_01'
    common_tests(data, result)


# Tests about values from test_02.json file
def test_json_02(cookies):

    # Load data file
    with open('./tests/test_02.json') as data_file:
        data = json.load(data_file)

    # Build template with json data
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == 'test_02'
    common_tests(data, result)


# Tests about values from test_03.json file
def test_json_03(cookies):

    # Load data file
    with open('./tests/test_03.json') as data_file:
        data = json.load(data_file)

    # Build template with json data
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == 'test_03'
    common_tests(data, result)


# Tests about values from test_04.json file
def test_json_04(cookies):

    # Load data file
    with open('./tests/test_04.json') as data_file:
        data = json.load(data_file)

    # Build template with json data
    result = cookies.bake(extra_context=data)

    # Common tests
    assert data.get('ansible_role_name') == 'test_04'
    common_tests(data, result)

