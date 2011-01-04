%define upstream_name	 DBI
%define upstream_version 1.616

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	The Perl Database Interface
License:	GPL
Group:		Development/Perl
URL:		http://dbi.perl.org/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Storable) >= 1
BuildRequires:	perl(Test::Simple) >= 0.400.0
BuildRequires:	perl-devel

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Perl Database Interface (DBI) is a database access Application Programming
Interface (API) for the Perl Language. The Perl DBI API specification defines a
set of functions, variables and conventions that provide a consistent database
interface independent of the actual database being used.

%package	proxy
Group:		Development/Perl
Summary: 	DBI proxy server and client
Requires:	%{name} = %{version}

%description	proxy
DBI::ProxyServer is a module for implementing a proxy for the DBI
proxy driver, DBD::Proxy.
DBD::Proxy is a Perl module for connecting to a database via a remote
DBI driver.

%package	ProfileDumper-Apache
Group:		Development/Perl
Summary: 	DBI profiling data for mod_perl
Requires:	%{name} = %{version}

%description ProfileDumper-Apache
This module interfaces DBI::ProfileDumper to Apache/mod_perl. Using this
module you can collect profiling data from mod_perl applications. It
works by creating a DBI::ProfileDumper data file for each Apache
process. These files are created in your Apache log directory. You can
then use dbiprof to analyze the profile files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make CFLAGS="%{optflags}"

%check
rm -f t/zvg_85gofer
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

# remove Win32 stuff
rm -rf %{buildroot}%{perl_vendorarch}/Win32
rm -f %{buildroot}%{perl_vendorarch}/DBI/W32ODBC.pm
rm -f %{buildroot}%{perl_vendorarch}/Roadmap.pod
rm -f %{buildroot}%{perl_vendorarch}/DBI/Roadmap.pm
rm -f %{buildroot}%{perl_vendorarch}/TASKS.pod
rm -f %{buildroot}%{perl_vendorarch}/DBI/TASKS.pm
rm -f %{buildroot}%{_mandir}/man3*/Win32::DBIODBC.3pm*
rm -f %{buildroot}%{_mandir}/man3*/DBI::W32ODBC.3pm*
rm -f %{buildroot}%{_mandir}/man3*/Roadmap.3pm*
rm -f %{buildroot}%{_mandir}/man3*/TASKS.3pm*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_bindir}/dbiprof
%{_bindir}/dbilogstrip
%{_mandir}/*/*
%exclude %{_mandir}/man1/dbiproxy.1*
%exclude %{_mandir}/man3*/DBD::Proxy.3pm*
%exclude %{_mandir}/man3*/DBI::ProxyServer.3pm*
%exclude %{_mandir}/man3*/DBI::ProfileDumper::Apache.3pm*
%{perl_vendorarch}/Bundle
%{perl_vendorarch}/DBD
%{perl_vendorarch}/dbixs_rev.pl
%exclude %{perl_vendorarch}/DBD/Proxy.pm
%{perl_vendorarch}/DBI.pm
%{perl_vendorarch}/DBI
%exclude %{perl_vendorarch}/DBI/ProfileDumper
%exclude %{perl_vendorarch}/DBI/ProxyServer.pm
%{perl_vendorarch}/auto/DBI

%files proxy
%defattr(-,root,root)
%{_bindir}/dbiproxy
%{perl_vendorarch}/DBD/Proxy.pm
%{perl_vendorarch}/DBI/ProxyServer.pm
%{_mandir}/man1/dbiproxy.1.*
%{_mandir}/man3*/DBI::ProxyServer.3pm.*
%{_mandir}/man3*/DBD::Proxy.3pm.*

%files ProfileDumper-Apache
%defattr(-,root,root)
%{perl_vendorarch}/DBI/ProfileDumper
%{perl_vendorarch}/DBI/ProfileDumper.pm
%{_mandir}/man3*/DBI::ProfileDumper::Apache.3pm.*

