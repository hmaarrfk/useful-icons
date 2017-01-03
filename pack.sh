#!/bin/sh


the_package=matlab-icons

if [ "$#" -ge 1 ]; then
    the_package=$1
fi

echo $the_package

rpmdev-setuptree
#rm -rf ~/rpmbuild/SOURCES/*
#rmdir ~/rpmbuild/SOURCES
ln -sfr -T $the_package ~/rpmbuild/SOURCES

spectool -g ${the_package}/*.spec -C ${the_package}

rpmbuild -bs ~/rpmbuild/SOURCES/*.spec
