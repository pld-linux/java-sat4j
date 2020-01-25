#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	source		# don't build source jar
%bcond_without	tests		# don't build and run tests


# We want the version to match that shipped in Eclipse's Orbit project
%define		eclipsedate	20100429

%define		srcname		sat4j
Summary:	A library of SAT solvers written in Java
Name:		java-%{srcname}
Version:	2.2.0
Release:	0.1
License:	EPL or LGPLv2
Group:		Libraries/Java
# Created by sh %{srcname}-fetch.sh
Source0:	%{srcname}-%{version}.tar.xz
# Source0-md5:	7f11f90302bbf8091c5c7b6e179df2bd
Source1:	%{srcname}-fetch.sh
URL:		http://www.sat4j.org/
BuildRequires:  ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q -n %{srcname}-%{version}

%build
export JAVA_HOME="%{java_home}"

%ant -Dbuild.compiler=modern -Drelease=%{version} -DBUILD_DATE=%{eclipsedate} p2 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a dist/%{version}/org.sat4j.core.jar $RPM_BUILD_ROOT%{_javadir}
cp -a dist/%{version}/org.sat4j.pb.jar $RPM_BUILD_ROOT%{_javadir}
cp -a dist/%{version}/sat4j-pb.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_javadir}/*.jar
