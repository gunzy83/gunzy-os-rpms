#
# spec file for package applet-window-appmenu
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           applet-window-appmenu
Version:        0.8.0
Release:        0
Summary:        Plasma 5 applet to show the window appmenu
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/psifidotos/applet-window-appmenu
Source0:        https://github.com/psifidotos/applet-window-appmenu/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  fedora-logos
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  libSM-devel
BuildRequires:  plasma-framework-devel
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)

%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels (as a global menu). This plasmoid supports both
latte-dock and standard Plasma panels.

%prep
%setup -q

%build
%cmake
%cmake_build
%install
%cmake_install
%fdupes %{buildroot}

%files
%license LICENSE
%dir /usr/lib64/qt5/qml/org/kde/private/windowAppMenu
%dir /usr/lib64/qt5/plugins/plasma/applets
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_windowappmenu.so
%dir /usr/share/plasma/plasmoids
%dir /usr/share/plasma/plasmoids/org.kde.windowappmenu
/usr/share/kservices5/plasma-applet-org.kde.windowappmenu.desktop
/usr/share/metainfo/org.kde.windowappmenu.appdata.xml
/usr/lib64/qt5/qml/org/kde/private/windowAppMenu/libappmenuplugin.so
/usr/lib64/qt5/qml/org/kde/private/windowAppMenu/qmldir
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/code/util.js
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/config/config.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/config/main.xml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/Broadcaster.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/CustomLabel.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/FlickableIndicators.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/LatteWindowsTracker.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/MenuFlickable.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/PaintedToolButton.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/PlasmaTasksModel.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/config/ColorsComboBox.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/config/ConfigGeneral.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.windowappmenu/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.windowappmenu/metadata.json
%changelog
