%define         beta beta1 
#
Summary:	GBiblioteka - a book and document manager
Summary(pl):	Program u³atwiaj±cy zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych
Name:		gbiblioteka
Version:	1.0
Release:	1.%{beta}
License:	GPL v2
Group:		Applications/Archiving	
Source0:	http://kermit.w.staszic.waw.pl/gb/download/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	dfbafc7744cb25d6a03b48d2ad952054
URL:		http://kermit.w.staszic.waw.pl/gb/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libglade2
BuildRequires:	sqlite3-devel >= 3.1
Requires:	sqlite3 >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GBiblioteka is a book and document manager.

%description -l pl
Program GBiblioteka u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów
elektronicznych. 

%prep
%setup -q -n %{name}-%{version}-%{beta}

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
%{_datadir}/gbiblioteka
