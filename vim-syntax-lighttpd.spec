%define		syntax	lighttpd
Summary:	Vim syntax: lighttpd
Name:		vim-syntax-%{syntax}
Version:	1.19
Release:	1
License:	Charityware
Group:		Applications/Editors/Vim
Source0:	https://github.com/glensc/vim-syntax-lighttpd/archive/v%{version}/%{syntax}-%{version}.tar.gz
# Source0-md5:	b1c104b2371d5a721e2b729c4df1ed47
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
This package provides syntax highlighting for lighttpd config files.

%prep
%setup -q

%build
ver=$(awk '/Version Info:/{print $4}' syntax/%{syntax}.vim)
if [ "$ver" != "%{version}" ]; then
	: Update version $ver, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a syntax ftdetect $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc syntax.sh
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
