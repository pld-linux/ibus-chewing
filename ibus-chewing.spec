Summary:	The Chewing engine for IBus input platform
Summary(pl.UTF-8):	Silnik Chewing dla platformy wprowadzania znaków IBus
Summary(zh_TW.UTF-8):	IBus新酷音輸入法
Name:		ibus-chewing
Version:	2.0.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/definite/ibus-chewing/releases
Source0:	https://github.com/definite/ibus-chewing/releases/download/v%{version}/%{name}-%{version}-Source.tar.xz
# Source0-md5:	e154ed095a769425dec7868f3924728a
URL:		https://chewing.im/projects/ibus-chewing
BuildRequires:	cmake >= 3.21.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk4-devel >= 4.0
BuildRequires:	ibus-devel >= 1.5.11
BuildRequires:	libadwaita-devel
BuildRequires:	libchewing-devel >= 0.5.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.604
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,preun):	glib2 >= 1:2.26
Requires:	ibus >= 1.5.11
Requires:	libchewing >= 0.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus-chewing is an IBus front-end of Chewing, an intelligent Chinese
input method for Zhuyin (BoPoMoFo) users. It supports various Zhuyin
keyboard layout, such as standard (DaChen), IBM, Gin-Yeah, Eten, Eten
26, Hsu, Dvorak, Dvorak-Hsu, and DaChen26.

Chewing also support toned Hanyu pinyin input.

%description -l pl.UTF-8
IBus-chewing to silnik dla platformy IBus będący interfejsem do
inteligentnej metody wprowadzania znaków Chewing, przeznaczonej dla
użytkowników Zhuyin (BoPoMoFo). Obsługuje różne układy klawiatury
Zhuyin, takie jak standardowy (DaChen), IBM, Gin-Yeah, Eten, Eten 26,
Hsu, Dvorak, Dvorak-Hsu, DaChen26.

%description -l zh_TW.UTF-8
IBus-chewing 是新酷音輸入法的IBus前端。
新酷音輸入法是個智慧型注音輸入法，支援多種鍵盤布局，諸如：
標準注音鍵盤、IBM、精業、倚天、倚天26鍵、許氏、Dvorak、
Dvorak許氏 及大千26鍵。

本輸入法也同時支援帶調漢語拼音輸入。

%prep
%setup -q -n %{name}-%{version}-Source

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# We install document using %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md ChangeLog-1.x README.md USER-GUIDE
%attr(755,root,root) %{_libexecdir}/ibus-engine-chewing
%attr(755,root,root) %{_libexecdir}/ibus-setup-chewing
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.freedesktop.IBus.Chewing.gschema.xml
%{_datadir}/ibus/component/chewing.xml
%{_desktopdir}/ibus-setup-chewing.desktop
