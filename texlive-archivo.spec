%global tl_name archivo
%global tl_revision 78931
%global tl_version 0.0.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The Archivo font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/archivo
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the Archivo family of fonts designed by Omnibus-
Type, with support for LaTeX and pdfLaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from archivo:
Map ArchivZero.map
TL_DROPIN_EOF
