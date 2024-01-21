Name:           ostree-rollback-to-rescue
Version:        0.1
Release:        1%{?dist}
Summary:        A systemd unit file that will rollback to rescue.target if we are not booted into the latest ostree deployment
License:        GPLv2
Requires:       ostree
Source0:        ostree-rollback-to-rescue.spec
Source1:        ostree-rollback-to-rescue

%description
%{summary}

%build

%install
install -D -m644 %{SOURCE0} ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.spec
install -D -m700 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_sbindir}/ostree-rollback-to-rescue

%files
%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.spec
%{_sbindir}/ostree-rollback-to-rescue

%changelog
* Thu Jan 18 2024 Eric Curtin <ecurtin@redhat.com>
- A systemd unit file that will rollback to rescue.target if we are
  not booted into the latest ostree deployment.

