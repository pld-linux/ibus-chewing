Summary:	The Chewing engine for IBus input platform
Summary(pl.UTF-8):	Silnik Chewing dla platformy wprowadzania znaków IBus
Summary(zh_TW.UTF-8):	IBus新酷音輸入法
Name:		ibus-chewing
Version:	1.4.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	67d944ddfb7dd4eb325967ce43390092
URL:		http://code.google.com/p/ibus/
BuildRequires:	GConf2-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	gettext-devel
BuildRequires:	gob2 >= 2.0.16
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	ibus-devel >= 1.4
BuildRequires:	libchewing-devel >= 0.3.3
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	rpmbuild(macros) >= 1.604
Requires(post,preun):	GConf2
Requires:	GConf2
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
%setup -q -n %{name}-%{version}-Source

%build
%cmake \
	-DLIBEXEC_DIR=%{_libexecdir}

%{__make}

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
%gconf_schema_install ibus-chewing.schemas

%preun
%gconf_schema_uninstall ibus-chewing.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README RELEASE-NOTES.txt USER-GUIDE
%attr(755,root,root) %{_libexecdir}/ibus-engine-chewing
%{_datadir}/%{name}
%{_datadir}/ibus/component/chewing.xml
%{_sysconfdir}/gconf/schemas/ibus-chewing.schemas
