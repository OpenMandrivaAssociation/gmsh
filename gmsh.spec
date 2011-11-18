Name:		gmsh
Summary:	Automatic 3D finite element grid generator
Summary(fr.UTF-8): Un générateur de maillage 3D pour les éléments finis
Version:	2.5.0
Release:	1
Group:		Sciences/Mathematics
License:	GPL v2
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
URL:		http://www.geuz.org/gmsh/
# buildsystem issue
#Packager:	Yann COLLETTE <ycollet at freesurf dot fr>

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 

BuildRequires:	cmake
BuildRequires:	fltk-devel
BuildRequires:	gcc-gfortran
BuildRequires:	GL-devel
BuildRequires:	gmp-devel
BuildRequires:	jpeg-devel
BuildRequires:  libatlas-devel
BuildRequires:	opencascade
BuildRequires:	opencascade-devel
BuildRequires:	png-devel
BuildRequires:	qt4-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel

Requires:	libatlas

Patch0:		gmsh-2.4.2-format.patch
Patch1:		gmsh-2.5.0-opencascade.patch
Patch2:		gmsh-2.5.0-med.patch
Patch3:		gmsh-2.5.0-png1.5.patch

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

%description	-l fr.UTF-8
Gmsh est un générateur automatique de maillage pour éléments finis. Il intègre des greffons permettant d'appeler des codes éléments finis et permet de faire du post-processing.
Son objectif est de fournir un outil simple pour les problèmes académiques avec des géométries paramétrées ainsi que des capacités de visualisation évoluées.

Gmsh est construit autour de quatres modules: geometrie, maillage, solveur et post-processing.
La sélection d'un de ces modules peut se faire soit de façon interactive via l'interface utilisateur, soit via un fichier ASCII en utilisant le langage de script de Gmsh.

%package	demos
Summary:	Tutorial and demo files for Gmsh
Summary(fr.UTF-8): Tutoriels et fichiers de démonstration pour Gmsh
Group:		Sciences/Mathematics
# known to have issues in mandriva build system
#BuildArch: noarch

%description	demos
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains tutorial and demo files for Gmsh.

%description	-l fr.UTF-8
Gmsh est un générateur automatique de maillage pour éléments finis. Il intègre des greffons permettant d'appeler des codes éléments finis et permet de faire du post-processing.
Son objectif est de fournir un outil simple pour les problèmes académiques avec des géométries paramétrées ainsi que des capacités de visualisation évoluées.

Gmsh est construit autour de quatres modules: geometrie, maillage, solveur et post-processing.
La sélection d'un de ces modules peut se faire soit de façon interactive via l'interface utilisateur, soit via un fichier ASCII en utilisant le langage de script de Gmsh.

Ce paquet contient les tutoriels ainsi que les fichiers de démonstration pour Gmsh.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
	-DCMAKE_DL_LIB=-ldl \
        -DCMAKE_BUILD_TYPE=release

%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
install -D utils/icons/gmsh48x48.png %{buildroot}%{_iconsdir}/%name.png

%files
%defattr(-,root,root,755)
%doc README.txt doc/{CREDITS.txt,VERSIONS.txt}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_iconsdir}/%name.png
%{_includedir}/%name/*
%exclude %_docdir/%name/demos
%exclude %_docdir/%name/tutorial

%clean
rm -rf %{buildroot}

%files demos
%_docdir/%name/demos
%_docdir/%name/tutorial

%define date %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog
* %{date} Yann COLLETTE <ycollet at freesurf dot fr> 2.4.2
- Version 2.4.2
