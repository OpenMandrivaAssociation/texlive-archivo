%global tl_name archivo
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.2
Release:	%{tl_revision}.1
Summary:	The Archivo font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/archivo
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Archivo family of fonts designed by Omnibus-
Type, with support for LaTeX and pdfLaTeX.

