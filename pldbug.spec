%define _short_name 	mwcls
Summary:	Makes PLD's bug report sending easier
Summary(pl):	£atwe wysy³±nie raportów o b³edach w PLD
Name:		pldbug
Version:	1.0
Release:	1
License:	GPL
Group:		Utilities/Console
Source0:	ftp://sokrates.mimuw.edu.pl/pub/users/pawelk/pldbug-%{version}.tgz
Requires:	dml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script that allow you to send bug report to PLD in easy way. It has got nice,
text mode, user interface. 


%description -l pl
Umo¿liwia ³atwe wysy³anie raportów o b³edach w PLD. Posiada zgrabny interfejs
u¿ytkownika.

%prep
%setup  -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d pldbug.sh $RPM_BUILD_ROOT%{_bindir}/pldbug 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_bindir}/pldbug
