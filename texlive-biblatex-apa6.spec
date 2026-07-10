%global tl_name biblatex-apa6
%global tl_revision 56209

Name:		texlive-%{tl_name}
Epoch:		1
Version:	8.5
Release:	%{tl_revision}.1
Summary:	BibLaTeX citation and reference style for APA 6th Edition
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-apa6
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa6.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa6.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a fairly complete BibLaTeX style (citations and references) for
APA (American Psychological Association) 6th Edition conformant
publications. It implements and automates most of the guidelines in the
APA 6th edition style guide for citations and references. An example
document is also given which typesets every citation and reference
example in the APA 6th edition style guide. This is a legacy style for
6th Edition documents. Please use the BibLaTeX-apa style package for the
latest APA edition conformance.

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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-apa6
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-apa6
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6-test-citations.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6-test-references.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6-test.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6-test.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-apa6/biblatex-apa6.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/american-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/apa6.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/apa6.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/apa6.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/austrian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/brazilian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/british-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/danish-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/dutch-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/english-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/french-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/galician-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/german-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/greek-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/italian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/naustrian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/ngerman-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/norsk-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/norwegian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/nswissgerman-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/nynorsk-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/portuguese-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/russian-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/slovene-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/spanish-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/swedish-apa6.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-apa6/swissgerman-apa6.lbx
