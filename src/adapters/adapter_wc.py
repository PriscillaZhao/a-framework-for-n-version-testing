import os
import re
import platform
import xml.etree.ElementTree as et
from src.common import comm
from subprocess import call
import src.config as cf


class WCAdaptor:

    """
        A InputAdaptor instance takes an input,run the test on target system,
        and message the result.
    """

    def invoke_on_input(xmlfile):

        """Return the commands from xml file."""

        dictionary = {}
        new_input={}  #dictionary for new inputs
        tree = et.parse(xmlfile)
        root = tree.getroot()
        for child in root:
            dictionary[child.tag] = child.text
        for key in dictionary:
            if not dictionary[key].isspace():
                new_input[key] = dictionary[key]
            else:
                print("There is no command in " + key)
        return new_input

    def get_wc_folder_names(wc_path,short_name):

        """Return wc file folder names."""

        wc_folder_list = []
        wc_path, wc_names = comm.get_file_names(wc_path)
        if len(wc_names) == 0:
            print("There is no wc program in wc_files folder")
        if len(wc_names) == 1:
            print("There is only one wc program in wc_files folder, which cannot be compared")
        for wc_name in wc_names:
            test_list = comm.get_file_list(cf.PROGRAM_PATH_AB_WC / wc_name)
            if len(test_list) == 0:
                print("In " + short_name + ", folder " + wc_name + " has no wc program")
            for i in test_list:
                s_name, ext = os.path.splitext(i)
                if ext != '.py':
                    print("The program " + i + " in folder " + wc_name + " is not python file")
                else:
                    wc_folder_list.append(wc_name)
        return wc_folder_list

    def get_output(wc_names, key, dic, short_name):

        """Return output after running wc programs"""

        out_path_list = []
        for wc_name in wc_names:
            # py_version = sys.version_info
            try:
                command = cf.PY_VERSION_CMD + cf.SPACE + cf.PROGRAM_PATH_REL_WC + wc_name + cf.WC_FILE + dic
            except ValueError:
                raise "The system you are using now has not installed python"

            raw_output_file_path = WCAdaptor.wc_runner(command, key, short_name)
            # normalised_output_file_path = WCAdaptor.output_normaliser(raw_output_file_path, key, short_name)

        out_path_list.append(raw_output_file_path)

        return out_path_list

    # execute wc programs and generate outputs
    def wc_runner(command, key, short_name):

        call(command, shell=True)
        text = os.popen(command).read()
        comm.get_log("Raw outputs:", short_name)
        comm.get_log(text,short_name)
        local_time = comm.get_local_time()
        raw_output_file_path = cf.OUTPUT_PATH / short_name / key / 'raw_output'
        comm.generate_folder(raw_output_file_path)
        raw_output_file_name = key + '_' + cf.SYS_NAME + '_' + 'raw' + '_' + local_time + '.txt'
        file_name = raw_output_file_path / raw_output_file_name
        comm.generate_file(file_name, text)
        return raw_output_file_path

    def wc_output_normaliser(out_path_list, key, short_name):

        normalised_output_file_list = []
        for out_path in out_path_list:
            normalised_output_file_path = cf.OUTPUT_PATH / short_name / key / 'normalised_output'
            raw_output_list = comm.get_file_list(out_path)
            for raw_output in raw_output_list:
                raw_output_file_name = out_path / raw_output
                # file_content = comm.read_file(raw_output_file_name)
                file_content = open(raw_output_file_name, 'r').read()
                file_content_list = file_content.split("\n")

                # generate normalised output folder
                comm.generate_folder(normalised_output_file_path)

                # normalised output file name
                normalised_output_file_name = raw_output.replace('raw', 'normalised')

                for line in file_content_list:

                    # remove leading and ending spaces
                    stripped_content = line.strip()

                    # replace several space with one
                    normalised_space_content = re.sub(r" +", " ", stripped_content)

                    # replace tab with a space
                    replaced_tab_content = re.sub(r"\t+", " ", normalised_space_content)

                    # replace several space with one
                    normalised_space_content2 = re.sub(r" +", " ", replaced_tab_content)

                    # generate normalised output file
                    file_name = normalised_output_file_path / normalised_output_file_name
                    comm.generate_file(file_name, normalised_space_content2)

                file_content = open(file_name, 'r').read()
                text = "Normalised output of program:"
                # print("Normalised output of program:")
                # print(file_content)
                comm.get_log(text, short_name)
                comm.get_log(file_content, short_name)

            normalised_output_file_list.append(normalised_output_file_path)
        return normalised_output_file_list

    def get_switch_list(xml_file):

        """Return the commands from xml file."""

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
                print("There is no test suite file in " + key)
        return new_input[key]

    def exe_process_wc(short_name, test):

        """follow the process from getting wc folders names to getting voting results"""
        
        print("Start " + short_name + "......")
        test_case_path = cf.TEST_FOLDER_PATH / test
        new_input_dic = WCAdaptor.invoke_on_input(test_case_path)
        for key in new_input_dic:
            # get wc folder names
            wc_folder_names = WCAdaptor.get_wc_folder_names(cf.PROGRAM_PATH_AB_WC, short_name)

            # execute wc programs and get their outputs
            out_path_list = WCAdaptor.get_output(wc_folder_names, key, new_input_dic[key], short_name)

            # get normalised output
            normalised_output_file_list= WCAdaptor.wc_output_normaliser(out_path_list, key, short_name)

            # compare their outputs
            group_list, file_num, case_num, out_list = comm.compare_outputs(normalised_output_file_list)

            # vote for majority
            comm.count_voting(group_list, file_num, case_num, short_name)

            # compare outputs across OS
            # comm.compareAcrossOS(outpath_list, file_num, out_list, sys_name, short_name)

