import shutil

import pytest

from pathlib import Path

from autogenfiles.files_helper import *


@pytest.fixture
def template_content():
    content = """---\nlayout: post\ntitle: '#{{ project_number }} {{ project_title }}'\nimage: "/assets/img/projects/{{ project_number }}/thumbnail.jpg"\n---\n\n<img src="/assets/img/projects/{{ project_number }}/full.jpg">"""  # noqa
    return content


@pytest.fixture
def erase_dir(dir_path):
    shutil.rmtree(dir_path)


def test_read_template_return_text_content(template_content):
    text = read_template('tests/fixtures/templates/{{ project_name }}.md')
    assert text == template_content


def test_prepare_output_path_dir_creates_new_dir():
    prepare_output_path_dir('tests/fixtures/test_output')
    assert Path('tests/fixtures/test_output').is_dir()
    shutil.rmtree('tests/fixtures/test_output')


def test_guarantee_trailing_slash_does_nothing_when_slash_present():
    result = guarantee_trailing_slash('test/')
    assert result == 'test/'


def test_guarantee_trailing_slash_adds_slash_when_no_slash_present():
    result = guarantee_trailing_slash('test')
    assert result == 'test/'


def test_prepapre_files_and_subfolders():
    result = prepapre_files_and_subfolders('tests/fixtures/templates')
    res_files, res_subf, res_template_qtd = result
    assert res_files == ['{{ project_name }}.md']
    assert res_subf == []
    assert res_template_qtd == 1


def test_create_subfolder_structure():
    subf = ['temp2_subdir']
    out_path = 'tests/fixtures/'
    create_subfolder_structure(subf, out_path)
    assert Path('tests/fixtures/temp2_subdir').is_dir()
    shutil.rmtree('tests/fixtures/temp2_subdir')
