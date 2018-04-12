Name:           xilinx-sdk-desktop
Version:        0.1

Release:        1%{?dist}
Summary:        Icons and launcher for Xilinx SDK

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/xilinx-sdk
Source0:        %{name}.tar.gz


BuildArch: noarch
BuildRequires: desktop-file-utils

%description
Launchers and icons for Xilinx SDK.


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
* Thu Apr 12 2018 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1
- Initial Build

