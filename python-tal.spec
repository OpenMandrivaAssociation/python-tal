%define name	python-tal
%define version 1.5.0
%define release 14

Name: 	 	%name
Summary: 	Zope Template Attribute Language (TAL) Python module
Version: 	%version
Release: 	%release

# (misc)  stolen on debian site
# the original "Source" file is http://ftp.debian.org/debian/pool/main/p/python-tal/python-tal_1.5.0.orig.tar.gz
Source:		%{name}-%{version}.tar.bz2
URL:		https://dev.zope.org/Wikis/DevSite/Projects/ZPT/FrontPage
License:	Zope Public Licence
Group:		 Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel
Requires:	python
BuildArch: noarch
#(misc) stolen to debian, again, could be improved

%description
This python module provides an implementation of TAL, the Zope Template
Attribute Language. For TAL, see the Zope Presentation Templates ZWiki:
 
     http://dev.zope.org/Wikis/DevSite/Projects/ZPT/FrontPage
%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -d $RPM_BUILD_ROOT/%py_puresitedir/TAL/


for file in `find . -name '*py' `; do
  install -m644 $file $RPM_BUILD_ROOT/%py_puresitedir/TAL/
done

# (misc) moved the test to the doc packages.
# 
#install -m755 -d $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages/TAL/tests/
#
#for file in `find ./tests/ -name '*py' -maxdepth 1`; do
#  install -m644 $file $RPM_BUILD_ROOT/%{_libdir}/python%{pyver}/site-packages/TAL/tests/
#done



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc benchmark/ CHANGES.txt tests/ HISTORY.txt README.txt
%py_puresitedir/TAL/





%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.5.0-13mdv2010.0
+ Revision: 442507
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.5.0-12mdv2009.1
+ Revision: 323377
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-11mdv2009.0
+ Revision: 259831
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-10mdv2009.0
+ Revision: 247695
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-8mdv2008.1
+ Revision: 139216
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.5.0-7mdv2007.0
+ Revision: 96065
- Rebuild against new python
- Rebuild against new Python
- import python-tal-1.5.0-5mdk

* Wed May 03 2006 Michael Scherer <misc@mandriva.org> 1.5.0-5mdk
- use python macro
- use mkrel

* Thu Feb 03 2005 Michael Scherer <misc@mandrake.org> 1.5.0-4mdk
- Really rebuild for new python

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.5.0-3mdk
- Rebuild for new python

* Fri Sep 03 2004 Michael Scherer <misc@mandrake.org> 1.5.0-2mdk 
- rebuild

