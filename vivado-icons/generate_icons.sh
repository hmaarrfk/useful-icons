#!/bin/bash
original_icon=$1
directory_prefix="icons/hicolor"
icon_resolutions="64x64"
directory_suffix="apps"
name=vivado

for i in $(seq ${2} ${3}); do
    for j in {1..4}; do
        version=${i}.${j}

        cat >${name}-${version}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Vivado ${version}
Comment=Xilinx Vivado
Icon=${name}-${version}
MimeType=application/${name};
TryExec=/opt/Xilinx/Vivado/${version}/bin/${name}
Exec=/opt/Xilinx/Vivado/${version}/bin/${name} -nolog -nojournal
StartupWMClass=Vivado
EOF
        for r in $icon_resolutions; do
            the_directory="${directory_prefix}/$r/${directory_suffix}"
            mkdir -p "${the_directory}"
            convert -size 64x64 xc:none -pointsize 15 \
                -stroke black -strokewidth 2 -annotate +15+60 "${version}" -blur 0x2 \
                -fill   white -stroke none   -annotate +15+60 "${version}" \
                -resize ${r} ${the_directory}/${name}-${version}.png
            composite ${the_directory}/${name}-${version}.png -resize ${r} ${original_icon} ${the_directory}/${name}-${version}.png
        done
    done
done
