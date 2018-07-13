#! /usr/bin/env python3

import sys
import doit
from src import case_switch
from src.adapters import adapter_wc
from src.common import comm
from src import config as cf


# def task_get_switch_list():
#     return{
#         'actions': [adapter_wc.WCAdaptor.get_switch_list(cf.CASE_SWITCH_LIST_PATH)],
#         # 'file_dep':[]
#
#     }
# DOIT_CONFIG = {
#     'default_tasks':['get_wc_folder_name'],
# }

def task_case_runner():
    indicator = cf.CASE_SWITCH_INDICATOR_ON
    return {
        'actions': [(case_switch.case_runner,[indicator])],
    }


def task_get_wc_folder_name():
    """get wc folder name"""
    return {
        'file_dep':[path],
        'targets': [wc_folder_names],
        'actions': [(adapter_wc.WCAdaptor.get_wc_folder_names,[cf.PROGRAM_PATH_AB_WC, short_name])],
        }




   # wc_folder_names = WCAdaptor.get_wc_folder_names(cf.PROGRAM_PATH_AB_WC, short_name)
   #
   #          # execute wc programs and get their outputs
   #          out_path_list = WCAdaptor.get_output(wc_folder_names, key, new_input_dic[key], short_name)
   #
   #          # get normalised output
   #          normalised_output_file_list= WCAdaptor.wc_output_normaliser(out_path_list, key, short_name)
   #
   #          # compare their outputs
   #          group_list, file_num, case_num, out_list = comm.compare_outputs(normalised_output_file_list)
   #
   #          # vote for majority
   #          comm.count_voting(group_list, file_num, case_num, short_name)


if __name__ == '__main__':
    doit.run(globals())







