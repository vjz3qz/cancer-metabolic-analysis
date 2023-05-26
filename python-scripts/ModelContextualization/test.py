import sys
filepath=sys.argv[1] # "/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/TSVFiles/"+site+str(i)+".tsv"
file=filepath.split("/")[-1] # site+str(i)+".tsv"
filename=file.split(".")[0] # site+str(i)
outpath=filepath.replace(file,filename) # "/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/TSVFiles/"+site+str(i)
outpath=outpath.replace("TSVFiles","RiptideOutputs") #"/gpfs/gpfs0/scratch/vjz3qz/sp23-project/NormalizedCancerData/"+site+"/RiptideOutputs/"+site+str(i)
print(filepath)
print(outpath)
