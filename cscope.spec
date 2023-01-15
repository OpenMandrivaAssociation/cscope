Summary:        C source file browser
Name:           cscope
Version:        15.9
Release:	1
License: BSD
Group: Development/Other
Source0: http://downloads.sourceforge.net/cscope/%name-%version.tar.gz
Patch0: cscope_prog_info.patch
URL: http://cscope.sourceforge.net/
BuildRequires: ncurses-devel
BuildRequires: bison flex

%description
cscope is an interactive, screen-oriented tool that allows the user to browse
through C source files for specified elements of code.

%prep
%autosetup -p0
%configure

%build
%make_build

%install
%make_install
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
