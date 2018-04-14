Name:           vivado-desktop
Version:        0.5

License:        Public domain
Release:        1%{?dist}
Summary:        Icons and launcher for Vivado

URL:            https://github.com/hmaarrfk/useful-icons/tree/master/vivado-icons
Source0:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/vivado-icons/vivado.png
Source1:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/vivado-icons/generate_icons.sh


BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick

%description
Launchers and icons for Vivado.

%package -n vivado-2017.1-desktop
Summary: Vivado 2017.1
%description -n vivado-2017.1-desktop
Launchers and icons for Xilinx Vivado 2017.1

%package -n vivado-2017.2-desktop
Summary: Vivado 2017.2
%description -n vivado-2017.2-desktop
Launchers and icons for Xilinx Vivado 2017.2

%package -n vivado-2017.3-desktop
Summary: Vivado 2017.3
%description -n vivado-2017.3-desktop
Launchers and icons for Xilinx Vivado 2017.3

%package -n vivado-2017.4-desktop
Summary: Vivado 2017.4
%description -n vivado-2017.4-desktop
Launchers and icons for Xilinx Vivado 2017.4

%package -n vivado-2018.1-desktop
Summary: Vivado 2018.1
%description -n vivado-2018.1-desktop
Launchers and icons for Xilinx Vivado 2018.1

%package -n vivado-2018.2-desktop
Summary: Vivado 2018.2
%description -n vivado-2018.2-desktop
Launchers and icons for Xilinx Vivado 2018.2

%package -n vivado-2018.3-desktop
Summary: Vivado 2018.3
%description -n vivado-2018.3-desktop
Launchers and icons for Xilinx Vivado 2018.3

%package -n vivado-2018.4-desktop
Summary: Vivado 2018.4
%description -n vivado-2018.4-desktop
Launchers and icons for Xilinx Vivado 2018.4

%package -n vivado-2019.1-desktop
Summary: Vivado 2019.1
%description -n vivado-2019.1-desktop
Launchers and icons for Xilinx Vivado 2019.1

%package -n vivado-2019.2-desktop
Summary: Vivado 2019.2
%description -n vivado-2019.2-desktop
Launchers and icons for Xilinx Vivado 2019.2

%package -n vivado-2019.3-desktop
Summary: Vivado 2019.3
%description -n vivado-2019.3-desktop
Launchers and icons for Xilinx Vivado 2019.3

%package -n vivado-2019.4-desktop
Summary: Vivado 2019.4
%description -n vivado-2019.4-desktop
Launchers and icons for Xilinx Vivado 2019.4

%prep

%build
bash %{_sourcedir}/generate_icons.sh %{_sourcedir}/vivado.png 2017 2019

%install
for r in `ls icons/hicolor`; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
    install -m644 icons/hicolor/${r}/apps/*.png %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
done
desktop-file-install --delete-original  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications *.desktop

%clean
rm -rf %{buildroot}

%files -n vivado-2017.1-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2017.1.png
%{_datadir}/applications/vivado-2017.1.desktop

%files -n vivado-2017.2-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2017.2.png
%{_datadir}/applications/vivado-2017.2.desktop

%files -n vivado-2017.3-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2017.3.png
%{_datadir}/applications/vivado-2017.3.desktop

%files -n vivado-2017.4-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2017.4.png
%{_datadir}/applications/vivado-2017.4.desktop

%files -n vivado-2018.1-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2018.1.png
%{_datadir}/applications/vivado-2018.1.desktop

%files -n vivado-2018.2-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2018.2.png
%{_datadir}/applications/vivado-2018.2.desktop

%files -n vivado-2018.3-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2018.3.png
%{_datadir}/applications/vivado-2018.3.desktop

%files -n vivado-2018.4-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2018.4.png
%{_datadir}/applications/vivado-2018.4.desktop

%files -n vivado-2019.1-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2019.1.png
%{_datadir}/applications/vivado-2019.1.desktop

%files -n vivado-2019.2-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2019.2.png
%{_datadir}/applications/vivado-2019.2.desktop

%files -n vivado-2019.3-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2019.3.png
%{_datadir}/applications/vivado-2019.3.desktop

%files -n vivado-2019.4-desktop
%{_datadir}/icons/hicolor/*/apps/vivado-2019.4.png
%{_datadir}/applications/vivado-2019.4.desktop

%changelog
* Sat Apr 14 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.5-1
- Single spec, multiple rpms

* Thu Apr 12 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-4
- rebuilt

* Sat Jan 14 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-3
- Blurred background for font

* Sat Jan 14 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-2
- Support for multiple Vivado version

* Wed Jan 11 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.2
- Updated to 2016.4

* Sat May 7 2016 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.2
- Updated to 2015.4

* Fri Aug 14 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-5
- Remvoed log and journal. Too many get created otherwise

* Sun Jul 19 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-4
- Added StartupWMClass

* Sun Jul 19 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-3
- rebuilt

* Sun Jul 19 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-2
- Only works with Vivado 2015.2 in the default directory /opt

* Sun Jul 19 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0-1
- Didn't have an apps directory inside 64x64

* Sun Jul 19 2015 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0-1
- Initial Build

