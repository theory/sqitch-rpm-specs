Name:           perl-Mouse
Version:        1.04
Release:        1%{?dist}
Summary:        Moose minus the antlers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mouse/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Mouse-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 1:5.6.2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Moose is a postmodern object system for Perl5. Moose is wonderful.

Unfortunately, Moose has a compile-time penalty. Though significant progress
has been made over the years, the compile time penalty is a non-starter for
some very specific applications. If you are writing a command-line application
or CGI script where startup time is essential, you may not be able to use
Moose (we recommend that you instead use persistent Perl executing
environments like FastCGI for the latter, if possible).

Mouse is a Moose compatible object system, which aims to alleviate this
penalty by providing a subset of Moose's functionality.

%prep
%setup -q -n Mouse-%{version}

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
%{perl_vendorarch}/Mouse*
%{perl_vendorarch}/Squirrel*
%{perl_vendorarch}/Test/Mouse*
%{perl_vendorarch}/ouse**
%{_mandir}/man3/*

%changelog
* Fri Jan 11 2013 David E. Wheeler <david.wheeler@iovation.com> 1.04-1
- Specfile autogenerated by cpanspec 1.78.