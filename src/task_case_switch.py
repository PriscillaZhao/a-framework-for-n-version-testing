import config
from src.common import comm
from src.adapter import (
    adapter_owl,
    adapter_wc,
)


def task_case_runner():
    def case_runner(indicator):
        if indicator == 'ON':
            case_list = config.CASE_SWITCH_LIST
            for case in case_list:
                # test = config.TEST_FOLDER_PATH / case
                short_name = comm.get_short_name(case)
                text = case + " indicator is on"
                comm.get_log(text, short_name)
                if 'wc' in short_name:
                    adapter_wc.WCAdaptor.exe_process_wc(short_name, case)

                elif 'owl' in short_name:
                    adapter_owl.OWLAdaptor.exe_process_owl(short_name, case)

        elif indicator == 'OFF':
            test_list = comm.get_file_list(config.TEST_FOLDER_PATH)
            for test in test_list:
                short_name = comm.get_short_name(test)
                text = test + " indicator is off,all cases will be executed"
                comm.get_log(text, short_name)
                if 'wc' in short_name:
                    adapter_wc.WCAdaptor.exe_process_wc(short_name, test)
                elif 'owl' in short_name:
                    adapter_owl.OWLAdaptor.exe_process_owl(short_name, test)

    return {'actions': [case_runner],
            'indicator':[config.CASE_SWITCH_INDICATOR_ON]
        }


# above could use template design pattern