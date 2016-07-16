## Don't mess with the contents, we're not building from source
#%define __jar_repack 0
#%define __os_install_post %{nil}

# Don't autocalculate provides list
#%define __find_provides %{nil}
#%define __find_requires %{nil}
#%define _use_internal_dependency_generator 0

# So we don't have to do complicated excludes/etc, just explicitly list what we want
#%define _unpackaged_files_terminate_build 0

Name: spirent-%{branch}-axon-utilenv
Version: 1.0
Release: %{spirent_buildnumber}
Summary: Spirent Python Environment
BuildArch: noarch
License: Original
Group: Applications/Spirent
Vendor: Spirent Communications plc
URL: http://www.spirent.com
Provides: spirent-axon-utilenv
Source0: make-index.pl
Source1: pkgs-to-install.txt
Source2: packages
Source3: setup.sh

%{?with_obsoletes:Obsoletes: spirent-axon-utilenv}

%description
Provides python virtualenv in /local/utilenv/install that
meets dependency requirements for axon use.

NOTICE - This is a Tomahawk/Axon specific packaging. Do not
use these RPMs elsewhere without contacting Enterprise team.

%prep

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/local/utilenv/repo
mkdir -p $RPM_BUILD_ROOT/local/utilenv/repo/packages

# Copy all of the python tarballs/zips from central repo
cp %{SOURCE0} $RPM_BUILD_ROOT/local/utilenv/repo/make-index.pl
cp %{SOURCE1} $RPM_BUILD_ROOT/local/utilenv/repo/pkgs-to-install.txt
cp %{SOURCE2}/* $RPM_BUILD_ROOT/local/utilenv/repo/packages/
cp %{SOURCE3} $RPM_BUILD_ROOT/local/utilenv/repo/setup.sh

%clean

rm -rf $RPM_BUILD_ROOT

%pre

grep "^utility:" /etc/passwd >/dev/null
if [ $? != 0 ]; then
mkdir -p /local/utility
adduser -d /local/utility utility
fi

%post

/local/utilenv/repo/setup.sh

%postun

%files
%defattr(644,utility,utility,755)

/local/utilenv/repo/packages/*

%attr(644,utility,utility) /local/utilenv/repo/pkgs-to-install.txt
%attr(755,utility,utility) /local/utilenv/repo/make-index.pl
%attr(755,utility,utility) /local/utilenv/repo/setup.sh

%changelog
