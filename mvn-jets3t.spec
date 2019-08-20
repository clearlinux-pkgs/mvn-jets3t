#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jets3t
Version  : 0.9.0
Release  : 2
URL      : http://bitbucket.org/jmurty/jets3t/downloads/jets3t-0.9.0.zip
Source0  : http://bitbucket.org/jmurty/jets3t/downloads/jets3t-0.9.0.zip
Source1  : https://repo.maven.apache.org/maven2/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.jar
Source2  : https://repo.maven.apache.org/maven2/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.pom
Source3  : https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.jar
Source4  : https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.1 MIT
Requires: mvn-jets3t-data = %{version}-%{release}
Requires: mvn-jets3t-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
JetS3t
======
JetS3t is a free, open-source Java toolkit and application suite for
Amazon Simple Storage Service (Amazon S3), Amazon CloudFront content
delivery network, and Google Storage for Developers.

%package data
Summary: data components for the mvn-jets3t package.
Group: Data

%description data
data components for the mvn-jets3t package.


%package license
Summary: license components for the mvn-jets3t package.
Group: Default

%description license
license components for the mvn-jets3t package.


%prep
%setup -q -n jets3t-0.9.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jets3t
cp LICENSE-2.0.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/LICENSE-2.0.txt
cp applets/images/nuvola/license.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/applets_images_nuvola_license.txt
cp libs/bouncycastle/license.html %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_bouncycastle_license.html
cp libs/commons-codec/LICENSE %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_commons-codec_LICENSE
cp libs/commons-logging/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_commons-logging_LICENSE.txt
cp libs/httpcomponents/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_httpcomponents_LICENSE.txt
cp libs/jackson/LICENSE %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_jackson_LICENSE
cp libs/java-xmlbuilder/LICENSE-2.0.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_java-xmlbuilder_LICENSE-2.0.txt
cp libs/logging-log4j/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_logging-log4j_LICENSE.txt
cp libs/safehaus_jug/LICENSE-2.0.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/libs_safehaus_jug_LICENSE-2.0.txt
cp resources/images/nuvola/license.txt %{buildroot}/usr/share/package-licenses/mvn-jets3t/resources_images_nuvola_license.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.jar
/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.7.1/jets3t-0.7.1.pom
/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.jar
/usr/share/java/.m2/repository/net/java/dev/jets3t/jets3t/0.9.0/jets3t-0.9.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jets3t/LICENSE-2.0.txt
/usr/share/package-licenses/mvn-jets3t/applets_images_nuvola_license.txt
/usr/share/package-licenses/mvn-jets3t/libs_bouncycastle_license.html
/usr/share/package-licenses/mvn-jets3t/libs_commons-codec_LICENSE
/usr/share/package-licenses/mvn-jets3t/libs_commons-logging_LICENSE.txt
/usr/share/package-licenses/mvn-jets3t/libs_httpcomponents_LICENSE.txt
/usr/share/package-licenses/mvn-jets3t/libs_jackson_LICENSE
/usr/share/package-licenses/mvn-jets3t/libs_java-xmlbuilder_LICENSE-2.0.txt
/usr/share/package-licenses/mvn-jets3t/libs_logging-log4j_LICENSE.txt
/usr/share/package-licenses/mvn-jets3t/libs_safehaus_jug_LICENSE-2.0.txt
/usr/share/package-licenses/mvn-jets3t/resources_images_nuvola_license.txt
