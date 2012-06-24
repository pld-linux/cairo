Summary:	Cairo - multi-platform 2D graphics library
Summary(pl):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	0.5.0
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	cf39f429026498128fd4711cf4b824bf
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	glitz-devel >= 0.4.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libpixman-devel >= 0.1.4
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
#BuildRequires:	xcb-devel (http://freedesktop.org/software/xcb - CVS only, not released yet)
BuildRequires:	xrender-devel >= 0.6
BuildRequires:	zlib-devel
Requires:	freetype >= 2.1.0
Requires:	glitz >= 0.4.0
Requires:	libpixman >= 0.1.4
Requires:	xrender >= 0.6
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
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.1.0
Requires:	glitz-devel >= 0.4.0
Requires:	libpixman-devel >= 0.1.4
Requires:	libpng-devel
Requires:	xrender-devel >= 0.6

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
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
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
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/cairo

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
