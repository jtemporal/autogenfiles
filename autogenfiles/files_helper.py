import glob

from pathlib import Path
from os import walk


def read_template(file_name: str) -> str:
    """Reads a template file and returns its content

    Args:
        file_name: str, Required
        Template file name

    Returns:
        Template file contents
    """
    return Path(file_name).read_text()


def prepare_output_path_dir(dir_name: str):
    """Creates missing directories for output files

    Args:
        dir_name: str, Required
        Name of output directory
    """
    if not Path(dir_name).is_dir():
        print(f'Creating dir named: {dir_name}')
        Path(dir_name).mkdir()


def guarantee_trailing_slash(directory_name: str) -> str:
    """
    """
    if not directory_name.endswith('/'):
        return directory_name + '/'
    return directory_name


def prepapre_files_and_subfolders(templates_dir: str = 'templates/'):
    # list files in templates
    walked = list(walk(templates_dir))
    files = walked[0][2]  # files inside templates/ and outside of subfolders
    subfolders = walked[0][1]  # always a list of subfolders
    templates_dir_quantity = walked.__len__()

    # if templates has subfolder structure this list all templates in subfold
    if templates_dir_quantity > 1:
        files = glob.glob(templates_dir + '*/*')

    return files, subfolders, templates_dir_quantity


def create_subfolder_structure(subfolders, output_path):
    """Creates subfolders inside output path

    Args:
        subfolders: list(str), Required
        A list of string cotaining templates/ subfolders names

        output_path: str, Required
        Output directory to write rendered templates
    """
    for subf in subfolders:
        prepare_output_path_dir(f'{output_path}{subf}')
