#!/bin/bash
# 
# OWL Reasoner Evaluation Workshop (ORE) 2014 for Konclude
# Example reasoner executor script
# 
memlimit=`expr $2 / 1024`
echo Memory Limit: $memlimit
ulimit -Sv $memlimit
timeoutsec=`expr $1 / 1000`
timeout $timeoutsec ./Konclude -DefaultReasonerLoader +Konclude.Calculation.ProcessorCount=1 -OWLlinkBatchFileLoader +Konclude.OWLlink.CloseAfterProcessedRequest=false +Konclude.OWLlink.BlockUntilProcessedRequest=true +Konclude.OWLlink.RequestFile="ORE-config.xml" -OREBatchProcessingLoader +Konclude.ORE.OperationTask="$3" +Konclude.ORE.OntologyFile="$4" +Konclude.ORE.ResponseFile="$5" +Konclude.ORE.IRIName="$6"