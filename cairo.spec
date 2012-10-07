#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_with	cogl		# Cogl surface backend [incompatible with cogl 1.12.x]
%bcond_with	directfb	# DirectFB surface backend
%bcond_with	drm		# DRM surface backend
%bcond_without	gl		# OpenGL surface backend
%bcond_with	glesv2		# OpenGLESv2 surface backend (mutually exclusive with gl)
%bcond_with	openvg		# OpenVG surface backend
%bcond_without	pdf		# PDF surface backend
%bcond_without	ps		# PS surface backend
%bcond_without	svg		# SVG surface backend (disable to boostrap librsvg)
%bcond_with	qt		# Qt surface backend [expects qt_draw_glyphs() API in Qt 4.7+]
%if "%{pld_release}" == "ac"
%bcond_with	xcb		# XCB backend
%else
%bcond_without	xcb		# XCB backend
%endif
%bcond_with	tests		# perform tests (can fail due to out of memory)
#
%if %{with glesv2}
%undefine	with_gl
%endif
Summary:	Cairo - multi-platform 2D graphics library
Summary(pl.UTF-8):	Cairo - wieloplatformowa biblioteka graficzna 2D
Name:		cairo
Version:	1.12.4
Release:	1
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	a64bb8774a1e476e5cdd69e635794dfb
Patch0:		%{name}-link.patch
URL:		http://cairographics.org/
%{?with_directfb:BuildRequires:	DirectFB-devel}
%if %{with gl} || %{with glesv2} || %{with openvg}
BuildRequires:	EGL-devel >= 1.1
%endif
%if %{with gl} || %{with openvg}
BuildRequires:	OpenGL-GLX-devel
%endif
%{?with_gl:BuildRequires:	OpenGL-devel}
%{?with_glesv2:BuildRequires:	OpenGLESv2-devel >= 2.0}
%{?with_openvg:BuildRequires:	OpenVG-devel}
%{?with_qt:BuildRequires:	QtGui-devel >= 4.4.0}
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	binutils-devel
%{?with_cogl:BuildRequires:	cogl-devel}
BuildRequires:	fontconfig-devel >= 2.2.95
BuildRequires:	freetype-devel >= 1:2.3.0
BuildRequires:	glib2-devel >= 1:2.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.15}
%{?with_drm:BuildRequires:	libdrm-devel}
BuildRequires:	libpng-devel >= 2:1.4.0
%if %{with svg} && %{with tests}
BuildRequires:	librsvg-devel >= 2.15.0
%endif
%if %{with ps} && %{with tests}
BuildRequires:	libspectre-devel >= 0.2.0
%endif
BuildRequires:	libtool >= 2:2.2
%{?with_xcb:BuildRequires:	libxcb-devel >= 1.6}
BuildRequires:	pixman-devel >= 0.22.0
BuildRequires:	pkgconfig >= 1:0.9
%if %{with pdf} && %{with tests}
BuildRequires:	poppler-glib-devel >= 0.17.4
%endif
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_drm:BuildRequires:	udev-devel >= 1:136}
%if "%{pld_release}" == "ac"
BuildRequires:	xrender-devel >= 0.6
%else
BuildRequires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.6
%endif
BuildRequires:	xz
BuildRequires:	zlib-devel
%{?with_qt:Requires:	QtGui >= 4.4.0}
Requires:	fontconfig-libs >= 2.2.95
Requires:	freetype >= 1:2.3.0
%{?with_xcb:Requires:	libxcb >= 1.6}
%{?with_drm:Requires:	udev-libs >= 1:136}
Requires:	pixman >= 0.22.0
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
%{?with_directfb:Requires:	DirectFB-devel}
%if %{with gl} || %{with glesv2} || %{with openvg}
Requires:	EGL-devel >= 1.1
%endif
%{?with_gl:Requires:	OpenGL-devel}
%{?with_glesv2:Requires:	OpenGLESv2-devel >= 2.0}
%{?with_openvg:Requires:	OpenVG-devel}
%{?with_qt:Requires:	QtGui-devel >= 4.4.0}
%{?with_cogl:Requires:	cogl-devel}
Requires:	fontconfig-devel >= 2.2.95
Requires:	freetype-devel >= 1:2.3.0
%{?with_drm:Requires:	libdrm-devel}
Requires:	libpng-devel >= 2:1.4.0
%{?with_xcb:Requires:	libxcb-devel >= 1.6}
Requires:	pixman-devel >= 0.22.0
%{?with_drm:Requires:	udev-devel >= 1:136}
%if "%{pld_release}" == "ac"
Requires:	xrender-devel >= 0.6
%else
Requires:	xorg-lib-libX11-devel%{?with_xcb: >= 1.1}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXrender-devel >= 0.6
%endif
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
	--disable-silent-rules \
	%{?with_cogl:--enable-cogl} \
	%{?with_directfb:--enable-directfb} \
	--enable-ft \
	%{?with_gl:--enable-gl} \
	%{?with_glesv2:--enable-glesv2} \
	%{?with_apidocs:--enable-gtk-doc} \
	%{?with_pdf:--enable-pdf} \
	--enable-png \
	%{?with_ps:--enable-ps} \
	%{?with_qt:--enable-qt} \
	%{!?with_svg:--disable-svg} \
	--enable-tee \
	%{?with_openvg:--enable-vg} \
	%{?with_xcb:--enable-xcb} \
	--enable-xml \
	--with-html-dir=%{_gtkdocdir}

%{__sed} -i 's/gobject-2.0 glib-2.0//' src/cairo.pc

%{__make}
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# LD_PRELOADable library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cairo/libcairo-trace.{la,a}
# LD_PRELOADable modules(?)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cairo/cairo-{fdr,sphinx}.{la,a}

%{!?with_apidocs:%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}/cairo}

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
%{?with_directfb:%{_pkgconfigdir}/cairo-directfb.pc}
%if %{with gl} || %{with glesv2} || %{with openvg}
%{_pkgconfigdir}/cairo-egl.pc
%endif
%{_pkgconfigdir}/cairo-fc.pc
%{_pkgconfigdir}/cairo-ft.pc
%{?with_gl:%{_pkgconfigdir}/cairo-gl.pc}
%if %{with gl} || %{with openvg}
%{_pkgconfigdir}/cairo-glx.pc
%endif
%{?with_pdf:%{_pkgconfigdir}/cairo-pdf.pc}
%{_pkgconfigdir}/cairo-png.pc
%{?with_ps:%{_pkgconfigdir}/cairo-ps.pc}
%{?with_qt:%{_pkgconfigdir}/cairo-qt.pc}
%{_pkgconfigdir}/cairo-script.pc
%{?with_svg:%{_pkgconfigdir}/cairo-svg.pc}
%{_pkgconfigdir}/cairo-tee.pc
%{?with_openvg:%{_pkgconfigdir}/cairo-vg.pc}
%{?with_xcb:%{_pkgconfigdir}/cairo-xcb.pc}
%{?with_xcb:%{_pkgconfigdir}/cairo-xcb-shm.pc}
%{_pkgconfigdir}/cairo-xlib.pc
%{_pkgconfigdir}/cairo-xlib-xrender.pc
%{_pkgconfigdir}/cairo-xml.pc

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
%attr(755,root,root) %{_bindir}/cairo-sphinx
%attr(755,root,root) %{_bindir}/cairo-trace
%dir %{_libdir}/cairo
%attr(755,root,root) %{_libdir}/cairo/cairo-fdr.so*
%attr(755,root,root) %{_libdir}/cairo/cairo-sphinx.so*
%attr(755,root,root) %{_libdir}/cairo/libcairo-trace.so*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cairo
%endif
