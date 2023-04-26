Summary:	Automatic 3D finite element grid generator
Name:		gmsh
Version:	4.11.1
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://www.geuz.org/gmsh/
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
#Patch0:		gmsh-2.4.2-format.patch
#Patch1:		gmsh-2.5.0-png1.5.patch
BuildRequires:	cmake ninja
BuildRequires:  cmake(MEDFile)
BuildRequires:	cmake(opencascade)
BuildRequires:	gcc-gfortran
BuildRequires:	texinfo
BuildRequires:	fltk-devel
BuildRequires:	gmp-devel
BuildRequires:	gomp-devel
BuildRequires:	hdf5-devel
BuildRequires:  metis-devel
BuildRequires:	pkgconfig(atlas)
BuildRequires:	pkgconfig(blas)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(lapack)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
# There's no more devel package
Obsoletes:	%{name}-devel < 2.8.4

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
%exclude %{_docdir}/%{name}/examples

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
%{_docdir}/%{name}/tutorials
%{_docdir}/%{name}/examples
%{_docdir}/%{name}/*.txt

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}-source

rm -fr contrib/blossom
rm -fr contrib/mpeg_encode

%build
%cmake \
	-Wno-dev \
	%{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
	-DENABLE_BUILD_LIB:BOOL=ON \
	-DENABLE_BUILD_DYNAMIC:BOOL=ON \
	-DENABLE_BUILD_SHARED:BOOL=ON \
	-DENABLE_MPEG_ENCODE:BOOL=OFF \
	-DENABLE_BLOSSOM:BOOL=OFF \
	-DENABLE_CGNS:BOOL=ON \
	-DENABLE_EIGEN:BOOL=ON \
	-DEIGEN_INC=%{_includedir}/eigen3 \
	-DENABLE_MED:BOOL=ON \
	-DENABLE_METIS:BOOL=ON \
	-DENABLE_OCC:BOOL=ON \
	-DENABLE_SYSTEM_CONTRIB:BOOL=ON \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# remove static libraries
#find %{buildroot} -type f -name libgmsh.a -exec rm -f {} \;

# icon
install -D utils/icons/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png

