Name:           opencore-amr
Version:        0.1.1
Release:        1%{?dist}
Summary:        OpenCORE Adaptive Multi Rate Narrowband and Wideband speech lib
Group:          System Environment/Libraries
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Library of OpenCORE Framework implementation of Adaptive Multi Rate Narrowband
and Wideband speech codec.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
# hack hack hack
if [ "%{_lib}" = "lib64" ]; then
  sed -i -e 's|/lib/|/lib64/|g' -e 's|/lib$|/lib64|g' */Makefile
fi


%build
make %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS -x c -std=c99 -fPIC"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}
# we don't want the static libraries
rm $RPM_BUILD_ROOT%{_libdir}/libopencore-amr??.a


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc opencore/ChangeLog opencore/NOTICE opencore/README
%{_libdir}/libopencore-amr??.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/opencore-amr??
%{_libdir}/libopencore-amr??.so


%changelog
* Thu Jul 30 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.1-1
- First version of the RPM Fusion package
