%define upstream_name    Convert-Units
%define upstream_version 0.43
Name:		perl-%{upstream_name}
Version:	0.43
Release:	3

Summary:	Convert-Units module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Convert-Units
Source0:	https://cpan.metacpan.org/authors/id/R/RR/RRWO/Convert-Units-0.43.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Units package is a collection of modules for parsing strings with unit
measurements (such as "12pt" or "3 meters") and converting them to some other
unit (such as "picas" or "inches").

%prep
%setup -q -n Convert-Units-0.43

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
make test || :
%make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Convert/Units
%{_mandir}/*/*


