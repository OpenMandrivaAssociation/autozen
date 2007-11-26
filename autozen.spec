%define name	autozen
%define version	2.1
%define release %mkrel 4

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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="AutoZen" longtitle="Brainwave controller" section="Multimedia/Sound" xdg="true"
EOF

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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc CHANGES COPYING doc/HTML/*
%{_bindir}/%name
%{_bindir}/seq2wav
%{_bindir}/zentime
%{_mandir}/man1/*
%{_datadir}/AutoZen/*.seq
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

