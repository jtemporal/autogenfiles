import glob
import click

from pathlib import Path
from os import walk

from jinja2 import Template


def read_template(file_name):
    return Path(file_name).read_text()


def preparing_path_dir(dir_name):
    if not Path(dir_name).is_dir():
        print(f'Creating dir named: {dir_name}')
        Path(dir_name).mkdir()


def files(variables, output_path):
    # avoids problem with concats without tralling slash
    if not output_path.endswith('/'):
        output_path = output_path + '/'

    # makes sure output dir exists to avoid FileNotFound error
    preparing_path_dir(output_path)

    # list files in templates
    walked = list(walk('templates/'))
    files = walked[0][2]  # files inside templates/ and outside of subfolders
    subfolders = walked[0][1]  # always a list of subfolders

    # if templates has subfolder structure this list all templates in subfold
    if walked.__len__() > 1:
        files = glob.glob('templates/*/*')

    # creates subfolders inside output path
    if subfolders:
        for subf in subfolders:
            preparing_path_dir(f'{output_path}{subf}')

    for f in files:
        # makes sure I have correct file names for subfolder structure
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
