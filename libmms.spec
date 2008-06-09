%define name	libmms
%define version	0.4
%define release	%mkrel 1

%define major		0
%define libname		%mklibname mms %major
%define develname	%mklibname mms -d

Summary:        MMS stream protocol library
Name:           %{name}
Version:        %{version}
Release:	%{release}
License:	LGPLv2.1
Group:          System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:         http://prdownloads.sourceforge.net/libmms/libmms-%{version}.tar.gz
URL:            http://libmms.sf.net
BuildRequires:	glib2-devel

%description
Libmms is a library implementing the MMS streaming protocol.

%package -n %libname
Group: System/Libraries
Summary: Shared library implementing the MMS protocol

%description -n %libname
Libmms is a library implementing the mms streaming protocol.

%package -n %develname
Summary: Development headers for developing with libmms
Group:	 Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname mms 0 -d

%description -n %develname
This package provides the necessary development headers and libraries
to allow you to build programs that use libmms.

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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS ChangeLog README TODO README.LICENSE
%{_libdir}/libmms.so.*

%files -n %develname
%defattr(-, root, root)
%{_includedir}/libmms
%{_libdir}/libmms.so
%{_libdir}/libmms.la
%{_libdir}/pkgconfig/libmms.pc
