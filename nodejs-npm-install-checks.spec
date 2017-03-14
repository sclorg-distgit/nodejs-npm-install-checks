%{?scl:%scl_package nodejs-npm-install-checks}
%{!?scl:%global pkg_name %{name}}

%nodejs_find_provides_and_requires

Name:           %{?scl_prefix}nodejs-npm-install-checks
Version:        3.0.0
Release:        1%{?dist}
Summary:        Install checks for NPM
License:        BSD
Url:            https://github.com/npm/npm-install-checks
Source:         http://registry.npmjs.org/npm-install-checks/-/npm-install-checks-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A package that contains checks that npm runs during the installation. 

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-install-checks
cp -pr package.json index.js \
        %{buildroot}%{nodejs_sitelib}/npm-install-checks/
%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/npm-install-checks

%changelog
* Tue Jan 17 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-1
- Update, correct license name

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.6-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.6-2
- Rebuilt with updated metapackage

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.6-1
- New upstream release

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

