Name:		texlive-biblatex-apa6
Version:	56209
Release:	1
Summary:	BibLaTeX citation and reference style for APA 6th Edition
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-apa6
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa6.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-apa6.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a fairly complete BibLaTeX style (citations and
references) for APA (American Psychological Association) 6th
Edition conformant publications. It implements and automates
most of the guidelines in the APA 6th edition style guide for
citations and references. An example document is also given
which typesets every citation and reference example in the APA
6th edition style guide. This is a legacy style for 6th Edition
documents. Please use the BibLaTeX-apa style package for the
latest APA edition conformance.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-apa6
%doc %{_texmfdistdir}/doc/latex/biblatex-apa6

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
