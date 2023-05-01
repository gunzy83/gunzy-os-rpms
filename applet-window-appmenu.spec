
Summary:        Plasma 5 applet to show the window appmenu

Name:           applet-window-appmenu
Version:        0.8.0
Release:        0
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/psifidotos/applet-window-appmenu
Source0:        https://github.com/psifidotos/applet-window-appmenu/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake >= 3.0
BuildRequires: extra-cmake-modules >= 0.0.11
BuildRequires: kdecoration-devel
BuildRequires: qt5-qtbase-devel >= 5.4.0
BuildRequires: qt5-qtdeclarative-devel >= 5.4.0
BuildRequires: qt5-qtx11extras-devel >= 5.4.0
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kwindowsystem-devel >= 5.0.0
BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-plasma-devel >= 5.0.0
BuildRequires: plasma-workspace-devel
BuildRequires: libSM-devel >= 1.2.3

%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels (as a global menu). This plasmoid supports both
latte-dock and standard Plasma panels.

%prep
%autosetup

%build
%cmake -Wno-dev
%cmake_build
%cmake_install

%files
%license LICENSE
%doc INSTALLATION.md README.md
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_windowappmenu.so
%{_libdir}/qt5/qml/org/kde/private/windowAppMenu/libappmenuplugin.so
%{_libdir}/qt5/qml/org/kde/private/windowAppMenu/qmldir
%{_datadir}/kservices5/plasma-applet-org.kde.windowappmenu.desktop
%{_datadir}/metainfo/org.kde.windowappmenu.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.windowappmenu

%changelog
* Mon May 25 2023 Ross Williams <gunzy83au@gmail.com> - 0.8.0-0
- Initial packaging
