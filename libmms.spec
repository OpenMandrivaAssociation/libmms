%define name	libmms
%define version	0.6.2
%define release	%mkrel 2

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
Source:         http://downloads.sourceforge.net/project/%name/%name/%version/%name-%version.tar.gz
URL:            http://www.sf.net/projects/libmms
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
rm -rf %{buildroot}

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root)
%doc AUTHORS ChangeLog README README.LICENSE
%{_libdir}/libmms.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_includedir}/libmms
%{_libdir}/libmms.so
%{_libdir}/libmms.la
%{_libdir}/pkgconfig/libmms.pc
