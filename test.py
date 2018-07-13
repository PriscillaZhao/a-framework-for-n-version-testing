# _*_ coding:utf-8 _*_
import jpype
from jpype import *
from pathlib import Path
from src import config as cf


if __name__ == '__main__':

    DIR = Path('.').absolute()
    # get jvm path , that is the path of jvm.dll
    jvm_path = jpype.getDefaultJVMPath()

    # jar path
    jar_path = DIR / 'lib' / 'owlapi-distribution-3.4.10.jar'
    jvm_arg = '-Djava.class.path=%s' % jar_path
    jpype.startJVM(jvm_path, jvm_arg)

    # get Java Class
    iri = jpype.JClass("org.semanticweb.owlapi.model.IRI")
    owl_manager = jpype.JClass("org.semanticweb.owlapi.apibinding.OWLManager")
    javaClass2 = jpype.JClass("org.semanticweb.owlapi.model.OWLOntologyManager")
    manager = owl_manager.createOWLOntologyManager()
    ontology = manager.createOntology(iri.create("http://org.semanticweb.ore/normalised-result-comparision-ontology"));
    input = cf.DIR / 'input.txt'
    file_n = jpype.java.io.File(input)
    print(file_n)

    # shutdown jvm
    jpype.shutdownJVM()


    # jvmPath = jpype.getDefaultJVMPath()  # 默认的JVM路径
    # print(jvmPath)
    # jpype.startJVM(jvmPath)
    # jpype.java.lang.System.out.println("hello world!")
    # jpype.java.lang.System.out.println("Hi")
    #
    # jpype.shutdownJVM()























