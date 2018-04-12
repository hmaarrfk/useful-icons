Name:           vivado-desktop
Version:        0.3

Release:        4%{?dist}
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


%files
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*



%changelog
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

