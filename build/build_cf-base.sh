#!/bin/bash -x

# input
if [ $# -ne 1 ]; then
    echo "usage: ./build_cf-base.sh src_dir"
    exit 1
fi
pkg_dir=`pwd`/cf-base
src_dir=$1
bd_dir=`pwd`
pkg_tar="cf-base.tar"
ver=`date +%Y%m%d`

# make pack
./build_pkg.sh cf-base $src_dir $bd_dir base-build
docker run -v $pkg_dir:/root/cf --name cf-base -d cf-base:$ver
sleep 90
#rm -f $pkg_dir/$pkg_tar
docker rm -f cf-base
