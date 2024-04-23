%global version 2
%global oname wayfire-rounded-corners

%global wfrc_commit 1e396e8b171df8703a1cb66585d14503e8e2292b
%global wfrc_shortcommit %(c=%{wfrc_commit}; echo ${c:0:7})

%global src0 wayfire-rounded-corners-%{wfrc_commit}

Name:           %{oname}-git
Version:        0.1.0^%{version}~git%{wfrc_shortcommit}
Release:        %autorelease
Summary:        Rounded corner plugin for Wayfire
License:        MIT
URL:            https://github.com/CharlieQLe/wayfire-rounded-corners

Source0:        https://github.com/CharlieQLe/wayfire-rounded-corners/archive/%{wfrc_commit}/wayfire-rounded-corners-%{wfrc_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.56.0
BuildRequires:  cmake(glm)

BuildRequires:  pkgconfig(wayfire) >= 0.9.0
BuildRequires:  pkgconfig(wf-config) >= 0.9.0
BuildRequires:  pkgconfig(wlroots) >= 0.17.2
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)

%description
Rounded corner plugin for Wayfire

%prep
%setup -n %src0

%build
%meson %{nil}

%meson_build
%install
%meson_install

%files
%license LICENSE
%{_datadir}/wayfire/metadata/rounded-corners.xml
%{_libdir}/wayfire/librounded-corners.so

%changelog
%autochangelog
