#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Outlook-Message
Summary:	Email::Outlook::Message - MS Outlook .msg format converter
Summary(pl.UTF-8):	Email::Outlook::Message - konwerter formatu .msg Microsoft Outlooka
Name:		perl-Email-Outlook-Message
Version:	0.909
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVZ/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94cc93fcf6657d8cd5254854cae6998a
#URL:		http://search.cpan.org/dist/Email-Outlook-Message/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::All)
BuildRequires:	perl-Email-MIME >= 1.454
BuildRequires:	perl-Email-MIME-ContentType >= 1.014
BuildRequires:	perl-Email-Simple >= 2.003
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
%dir %{perl_vendorlib}/Email/Outlook
%{perl_vendorlib}/Email/Outlook/*.pm
%{_mandir}/man3/*
