#!/usr/bin/env bash
# = Installation script for Surface Evolver with OpenGL GLUT

# Exit on error.
set -e

# Set variables.
PREFIX=~/.local
CACHE=~/.cache
VERSION=2.70

# Download and unpack the latest release tarball.
rm -rf $CACHE/evolver-$VERSION/
mkdir -p $CACHE/evolver-$VERSION/
curl --location http://facstaff.susqu.edu/brakke/evolver/downloads/evolver-$VERSION.tar.gz \
     --output $CACHE/evolver-$VERSION.tar.gz
tar -xzf $CACHE/evolver-$VERSION.tar.gz -C $CACHE/evolver-$VERSION/ 

# Compile and install. The lines 64-66 of the Makefile are uncommented to compile evolver with OpenGL GLUT graphics.
SCRIPTDIR=$PWD
cd $CACHE/evolver-$VERSION/src/
sed -i '64s|^.||' Makefile
sed -i '65s|^.||' Makefile
sed -i '66s|^.||' Makefile
make
cd ..
mkdir -p $PREFIX/bin/
mkdir -p $PREFIX/share/evolver/
mkdir -p $PREFIX/share/man/man1/
cp src/evolver $PREFIX/bin/
cp fe/* $PREFIX/share/evolver/
cp evolver.1 $PREFIX/share/man/man1/
cd $SCRIPTDIR

echo -e
echo "[NOTE]"
echo "===="
echo "At shell startup, export"
echo -e
echo "    PATH=$PREFIX/bin:\$PATH"
echo "    MANPATH=$PREFIX/share/man:\$MANPATH"
echo "    EVOLVERPATH=$PREFIX/share/evolver"
echo -e
echo "===="
