Name:           perl-Moo
Version:        1.005000
Release:        1%{?dist}
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Moo/
Source0:        http://cpan.metacpan.org//authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Method::Modifiers) >= 1.1
BuildRequires:  perl(Class::XSAccessor) >= 1.18
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.11
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Import::Into) >= 1.002
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Role::Tiny) >= 1.003003
BuildRequires:  perl(strictures) >= 1.004003
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Class::Method::Modifiers) >= 1.1
Requires:       perl(Class::XSAccessor) >= 1.18
Requires:       perl(Devel::GlobalDestruction) >= 0.11
Requires:       perl(Import::Into) >= 1.002
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(Role::Tiny) >= 1.003003
Requires:       perl(strictures) >= 1.004003
Requires:       perl(Sub::Name)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is an extremely light-weight subset of Moose optimised for
rapid startup and "pay only for what you use".

%prep
%setup -q -n Moo-%{version}

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
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 29 2014 David E. Wheeler <david.wheeler@iovation.com> 1.005000-1
- Specfile autogenerated by cpanspec 1.78.
