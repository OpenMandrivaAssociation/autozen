Summary:	Brainwave controller
Name:		autozen
Version:	2.1
Release:	7
License:	GPLv2+
Group:		Sound
Url:		http://www.linuxlabs.com/autozen.html
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}48.png
Source2:	%{name}32.png
Source3:	%{name}16.png
Patch0:		autozen-2.1-no-strip.patch
BuildRequires:	pkgconfig(gtk+)

%description
AutoZen is a software 'brain machine' for Linux. It generates sounds that are
meant to cause the brain to temporarily shift to a different dominant
frequency and cause the user to experience an altered state of consciousness.

NOTE: Requires headphones.

%files
%doc CHANGES COPYING doc/HTML/*
%{_bindir}/%{name}
%{_bindir}/seq2wav
%{_bindir}/zentime
%{_mandir}/man1/*
%{_datadir}/AutoZen/*.seq
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
make clean
make CFLAGS="%{optflags}"

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}
rm -fr %{buildroot}%{_docdir}/AutoZen
mv %{buildroot}/usr/man %{buildroot}/%{_datadir}/

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=AutoZen
Comment=Brainwave controller
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;AudioVideo;Audio;AudioVideoEditing;
EOF

#icons
mkdir -p %{buildroot}%{_liconsdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

