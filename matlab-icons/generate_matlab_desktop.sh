#!/bin/bash
directory_prefix="icons/hicolor"
icon_resolutions="256x256 128x128 64x64 32x32"
directory_suffix="apps"
name=matlab

for i in {2016..2019}; do
    for j in a b; do
        version=R${i}${j}
        package_name=${name}-${version}-desktop
        rm -rf ${package_name}
        mkdir $package_name
        pushd  $package_name >> /dev/null

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
