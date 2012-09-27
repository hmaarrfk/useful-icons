#!/bin/bash

# Following intructions at:
# http://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package
# http://fedoraproject.org/wiki/How_to_create_an_RPM_package
BASEDIR=$(dirname $0)

if [ -d "~/rpmbuild" ]; then
	echo "~/rpmbuild" exists, please remove it before attempting to build this package
fi

rpmdev-setuptree

topackage=matlab-icons
version=`cat ${topackage}/VERSION`

mkdir -p ./BUILD

cp ${topackage}/packagers/rpm/${topackage}.spec ~/rpmbuild/SPECS/.

cp -R ${topackage} ./BUILD/${topackage}-${version}

tar czf ~/rpmbuild/SOURCES/${topackage}-${version}.tar.gz -C ./BUILD ${topackage}-${version}  

rm -rf ./BUILD/${topackage}-${version}

rpmbuild -ba ~/rpmbuild/SPECS/matlab-icons.spec
