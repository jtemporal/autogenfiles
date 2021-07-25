from autogenfiles.configuration import variables_to_substitute


def test_variables_to_substitute_fail_find_variables():
    variables = variables_to_substitute('tests/fixtures/variables_fail.yaml')
    assert variables is None


def test_variables_to_substitute_succeed_find_variables():
    variables = variables_to_substitute('tests/fixtures/variables.yaml')
    expected = {
        'base_url': 'https://jtemporal.com/',
        'project_name': 'OperationSimplicity',
        'project_number': '42',
        'project_title': 'Operation Simplicity'
    }
    assert variables == expected
