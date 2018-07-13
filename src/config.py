import jpype
import platform
from pathlib import Path
from src.reasoners.owl import OWLReasoner
from src.owl_tests.java import JavaReasoner
from .reasoners.konclude import Konclude
from src.adapters import adapter_owl


"""Paths configuration"""

#
# wc paths
#

DIR = Path('.').absolute()
SOURCE_PATH = DIR / 'src'
DATA_PATH = DIR / 'data'
N_VERSION_PROGRAM_PATH = SOURCE_PATH / 'n_version_programs'
ADAPTER_PATH = SOURCE_PATH / 'adapters'
COMMON_PATH = SOURCE_PATH / 'common'
CONFIG_PATH = SOURCE_PATH / 'config'
TEST_FOLDER_PATH = DIR / 'test_suite'
PROGRAM_PATH_AB_WC = N_VERSION_PROGRAM_PATH / 'wc_files'  # absolute path of wc files
PROGRAM_PATH_REL_WC = 'src/n_version_programs/wc_files/'
INPUT_PATH = DATA_PATH / 'inputs'
INPUT_PATH_WC = INPUT_PATH / 'in_wc'
OUTPUT_PATH = DATA_PATH / 'outputs'
LOG_PATH = DATA_PATH / 'log'
RESULTS_DIR = DATA_PATH / 'results'
DATA_SETS = DATA_PATH / 'test.owl'

#
# owl paths
#

PROGRAM_PATH_AB_OWL = N_VERSION_PROGRAM_PATH / 'owl_reasoners'  # absolute path of wc files
PROGRAM_PATH_REL_OWL = 'src/n_version_programs/owl_reasoners/'
INPUT_PATH_OWL =  INPUT_PATH / 'in_owl'

FACT_DIR = PROGRAM_PATH_AB_OWL / 'fact++-linux'
FACT_JAR_LINUX = FACT_DIR / 'factplusplus-1.6.3.jar'
HERMIT_JAR_LINUX = PROGRAM_PATH_AB_OWL / 'hermit-linux' / 'HermiT.jar'
KONCLUDE_JAR_LINUX = PROGRAM_PATH_AB_OWL / 'konclude-linux' / 'konclude.jar'
TR_OWL_JAR_LINUX = PROGRAM_PATH_AB_OWL / 'trowl-linux' / 'TrOWLvORE2014.jar'
HERMIT_JAR_WINDOWS = PROGRAM_PATH_AB_OWL / 'hermit-windows' / 'HermiT.jar'
HERMIT_JAR_WINDOWS2 = 'HermiT.jar'


#
# reasoner wrapper(Linux)
#
CHAINSAW_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'
ELK_WRAPPER_LINUX = 'elk-ore.jar'
FACT_PLUSPLUS_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'
HERMIT_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'
JCEL_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'
JFACT_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'
KONCLUDE_WRAPPER_LINUX = '??'
MOREHERMIT_WRAPPER_LINUX = 'MOReHermiTReasonerWrapper'
TREASONER_WRAPPER_LINUX = 'TReasonerWrapper'
TR_OWL_WRAPPER_LINUX = 'OREv2ReasonerWrapper.jar'



#
# reasoner factory (Linux)
#
CHAINSAW_FACTORY_LINUX = 'uk.ac.manchester.cs.chainsaw.ChainsawReasonerFactory'
FACT_PLUSPLUS_FACTORY_LINUX = 'uk.ac.manchester.cs.factplusplus.owlapiv3.FaCTPlusPlusReasonerFactory'
HERMIT_FACTORY_LINUX = 'org.semanticweb.HermiT.Reasoner\$ReasonerFactory'
JCEL_FACTORY_LINUX = 'de.tudresden.inf.lat.jcel.owlapi.main.JcelReasonerFactory'
JFACT_FACTORY_LINUX = 'uk.ac.manchester.cs.jfact.JFactFactory'
KONCLUDE_FACTORY_LINUX = '??'
TREASONER_FACTORY_LINUX = 'TReasoner.TReasoner'
TR_OWL_FACTORY_LINUX = 'eu.trowl.owlapi3.rel.reasoner.el.RELReasonerFactory'


#
# owlapi(Linux)
#
HERMIT_API_LINUX = 'owlapi-distribution-3.4.10.jar'
HERMIT_FACTORY_LINUX = 'org.semanticweb.owlapi.io.OWLParserFactory'

#
# reasoner wrapper(Windows)
#

# HERMIT_WRAPPER_WINDOWS = 'OREv2ReasonerWrapper.jar'
# HERMIT_WRAPPER_WINDOWS = 'src/n-version-programs/owl_reasoners/OREv2ReasonerWrapper.jar'
HERMIT_WRAPPER_WINDOWS = 'OREv2ReasonerWrapper.jar'

#
# reasoner factory (Windows)
#

HERMIT_FACTORY_WINDOWS = 'org.semanticweb.HermiT.Reasoner$ReasonerFactory'

"""Variables"""

#
# wc variables
#

SPACE = ' '
SPLIT_LINE = '==========================================================================================='
ALL_AGREE_LINE = '==================================All agrees==============================================='
MAJORITY_AND_PLURALITY_LINE = 'There is  plurality and it is majority'
PLURALITY_NOT_MAJORITY_LINE = 'There is  plurality but it is not majority'
NO_AGREE_LINE = '===================================No program agrees========================================'
NO_FILE_GENERATED_MESSAGE = 'No file generated in output'
VOTER_RESULTS_MESSAGE = '===========================Voter results are as follows===================================='
WC_FILE = '/wc.py '
PATH_SEPARATOR = '/'

#
# owl variables
#

EXEC_REASONER = 'execReasoner'

"""Reasoners config"""
#
# reasoner names
#
REASONER_HERMIT = 'hermit'
REASONER_FACT_PLUS_PLUS = 'fact++'
REASONER_KONCLUDE = 'konclude'
REASONER_TR_OWL = 'trowl'

#
# timeout config
#

CLASSIFICATION_TIMEOUT = 1200.0
CONSISTENCY_TIMEOUT = 1200.0
REALISATION_TIMEOUT = 1200.0

# COMMON_VM_OPTS = ['-Xmx1024M', '-DentityExpansionLimit=1000000000']
COMMON_VM_OPTS = '-Xmx1024M'

#
# commands
#

HERMIT_CMD_LINUX = 'timeout ' + str(CLASSIFICATION_TIMEOUT) + SPACE + COMMON_VM_OPTS + ' -jar ' + HERMIT_WRAPPER_LINUX + SPACE + HERMIT_FACTORY_LINUX + SPACE
FACT_PLUSPLUS_CMD_LINUX = 'timeout ' + str(CLASSIFICATION_TIMEOUT) + ' java ' + COMMON_VM_OPTS + ' -Djava.library.path=.:./lib - ' +  FACT_PLUSPLUS_WRAPPER_LINUX + SPACE + FACT_PLUSPLUS_FACTORY_LINUX + SPACE
TR_OWL_CMD_LINUX = 'timeout ' + str(CLASSIFICATION_TIMEOUT) + SPACE + COMMON_VM_OPTS + ' -jar ' + TR_OWL_WRAPPER_LINUX + SPACE + TR_OWL_FACTORY_LINUX + SPACE
KONCLUDE_CMD_LINUX = ''

HERMIT_CMD_WINDOWS = 'java ' + COMMON_VM_OPTS + ' -cp .;lib -jar ' + HERMIT_WRAPPER_WINDOWS + SPACE + HERMIT_FACTORY_WINDOWS + SPACE
# HERMIT_CMD_WINDOWS = 'java ' + COMMON_VM_OPTS + SPACE + HERMIT_JAR_WINDOWS + SPACE + HERMIT_WRAPPER_WINDOWS + SPACE + HERMIT_FACTORY_WINDOWS + SPACE


#
# # reasoners config
# #
# HERMIT_LINUX = adapter_owl.OWLAdaptor.java_reasoner_handler('HermiT',
#                                                             HERMIT_JAR_LINUX,
#                                                             HERMIT_WRAPPER_LINUX,
#                                                             vm_opts=COMMON_VM_OPTS)
#
# HERMIT_WINDOWS = adapter_owl.OWLAdaptor.java_reasoner_handler('HermiT',
#                                                               HERMIT_JAR_WINDOWS,
#                                                               HERMIT_WRAPPER_WINDOWS,
#                                                               COMMON_VM_OPTS)
#
# FACT_PLUSPLUS_LINUX = adapter_owl.OWLAdaptor.java_reasoner_handler('Fact++',
#                                                                     FACT_JAR_LINUX,
#                                                                     FACT_PLUSPLUS_WRAPPER_LINUX,
#                                                                     COMMON_VM_OPTS + '-Djava.library.path={}'.format(FACT_DIR))
#
# TR_OWL_LINUX = adapter_owl.OWLAdaptor.java_reasoner_handler('TrOWL',
#                                                             TR_OWL_JAR_LINUX,
#                                                             TR_OWL_WRAPPER_LINUX,
#                                                             COMMON_VM_OPTS)
#
# #
#
# REASONER_LIST = [FACT_PLUSPLUS_LINUX, HERMIT_LINUX, TR_OWL_LINUX, HERMIT_WINDOWS]
"""Reasoners config namespace."""
CLASSIFICATION_TIMEOUT = 1200.0
CONSISTENCY_TIMEOUT = 1200.0
REALIZATION_TIMEOUT = 1200.0

DEFAULT_ITERATIONS = 5
COMMON_VM_OPTS = ['-Xmx16g', '-DentityExpansionLimit=1000000000']

HERMIT_LINUX = JavaReasoner('HermiT', HERMIT_JAR_LINUX, HERMIT_WRAPPER_LINUX, COMMON_VM_OPTS)

HERMIT_WINDOWS = JavaReasoner('HermiT', HERMIT_JAR_WINDOWS, HERMIT_WRAPPER_WINDOWS, COMMON_VM_OPTS)

# FACT_PLUSPLUS_LINUX = JavaReasoner('Fact++', FACT_JAR_LINUX, FACT_PLUSPLUS_WRAPPER_LINUX, COMMON_VM_OPTS + '-Djava.library.path={}'.format(FACT_DIR))

TR_OWL_LINUX = JavaReasoner('TrOWL', TR_OWL_JAR_LINUX, TR_OWL_WRAPPER_LINUX, COMMON_VM_OPTS)

# KONCLUDE = Konclude(path=Paths.KONCLUDE, owl_tool_path=Paths.OWLTOOL, vm_opts=COMMON_VM_OPTS)

# REFERENCE = KONCLUDE

ALL = [HERMIT_LINUX, TR_OWL_LINUX, HERMIT_WINDOWS]

"""Reasoning tasks"""
REASONING_TASK_CLASSIFICATION = 'classification'
REASONING_TASK_CONSISTENCY = 'consistency'
REASONING_TASK_REALISATION = 'realisation'
REASONING_TASK_SATISFIABILITY = 'satisfiability'
REASONING_TASK_ENTAILMENT = 'entailment'

"""Java classes"""
OWL_MANAGER = "org.semanticweb.owlapi.apibinding.OWLManager"
FILE_DOC_SRC = "org.semanticweb.owlapi.io.FileDocumentSource"
OWL_XML_ONTO_FORMAT = "org.semanticweb.owlapi.io.OWLXMLOntologyFormat"

AXIOM_TYPE = "org.semanticweb.owlapi.model.AxiomType"
IRI = "org.semanticweb.owlapi.model.IRI"
MISSING_IMPORT_HANDLING_STRATEGY = "org.semanticweb.owlapi.model.MissingImportHandlingStrategy"
OWL_AXIOM = "org.semanticweb.owlapi.model.OWLAxiom"
OWL_ClASS = "org.semanticweb.owlapi.model.OWLClass"

OWL_ClASS_ASSERTION_AXIOM = "org.semanticweb.owlapi.model.OWLClassAssertionAxiom"
OWL_CLASS_EXPRESSION = "org.semanticweb.owlapi.model.OWLClassExpression"
OWL_DATA_FACTORY = "org.semanticweb.owlapi.model.OWLDataFactory"
OWL_EQUIVALENT_CLASSES_AXIOM = "org.semanticweb.owlapi.model.OWLEquivalentClassesAxiom"
OWL_NAMED_INDIVIDUAL = "org.semanticweb.owlapi.model.OWLNamedIndividual"

OWL_ONTOLOGY = "org.semanticweb.owlapi.model.OWLOntology"
OWL_ONTOLOGY_CREATION_EXCEPTION = "org.semanticweb.owlapi.model.OWLOntologyCreationException"
OWL_ONTOLOGY_FORMAT = "org.semanticweb.owlapi.model.OWLOntologyFormat"
OWL_ONTOLOGY_LOADER_CONFIGURATION = "org.semanticweb.owlapi.model.OWLOntologyLoaderConfiguration"
OWL_ONTOLOGY_MANAGER = "org.semanticweb.owlapi.model.OWLOntologyManager"
OWL_SUB_ClASS_Of_AXIOM = "org.semanticweb.owlapi.model.OWLSubClassOfAxiom"

"""Jar path"""

JVM_PATH = jpype.getDefaultJVMPath()
OWL_API_JAR_PATH = DIR / 'lib' / 'owlapi-distribution-3.4.10.jar'
JVM_ARG = '-Djava.class.path=%s' % OWL_API_JAR_PATH

#
# common configuration
#
"""OS platform"""
OS_WINDOWS = 'Windows'
OS_LINUX = 'Linux'

"""Python version"""
PY_VERSION_CMD = 'python'

"""System name"""
SYS_NAME = platform.system()

"""Case switch indicator"""
# ON means only cases in CASE_SWITCH_LIST can be selected to execute
CASE_SWITCH_INDICATOR_ON = 'ON'

# OFF means ALL cases in test_suite can be executed.
CASE_SWITCH_INDICATOR_OFF = 'OFF'

"""Case switch list"""
CASE_SWITCH_LIST_PATH = DATA_PATH / 'case_switch_list' / 'case_switch_list.xml'
CASE_SWITCH_LIST = ['owl_test1.xml']

HELLO_PATH = DATA_PATH / 'hello.txt'