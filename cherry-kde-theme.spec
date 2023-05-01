Summary: Clean, Flat, Δ Theme for Plasma Desktop

Name:           cherry-kde-theme
Version:        1.6
Release:        0
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/nullxception/cherry-kde-theme
Source0:        https://github.com/nullxception/cherry-kde-theme/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: coreutils
Suggests: kvantum
Suggests: konsole


%description
Cherry is a theme inspired by Δ (delta) battlesuit from Honkai Impact 3.

This theme consist of several components including :

aurorae themes (regular, solid, square, square-solid)
konsole and kitty colorscheme
kvantum theme (regular, solid)
plasma colorscheme
plasma desktop theme
splash screen

%prep
%autosetup

%build
THEME_NAME=cherry
SRC=.
PREFIX="%{buildroot}%{_datadir}"

# Destination directory
AURORAE="$PREFIX/aurorae/themes"
KONSOLE="$PREFIX/konsole"
KVANTUM="$PREFIX/Kvantum"
LOOKFEEL="$PREFIX/plasma/look-and-feel"
PLASMA="$PREFIX/plasma/desktoptheme"
SCHEMES="$PREFIX/color-schemes"
WALLPAPER="$PREFIX/wallpapers"

[[ ! -d ${AURORAE} ]] && mkdir -p ${AURORAE}
[[ ! -d ${KVANTUM} ]] && mkdir -p ${KVANTUM}
[[ ! -d ${KONSOLE} ]] && mkdir -p ${KONSOLE}
[[ ! -d ${LOOKFEEL} ]] && mkdir -p ${LOOKFEEL}
[[ ! -d ${PLASMA} ]] && mkdir -p ${PLASMA}
[[ ! -d ${SCHEMES} ]] && mkdir -p ${SCHEMES}
[[ ! -d ${WALLPAPER} ]] && mkdir -p ${WALLPAPER}

in_aurorae() {
    local name=${1}
    local variants=("solid"
    "square"
    "square-solid")

    cp -r ${SRC}/aurorae/${name} -t ${AURORAE}

    for variant in "${variants[@]}"; do
        cp -r ${SRC}/aurorae/${name} ${AURORAE}/${name}-${variant}
        cp -r ${SRC}/aurorae/${name}-${variant}/. ${AURORAE}/${name}-${variant}
    done
}

in_kvantum() {
    local name=${1}
    local variants=("solid")

    cp -r ${SRC}/kvantum/${name} -t ${KVANTUM}

    for variant in "${variants[@]}"; do
        cp -r ${SRC}/kvantum/${name}-${variant} -t ${KVANTUM}
    done
}

in_plasma() {
    local name=${1}
    local variants=("solid")

    cp -r ${SRC}/plasma/desktoptheme/${name} -t ${PLASMA}
    mkdir ${PLASMA}/${name}/colors
    cp ${SRC}/color-schemes/${name}.colors -t ${PLASMA}/${name}/colors

    for variant in "${variants[@]}"; do
        cp -r ${SRC}/plasma/desktoptheme/${name} ${PLASMA}/${name}-${variant}
        cp -r ${SRC}/plasma/desktoptheme/${name}-${variant}/. ${PLASMA}/${name}-${variant}

        if [[ -f ${SRC}/color-schemes/${name}-${variant}.colors ]]; then
            cp ${SRC}/color-schemes/${name}-${variant}.colors -t ${PLASMA}/${name}/colors
        fi
    done
}

in_global() {
    local name=${1}
    local domain=com.github.nullxception

    cp -r ${SRC}/plasma/look-and-feel/${domain}.${name} -t ${LOOKFEEL}
}

in_colors() {
    local name=${1}

    cp ${SRC}/color-schemes/${name}.colors -t ${SCHEMES}
    cp ${SRC}/konsole/${name}.colorscheme -t ${KONSOLE}
}

in_wallpaper() {
    local name=${1}

    cp -r ${SRC}/wallpaper/${name} -t ${WALLPAPER}
}

echo "Installing ${THEME_NAME}"
in_aurorae    "${THEME_NAME}"
in_colors     "${THEME_NAME}"
in_global     "${THEME_NAME}"
in_kvantum    "${THEME_NAME}"
in_plasma     "${THEME_NAME}"
in_wallpaper  "${THEME_NAME}"

%files
%license LICENSE
%doc README.md
%{_datadir}/aurorae/themes
%{_datadir}/konsole
%{_datadir}/Kvantum
%{_datadir}/plasma/look-and-feel
%{_datadir}/plasma/desktoptheme
%{_datadir}/color-schemes
%{_datadir}/wallpapers

%changelog
* Mon May 1 2023 Ross Williams <gunzy83au@gmail.com> - 1.6-0
- Initial packaging
