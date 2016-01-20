Name: sailfishos-patch-camera-quickactions
BuildArch: noarch
Summary: Adds quick actions to take photos and record videos
Version: 0.2
Release: 1
Group: System/Patches
Vendor: AliNa
License: GPLv3
Source0: %{name}-%{version}.tar.xz
Conflicts: sailfishos-patch-quickaction-photo
Conflicts: sailfishos-patch-quickaction-video
Requires: sailfish-version >= 2.0.1

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

mkdir -p %{buildroot}/usr/share/lipstick/quickactions
cp -r quickactions/* %{buildroot}/usr/share/lipstick/quickactions
mkdir -p %{buildroot}/usr/share/themes/sailfish-default/meegotouch/z1.0/icons
cp icons/* %{buildroot}/usr/share/themes/sailfish-default/meegotouch/z1.0/icons
mkdir -p %{buildroot}/usr/share/translations
cp -r translations/* %{buildroot}/usr/share/translations

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/lipstick/quickactions
%{_datadir}/themes/sailfish-default/meegotouch/z1.0/icons/
%{_datadir}/translations
