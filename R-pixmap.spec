#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pixmap
Version  : 0.4.12
Release  : 21
URL      : https://cran.r-project.org/src/contrib/pixmap_0.4-12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pixmap_0.4-12.tar.gz
Summary  : Bitmap Images / Pixel Maps
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
manipulations of bitmapped images.

%prep
%setup -q -c -n pixmap
cd %{_builddir}/pixmap

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641074281

%install
export SOURCE_DATE_EPOCH=1641074281
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pixmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pixmap
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pixmap
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pixmap || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pixmap/DESCRIPTION
/usr/lib64/R/library/pixmap/INDEX
/usr/lib64/R/library/pixmap/Meta/Rd.rds
/usr/lib64/R/library/pixmap/Meta/features.rds
/usr/lib64/R/library/pixmap/Meta/hsearch.rds
/usr/lib64/R/library/pixmap/Meta/links.rds
/usr/lib64/R/library/pixmap/Meta/nsInfo.rds
/usr/lib64/R/library/pixmap/Meta/package.rds
/usr/lib64/R/library/pixmap/NAMESPACE
/usr/lib64/R/library/pixmap/NEWS
/usr/lib64/R/library/pixmap/R/pixmap
/usr/lib64/R/library/pixmap/R/pixmap.rdb
/usr/lib64/R/library/pixmap/R/pixmap.rdx
/usr/lib64/R/library/pixmap/help/AnIndex
/usr/lib64/R/library/pixmap/help/aliases.rds
/usr/lib64/R/library/pixmap/help/paths.rds
/usr/lib64/R/library/pixmap/help/pixmap.rdb
/usr/lib64/R/library/pixmap/help/pixmap.rdx
/usr/lib64/R/library/pixmap/html/00Index.html
/usr/lib64/R/library/pixmap/html/R.css
/usr/lib64/R/library/pixmap/pictures/logo.pbm
/usr/lib64/R/library/pixmap/pictures/logo.pgm
/usr/lib64/R/library/pixmap/pictures/logo.ppm
/usr/lib64/R/library/pixmap/tests/bugs.R
/usr/lib64/R/library/pixmap/tests/logo-ex.R
