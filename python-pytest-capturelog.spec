#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	py.test plugin to capture log messages
Summary(pl.UTF-8):	Wtyczka py.test do przechwytywania logowanych komunikatów
Name:		python-pytest-capturelog
Version:	0.7
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-capturelog
Source0:	https://pypi.python.org/packages/source/p/pytest-capturelog/pytest-capturelog-%{version}.tar.gz
# Source0-md5:	cfeac23d8ed254deaeb50a8c0aa141e9
URL:		https://bitbucket.org/memedough/pytest-capturelog/overview
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py.test plugin to capture log messages.

%description -l pl.UTF-8
Wtyczka py.test do przechwytywania logowanych komunikatów.

%package -n python3-pytest-capturelog
Summary:	py.test plugin to capture log messages
Summary(pl.UTF-8):	Wtyczka py.test do przechwytywania logowanych komunikatów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pytest-capturelog
py.test plugin to capture log messages.

%description -n python3-pytest-capturelog -l pl.UTF-8
Wtyczka py.test do przechwytywania logowanych komunikatów.

%prep
%setup -q -n pytest-capturelog-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/pytest_capturelog.py[co]
%{py_sitescriptdir}/pytest_capturelog-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-capturelog
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/pytest_capturelog.py
%{py3_sitescriptdir}/__pycache__/pytest_capturelog.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_capturelog-%{version}-py*.egg-info
%endif
