#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : systemd-bootchart
Version  : 233
Release  : 26
URL      : https://github.com/systemd/systemd-bootchart/releases/download/v233/systemd-bootchart-233.tar.xz
Source0  : https://github.com/systemd/systemd-bootchart/releases/download/v233/systemd-bootchart-233.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: systemd-bootchart-config
Requires: systemd-bootchart-doc
BuildRequires : docbook-xml
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libsystemd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0002-bootchart-drop-log_info-spam-to-serial-console.patch
Patch2: 0003-Do-not-use-urandom-during-boot.patch
Patch3: 0005-Mount-proc-early-during-boot.patch
Patch4: 0006-Delay-writing-out-the-chart-result.patch
Patch5: 0007-Show-the-cmdline-by-default.patch
Patch6: 0008-Prevent-null-deref-detecting-idle.patch

%description
For systemd-bootchart, several proc debug interfaces are required in the kernel config:
CONFIG_SCHEDSTATS
below is optional, for additional info:
CONFIG_SCHED_DEBUG

%package config
Summary: config components for the systemd-bootchart package.
Group: Default

%description config
config components for the systemd-bootchart package.


%package doc
Summary: doc components for the systemd-bootchart package.
Group: Documentation

%description doc
doc components for the systemd-bootchart package.


%package extras
Summary: extras components for the systemd-bootchart package.
Group: Default

%description extras
extras components for the systemd-bootchart package.


%prep
%setup -q -n systemd-bootchart-233
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508443723
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1508443723
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/systemd-bootchart.service
/usr/lib/systemd/systemd-bootchart

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/systemd-bootchart.service
