from configparser import ConfigParser
from pathlib import Path

import click

from .files_helper import files


def variables_to_substitute(variable_list):
    parser = ConfigParser()
    parser.read(variable_list)
    try:
        variables = dict(parser['variables'])
    except KeyError:
        print(f'Oh no! No "variables" section found in {variable_list}')
        return
    return variables


@click.command()
@click.option('-v', '--variable-list', default='variables.yaml',
              help='Name of the yaml files containing varibales')
@click.option('-o', '--output-path', default='./',
              help='Output path, by default writes to root')
def main(variable_list, output_path):
    print(f'Output path: {output_path}')
    # read variables to substitute
    if not Path(variable_list).is_file():
        print(f'Oh no! No file named {variable_list} found!')
        return

    variables = variables_to_substitute(variable_list)
    if not variables:
        return
    click.echo(f'Variables found: {list(variables.keys())}')

    files(variables, output_path)
    click.echo('Output fully written')


if __name__ == '__main__':
    main()
