Name:           perl-version
Version:        0.99
Release:        3%{?dist}
Epoch:          4
Summary:        Perl extension for Version Objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/version/
Source0:        http://cpan.metacpan.org//authors/id/J/JP/JPEACOCK/version-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.45
Requires:       perl(Test::More) >= 0.45
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Version objects were added to Perl in 5.10. This module implements version
objects for older version of Perl and provides the version object API for
all versions of Perl.

%prep
%setup -q -n version-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/version*
%{_mandir}/man3/*

%changelog
* Wed Jan 23 2013 David E. Wheeler <david.wheeler@iovation.com> 0.99-3
- Shortened the description.

* Wed Jan 23 2013 David E. Wheeler <david.wheeler@iovation.com> 0.99-2
- Set Epoch to 4.

* Sat Aug 04 2012 David E. Wheeler <david.wheeler@iovation.com> 0.99-1
- Specfile autogenerated by cpanspec 1.78.
