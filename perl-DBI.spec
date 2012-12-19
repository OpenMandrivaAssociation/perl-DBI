%define	module	DBI
%define	modver	1.616

Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	10

Summary:	The Perl Database Interface
License:	GPL
Group:		Development/Perl
URL:		http://dbi.perl.org/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBI/%{module}-%{modver}.tar.gz

BuildRequires:	perl(Storable) >= 1
BuildRequires:	perl(Test::Simple) >= 0.400.0
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3

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
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
rm -f t/zvg_85gofer
%make test

%install
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

# we don't want requires on Coro which is not even really used
rm -f %{buildroot}%{perl_vendorarch}/DBD/Gofer/Transport/corostream.pm

%files
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
%exclude %{perl_vendorarch}/DBI/ProfileDumper.pm
%exclude %{perl_vendorarch}/DBI/ProxyServer.pm
%{perl_vendorarch}/auto/DBI

%files proxy
%{_bindir}/dbiproxy
%{perl_vendorarch}/DBD/Proxy.pm
%{perl_vendorarch}/DBI/ProxyServer.pm
%{_mandir}/man1/dbiproxy.1.*
%{_mandir}/man3*/DBI::ProxyServer.3pm.*
%{_mandir}/man3*/DBD::Proxy.3pm.*

%files ProfileDumper-Apache
%{perl_vendorarch}/DBI/ProfileDumper
%{perl_vendorarch}/DBI/ProfileDumper.pm
%{_mandir}/man3*/DBI::ProfileDumper::Apache.3pm.*



%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.980.0-10
- rebuild for new perl 5.16.2
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.616.0-7
+ Revision: 765165
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.616.0-6
+ Revision: 763694
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.616.0-5
+ Revision: 763055
- rebuild

* Fri Jan 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.616.0-4
+ Revision: 762871
- Build for perl 5.14.x
- Fix duplicate packaging of ProfileDumper.pm

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.616.0-3
+ Revision: 667068
- mass rebuild

* Tue Jan 04 2011 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.616.0-2mdv2011.0
+ Revision: 628639
- using meta.yml to get upstream prereqs

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.616.0-1mdv2011.0
+ Revision: 626857
- new version

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.615.0-1mdv2011.0
+ Revision: 586087
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.613.0-2mdv2011.0
+ Revision: 564425
- rebuild for perl 5.12.1

* Tue Jul 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.613.0-1mdv2011.0
+ Revision: 561558
- update to 1.613

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.611.0-3mdv2011.0
+ Revision: 555306
- rebuild

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.611.0-1mdv2011.0
+ Revision: 551986
- update to 1.611

* Fri Jul 17 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.609.0-2mdv2010.1
+ Revision: 396881
- rebuild for new auto provides extraction

* Tue Jun 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.609-1mdv2010.0
+ Revision: 384240
- update to new version 1.609

* Wed May 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.608-1mdv2010.0
+ Revision: 372461
- update to new version 1.608

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.607-2mdv2009.1
+ Revision: 351713
- rebuild

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.607-1mdv2009.0
+ Revision: 242057
- update to new version 1.607

* Tue Jun 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.605-1mdv2009.0
+ Revision: 222659
- update to new version 1.605

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.604-1mdv2009.0
+ Revision: 193795
- update to new version 1.604

* Tue Feb 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.602-1mdv2008.1
+ Revision: 166548
- update to new version 1.602

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.601-3mdv2008.1
+ Revision: 151248
- rebuild for perl-5.10.0

* Fri Jan 04 2008 Olivier Thauvin <nanardon@mandriva.org> 1.601-2mdv2008.1
+ Revision: 144942
- rebuild to fix man permissions

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.601-1mdv2008.1
+ Revision: 104520
- update to new version 1.601

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.59-1mdv2008.0
+ Revision: 75271
- new version

* Fri Jul 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.58-1mdv2008.0
+ Revision: 53846
- new version

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.56-1mdv2008.0
+ Revision: 49136
- new version


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2007.1
+ Revision: 138896
- remove failing test, due to a timeout problem
- new version

* Fri Dec 15 2006 Scott Karns <scottk@mandriva.org> 1.53-1mdv2007.1
+ Revision: 97420
- CPAN release 1.53

* Thu Aug 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.52-1mdv2007.0
+ Revision: 54645
- 1.52
- Import perl-DBI

* Thu Jun 15 2006 Scott Karns <scottk@mandriva.org> 1.51-1mdv2007.0
- 1.51

* Sun May 07 2006 Scott Karns <scottk@mandriva.org> 1.50-3mdk
- Remove mdkversion conditional surrounding BuildRequires perl-devel.
  (Needed for arch specific perl packages.)

* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 1.50-2mdk
- Updated BuildRequires, source URL

* Thu Dec 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.50-1mdk
- 1.50

* Wed Nov 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.49-1mdk
- 1.49

* Sat Apr 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.48-1mdk
- 1.48
- Remove requires on release for subpackages

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.47-1mdk
- 1.47

* Fri Nov 26 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.46-1mdk
- 1.46

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.45-2mdk
- rebuild for new perl

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.45-1mdk
- New version 1.45.
- Add Tim's development roadmap to docs, but not in perl's install tree.
- Remove manpages of Windows-specific modules (not installed)

* Thu Jul 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.43-2mdk
- Rebuild for new perl.
- Description nits.

* Tue Jul 06 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.43-1mdk
- 1.43

* Thu Apr 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.42-1mdk
- 1.42
- use %%make and %%makeinstall_std macro
- drop prefix
- spec cosmetics

