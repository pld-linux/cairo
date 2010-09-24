#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%if "%{pld_release}" == "ac"
%bcond_with	xcb		# XCB backend
%else
%bcond_without	xcb		# XCB backend
%endif
%bcond_with	tests		# perform tests (can fail due to out of memory)
#
Summary:	Cairo - multi-platform 2D graphics library
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	1.10.0
Release:	3
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	70a2ece66cf473d976e2db0f75bf199e
Patch0:		%{name}-link.patch
Patch1:		%{name}-comma.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.6
BuildRequires:	fontconfig-devel >= 2.2.95
BuildRequires:	freetype-devel >= 1:2.3.0
BuildRequires:	glib2-devel >= 1:2.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.6}
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	librsvg-devel >= 2.15.0
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pixman-devel >= 0.18.4
BuildRequires:	pkgconfig >= 1:0.9
BuildRequires:	poppler-glib-devel >= 0.13.3
BuildRequires:	rpm >= 4.4.9-56
%if %{with xcb}
BuildRequires:	libxcb-devel >= 1.4
%endif
%if "%{pld_release}" == "ac"
BuildRequires:	xrender-devel >= 0.6
%else
BuildRequires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
BuildRequires:	xorg-lib-libXrender-devel >= 0.6
%endif
BuildRequires:	zlib-devel
Requires:	freetype >= 1:2.3.0
Requires:	pixman >= 0.18.4
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
Requires:	freetype-devel >= 1:2.3.0
Requires:	libpng-devel >= 2:1.4.0
%{?with_xcb:Requires:	libxcb-devel >= 1.4}
Requires:	pixman-devel >= 0.18.4
%if "%{pld_release}" == "ac"
Requires:	xrender-devel >= 0.6
%else
Requires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
Requires:	xorg-lib-libXrender-devel >= 0.6
%endif

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
Requires:	glib2-devel >= 1:2.0

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
Summary:	Cairo calls tracing utility
Summary(pl.UTF-8):	Narzędzie do śledzenia wywołań Cairo
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description trace
Cairo calls tracing utility.

%description trace -l pl.UTF-8
Narzędzie do śledzenia wywołań Cairo.

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
%patch1 -p1

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I build
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-freetype \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-pdf \
	--enable-png \
	--enable-ps \
	%{?with_xcb:--enable-xcb} \
	--with-html-dir=%{_gtkdocdir}
%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# LD_PRELOADable library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cairo/libcairo-trace.{la,a}

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/cairo}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes, not LGPL/MPL texts
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcairo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo.so.2
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairo-script-interpreter.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairo.so
%attr(755,root,root) %{_libdir}/libcairo-script-interpreter.so
%{_libdir}/libcairo.la
%{_libdir}/libcairo-script-interpreter.la
%{_includedir}/cairo
%exclude %{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo.pc
%{_pkgconfigdir}/cairo-fc.pc
%{_pkgconfigdir}/cairo-ft.pc
%{_pkgconfigdir}/cairo-pdf.pc
%{_pkgconfigdir}/cairo-png.pc
%{_pkgconfigdir}/cairo-ps.pc
%{_pkgconfigdir}/cairo-svg.pc
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
%{_libdir}/libcairo-gobject.la
%{_includedir}/cairo/cairo-gobject.h
%{_pkgconfigdir}/cairo-gobject.pc

%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libcairo-gobject.a

%files trace
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cairo-trace
%dir %{_libdir}/cairo
%attr(755,root,root) %{_libdir}/cairo/libcairo-trace.so*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
%endif
