Name:           perl-MouseX-Types
Version:        0.06
Release:        1%{?dist}
Summary:        MouseX::Types Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MouseX-Types/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/MouseX-Types-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.2
BuildRequires:  perl(Any::Moose) >= 0.15
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mouse) >= 0.77
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(Any::Moose) >= 0.15
Requires:       perl(Mouse) >= 0.77
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MouseX::Types Perl module

%prep
%setup -q -n MouseX-Types-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 11 2013 David E. Wheeler <david.wheeler@iovation.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.