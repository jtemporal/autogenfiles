"""
The module that reads the variables file and return the variables
"""

from configparser import ConfigParser


def variables_to_substitute(variable_list: str):
    """Reads variable file

    Params:
        :variable_list: str, Required
            The variable file to be read and interpreted
    """
    parser = ConfigParser()
    parser.read(variable_list)
    try:
        variables = dict(parser['variables'])
    except KeyError:
        print(f'Oh no! No "variables" section found in {variable_list}')
        return
    return variables
