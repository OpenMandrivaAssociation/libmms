%define major	0
%define libname	%mklibname mms %{major}
%define devname	%mklibname mms -d

Summary:	MMS stream protocol library
Name:		libmms
Version:	0.6.2
Release:	9
License:	LGPLv2.1
Group:		System/Libraries
Url:		http://www.sf.net/projects/libmms
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)

%description
Libmms is a library implementing the MMS streaming protocol.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library implementing the MMS protocol

%description -n %{libname}
Libmms is a library implementing the mms streaming protocol.

%package -n %{devname}
Summary:	Development headers for developing with libmms
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development headers and libraries
to allow you to build programs that use libmms.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmms.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README README.LICENSE
%{_includedir}/libmms
%{_libdir}/libmms.so
%{_libdir}/pkgconfig/libmms.pc

