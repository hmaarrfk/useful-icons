Name:           matlab-desktop
Version:        0.3

Release:        5%{?dist}
Summary:        Icons and launcher for Matlab

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/matlab-icons
Source0:        %{name}.tar.gz


BuildArch: noarch
BuildRequires: desktop-file-utils

%description
Launchers and icons for Matlab.


%prep
%autosetup -c name

%build

%install
for r in `ls %{name}/icons/hicolor`; do
    install -d %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
    install -m644 %{name}/icons/hicolor/${r}/apps/*.png %{buildroot}%{_datadir}/icons/hicolor/${r}/apps
done
desktop_file_name=%{name}
desktop_file_name=${desktop_file_name::-8}.desktop
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}/${desktop_file_name}


%clean
rm -rf %{buildroot}

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*



%changelog
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
