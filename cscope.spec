%define name    cscope
%define version 15.7a
%define release %mkrel 2
%define Summary C source file browser

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License: BSD
Group: Development/Other
Source: http://downloads.sourceforge.net/cscope/%name-%version.tar.bz2
Patch0: cscope_prog_info.patch
URL: http://cscope.sourceforge.net/
Buildroot: %{_tmppath}/%{name}--buildroot
BuildRequires: ncurses-devel
BuildRequires: bison flex

%description
cscope is an interactive, screen-oriented tool that allows the user to browse
through C source files for specified elements of code.

%prep
%setup -q
%patch0

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
install contrib/xcscope/xcscope.el %{buildroot}%{_datadir}/emacs/site-lisp/

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
%{_datadir}/emacs/site-lisp/xcscope.el


