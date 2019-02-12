Name:           photoflare
Version:        1.5.6
Release:        1
Summary:        Quick, simple but powerful Cross Platform image editor.
License:        GPL3
Group:          Graphics
URL:            http://photoflare.io/
Source0:        https://github.com/PhotoFlare/photoflare/archive/v1.5.6/photoflare-1.5.6.tar.gz
BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qmake5
BuildRequires:  rpm-helper

%description
Quick, simple but powerful Cross Platform image editor.

%prep
%setup -q

%build
%qmake_qt5
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
