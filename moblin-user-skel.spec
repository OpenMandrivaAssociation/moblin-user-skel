Name:           moblin-user-skel
Version:        0.11
Release:        %mkrel 1
Summary:        Skel files for users on Moblin
Group:          System Environment/Base
License:        CC-BY
URL:            http://www.moblin.org
Source0:        http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Populate the home directory for Moblin users.

%prep
%setup -q


%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} $RPM_BUILD_ROOT/etc/skel
%{__cp} -r .bkl-thumbnails $RPM_BUILD_ROOT/etc/skel
%{__cp} -r .kozo $RPM_BUILD_ROOT/etc/skel
%{__cp} -r .local $RPM_BUILD_ROOT/etc/skel
%{__cp} -r .gnome2 $RPM_BUILD_ROOT/etc/skel 
%{__cp} -r .thumbnails $RPM_BUILD_ROOT/etc/skel 
%{__cp} -r .recently-used.xbel $RPM_BUILD_ROOT/etc/skel 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/skel/
