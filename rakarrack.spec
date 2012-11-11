%define		gitver	bdbed3f5ac1635c4ca9f2af33fcd57dae4d727d7

Summary:	Realtime guitar effects processor
Name:		rakarrack
Version:	0.6.2
Release:	0.%{gitver}.1
License:	GPL v2
Group:		X11/Applications/Sound
#Source0:	http://downloads.sourceforge.net/rakarrack/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{gitver}.tar.xz
# Source0-md5:	ccf0eb14f5c82e61f2601476a8940ecf
Patch0:		%{name}-desktop.patch
URL:		http://rakarrack.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	fltk-devel >= 1.1.3
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rakarrack is a guitar effects processor for GNU / Linux simple
and easy to use but it contains features that make it unique
in this field of applications. It contains 17 effects and
integrates a tuner and a MIDI converter.  It can also be handle
by an external MIDI controller. The settings designed by the user
can be stored in presets and these presets can be used to create
banks of effects.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	ACONNECT=%{_bindir}/aconnect \
	OPTLAGS="%{rpmcxxflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icons/icono_rakarrack_64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/rakarrack.png

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/icono_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rak*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/rakarrack.png
%{_mandir}/man1/rakarrack.1*

