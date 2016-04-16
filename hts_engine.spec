Summary:	hts_engine API
Name:		hts_engine
Version:	1.10
Release:	1
License:	BSD
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/hts-engine/%{name}_API-%{version}.tar.gz
# Source0-md5:	5626d1e2522659e93fb295f0b42339f5
URL:		http://hts-engine.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The hts_engine is software to synthesize speech waveform from HMMs
trained by the HMM-based speech synthesis system (HTS).

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{name}_API-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_bindir}/hts_engine

%files devel
%defattr(644,root,root,755)
%{_includedir}/HTS_engine.h
%{_libdir}/libHTSEngine.a
