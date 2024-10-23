%global debug_package %{nil}
%global git_commit 84ee9f08adb1b7e50325ddfe85044bd78788e96f
%global git_shortcommit %(c=%{git_commit}; echo ${c:0:7})

Name:       nautilus-open-in-blackbox
Version:    1.0
Release:    %autorelease
Summary:    Adds a button to open BlackBox Terminal to the Nautilus menu

License:    GNUv3
URL:        https://github.com/ppvan/nautilus-open-in-blackbox
Source0:    https://github.com/ppvan/nautilus-open-in-blackbox/archive/%{git_commit}/nautilus-open-in-blackbox-%{git_shortcommit}.tar.gz

Requires: blackbox-terminal
Requires: nautilus
Requires: nautilus-extensions
Requires: nautilus-python

%description
Adds a button to open BlackBox Terminal to the Nautilus menu.

%prep
%autosetup -n nautilus-open-in-blackbox-%{git_commit}

%install
mkdir -p %{buildroot}/%{_datadir}/nautilus-python/extensions/
cp nautilus-open-in-blackbox.py %{buildroot}/%{_datadir}/nautilus-python/extensions/

%files
%license LICENSE
%doc README.md
%attr(644, root, root) %{_datadir}/nautilus-python/extensions/nautilus-open-in-blackbox.py