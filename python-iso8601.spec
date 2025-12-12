Name:		python-iso8601
Version:	2.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/iso8601/iso8601-%{version}.tar.gz
Summary:	Simple module to parse ISO 8601 dates
URL:		https://pypi.org/project/iso8601/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
Simple module to parse ISO 8601 dates

%files
%{py_sitedir}/iso8601
%{py_sitedir}/iso8601-*.*-info
