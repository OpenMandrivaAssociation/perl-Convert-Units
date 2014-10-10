%define upstream_name    Convert-Units
%define upstream_version 0.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert-Units module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Convert/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Units package is a collection of modules for parsing strings with unit
measurements (such as "12pt" or "3 meters") and converting them to some other
unit (such as "picas" or "inches").

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Convert/Units
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.430.0-2mdv2011.0
+ Revision: 680848
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 504939
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.43-5mdv2010.0
+ Revision: 430339
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.43-4mdv2009.0
+ Revision: 241193
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-2mdv2008.0
+ Revision: 86232
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.43-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.43-1mdk
- initial Mandriva package

