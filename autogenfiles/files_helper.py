import glob

from pathlib import Path
from os import walk

import click

from jinja2 import Template


def read_template(file_name):
    return Path(file_name).read_text()


def preparing_path_dir(dir_name):
    if not Path(dir_name).is_dir():
        print(f'Creating dir named: {dir_name}')
        Path(dir_name).mkdir()


def files(variables, output_path):
    if not output_path.endswith('/'):
        output_path = output_path + '/'

    preparing_path_dir(output_path)

    walked = list(walk('templates/'))
    files = walked[0][2]
    subfolders = walked[0][1]

    if walked.__len__() > 1:
        files = glob.glob('templates/*/*')

    if subfolders:
        for subf in subfolders:
            preparing_path_dir(f'{output_path}{subf}')

    for f in files:
        if walked.__len__() == 1:
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
