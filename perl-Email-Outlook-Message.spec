#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Email
%define	pnam	Outlook-Message
%include	/usr/lib/rpm/macros.perl
Summary:	Email::Outlook::Message - MS Outlook .msg format converter
Summary(pl.UTF-8):	Email::Outlook::Message - konwerter formatu .msg Microsoft Outlooka
Name:		perl-Email-Outlook-Message
Version:	0.918
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVZ/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9d0d5129219b1511b8ca514f4fe51c8
URL:		http://search.cpan.org/dist/Email-Outlook-Message/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::All)
BuildRequires:	perl-Email-MIME >= 1.923
BuildRequires:	perl-Email-MIME-ContentType >= 1.014
BuildRequires:	perl-Email-Simple >= 2.102
BuildRequires:	perl-OLE-Storage_Lite >= 0.14
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses .msg message files as produced by Microsoft Outlook.

%description -l pl.UTF-8
Email::Outlook::Message - konwerter formatu .msg Microsoft Outlooka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/msgconvert
%{_mandir}/man1/msgconvert.1*
%{perl_vendorlib}/Email/Outlook
%{_mandir}/man3/*
