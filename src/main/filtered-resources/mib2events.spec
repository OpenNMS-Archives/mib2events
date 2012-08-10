%define rel 1
%define version ${project.version}

Name: mib2events
Version: %{version}
Release: %{rel}
License: GPL
Group: Applications/System
Summary: Generate OpenNMS Events from MIB Traps
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Obsoletes: mib2opennms

%description
A tool to generate OpenNMS events from MIB traps.

%prep
%setup -n %{name}-%{version}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 lib/%{name}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/
cat <<END >$RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
java -jar %{_datadir}/%{name}/%{name}.jar "\$@"
END

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
	rm -rf "$RPM_BUILD_ROOT"
fi

%files
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_datadir}/%{name}/*

%changelog
* Fri Aug 10 2012 Benjamin Reed <ranger@opennms.org>
- initial package
