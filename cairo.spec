%define	cvs_release 20030830
Summary:	Cairo graphics API
Name:		cairo
Version:	0
Release:	0.%{cvs_release}.1
License:	BSD-like
Group:		Development/Libraries
Source0:	%{name}-cvs-%{cvs_release}.tar.gz
# Source0-md5:	6f1f206e8b9d19b520245b27364a6128
URL:		http://cairographics.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires: libic-devel
BuildRequires: libpixregion-devel

%description
cairo

%package devel
Summary: Devel files for cairo
Group: Development/Libraries

%description devel
Devel files for cairo

%package static
Summary: Static libraries for cairo
Group: Development/Libraries

%description static
Static libraries for cairo

%prep
%setup -n %{name}

%build
%{__libtoolize} --force --copy
%{__aclocal}
%{__autoheader}
%{__automake} --add-missing
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/*.so.*

%files static
%{_libdir}/*.a

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.la
