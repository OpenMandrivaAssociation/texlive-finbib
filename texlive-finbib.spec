# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/finplain.bst
# catalog-date 2008-12-07 00:01:13 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-finbib
Version:	20081207
Release:	9
Summary:	A Finnish version of plain.bst
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/finplain.bst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/finbib.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive finbib package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/finbib/finplain.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081207-2
+ Revision: 751871
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081207-1
+ Revision: 718441
- texlive-finbib
- texlive-finbib
- texlive-finbib
- texlive-finbib

