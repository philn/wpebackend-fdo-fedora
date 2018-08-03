Name:           wpebackend-fdo
Version:        0.1
Release:        1%{?dist}
Summary:        A WPE backend designed for Linux desktop systems

License:        BSD
URL:            https://github.com/Igalia/%{name}
Source0:        https://github.com/Igalia/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  wpebackend-devel
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  glib2-devel
BuildRequires:  wpebackend-fdo

%description
A WPE backend designed for Linux desktop systems.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n WPEBackend-fdo-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake \
  ..
popd

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-0.1.so.0
%{_libdir}/libWPEBackend-fdo-0.1.so.0.*

%files devel
%{_includedir}/wpe-fdo-0.1
%{_libdir}/libWPEBackend-fdo-0.1.so
%{_libdir}/pkgconfig/wpebackend-fdo-0.1.pc

%changelog
* Mon Jul 16 2018 Chris King <bunnyapocalypse@fedoraproject.org> - 0.1-1
- Initial RPM package
