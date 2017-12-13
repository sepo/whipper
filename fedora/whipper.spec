%global srcname whipper
%global sum Python CD-DA ripper preferring accuracy over speed
%global desc CD ripper preferring accuracy over speed

Name:    %{srcname}
Version: 0.5.1
Release: 4%{?dist}
Summary: %{sum}
URL:     https://github.com/JoeLametta/whipper
License: GPLv3+

Source0: https://github.com/JoeLametta/%{srcname}/archive/v%{version}.tar.gz
Patch1: accuraterip-checksum.patch

BuildRequires: python2-devel python-setuptools libsndfile-devel
Requires: python2-%{srcname}

%description
%{desc}

%package -n python2-%{srcname}
Summary: %{sum}
Requires: cdparanoia cdrdao python-gobject python2-musicbrainzngs python-mutagen python-CDDB pycdio flac sox
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} 
%{desc}

%prep
%setup -q
%patch1 -p1

%build
cd src
%make_build
cd ..
%py2_build

%install
cd src
%make_install
cd ..
%py2_install

%files
%{_bindir}/whipper
%{_bindir}/accuraterip-checksum

%files -n python2-%{srcname}
%{python2_sitelib}/whipper-%{version}-py2.7.egg-info/*
%{python2_sitelib}/morituri/*
%license LICENSE
%doc README.md TODO CHANGELOG.md HACKING

%changelog
* Tue Jun 27 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-4
- Move python2 sitelib into python2 subpackage.

* Tue Apr 25 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-3
- Added license and doc macros to conform with proper best practices.

* Mon Apr 24 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-2
- Remove libsndfile dependency, rpm picks that up on build.

* Mon Apr 24 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.5.1-1
- Version 0.5.1

* Sun Jan 8 2017 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.2-1
- Version 0.4.2 released. Removal of submodule logic.

* Wed Dec 21 2016 Matthew Ruzczyk <mruszczyk17@gmail.com> - 0.4.0-3
- Fixed setup macro and patches accuraterip-checksum to the correct bin
  directory

* Wed Dec 21 2016 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.0-2
- Added forgotten python2 requirement

* Wed Dec 21 2016 Matthew Ruszczyk <mruszczyk17@gmail.com> - 0.4.0-1
- Initial RPM release
