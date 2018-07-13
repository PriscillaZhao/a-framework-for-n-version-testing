# _*_ coding:utf-8 _*_
import jpype
from src.common import comm
import os
from shutil import copyfile
from src import config as cf


if __name__ == '__main__':
    source_input_file_path = cf.INPUT_PATH_OWL / 'test.owl'
    print(source_input_file_path)
    destination_input_file_path = cf.PROGRAM_PATH_AB_OWL / 'hermit-windows'/ 'test.owl'
    print(destination_input_file_path)
    copyfile(source_input_file_path, destination_input_file_path)




















