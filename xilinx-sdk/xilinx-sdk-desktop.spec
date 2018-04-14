Name:           xilinx-sdk-desktop
Version:        0.5

Release:        1%{?dist}
Summary:        Icons and launcher for Xilinx SDK

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/xilinx-sdk
Source0:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/xilinx-sdk/xilinx-sdk.png
Source1:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/xilinx-sdk/generate_icons.sh


BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick

%description
Launchers and icons for Xilinx SDK.

%package -n xilinx-sdk-2017.1-desktop
Summary: Xilinx SDK 2017.1
%description -n xilinx-sdk-2017.1-desktop
Launchers and icons for Xilinx SDK 2017.1

%package -n xilinx-sdk-2017.2-desktop
Summary: Xilinx SDK 2017.2
%description -n xilinx-sdk-2017.2-desktop
Launchers and icons for Xilinx SDK 2017.2

%package -n xilinx-sdk-2017.3-desktop
Summary: Xilinx SDK 2017.3
%description -n xilinx-sdk-2017.3-desktop
Launchers and icons for Xilinx SDK 2017.3

%package -n xilinx-sdk-2017.4-desktop
Summary: Xilinx SDK 2017.4
%description -n xilinx-sdk-2017.4-desktop
Launchers and icons for Xilinx SDK 2017.4

%package -n xilinx-sdk-2018.1-desktop
Summary: Xilinx SDK 2018.1
%description -n xilinx-sdk-2018.1-desktop
Launchers and icons for Xilinx SDK 2018.1

%package -n xilinx-sdk-2018.2-desktop
Summary: Xilinx SDK 2018.2
%description -n xilinx-sdk-2018.2-desktop
Launchers and icons for Xilinx SDK 2018.2

%package -n xilinx-sdk-2018.3-desktop
Summary: Xilinx SDK 2018.3
%description -n xilinx-sdk-2018.3-desktop
Launchers and icons for Xilinx SDK 2018.3

%package -n xilinx-sdk-2018.4-desktop
Summary: Xilinx SDK 2018.4
%description -n xilinx-sdk-2018.4-desktop
Launchers and icons for Xilinx SDK 2018.4

%package -n xilinx-sdk-2019.1-desktop
Summary: Xilinx SDK 2019.1
%description -n xilinx-sdk-2019.1-desktop
Launchers and icons for Xilinx SDK 2019.1

%package -n xilinx-sdk-2019.2-desktop
Summary: Xilinx SDK 2019.2
%description -n xilinx-sdk-2019.2-desktop
Launchers and icons for Xilinx SDK 2019.2

%package -n xilinx-sdk-2019.3-desktop
Summary: Xilinx SDK 2019.3
%description -n xilinx-sdk-2019.3-desktop
Launchers and icons for Xilinx SDK 2019.3

%package -n xilinx-sdk-2019.4-desktop
Summary: Xilinx SDK 2019.4
%description -n xilinx-sdk-2019.4-desktop
Launchers and icons for Xilinx SDK 2019.4

%prep

%build
bash %{_sourcedir}/generate_icons.sh %{_sourcedir}/*.png 2017 2019

%install
for r in `ls icons/hicolor`; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
    install -m644 icons/hicolor/${r}/apps/*.png %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
done
desktop-file-install --delete-original  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications *.desktop


%clean
rm -rf %{buildroot}


%files -n xilinx-sdk-2017.1-desktop
%{_datadir}/icons/hicolor/*/apps/*-2017.1.png
%{_datadir}/applications/*-2017.1.desktop

%files -n xilinx-sdk-2017.2-desktop
%{_datadir}/icons/hicolor/*/apps/*-2017.2.png
%{_datadir}/applications/*-2017.2.desktop

%files -n xilinx-sdk-2017.3-desktop
%{_datadir}/icons/hicolor/*/apps/*-2017.3.png
%{_datadir}/applications/*-2017.3.desktop

%files -n xilinx-sdk-2017.4-desktop
%{_datadir}/icons/hicolor/*/apps/*-2017.4.png
%{_datadir}/applications/*-2017.4.desktop

%files -n xilinx-sdk-2018.1-desktop
%{_datadir}/icons/hicolor/*/apps/*-2018.1.png
%{_datadir}/applications/*-2018.1.desktop

%files -n xilinx-sdk-2018.2-desktop
%{_datadir}/icons/hicolor/*/apps/*-2018.2.png
%{_datadir}/applications/*-2018.2.desktop

%files -n xilinx-sdk-2018.3-desktop
%{_datadir}/icons/hicolor/*/apps/*-2018.3.png
%{_datadir}/applications/*-2018.3.desktop

%files -n xilinx-sdk-2018.4-desktop
%{_datadir}/icons/hicolor/*/apps/*-2018.4.png
%{_datadir}/applications/*-2018.4.desktop

%files -n xilinx-sdk-2019.1-desktop
%{_datadir}/icons/hicolor/*/apps/*-2019.1.png
%{_datadir}/applications/*-2019.1.desktop

%files -n xilinx-sdk-2019.2-desktop
%{_datadir}/icons/hicolor/*/apps/*-2019.2.png
%{_datadir}/applications/*-2019.2.desktop

%files -n xilinx-sdk-2019.3-desktop
%{_datadir}/icons/hicolor/*/apps/*-2019.3.png
%{_datadir}/applications/*-2019.3.desktop

%files -n xilinx-sdk-2019.4-desktop
%{_datadir}/icons/hicolor/*/apps/*-2019.4.png
%{_datadir}/applications/*-2019.4.desktop



%changelog
* Sat Apr 14 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.5-1
- Single spec, multiple rpms

* Thu Apr 12 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.1-3
- proper command line arguments

* Thu Apr 12 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.1-2
- Cooler icon

* Thu Apr 12 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1
- Initial Build

