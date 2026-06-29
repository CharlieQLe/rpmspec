Name: iio-niri
Version: 2.2.0
Release: %autorelease
Summary: Listen to iio-sensor-proxy and updates Niri output orientation depending on the accelerometer orientation.
SourceLicense: MIT
License: MIT
URL: https://github.com/Zhaith-Izaliel/iio-niri
Source: %url/archive/v%version.tar.gz

BuildRequires: cargo-rpm-macros
BuildRequires: rust-anyhow-devel
BuildRequires: rust-clap-devel
BuildRequires: rust-clap-verbosity-flag-devel
BuildRequires: rust-clap-verbosity-flag+default-devel
BuildRequires: rust-clap_derive-devel
BuildRequires: rust-clap_complete-devel
BuildRequires: rust-clap_complete+default-devel
BuildRequires: rust-dbus-devel
BuildRequires: rust-dbus+default-devel
BuildRequires: rust-env_logger-devel
BuildRequires: rust-log-devel
BuildRequires: rust-serde-devel
BuildRequires: rust-serde_json-devel
BuildRequires: rust-signal-hook-devel
BuildRequires: rust-signal-hook+default-devel
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
