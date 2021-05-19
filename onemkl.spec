#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : onemkl
Version  : 0.2
Release  : 1
URL      : file:///aot/build/clearlinux/packages/onemkl/onemkl-v0.2.tar.gz
Source0  : file:///aot/build/clearlinux/packages/onemkl/onemkl-v0.2.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : Sphinx
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cuda
BuildRequires : cuda-dev
BuildRequires : cuda-staticdev
BuildRequires : doxygen
BuildRequires : eigen
BuildRequires : eigen-data
BuildRequires : eigen-dev
BuildRequires : elfutils-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : graphviz
BuildRequires : hwloc
BuildRequires : hwloc-dev
BuildRequires : hwloc-extras
BuildRequires : hwloc-lib
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : llvm
BuildRequires : llvm-abi
BuildRequires : llvm-bin
BuildRequires : llvm-data
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : llvm-libexec
BuildRequires : llvm-man
BuildRequires : llvm-staticdev
BuildRequires : mesa-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : nv-codec-headers
BuildRequires : nv-codec-headers-dev
BuildRequires : nvidia
BuildRequires : nvidia-dev
BuildRequires : nvidia-lib
BuildRequires : onetbb
BuildRequires : onetbb-dev
BuildRequires : openblas
BuildRequires : openblas-dev
BuildRequires : openblas-staticdev
BuildRequires : opencl-headers
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg-dev
BuildRequires : openjpeg-staticdev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkg-config
BuildRequires : procps-ng
BuildRequires : procps-ng-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : swig
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-FindCBLAS.cmake.patch

%description
# oneAPI Math Kernel Library (oneMKL) Interfaces
oneMKL interfaces are an open-source implementation of the oneMKL Data Parallel C++ (DPC++) interface according to the [oneMKL specification](https://spec.oneapi.com/versions/latest/elements/oneMKL/source/index.html). It works with multiple devices (backends) using device-specific libraries underneath.

%prep
%setup -q -n onemkl
cd %{_builddir}/onemkl
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621434376
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fcs-profile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic -fprofile-arcs -ftest-coverage"
export CFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_GEN"
#
export CXXFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -fomit-frame-pointer -pthread $PGO_GEN"
#
export FCFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_GEN"
export FFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer $PGO_GEN"
export CFFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_GEN"
#
export LDFLAGS_GENERATE="-Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -lpthread $PGO_GEN"
## pgo use
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo"
export CFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_USE"
#
export CXXFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -fomit-frame-pointer -pthread $PGO_USE"
#
export FCFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_USE"
export FFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer $PGO_USE"
export CFFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread $PGO_USE"
#
export LDFLAGS_USE="-g -Wno-unused-function -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -funroll-loops -fasynchronous-unwind-tables -fno-stack-protector -feliminate-unused-debug-types -ipo -flto=full -flto-jobs=16 -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -lpthread $PGO_USE"
#
#export AR=/usr/bin/gcc-ar
#export RANLIB=/usr/bin/gcc-ranlib
#export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export CMAKE_MODULE_PATH="/aot/intel/oneapi/lib64/cmake/"
export CXX="/aot/intel/oneapi/compiler/latest/linux/bin/dpcpp"
export CC="/aot/intel/oneapi/compiler/latest/linux/bin/icx"
export C_INCLUDE_PATH="/usr/include/c++/11:/usr/include/c++/11/x86_64-generic-linux"
export CPLUS_INCLUDE_PATH="/usr/include/c++/11:/usr/include/c++/11/x86_64-generic-linux"
export CPATH="/usr/include/c++/11:/usr/include/c++/11/x86_64-generic-linux"
source /aot/intel/oneapi/setvars.sh
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -GNinja \
-DCMAKE_JOB_POOLS="full_jobs=16" \
-DCMAKE_JOB_POOL_COMPILE="full_jobs" \
-DCMAKE_JOB_POOL_LINK="full_jobs" \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DREF_BLAS_ROOT="/usr" \
-DCMAKE_C_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/icx" \
-DCMAKE_CXX_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/dpcpp" \
-DBUILD_DOC:BOOL=ON \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DENABLE_MKLCPU_BACKEND:BOOL=ON \
-DENABLE_MKLGPU_BACKEND:BOOL=ON \
-DENABLE_CUBLAS_BACKEND:BOOL=ON \
-DENABLE_CURAND_BACKEND:BOOL=ON \
-DENABLE_MKLCPU_THREAD_TBB:BOOL=ON \
-DBUILD_FUNCTIONAL_TESTS:BOOL=ON
ninja --verbose -j16
## ccache stats
ccache -s
## ccache stats

ctest -j8 --progress || :
llvm-profdata merge -output=default.profdata /var/tmp/pgo/
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -GNinja \
-DCMAKE_JOB_POOLS="full_jobs=16" \
-DCMAKE_JOB_POOL_COMPILE="full_jobs" \
-DCMAKE_JOB_POOL_LINK="full_jobs" \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DREF_BLAS_ROOT="/usr" \
-DCMAKE_C_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/icx" \
-DCMAKE_CXX_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/dpcpp" \
-DBUILD_DOC:BOOL=ON \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DENABLE_MKLCPU_BACKEND:BOOL=ON \
-DENABLE_MKLGPU_BACKEND:BOOL=ON \
-DENABLE_CUBLAS_BACKEND:BOOL=ON \
-DENABLE_CURAND_BACKEND:BOOL=ON \
-DENABLE_MKLCPU_THREAD_TBB:BOOL=ON \
-DBUILD_FUNCTIONAL_TESTS:BOOL=OFF
ninja --verbose -j16
## ccache stats
ccache -s
## ccache stats
fi
popd

%install
export SOURCE_DATE_EPOCH=1621434376
rm -rf %{buildroot}
pushd clr-build
%ninja_install
popd

%files
%defattr(-,root,root,-)
