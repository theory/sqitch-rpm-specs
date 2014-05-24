Name:           perl-Term-ANSIColor
Version:        3.02
Release:        1%{?dist}
Summary:        Color screen output using ANSI escape sequences
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-ANSIColor/
Source0:        http://cpan.metacpan.org//authors/id/R/RR/RRA/Term-ANSIColor-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), and colorvalid(), which have to be explicitly imported to be
used (see "SYNOPSIS").

%prep
%setup -q -n Term-ANSIColor-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# Delete man file to avoid conflict with perl-4:5.10.1-119.el6_1.1.x86_64.
# Yes, this is a hack. http://www.dark.ca/2010/04/08/cpan-rpms-in-rhel-centos/fg
find $RPM_BUILD_ROOT -type f -name '*.3pm' -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/*
#%{_mandir}/man3/*

%changelog
* Thu Aug 02 2012 David E. Wheeler <david.wheeler@iovation.com> 3.02-1
- Specfile autogenerated by cpanspec 1.78.