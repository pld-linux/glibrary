Summary:	GBiblioteka is a book and document manager
Summary(pl):	Program u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych
Name:		gbiblioteka
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications/Archiving	
Source0:	http://members.lycos.co.uk/gbiblioteka/%{name}-%{version}.tar.gz
# Source0-md5:	77bcb252e8486167d409de162e2f901d
URL:		http://members.lycos.co.uk/gbiblioteka/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	sqlite3-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GBiblioteka is a book and document manager.

%description -l pl
Program u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych. 

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc ChangeLog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
