Summary:	The Chewing engine for IBus input platform
Summary(pl.UTF-8):	Silnik Chewing dla platformy wprowadzania znaków IBus
Summary(zh_TW.UTF-8):	IBus新酷音輸入法
Name:		ibus-chewing
Version:	1.6.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/definite/ibus-chewing/releases
Source0:	https://github.com/definite/ibus-chewing/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	65a947645ceaef03fc18cd6ebbeddb22
URL:		http://chewing.im/projects/ibus-chewing
BuildRequires:	cmake >= 2.8.0
BuildRequires:	cmake-fedora-modules
BuildRequires:	gettext-tools
BuildRequires:	gob2 >= 2.0.16
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	ibus-devel >= 1.4
BuildRequires:	libchewing-devel >= 0.3.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.604
BuildRequires:	xorg-lib-libX11-devel
Requires(post,preun):	glib2 >= 1:2.26
Requires:	ibus >= 1.4
Requires:	libchewing >= 0.3.3
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
%setup -q

%build
%cmake \
	-DLIBEXEC_DIR=%{_libexecdir}

%{__make}

# *.po files not compiled by default, but required on install(?)
%{__make} -C po translations

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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
%doc AUTHORS ChangeLog README.md RELEASE-NOTES.txt USER-GUIDE
%attr(755,root,root) %{_libexecdir}/ibus-engine-chewing
%attr(755,root,root) %{_libexecdir}/ibus-setup-chewing
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.freedesktop.IBus.Chewing.gschema.xml
%{_datadir}/ibus/component/chewing.xml
%{_desktopdir}/ibus-setup-chewing.desktop
