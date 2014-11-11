Name:           comsol-icons
Version:        0.1.0

Release:        4%{?dist}
Summary:        Icons and launcher for Comsol

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/comsol-icons
Source0:        comsol-icons-%{version}.tar.gz


BuildArch: noarch

# It does not really require this because what if the user just wants the files
# So I just leave it here for convenience
#BuildRequires: desktop-file-utils

%description
I created launchers and icons for Comsol.


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
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./comsol.desktop
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./comsol_matlab.desktop


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
%{_datadir}/icons/hicolor/256x256/apps/*
%{_datadir}/applications/*




%changelog
* Tue Nov 11 2014 makerpm - 0.1.0-4
- rebuilt

* Tue Nov 11 2014 makerpm - 0.1.0-3
- rebuilt

* Tue Nov 11 2014 makerpm - 0.1.0-2
- Added the comsol matlab server

* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.0
- Initial commit.
