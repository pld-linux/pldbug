Summary:	Makes PLD's bug report sending easier
Summary(pl):	£atwe wysy³±nie raportów o b³edach w PLD
Name:		pldbug
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	ftp://sokrates.mimuw.edu.pl/pub/users/pawelk/%{name}-%{version}.tgz
Requires:	dml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script that allow you to send bug report to PLD in easy way. It has
got nice, text mode, user interface.

%description -l pl
Umo¿liwia ³atwe wysy³anie raportów o b³edach w PLD. Posiada zgrabny
interfejs u¿ytkownika.

%prep
%setup 

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install pldbug.sh $RPM_BUILD_ROOT%{_bindir}/pldbug

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pldbug
