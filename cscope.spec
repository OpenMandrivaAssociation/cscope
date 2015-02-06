%define name    cscope
%define version 15.8
%define release 2
%define Summary C source file browser

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License: BSD
Group: Development/Other
Source0: http://downloads.sourceforge.net/cscope/%name-%version.tar.bz2
Patch0: cscope_prog_info.patch
URL: http://cscope.sourceforge.net/
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

%files
%defattr(0755,root,root,0755)
%{_bindir}/cscope
%{_bindir}/ocs

%defattr(0644,root,root,0755)
%doc TODO COPYING ChangeLog AUTHORS README NEWS INSTALL
%{_mandir}/man1/cscope.1*
%{_datadir}/emacs/site-lisp/xcscope.el




%changelog
* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 15.8-1
+ Revision: 808339
- version update 15.8

* Fri Sep 09 2011 trem <trem@mandriva.org> 15.7a-2
+ Revision: 699156
- add xcscope.el from contrib

* Wed May 06 2009 Funda Wang <fwang@mandriva.org> 15.7a-1mdv2011.0
+ Revision: 372616
- New version 15.7a

* Thu Mar 19 2009 Funda Wang <fwang@mandriva.org> 15.7-1mdv2009.1
+ Revision: 357627
- BR flex
- BR bison
- New version 15.7

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 15.6-3mdv2009.0
+ Revision: 243798
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 15.6-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

