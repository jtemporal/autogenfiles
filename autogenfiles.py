from configparser import ConfigParser
from pathlib import Path

import click

from jinja2 import Template


def variables_to_substitute(variable_list):
    parser = ConfigParser()
    parser.read(variable_list)

    return dict(parser['variables'])


def read_template(file_name):
    return Path(file_name).read_text()


@click.command()
@click.option('-v', '--variable-list', default='variables.yaml',
              help='Name of the yaml files containing varibales')
def main(variable_list):

    # read variables to substitute
    variables = variables_to_substitute(variable_list)
    click.echo(f'Variables found: {variables.keys()}')

    # prepare templates
    # TODO: find automagically file names and reproduce file structure
    file_name = '{{ project_number }}.md'
    template = read_template(f'templates/{file_name}')

    # create templates
    file_template = Template(template)
    file_name_template = Template(file_name)
    click.echo('Templates created')

    # rendered file and file name
    output_file_name = file_name_template.render(variables)
    output_file = file_template.render(variables)

    # writing outputs
    with open(f'rendered/{output_file_name}', 'w') as f:
        f.write(output_file)
    click.echo('Output written')


if __name__ == '__main__':
    main()
