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

%description
# oneAPI Math Kernel Library (oneMKL) Interfaces
oneMKL interfaces are an open-source implementation of the oneMKL Data Parallel C++ (DPC++) interface according to the [oneMKL specification](https://spec.oneapi.com/versions/latest/elements/oneMKL/source/index.html). It works with multiple devices (backends) using device-specific libraries underneath.

%prep
%setup -q -n onemkl
cd %{_builddir}/onemkl

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621420468
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -fuse-ld=ldd -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc"
#
export CXXFLAGS="-g -fuse-ld=bfd -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc"
#
export FCFLAGS="-g -fuse-ld=ldd -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc"
export FFLAGS="-g -fuse-ld=ldd -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer"
export CFFLAGS="-g -fuse-ld=ldd -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -Wall -falign-functions=32 -fasynchronous-unwind-tables -fno-stack-protector -fno-trapping-math -feliminate-unused-debug-types -ipo -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread"
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
export CC="/aot/intel/oneapi/compiler/latest/linux/bin/clang"
source /aot/intel/oneapi/setvars.sh
## altflags1 end
%cmake .. -GNinja \
-DCMAKE_C_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/clang" \
-DCMAKE_CXX_COMPILER="/aot/intel/oneapi/compiler/latest/linux/bin/dpcpp" \
-DCMAKE_C_FLAGS="$CFLAGS" \
-DCMAKE_CXX_FLAGS="$CXXFLAGS" \
-DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" \
-DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS" \
-DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
-DBUILD_DOC:BOOL=ON \
-DMKL_ROOT=/usr \
-DREF_BLAS_ROOT=/usr \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DENABLE_MKLCPU_BACKEND:BOOL=ON \
-DENABLE_MKLGPU_BACKEND:BOOL=OFF \
-DENABLE_MKLCPU_THREAD_TBB:BOOL=ON \
-DBUILD_FUNCTIONAL_TESTS:BOOL=ON
ninja --verbose -j16
ctest -j16 --verbose --progress || :
## ccache stats
ccache -s
## ccache stats
popd

%install
export SOURCE_DATE_EPOCH=1621420468
rm -rf %{buildroot}
pushd clr-build
%ninja_install
popd

%files
%defattr(-,root,root,-)
