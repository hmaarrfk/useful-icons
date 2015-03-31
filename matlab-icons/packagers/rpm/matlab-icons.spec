Name:           matlab-icons
Version:        0.1.1

Release:        10%{?dist}
Summary:        Icons and launcher for Matlab

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/matlab-icons
Source0:        matlab-icons-%{version}.tar.gz


BuildArch: noarch

# It does not really require this because what if the user just wants the files
# So I just leave it here for convenience
BuildRequires: desktop-file-utils

%description
I created launchers and icons for Matlab.


%prep
%setup -q

%build
#Nothing to do really since the files are all as is

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_bindir}/
#ls -lah
cp -R ./icons %{buildroot}%{_datadir}
# see  to learn how to properly install a .desktop see
# https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Desktop_files
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./matlab.desktop


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
%doc README LICENSE
%{_datadir}/icons/hicolor/64x64/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/36x36/apps/*
%{_datadir}/applications/*




%changelog
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
