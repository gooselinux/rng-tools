
%global _sbindir /sbin

Summary:	Random number generator related utilities
Name:		rng-tools
Version:	2
Release:	8%{?dist}
Group:		System Environment/Base
License:	GPLv2+
URL:		http://sourceforge.net/projects/gkernel/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source0:	http://downloads.sourceforge.net/gkernel/rng-tools-%{version}.tar.gz
Patch0:		rng-tools-2-devname.patch
Patch1:		rng-tools-2-tpm.patch
Patch2:		rng-tools-2-warnings.patch
Patch3:		rng-tools-2-xread-retval.patch
Patch4:		rng-tools-2-failures-disable.patch

Requires:	chkconfig initscripts
BuildRequires:	automake autoconf groff gettext
Obsoletes:	rng-utils <= 1:2.0-4.1

%description
Hardware random number generation tools.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/rngtest
%{_sbindir}/rngd
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*

%changelog
* Mon Aug 23 2010 Jeff Garzik <jgarzik@redhat.com> - 2-8
- Resolves: bz#624530
- Fix loop on bad RNG

* Fri May 28 2010 David Howells <dhowells@rehdat.com> - 2-7
- Resolves: bz#597221
- Fix some compiler warnings thus dealing with the SEGV
- Make do_loop() correctly interpret the result of iter->xread()

* Fri Mar 26 2010 Jeff Garzik <jgarzik@redhat.com> - 2-6
- Resolves: bz#576678
- increase version number of rng-utils that we obsolete
- use global rather than define, for sbindir (Fedora pkg review)
- improve BuildRoot (Fedora pkg review)

* Thu Mar 25 2010 Jeff Garzik <jgarzik@redhat.com> - 2-5
- Fix specfile error preventing TPM patch from being applied
- Resolves: bz#530012

* Thu Mar 25 2010 Jeff Garzik <jgarzik@redhat.com> - 2-4
- Add TPM patch from Dell
- Resolves: bz#530012

* Thu Mar 25 2010 Jeff Garzik <jgarzik@redhat.com> - 2-3
- Related: bz#576678
- bump release number due to tag confusion w/ devel branch

* Thu Mar 25 2010 Jeff Garzik <jgarzik@redhat.com> - 2-2
- Related: bz#576678
- several minor updates from Fedora package review

* Wed Mar 24 2010 Jeff Garzik <jgarzik@redhat.com> - 2-1
- initial revision (as rng-tools)

