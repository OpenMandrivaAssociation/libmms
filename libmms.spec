%define major		0
%define libname		%mklibname mms %{major}
%define develname	%mklibname mms -d

Summary:	MMS stream protocol library
Name:		libmms
Version:	0.6.2
Release:	5
License:	LGPLv2.1
Group:		System/Libraries
URL:		http://www.sf.net/projects/libmms
Source:		http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)

%description
Libmms is a library implementing the MMS streaming protocol.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library implementing the MMS protocol

%description -n %{libname}
Libmms is a library implementing the mms streaming protocol.

%package -n %{develname}
Summary:	Development headers for developing with libmms
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
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
%doc AUTHORS ChangeLog README README.LICENSE
%{_libdir}/libmms.so.%{major}*

%files -n %{develname}
%{_includedir}/libmms
%{_libdir}/libmms.so
%{_libdir}/pkgconfig/libmms.pc

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-2mdv2011.0
+ Revision: 662381
- mass rebuild

* Sat Feb 05 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.2-1
+ Revision: 636200
- new version
- new URL

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 0.6-1mdv2011.0
+ Revision: 569838
- New version 0.6
- check major

* Wed Dec 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.5-1mdv2010.1
+ Revision: 481646
- new version
- new URL

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4-3mdv2010.0
+ Revision: 425621
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2009.0
+ Revision: 222930
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Dec 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4-1mdv2008.1
+ Revision: 120763
- new version

* Thu Jul 26 2007 Adam Williamson <awilliamson@mandriva.org> 0.3-2mdv2008.0
+ Revision: 55729
- rebuild for 2008
- new devel policy
- spec clean
- Import libmms



* Fri Aug  4 2006 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2007.0
- drop merged patch
- New release 0.3

* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 0.2-3mdv2007.0
- replace patch by Debian version (Stew Benedict)

* Thu Jul 13 2006 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2007.0
- security fix for CVE-2006-2200

* Mon Dec 12 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.2-1mdk
- New release 0.2
- use mkrel

* Tue Mar  8 2005 Götz Waschk <waschk@linux-mandrake.com> 0.1-1mdk
- initial mdk package

* Thu Dec 9 2004 Christian Schaller <christian@fluendo.com>
-first attempt at SPEC
