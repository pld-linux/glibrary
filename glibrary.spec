Summary:	Glibrary - a book and document manager
Summary(pl):	Program u³atwiaj±cy zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych
Name:		glibrary
Version:	1.0.1
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://www.glibrary.svx.pl/download/1_0_1/%{name}-%{version}.tar.gz
# Source0-md5:	f4b2d4e8943e83a8897c8711bfaf7ecb
URL:		http://www.glibrary.svx.pl/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libglade2
BuildRequires:	sqlite3-devel >= 3.1
Requires:	sqlite3 >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glibrary is a book and document manager.

%description -l pl
Program Glibrary u³atwia zarz±dzanie zbiorami ksi±¿ek i dokumentów
elektronicznych.

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
%defattr(644,root,root,755)
%doc ChangeLog
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glibrary
%{_desktopdir}/glibrary.desktop
