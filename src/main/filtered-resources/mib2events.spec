%define rel 1
%define version ${project.version}

Name: mib2events
Version: %{version}
Release: %{rel}
License: GPL
Group: Applications/System
Summary: Generate OpenNMS Events from MIB Traps
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Obsoletes: mib2opennms

%description
A tool to generate OpenNMS events from MIB traps.

%prep
%setup -n %{name}-%{version}-source

%build
#mvn package

%install
exit 1

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
	rm -rf "$RPM_BUILD_ROOT"
fi

%files
%attr(755,root,root) %{_bindir}/*

%changelog
* Fri Aug 10 2012 Benjamin Reed <ranger@opennms.org>
- initial package
