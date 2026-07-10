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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

