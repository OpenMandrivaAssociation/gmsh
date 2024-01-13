#!/bin/sh
curl -L "http://gmsh.info//src/" 2>/dev/null |sed -ne 's,.*>gmsh-\(.*\)-source.*,\1,p' | sed -e '/git/d' -e '/stable/d;' |tail -n1

