#!/bin/bash
original_icon=$1
directory_prefix="icons/hicolor"
icon_resolutions="256x256 128x128 64x64 32x32"
directory_suffix="apps"
name=matlab

for i in $(seq ${2} ${3}); do
    for j in a b; do
        version=R${i}${j}

        cat >${name}-${version}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Matlab ${matlab_version}
Comment=The Language of Technical Computing
Icon=${name}-${version}
MimeType=application/${name};
TryExec=/usr/local/MATLAB/${version}/bin/matlab
Exec=/usr/local/MATLAB/${version}/bin/matlab -desktop
StartupWMClass=MATLAB ${version}
EOF

        for r in $icon_resolutions; do
            the_directory="${directory_prefix}/$r/${directory_suffix}"
            mkdir -p "${the_directory}"
            convert -size 256x256 xc:none -pointsize 60 \
                -stroke black -strokewidth 4 -annotate +40+240 "${version}" -blur 0x4 \
                -fill   white -stroke none   -annotate +40+240 "${version}" \
                -resize ${r} ${the_directory}/${name}-${version}.png
            composite ${the_directory}/${name}-${version}.png -resize ${r} ${original_icon} ${the_directory}/${name}-${version}.png
        done
    done
done
