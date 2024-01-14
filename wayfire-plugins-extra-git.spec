%global version 1

%global wpe_commit 5386f5219eb2071dfd255836d91ef953d779c47f
%global wpe_shortcommit %(c=%{wpe_commit}; echo ${c:0:7})

%global src0 wayfire-plugins-extra-%{wpe_commit}

Name:           wayfire-plugins-extra
Version:        0.9.0^%{version}~git%{wpe_shortcommit}
Release:        %autorelease
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire-plugins-extra

Source0:        https://github.com/WayfireWM/wayfire-plugins-extra/archive/%{wpe_commit}/wayfire-plugins-extra-%{wpe_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libevdev-devel
BuildRequires:  meson >= 0.56.0
BuildRequires:  cmake(glm)

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(wayfire) >= 0.9.0
BuildRequires:  pkgconfig(wf-config) >= 0.9.0
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)

%description
Additional plugins for Wayfire

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -n %src0

%build
%meson %{nil}

%meson_build
%install
%meson_install

%files
%license LICENSE
%{_datadir}/wayfire/metadata
%{_libdir}/wayfire/

%changelog
%autochangelog
