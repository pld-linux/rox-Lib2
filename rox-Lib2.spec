%define _name ROX-Lib2
Summary:	A library for ROX applications
Summary(pl):	Biblioteka dla aplikacji ROXa
Name:		rox-Lib2
Version:	1.9.15
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/rox/rox-lib-%{version}.tgz
# Source0-md5:	439d54bf80ebcd2a83ea9acd2b22e7e3
URL:		http://rox.sourceforge.net/rox_lib.php3
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk-gtk
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROX-Lib contains shared code which can be used by other ROX
applications. It is a GTK+2 version.

%description -l pl
ROX-Lib zawiera dzielone biblioteki, które mog± byæ u¿ywane przez inne
aplikacje ROXa. To jest wersja dla GTK+2.

%prep
%setup -q -n rox-lib-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{_name}/{bin,Help,python/rox} \
	$RPM_BUILD_ROOT%{_libdir}/%{_name}/Messages

install %{_name}/App* $RPM_BUILD_ROOT%{_libdir}/%{_name}
install %{_name}/.DirIcon $RPM_BUILD_ROOT%{_libdir}/%{_name}
install %{_name}/python/*.py $RPM_BUILD_ROOT%{_libdir}/%{_name}/python
install %{_name}/python/rox/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
install %{_name}/Help/README $RPM_BUILD_ROOT%{_libdir}/%{_name}/Help
install %{_name}/Messages/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/Messages

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/{Changes,findrox.py,python}
%attr(755,root,root) %{_libdir}/%{_name}/AppRun
%attr(755,root,root) %{_libdir}/%{_name}/Messages
%attr(755,root,root) %{_libdir}/%{_name}/python/make_docs.py
%{_libdir}/%{_name}/AppI*
%{_libdir}/%{_name}/.DirIcon
%{_libdir}/%{_name}/Help
%{_libdir}/%{_name}/python/rox/*.py[co]
%dir %{_libdir}/%{_name}
%dir %{_libdir}/%{_name}/python
%dir %{_libdir}/%{_name}/python/rox
