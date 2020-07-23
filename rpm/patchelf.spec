Name:       patchelf
Summary:    A utility for patching ELF binaries
Version:    0.11
Release:    1
License:    GPLv3+
URL:        http://nixos.org/patchelf.html
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-Disable-failing-test.patch

%description
PatchELF is a simple utility for modifing existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
autoreconf -v -f -i

%configure --disable-static
make %{?jobs:-j%jobs}

%if ! 0%{?qemu_user_space_build}
make check
%endif

%install
rm -rf %{buildroot}
%make_install

strip $RPM_BUILD_ROOT/%{_prefix}/bin/* || true
rm -rf $RPM_BUILD_ROOT/%{_datadir}/man

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/patchelf
%{_datadir}/doc/patchelf/README.md
