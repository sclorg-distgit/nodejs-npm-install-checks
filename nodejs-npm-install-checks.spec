%{?scl:%scl_package nodejs-npm-install-checks}
%{!?scl:%global pkg_name %{name}}

%nodejs_find_provides_and_requires

Name:           %{?scl_prefix}nodejs-npm-install-checks
Version:        1.0.4
Release:        2%{?dist}
Summary:        Install checks for NPM
License:        BSD-2-Clause
Group:          Development/Languages/Other
Url:            https://github.com/npm/npm-install-checks
Source:         http://registry.npmjs.org/npm-install-checks/-/npm-install-checks-%{version}.tgz
BuildRequires:  nodejs010
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
A package that contains checks that npm runs during the installation. 

%prep
%setup -q -n package

%build
%nodejs_fixdep semver 2.3

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-install-checks
cp -pr package.json index.js \
        %{buildroot}%{nodejs_sitelib}/npm-install-checks/
%nodejs_symlink_deps

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{nodejs_sitelib}/npm-install-checks

%changelog
* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

