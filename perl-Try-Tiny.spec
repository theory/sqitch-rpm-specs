Name:           perl-Try-Tiny
Version:        0.09
Release:        1%{?dist}
Summary:        Minimal try/catch with proper localization of $@
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Try-Tiny/
Source0:        http://www.cpan.org/modules/by-module/Try/Try-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
#Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides bare bones try/catch/finally statements that are
designed to minimize common mistakes with eval blocks, and NOTHING else.

%prep
%setup -q -n Try-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Feb 14 2011 Jeff Lavallee <jeff.lavallee@iovation.com> 0.09-1
- Specfile autogenerated by cpanspec 1.77.
