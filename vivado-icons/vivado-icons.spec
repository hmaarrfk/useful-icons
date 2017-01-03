Name:           vivado-icons
Version:        0.1.2

Release:        1%{?dist}
Summary:        Icons and launcher for Vivado

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/vivado-icons
Source0:        vivado-icons-%{version}.tar.gz


BuildArch:      noarch

# It does not really require this because what if the user just wants the files
# So I just leave it here for convenience
BuildRequires: desktop-file-utils

%description
I created launchers and icons for Vivado.


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
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./*.desktop


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
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*




%changelog
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

