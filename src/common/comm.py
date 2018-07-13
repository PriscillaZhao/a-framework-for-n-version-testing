import os
import sys
import time
import logging
import platform
import hashlib
from subprocess import call
from pathlib import Path
from src import config as cf
from enum import Enum
from typing import TextIO
# from src.pyutils import echo, exc, fileutils


def generate_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def read_file(file_name):
    file_content = open(file_name, 'r').read()
    return file_content


def get_file_num(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for each in files:
            count += 1
    return count


def get_local_time():
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return local_time

# def getFileList(p):
#     p = str(p)
#     if p == "":
#         return []
#     p = p.replace("/", "\\")
#     print(p[-1])
#     #if p[-1] != "\\":
#     if p[-1] != "\\":
#         p = p + "\\"
#         a = os.listdir(p)
#         b = [x for x in a if os.path.isfile(p + x)]
#         return b


def get_file_list(path):
    if path == "":
        return []
    return os.listdir(path)


def get_log(text, short_name):
    local_time = get_local_time()
    log_path = generate_folder(cf.LOG_PATH / short_name)
    file_name = 'log_' + cf.SYS_NAME + '_' + local_time + '.txt'
    file = log_path / file_name
    logging.basicConfig(filename=file, level=logging.DEBUG)
    logging.info(text)


def get_short_name(file_name):
    file_name, ext_num = os.path.splitext(file_name)
    return file_name


def get_current_path():
    current_path = Path('.')
    return current_path


def generate_file(file_name, text):
    time.sleep(1)
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))
    file_content = open(file_name, 'a')
    file_content.write(text)
    file_content.write('\n')
    file_content.close()


def get_file_names(file_path):
    file_names = os.listdir(file_path)
    return file_path, file_names


def compare_outputs(out_path_list):
    # output file path list
    for out in out_path_list:
        out_list = get_file_list(out)
        # filename contains "Windows" will be appended to this list
        windows_list = []
        # filename contains "Linux" will be appended to this list
        linux_list = []
        # filename contains "Mac" will be appended to this list
        mac_list = []
        os_list = []
        for file_name in out_list:
            if "Windows" in file_name:
                windows_list.append(file_name)

            if "Linux" in file_name:
                linux_list.append(file_name)

            if "Mac" in file_name:
                mac_list.append(file_name)

        if cf.SYS_NAME == "Windows":
            os_list = windows_list
        
        if cf.SYS_NAME == "Linux":
            os_list = linux_list
        
        if cf.SYS_NAME == "Mac":
            os_list = mac_list

        group_list, file_num, case_num = classify_comparison_results(os_list, out)
        return group_list, file_num, case_num,out_list


# Classify comparision results and put the programs with same results into same list
def classify_comparison_results(os_list, out):
    out_path = Path(out)
    if len(os_list) != 0:
        file_num = len(os_list)
        content = []
        for name in os_list:
            case_num = name[0:5]
            file_name = out_path / name
            file_content = open(file_name, 'r').read()
            content.append(file_content)
        group_list = []  # two dimensional list for wc file name list
        overall_list = []  # one dimensional list for wc file name list
        for i in range(0, len(content)):
            for j in range(i + 1, len(content)):
                if content[i] == content[j]:
                    is_existing = False
                    for key, group in enumerate(group_list):
                        if i in group or j in group:
                            is_existing = True
                            if not i in group:
                                group.append(i)
                            if not j in group:
                                group.append(j)

                            group_list[key] = group
                            break

                    if not is_existing:
                        group_list.append([i, j])
        for n in group_list:
            for t in n:
                overall_list.append(t)
        for f in range(file_num):
            if f not in overall_list:
                group_list.append([f])
    else:
        print("There is no outputs for " + os_list)

    return group_list, file_num, case_num


# Comparision across operation system
def compare_across_os(outpath_list, file_num, out_list, short_name):

    if len(out_list) == file_num:
        print("Only outputs of " + cf.SYS_NAME + " exist,so currently there is no need to compare outputs across platform.")
    else:
        for out in outpath_list:
            o_list = get_file_list(out)
            list, file_num, case_num = classify_comparison_results(o_list,out)
            count_voting(list, file_num, case_num, short_name)


# vote for plurality or majority
def count_voting(group_list, file_num, case_num, short_name):
    case_num_str = str(case_num)
    file_num_str = str(file_num)
    is_majority = False
    is_plurality = False
    is_unanimous = False
    if len(group_list) == file_num:
        text = "Comparision result for " + case_num_str + ": There are " \
               + file_num_str + " wc files, their outputs are different."
        print(text)
        get_log(text,short_name)

    elif len(group_list) == 1 and len(group_list[0]) == file_num:
        is_plurality = True
        is_majority = True
        is_unanimous = True

    else:
        max_list = []
        plurality = []
        # dictionary for plurality
        plurality_dic = {}

        for i in group_list:
            if file_num == 0:
                print(cf.NO_FILE_GENERATED_MESSAGE)
                get_log(cf.NO_FILE_GENERATED_MESSAGE,short_name)
            else:
                # count the average percentage of each program
                n = 1 / file_num
                file_len = len(i)
                # count the percentage of each list in group_list[] and append to max_list[]
                per = "%.2f" % (file_len * n * 100)
                max_list.append(per)
        # find the max percentage in group_list
        max_per = max(max_list)
        k = 0
        # converge list
        con_list = []
        # split the plurality from the max_list
        for plu in max_list:
            if plu == max_per:
                plurality_dic[k] = plu
                plurality.append(plu)
                k = k + 1
            else:
                plurality_dic[k] = plu
                # plu > 0 means there is convergence except plurality
                if float(plu) > float("%.2f" % (n * 100)):
                    con_list.append(k)
                k = k + 1

        print(cf.VOTER_RESULTS_MESSAGE)
        # specify which programs are the plurality
        for k in plurality_dic:
            plus = []
            for i in group_list[k]:
                # i is from 0, but the program is from 1, so assign value of i+1 to variable a
                a = i + 1
                plus.append(a)

            print(case_num , ": Outputs of wc", plus, " are the same. They account for totally" , max_list[k] , "%")
            text = case_num, ": Outputs of wc", plus, " are the same. They account for totally", max_list[k], "%"
            get_log(text, short_name)

        if len(plurality) > 1 or len(max_list) == 0:
            is_majority = False
            is_plurality = False
            is_unanimous = False
        else:
            if float(plurality[0]) > 50.00:
                is_majority = True
                is_plurality = True
                is_unanimous = False
            else:
                is_majority = False
                is_plurality = True
                is_unanimous = False

    voting_result(is_majority, is_plurality, is_unanimous, short_name)
    for k in plurality_dic:
        plus = []
        for i in group_list[k]:
            # i is from 0, but the program is from 1, so assign value of i+1 to variable a
            a = i + 1
            plus.append(a)
        for con in con_list:
            if k == con:
                print("wc", plus, "is not plurality,but they have converged outputs")
                text = "wc", plus, "is not plurality,but they have converged outputs"
                get_log(text, short_name)
    print(cf.SPLIT_LINE)
    get_log(cf.SPLIT_LINE, short_name)


# def check_convergence(group_list):
def voting_result(is_majority, is_plurality, is_unanimous, short_name):
    # print(cf.VOTER_RESULTS_MESSAGE)
    get_log(cf.VOTER_RESULTS_MESSAGE, short_name)
    print(cf.SPLIT_LINE)
    get_log(cf.SPLIT_LINE, short_name)

    if is_unanimous is True:
        print(cf.ALL_AGREE_LINE)
        get_log(cf.ALL_AGREE_LINE, short_name)

    elif is_majority is True and is_plurality is True:
        print(cf.MAJORITY_AND_PLURALITY_LINE)
        get_log(cf.MAJORITY_AND_PLURALITY_LINE, short_name)

    elif is_majority is False and is_plurality is True:
        print(cf.PLURALITY_NOT_MAJORITY_LINE)
        get_log(cf.PLURALITY_NOT_MAJORITY_LINE, short_name)

    else:
        print(cf.NO_AGREE_LINE)
        get_log(cf.NO_AGREE_LINE, short_name)

def read_hash_file(file_name):
    hasher = hashlib.md5()
    with open(file_name, 'rb') as a_file:
        buf = a_file.read()
        print(buf)
        hasher.update(buf)
        print("hasher.hexdigest() is ",hasher.hexdigest())
        return hasher.hexdigest()

# BLOCKSIZE = 65536
# hasher = hashlib.md5()
# with open('anotherfile.txt', 'rb') as afile:
#     buf = afile.read(BLOCKSIZE)
#     while len(buf) > 0:
#         hasher.update(buf)
#         buf = afile.read(BLOCKSIZE)
# print(hasher.hexdigest())


