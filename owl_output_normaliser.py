# _*_ coding:utf-8 _*_
import jpype
from pathlib import Path
from src import config as cf
from src.common import comm
from src.adapters import adapter_owl


def start_jvm():
    jpype.startJVM(cf.JVM_PATH, cf.JVM_ARG)


def shutdown_jvm():
    jpype.shutdownJVM()


def get_class_instance(class_name):
    class_instance = jpype.JClass(class_name)
    return class_instance

    # # 获得默认jvm路径，即jvm.dll文件路径
    # # jvm_path = jpype.getDefaultJVMPath()
    #
    # # jar path
    # # jar_path = cf.DIR / 'lib' / 'owlapi-distribution-3.4.10.jar'
    # # jvm_arg = '-Djava.class.path=%s' % jar_path
    # start_jvm()
    #
    # # 获取相应的Java类
    # owl_manager = jpype.JClass(cf.OWL_MANAGER)
    # file_doc_src = jpype.JClass(cf.FILE_DOC_SRC)
    # owl_xml_onto_format = jpype.JClass(cf.OWL_XML_ONTO_FORMAT)
    #
    # axiom_type = jpype.JClass(cf.AXIOM_TYPE)
    # iri = jpype.JClass(cf.IRI)
    # missing_import_handling_strategy = jpype.JClass(cf.MISSING_IMPORT_HANDLING_STRATEGY)
    # owl_axiom = jpype.JClass(cf.OWL_AXIOM)
    # owl_class = jpype.JClass(cf.OWL_CLASS)
    #
    # owl_class_assertion_axiom = jpype.JClass(cf.OWL_ClASS_ASSERTION_AXIOM)
    # owl_class_expression = jpype.JClass(cf.OWL_CLASS_EXPRESSION)
    # owl_data_factory = jpype.JClass(cf.OWL_DATA_FACTORY)
    # owl_equivalent_classes_axiom = jpype.JClass(cf.OWL_EQUIVALENT_ClASS_AXIOM)
    # owl_named_individual = jpype.JClass(cf.OWL_NAMED_INDIVIDUAL)
    #
    # owl_ontology = jpype.JClass(cf.OWL_ONTOLOGY)
    # owl_ontology_creation_exception = jpype.JClass(cf.OWL_ONTOLOGY_CREATION_EXCEPTION)
    # owl_ontology_format = jpype.JClass(cf.OWL_ONTOLOGY_FORMAT)
    # owl_ontology_loader_configuration = jpype.JClass(cf.OWL_ONTOLOGY_LOADER_CONFIGURATION)
    # owl_ontology_manager = jpype.JClass(cf.OWL_ONTOLOGY_MANAGER)
    # owl_sub_class_of_axiom = jpype.JClass(cf.OWL_SUB_ClASS_Of_AXIOM)
    #
    #
    # # 关闭jvm
    # # jpype.shutdownJVM()
    # shutdown_jvm()


def get_normalised_output(output_path_list, key, short_name,reasoning_task):
    start_jvm()
    normalised_output_file_list = []
    for out_path in output_path_list:
        raw_output_list = comm.get_file_list(out_path)
        normalised_output_file_path = cf.OUTPUT_PATH / short_name / key / 'normalised_output'
        for raw_output in raw_output_list:
            raw_output_file_name = out_path / raw_output
            file_content = open(raw_output_file_name, 'r').read()
            file_content_list = file_content.split("\n")

            # generate normalised output folder
            comm.generate_folder(normalised_output_file_path)

            # normalised output file name
            normalised_output_file_name = raw_output.replace('raw', 'normalised')

            owl_manager = get_class_instance(cf.OWL_MANAGER)
            owl_ontology_manager = owl_manager.createOWLOntologyManager()
            iri = get_class_instance(cf.IRI)
            ontology = owl_ontology_manager.createOntology(iri.create("http://org.semanticweb.ore/normalised-result-comparision-ontology"))

            if reasoning_task == cf.REASONING_TASK_CLASSIFICATION:
                load_classification_result_data(ontology)

            elif reasoning_task == cf.REASONING_TASK_CONSISTENCY:
                load_classification_result_data(ontology)

            elif reasoning_task == cf.REASONING_TASK_REALISATION:
                load_classification_result_data(ontology)

            elif reasoning_task == cf.REASONING_TASK_SATISFIABILITY:
                load_classification_result_data(ontology)

            elif reasoning_task == cf.REASONING_TASK_ENTAILMENT:
                load_classification_result_data(ontology)
    shutdown_jvm()
    return normalised_output_file_list


def load_classification_result_data(ontology):

    owl_ontology_manager = ontology.getOWLOntologyManager()
    owl_data_factory = owl_ontology_manager.getOWLDataFactory()
    top_class = owl_data_factory.getOWLThing()
    bottom_class = owl_data_factory.getOWLNothing()

    try:

        owl_manager = get_class_instance(cf.OWL_MANAGER)
        # create owl ontology manager
        created_owl_ontology_manager = owl_manager.createOWLOntologyManager()
        owl_ontology_loader_configuration = get_class_instance(cf.OWL_ONTOLOGY_LOADER_CONFIGURATION)

        # owl_ontology_loader_configuration2 = owl_ontology_loader_configuration.setLoadAnnotationAxioms('false')
        # owl_ontology_loader_configuration.setMissingImportHandlingStrategy(MissingImportHandlingStrategy.SILENT)
        ontology.getAxioms()



    except ValueError:
        raise "The system you are using now has not installed python"



# if __name__ == '__main__':
#     # jpype.startJVM(jvm_path, jvm_arg)
#     # owl_manager = jpype.JClass(cf.OWL_MANAGER)
#     # manager = owl_manager.createOWLOntologyManager()
#     # iri = jpype.JClass(cf.IRI)
#     # ontology = manager.createOntology(
#     #     iri.create("http://org.semanticweb.ore/normalised-result-comparision-ontology"))
#     #
#     # print(ontology)
#     # # 关闭jvm
#     # jpype.shutdownJVM()
#     get_normalised_output(raw_output_path_list, key, short_name, reasoning_task)





