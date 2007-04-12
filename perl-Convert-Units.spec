%define real_name Convert-Units

Summary:	Convert-Units module for perl 
Name:		perl-%{real_name}
Version:	0.43
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Units package is a collection of modules for parsing strings with unit
measurements (such as "12pt" or "3 meters") and converting them to some other
unit (such as "picas" or "inches").

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Convert/Units
%{_mandir}/*/*


