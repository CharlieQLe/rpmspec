%global debug_package %{nil}
%global commit 1a032fb4dd76f3f5496955d293eab2ea90f7fc15
%global commit_short %(c=%{commit}; echo ${c:0:7})

Name: sysboard
Version: 9.9.9.git.%{commit_short}
Release: 1
Summary: Sysboard is a simple virtual keyboard (On screen keyboard) for wayland written in gtkmm 4
License:        GPL-3.0-only
URL: https://github.com/System64fumo/sysboard
Source: https://github.com/System64fumo/sysboard/archive/%{commit}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(gtk4-layer-shell-0)

%description
%summary

%prep
%setup -n %name-%{commit}

%build
%make_build

%install
%make_install PREFIX=%_prefix

%files
%license LICENSE
%doc README.md
%_bindir/sysboard
%_datadir/sys64/board/style.css
%_datadir/sys64/board/config.conf
%_prefix/lib/libsysboard.so

%changelog
%autochangelog
