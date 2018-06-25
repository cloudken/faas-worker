#!/bin/bash -x

# input
if [ $# -ne 1 ]; then
    echo "usage: ./build_allpkgs.sh src_path"
    exit 1
fi
src_path=$1
build_path=`pwd`

./build_pkg.sh faas-worker $src_path $build_path faas-worker
