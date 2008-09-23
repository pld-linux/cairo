#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_with	glitz		# build with glitz backend
%bcond_without	xcb		# XCB backend
%bcond_with	tests		# perform tests (can fail due to out of memory)
#
Summary:	Cairo - multi-platform 2D graphics library
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	1.7.6
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	c612f581b18903b0751a171685fc38dd
Patch0:		%{name}-link.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.8
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 1:2.3.0
%{?with_glitz:BuildRequires:	glitz-devel >= 0.5.1}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pixman-devel >= 0.12.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.8.0
%if %{with xcb}
BuildRequires:	libxcb-devel >= 0.9.92
BuildRequires:	xcb-util-devel >= 0.2
%endif
BuildRequires:	xorg-lib-libXrender-devel >= 0.6
BuildRequires:	zlib-devel
Requires:	freetype >= 1:2.3.0
%{?with_glitz:Requires:	glitz >= 0.5.1}
Requires:	pixman >= 0.12.0
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
przy użyciu rozszerzonego algorytmu składania Portera-Duffa, który
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
Requires:	freetype-devel >= 1:2.3.0
%{?with_glitz:Requires:	glitz-devel >= 0.5.1}
Requires:	libpng-devel
%{?with_xcb:Requires:	libxcb-devel >= 0.9.92}
Requires:	pixman-devel >= 0.12.0
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

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I build
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	%{?with_xcb:--enable-xcb} \
	%{?with_glitz:--enable-glitz} \
	--enable-ps \
	--enable-pdf \
	--enable-png \
	--enable-freetype \
	--with-html-dir=%{_gtkdocdir}
%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/cairo}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcairo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo.so
%{_libdir}/libcairo.la
%{_includedir}/cairo
%{_pkgconfigdir}/cairo.pc
%{_pkgconfigdir}/cairo-ft.pc
%{_pkgconfigdir}/cairo-pdf.pc
%{_pkgconfigdir}/cairo-png.pc
%{_pkgconfigdir}/cairo-ps.pc
%{_pkgconfigdir}/cairo-svg.pc
%{?with_xcb:%{_pkgconfigdir}/cairo-xcb.pc}
%{_pkgconfigdir}/cairo-xlib.pc
%{_pkgconfigdir}/cairo-xlib-xrender.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairo.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
%endif
