Summary: A portable (Linux, Mac, BSD) bashrc file for a better bash prompt and other enhancments
Name: ninjab
Version: %(grep "^##" CHANGELOG.md | head -n 1 | awk {'print $2'})
Release: 1
License: GPL
Group: System Tools
URL: https://github.com/xeor/bashrc
Packager: Lars Solberg <lars.solberg@gmail.com>
buildarch: noarch

%description
Ninjab Is Not Just Another Bashrc

%build
cd %git_dir
install -o root -g root -m 0755 -d %{buildroot}/etc
install -o root -g root -m 0755 config %{buildroot}/etc/ninjab.conf
install -o root -g root -m 0755 -d %{buildroot}/usr/share/ninjab
install -o root -g root -m 0755 functions %{buildroot}/usr/share/ninjab/
install -o root -g root -m 0755 loader %{buildroot}/usr/share/ninjab/
install -o root -g root -m 0755 -d %{buildroot}/usr/share/ninjab/parts
install -o root -g root -m 0755 parts/* %{buildroot}/usr/share/ninjab/parts

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/ninjab.conf
/usr/share/ninjab
/usr/share/ninjab/functions
/usr/share/ninjab/loader
/usr/share/ninjab/parts/*

