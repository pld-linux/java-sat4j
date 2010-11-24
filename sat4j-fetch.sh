#!/bin/sh
name=sat4j
#tag=ECLIPSE_3_6
tag=org.sat4j.pom-2.2.0
version=2.2.0
tar_name=$name-$version

rm -fr $tar_name && mkdir $tar_name
cd $tar_name

# Fetch plugins
svn co svn://svn.forge.objectweb.org/svnroot/sat4j/maven/tags/$tag .

cd -
# create archive
tar -caf $tar_name.tar.xz $tar_name
