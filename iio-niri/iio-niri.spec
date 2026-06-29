Name: iio-niri
Version: 2.2.0
Release: %autorelease
Summary: Listen to iio-sensor-proxy and updates Niri output orientation depending on the accelerometer orientation.
SourceLicense: MIT
License: MIT
URL: https://github.com/Zhaith-Izaliel/iio-niri
Source: %url/archive/v%version.tar.gz

BuildRequires: cargo-rpm-macros
Requires: niri
Requires: iio-sensor-proxy

%description
%summary

%prep
%autosetup -p1 -n %name-%version
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/release/iio-niri -t %{buildroot}%{_bindir}

%files
%license LICENSE.md
%license LICENSE.dependencies
%doc README.md
%{_bindir}/iio-niri

%changelog
%autochangelog
