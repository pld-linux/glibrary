Summary:	Glibrary - a book and document manager
Summary(pl):	Program u³atwiaj±cy zarz±dzanie zbiorami ksi±¿ek i dokumentów elektronicznych
Name:		glibrary
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Archiving	
Source0:	http://www.glibrary.svx.pl/download/1_0/%{name}-%{version}.tar.gz
# Source0-md5:	ea6299c9876d027e9a5beab4d6b05ca4
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
%setup -q -n %{name}-%{version}

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
#%{_datadir}
/usr/share/applications/glibrary.desktop
/usr/share/glibrary/glade/glibrary.glade
/usr/share/glibrary/glade/glibrary.gladep
/usr/share/glibrary/pixmaps/glibrary.png
/usr/share/glibrary/pixmaps/glibrary_icon.png
