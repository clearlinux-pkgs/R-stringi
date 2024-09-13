#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-stringi
Version  : 1.8.4
Release  : 117
URL      : https://cran.r-project.org/src/contrib/stringi_1.8.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stringi_1.8.4.tar.gz
Summary  : Fast and Portable Character String Processing Facilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-stringi-lib = %{version}-%{release}
Requires: R-stringi-license = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : pkgconfig(icu-uc)

%description
processing tools for pattern searching (e.g., with 'Java'-like regular
    expressions or the 'Unicode' collation algorithm), random string generation,
    case mapping, string transliteration, concatenation, sorting, padding,
    wrapping, Unicode normalisation, date-time formatting and parsing,
    and many more. They are fast, consistent, convenient, and -
    thanks to 'ICU' (International Components for Unicode) -
    portable across all locales and platforms. Documentation about 'stringi' is

%package lib
Summary: lib components for the R-stringi package.
Group: Libraries
Requires: R-stringi-license = %{version}-%{release}

%description lib
lib components for the R-stringi package.


%package license
Summary: license components for the R-stringi package.
Group: Default

%description license
license components for the R-stringi package.


%prep
%setup -q -n stringi
pushd ..
cp -a stringi buildavx2
popd
pushd ..
cp -a stringi buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715021820

%install
export SOURCE_DATE_EPOCH=1715021820
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-stringi
cp %{_builddir}/stringi/src/icu74/LICENSE %{buildroot}/usr/share/package-licenses/R-stringi/86358f901053b66a405e3b6b963701429987ca71 || :
cp %{_builddir}/stringi/src/icu74/data/LICENSE %{buildroot}/usr/share/package-licenses/R-stringi/084ada16bc84bd4291324f3f86d5a9c501d7c1cc || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stringi/AUTHORS
/usr/lib64/R/library/stringi/CITATION
/usr/lib64/R/library/stringi/DESCRIPTION
/usr/lib64/R/library/stringi/INDEX
/usr/lib64/R/library/stringi/LICENSE
/usr/lib64/R/library/stringi/Meta/Rd.rds
/usr/lib64/R/library/stringi/Meta/features.rds
/usr/lib64/R/library/stringi/Meta/hsearch.rds
/usr/lib64/R/library/stringi/Meta/links.rds
/usr/lib64/R/library/stringi/Meta/nsInfo.rds
/usr/lib64/R/library/stringi/Meta/package.rds
/usr/lib64/R/library/stringi/NAMESPACE
/usr/lib64/R/library/stringi/NEWS
/usr/lib64/R/library/stringi/R/stringi
/usr/lib64/R/library/stringi/R/stringi.rdb
/usr/lib64/R/library/stringi/R/stringi.rdx
/usr/lib64/R/library/stringi/help/AnIndex
/usr/lib64/R/library/stringi/help/aliases.rds
/usr/lib64/R/library/stringi/help/paths.rds
/usr/lib64/R/library/stringi/help/stringi.rdb
/usr/lib64/R/library/stringi/help/stringi.rdx
/usr/lib64/R/library/stringi/html/00Index.html
/usr/lib64/R/library/stringi/html/R.css
/usr/lib64/R/library/stringi/include/stringi.cpp
/usr/lib64/R/library/stringi/include/stringi.h

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/stringi/libs/stringi.so
/V4/usr/lib64/R/library/stringi/libs/stringi.so
/usr/lib64/R/library/stringi/libs/stringi.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-stringi/084ada16bc84bd4291324f3f86d5a9c501d7c1cc
/usr/share/package-licenses/R-stringi/86358f901053b66a405e3b6b963701429987ca71
