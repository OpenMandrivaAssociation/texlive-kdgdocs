Name:		texlive-kdgdocs
Version:	24498
Release:	2
Summary:	Document classes for Karel de Grote University College
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kdgdocs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdgdocs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two classes for usage by KdG professors and
master students: - kdgcoursetext: for writing course texts, and
- kdgmasterthesis: for writing master's theses. The bundle
replaces the original kdgcoursetext package (now removed from
the archive).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
