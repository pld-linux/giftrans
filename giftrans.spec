Summary:	converts and manipulates GIFs
Summary(de):	konvertiert und manipuliert GIFs 
Summary(fr):	converti et manipule des GIFs
Summary(pl):	Program do konwertowania i manipulacji plikami w formacie GIF
Summary(tr):	GIF dosyalar�n� ba�ka bi�imlere �evirir
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
manipulieren. Besonders praktisch ist es, um eine Farbe f�r Web-Seiten
transparent zu machen. 

%description -l fr
Ce programme convertit et manipule des images GIF � partir de
la ligne de commande. Il est surtout utilis� pour cr�er une
couleur transparente pour les sites web.

%description -l pl
Program do konwertowania i manipulacji plikami w formacie GIF.
Szczeg�lnie u�yteczny do robienia kolorowych witryn WWW.

%description -l tr
Bu program, GIF bi�imindeki resim dosyalar�n� ba�ka bi�imlere �evirir. En
yayg�n kullan�m alanlar�ndan biri, web siteleri i�in resimleri saydam hale
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
