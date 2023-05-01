%global git_ref bbad71b
%global git_full_commit bbad71b48073879f16b484788d01831ad53316b5

Summary: Your usual clock widget, just way better and on a single line!

Name:           applet-betterinlineclock
Version:        3.1
Release:        %{?git_ref:0.git.%{git_ref}}%{?dist}
License:        GPL-3.0
Group:          System/GUI/KDE
URL:            https://github.com/MarianArlt/kde-plasmoid-betterinlineclock
Source0:        https://github.com/MarianArlt/kde-plasmoid-betterinlineclock/archive/%{git_ref}/%{name}-%{git_ref}.tar.gz

BuildArch: noarch

BuildRequires: coreutils
Requires: plasma-workspace
Requires: qt5-qtgraphicaleffects

%description
This is a Plasma 5 applet that replaces the standard clock
applet by showing on a single line instead of multiple.

%prep
%autosetup -n kde-plasmoid-betterinlineclock-%{git_full_commit}

%build
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.betterinlineclock
cp -dpRf org.kde.plasma.betterinlineclock/* %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.betterinlineclock

%files
%license LICENSE.md
%doc README.md CHANGELOG.md
%{_datadir}/plasma/plasmoids/org.kde.plasma.betterinlineclock

%changelog
* Mon May 1 2023 Ross Williams <gunzy83au@gmail.com> - 3.1-0.git.bbad71b
- Initial packaging
