%undefine __cmake_in_source_build

Name:           wpebackend-fdo
Version:        1.14.3
Release:        %autorelease
Summary:        A WPE backend designed for Linux desktop systems

License:        BSD
URL:            https://github.com/Igalia/%{name}
Source0:        https://wpewebkit.org/releases/wpebackend-fdo-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0)

%description
A WPE backend designed for Linux desktop systems.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-1.0.so.1
%{_libdir}/libWPEBackend-fdo-1.0.so.1.*

%files devel
%{_includedir}/wpe-fdo-1.0
%{_libdir}/libWPEBackend-fdo-1.0.so
%{_libdir}/pkgconfig/wpebackend-fdo-1.0.pc

%changelog
%autochangelog
