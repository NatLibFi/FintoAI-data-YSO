#!/bin/bash

repo_api_list=(
    "https://theseus.fi"
    "https://trepo.tuni.fi"
    "https://taju.uniarts.fi"
    "https://lauda.ulapland.fi"
    "https://publications.bof.fi"
    "https://osuva.uwasa.fi"
)

for repo in "${repo_api_list[@]}"; do
    # get the repo name from the URL subdomain
    repo_name=$(echo "$repo" | awk -F/ '{print $3}' | awk -F. '{print $1}')

    echo "Collecting data from $repo_name"
    python collect.py $repo > collection/$repo_name.ndjson 2> collection/$repo_name.log
done
