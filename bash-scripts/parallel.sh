#!/bin/bash

basepath=`pwd`

datadir=${basepath}"/NormalizedCancerData"
scriptdir=${basepath}"/PythonScripts"

cd $datadir
sites=`ls`

# Use somesites rather than sites for testing
somesites=( "bladder" "kidney" "liver" )
#loop over all sites
#for site in ${sites[@]}; do
for site in ${somesites[@]}; do
    cd $site"/TSVFiles"
    files=`ls`
    numlist=()
    #extract the number of each file to get the list 
    for file in ${files[@]}; do
        numtsv=${file##$site} # what is ##
        number=${numtsv%%".tsv"} # what is %%
        numlist+=($number)
    done
    fullpath="${datadir}/${site}/TSVFiles"
    #sort into numerical order
    readarray -t sorted < <(printf '%s\n' "${numlist[@]}" | sort -n) 
    #generate slurm script
    echo "#!/bin/bash" >> slurm.sh
    echo "#SBATCH -t 10:00:00" >> slurm.sh
    echo "#SBATCH -A csblrivanna" >> slurm.sh
    echo "#SBATCH -p standard" >> slurm.sh
    echo "module load anaconda/2020.11-py3.8" >> slurm.sh
    echo "source activate cobra_env" >> slurm.sh
    echo "python ${scriptdir}/RunRiptide.py ${fullpath}/$site\${SLURM_ARRAY_TASK_ID}.tsv" >> slurm.sh
    #launch slurm script
    cmd="sbatch -a ${sorted[0]}-${sorted[-1]} slurm.sh"
    $cmd
    #clean up so if we run it again, it won't keep appending to slurm.sh
    rm ./slurm.sh

    #back to top of loop
    cd $datadir
done
