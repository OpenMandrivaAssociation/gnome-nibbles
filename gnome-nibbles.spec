%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:		gnome-nibbles
Version:	4.2.0
Release:	1
Summary:	GNOME Nibbles game
License:	GPLv2+ and GFDL
Group:		Games/Arcade
URL:		https://wiki.gnome.org/Nibbles
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(libgnome-games-support-2)
BuildRequires:  gtk-update-icon-cache
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
BuildRequires:  vala
Obsoletes:	gnibbles
# For help
Requires:	yelp

%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Nibbles.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Nibbles.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Nibbles.service
%{_datadir}/%{name}
%{_iconsdir}/*/*/apps/org.gnome.Nibbles.*
%{_iconsdir}/*/*/apps/org.gnome.Nibbles-symbolic.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Nibbles.appdata.xml


