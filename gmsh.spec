Summary:	Automatic 3D finite element grid generator
Name:		gmsh
Version:	2.8.4
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://www.geuz.org/gmsh/
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
BuildRequires:	cmake
BuildRequires:	gcc-gfortran
BuildRequires:	opencascade
BuildRequires:	texinfo
BuildRequires:	fltk-devel
BuildRequires:	gmp-devel
BuildRequires:	jpeg-devel
BuildRequires:	libatlas-devel
BuildRequires:	opencascade-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
Patch0:		gmsh-2.4.2-format.patch
Patch1:		gmsh-2.5.0-png1.5.patch

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD
engine and post-processor. Its design goal is to provide a simple meshing tool
for academic problems with parametric input and advanced visualization
capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

%files
%doc README.txt doc/{CREDITS.txt,VERSIONS.txt}
%{_bindir}/*
%{_mandir}/man1/*
%{_iconsdir}/%{name}.png
%exclude %{_docdir}/%{name}/demos
%exclude %{_docdir}/%{name}/tutorial

#----------------------------------------------------------------------------

%package	demos
Summary:	Tutorial and demo files for Gmsh
Group:		Sciences/Mathematics
# known to have issues in mandriva build system
BuildArch:	noarch

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

%files demos
%{_docdir}/%{name}/demos
%{_docdir}/%{name}/tutorial

#----------------------------------------------------------------------------

%package	devel
Summary:	Development files for Gmsh
Group:		Development/Other

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

%files devel
%{_includedir}/%{name}/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build
install -D utils/icons/gmsh48x48.png %{buildroot}%{_iconsdir}/%{name}.png

