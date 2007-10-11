Summary:	bbe - Binary block editor
Summary(pl.UTF-8):	bbe - binarny edytor blokowy
Name:		bbe
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/bbe-/%{name}-%{version}.tar.gz
# Source0-md5:	b056d0bfd852384aced73d4533887d4b
URL:		http://members.surfeu.fi/tjsa/bbe/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bbe program is a sed-like editor for binary files. bbe performs
basic byte related transformations on blocks of input stream. bbe is
non-interactive command line tool and can be used as a part of a
pipeline. bbe makes only one pass over input stream.

bbe contains also grep-like features, like printing the filename,
offset and block number.

%description -l pl.UTF-8
bbe to podobny do seda edytor do plików binarnych. Wykonuje podstawowe
przekształcenia związane z bajtami na blokach strumienia wejściowego.
bbe jest nieinteraktywnym narzędziem linii poleceń i może być używany
jako część potoku. Wykonuje tylko jedno przejście strumienia
wejściowego.

bbe zawiera także elementy podobne do grepa, takie jak wypisywanie
nazwy pliku, offsetu i numeru bloku.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	htmldir=%{_docdir}/%{name}-%{version}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/bbe
%{_mandir}/man1/bbe.*
%{_infodir}/bbe.*

%clean
rm -rf $RPM_BUILD_ROOT
