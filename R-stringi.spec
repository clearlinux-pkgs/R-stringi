#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-stringi
Version  : 1.4.6
Release  : 76
URL      : https://cran.r-project.org/src/contrib/stringi_1.4.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stringi_1.4.6.tar.gz
Summary  : Character String Processing Facilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause ICU MIT
Requires: R-stringi-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : pkgconfig(icu-uc)

%description
string/text processing in every locale and any native encoding. 
    Owing to the use of the 'ICU' (International Components for Unicode) 
    library, the package provides 'R' users with platform-independent functions
    known to 'Java', 'Perl', 'Python', 'PHP' and 'Ruby' programmers. Available

%package lib
Summary: lib components for the R-stringi package.
Group: Libraries

%description lib
lib components for the R-stringi package.


%prep
%setup -q -c -n stringi
cd %{_builddir}/stringi

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590012884

%install
export SOURCE_DATE_EPOCH=1590012884
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringi
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library stringi
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc stringi || :


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
/usr/lib64/R/library/stringi/libs/stringi.so
