Name:           matlab-icons
Version:        0.1.1

Release:        5%{?dist}
Summary:        Icons and launcher for Matlab

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/matlab-icons
Source0:        matlab-icons-%{version}.tar.gz


BuildArch: noarch

# It does not really require this because what if the user just wants the files
# So I just leave it here for convenience
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
cp -R ./icons %{buildroot}%{_datadir}
# see  to learn how to properly install a .desktop see
# https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Desktop_files
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications ./matlab.desktop


%clean
rm -rf %{buildroot}

%post
#things to run after the install is complete

# Update Icon cache script obtained from
#http://fedoraproject.org/wiki/Archive:PackagingDrafts/ScriptletSnippets/iconcache
if [ -f "%{_bindir}/xdg-icon-resource" ]
then
	%{_bindir}/xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
fi
if which update-desktop-database >>/dev/null
then
	update-desktop-database
fi

%postun
#things to run after uninstalling the stuff
if [ -f "%{_bindir}/xdg-icon-resource" ]
then
	%{_bindir}/xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
fi
if which update-desktop-database >>/dev/null
then
	update-desktop-database
fi

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
* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.1-5
- The package now follows the new structure of the source
* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.1-4
- The package now updates the icon cache.

* Thu Sep 27 2012 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.1
- Changed the format of the source, to make it more obvious how to install from source
* Wed Sep 26 2012 Mark Harfouche <mark.harfouche@gmail.com> - 0.1.0
- Initial version of package.
