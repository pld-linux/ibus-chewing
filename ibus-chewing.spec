Summary:	The Chewing engine for IBus input platform
Summary(zh_TW):	IBus新酷音輸入法
Name:		ibus-chewing
Version:	1.3.9.2
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	8d177d67647944f5d1f9cca0654eaccb
Patch0:		%{name}-696864-abrt-ibus-1.4.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	GConf2-devel
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	gob2 >= 2.0.16
BuildRequires:	gtk+2-devel
BuildRequires:	ibus-devel >= 1.1
BuildRequires:	libchewing-devel >= 0.3.3
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	ibus >= 1.1
Requires:	libchewing >= 0.3.3
Requires:	GConf2
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus-chewing is an IBus front-end of Chewing, an intelligent Chinese
input method for Zhuyin (BoPoMoFo) users. It supports various Zhuyin
keyboard layout, such as standard (DaChen), IBM, Gin-Yeah, Eten, Eten
26, Hsu, Dvorak, Dvorak-Hsu, and DaChen26.

Chewing also support toned Hanyu pinyin input.

%description -l zh_TW
IBus-chewing 是新酷音輸入法的IBus前端。
新酷音輸入法是個智慧型注音輸入法，支援多種鍵盤布局，諸如：
標準注音鍵盤、IBM、精業、倚天、倚天26鍵、許氏、Dvorak、
Dvorak許氏 及大千26鍵。

本輸入法也同時支援帶調漢語拼音輸入。

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p1

%build
%cmake \
	-DLIBEXEC_DIR=%{_libexecdir}

%{__make} VERBOSE=1

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
%doc RELEASE-NOTES.txt AUTHORS README ChangeLog USER-GUIDE
%{_libexecdir}/ibus-engine-chewing
%{_datadir}/%{name}
%{_datadir}/ibus/component/chewing.xml
%{_sysconfdir}/gconf/schemas/ibus-chewing.schemas
