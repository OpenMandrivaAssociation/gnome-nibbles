%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		gnome-nibbles
Version:	3.16.1
Release:	1
Summary:	GNOME Nibbles game
License:	GPLv2+ and GFDL
Group:		Games/Arcade
URL:		https://wiki.gnome.org/Nibbles
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	gnibbles
# For help
Requires:	yelp

%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.nibbles.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.*
%{_iconsdir}/*/*/apps/%{name}-symbolic.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.1-3.mga5
+ Revision: 815341
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 747000
- Second Mageia 5 Mass Rebuild

* Tue Oct 14 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738536
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719217
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679741
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676951
- new version 3.13.92

* Tue Sep 02 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670848
- new version 3.13.91

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665383
- new version 3.13.90

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622221
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 613932
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607774
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604301
- new version 3.11.92

* Mon Feb 17 2014 ovitters <ovitters> 3.11.90.1-1.mga5
+ Revision: 593204
- new version 3.11.90.1

* Sat Feb 15 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 592412
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 583018
- new version 3.11.5

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-3.mga4
+ Revision: 550164
- fix url

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541369
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495778
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483779
- new version 3.10.0

* Sun Sep 15 2013 dams <dams> 3.9.92-1.mga4
+ Revision: 479798
- new version 3.9.92

  + fwang <fwang>
    - cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.0-1.mga4
+ Revision: 440860
- imported package gnome-nibbles

