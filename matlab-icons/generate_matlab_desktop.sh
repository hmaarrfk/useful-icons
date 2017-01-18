#!/bin/bash
directory_prefix="icons/hicolor"
icon_resolutions="256x256 128x128 64x64 32x32"
directory_suffix="apps"

for i in {2014..2017}; do
    for j in a b; do
        matlab_version=R${i}${j}
        package_name=matlab-${matlab_version}-desktop
        rm -rf ${package_name}
        mkdir $package_name
        pushd  $package_name >> /dev/null

        cat >matlab-${matlab_version}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Matlab ${matlab_version}
Comment=The Language of Technical Computing
Icon=matlab-${matlab_version}
MimeType=application/matlab;
TryExec=/usr/local/MATLAB/${matlab_version}/bin/matlab
Exec=/usr/local/MATLAB/${matlab_version}/bin/matlab -desktop
StartupWMClass=MATLAB ${matlab_version}
EOF

        for r in $icon_resolutions; do
            the_directory="${directory_prefix}/$r/${directory_suffix}"
            mkdir -p "${the_directory}"
            convert -pointsize 30 -fill white -draw 'text 140,220 '"${matlab_version}"' ' -resize ${r} ../matlab.png ${the_directory}/matlab-${matlab_version}.png
        done
        popd >> /dev/null
        tar -cf ${package_name}.tar.gz ${package_name}
        echo "Name:           matlab-${matlab_version}-desktop" > matlab-${matlab_version}-desktop.spec
        #cat matlab-desktop.spec >> matlab-${matlab_version}-desktop.spec
        tail -n +1 matlab-desktop.spec >> matlab-${matlab_version}-desktop.spec

        rpmdev-setuptree
        cp matlab-${matlab_version}-desktop.spec ~/rpmbuild/SPECS/.
        cp matlab-${matlab_version}-desktop.tar.gz ~/rpmbuild/SOURCES/.
        rpmbuild -bs matlab-${matlab_version}-desktop.spec
        rm -rf matlab-${matlab_version}-desktop matlab-${matlab_version}-desktop.spec matlab-${matlab_version}-desktop.tar.gz
    done
done
