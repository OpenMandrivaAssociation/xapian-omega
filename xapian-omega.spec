Summary:	A CGI search frontend and indexers built on Xapian
Name:		xapian-omega
Version:	1.0.0
Release:	%mkrel 1
License:	GPL
Group:		Internet
URL:		http://www.xapian.org
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	xapian-devel
BuildRequires:	xapian
Buildroot:	%{_tmppath}/%{name}-%{version}-root

%description
Omega is a CGI application which uses the Xapian Information Retrieval
library to index and search collections of documents.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# CGI application
mkdir -p %{buildroot}%{_var}/www/cgi-bin/
mv %{buildroot}%{_libdir}/%{name}/bin/omega %{buildroot}%{_var}/www/cgi-bin

# Create /var directories
mkdir -p %{buildroot}%{_var}/lib/omega/data
mkdir -p %{buildroot}%{_var}/lib/omega/cdb
mkdir -p %{buildroot}%{_var}/log/omega

# Default templates
mkdir -p %{buildroot}%{_var}/lib/omega/templates
cp -r templates/* %{buildroot}%{_var}/lib/omega/templates/

# Images
mkdir -p %{buildroot}%{_var}/www/icons/omega
cp -r images/* %{buildroot}%{_var}/www/icons/omega/

# Move the scripts to the right place
#mv %{buildroot}/usr/share/omega %{buildroot}%{_datadir}/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%doc AUTHORS ChangeLog COPYING README TODO NEWS
%dir %{_datadir}/omega
%dir %{_var}/www/cgi-bin/omega
%dir %{_var}/www/icons/omega
#%dir %{contentdir}/templates
%{_bindir}/dbi2omega
%{_bindir}/omindex
%{_bindir}/scriptindex
%{_bindir}/htdig2omega
%{_bindir}/mbox2omega
%{_var}/lib/omega/templates/*
%{_var}/log/omega
%{_var}/www/cgi-bin/omega
%{_var}/www/icons/omega/*.png
%{_datadir}/omega/*.script
%config(noreplace) %{_sysconfdir}/omega.conf
%{_mandir}/man1/omindex.1*
%{_mandir}/man1/scriptindex.1*