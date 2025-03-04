Summary:	A CGI search frontend and indexers built on Xapian
Name:		xapian-omega
Version:	1.2.22
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://www.xapian.org
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	xapian-devel >= %{version}
BuildRequires:	pcre-devel
Requires:	xapian-core >= %{version}

%description
Omega is a CGI application which uses the Xapian Information Retrieval
library to index and search collections of documents.

%prep
%setup -q

%build
%configure
%make

%install
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

%files
%doc AUTHORS ChangeLog README TODO NEWS
%dir %{_datadir}/omega
%dir %{_var}/www/icons/omega
%dir %{_var}/lib/omega
%dir %{_var}/lib/omega/templates
%{_bindir}/dbi2omega
%{_bindir}/omindex
%{_bindir}/scriptindex
%{_bindir}/htdig2omega
%{_bindir}/mbox2omega
%{_libdir}/xapian-omega/bin/outlookmsg2html
%{_var}/lib/omega/templates/*
%{_var}/log/omega
%{_var}/www/cgi-bin/omega
%{_var}/www/icons/omega/*.png
%{_datadir}/omega/*.script
%config(noreplace) %{_sysconfdir}/omega.conf
%{_mandir}/man1/omindex.1*
%{_mandir}/man1/scriptindex.1*
