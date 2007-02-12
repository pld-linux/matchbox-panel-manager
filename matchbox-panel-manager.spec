Summary:	Matchbox Panel Manager
Summary(pl.UTF-8):   Narzędzie do zarządzania panelem środowiska Matchbox
Name:		matchbox-panel-manager
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/matchbox-panel-manager/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0ea7b03abd7b90eda601b8658a859fb6
Patch0:		%{name}-desktop.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
Requires:	matchbox-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An application to manage Matchbox panel configuration.

%description -l pl.UTF-8
Aplikacja do zarządzania konfiguracją panelu środowiska Matchbox.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/matchbox-panel-manager
%{_desktopdir}/mb-panel-manager.desktop
%{_pixmapsdir}/mbpanelmgr.png
