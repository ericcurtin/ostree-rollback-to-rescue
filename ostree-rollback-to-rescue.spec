Name:           ostree-rollback-to-rescue
Version:        0.1
Release:        1%{?dist}
Summary:        A systemd unit file that will rollback to rescue.target if we are not booted into the latest ostree deployment

License:        GPLv2
Source0:        ostree-rollback-to-rescue.spec

%description
%{summary}

%build

%install
install -D -m644 %{SOURCE0} ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.spec

%files
%{_prefix}/lib/systemd/system/ostree-rollback-to-rescue.spec

%changelog
* Thu Jan 18 2024 Eric Curtin <ecurtin@redhat.com>
- A systemd unit file that will rollback to rescue.target if we are
  not booted into the latest ostree deployment.

