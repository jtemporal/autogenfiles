from configparser import ConfigParser


def variables_to_substitute(variable_list):
    parser = ConfigParser()
    parser.read(variable_list)
    try:
        variables = dict(parser['variables'])
    except KeyError:
        print(f'Oh no! No "variables" section found in {variable_list}')
        return
    return variables
