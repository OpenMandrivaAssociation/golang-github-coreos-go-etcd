# Run tests in check section
# Needs etcd running
%bcond_with check

# https://github.com/coreos/go-etcd
%global goipath         github.com/coreos/go-etcd
Version:                2.0.0

%global common_description %{expand:
Go client library for etcd.}

%gometa

Name:           golang-github-coreos-go-etcd
Release:        1%{?dist}
Summary:        Go client library for etcd
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/ugorji/go/codec)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Update to new go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.13.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.12.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.11.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.10.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.9.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.8.git68b33a3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.7.git68b33a3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.6.git68b33a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.5.git68b33a3
- Bump to upstream 68b33a3ba02a45d5f98bd7952e3e63e653a38252
  related: #1246214

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.4.git4cceaf7
- Update to spec-2.1
  related: #1246214

* Mon Aug 31 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.3.git4cceaf7
- Bump to upstream 4cceaf7283b76f27c4a732b20730dcdb61053bf5
  resolves: #1246214

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-0.2.git0424b5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 2.0.0-0.1.git0424b5f
- Bump to upstream 0424b5f86ef0ca57a5309c599f74bbb3e97ecd9d
  related: #1141807

* Fri Apr 10 2015 Eric Paris <eparis@redhat.com>
- Bump to version supporting etcd 2.0

* Tue Apr 7 2015 Eric Paris <eparis@redhat.com>
- include etcd dep

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 0.4.6-0.2.rc1.git2af7a95
- Bump to upstream 2af7a9525b09fb715b215a1fb852dd4814ef52b5
  related: #1141807

* Wed Feb 18 2015 jchaloup <jchaloup@redhat.com> - 0.4.6-0.1.rc1.git6aa2da5
- Bump to upstream 6aa2da5a7a905609c93036b9307185a04a5a84a5
  related: #1141807

* Wed Jan 28 2015 jchaloup <jchaloup@redhat.com> - 0.2.0-0.5.rc1.gitb7c233e
- Bump to upstream b7c233e2ef9be1016c63f66145161b317165ad7e
  related: #1141807

* Thu Oct 23 2014 jchaloup <jchaloup@redhat.com> - 0.2.0-0.4.rc1.git6fe04d5
- Choose the correct architecture
  related: #1141807

* Thu Oct 23 2014 jchaloup <jchaloup@redhat.com> - 0.2.0-0.3.rc1.git6fe04d5
- Bump to upstream 6fe04d580dfb71c9e34cbce2f4df9eefd1e1241e
  resolves: #1141807

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-0.2.rc1.git23142f6
 - do not redefine gopath
 - do not own dirs owned by golang
 - correct version number, rc tag goes in release
 - noarch

* Sat Sep 06 2014 Eric Paris <eparis@redhat.com - 0.2.rc1-0.1.git23142f67.2
- Bump to upstream 23142f6773a676cc2cae8dd0cb90b2ea761c853f

* Wed Aug 20 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.0-0.1-rc1
- Initial fedora package
