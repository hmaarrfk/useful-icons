Name:           matlab-icons
Version:        0.1.0
Release:        1%{?dist}
Summary:        Icons and launcher for Matlab

License:        MIT
URL:            http://markharfouche.com/
Source0:        ftp://markharfouche.com/matlab-icons-0.1.0.tar.gz


BuildArch: noarch
#BuildRequires: desktop-file-utils

%description
I created launchers and icons for Matlab.


%prep
%setup -q

%build
#Nothing to do really since the files are all as is

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/
ls -lah
cp -R ./%{_datadir} %{buildroot}%{_datadir}


%clean
rm -rf %{buildroot}

%post
#things to run after the install is complete
if which update-desktop-database >>/dev/null
then
	update-desktop-database
fi

%postun
#things to run after uninstalling the stuff
if which update-desktop-database >>/dev/null
then
	update-desktop-database
fi

%files
%doc README LICENSE
%{_datadir}/icons/hicolor/64x64/apps/matlab.png
%{_datadir}/icons/hicolor/32x32/apps/matlab.png
%{_datadir}/icons/hicolor/16x16/apps/matlab.png
%{_datadir}/icons/hicolor/24x24/apps/matlab.png
%{_datadir}/icons/hicolor/48x48/apps/matlab.png
%{_datadir}/icons/hicolor/256x256/apps/matlab.png
%{_datadir}/icons/hicolor/128x128/apps/matlab.png
%{_datadir}/icons/hicolor/36x36/apps/matlab.png
%{_datadir}/applications/matlab.desktop




%changelog
* Wed Sep 26 2012 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0
- Initial version of package.
