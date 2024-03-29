#
# Conditional build:
%bcond_with	tests	# unit tests
#
%define		pdir	Net
%define		pnam	HTTP
Summary:	Net::HTTP - Low-level HTTP connection (client)
Summary(pl.UTF-8):	Net::HTTP - nieskopoziomowe połączenie HTTP (klient)
Name:		perl-Net-HTTP
Version:	6.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1682735ddd1c059864ca5c1bbf15ab95
URL:		https://metacpan.org/release/Net-HTTP
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-URI
%endif
Suggests:	perl-IO-Socket-SSL >= 2.012
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::HTTP class is a low-level HTTP client. An instance of the
Net::HTTP class represents a connection to an HTTP server. The HTTP
protocol is described in RFC 2616. The Net::HTTP class supports
HTTP/1.0 and HTTP/1.1.

%description -l pl.UTF-8
Klasa Net::HTTP jest niskopoziomowym klientem HTTP. Instancja tej
klasy reprezentuje połączenie z serwerem HTTP. Protokół HTTP jest
opisany w RFC 2616. Klasa Net::HTTP obsługuje HTTP/1.0 i HTTP/1.1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS Changes
%{perl_vendorlib}/Net/HTTP.pm
%{perl_vendorlib}/Net/HTTPS.pm
%{perl_vendorlib}/Net/HTTP
%{_mandir}/man3/Net::HTTP*.3pm*
