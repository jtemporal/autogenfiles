import glob

from pathlib import Path
import click

from jinja2 import Template


def read_template(file_name):
    return Path(file_name).read_text()


def files(variables, output_path):
    files = glob.glob('templates/*/*')
    # subfolders = [p.split('templates/')[1] for p in glob.glob('templates/*')]

    for f in files:
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
