%define name	python-tal
%define version 1.5.0
%define release %mkrel 8

Name: 	 	%name
Summary: 	Zope Template Attribute Language (TAL) Python module
Version: 	%version
Release: 	%release

# (misc)  stolen on debian site
# the original "Source" file is http://ftp.debian.org/debian/pool/main/p/python-tal/python-tal_1.5.0.orig.tar.gz
Source:		%{name}-%{version}.tar.bz2
URL:		http://dev.zope.org/Wikis/DevSite/Projects/ZPT/FrontPage
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



