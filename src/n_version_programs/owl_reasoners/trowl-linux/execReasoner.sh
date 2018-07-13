#!/bin/bash
# 
# OWL Reasoner Evaluation Workshop (ORE) 2013
# Example reasoner executor script
# Last updated: 27-Mar-13
# 
# java -jar OREv2ReasonerWrapper.jar eu.trowl.owl.api3.ReasonerFactory $*
# java -jar OREv2ReasonerWrapper.jar eu.trowl.owl.api3.Reasoner $*
# java -jar OREv2ReasonerWrapper.jar trowl.LoadTool $*
# java -jar OREv2ReasonerWrapper.jar eu.trowl.owl.api3.TrOWLReasonerFactory $*
timeoutsec=`expr $1 / 1000`
timeout $timeoutsec java -Xmx$2 -jar OREv2ReasonerWrapper.jar eu.trowl.owlapi3.rel.reasoner.el.RELReasonerFactory $3 $4 $5 $6 $7 $8 $9

