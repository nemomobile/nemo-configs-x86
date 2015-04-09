# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-configs-x86

# >> macros
# << macros

Summary:    Some configs for x86-generic adaptation in Nemo Mobile
Version:    0.1
Release:    1
Group:      Configs
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/nemomobile/nemo-configs-x86
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-configs-x86.yaml

%description
%{summary}.


%package vm-common
Summary:    Common files shared by both Xorg and Wayland for x86 vm adaptation
Group:      Configs

%description vm-common
%{summary}.


%package vm-xorg
Summary:    Xorg Configs for x86 vm adaptation
Group:      Configs
Requires:   nemo-configs-x86-vm-common
Provides:   nemo-configs-x86-vm > 0.2.1
Provides:   nemo-mobile-configs-x86-vm > 2
Conflicts:  nemo-configs-x86-vm-wayland
Obsoletes:  nemo-configs-x86-vm <= 0.2.1
Obsoletes:  nemo-mobile-configs-x86-vm <= 2

%description vm-xorg
%{summary}.


%package vm-wayland
Summary:    Wayland Configs for x86 vm adaptation
Group:      Configs
Requires:   nemo-configs-x86-vm-common
Requires:   qt5-plugin-generic-vboxtouch
Conflicts:  nemo-configs-x86-vm-xorg

%description vm-wayland
%{summary}.


%package generic
Summary:    Configs for generic x86 adaptation
Group:      Configs
Provides:   nemo-mobile-configs-x86-generic > 2
Obsoletes:  nemo-mobile-configs-x86-generic <= 2

%description generic
%{summary}.


%package prjconf
Summary:    Project configs for obs projects
Group:      Configs
Provides:   project-config

%description prjconf
%{summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%make_install
# << install pre

# >> install post
# << install post


%files vm-common
%defattr(-,root,root,-)
%{_sharedstatedir}/environment/nemo/61-x86-vm.conf
%{_sysconfdir}/mce/70-emul-mce.conf
# >> files vm-common
# << files vm-common

%files vm-xorg
%defattr(-,root,root,-)
# >> files vm-xorg
# << files vm-xorg

%files vm-wayland
%defattr(-,root,root,-)
%{_sharedstatedir}/environment/compositor/61-x86-vm-ui.conf
# >> files vm-wayland
# << files vm-wayland

%files generic
%defattr(-,root,root,-)
%{_sharedstatedir}/environment/nemo/61-x86-generic.conf
# >> files generic
# << files generic

%files prjconf
%defattr(-,root,root,-)
%{_datadir}/prjconf/x86-prjconf.xml
# >> files prjconf
# << files prjconf
