#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_with	glitz		# build with glitz backend
%bcond_without	xcb		# XCB backend
%bcond_with	tests		# perform tests (can fail due to out of memory)
%bcond_without	lcd             # use own LCD filtering instead of freetype's
#
Summary:	Cairo - multi-platform 2D graphics library
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	1.4.4
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a609118644e1d958d977821c6fd765a9
Patch0:		%{name}-link.patch
Patch1:		http://david.freetype.org/lcd/cairo-1.2.4-lcd-filter-1.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	fontconfig-devel
%{?with_lcd:BuildRequires:	freetype-devel >= 1:2.3.0}
%{!?with_lcd:BuildRequires:	freetype-devel >= 1:2.1.10}
%{?with_glitz:BuildRequires:	glitz-devel >= 0.5.1}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.3}
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
%if %{with xcb}
BuildRequires:	libxcb-devel >= 0.9.92
BuildRequires:	xcb-util-devel >= 0.2
%endif
BuildRequires:	xorg-lib-libXrender-devel >= 0.6
BuildRequires:	zlib-devel
%{!?with_lcd:Requires:	freetype >= 1:2.1.10}
%{?with_lcd:Requires:	freetype >= 1:2.3.0}
%{?with_glitz:Requires:	glitz >= 0.5.1}
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

%description -l pl.UTF-8
Cairo obsługuje oparty na wektorach rendering z antyaliasingiem dla X.
Ścieżki składają się z odcinków i splajnów kubicznych, a renderowane
mogą być z dowolną grubością i różnymi stylami połączeń i zakończeń.
Wszystkie kolory mogą być podane z opcjonalną półprzezroczystością
(podaną przez współczynnik nieprzezroczystości lub alpha) i łączone
przy użyciu rozszerzonego algorytmu mieszania Portera-Duffa, który
można znaleźć w rozszerzeniu X Render.

Cairo eksportuje stanowe API renderujące w duchu podobne do operatorów
konstruowania ścieżek, tekstu i rysowania z PostScriptu (ze znacznym
dodatkiem półprzezroczystości w modelu obrazu). Kiedy API zostanie
ukończone, ma obsługiwać pełny model obrazu z PDF w wersji 1.4.

%package devel
Summary:	Development files for Cairo library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 1:2.1.10
%{?with_glitz:Requires:	glitz-devel >= 0.5.1}
Requires:	libpng-devel
%{?with_xcb:Requires:	libxcb-devel >= 0.9.92}
%{?with_xcb:Requires:	xcb-util-devel >= 0.2}
Requires:	xorg-lib-libXrender-devel >= 0.6

%description devel
Development files for Cairo library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Cairo.

%package static
Summary:	Static Cairo library
Summary(pl.UTF-8):	Statyczna biblioteka Cairo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Cairo library.

%description static -l pl.UTF-8
Statyczna biblioteka Cairo.

%package apidocs
Summary:	Cairo API documentation
Summary(pl.UTF-8):	Dokumentacja API Cairo
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Cairo API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Cairo. 

%prep
%setup -q
%patch0 -p1
%{?with_lcd:%patch1 -p1}

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	%{?with_xcb:--enable-xcb} \
	%{?with_glitz:--enable-glitz} \
	--enable-ps \
	--enable-pdf \
	--with-html-dir=%{_gtkdocdir}
%{__make}
%{?with_tests:%{__make} check}

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
