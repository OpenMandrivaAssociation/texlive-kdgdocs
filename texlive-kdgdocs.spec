# revision 24498
# category Package
# catalog-ctan /macros/latex/contrib/kdgdocs
# catalog-date 2011-11-03 00:18:47 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-kdgdocs
Version:	1.0
Release:	1
Summary:	Document classes for Karel de Grote University College
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kdgdocs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle provides two classes for usage by KdG professors and
master students: - kdgcoursetext: for writing course texts, and
- kdgmasterthesis: for writing master's theses. The bundle
replaces the original kdgcoursetext package (now removed from
the archive).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kdgdocs/kdgcoursetext.cls
%{_texmfdistdir}/tex/latex/kdgdocs/kdgmasterthesis.cls
%doc %{_texmfdistdir}/doc/latex/kdgdocs/LICENSE
%doc %{_texmfdistdir}/doc/latex/kdgdocs/README
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdg_color.eps
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdg_color.pdf
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdgcoursetext-example.pdf
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdgcoursetext-example.tex
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdgdocs.pdf
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdgmasterthesis-example.pdf
%doc %{_texmfdistdir}/doc/latex/kdgdocs/kdgmasterthesis-example.tex
%doc %{_texmfdistdir}/doc/latex/kdgdocs/manifest.txt
%doc %{_texmfdistdir}/doc/latex/kdgdocs/pi-orchid.jpg
#- source
%doc %{_texmfdistdir}/source/latex/kdgdocs/kdgdocs.dtx
%doc %{_texmfdistdir}/source/latex/kdgdocs/kdgdocs.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}