%global wayfire_commit d4360a8ab1a9555e511e7330e9dae65aa52cd6de
%global wayfire_shortcommit %(c=%{wayfire_commit}; echo ${c:0:7})

%global wfconfig_commit 3da1c2254e645ba139b0db268349eb00d65162a6
%global wfconfig_shortcommit %(c=%{wfconfig_commit}; echo ${c:0:7})

%global wfutils_commit 15f8e16721585ae3eaf278ba71d7064237eb23f5
%global wfutils_shortcommit %(c=%{wfutils_commit}; echo ${c:0:7})

%global wftouch_commit 8974eb0f6a65464b63dd03b842795cb441fb6403
%global wftouch_shortcommit %(c=%{wftouch_commit}; echo ${c:0:7})

%global wlroots_commit 767eedd3cbe9900687bf3b82236320dcd7b77aae
%global wlroots_shortcommit %(c=%{wlroots_commit}; echo ${c:0:7})

%global src0 wayfire-%{wayfire_commit}

Name:           wayfire
Version:        0.9.0~git%{wayfire_shortcommit}
Release:        %autorelease
Summary:        3D wayland compositor
License:        MIT
URL:            https://github.com/WayfireWM/wayfire

Source0:        https://github.com/WayfireWM/wayfire/archive/%{wayfire_commit}/wayfire-%{wayfire_shortcommit}.tar.gz
Source1:        https://github.com/WayfireWM/wf-utils/archive/%{wfutils_commit}/wf-utils-%{wfutils_shortcommit}.tar.gz
Source2:        https://github.com/WayfireWM/wf-touch/archive/%{wftouch_commit}/wf-touch-%{wftouch_shortcommit}.tar.gz
Source3:        https://github.com/WayfireWM/wf-config/archive/%{wfconfig_commit}/wf-touch-%{wfconfig_shortcommit}.tar.gz
Source4:        https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/%{wlroots_commit}/wlroots-%{wlroots_shortcommit}.tar.gz

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
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
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
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

Provides:       bundled(wf-touch) = 0.0~git%{wftouch_commit}
Provides:       bundled(wf-utils) = 0.0~git%{wfutils_commit}
Provides:       bundled(wf-config) = 0.9.0~git%{wfconfig_commit}
Provides:       bundled(wlroots) = 0.17.0~git%{wlroots_commit}

%description
Wayfire is a 3D Wayland compositor, inspired by Compiz and based on wlroots.
It aims to create a customizable, extendable and lightweight environment
without sacrificing its appearance.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -n %src0
tar -xf %{SOURCE1} -C subprojects/wf-utils --strip=1
tar -xf %{SOURCE2} -C subprojects/wf-touch --strip=1
tar -xf %{SOURCE3} -C subprojects/wf-config --strip=1
tar -xf %{SOURCE4} -C subprojects/wlroots --strip=1

%build
%meson                            \
    -Duse_system_wfconfig=disabled \
    -Duse_system_wlroots=disabled  \
    %{nil}

%meson_build
%install
%meson_install
install -D -p -m 0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
rm -f %{buildroot}%{_libdir}/libwftouch.a
# Duplicate man file
rm -f %{buildroot}%{_prefix}/man/%{name}.1
rm -f %{buildroot}%{_libdir}/libwlroots.a
rm -rf %{buildroot}%{_prefix}/lib

%files
%license LICENSE
%doc README.md %{name}.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{name}/
%{_libdir}/libwf-config.so*
%{_libdir}/libwf-utils.so*
%{_libdir}/libwlroots.so*
%{_libdir}/lib%{name}-blur-base.so
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_includedir}/wlr/
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
