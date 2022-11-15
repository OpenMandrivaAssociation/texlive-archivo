Name:		texlive-archivo
Version:	57283
Release:	1
Summary:	The Archivo font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/archivo
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/archivo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Archivo family of fonts designed by
Omnibus-Type, with support for LaTeX and pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/archivo
%{_texmfdistdir}/fonts/vf/public/archivo
%{_texmfdistdir}/fonts/type1/public/archivo
%{_texmfdistdir}/fonts/tfm/public/archivo
%{_texmfdistdir}/fonts/opentype/public/archivo
%{_texmfdistdir}/fonts/map/dvips/archivo
%{_texmfdistdir}/fonts/enc/dvips/archivo
%doc %{_texmfdistdir}/doc/fonts/archivo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
