#!/usr/bin/env python
# coding: utf-8

import cobra
import riptide
import sys

filepath=sys.argv[1] # "/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/TSVFiles/"+site+str(i)+".tsv"

file=filepath.split("/")[-1] # site+str(i)+".tsv"
filename=file.split(".")[0] # site+str(i)

outpath=filepath.replace(file,filename) # "/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/TSVFiles/"+site+str(i)
outpath=outpath.replace("TSVFiles","RiptideOutputs") #"/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/RiptideOutputs/"+site+str(i)

model = cobra.io.read_sbml_model("/gpfs/gpfs0/scratch/vjz3qz/sp23-project/Human-GEM/model/Human-GEM.xml")
model.solver="glpk"
model.slim_optimize()

transcriptionFile=riptide.read_transcription_file(filepath)
contextualizedOutput=riptide.contextualize(model=model,transcriptome=transcriptionFile)
riptide.save_output(riptide_obj=contextualizedOutput,path=outpath)

