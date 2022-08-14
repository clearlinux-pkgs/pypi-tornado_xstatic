#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tornado_xstatic
Version  : 0.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/8d/85/368b4f9ad0708e9a56a35903d5fbd43473dc1f69bab7bbbe342f3808adb4/tornado_xstatic-0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/85/368b4f9ad0708e9a56a35903d5fbd43473dc1f69bab7bbbe342f3808adb4/tornado_xstatic-0.3.tar.gz
Summary  : Utilities for using XStatic in Tornado applications
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-tornado_xstatic-license = %{version}-%{release}
Requires: pypi-tornado_xstatic-python = %{version}-%{release}
Requires: pypi-tornado_xstatic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
Utilities for using XStatic in Tornado applications
---------------------------------------------------

%package license
Summary: license components for the pypi-tornado_xstatic package.
Group: Default

%description license
license components for the pypi-tornado_xstatic package.


%package python
Summary: python components for the pypi-tornado_xstatic package.
Group: Default
Requires: pypi-tornado_xstatic-python3 = %{version}-%{release}

%description python
python components for the pypi-tornado_xstatic package.


%package python3
Summary: python3 components for the pypi-tornado_xstatic package.
Group: Default
Requires: python3-core
Provides: pypi(tornado_xstatic)
Requires: pypi(tornado)

%description python3
python3 components for the pypi-tornado_xstatic package.


%prep
%setup -q -n tornado_xstatic-0.3
cd %{_builddir}/tornado_xstatic-0.3
pushd ..
cp -a tornado_xstatic-0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656367630
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tornado_xstatic
cp %{_builddir}/tornado_xstatic-0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tornado_xstatic/cd09ea989ddb8ad337dc0b791fed46934a50c36c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tornado_xstatic/cd09ea989ddb8ad337dc0b791fed46934a50c36c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
