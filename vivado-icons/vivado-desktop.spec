Name:           vivado-desktop
Version:        0.3

Release:        2%{?dist}
Summary:        Icons and launcher for Vivado

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/vivado-icons
Source0:        %{name}.tar.gz


BuildArch: noarch
BuildRequires: desktop-file-utils

%description
Launchers and icons for Vivado.


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

