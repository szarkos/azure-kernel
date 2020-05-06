Name:		centos-release-azure
Summary:	Yum configuration for CentOS Virt SIG Azure repo
Version:        1.1
Release:        1%{?dist}

Group:		System Environment/Base
License:	GPLv2

URL:		https://wiki.centos.org/SpecialInterestGroup/Virtualization
Source0:	CentOS-Azure.repo

Provides:	centos-release-azure
Requires:	centos-release-virt-common

BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
Vendor:		Microsoft Corporation
Packager:	Microsoft Corporation


%description
Yum repo configuration for kernel and userspace packages built for Microsoft Azure. These are provided via the CentOS Virtualization SIG repositories.

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Azure.repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Azure.repo

%changelog
* Fri May 01 2020 Stephen A. Zarkos <steve@sentry.net> - 1.1-1
- Update repository name from 'azure' to 'azure-kernel' (CentOS bug #17302)

* Thu Jul 26 2018 Stephen A. Zarkos <stephen.zarkos@microsoft.com> - 1.0-2
- Minor .repo file update

* Fri Jun 22 2018 Stephen A. Zarkos <stephen.zarkos@microsoft.com> - 1.0-1
- Initial release

