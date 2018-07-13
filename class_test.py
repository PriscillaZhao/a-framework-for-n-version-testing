# _*_ coding:utf-8 _*_
import jpype
from src.common import comm
import os
from shutil import copyfile
from src import config as cf
from src.owl_tests import classification
from src.owl_tests import test
from src.pyutils import logger
if __name__ == '__main__':

    data_sets = cf.DATA_SETS
    reasoners = cf.ALL
    test = test.Test(data_sets, reasoners)
    class_test = classification.ClassificationCorrectnessTest(data_sets, reasoners)
    # logger = logger.Logger("123")
    class_test.run('on_name',cf.DATA_SETS,'123',789)




















