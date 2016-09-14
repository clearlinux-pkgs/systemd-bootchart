Name     : systemd-bootchart
Version  : 231
Release  : 8
URL      : https://github.com/systemd/systemd-bootchart/releases/download/v231/systemd-bootchart-230.tar.xz
Source0  : https://github.com/systemd/systemd-bootchart/releases/download/v231/systemd-bootchart-231.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: systemd-bootchart-bin
Requires: systemd-bootchart-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : intltool
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libsystemd)
Patch1: 0001-systemd-bootchart-dont-use-gold.patch
Patch2: 0002-bootchart-use-ms-units-in-a-few-places.patch
Patch4: 0004-bootchart-fix-per-cpu-small-scales.patch
Patch5: 0005-bootchart-drop-log_info-spam-to-serial-console.patch
Patch6: 0006-no-dev-urandom.patch
Patch7: 0007-no-libsystemd.patch
Patch8: wait-one-second.patch
Patch9: mountproc.patch

%description
For systemd-bootchart, several proc debug interfaces are required in the kernel config:
CONFIG_SCHEDSTATS
CONFIG_SCHED_DEBUG

%package bin
Summary: bin components for the systemd-bootchart package.
Group: Default

%description bin
bin components for the systemd-bootchart package.


%package doc
Summary: doc components for the systemd-bootchart package.
Group: Documentation

%description doc
doc components for the systemd-bootchart package.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/systemd-bootchart.service

%files bin
%defattr(-,root,root,-)
/usr/lib/systemd/systemd-bootchart

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
