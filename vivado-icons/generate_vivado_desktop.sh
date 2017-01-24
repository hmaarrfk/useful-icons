#!/bin/bash
directory_prefix="icons/hicolor"
icon_resolutions="64x64"
directory_suffix="apps"

for i in {2014..2017}; do
    for j in {1..4}; do
        vivado_version=${i}.${j}
        package_name=vivado-${vivado_version}-desktop
        rm -rf ${package_name}
        mkdir $package_name
        pushd  $package_name >> /dev/null

        cat >vivado-${vivado_version}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Vivado ${vivado_version}
Comment=Vivado
Icon=vivado-${vivado_version}
MimeType=application/vivado;
TryExec=/opt/Xilinx/Vivado/${vivado_version}/bin/vivado
Exec=/opt/Xilinx/Vivado/${vivado_version}/bin/vivado -nolog -nojournal
StartupWMClass=Vivado
#StartupWMClass=Vivado ${vivado_version}
EOF

        for r in $icon_resolutions; do
            the_directory="${directory_prefix}/$r/${directory_suffix}"
            mkdir -p "${the_directory}"
            #convert -pointsize 15 -fill white -draw 'text 15,60 '\"${vivado_version}\"' ' -resize ${r} ../vivado.png ${the_directory}/vivado-${vivado_version}.png
            convert -size 64x64 xc:none -pointsize 15 \
                -stroke black -strokewidth 2 -annotate +15+60 "${vivado_version}" -blur 0x2 \
                -fill   white -stroke none   -annotate +15+60 "${vivado_version}" \
                -resize ${r} ${the_directory}/vivado-${vivado_version}.png
            composite ${the_directory}/vivado-${vivado_version}.png -resize ${r} ../vivado.png ${the_directory}/vivado-${vivado_version}.png
        done
        popd >> /dev/null
        tar -cf ${package_name}.tar.gz ${package_name}
        echo "Name:           vivado-${vivado_version}-desktop" > vivado-${vivado_version}-desktop.spec
        tail -n +2 vivado-desktop.spec >> vivado-${vivado_version}-desktop.spec

        rpmdev-setuptree
        cp vivado-${vivado_version}-desktop.spec ~/rpmbuild/SPECS/.
        cp vivado-${vivado_version}-desktop.tar.gz ~/rpmbuild/SOURCES/.
        rpmbuild -bs vivado-${vivado_version}-desktop.spec
        rm -rf vivado-${vivado_version}-desktop vivado-${vivado_version}-desktop.spec vivado-${vivado_version}-desktop.tar.gz
    done
done
