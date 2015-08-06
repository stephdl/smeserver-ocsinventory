# $Id: smeserver-ocsinventory.spec,v 1.7 2013/12/15 18:39:44 unnilennium Exp $
# Authority: vip-ire
# Name: Daniel Berteaud

Summary: Open Computer and Software Inventory Next Generation (SME Server integration)
%define name smeserver-ocsinventory
Name: %{name}
%define version 0.3
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz

URL: http://sme.firewall-services.com
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 9.0
Requires: ocsinventory-server
Requires: ocsinventory-reports

Conflicts: smeserver-inventory-tools

%description
Open Computer and Software Inventory Next Generation is an application
designed to help a network or system administrator keep track of the
computers configuration and software that are installed on the network.

OCS Inventory is also able to detect all active devices on your network,
such as switch, router, network printer and unattended devices.

OCS Inventory NG includes package deployment feature on client computers

%changelog
* Thu Aug 06 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 0.3-1.sme
- Initial release to sme9

* Sun Dec 15 2013 JP Pialasse <tests@pialasse.com> 0.1-14.sme
- Can't exec "rpm" fix 

* Sat May 25 2013 JP Pialasse <tests@pialasse.com> 0.1-13.sme
- reversing previous changes, wrong rpm

* Sat May 25 2013 JP Pialasse <tests@pialasse.com> 0.1-12.sme
- added requirement that were to be installed from wiki manually

* Tue May 04 2010 Daniel B. <daniel@firewall-services.com> 0.1-11.sme
- Check if cacert size is zero

* Thu Jun 18 2009 Daniel B. <daniel@firewall-services.com> 0.1-10
- Fixe inventory access

* Mon Jun 15 2009 Daniel B. <daniel@firewall-services.com> 0.1-9
- expand php.ini template during ocs-update event

* Wed Mar 25 2009 Daniel B. <daniel@firewall-services.com> 0.1-8
- Should work with any perl version
- Update cacert if it has changed

* Thu Mar 19 2009 Daniel B. <daniel@firewall-services.com> 0.1-7
- Update paths to the new "download" directory /var/lib/ocsinventory-reports

* Wed Mar 18 2009 Daniel B. <daniel@firewall-services.com> 0.1-6
- Correct openbasedir directive so package creation works

* Mon Mar 16 2009 Daniel B. <daniel@firewall-services.com> 0.1-5
- Conflicts with smeserver-inventory-tools

* Tue Dec 09 2008 Daniel B. <daniel@firewall-services.com> 0.1-4
- Add a link in the server-manager
- expand mysql fragment during ocs-update event

* Tue Oct 21 2008 Daniel B. <daniel@firewall-services.com> 0.1-3
- correct templates2expand for ocs-update event

* Wed Oct 17 2008 Daniel B. <daniel@firewall-services.com> 0.1-2
- Compatibility with mod_perl 2
- Change config path

* Thu Sep 10 2008 Daniel B. <daniel@firewall-services.com> 0.1-0
- Initial RPM


%prep
%setup

%build
/usr/bin/perl createlinks

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-, root, root, -)

%clean
rm -rf $RPM_BUILD_ROOT


