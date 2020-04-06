#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF3599FF828C67298 (nisse@lysator.liu.se)
#
Name     : nettle
Version  : 3.5.1
Release  : 43
URL      : https://mirrors.kernel.org/gnu/nettle/nettle-3.5.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/nettle/nettle-3.5.1.tar.gz
Source1 : https://mirrors.kernel.org/gnu/nettle/nettle-3.5.1.tar.gz.sig
Summary  : Nettle low-level cryptographic library (symmetric algorithms)
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0+ LGPL-3.0
Requires: nettle-bin = %{version}-%{release}
Requires: nettle-info = %{version}-%{release}
Requires: nettle-lib = %{version}-%{release}
Requires: nettle-license = %{version}-%{release}
Requires: p11-kit
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gmp-dev
BuildRequires : gmp-dev32
BuildRequires : gmp-lib32
BuildRequires : openssl-dev
BuildRequires : p11-kit
BuildRequires : texinfo

%description
What is GNU Nettle? A quote from the introduction in the Nettle Manual:
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space. In most contexts, you need more than the basic
cryptographic algorithms, you also need some way to keep track of available
algorithms, their properties and variants. You often have some algorithm
selection process, often dictated by a protocol you want to implement.

And as the requirements of applications differ in subtle and not so
subtle ways, an API that fits one application well can be a pain to use
in a different context. And that is why there are so many different
cryptographic libraries around.

Nettle tries to avoid this problem by doing one thing, the low-level
crypto stuff, and providing a simple but general interface to it.
In particular, Nettle doesn't do algorithm selection. It doesn't do
memory allocation. It doesn't do any I/O.

The idea is that one can build several application and context specific
interfaces on top of Nettle, and share the code, test cases, benchmarks,
documentation, etc. Examples are the Nettle module for the Pike
language, and LSH, which both use an object-oriented abstraction on top
of the library.

%package bin
Summary: bin components for the nettle package.
Group: Binaries
Requires: nettle-license = %{version}-%{release}

%description bin
bin components for the nettle package.


%package dev
Summary: dev components for the nettle package.
Group: Development
Requires: nettle-lib = %{version}-%{release}
Requires: nettle-bin = %{version}-%{release}
Provides: nettle-devel = %{version}-%{release}
Requires: nettle = %{version}-%{release}

%description dev
dev components for the nettle package.


%package dev32
Summary: dev32 components for the nettle package.
Group: Default
Requires: nettle-lib32 = %{version}-%{release}
Requires: nettle-bin = %{version}-%{release}
Requires: nettle-dev = %{version}-%{release}

%description dev32
dev32 components for the nettle package.


%package info
Summary: info components for the nettle package.
Group: Default

%description info
info components for the nettle package.


%package lib
Summary: lib components for the nettle package.
Group: Libraries
Requires: nettle-license = %{version}-%{release}

%description lib
lib components for the nettle package.


%package lib32
Summary: lib32 components for the nettle package.
Group: Default
Requires: nettle-license = %{version}-%{release}

%description lib32
lib32 components for the nettle package.


%package license
Summary: license components for the nettle package.
Group: Default

%description license
license components for the nettle package.


%prep
%setup -q -n nettle-3.5.1
cd %{_builddir}/nettle-3.5.1
pushd ..
cp -a nettle-3.5.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573790313
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-openssl --enable-shared --enable-static  --enable-x86-aesni
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-openssl --enable-shared --enable-static  --enable-x86-aesni   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C testsuite check
make -C ../build32/testsuite check

%install
export SOURCE_DATE_EPOCH=1573790313
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nettle
cp %{_builddir}/nettle-3.5.1/COPYING.LESSERv3 %{buildroot}/usr/share/package-licenses/nettle/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/nettle-3.5.1/COPYINGv2 %{buildroot}/usr/share/package-licenses/nettle/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/nettle-3.5.1/COPYINGv3 %{buildroot}/usr/share/package-licenses/nettle/e88f6aea9379eb98a7bbea965fc7127a64b41ad9
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/nettle-hash
rm -f %{buildroot}/usr/bin/nettle-lfib-stream
rm -f %{buildroot}/usr/bin/pkcs1-conv
rm -f %{buildroot}/usr/bin/sexp-conv

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nettle-pbkdf2

%files dev
%defattr(-,root,root,-)
/usr/include/nettle/aes.h
/usr/include/nettle/arcfour.h
/usr/include/nettle/arctwo.h
/usr/include/nettle/asn1.h
/usr/include/nettle/base16.h
/usr/include/nettle/base64.h
/usr/include/nettle/bignum.h
/usr/include/nettle/blowfish.h
/usr/include/nettle/buffer.h
/usr/include/nettle/camellia.h
/usr/include/nettle/cast128.h
/usr/include/nettle/cbc.h
/usr/include/nettle/ccm.h
/usr/include/nettle/cfb.h
/usr/include/nettle/chacha-poly1305.h
/usr/include/nettle/chacha.h
/usr/include/nettle/cmac.h
/usr/include/nettle/ctr.h
/usr/include/nettle/curve25519.h
/usr/include/nettle/des.h
/usr/include/nettle/dsa-compat.h
/usr/include/nettle/dsa.h
/usr/include/nettle/eax.h
/usr/include/nettle/ecc-curve.h
/usr/include/nettle/ecc.h
/usr/include/nettle/ecdsa.h
/usr/include/nettle/eddsa.h
/usr/include/nettle/gcm.h
/usr/include/nettle/gosthash94.h
/usr/include/nettle/hkdf.h
/usr/include/nettle/hmac.h
/usr/include/nettle/knuth-lfib.h
/usr/include/nettle/macros.h
/usr/include/nettle/md2.h
/usr/include/nettle/md4.h
/usr/include/nettle/md5-compat.h
/usr/include/nettle/md5.h
/usr/include/nettle/memops.h
/usr/include/nettle/memxor.h
/usr/include/nettle/nettle-meta.h
/usr/include/nettle/nettle-types.h
/usr/include/nettle/pbkdf2.h
/usr/include/nettle/pgp.h
/usr/include/nettle/pkcs1.h
/usr/include/nettle/poly1305.h
/usr/include/nettle/pss-mgf1.h
/usr/include/nettle/pss.h
/usr/include/nettle/realloc.h
/usr/include/nettle/ripemd160.h
/usr/include/nettle/rsa.h
/usr/include/nettle/salsa20.h
/usr/include/nettle/serpent.h
/usr/include/nettle/sexp.h
/usr/include/nettle/sha.h
/usr/include/nettle/sha1.h
/usr/include/nettle/sha2.h
/usr/include/nettle/sha3.h
/usr/include/nettle/twofish.h
/usr/include/nettle/umac.h
/usr/include/nettle/version.h
/usr/include/nettle/xts.h
/usr/include/nettle/yarrow.h
/usr/lib64/libhogweed.so
/usr/lib64/libnettle.so
/usr/lib64/pkgconfig/hogweed.pc
/usr/lib64/pkgconfig/nettle.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libhogweed.so
/usr/lib32/libnettle.so
/usr/lib32/pkgconfig/32hogweed.pc
/usr/lib32/pkgconfig/32nettle.pc
/usr/lib32/pkgconfig/hogweed.pc
/usr/lib32/pkgconfig/nettle.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/nettle.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhogweed.so.5
/usr/lib64/libhogweed.so.5.0
/usr/lib64/libnettle.so.7
/usr/lib64/libnettle.so.7.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libhogweed.so.5
/usr/lib32/libhogweed.so.5.0
/usr/lib32/libnettle.so.7
/usr/lib32/libnettle.so.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nettle/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/nettle/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
/usr/share/package-licenses/nettle/e88f6aea9379eb98a7bbea965fc7127a64b41ad9
