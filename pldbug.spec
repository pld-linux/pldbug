Summary:	Makes PLD's bug report sending easier
Summary(pl):	£atwe wysy³anie raportów o b³êdach w PLD
Name:		pldbug
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://sokrates.mimuw.edu.pl/pub/users/pawelk/%{name}-%{version}.tgz
# Source0-md5:	cf7e7edf500714e2054f8cd1cfe0e1a9
Requires:	dml
Requires:	mailx
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script that allows you to send bug report to PLD in easy way. It has
got nice, text mode, user interface.

%description -l pl
Ten skrypt umo¿liwia ³atwe wysy³anie raportów o b³êdach w PLD. Posiada
zgrabny interfejs u¿ytkownika.

%prep
%setup 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pldbug.sh $RPM_BUILD_ROOT%{_bindir}/pldbug

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pldbug
