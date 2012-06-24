Summary:	Converts and manipulates GIFs
Summary(de):	Konvertiert und manipuliert GIFs
Summary(fr):	Converti et manipule des GIFs
Summary(pl):	Program do konwertowania i manipulacji plikami w formacie GIF
Summary(tr):	GIF dosyalar�n� ba�ka bi�imlere �evirir
Name:		giftrans
Version:	1.12.2
Release:	10
License:	BSD
Group:		Applications/Graphics
Source0:	ftp://ftp.rz.uni-karlsruhe.de/pub/net/www/tools/%{name}-%{version}.tar.gz
# Source0-md5:	58712d7c2dcbd8ea5f0dc18945dfcabd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program can convert and manipulate GIF images from the command
line. It is most useful for making a color transparent for web sites.

%description -l de
Dieses Programm kann GIF-Bilder aus der Befehlszeile konvertieren und
manipulieren. Besonders praktisch ist es, um eine Farbe f�r Web-Seiten
transparent zu machen.

%description -l fr
Ce programme convertit et manipule des images GIF � partir de la ligne
de commande. Il est surtout utilis� pour cr�er une couleur
transparente pour les sites web.

%description -l pl
Program do konwertowania i manipulacji plikami w formacie GIF.
Szczeg�lnie u�yteczny do robienia kolorowych witryn WWW.

%description -l tr
Bu program, GIF bi�imindeki resim dosyalar�n� ba�ka bi�imlere �evirir.
En yayg�n kullan�m alanlar�ndan biri, web siteleri i�in resimleri
saydam hale getirmektir.

%prep
%setup -q

%build
%{__cc} -Dvoidd=void %{rpmcflags} -o giftrans giftrans.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install giftrans $RPM_BUILD_ROOT%{_bindir}
install giftrans.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
