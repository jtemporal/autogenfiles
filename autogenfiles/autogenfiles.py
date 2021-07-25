from pathlib import Path

import click
from jinja2 import Template

from .configuration import variables_to_substitute
from .files_helper import guarantee_trailing_slash, create_subfolder_structure
from .files_helper import prepare_files_and_subfolders
from .files_helper import prepare_output_path_dir, read_template


def run(variables: dict, output_path: str):
    """Runs the logic for generating rendered templates outcome

    Args:
        dir_name: str, Required
        Name of output directory
    """
    # avoids problem with concats without trailling slash
    output_path = guarantee_trailing_slash(output_path)

    # makes sure output dir exists to avoid FileNotFound error
    prepare_output_path_dir(output_path)

    file_list, subfolders, dir_size = prepare_files_and_subfolders()

    if subfolders:
        create_subfolder_structure(subfolders, output_path)

    for f in file_list:
        # makes sure I have correct file names for subfolder structure
        if dir_size == 1:
            file_name = f
            f = f'templates/{f}'
        else:
            file_name = f.split('templates/')[1]
        template = read_template(f)

        # create templates
        file_template = Template(template)
        file_name_template = Template(file_name)

        # rendering templates
        output_file_name = file_name_template.render(variables)
        output_file = file_template.render(variables)

        # writing outputs
        with open(f'{output_path}/{output_file_name}', 'w') as f:
            click.echo(f'Writting file: {output_file_name}')
            f.write(output_file)


@click.command()
@click.option('-v', '--variable-list', default='variables.yaml',
              help='Name of the yaml files containing variables')
@click.option('-o', '--output-path', default='./',
              help='Output path, by default writes to root')
def AutoGenFiles(variable_list, output_path):
    print(f'Output path: {output_path}')
    # read variables to substitute
    if not Path(variable_list).is_file():
        print(f'Oh no! No file named {variable_list} found!')
        return

    variables = variables_to_substitute(variable_list)
    if not variables:
        return
    click.echo(f'Variables found: {list(variables.keys())}')

    run(variables, output_path)
    click.echo('Output fully written')
