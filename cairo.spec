Summary:	Cairo - multi-platform 2D graphics library
Summary(pl):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	0.1.20
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	1203aec55f9ec7beee317f4f84f08fa2
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpixman-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.

Cairo relies on the Xc library for backend rendering. Xc provides an
abstract interface for rendering to multiple target types. As of this
writing, Xc allows Cairo to target X drawables as well as generic
image buffers. Future backends such as PostScript, PDF, and perhaps
OpenGL are currently being planned.

%description -l pl
Cairo obs�uguje oparty na wektorach rendering z antyaliasingiem dla X.
�cie�ki sk�adaj� si� z odcink�w i splajn�w kubicznych, a renderowane
mog� by� z dowoln� grubo�ci� i r�nymi stylami po��cze� i zako�cze�.
Wszystkie kolory mog� by� podane z opcjonaln� p�przezroczysto�ci�
(podan� przez wsp�czynnik nieprzezroczysto�ci lub alpha) i ��czone
przy u�yciu rozszerzonego algorytmu mieszania Portera-Duffa, kt�ry
mo�na znale�� w rozszerzeniu X Render.

Cairo eksportuje stanowe API renderuj�ce w duchu podobne do operator�w
konstruowania �cie�ek, tekstu i rysowania z PostScriptu (ze znacznym
dodatkiem p�przezroczysto�ci w modelu obrazu). Kiedy API zostanie
uko�czone, ma obs�ugiwa� pe�ny model obrazu z PDF w wersji 1.4.

Cairo do backendowego renderowania wykorzystuje bibliotek� Xc. Xc
dostarcza abstrakcyjny interfejs do renderowania na wiele rodzaj�w
wyj��. Aktualnie Xc pozwala Cairo tworzy� obiekty X, a tak�e og�lne
bufory obrazu. W przysz�o�ci planowane s� takie backendy jak
PostScript, PDF i by� mo�e OpenGL.

%package devel
Summary:	Development files for Cairo library
Summary(pl):	Pliki programistyczne biblioteki Cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpixman-devel >= 0.1.0

%description devel
Development files for Cairo library.

%description devel -l pl
Pliki programistyczne biblioteki Cairo.

%package static
Summary:	Static Cairo library
Summary(pl):	Statyczna biblioteka Cairo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Cairo library.

%description static -l pl
Statyczna biblioteka Cairo.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
