Name:          ostree-rollback-to-rescue
Version:       0.1
Release:       1%{?dist}
Summary:       A systemd service that will rollback to rescue.target
License:       GPLv2
URL:           https://github.com/ericcurtin/ostree-rollback-to-rescue
Requires:      ostree
Source0:       ostree-rollback-to-rescue.service
Source1:       ostree-rollback-to-rescue

%description
%{summary}

%prep

%build

%install
install -D -m644 %{SOURCE0} ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.service
install -D -m700 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_sbindir}/ostree-rollback-to-rescue

%post
%systemd_post ostree-rollback-to-rescue.service

%preun
%systemd_preun ostree-rollback-to-rescue.service

%files
%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.service
%{_sbindir}/ostree-rollback-to-rescue

%changelog
* Thu Jan 18 2024 Eric Curtin <ecurtin@redhat.com> 0.1-1
- A systemd unit file that will rollback to rescue.target if we are
  not booted into the latest ostree deployment.

