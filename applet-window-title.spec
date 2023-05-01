Summary: Plasma 5 applet that shows the application title and icon for active window

Name:           applet-window-title
Version:        0.7.1
Release:        0
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/psifidotos/applet-window-title
Source0:        https://github.com/psifidotos/applet-window-title/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: coreutils
Requires: plasma-workspace >= 5.8
Requires: kf5-kdeclarative >= 5.8
Requires: kf5-kirigami2 >= 5.8

%description
This is a Plasma 5 applet that shows the current window appmenu
in your panels. This plasmoid is coming from Latte land but it
can also support Plasma panels.

%prep
%autosetup

%build
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.windowtitle
cp -dpRf contents metadata.desktop %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.windowtitle

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/plasma/plasmoids/org.kde.windowtitle

%changelog
* Mon May 1 2023 Ross Williams <gunzy83au@gmail.com> - 0.7.1-0
- Initial packaging
