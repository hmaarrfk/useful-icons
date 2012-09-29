#!/bin/bash

# Following intructions at:
# http://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package
# http://fedoraproject.org/wiki/How_to_create_an_RPM_package

echo Parameters are $0 $1 $2 $3

if [ $# -ne 1 ]
then 
	echo "Must provide the package to create"
fi


topackage=$1
#topackage=matlab-icons

BASEDIR=$(dirname $0)

if [ -d "~/rpmbuild" ]; then
	echo "~/rpmbuild" exists, please remove it before attempting to build this package
fi

rpmdev-setuptree

version=`cat ${topackage}/VERSION`

mkdir -p ./BUILD

cp ${topackage}/packagers/rpm/${topackage}.spec ~/rpmbuild/SPECS/.

cp -R ${topackage} ./BUILD/${topackage}-${version}

tar czf ~/rpmbuild/SOURCES/${topackage}-${version}.tar.gz -C ./BUILD ${topackage}-${version}  

rm -rf ./BUILD/${topackage}-${version}

rpmbuild -ba ~/rpmbuild/SPECS/${topackage}.spec
