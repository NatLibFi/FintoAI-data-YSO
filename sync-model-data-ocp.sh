#!/bin/bash

# Runs rsync to transfer model data from the current directory to an OpenShift volume
# that is attached to a pod which is running Annif. The instance
# {api-annif-org,ai-finto-fi, etc.} to transfer to is given as the argument.
# You need to be logged to the cluster with the oc tool.

set -e

if [ $# -ne 1 ]
  then
    echo "Not enough arguments; argument 1: destination_instance"
    exit 1
fi

pod=$(oc get pods -l app.kubernetes.io/instance=$1,app.kubernetes.io/name=annif -o name)

if [[ $pod = *[[:space:]]* ]]
  then
    echo "Multiple pod exists; using first"
    pod=(${pod//$'\n'/ })
fi
echo "Target is "$pod
pod=${pod#pod/}
if [ -z "${pod}" ]
  then
    echo "No target pod found"
    exit 1
fi

rsync --rsh='oc rsh' -avrL --exclude="*train*" --exclude="*zip" --inplace projects.d $pod:/annif-projects
rsync --rsh='oc rsh' -avrL --exclude="*train*" --exclude="*zip" --inplace data/{projects,vocabs} $pod:/annif-projects/data
