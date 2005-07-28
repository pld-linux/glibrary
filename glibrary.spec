Summary:	GBiblioteka is a book and document manager
Summary(pl):	Program u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych
Name:		gbiblioteka
Version:	0.5
Release:	0.1
License:	GPL v2
Group:		Applications/Archiving	
Source0:	http://members.lycos.co.uk/gbiblioteka/%{name}-%{version}.tar.gz
# Source0-md5:	8f4c5237f26396208c2390dddb06ff15
URL:		http://members.lycos.co.uk/gbiblioteka/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	sqlite-devel
Requires:	gtk+2
Requires:	sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GBiblioteka is a book and document manager.

%description -l pl
Program u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych. 

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%lang(pl) %{_datadir}/locale/pl 
