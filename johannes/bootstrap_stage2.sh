#!/bin/bash
# stage2 script for bootstrapping johannes DeVIDE build system
# this will build and install python in the johannes working directory
# copyright cpbotha.net


# change this to 0 if you DON'T want this script to do its
# rudimentary dependency checking.
TEST_DEPS=1

if [ -z $1 ]; then
echo "Specify working directory as first parameter."
exit;
fi

FLAG_FILE1=$1/flags/stage1_complete

p=$1/inst/python/bin/python
if [ -f $p ]; then
echo "It seems that bootstrap_stage2.sh has already executed."
echo "If you want to run it again, delete $p."
exit
fi

if [ ! -f $FLAG_FILE1 ]; then
echo "You have to run bootstrap_stage1.sh before you run stage2."
exit
fi


cd $1
WD=`pwd`

if [ "$TEST_DEPS" -ne 0 ]; then

echo "JOHANNES ##### testing dependencies.  Edit this script and "
echo "               set TEST_DEPS to 0 to disable this."

# test whether gcc and bz2 are available
DEPS_TEST_FN=dtest.c

cat > $DEPS_TEST_FN << EOF
#include <bzlib.h>
#include <sqlite3.h>
#include <ncurses.h>
#include <readline/readline.h>
#include <gtk/gtkversion.h>
#include <ft2build.h>
#include <png.h>
#include <zlib.h>
#include <X11/Intrinsic.h>
#include <GL/glu.h>
int main(void) {}
EOF

cc -I/usr/include/gtk-2.0 -I/usr/include/freetype2 -o dtest $DEPS_TEST_FN

if [ "$?" -ne "0" ]; then
    rm -f dtest*
cat << EOF
JOHANNES ##### cc (compiler) or necessary headers not found.
See error above.  Please fix and try again.

* See the johannes README.txt for more details on which packages to
  install, and also for correct apt-get invocation to install them all
  on for example Debian / Ubuntu.
EOF
    exit
fi

# test whether g++ is available
echo "int main(void) {}" > cpptest.cc 
c++ -o cpptest cpptest.cc
if [ "$?" -ne "0" ]; then
    rm -f cpptest*
    echo "JOHANNES ##### c++ (compiler) not found."
    echo "Please fix and try again."
    exit
fi

echo ">>>>> Dependency checking successful."

# end of if [ "$TEST_DEPS" ...
fi


cd build
tar xjvf ../archive/Python-2.6.2.tar.bz2
cd Python-2.6.2
./configure --enable-shared --prefix=$WD/inst/python

if [ "$?" -ne "0" ]; then
echo "JOHANNES ##### Python config error.  Please fix errors and try again."
exit
fi

make
make install

if [ "$?" -ne "0" ]; then
echo "JOHANNES ##### Python build error.  Please fix errors and try again."
exit
fi

cd $WD

ENV_FILE=python_setup_env.sh
echo "#!/bin/sh" > $ENV_FILE
echo "export LD_LIBRARY_PATH=$WD/inst/python/lib" >> $ENV_FILE
echo "export PATH=$WD/inst/python/bin/:\$PATH" >> $ENV_FILE

echo "JOHANNES #####"
echo "Successfully built Python.  Start the build system with "
echo ". $WD/$ENV_FILE"
echo "$WD/inst/python/bin/python johannes.py -w $WD"

cd flags
touch stage2_complete
cd $WD
