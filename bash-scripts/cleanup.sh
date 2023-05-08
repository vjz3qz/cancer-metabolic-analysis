#!/bin/bash

basepath=`pwd`

datadir=${basepath}"/NormalizedCancerData"
scriptdir=${basepath}"/PythonScripts"

cd $datadir
sites=`ls`

for site in ${sites[@]}; do
    cd $site"/TSVFiles"
    files=`ls slurm*out`
    for file in ${files[@]}; do
        rm $file
    done
    cd ../.. 
done
