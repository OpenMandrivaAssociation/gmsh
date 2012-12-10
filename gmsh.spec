Name:		gmsh
Summary:	Automatic 3D finite element grid generator
Version:	2.6.1
Release:	2
Group:		Sciences/Mathematics
License:	GPLv2
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
URL:		http://www.geuz.org/gmsh/

BuildRequires:	cmake
BuildRequires:	fltk-devel
BuildRequires:	gcc-gfortran
BuildRequires:	GL-devel
BuildRequires:	gmp-devel
BuildRequires:	jpeg-devel
BuildRequires:	libatlas-devel
BuildRequires:	opencascade
BuildRequires:	opencascade-devel
BuildRequires:	png-devel
BuildRequires:	qt4-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel

Patch0:		gmsh-2.4.2-format.patch
Patch1:		gmsh-2.5.0-opencascade.patch
Patch2:		gmsh-2.5.0-med.patch
Patch3:		gmsh-2.5.0-png1.5.patch

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD
engine and post-processor. Its design goal is to provide a simple meshing tool
for academic problems with parametric input and advanced visualization
capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

%package	demos
Summary:	Tutorial and demo files for Gmsh
Group:		Sciences/Mathematics
# known to have issues in mandriva build system
BuildArch: noarch

%description	demos
Gmsh is an automatic 3D finite element grid generator with a built-in CAD
engine and post-processor. Its design goal is to provide a simple meshing tool
for academic problems with parametric input and advanced visualization
capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains tutorial and demo files for Gmsh.

%package	devel
Summary:	Development files for Gmsh

%description	devel
Gmsh is an automatic 3D finite element grid generator with a built-in CAD
engine and post-processor. Its design goal is to provide a simple meshing tool
for academic problems with parametric input and advanced visualization
capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains development files for Gmsh.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
#patch1 -p1
#patch2 -p1
%patch3 -p1

%build
%cmake

%make

%install
%makeinstall_std -C build
install -D utils/icons/gmsh48x48.png %{buildroot}%{_iconsdir}/%name.png

%files
%defattr(644,root,root,755)
%doc README.txt doc/{CREDITS.txt,VERSIONS.txt}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_iconsdir}/%name.png
%exclude %_docdir/%name/demos
%exclude %_docdir/%name/tutorial

%files demos
%_docdir/%name/demos
%_docdir/%name/tutorial

%files devel
%{_includedir}/%name/*


%changelog
* Tue Jul 24 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.6.1-1
+ Revision: 810967
- update to 2.6.1
- separate devel package
- remove fr summaries and descriptions from spec
- various cleanups

* Fri Nov 18 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5.0-1
+ Revision: 731673
- Update to latest upstream release.

* Wed Jul 14 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.4.2-1mdv2011.0
+ Revision: 552963
- Import gmsh
- gmsh

