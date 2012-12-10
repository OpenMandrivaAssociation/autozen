%define name	autozen
%define version	2.1
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Brainwave controller
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
URL:		http://www.linuxlabs.com/autozen.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk-devel

%description
AutoZen is a software 'brain machine' for Linux. It generates sounds that are
meant to cause the brain to temporarily shift to a different dominant
frequency and cause the user to experience an altered state of consciousness.

NOTE: Requires headphones.

%prep
%setup -q

%build
make clean
make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT/%_prefix install
rm -fr $RPM_BUILD_ROOT/%_docdir/AutoZen
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%_datadir/

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AutoZen
Comment=Brainwave controller
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;AudioVideo;Audio;AudioVideoEditing;X-MandrivaLinux-Multimedia-Video;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc CHANGES COPYING doc/HTML/*
%{_bindir}/%name
%{_bindir}/seq2wav
%{_bindir}/zentime
%{_mandir}/man1/*
%{_datadir}/AutoZen/*.seq
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-6mdv2011.0
+ Revision: 616670
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.1-5mdv2010.0
+ Revision: 423997
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.1-4mdv2009.0
+ Revision: 218430
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.1-4mdv2008.1
+ Revision: 135825
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import autozen


* Tue Sep 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.1-4mdv2007.0
- XDG

* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 2.1-3mdk
- Rebuild

* Sat Jul 17 2004 Austin Acton <austin@mandrake.org> 2.1-2mdk
- rebuild

* Tue May 27 2003 Austin Acton <aacton@yorku.ca> 2.1-1mdk
- initial package
