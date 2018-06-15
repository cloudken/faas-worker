#!/bin/bash -x

# input
if [ $# -ne 1 ]; then
    echo "usage: ./build_rf-base.sh src_dir"
    exit 1
fi
pkg_dir=`pwd`/rf-base
src_dir=$1
bd_dir=`pwd`
pkg_tar="rf-base.tar"
ver=`date +%Y%m%d`

# make pack
./build_pkg.sh rf-base $src_dir $bd_dir base-build
docker run -v $pkg_dir:/root/cf --name rf-base -d rf-base:$ver
sleep 120
#rm -f $pkg_dir/$pkg_tar
docker rm -f rf-base
