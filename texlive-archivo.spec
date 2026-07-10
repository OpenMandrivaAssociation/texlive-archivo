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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Archivo family of fonts designed by Omnibus-
Type, with support for LaTeX and pdfLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/archivo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/archivo
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/archivo
%dir %{_datadir}/texmf-dist/fonts/map/dvips/archivo
%dir %{_datadir}/texmf-dist/fonts/opentype/public/archivo
%dir %{_datadir}/texmf-dist/fonts/tfm/public/archivo
%dir %{_datadir}/texmf-dist/fonts/type1/public/archivo
%dir %{_datadir}/texmf-dist/fonts/vf/public/archivo
%doc %{_datadir}/texmf-dist/doc/fonts/archivo/Archivo-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/archivo/Archivo-samples.tex
%doc %{_datadir}/texmf-dist/doc/fonts/archivo/LICENSE.TXT
%doc %{_datadir}/texmf-dist/doc/fonts/archivo/README
%doc %{_datadir}/texmf-dist/doc/fonts/archivo/README.doc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_24xxsv.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_5xld5w.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_7npxgm.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_fiyauo.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_flfbvu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_lwgukc.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_lzhlbi.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_mq36jn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_owzwzj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_ttjzpe.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_utd4ik.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_vgwtwr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/archivo/a_vqpkf5.enc
%{_datadir}/texmf-dist/fonts/map/dvips/archivo/ArchivZero.map
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-Medium.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-MediumItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-SemiBold.otf
%{_datadir}/texmf-dist/fonts/opentype/public/archivo/Archiv0-SemiBoldItalic.otf
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Bold-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-BoldItalic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Italic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Medium-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-MediumItalic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-Regular-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBold-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/archivo/Archiv0-SemiBoldItalic-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-Medium.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-MediumItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-Regular.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-SemiBold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/archivo/Archiv0-SemiBoldItalic.pfb
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Bold-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-BoldItalic-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Italic-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Medium-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-MediumItalic-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-Regular-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBold-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/archivo/Archiv0-SemiBoldItalic-tosf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/archivo/Archivo.sty
%{_datadir}/texmf-dist/tex/latex/archivo/LY1ArchivZero-LF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/LY1ArchivZero-OsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/LY1ArchivZero-Sup.fd
%{_datadir}/texmf-dist/tex/latex/archivo/LY1ArchivZero-TLF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/LY1ArchivZero-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/OT1ArchivZero-LF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/OT1ArchivZero-OsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/OT1ArchivZero-Sup.fd
%{_datadir}/texmf-dist/tex/latex/archivo/OT1ArchivZero-TLF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/OT1ArchivZero-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/T1ArchivZero-LF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/T1ArchivZero-OsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/T1ArchivZero-Sup.fd
%{_datadir}/texmf-dist/tex/latex/archivo/T1ArchivZero-TLF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/T1ArchivZero-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/TS1ArchivZero-LF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/TS1ArchivZero-OsF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/TS1ArchivZero-TLF.fd
%{_datadir}/texmf-dist/tex/latex/archivo/TS1ArchivZero-TOsF.fd
