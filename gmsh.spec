Summary:	Automatic 3D finite element grid generator
Name:		gmsh
Version:	4.11.1
Release:	1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://www.geuz.org/gmsh/
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
Patch0:		gmsh-4.11.1-fix_install_path.patch
Patch1:		gmsh-4.11.1-add_missing_heades.patch

BuildRequires:	cmake ninja
BuildRequires:  cmake(MEDFile)
BuildRequires:	cmake(opencascade)
BuildRequires:	imagemagick
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
%doc README.txt CREDITS.txt CHANGELOG.txt doc/WELCOME.txt
%{_bindir}/*
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/*
%{py_platsitedir}/onelab.py
#{py_platsitedir}/__pycache__/onelab.*
%exclude %{_docdir}/%{name}/*txt
%exclude %{_docdir}/%{name}/examples
%exclude %{_docdir}/%{name}/images
%exclude %{_docdir}/%{name}/tutorials

#----------------------------------------------------------------------------

%package       devel
Summary:       Development files for Gmsh
Group:         Development/Other

%description   devel
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
%{_includedir}/%{name}*
%{_libdir}/libgmsh.so

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python API for %{name}
%{?python_provide:%python_provide python-%name}

%description -n python-%{name}
Python3 API for %{name}.

%files -n python-%{name}
%{py_platsitedir}/%{name}.py
%{py_platsitedir}/%{name}*.*-info/

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
%{_docdir}/%{name}/images/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}-source

rm -fr contrib/blossom
rm -fr contrib/mpeg_encode

%build
%cmake \
	-Wno-dev \
	%{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
	-DENABLE_BUILD_LIB:BOOL=OFF \
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

# .deskop
install -dm 0755 %{buildroot}/%{_datadir}/applications
cat << EOF > %{buildroot}/%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Name=Gmsh
GenericName=Mesh Generator
Comment=A 3D finite element mesh generator
Exec=gmsh
Icon=gmsh
Type=Application
Terminal=false
Categories=Science;Engineering;
EOF

# icon
for d in 16 32 48 64 72 128 256 512
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -scale ${d}x${d} utils/icons/%{name}.png \
		%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -scale 32x32 utils/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

