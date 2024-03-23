%global version 8
%global oname wayfire

%global wayfire_commit 101dad07f2bc7d3ebf0fdedf0a32e3fbb07e469b
%global wayfire_shortcommit %(c=%{wayfire_commit}; echo ${c:0:7})

%global wfconfig_commit aba330e7e22bbbeb5147af6e2cb0f30fb840cdd8
%global wfconfig_shortcommit %(c=%{wfconfig_commit}; echo ${c:0:7})

%global wfutils_commit 15f8e16721585ae3eaf278ba71d7064237eb23f5
%global wfutils_shortcommit %(c=%{wfutils_commit}; echo ${c:0:7})

%global wftouch_commit 8974eb0f6a65464b63dd03b842795cb441fb6403
%global wftouch_shortcommit %(c=%{wftouch_commit}; echo ${c:0:7})

%global src0 wayfire-%{wayfire_commit}

Name:           %{oname}-git
Version:        0.9.0^%{version}~git%{wayfire_shortcommit}
Release:        %autorelease
Summary:        3D wayland compositor
License:        MIT
URL:            https://github.com/WayfireWM/wayfire

Source0:        https://github.com/WayfireWM/wayfire/archive/%{wayfire_commit}/wayfire-%{wayfire_shortcommit}.tar.gz
Source1:        https://github.com/WayfireWM/wf-utils/archive/%{wfutils_commit}/wf-utils-%{wfutils_shortcommit}.tar.gz
Source2:        https://github.com/WayfireWM/wf-touch/archive/%{wftouch_commit}/wf-touch-%{wftouch_shortcommit}.tar.gz
Source3:        https://github.com/WayfireWM/wf-config/archive/%{wfconfig_commit}/wf-touch-%{wfconfig_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson >= 0.56.0

BuildRequires:  cmake(doctest)
BuildRequires:  cmake(glm)

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots) >= 0.17.1
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

Provides:       bundled(wf-touch) = 0.0~git%{wftouch_commit}
Provides:       bundled(wf-utils) = 0.0~git%{wfutils_commit}
Provides:       bundled(wf-config) = 0.9.0~git%{wfconfig_commit}

Conflicts:	wayfire
Provides:       wayfire = %{version}-%{release}

%description
Wayfire is a 3D Wayland compositor, inspired by Compiz and based on wlroots.
It aims to create a customizable, extendable and lightweight environment
without sacrificing its appearance.

%package        devel
Summary:        Development files for %{oname}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{oname}.

%prep
%setup -n %src0
tar -xf %{SOURCE1} -C subprojects/wf-utils --strip=1
tar -xf %{SOURCE2} -C subprojects/wf-touch --strip=1
tar -xf %{SOURCE3} -C subprojects/wf-config --strip=1

%build
%meson                            \
    -Duse_system_wfconfig=disabled \
    -Duse_system_wlroots=enabled  \
    %{nil}

%meson_build
%install
%meson_install
install -D -p -m 0644 %{oname}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{oname}.desktop
rm -f %{buildroot}%{_libdir}/libwftouch.a
# Duplicate man file
rm -f %{buildroot}%{_prefix}/man/%{oname}.1
rm -rf %{buildroot}%{_prefix}/lib

%files
%license LICENSE
%doc README.md %{oname}.ini
%{_bindir}/%{oname}
%{_datadir}/%{oname}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{oname}/
%{_libdir}/libwf-config.so*
%{_libdir}/libwf-utils.so*
%{_libdir}/lib%{oname}-blur-base.so
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{oname}/
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
