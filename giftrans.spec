Summary:	converts and manipulates GIFs
Summary(de):	konvertiert und manipuliert GIFs 
Summary(fr):	converti et manipule des GIFs
Summary(pl):	Program do konwertowania i manipulacji plikami w formacie GIF
Summary(tr):	GIF dosyalarýný baþka biçimlere çevirir
Name:		giftrans
Version:	1.12.2
Release:	5
Copyright:	BSD
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source:		ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program can convert and manipulate GIF images from the 
command line.  It is most useful for making a color transparent
for web sites.

%description -l de
Dieses Programm kann GIF-Bilder aus der Befehlszeile konvertieren und 
manipulieren. Besonders praktisch ist es, um eine Farbe für Web-Seiten
transparent zu machen. 

%description -l fr
Ce programme convertit et manipule des images GIF à partir de
la ligne de commande. Il est surtout utilisé pour créer une
couleur transparente pour les sites web.

%description -l pl
Program do konwertowania i manipulacji plikami w formacie GIF.
Szczególnie u¿yteczny do robienia kolorowych witryn WWW.

%description -l tr
Bu program, GIF biçimindeki resim dosyalarýný baþka biçimlere çevirir. En
yaygýn kullaným alanlarýndan biri, web siteleri için resimleri saydam hale
getirmektir.

%prep
%setup -q

%build
gcc -Dvoidd=void $RPM_OPT_FLAGS -s -o giftrans giftrans.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s giftrans $RPM_BUILD_ROOT%{_bindir}
install giftrans.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
