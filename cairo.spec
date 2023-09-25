#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	pdf		# PDF surface backend
%bcond_without	svg		# SVG surface backend
%bcond_without	xcb		# XCB backend
%bcond_with	tests		# perform tests (can fail due to out of memory)

Summary:	Cairo - multi-platform 2D graphics library
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	1.18.0
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	https://www.cairographics.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	3f0685fbadc530606f965b9645bb51d9
URL:		https://www.cairographics.org/
BuildRequires:	binutils-devel
BuildRequires:	fontconfig-devel >= 2.2.95
%if %{with tests}
# ttx
BuildRequires:	fonttools
%endif
# pkgconfig(freetype2) >= 25.0.19
BuildRequires:	freetype-devel >= 1:2.13.0
BuildRequires:	glib2-devel >= 1:2.14
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.15}
BuildRequires:	libpng-devel >= 2:1.4.0
%if %{with svg} && %{with tests}
BuildRequires:	librsvg-devel >= 2.35.0
%endif
%if %{with tests}
BuildRequires:	libspectre-devel >= 0.2.0
%endif
%{?with_xcb:BuildRequires:	libxcb-devel >= 1.6}
BuildRequires:	lzo-devel >= 2
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pixman-devel >= 0.36.0
BuildRequires:	pkgconfig >= 1:0.18
%if %{with pdf} && %{with tests}
BuildRequires:	poppler-glib-devel >= 0.17.4
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.6
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	fontconfig-libs >= 2.2.95
Requires:	freetype >= 1:2.13.0
%{?with_xcb:Requires:	libxcb >= 1.6}
Requires:	pixman >= 0.36.0
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
Requires:	fontconfig-devel >= 2.2.95
Requires:	freetype-devel >= 1:2.13.0
Requires:	libpng-devel >= 2:1.4.0
%{?with_xcb:Requires:	libxcb-devel >= 1.6}
Requires:	lzo-devel >= 2
Requires:	pixman-devel >= 0.36.0
Requires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXrender-devel >= 0.6
Requires:	zlib-devel

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

%package gobject
Summary:	GObject functions library for Cairo graphics library
Summary(pl.UTF-8):	Biblioteka funkcji GObject dla biblioteki graficznej Cairo
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.14

%description gobject
GObject functions library for Cairo graphics library.

%description gobject -l pl.UTF-8
Biblioteka funkcji GObject dla biblioteki graficznej Cairo.

%package gobject-devel
Summary:	Header files for Cairo GObject library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Cairo GObject
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}
Requires:	glib2-devel >= 1:2.14

%description gobject-devel
Header files for Cairo GObject library.

%description gobject-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Cairo GObject.

%package gobject-static
Summary:	Static Cairo GObject library
Summary(pl.UTF-8):	Statyczna biblioteka Cairo GObject
Group:		Development/Libraries
Requires:	%{name}-gobject-devel = %{version}-%{release}

%description gobject-static
Static Cairo GObject library.

%description gobject-static -l pl.UTF-8
Statyczna biblioteka Cairo GObject.

%package trace
Summary:	Cairo calls tracing utilities
Summary(pl.UTF-8):	Narzędzia do śledzenia wywołań Cairo
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	binutils-libs >= 2.21.53

%description trace
Cairo calls tracing utilities.

%description trace -l pl.UTF-8
Narzędzia do śledzenia wywołań Cairo.

%package apidocs
Summary:	Cairo API documentation
Summary(pl.UTF-8):	Dokumentacja API Cairo
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
Cairo API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Cairo.

%prep
%setup -q

%build
%meson build \
	-Dfontconfig=enabled \
	-Dfreetype=enabled \
	-Dgtk_doc=%{__true_false apidocs} \
	-Dpng=enabled \
	-Dspectre=%{__enabled_disabled tests} \
	-Dtee=enabled \
	-Dtests=disabled \
	-Dxcb=%{__enabled_disabled xcb} \
	-Dxlib=enabled \
	-Dzlib=enabled

%ninja_build -C build

%{?with_tests:%ninja_test -C build}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# LD_PRELOADable library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cairo/libcairo-{fdr,trace}.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS BUGS COPYING NEWS README.md
%attr(755,root,root) %{_libdir}/libcairo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo.so.2
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo-script-interpreter.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo.so
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so
%{_includedir}/cairo
%exclude %{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo.pc
%{_pkgconfigdir}/cairo-fc.pc
%{_pkgconfigdir}/cairo-ft.pc
%{?with_pdf:%{_pkgconfigdir}/cairo-pdf.pc}
%{_pkgconfigdir}/cairo-png.pc
%{_pkgconfigdir}/cairo-ps.pc
%{_pkgconfigdir}/cairo-script.pc
%{_pkgconfigdir}/cairo-script-interpreter.pc
%{?with_svg:%{_pkgconfigdir}/cairo-svg.pc}
%{_pkgconfigdir}/cairo-tee.pc
%{?with_xcb:%{_pkgconfigdir}/cairo-xcb.pc}
%{?with_xcb:%{_pkgconfigdir}/cairo-xcb-shm.pc}
%{_pkgconfigdir}/cairo-xlib.pc
%{_pkgconfigdir}/cairo-xlib-xrender.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairo.a
%{_libdir}/libcairo-script-interpreter.a

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo-gobject.so.2

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo-gobject.so
%{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo-gobject.pc

%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libcairo-gobject.a

%files trace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cairo-trace
%dir %{_libdir}/cairo
%attr(755,root,root) %{_libdir}/cairo/libcairo-fdr.so
%attr(755,root,root) %{_libdir}/cairo/libcairo-trace.so*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
%endif
