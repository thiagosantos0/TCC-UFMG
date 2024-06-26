from dotenv import load_dotenv
import os
import sys
import pytest
load_dotenv()

project_path = os.getenv('PYTHONPATH')
if project_path not in sys.path:
    sys.path.append(project_path)

file_dir = os.path.dirname(__file__)
dir_path_mock_project = os.path.join(file_dir, '..', 'mock_project/')

from ifft_core.ifft_parser import scan_files

@pytest.fixture
def setup():
    filepath = dir_path_mock_project
    return filepath

def test_content_parse_ifft(setup):
    filepath = setup
    results_dict = scan_files(filepath)
    # Getting one of the files in the projmock_project as example
    assert results_dict['file1.py'][0][0] == "#IFFT.If This is a test comment\n\nprint('Hello world!')\n\n"

def test_filepath_parse_ifft_invalid_associated_file(setup):
    filepath = setup
    results_dict = scan_files(filepath)
    #
    assert results_dict['file1.py'][0][1] == ""

def test_filelabel_parse_ifft_invalid_associated_file_label(setup):
    filepath = setup
    results_dict = scan_files(filepath)
    assert results_dict['file1.py'][0][2] == ""

def test_scan_repositoty_files(setup):
    repo_path = setup
    results_dict = scan_files(repo_path)
    files_identified = list(results_dict.keys())

    files = os.listdir(repo_path)
    python_files = [file for file in files if file.endswith('.py')]
    
    assert set(python_files) == set(files_identified)



