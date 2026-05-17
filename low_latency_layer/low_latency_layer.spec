Name: low_latency_layer
Version: 0.1.0
Release: %autorelease
Summary: Vulkan layer for hardware agnostic input latency reduction.
SourceLicense: MIT
License: MIT
URL: https://github.com/Korthos-Software/low_latency_layer
Source: %url/archive/refs/tags/v%version.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: vulkan-headers
BuildRequires: vulkan-utility-libraries-devel

Requires: vulkan-loader

%description
%summary

%prep
%autosetup

%build
cmake -B build -DCMAKE_INSTALL_PREFIX=%{_prefix} ./

%install
cd ./build
%make_install

%files
%doc README.md
%{_libdir}/libVkLayer_KORTHOS_LowLatency.so
%{_datadir}/vulkan/implicit_layer.d/low_latency_layer.json

%changelog
%autochangelog
