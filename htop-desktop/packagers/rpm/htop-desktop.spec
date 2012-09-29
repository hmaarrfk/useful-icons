Name:           htop-desktop
Version:        0.1.0

# Since whenever you update this file on git, it should be a new version
# This realease number should stay at 1
Release:        1%{?dist}
Summary:        Desktop file entry for htop

License:        MIT
URL:            https://github.com/hmaarrfk/useful-icons/tree/master/htop-desktop
Source0:        htop-desktop-%{version}.tar.gz


BuildArch: 	noarch

# It does not really require this because what if the user just wants the files
# So I just leave it here for convenience
BuildRequires: desktop-file-utils

%description
I created a .desktop file for htop because I wanted to be able to run it from the Gnome Shell.


%prep
%setup -q

%build
#Nothing to do really since the files are all as is

%install
rm -rf %{buildroot}
# see  to learn how to properly install a .desktop see
# https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Desktop_files
desktop-file-install --delete-original --dir=${RPM_BUILD_ROOT}%{_datadir}/applications/ ./htop.desktop


%clean
rm -rf %{buildroot}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/htop.desktop

%files
%doc LICENSE
%{_datadir}/applications/htop.desktop




%changelog
* Thu Sep 27 2012 Mark Harfouche+mark.harfouche@gmail.com - 0.1.0
- Initial version of package.
