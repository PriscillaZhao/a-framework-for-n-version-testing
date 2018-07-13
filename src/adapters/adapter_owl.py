# _*_ coding:utf-8 _*_
import os
import shutil
from pathlib import Path
from shutil import copyfile
from src.common import comm
from subprocess import call
from src import config as cf
import xml.etree.ElementTree as et


class OWLAdaptor:

    """ An OWL Adaptor """

    def invoke_on_input(xml_file):

        """Return test suite values from xml file."""

        dictionary = {}
        new_input = {}  # dictionary for new inputs
        tree = et.parse(xml_file)
        root = tree.getroot()
        for child in root:
            dictionary[child.tag] = child.text
        for key in dictionary:
            if not dictionary[key].isspace():
                new_input[key] = dictionary[key]
            else:
                print("There is no command in " + key)
        return new_input

    def get_output(owl_folder_names, key, new_input_dic, short_name):
        """Return output after running owl programs"""

        out_path_list = []
        for owl_folder_name in owl_folder_names:
            reasoner_name, reasoner_args = OWLAdaptor.get_reasoner_name(owl_folder_name)
            try:
                if cf.SYS_NAME == cf.OS_WINDOWS:
                    command = reasoner_args + cf.SPACE + new_input_dic[key]

                elif cf.SYS_NAME == cf.OS_LINUX:
                    command = reasoner_args + cf.SPACE + new_input_dic[key]

            except ValueError:
                raise 'The system you are using now has not installed python'

            path_framework = Path('.').absolute()
            path_owl_folder = cf.PROGRAM_PATH_REL_OWL + owl_folder_name
            os.chdir(path_owl_folder)

            source_path = path_framework / path_owl_folder
            out_path = OWLAdaptor.owl_runner(command, key, short_name,reasoner_name, source_path)
            os.chdir(path_framework)

        out_path_list.append(out_path)

        return out_path_list

    # execute wc programs and generate outputs
    def owl_runner(command, key, short_name, reasoner_name, source_path):

        call(command, shell=True)
        # text = os.popen(command).read()
        # local_time = comm.get_local_time()
        sub_path = cf.OUTPUT_PATH / short_name / key / 'raw_output'
        out_path = comm.generate_folder(sub_path)
        # source_file = source_path / "output.owl"
        # file_path = os.path.join(out_path, key + '_' + sys_name + '_' + local_time + '.txt')
        # file_path = out_path / key + '_' + sys_name + '_' + local_time + '.txt'
        # output_content = open(source_file, 'r').read()
        OWLAdaptor.move_owl_output_file(source_path, reasoner_name, out_path, key)

        return out_path

    def prepare_input_file_path(input_file, owl_folder_names):
        destination_input_file_path_list = []
        for owl_folder_name in owl_folder_names:
            source_input_file_path = cf.INPUT_PATH_OWL / input_file
            destination_input_file_path = cf.PROGRAM_PATH_AB_OWL / owl_folder_name / input_file
            copyfile(source_input_file_path, destination_input_file_path)
            destination_input_file_path_list.append(destination_input_file_path)
        return destination_input_file_path_list

    def remove_input_file_path(destination_input_file_path_list):
        for destination_input_file_path in destination_input_file_path_list:
            os.remove(destination_input_file_path)

    def get_cmd_by_reasoner(reasoner_name):
        cmd = None
        if cf.SYS_NAME == cf.OS_LINUX:

            if reasoner_name == "hermit":
                cmd = cf.HERMIT_CMD_LINUX

            elif reasoner_name == "fact++":
                cmd = cf.FACT_PLUSPLUS_CMD_LINUX

            elif reasoner_name == "trowl":
                cmd = cf.TR_OWL_CMD_LINUX

            elif reasoner_name == "konclude":
                cmd = cf.KONCLUDE_CMD_LINUX

        elif cf.SYS_NAME == cf.OS_WINDOWS:
            if reasoner_name == "hermit":
                cmd = cf.HERMIT_CMD_WINDOWS
        return cmd

    def start_classification(input_file, output_file):
        owl_folder_names = OWLAdaptor.get_owl_folder_names(cf.PROGRAM_PATH_AB_OWL)
        for owl_folder_name in owl_folder_names:
            reasoner_name, reasoner_args = OWLAdaptor.get_reasoner_name(owl_folder_name)
            command = reasoner_args + cf.SPACE + 'classification' + cf.SPACE + input_file + cf.SPACE + output_file
            # framework_path = Path('.').absolute()
            # owl_folder_path = cf.PROGRAM_PATH_REL_OWL + owl_folder_name
            # os.chdir(owl_folder_path)
            # call(command, shell=True)
            # os.chdir(framework_path)
        return command

    def move_owl_output_file(source_path, reasoner_name, out_path, key):
        local_time = comm.get_local_time()
        source_file = source_path / "output.owl"
        file_name = key + '_' + cf.SYS_NAME + '_' + reasoner_name + '_' + 'raw' + '_' + local_time + '.owl'
        comm.generate_folder(out_path)
        shutil.move(source_file, out_path / file_name)

    def get_input_file(new_input_dic, key):
        arg_list = new_input_dic[key].split(' ')
        input_file = arg_list[1]
        return input_file

    def exe_process_owl(short_name, test):
        """follow the process from getting wc folders names to getting voting results"""

        print("Start " + short_name + "......")
        test_case_path = cf.TEST_FOLDER_PATH / test
        new_input_dic = OWLAdaptor.invoke_on_input(test_case_path)

        for key in new_input_dic:
            input_file = OWLAdaptor.get_input_file(new_input_dic, key)
            owl_folder_names = OWLAdaptor.get_owl_folder_names(cf.PROGRAM_PATH_AB_OWL)
            destination_input_file_path_list = OWLAdaptor.prepare_input_file_path(input_file, owl_folder_names)
            out_path_list = OWLAdaptor.get_output(owl_folder_names, key, new_input_dic, short_name)
            OWLAdaptor.remove_input_file_path(destination_input_file_path_list)


            # source_path = framework_path / owl_folder_path
            # OWLAdaptor.move_owl_output_file(source_path, reasoner_name, out_path, key)

            # prepare_input_file_path(input_file, destination_input_file_path)

            # # execute wc programs and get their outputs
            # out_path_list = OWLAdaptor.get_output(owl_folder_names, key, new_input_dic, short_name)


            # # compare their outputs
            # group_list, file_num, case_num, out_list, sys_name = comm.compare_outputs(normalised_output_file_list, sys_name)
            #
            # # vote for majority
            # comm.count_voting(group_list, file_num, case_num, short_name)

    def get_owl_folder_names(owl_path):
        """Return wc file folder names."""

        # owl_path = cf.PROGRAM_PATH_AB_OWL
        owl_folder_names = []
        owl_path, owl_names = comm.get_file_names(owl_path)
        if len(owl_names) == 0:
            print("There is no owl program in owl_reasoners folder")
        if len(owl_names) == 1:
            print("There is only one owl reasoner in owl_reasoners folder, which cannot be compared")
        for owl_name in owl_names:
            # test_list = comm.get_file_list(cf.PROGRAM_PATH_AB_OWL / owl_name)
            # if len(test_list) == 0:
            #     print("In " + short_name + ", folder " + owl_name + " has no owl program")

            if cf.SYS_NAME.lower() in owl_name.lower():
                owl_folder_names.append(owl_name)

        return owl_folder_names

    def get_reasoner_name(owl_folder_name):

        if cf.SYS_NAME == cf.OS_LINUX:
            if cf.REASONER_HERMIT in owl_folder_name:
                reasoner_name = cf.REASONER_HERMIT
                reasoner_args = cf.HERMIT_CMD_LINUX

            elif cf.REASONER_FACT_PLUS_PLUS in owl_folder_name:
                reasoner_name = cf.REASONER_FACT_PLUS_PLUS
                reasoner_args = cf.FACT_PLUSPLUS_CMD_LINUX

            elif cf.REASONER_TR_OWL in owl_folder_name:
                reasoner_name = cf.REASONER_TR_OWL
                reasoner_args = cf.TR_OWL_CMD_LINUX

            elif cf.REASONER_KONCLUDE in owl_folder_name:
                reasoner_name = cf.REASONER_KONCLUDE
                reasoner_args = cf.KONCLUDE_CMD_LINUX

        elif cf.SYS_NAME == cf.OS_WINDOWS:
            if cf.REASONER_HERMIT in owl_folder_name:
                reasoner_name = cf.REASONER_HERMIT
                reasoner_args = cf.HERMIT_CMD_WINDOWS

        return reasoner_name, reasoner_args

    def get_reasoner_args(reasoner_name):
        if cf.SYS_NAME == cf.OS_LINUX:
            if reasoner_name == cf.REASONER_HERMIT:
                reasoner_args = cf.HERMIT_CMD_LINUX

            elif reasoner_name == cf.REASONER_FACT_PLUS_PLUS:
                reasoner_args = cf.FACT_PLUSPLUS_CMD_LINUX

            elif reasoner_name == cf.REASONER_TR_OWL:
                reasoner_args = cf.TR_OWL_CMD_LINUX

            elif reasoner_name == cf.REASONER_KONCLUDE:
                reasoner_args = cf.KONCLUDE_CMD_LINUX

        elif cf.SYS_NAME == cf.OS_WINDOWS:
            if reasoner_name == cf.REASONER_HERMIT:
                reasoner_args = cf.HERMIT_CMD_WINDOWS

        return reasoner_args
