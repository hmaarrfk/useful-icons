Name:           matlab-desktop
Version:        0.5

License:        PublicDomain
Release:        3%{?dist}
Summary:        Icons and launcher for Matlab

URL:            https://github.com/hmaarrfk/useful-icons/tree/master/matlab-icons
Source0:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/matlab-icons/matlab.png
Source1:        https://raw.githubusercontent.com/hmaarrfk/useful-icons/master/matlab-icons/generate_icons.sh

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick


%description
Launchers and icons for Matlab.

%define build_targets 2011a 2011b 2012a 2012b

%package -n matlab-R2011a-desktop
Summary: Matlab R2011a
%description -n matlab-R2011a-desktop
Launchers and icons for Matlab R2011a

%package -n matlab-R2011b-desktop
Summary: Matlab R2011b
%description -n matlab-R2011b-desktop
Launchers and icons for Matlab R2011b

%package -n matlab-R2012a-desktop
Summary: Matlab R2012a
%description -n matlab-R2012a-desktop
Launchers and icons for Matlab R2012a

%package -n matlab-R2012b-desktop
Summary: Matlab R2012b
%description -n matlab-R2012b-desktop
Launchers and icons for Matlab R2012b

%package -n matlab-R2013a-desktop
Summary: Matlab R2013a
%description -n matlab-R2013a-desktop
Launchers and icons for Matlab R2013a

%package -n matlab-R2013b-desktop
Summary: Matlab R2013b
%description -n matlab-R2013b-desktop
Launchers and icons for Matlab R2013b

%package -n matlab-R2014a-desktop
Summary: Matlab R2014a
%description -n matlab-R2014a-desktop
Launchers and icons for Matlab R2014a

%package -n matlab-R2014b-desktop
Summary: Matlab R2014b
%description -n matlab-R2014b-desktop
Launchers and icons for Matlab R2014b

%package -n matlab-R2015a-desktop
Summary: Matlab R2015a
%description -n matlab-R2015a-desktop
Launchers and icons for Matlab R2015a

%package -n matlab-R2015b-desktop
Summary: Matlab R2015b
%description -n matlab-R2015b-desktop
Launchers and icons for Matlab R2015b

%package -n matlab-R2016a-desktop
Summary: Matlab R2016a
%description -n matlab-R2016a-desktop
Launchers and icons for Matlab R2016a

%package -n matlab-R2016b-desktop
Summary: Matlab R2016b
%description -n matlab-R2016b-desktop
Launchers and icons for Matlab R2016b

%package -n matlab-R2017a-desktop
Summary: Matlab R2017a
%description -n matlab-R2017a-desktop
Launchers and icons for Matlab R2017a

%package -n matlab-R2017b-desktop
Summary: Matlab R2017b
%description -n matlab-R2017b-desktop
Launchers and icons for Matlab R2017b

%package -n matlab-R2018a-desktop
Summary: Matlab R2018a
%description -n matlab-R2018a-desktop
Launchers and icons for Matlab R2018a

%package -n matlab-R2018b-desktop
Summary: Matlab R2018b
%description -n matlab-R2018b-desktop
Launchers and icons for Matlab R2018b

%package -n matlab-R2019a-desktop
Summary: Matlab R2019a
%description -n matlab-R2019a-desktop
Launchers and icons for Matlab R2019a

%package -n matlab-R2019b-desktop
Summary: Matlab R2019b
%description -n matlab-R2019b-desktop
Launchers and icons for Matlab R2019b

%package -n matlab-R2020a-desktop
Summary: Matlab R2020a
%description -n matlab-R2020a-desktop
Launchers and icons for Matlab R2020a

%package -n matlab-R2020b-desktop
Summary: Matlab R2020b
%description -n matlab-R2020b-desktop
Launchers and icons for Matlab R2020b

%package -n matlab-R2021a-desktop
Summary: Matlab R2021a
%description -n matlab-R2021a-desktop
Launchers and icons for Matlab R2021a

%package -n matlab-R2021b-desktop
Summary: Matlab R2021b
%description -n matlab-R2021b-desktop
Launchers and icons for Matlab R2021b

%package -n matlab-R2022a-desktop
Summary: Matlab R2022a
%description -n matlab-R2022a-desktop
Launchers and icons for Matlab R2022a

%package -n matlab-R2022b-desktop
Summary: Matlab R2022b
%description -n matlab-R2022b-desktop
Launchers and icons for Matlab R2022b

%prep

%build
bash %{_sourcedir}/generate_icons.sh %{_sourcedir}/matlab.png 2011 2022

%install
for r in `ls icons/hicolor`; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
    install -m644 icons/hicolor/${r}/apps/*.png %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
done
desktop-file-install --delete-original  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications *.desktop


%clean
rm -rf %{buildroot}

%files -n matlab-R2011a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2011a.png
%{_datadir}/applications/matlab-R2011a.desktop

%files -n matlab-R2011b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2011b.png
%{_datadir}/applications/matlab-R2011b.desktop

%files -n matlab-R2012a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2012a.png
%{_datadir}/applications/matlab-R2012a.desktop

%files -n matlab-R2012b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2012b.png
%{_datadir}/applications/matlab-R2012b.desktop

%files -n matlab-R2013a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2013a.png
%{_datadir}/applications/matlab-R2013a.desktop

%files -n matlab-R2013b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2013b.png
%{_datadir}/applications/matlab-R2013b.desktop

%files -n matlab-R2014a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2014a.png
%{_datadir}/applications/matlab-R2014a.desktop

%files -n matlab-R2014b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2014b.png
%{_datadir}/applications/matlab-R2014b.desktop

%files -n matlab-R2015a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2015a.png
%{_datadir}/applications/matlab-R2015a.desktop

%files -n matlab-R2015b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2015b.png
%{_datadir}/applications/matlab-R2015b.desktop

%files -n matlab-R2016a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2016a.png
%{_datadir}/applications/matlab-R2016a.desktop

%files -n matlab-R2016b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2016b.png
%{_datadir}/applications/matlab-R2016b.desktop

%files -n matlab-R2017a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2017a.png
%{_datadir}/applications/matlab-R2017a.desktop

%files -n matlab-R2017b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2017b.png
%{_datadir}/applications/matlab-R2017b.desktop

%files -n matlab-R2018a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2018a.png
%{_datadir}/applications/matlab-R2018a.desktop

%files -n matlab-R2018b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2018b.png
%{_datadir}/applications/matlab-R2018b.desktop

%files -n matlab-R2019a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2019a.png
%{_datadir}/applications/matlab-R2019a.desktop

%files -n matlab-R2019b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2019b.png
%{_datadir}/applications/matlab-R2019b.desktop

%files -n matlab-R2020a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2020a.png
%{_datadir}/applications/matlab-R2020a.desktop

%files -n matlab-R2020b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2020b.png
%{_datadir}/applications/matlab-R2020b.desktop

%files -n matlab-R2021a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2021a.png
%{_datadir}/applications/matlab-R2021a.desktop

%files -n matlab-R2021b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2021b.png
%{_datadir}/applications/matlab-R2021b.desktop

%files -n matlab-R2022a-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2022a.png
%{_datadir}/applications/matlab-R2022a.desktop

%files -n matlab-R2022b-desktop
%{_datadir}/icons/hicolor/*/apps/matlab-R2022b.png
%{_datadir}/applications/matlab-R2022b.desktop

%changelog
* Sat Apr 14 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.5-3
- Fixed execusion of the build script

* Sat Apr 14 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.5-2
- Single spec file, multiple rpms
k
* Sat Apr 14 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.5-1
- Much simplified script

* Wed Jan 18 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-5
- Blurred black background

* Wed Jan 18 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-4
- Bigger font on icons for R20XXx

* Wed Jan 18 2017 Mark Harfouche <mark.harfouche@gmail.com>
- rebuilt

* Sat Jan 14 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.3-2
- Support for multiple Matlab version

* Tue Jan 03 2017 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1-11
- R2016b

* Tue Mar 31 2015 Mark Harfouche - 0.1.1-10
- Added a build require for the desktop file

* Sun Dec 15 2013 Mark Harfouche - 0.1.1-9
- Changed the WMClass type so that it catches the windows from R2103a and
  classifies them under the same icon.

* Thu May 30 2013 Mark Harfouche - 0.1.1-8
- If you do a custom install of matlab it will create symlinks for you, so I
  undid the last change

* Thu May 30 2013 Mark Harfouche - 0.1.1-7
- Updated for R2013a. Had to create a link to the executable since it wasn't
  created by default

* Wed Jan 30 2013 RPM Maker - 0.1.1-6
- Fixed the icon cache update

* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.1-5
- The package now follows the new structure of the source
* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.1-4
- The package now updates the icon cache.

* Thu Sep 27 2012 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1
- Changed the format of the source, to make it more obvious how to install from source
* Wed Sep 26 2012 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0
- Initial version of package.
