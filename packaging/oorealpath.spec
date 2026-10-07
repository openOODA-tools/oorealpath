Name:           oorealpath
Version:        0.1.0
Release:        1%{?dist}
Summary:        Resolves all symlinks, relative components, and canonicalizes absolute path roots.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oorealpath
Source0:        oorealpath-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oorealpath is a sovereign, capability-bounded CANONICAL PATH written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oorealpath
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oorealpath-uninstall

%files
/usr/bin/oorealpath
/usr/bin/oorealpath-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
