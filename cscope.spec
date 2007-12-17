%define name    cscope
%define version 15.6
%define release %mkrel 1
%define Summary C source file browser

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License: BSD
Group: Development/Other
Source: %name-%version.tar.bz2
Patch0: cscope_prog_info.patch
URL: http://cscope.sourceforge.net/
BuildRequires: ncurses-devel

%description
cscope is an interactive, screen-oriented tool that allows the user to browse
through C source files for specified elements of code.

%prep

%setup
%patch0

%build

%configure

%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%defattr(0755,root,root,0755)
%{_bindir}/cscope
%{_bindir}/ocs

%defattr(0644,root,root,0755)
%doc TODO COPYING ChangeLog AUTHORS README NEWS INSTALL
%{_mandir}/man1/cscope.1*


