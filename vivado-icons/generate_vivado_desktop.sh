#!/bin/bash
directory_prefix="icons/hicolor"
icon_resolutions="64x64"
directory_suffix="apps"
name=vivado

for i in {2014..2019}; do
    for j in {1..4}; do
        version=${i}.${j}
        package_name=${name}-${version}-desktop
        rm -rf ${package_name}
        mkdir ${package_name}
        pushd  ${package_name} >> /dev/null

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
            composite ${the_directory}/${name}-${version}.png -resize ${r} ../${name}.png ${the_directory}/${name}-${version}.png
        done
        popd >> /dev/null
        tar -cf ${package_name}.tar.gz ${package_name}
        echo "Name:           ${name}-${version}-desktop" > ${name}-${version}-desktop.spec
        tail -n +2 ${name}-desktop.spec >> ${name}-${version}-desktop.spec

        rpmdev-setuptree
        cp ${name}-${version}-desktop.spec ~/rpmbuild/SPECS/.
        cp ${name}-${version}-desktop.tar.gz ~/rpmbuild/SOURCES/.
        rpmbuild -bs ${name}-${version}-desktop.spec
        rm -rf ${name}-${version}-desktop ${name}-${version}-desktop.spec ${name}-${version}-desktop.tar.gz
    done
done
