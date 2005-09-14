%define _name ROX-Lib2
Summary:	A library for ROX applications
Summary(pl):	Biblioteka dla aplikacji ROXa
Name:		rox-Lib2
Version:	2.0.2
Release:	1
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/rox/rox-lib-%{version}.tgz
# Source0-md5:	e7d168299e7812d4df729cc175b44e2e
URL:		http://rox.sourceforge.net/phpwiki/index.php/ROX-Lib
Requires:	python-pygtk-gtk >= 2.0
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROX-Lib contains shared code which can be used by other ROX
applications. It is a GTK+2 version.

%description -l pl
ROX-Lib zawiera dzielone biblioteki, które mog± byæ u¿ywane przez inne
aplikacje ROXa. To jest wersja dla GTK+2.

%package devel
Summary:	ROX-Lib2 library development files
Summary(pl):	Pliki programistyczne biblioteki ROX-Lib2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Documentation for developing applications using ROX-Lib2 library.

%description devel -l pl
Dokumentacja dla osób tworz±cych aplikacje u¿ywaj±ce biblioteki ROX-Lib2.

%prep
%setup -q -n rox-lib-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{_name}/{bin,Help/python,python/rox} \
	$RPM_BUILD_ROOT%{_libdir}/%{_name}/Messages

install %{_name}/App* $RPM_BUILD_ROOT%{_libdir}/%{_name}
install %{_name}/.DirIcon $RPM_BUILD_ROOT%{_libdir}/%{_name}
install %{_name}/python/rox/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
install %{_name}/Help/README $RPM_BUILD_ROOT%{_libdir}/%{_name}/Help
install %{_name}/Help/python/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/Help/python
install %{_name}/Messages/*.gmo $RPM_BUILD_ROOT%{_libdir}/%{_name}/Messages

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/{Changes,Errors,README,TODO,findrox.py}
%attr(755,root,root) %{_libdir}/%{_name}/AppRun
%attr(755,root,root) %{_libdir}/%{_name}/python/rox/suchild.sh
%{_libdir}/%{_name}/AppI*
%{_libdir}/%{_name}/.DirIcon
%dir %{_libdir}/%{_name}/Help
%{_libdir}/%{_name}/Help/README
%lang(de) %{_libdir}/%{_name}/Messages/de.gmo
%lang(fr) %{_libdir}/%{_name}/Messages/fr.gmo
%lang(it) %{_libdir}/%{_name}/Messages/it.gmo
%lang(pt_BR) %{_libdir}/%{_name}/Messages/pt_BR.gmo
%lang(zh_CN) %{_libdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_libdir}/%{_name}/Messages/zh_TW.gmo
%{_libdir}/%{_name}/python/rox/*.py[co]
%dir %{_libdir}/%{_name}
%dir %{_libdir}/%{_name}/Messages
%dir %{_libdir}/%{_name}/python
%dir %{_libdir}/%{_name}/python/rox

%files devel
%defattr(644,root,root,755)
%dir %{_libdir}/%{_name}/Help/python
%{_libdir}/%{_name}/Help/python/*.html
