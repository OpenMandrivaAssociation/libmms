%define libname %mklibname mms 0
Summary:        MMS stream protocol library
Name:           libmms
Version:        0.3
Release: %mkrel 1
License:      LGPL
Group:          System/Libraries
Source:         http://prdownloads.sourceforge.net/libmms/libmms-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{PACKAGE_VERSION}-root
URL:            http://libmms.sf.net
BuildRequires: glib2-devel

%description
Libmms is a library implementing the mms streaming protocol.

%package -n %libname
Group: System/Libraries
Summary: Shared library implementing the MMS protocol

%description -n %libname
Libmms is a library implementing the mms streaming protocol.

%package -n %libname-devel
Summary: Libraries and includefiles for developing with libmms
Group:	 Development/C
Requires: %libname = %version
Provides: libmms-devel = %version-%release

%description -n %libname-devel
This paackage provides the necessary development headers and libraries
to allow you to devel with libmms

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog README TODO README.LICENSE
# NEWS
%{_libdir}/libmms.so.*

%files -n %libname-devel
%defattr(-, root, root)
%{_includedir}/libmms/
%{_libdir}/libmms.so
%{_libdir}/libmms.la
%{_libdir}/pkgconfig/libmms.pc
