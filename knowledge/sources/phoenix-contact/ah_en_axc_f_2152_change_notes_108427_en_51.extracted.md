<!-- Extracted from ah_en_axc_f_2152_change_notes_108427_en_51.pdf by extract_pdf.py (pypdf) on 2026-11-10. Working copy: check against the PDF before quoting. -->

<!-- page 1 -->

© Phoenix Contact 2025-08-13108427_en_51
AXC F 2152 – CHANGE NOTES
Application note 
1 General information
This document contains all changes made between firm-
ware version 1.0.0 and the current firmware version of the 
AXC F 2152 controller (item no. 2404267).
Current firmware version: 2025.6.0
Observe the following general notes:
Changes in firmware version 2025.0
The firmware version 2025.0 contains updated parts of 
the underlying Linux® operating system and adapts the 
PLCnext Runtime System to these changes. This can have 
an impact on your application.
It is therefore absolutely necessary to familiarize your-
self with these changes and the associated conse-
quences before performing the update to firmware ver-
sion 2025.0.
Note all the information in section 6 “Changes in firmware 
version 2025.0.2” and also read the additional information 
under Application-relevant changes 2025 and evaluate 
them for your own application.
Toolchain
To be able to use all new functions of a firmware version, 
always use all elements of the toolchain in the same ver-
sion. The toolchain includes, for example, 
PLCnext Engineer, SDK and PLCnext CLI.
Material damage due to a freezing of the outputs
With firmware versions 2019.6, 2019.3, or 2019.0 LTS, a 
high CPU load in conjunction with frequent PROFINET dis-
connections may cause the outputs of the Axioline local 
bus to freeze.
Make sure to perform an update to firmware version 
2019.0.4 LTS, 2019.6.3 or 2019.9 or higher.
Firmware update
In the context of a firmware update, the controller will be 
restarted. During this time, the plant availability can not be 
guaranteed.
Firmware releases
Feature releases or hotfixes of an LTS version are based on 
the previous versions of the respective branch. Therefore 
they only contain the features, changes, error corrections, 
and security updates of the previous version. Refer to 
“Firmware releases AXC F 2152” on page 3 to see on 
which release branch your firmware version is located and 
which features, changes, error corrections, and security 
updates your firmware version contains.
Documentation
– Make sure you always use the latest documentation. 
It can be downloaded at
phoenixcontact.net/product/2404267.
– Further information on the PLCnext Runtime and 
programming can be found under
plcnext.help
– Further information on security in the context of 
PLCnext Technology can be found under
security.plcnext.help
Firmware version
Product revision VC 19 of the controller is delivered with 
firmware version 2024.0.8 LTS.
1.1 Maritime approvals
The following firmware versions are certified for use in 
maritime applications:
2024.0.0 LTS, 2023.0.0 LTS, 2022.0.4 LTS, 2022.0.3 LTS, 
2021.0.3 LTS, 2020.0.1 LTS, 2020.0 LTS, 2019.0.4 LTS, 
2019.0 LTS
Change notes for the AXC F 2152 controller

<!-- page 2 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 2 / 101
2 Table of contents
1 General information......................................................1
2 Table of contents..........................................................2
3 Firmware releases AXC F 2152....................................3
4 Changes in firmware version 2025.6.0........................4
5 Changes in firmware version 2025.0.3........................7
6 Changes in firmware version 2025.0.2........................8
7 Changes in firmware version 2024.6.1..................... 17
8 Changes in firmware version 2024.6.0..................... 18
9 Changes in firmware version 2024.0.9 LTS.............. 21
10 Changes in firmware version 2024.0.8 LTS.............. 23
11 Changes in firmware version 2024.0.6 LTS.............. 24
12 Changes in firmware version 2024.0.5 LTS.............. 26
13 Changes in firmware version 2024.0.0 LTS.............. 27
14 Changes in firmware version 2023.6.1..................... 33
15 Changes in firmware version 2023.6.0..................... 34
16 Changes in firmware version 2023.0.7 LTS.............. 39
17 Changes in firmware version 2023.0.0 LTS.............. 41
18 Changes in firmware version 2022.9.0..................... 46
19 Changes in firmware version 2022.6.0..................... 48
20 Changes in firmware version 2022.3.0..................... 52
21 Changes in firmware version 2022.0.10 LTS............ 53
22 Changes in firmware version 2022.0.8 LTS.............. 54
23 Changes in firmware version 2022.0.4 LTS.............. 56
24 Changes in firmware version 2022.0.3 LTS.............. 57
25 Changes in firmware version 2021.9.0..................... 61
26 Changes in firmware version 2021.6.0..................... 64
27 Changes in firmware version 2021.0.5 LTS.............. 69
28 Changes in firmware version 2021.0.3 LTS.............. 70
29 Changes in firmware version 2021.0.2 LTS.............. 71
30 Changes in firmware version 2021.0 LTS ................. 73
31 Changes in firmware version 2020.6.1..................... 79
32 Changes in firmware version 2020.3.1..................... 83
33 Changes in firmware version 2020.0.1 LTS.............. 86
34 Changes in firmware version 2020.0 LTS ................. 86
35 Changes in firmware version 2019.9........................ 89
36 Changes in firmware version 2019.0.4 LTS.............. 91
37 Changes in firmware version 2019.6.3..................... 91
38 Changes in firmware version 2019.6........................ 92
39 Changes in firmware version 2019.3........................ 95
40 Changes in firmware version 2019.0 LTS ................. 96
41 Changes in firmware version 1.2.0 ........................... 98
42 Changes in firmware version 1.1.0 ........................... 99
43 Changes in firmware version 1.0.2 ......................... 100
44 Changes in firmware version 1.0.1 ......................... 101

<!-- page 3 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 3 / 101
3 Firmware releases AXC F 2152
Long-term
support
Feature
release
2023.0.0 LTS
2023.6.0
2024.0.0 LTS
2023.0.7 LTS
2024.0.6 LTS
2024.6.0
2024.0.8 LTS
2024.6.1
2025.0.2
2024.0.9 LTS
2025.0.3
2025.6.0
2020.0.1 LTS
2020.6.1
2020.3.1
2021.0 LTS
2021.0.2 LTS
2021.0.3 LTS
2021.0.5 LTS
2021.6.0
2021.9.0
2022.0.3 LTS
2022.0.4 LTS
2019.0 LTS
2019.9
2019.6
2019.3
2019.6.32019.0.4 LTS
2020.0 LTS
Long-term
support
Feature
release

<!-- page 4 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 4 / 101
4 Changes in firmware version 
2025.6.0
This section describes changes made between firmware 
version 2025.0.3 and firmware version 2025.6.0.
All parts of the previously released version are included in 
the current version.
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2025.6 or new-
er.
Select the latest template for firmware version 
2025.6 in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used. 
Please contact the Competence Center Services as 
to the details on safety firmware update procedure:
Phone: +49 5281 946 2777
E-mail: safety-service@phoenixcontact.com
AXC F XT SPLC 1000: 
AXC F XT SPLC 3000: 
4.1 New functions
Linux
In order to support the L2TPv4 protocol the modules 
l2tp_core, l2tp_netlink, l2tp_eth, and l2tp_ip are in-
cluded in the PLCnext Linux.
4.2 Error corrections
App
If an OCI container app was updated while it was in the 
RUN state, the app disappeared from the web‑based man-
agement 2 (WBM 2) without an error message. After re-
starting the PLC, the app was displayed again. To prevent 
this behavior, the app had to be set to the STOP state be-
fore updating. This known issue has been fixed.
Backup
The backup and restore feature did use a maximum file 
name length of 256 bytes for the backup archive. In some 
cases this was too short and backup and restore did not 
work properly. The maximum file name size has been in-
creased to 4096 bytes.
C/C++
Using the ANSI C API it was possible to trigger a Start() at 
the PlcManager while the PLC was in state “Starting”. This 
led to an invalid PlcState “Running | Starting”. Now the 
PlcManager waits until the “Starting” state has been fin-
ished.
WBM
– On the “password policy” tab of the WBM page “User 
policies" the values of the password interval rules 
“Password changes per interval” and “password 
change interval” were swapped with firmware version 
2025.0.
– On the WBM page “Diagnostics - Axioline”, diagnostic 
information could be cleared when downloading the 
project although the diagnostics information was still 
valid.
– On the WBM page “Diagnostics - Profinet”, the scroll-
ing behavior has been corrected in the tree view.
OPC UA server
If the OPC UA server's endpoint has been configured with 
an IP address that does not match to the IP configuration 
of the PLC, the OPC UA server threw an exception and the 
firmware exited. In this situation now the OPC UA server 
emits the notification 
Arp.Services.OpcUAServer.StartFailed. The firmware 
starts up and after  correction of the endpoint configura-
tion a project download turns the OPCUA server into oper-
ation. 
OPC UA client
The behavior of the PLC's built-in OPC UA client has been 
improved for a better coherency in the following cases: 
– A value change at the server side could be missed 
by OPC UA client if this change occurred while the 
connection between client and server is cut. 
– After the PLC program is started (also if “Write 
and start project” is executed in PLCnext Engi-
neer) the OPC UA client now retrieves the latest 
values from the configured server. After receiving 
these values, which may take some time, the 
OPC UA client writes them to the configured vari-
ables (thus overwriting the variables' initial val-
ue).
01.01.0000 ✓
02.10.0007 ✓
02.10.0006 -

<!-- page 5 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 5 / 101
System
– If with firmware 2025.0 the static logger was used by 
a component, which was executed in the PLCnext 
firmware process, no messages have been logged. 
This error has been fixed.
– When activating the Security Profile, the IP configura-
tion sometimes got lost and the PLC started with the 
default IP configuration. The PLC needed to be re-
booted another time. This known issue has been fixed.
Proficloud
If too many OUT port variables have been marked as “IoT” 
in PLCnext Engineer or as “Proficloud” attribute in C++, a 
System Watchdog (SWD) occurred. With firmware 2025.6, 
no SWD occurs in this case. Instead, a warning is issued in 
the “Arp.log” file, indicating that not all variables are sent 
to the Proficloud or to an MQTT broker.
PROFINET system redundancy
Depending on the behavior of the superior PROFINET con-
troller the configured “System redundancy data hold time” 
did not become effective for the built-in PROFINET device 
of the PLC. The robustness of the PROFINET device has 
now been increased.
EHMI
When retrieving a range of array values via REST call, the 
entire array was returned. This issue has been fixed and 
now only the values within the requested range are re-
turned.
SPNS
– When the “Signature verification” check was enabled 
on the WBM page “Security - Project integrity”, the 
“AXC F XT SPLC 1000” often went into failure state 
and also caused an ESM task watchdog in the 
“SafetyProxyTask” after the download of a safety 
project. This bug has been fixed.
– The SPLC 3000 copied exchange variables (non-safe-
exchange process-data) of data type BOOL only if pro-
cess data links were present in the project. In most 
cases such links do exist. This bug has been fixed.
4.3 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
4.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Abseil CPP
– CVE-2025-0838
Curl
– CVE-2025-4947
FastCGI
– CVE-2025-23016
Git
– CVE-2025-46835 
– CVE-2025-48384 
– CVE-2025-48385 
– CVE-2025-48386
Less
– CVE-2024-32487
Libxml2
– CVE-2025-6021 
– CVE-2025-49794 
– CVE-2025-49795 
– CVE-2025-49796
Libssh
– CVE-2025-5318
Libpam
– CVE-2025-6020 
– CVE-2024-10041
OpenVPN
– CVE-2025-2704
Perl
– CVE-2024-56406

<!-- page 6 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 6 / 101
Podman
– CVE-2024-11218
– CVE-2025-6032
Setuptools
– CVE-2025-47273
Sqlite
– CVE-2025-29088 
– CVE-2025-29087 
– CVE-2025-3277
Sudo
– CVE-2025-32462
– CVE-2025-32463
Syslog-ng
– CVE-2024-47619
TPM2
– CVE-2024-29040
WBM
– With firmware 2025.0, the user role “SecurityAdmin” 
has been renamed to “SecurityEngineer” but the per-
missions stayed the same. With that release, a minor 
issue is present: The “SecurityEngineer” user role 
must be used together with the “Admin” user role, 
because the user role “SecurityEngineer” incorrectly 
had no access rights for the user management as well 
as to activate/deactivate system services via WBM. 
This known issue has been fixed.
PROFINET
– A specific invalid UDP datagram sent to a PROFINET 
UDP port could cause a segmentation fault 
(SIGSEGV).

<!-- page 7 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 7 / 101
5 Changes in firmware version 
2025.0.3
This section describes changes made between firmware 
version 2025.0.2 and firmware version 2025.0.3.
All parts of the previously released version are included in 
the current version.
Important information
Updating to firmware versions 2025.0.2 and newer 
from older firmware versions may have unexpected 
effects on the existing application or specific user 
settings. 
It is strongly recommended to observe the following 
points before rolling out the firmware into productive 
operation: 
– Intensive study of the change notes in this section 
and further documentation under Application-
relevant changes 2025. 
– Backup the project data and configurations be-
fore the update.
– Qualification of the application with regard to 
functionality or compatibility after the update.
– A downgrade back is possible, but an automatic 
restoration of all specific configurations cannot be 
guaranteed. 
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2025.0 LTS or 
newer.
Select the latest template for firmware version 
2025.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used. 
Please contact the Competence Center Services as 
to the details on safety firmware update procedure:
Phone: +49 5281 946 2777
E-mail: safety-service@phoenixcontact.com
AXC F XT SPLC 1000: 
AXC F XT SPLC 3000: 
5.1 Error corrections
Network
– After updating the PLC to firmware 2025.0.2, domain 
names could sometimes not be resolved. As a result, 
it was not possible to establish a connection to the 
PLCnext Store, for example. Resolving domain names 
was only possible after one additional reboot after up-
dating the PLC. This error has now been fixed.
– If a gateway “0.0.0.0” was configured with a firmware 
older than 2025.0 the conversion of the IP configura-
tion incorrectly added this gateway to the network 
configuration of firmware 2025.0.2 (systemd). Now 
from firmware 2025.0.3 a gateway “0.0.0.0” is ig-
nored when converting the IP configuration and the 
“systemd” network management sets up a default 
gateway.
System
– Applications that caused certain system exceptions 
could raise a system watchdog which led to a reboot 
loop in firmware 2025.0.2. Under normal conditions 
the number of consecutive reboots is limited by the 
system. 
This error has been fixed.
5.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
01.01.0000 ✓
02.10.0007 ✓
02.10.0006 -

<!-- page 8 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 8 / 101
6 Changes in firmware version 
2025.0.2
This section describes changes made between firmware 
version 2024.6.1 and firmware version 2025.0.2.
All parts of the previously released version are included in 
the current version.
Important information
Updating to firmware versions 2025.0.2 and newer 
from older firmware versions may have unexpected 
effects on the existing application or specific user 
settings. 
It is strongly recommended to observe the following 
points before rolling out the firmware into productive 
operation: 
– Intensive study of the change notes in this section 
and further documentation under Application-
relevant changes 2025. 
– Backup the project data and configurations be-
fore the update.
– Qualification of the application with regard to 
functionality or compatibility after the update.
– A downgrade back is possible, but an automatic 
restoration of all specific configurations cannot be 
guaranteed. 
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2025.0 LTS or 
newer.
Select the latest template for firmware version 
2025.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used. 
Please contact the Competence Center Services as 
to the details on safety firmware update procedure:
Phone: +49 5281 946 2777
E-mail: safety-service@phoenixcontact.com
AXC F XT SPLC 1000: 
AXC F XT SPLC 3000: 
6.1 New functions
App Manager
As announced, the app part types “Linux Daemons” and 
"Shared Libraries" are discontinued. The AppManager 
supports the new app part type “OCI Container” which is 
intended to become the successor of daemon apps. Addi-
tionally the AppManager does no longer include the path 
of *.so files announced as “sharedlibs” by the 
app_info.json into the ld.so.conf file of the Linux OS.  Fur-
thermore, a new RSC service IAppManagerService has 
been developed. This service can be used to retrieve infor-
mation about installed apps and their state. In case of 
complex apps that are a combination of several apps the 
RSC service can be used to install the dependent apps in 
the necessary order.
Backup & Restore
The WBM has been extended by the page “Backup & Re-
store”. On this page, different data sets, for example con-
figuration or project files, can be selected and saved into 
an archive. Vice-versa an archive can be selected and its 
data sets can be restored. Backup & Restore uses the 
“PreparedForUpdate” state. At the moment only archives 
created with the same firmware version can be restored in 
order to ensure proper operation in case of future exten-
sions.
Configurable alarms
– In combination with firmware 2025.0.2 (or newer) 
PLCnext Engineer 2025.0 (or newer) supports a sys-
tem variable “ALARM_PROGRAM_STATUS” which 
provides information about the execution duration of 
the “AlarmProgram” instances.
– In combination with firmware 2025.0.2 (or newer) 
PLCnext Engineer 2025.0 (or newer) supports the use 
of variables to configure the alarm thresholds (previ-
ously only constants were supported).
GDS
IN and OUT ports of a field bus component can be ac-
cessed via GDS data access services. This includes IOs of 
the following field busses: 
– Axioline
– EtherNet/IP
– INTERBUS
– Modbus TCP client
– PROFIBUS
– PROFINET  
Additionally, the implementation of this feature enables to 
use elements of a field bus array in a GDS connector. Of 
01.01.0000 ✓
02.10.0007 ✓
02.10.0006 -

<!-- page 9 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 9 / 101
course, the data types of the “startPort” and “endPort” 
have to be compatible.
GRPC
The PLCnext gRPC service supports to browse for existent 
gRPC services. There is no need to use the related 
protobuf files.
Licenses
For certain licenses (for example license is checked from 
an OCI container) and as a preparation for future features, 
CodeMeter Runtime from WIBU-Systems has been added 
to the firmware. The WIBU runtime is not automatically 
started by the firmware.
Podman
The Podman container system can also be operated by the 
Linux user “admin” without root rights being required. 
Project integrity
The project integrity check has been extended by a project 
signature. On the WBM page “Project Integrity” the con-
troller can be configured if and how the integrity or signa-
ture is checked and how to react in case of an integrity 
breach. PLCnext Engineer 2025.0 (or newer) projects can 
be configured with a private key and a certificate for sign-
ing projects when downloading the project. Using the 
WBM this certificate can be stored in the trust store “Code 
Signing”. During this implementation also the safety proj-
ect is included in the project integrity check. 
A new RSC service has been implemented to read or write 
the project integrity configuration: 
Arp::Plc::Domain::Services::IPlcConfigService.
PROFINET
– The minimum update rate of the built-in PROFINET 
device has been reduced to 2 ms.
– The filter options “Station name”, “IP address” and 
“Device state” are supported on the “Diagnostics” - 
“Profinet” WBM page tabs “Device list” and 
“Tree view”.
SDK/C++
When creating a new project with the PLCnext CLI tool-
chain a header file named “<projectName>Library-
Info.hpp” is created. This header file yields a version num-
ber of the library as an instance of the ArpVersion class. A 
user-specific version number can be entered and main-
tained during further development of the library. For ACF 
components this version number can be retrieved among 
other information by the RSC service Arp::Base::Rsc:Com-
mons::ISystemInfoService.
WBM
– The WBM page “Local bus” has been split into two 
pages: “Axioline” and “INTERBUS”. This enables bus 
diagnostics if INTERBUS and Axioline are operated in 
parallel using an “AXC F XT IB” extension module.
– The WBM page “Firmware update” has been reworked 
in order to use the “PreparedForUpdate” state. At the 
same time not only the firmware but also 
“PLCnext Engineer Software Packages” can be in-
stalled to the PLC. Consequently the WBM page has 
been renamed to “Update”. In a future version this 
page can be extended to install further packages, for 
example safety-related firmware.
6.2 Changes
C++
– With the SDK version 2025.0 the language 
standard C++ 20 has been set in the compiler op-
tions (“-std=c++20”). The firmware itself is also com-
piled with this option set.
– For libraries created from C++, the firmware 2025.0 
checks the version of the SDK used to compile these 
libraries. If the SDK version is 2024.6 or older then the 
library is not loaded and a notification is emitted. In 
these cases the libraries have to be recompiled with 
an appropriate SDK. Note that such libraries may also 
be part of a PLCnext Engineer project.
General
Firmware version 2025.0.2 brings some fundamentally 
updated parts of the underlying Linux® operating system 
and adapts the PLCnext Runtime System to these 
changes, resulting in higher RAM and CPU utilization. This 
in turn can have an impact on existing applications if these 
applications are close to the maximum RAM and CPU per-
formance of the respective PLC type. For such applica-
tions, Phoenix Contact recommends also checking the 
RAM and CPU utilization when validating the functionality 
after a firmware and application update.
Firmware update
The Linux script “update-plcnext” has been removed (in-
cluding its product-specific symlinks). Please use the 
WBM, DaUM, OPC UA or the RSC service IDeviceControlS-
ervice::StartFirmwareUpdate() to install a different firm-
ware version.

<!-- page 10 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 10 / 101
Linux
– The Linux system has been updated to version 6.1.
– The “boost” packages have been updated to version 
1.84.0.
– Busybox has been removed entirely from the 
PLCnext Linux. Alternatives have been implemented 
for all necessary tools. Some of these alternatives 
have already been added with previous firmware ver-
sions. 
At the same time the following packages have also 
been removed:
– text editor “vim” as well as “vi”. Please use “na-
no” instead which is also set via Linux environ-
ment variable “EDITOR”.
– obsolete scripts related to gdbserver. These 
scripts have been added by Phoenix Contact but 
are no longer needed.
– script “plcnext-update” (see above)
– deprecated plug-in “stroke” of strongwan, exist-
ing configuration files (ipsec.conf) from 2024.6 or 
earlier firmware must be migrated to the new 
swanctl.conf syntax.
– the “ipsec” script, to control an ipsec connection. 
The swanctl commands must be used.
– the packages “cyrus-sasl” and “krb5” have been 
removed from the PLCnext Linux.
– Firmware 2024.0 shifted to OpenSSL 3.0. With firm-
ware 2025.0 the outdated OpenSSL 1.1.1 binaries 
have been removed as announced.
– Since the Linux init system “SysV” has been replaced 
with “systemd” the firmware can no longer be started 
or stopped with the “/etc/init.d/plcnext” script. 
Please use the command “systemctl” instead, e.g. 
“sudo systemctl stop plcnext”.
– The size of the “tmpfs” file system which is used for 
temporary files has been limited.
– Due to security reasons it is no longer possible to add 
users directly to the Linux system (using the command 
“useradd”). So the PLCnext user management is now 
the central authority to manage users.
LDAPS
In the past the firmware added PLCnext users with the role 
“Admin” also as Linux users to the Linux user manage-
ment. Consequently, these users are stored in the PLCnext 
user management as well as (local) users in the Linux user 
management. Furthermore, logging in to Linux (SSH, 
SFTP) was not possible for PLCnext users defined via LDAP 
server.
By enabling the LDAP server to make use of the PLCnext 
user role “Admin”, this procedure needed to be changed. 
As a consequence, before updating the firmware from 
≤ 2024.6 to ≥ 2025.0, these users as well as users added 
directly to the Linux system need to be removed manually. 
Any files and folders created by these users must be re-
moved, too, otherwise these files have an owner that is no 
longer known to the Linux user management. The same 
holds true for PLCnext user roles to which you have added 
the permission “arp.device/protocol.restricted_sftp:22”. 
All these data will be removed by resetting the PLC to de-
fault settings.
Network/system
By changing the Linux init system from “SysV” to “sys-
temd” Linux stores the IP configuration in different files 
and formats. As a consequence, PLCnext Linux is equipped 
with a conversion from the “SysV”-based configuration to 
the “systemd”-based configuration. When the PLC is 
booted this conversion starts. After a successful conver-
sion the firmware saves itself a hash of the converted IP 
configuration. At its next execution the conversion com-
pares the “SysV”-based configuration against the saved 
hash and converts only if necessary. The old IP configura-
tion remains at the overlay file system, so that this config-
uration becomes active when downgrading to a firmware 
≤ 2025.0. Furthermore, this conversion can handle all IP 
configurations set via PLCnext Engineer or the WBM.  In 
case the “SysV”-based configuration file 
“/etc/network/interfaces” was manually changed (root 
rights necessary) it must be checked if these changes have 
been converted, too. Note that firmware 2025.0.2 (and 
newer) only saves changes to the IP configuration in the 
new “systemd”-based configuration. Therefore when 
downgrading from firmware 2025.0.2 (or newer) to firm-
ware 2024.6 (or older) the IP configuration may change 
while up/downgrading between firmware 2019.x and 
2024.x keeps the IP configuration.  
Note: When switching to DHCP via RSC service 
“IDeviceSettingsService” using the key 
“Interfaces.Ethernet.[AdapterIndex].IpAssign” 
(PLCnext Engineer uses this service at its 
“Online parameters” editor) firmware version 2025.0.2 
keeps the set static IP address as well as the address set 
via DHCP while firmware version ≤ 2024.6 only makes use 
of the IP address set via DHCP.
GDS
Global variables connected to I/O and also system vari-
ables are no longer updated by the ESM task “GLOBALS” if 
no update task is configured. Instead the update is per-
formed by the task “GdsGlobals”. This task has the same 
priority and the same interval time of 50 ms but is not con-
trolled by the ESM. This means that the variables are up-
dated even in PLC state “Stop”.

<!-- page 11 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 11 / 101
Note: This is especially useful if the new system variable 
“PLC_STATE” shall be displayed via HMI.
Diagnostic log files
The diagnostic logging is split into several files, for exam-
ple: 
– Arp.log 
– Arp.Init.log
– Arp.Io.ProfinetStack.log 
– Arp.Services.Ehmi.log 
– Arp.Services.SpnsProx.log
– Custom.log
Previously, all log message have been logged in the file 
“Output.log”. In addition, the Linux command line tool 
“arp-merge-logs” has been developed and integrated in 
the PLCnext Linux. With this tool multiple log files can be 
merged into a single file. 
At the same time the non-security-related Arp log mes-
sages are no longer forwarded to syslog. Security-related 
logs are forwarded to syslog as with previous firmware 
versions.
User manager
The name of the PLCnext user role “SecurityAdmin” has 
been changed to “SecurityEngineer”. Only the name has 
been changed, the role's permissions remain the same.
Security Profile
– When activating the Security Profile, the PLCnext user 
“admin” remains (previous firmware versions did re-
move this user). Anyhow, this configuration must be 
adopted after the first installation to a minimum con-
figuration feature set needed for the application. See 
PLCnext Security Info Center (2025.0) for further in-
formation on risk analysis and secure-by-default con-
figuration.
– When the Security Profile is active, the system ser-
vices “APP MANAGER”, “DATALOGGER”, “GRPC LO-
CAL SERVER”, “LINUX SYSLOG”, “MODBUS CLIENT 
TCP”, “NETLOAD LIMITER”, “OPCUA CLIENT”, 
“PLCNEXT STORE”, “PROFICLOUD” and “SOFTWARE 
UPDATE” can be activated or deactivated via WBM or 
by an app.
– When activating the Security Profile, the system ser-
vices “APP MANAGER”, “DATALOGGER”, “GRPC LO-
CAL SERVER”, and “NETLOAD LIMITER” are active 
additionally compared to firmware 2024.6.
– When activating the Security Profile, the firewall con-
figuration allows incoming and outgoing ICMP re-
quests (ping). 
System watchdog/system monitor
A new firmware component “system monitor” has been 
implemented. It monitors RAM and CPU load and emits 
notifications if certain levels are exceeded. In case of fur-
ther exceeding the component “system watchdog” is in-
formed and becomes active. Therefore, this component 
has been refactored. Both components reside in the same 
library. The “system watchdog” also reacts when a firm-
ware process died. In these cases the “systemwatchdog” 
collects diagnostic information and supervises an emer-
gency exit procedure. For diagnostics purpose several logs 
and active LTTNG traces are collected into a folder named 
/opt/plcnext/logs/Arp.System.Monitoring/[timestamp]-
Arp.system.Monitoring.Monitor.[reason] (Note that this 
path has been changed compared to FW 2024.0 and 
2024.6.). Up to 10 logs can be stored, older folders are de-
leted if necessary.
Furthermore, by RSC service or using PLCnext Engineer 
the start behavior after a system watchdog can be config-
ured (PLC remains in PlcState::Stop or performs a cold 
start). The above mentioned refactoring also changed the 
location where this configuration is stored. Consequently 
after updating to firmware 2025.0 or newer this configura-
tion is reset to the default setting (PLC remains in Plc-
State::Stop). Similarly, if this setting is performed with 
firmware version 2025.0 or newer, it will be lost during a 
firmware downgrade.
PLC
– The PLC state is available as system variable 
“PLC_STATE” (global variable in PLCnext Engineer). 
This variable is updated by the “GdsGlobals” task.
– The PLC state has been extended by the flag “Syste-
mError”. This flag is set when an error is detected 
during the setup phase of the firmware. Often these 
are configuration errors and should be fixed before re-
booting the PLC. A “SystemError” will also occur if a 
shared object (*.so) is configured for loading  in an ACF 
project that is compiled for an older version of the 
firmware (≤ 2024.6).

<!-- page 12 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 12 / 101
RSC
– The RSC service “IDeviceControl::StartFirmwareUp-
date()” has been refactored in order to use the update 
mechanism of the Software Update component in-
cluding the “PreparedForUpdate” state. In this con-
text the RSC service expects the firmware RAUC 
container in the folder /opt/plcnext/custom (previ-
ously /opt/plcnext).
WBM
– The integrated NTP server has been changed from 
“ntpd” to “chronyd”.  Configured NTP servers are not 
converted during firmware up- or downgrade. There-
fore check the NTP configuration and correct it if nec-
essary after a firmware up- or downgrade. 
Furthermore firmware ≤  2024.6 was able to store a 
comment per each configured NTP server, which is no 
longer supported with firmware 2025.0. 
Notes:
– “ntpd” is configured at /etc/ntp.conf. If necessary 
check here for the NTP server's IP addresses 
when updating the NTP configuration via WBM or 
PLCnext Engineer.
– With firmware 2025.0 the PLC may take several 
minutes to store date and time, for example if it is 
set via PLCnext Engineer. Do not power off the 
PLC during this period.
– With firmware 2025.0 the WBM has been refactored. 
In this context the former WBM page “Cockpit” was 
split into the pages “Overview” and 
“Device Maintenance”. “Overview” is displayed as de-
fault page after login and contains all displays while 
“Device Maintenance” contains all operational but-
tons. The “Welcome page” has been removed in the 
context of this refactoring.
– The diagnosis of the Axioline local bus was improved.  
In particular with many Axioline modules and/or mod-
ules which need longer time to respond to the PDI re-
quests of the PLC, some diagnostic information was 
not displayed in the past.
6.3 Error corrections
ANSI C LIB
The ANSI C function “getBufferPtrByPortname()” created 
unnecessary copies of the buffer. As a consequence buf-
fers returned by a previous call to this function (to get the 
buffer of a different port) were not updated on the 
fieldbus.
Axioline
Writing output process data in case of a PLC stop event 
with option “Substitution behavior: maintain last values” 
(setting in PLCnext Engineer) did not work.
DataLogger
The “IDataLoggerService2” “ReadVariablesData” method 
returned unexpected results like records for the NULL en-
tries in the database, but these only contained the 
“consistency” flag and the record type and no value.
EHMI
An exception of the eHMI occurred when too long strings 
for “user” or “password” were used for authentication.
GDS
Sporadic flickering could occur at fieldbus outputs when 
global variables were forced.
IEC 61131-3
–  A non-existent “AR_USER_ID” generated an excep-
tion in the PROFINET function block “GET_MODULE_-
DIFF_BLOCK” and stopped the PLC project.
– The function “GET_MICROSECONDS” returned wrong 
values after a 32 bit value overflow.
– The “IDLE Task” priority was displayed incorrectly as 
“0” in the “TASK_INFO” structure.
– The function blocks “PACK” and “UNPACK” do not 
process variables of data type “WSTRING”.
– After “Download Changes” (“Write and Start Project 
Changes” in PLCnext Engineer) the error message 
“free node at xxx is too small during DC procedure” 
could occur.
– When loading a retain backup file, the text “Backup 
file generated” was displayed incorrectly in the notifi-
cation “Security.Arp.Plc.Retain.BackupFilePrepared”.
– In case the PLC is stopped due to an exception (within 
the code of an ESM task) the retain values are invali-
dated. As a consequence a cold restart is required. So 
far the invalidation was performed only in case of an 
ESM task watchdog (but not in case of other excep-
tions). Tipp: If you are regularly facing exceptions, 
consider to use the function save/restore retain val-
ues in the cockpit of the WBM or PLCnext Engineer.
– After “Download Changes” (“Write and Start Project 
Changes” in PLCnext Engineer) it was not possible to 
safe the retain data with the button from 
PLCnext Engineer cockpit.

<!-- page 13 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 13 / 101
– If the PLC was in “RUN” or “STOP” state and “Reset” 
was called in this state, the PLC was first stopped and 
then reset. The entire sequence had no timeout mon-
itoring, which could lead to blocking in unfavorable 
project situations.
– The data type “IecWString80” was incorrectly not 
supported in Native Shared Library (C#/C++) projects.
Modbus client
In the event of a Modbus exception, invalid and changing 
input data can occur. This error will be fixed with a further 
firmware release. Meanwhile, as a workaround, process 
the read data only if the TCP communication is active and 
no exception is reported. This is true if the STATE variable 
has the value 16#0001. 
This known issue has been fixed.
Network
– Under high network load the built-in Ethernet inter-
face of the affected PLC types sometimes can reach a 
blocking state. In this state only a power reset can re-
enable the interface communication. To avoid this the 
PLCnext Technology network driver has a mechanism 
implemented to detect such situations and to react 
with a reset of the specific interface. By default behav-
ior of the Linux network stack a predefined default 
gateway configuration got lost during this reset. This 
“Known Issue” has been fixed.
– When new network adapter settings were written by 
“DCP”, two gateway entries were active by mistake.
OPC UA server
After downloading a new project, a system crash could 
occur sporadically if the OPC UA configuration was 
changed from “DNS name” to “IP address”. 
OPC UA client
– After a running OPC UA server/client communication 
is disconnected, it could happen that the exchanged 
data to the client was not updated according to the 
PLC project status after the connection was re-estab-
lished.
– If communication with the OPC UA server failed, for 
example due to a system crash, the communication of 
the OPC UA client never restarted correctly, even if the 
OPC UA server returned to normal status.
– Subscribing a huge amount of variables on the OPCUA 
server led to a “FATAL - Signal SIGSEGV” error when 
at the same target 32 clients were also subscribing a 
huge amount of variables.
– The OPC UA client has logged important information 
only with activated DEBUG level to the 'Output.log' 
file.
– The OPC UA client feature relies on changes in the 
source data to trigger the transfer of data between the 
client and the server. If the source data did not change 
for any period of time, there was no guarantee that the 
data values were synchronized between the client and 
the server, for example after an interruption in the cli-
ent-server connection.
PROFINET controller
– After hot-swapping a connected “AXL-P” I/O module, 
all PROFINET channel alarms were incorrectly 
cleared. 
– The root-cause of LLDP error messages in the log file 
“Output.log” in combination with several switch types 
was fixed.
RSC
It was not possible to use a string length of greater than 
4096 bytes in the data type “RscString<int N>” of 
RSC services.
Safety
AXC F 2152 with AXC F XT SPLC 1000 or 
AXC F XT SPLC 3000
The following known issue has been fixed:
If the “Download Changes” mechanism (“Write and Start 
Project Changes” in PLCnext Engineer) is used along with 
the SPLC 1000/3000, please take into account a possible 
malfunction in case the following steps have been per-
formed:
1 A safety-related project is downloaded to the safety-
related controller.  
2 A non-safety-related project is downloaded to the 
standard controller.  
3 A modified safety-related project is downloaded to 
the safety-related controller.  
4 An attempt is made to change the non-safety-related 
project using “Download Changes” (“Write and Start 
Project Changes” in PLCnext Engineer), which is re-
jected by the PLCnext firmware of the standard con-
troller (for example, by changing the task 
configuration).  
5 The device is restarted. (for example, voltage failure 
and recovery or request for restart in 
PLCnext Engineer)  
Attention: After the restart, the safety-related controller 
executes the original safety-related project from step 1. In 
order to prevent the described behavior, please addition-

<!-- page 14 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 14 / 101
ally carry out the following measures after every change of 
the safety project: 
– Perform a restart in the PLCnext Engineer software in 
the “Cockpit” editor of the standard controller or 
switch off the supply voltage of the device for at least 
30 s and then switch it on again (power reset).
– Compare the CRC checksum of the safety-related 
project using the system variables of the safety-relat-
ed controller or in the ”Cockpit Safe PLC” in the 
PLCnext Engineer software with the original CRC 
checksum before the restart.
SDK
With the SDK version 2021.6 the language standard C++ 
17 has been set in the compiler options (-std=c++17). The 
firmware itself is also compiled with this option set. Be-
sides some general C++ issues related to this C++17 stan-
dard, the following issue is related to PLCnext Technology: 
C++ 17 introduced the data type std::byte which was un-
fortunately not compatible with Arp::byte. Therefore, if the 
namespaces std and Arp were both active in the compila-
tion process, this resulted in an error. 
This known issue has been fixed, Arp::byte is now mapped 
to std:.byte.
SD card
The log message from the ExternalSDCardComponent in 
the log file in “Output.log” was ambiguous: It was unclear 
whether the message “de-activation state: activated” 
meant that the state was “deactivated” or “activated”.
SPNS
AXC F 2152 with AXC F XT SPLC 1000 or 
AXC F XT SPLC 3000
It was not possible to keep a stable running PROFINET 
process data communication with a system load of around 
85 % or more in combination with a SPLC left-alignable ex-
tension module.
System
– A system watchdog could occur sporadically. A possi-
ble cause of these watchdogs could be found in the 
connector to the PLCnext Store, especially when the 
PLC was not connected to the store. The system 
watchdog was preceded by a SIGSEGV.
– If the PROFINET device system service was deacti-
vated on the AXC F 2152 with an 
attached AXC F XT ETH 1TX module, a SIGSEGV (seg-
mentation fault) occurred. 
This known issue has been fixed.
– A software update could not be performed if the PLC 
was in state “FatalError”.
– An attempt to set the system time of the controller to 
a timepoint in year 2038 or later resulted in a system 
watchdog. This known issue has been fixed.
– If a user component caused a crash before the system 
watchdog was activated, the firmware terminated and 
the controller was available only via SSH. 
Note: The system watchdog was activated just before 
the “IControllerComponent::Start()” method was in-
voked. This known issue has been fixed.
TLS 2 FB
– An exception occurred in the function block in case 
the Ethernet connection was interrupted.
– The error code “0xC212” occurred unexpectedly on 
the function block “TLS_SOCKET_2”, although data 
could be exchanged.
– A high CPU load that was associated to the use of the 
“TLS_2” function blocks has been detected in the pre-
vious firmware version.
– The TLS_*_2 FB could not detect some passive socket 
closed when “a cable got pulled”. The TLS_*_2 FB 
continued to show an active connection for quite 
some time, way beyond the PLC's KeepAlive settings. 
In combination with PLCnext Engineer version 
2024.0.4 LTS or newer this issue has been solved.
Note: This issue was erroneously reported as fixed 
with firmware 2024.0.6 LTS. Now it has definitely 
been fixed.
WBM
– It was impossible to select a “Identity Store for HTTPS 
certificate” if a bad certificate was installed before-
hand.
– The texts and icons for the diagnostic pages in the 
WBM for PROFINET and local bus were previously dif-
ferent and have now been harmonized.
– The role “UserManager” did not have the permission 
for the LDAP configuration in the WBM as described in 
the documentation.
6.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 15 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 15 / 101
6.5 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
PLCnext Technology App
– The start script “initScriptTemplate” of 
PLCnext Technology Apps could be executed by the 
local user “root”.  If an attacker succeeded in install-
ing a malicious app or have it installed, he was able to 
fully compromise the system.
– The “post_updatescript” within the “updateconfigs” 
part was executed with “root” privileges. This allowed 
a PLCnext Technology App to extend its privileges.
Bind
– CVE-2024-12705
Crun
– CVE-2025-24965
Curl
– CVE-2025-0665 
– CVE-2025-0167 
– CVE-2024-11053
– CVE-2024-9681
Coreutils
– CVE-2024-0684
Glib
– CVE-2024-52533
Kernel
– CVE-2020-16120
Libpcap
– CVE-2023-7256 
– CVE-2024-8006
Libexpat
– CVE-2024-8176 
– CVE-2024-50602
Libmodbus
– CVE-2024-10918
Libtasn1
– CVE-2024-12133
Libxml2
– CVE-2025-27113
– CVE-2024-25062
Nano
– CVE-2024-5742
Openssh
– CVE-2025-26466 
– CVE-2025-26465
Openssl
– CVE-2024-6119
– CVE-2024-9143 
– CVE-2024-5535
OpenVPN
– CVE-2024-28882 
– CVE-2024-5594
Patch
– CVE-2019-20633 
– CVE-2019-13638
– CVE-2019-13636 
– CVE-2018-1000156
– CVE-2018-20969
– CVE-2018-6951 
– CVE-2018-6952
Podman
– CVE-2024-9341
Python
– CVE-2023-27043 
– CVE-2024-9287 
– CVE-2024-6232
– CVE-2024-6345

<!-- page 16 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 16 / 101
Rsync
– CVE-2024-12084 
– CVE-2024-12085
– CVE-2024-12086 
– CVE-2024-12087
– CVE-2024-12088
– CVE-2024-12747
System
– In addition to the standard file attributes, ACL (Access 
Control Lists) are implemented into the file system. 
ACL enable a more specific set of permissions to a file 
or directory.
– The user “plcnext_firmware” or “admin” could create 
ACF settings files in an unintended location that was 
evaluated during startup.
– An attacker who has local access to the system with 
the unprivileged user “plcnext_firmware” could gain 
root privileges by manipulating the network configura-
tion.
– With the call “sudo date -f file_name” it was possible 
to read any file without permission.
– An attacker who has local access to the system with 
the unprivileged user “admin” or “plcnext_firmware” 
could manipulate any software libraries on the sys-
tem. This allowed them to gain “root” privileges.
– An attacker who has local access to the system with 
the unprivileged user “admin” was able to replace the 
“CNI” plugins for the “Podman” container environ-
ment with malicious scripts. In this way, he was able 
to gain “root” privileges.
– Some “bash” scripts that are allowed to be executed 
by users of the “plcnext” group or the “plcnext_firm-
ware” user were vulnerable to the injection of unsafe 
environment variables.
– The “admin” user was able to edit files in the “/etc/
plcnext/” folder using the “sed -i” command.
– All users had “read/write” access in “/dev/shm”. 
Shared memory should usually be only read/writeable 
by the group or user that created the memory. This 
was corrected.
– When the “Security Profile” was activated, the 
“Notification Manager” incorrectly displayed 
PROFINET entries, although PROFINET was deacti-
vated. 
Unzip
– CVE-2022-0530 
– CVE-2022-0529 
– CVE-2021-4217 
– CVE-2018-1000035 
– CVE-2018-18384 
– CVE-2016-9844 
– CVE-2019-13232 
– CVE-2015-7696 
– CVE-2015-7697
WBM
– Certain “cipher suites” that are no longer considered 
secure have been deactivated.
– In the “Cockpit” view, the connection was lost if it was 
also opened in another browser tab.
– It was possible to open an “Alert” window via script 
using the name of a “TrustStore”.
– The “nginx” logging could under certain circumstanc-
es lead to flooding of the log files “auth.log”, “syslog”, 
“error” and “nginx/error.log”.
– The cache-control and pragma HTTP header had not 
been set properly or are missing allowing the browser 
and proxies to cache content.
Wget
– CVE-2024-38428
– CVE-2024-10524

<!-- page 17 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 17 / 101
7 Changes in firmware version 
2024.6.1
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.6 or new-
er.
Select the latest template for firmware version 
2024.6 in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2024.6.0 and firmware version 2024.6.1.
All parts of the previously released version are included in 
the current version.
7.1 Error corrections
ANSI C
The ANSI C function “getBufferPtrByPortname()” created 
unnecessary copies of the buffer. As a consequence buf-
fers returned by a previous call to this function (to get the 
buffer of a different port) were not updated to the fieldbus. 
OPC UA client
– The following known issue has been fixed: 
The OPC UA client feature relies on changes in the 
source data to trigger the transfer of data between the 
client and the server. If the source data does not 
change for any period of time, then there is no guaran-
tee that the data values will be synchronized between 
the client and the server, for example after an inter-
ruption in the client-server connection.
– The CPU load has been reduced compared to firm-
ware version 2024.6.0. The CPU load was caused by 
variables that the OPC UA client reads from a remote 
server and writes to a local variable.
PLCnext Technology Apps
The PLCnext Technology App “CODESYS Control for 
PLCnext SL” could not access Axioline I/O with firmware 
version 2024.6.0. 
PROFINET
– If the PLC has established a connection to another 
PROFINET device and this device is renamed (for ex-
ample using “Netnames+”), then the connection is 
lost. This is indicated both via the WBM page “Profinet 
diagnostics” and via the system variable 
“*PN_AR_VALID” (generated by 
PLCnext Engineer). With firmware version 2024.6.0, 
this was not indicated via the system variable (al-
though the WBM indicated the lost connection). 
– If a PROFINET communication was configured with a 
polling rate of 1ms, there could be a delay in the input 
data in rare cases. The delay could be up to another 
1 ms. This behavior occurred with firmware version 
2024.6.0.
System watchdog
Sporadically a system watchdog could occur. A possible 
cause of these watchdogs could be found in the connector 
to the PLCnext Store, especially when the PLC was not 
connected to the store. The system watchdog was pre-
ceded by a SIGSEGV.
7.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 18 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 18 / 101
8 Changes in firmware version 
2024.6.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.6 or new-
er.
Select the latest template for firmware version 
2024.6 in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2024.0.6 LTS and firmware version 2024.6.0.
All parts of the previously released version are included in 
the current version.
8.1 New functions
Configurable alarms
When configurable alarms (as defined in 
PLCnext Engineer) are confirmed or acknowledged via 
REST API a comment can be specified optionally. The 
alarm stores the latest comment. Specifying no comment 
keeps the previous comment, specifying an empty com-
ment removes the previous comment.
Modbus TCP client
In combination with PLCnext Engineer 2024.6 (or newer) 
the firmware supports an Modbus TCP client. This client 
can be configured using PLCnext Engineer.
As factory default setting, the feature Modbus TCP client is 
deactivated. If necessary it can be activated via the WBM 
page “System Services”.
OPC UA
The OPC UA client delivers diagnostic information. This in-
formation can be retrieved from the OPC UA server: 
For each client connection there is one node (with child 
nodes) under Root.Objects.DeviceSet.<PLC-type>.eUA-
Client.Connections, where <PLC-type> is the type name of 
the PLCnext Control device (e.g. “AXC F 2152” or 
”RFC 4072S”). These nodes belong to the newly intro-
duced namespace “urn:<node-name>:PhoenixCon-
tact:eUAServer/eUAClient/” where <node-name> is the 
name configured for the OPC UA server.
8.2 Changes
OPC UA client
The performance of subscription (retrieving values from a 
remote OPC UA server) has been improved.
OPC UA server
The namespace “urn:<node-name>:PhoenixContact:eUA-
Server/eUAClient/” where <node-name> is the name con-
figured for the OPC UA server has been introduced with 
firmware 2024.6 and is only present if the OPCUA client is 
activated (WBM page “System Services”). This namespace 
uses index 2 (index 3 if OPC UA PubSub is activated addi-
tionally) at the “NamespaceArray” of the OPC UA server 
and all following namespaces are shifted by one index (if 
OPC UA client is activated).
PROFINET
– In case of factory defaults behavior the PROFINET 
names of the PLC have been changed. In the past the 
name “pnc” indicated PROFINET controller and “pnd” 
indicated PROFINET device function. As this is ambig-
uous for ETH adapters which support both functions 
now the name of the ETH adapter became part of the 
PROFINET name. The names have been changed: 
– LAN1: From “axcf2152-pnd” to “axcf2152-lan1”
– EXTLAN (AXC F XT ETH 1 TX): From “axcf2152-
pnc” to “axcf2152-extlan1”
– The PROFINET controller stack had to be adapted to 
the increased requirements of the PROFINET certifi-
cation test, resulting in an increased CPU load in 
ESM 1. In exceptional cases, this can lead to a task 
watchdog in PLC projects with many PROFINET con-
nections and tightly set ESM task watchdog times.
8.3 Error corrections
Axioline
The following error occurred in combination with a con-
nected Axioline bus that contained a power module (e.g. 
“AXL F PWR 1H”) and right-hand-side an AxiolineSE mod-
ule carrier with at least one empty slot. If in this case the 
bus power was lost, the Axioline bus was not set to opera-
tion entirely after power return. 
Configurable alarms
When a “ConfirmAlarm” or “AcknowledgeAlarm” was pro-
cessed and Authentication was used by the project, the

<!-- page 19 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 19 / 101
alarm server was not setting the user field to the user 
name of the currently logged in user if the call succeeds.
HMI
When a configurable alarm (configured in 
PLCnext Engineer) was confirmed or acknowledged, this 
state could be seen in the HMI. If in this situation the 
browser has been refreshed (F5) or a new HMI session 
was started, the information about which user (IP address) 
confirmed/acknowledged was lost. This information is 
now available.
Network
If the PROFINET controller or the PROFINET device was 
deactivated via the system management for the purpose 
of IP address assignment via DHCP for the corresponding 
interface, the system crashed when the firmware was re-
started.
OPC UA client
– The OPC UA client did not handle its subscriptions cor-
rectly when the OPC UA server was shut down (e.g. 
due to a “Write and start project” command in 
PLCnext Engineer). Therefore, the firmware was ter-
minated due to a segmentation violation (SIGSEGV) or 
the configured local variables were no longer updated. 
Both effects occurred sporadically.
– The OPC UA client did not check whether certain write 
operations were successful. After a connection 
loss this sometimes led to longer periods of time in 
which the values of the variables in the OPC UA client 
did not match the values in the OPC UA server, even if 
the connection had been re-established for some 
time.
OPC UA server
During data access via OPC UA and the simultaneous exe-
cution of a PLC state transition, an unexpected exception 
could occur sporadically. The OPC UA server is now syn-
chronized against these PLC state transitions.
Proficloud
When remanent buffering was activated after the connec-
tion to the Proficloud was interrupted, the PLC prevented 
Proficloud from reestablishing the connection. Addition-
ally, if in this situation the WBM page “ProficloudServices” 
was opened, the WBM got blocked and a new connection 
to the WBM could not be established. To recover from ei-
ther of both problems the PLC needed to be restarted.
PROFINET
– Sporadically, an “AR Device deactivated” was sent by 
the PROFINET controller during a PLC project change.
– In the case that a module is configured on a 
PROFINET device whose submodules are configured 
in different APIs and alarms were received by the 
PROFINET controller for one or more of these sub-
modules, the diagnostic processing in the WBM en-
tered an endless loop, which led to the high CPU load 
by a WBM task. This effect has been observed with 
PROFINET devices which are connected via 
VXLAN tunnel to the PROFINET controller.
PROFINET device
– If the PROFINET device was requested to reset its set-
tings to factory defaults via DCP (e.g. using 
“NetNames+”), a connection to the PROFINET device 
was not possible. A reboot was necessary.
– PROFINET System Redundancy: When the primary 
PROFINET controller has already established an AR to 
the built-in PROFINET device of the PLCnext Control 
device and now the backup PROFINET controller es-
tablished its AR, an unnecessary alarm has been sent 
to the primary controller indicating return of submod-
ule.
SPLC
When using an “AXC F XT SPLC 1000” or 
“AXC F XT SPLC 3000” left-alignable safety-oriented ex-
tension module and the CPU load of the PLC was high, it 
could happen sporadically that running PROFINET con-
nections could not be kept stable.
8.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
8.5 Security updates
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt

<!-- page 20 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 20 / 101
Git
– CVE-2024-32002
OpenSSH
– CVE-2024-6387 
– CVE-2024-39894
OpenSSL
– CVE-2023-5678 
– CVE-2024-0727 
– CVE-2024-2511 
– CVE-2024-4741 
– CVE-2024-4603
LibSSH2
– CVE-2023-48795
Network
– A weakness in network robustness in case of a DoS at-
tack has been fixed.
– A system watchdog in combination with TCP network 
load on two interfaces simultaneously with active 
NetloadLimiter has been fixed.

<!-- page 21 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 21 / 101
9 Changes in firmware version 
2024.0.9 LTS
This section describes changes made between firmware 
version 2024.0.8 LTS and firmware version 2024.0.9 LTS.
All parts of the previously released version are included in 
the current version.
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.0 LTS or 
newer.
Select the latest template for firmware version 
2024.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used. 
Please contact the Competence Center Services as 
to the details on safety firmware update procedure:
Phone: +49 5281 946 2777
E-mail: safety-service@phoenixcontact.com
AXC F XT SPLC 1000: 
AXC F XT SPLC 3000: 
9.1 Error corrections
DataLogger
The “IDataLoggerService2” “ReadVariablesData” method 
returned unexpected results like records for the NULL en-
tries in the database, but these only contained the 
“consistency” flag and the record type and no value.
Network
Under high network load the built-in Ethernet interface of 
the affected PLC types sometimes can reach a blocking 
state. In this state only a power reset can re-enable the in-
terface communication. To avoid this the 
PLCnext Technology network driver has a mechanism im-
plemented to detect such situations and to react with a 
reset of the specific interface. By default behavior of the 
Linux network stack a predefined default gateway config-
uration got lost during this reset. This “Known Issue” has 
been fixed.
RSC
 It was not possible to use a string length of greater than 
4096 bytes in the data type “RscString<int N>” of RSC ser-
vices.
Safety
AXC F 2152 with AXC F XT SPLC 1000 or 
AXC F XT SPLC 3000
The following known issue has been fixed:
If the “Download Changes” mechanism (“Write and Start 
Project Changes” in PLCnext Engineer) is used along with 
the SPLC 1000/3000, please take into account a possible 
malfunction in case the following steps have been per-
formed:
1 A safety-related project is downloaded to the safety-
related controller.  
2 A non-safety-related project is downloaded to the 
standard controller.  
3 A modified safety-related project is downloaded to 
the safety-related controller.  
4 An attempt is made to change the non-safety-related 
project using “Download Changes” (“Write and Start 
Project Changes” in PLCnext Engineer), which is re-
jected by the PLCnext firmware of the standard con-
troller (for example, by changing the task 
configuration).  
5 The device is restarted. (for example, voltage failure 
and recovery or request for restart in 
PLCnext Engineer)  
Attention: After the restart, the safety-related controller 
executes the original safety-related project from step 1. In 
order to prevent the described behavior, please addition-
ally carry out the following measures after every change of 
the safety project: 
– Perform a restart in the PLCnext Engineer software in 
the “Cockpit” editor of the standard controller or 
switch off the supply voltage of the device for at least 
30 s and then switch it on again (power reset).
– Compare the CRC checksum of the safety-related 
project using the system variables of the safety-relat-
ed controller or in the ”Cockpit Safe PLC” in the 
PLCnext Engineer software with the original CRC 
checksum before the restart.
TLS FB
– A high CPU load that was associated to the use of the 
“TLS_2” function blocks has been detected in the pre-
vious firmware version.
01.01.0000 ✓
02.10.0007 ✓
02.10.0006 ✓

<!-- page 22 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 22 / 101
– The TLS_*_2 FB could not detect some passive socket 
closed when “a cable got pulled”. The TLS_*_2 FB 
continued to show an active connection for quite 
some time, way beyond the PLC's KeepAlive settings. 
In combination with PLCnext Engineer version 
2024.0.4 LTS or newer this issue has been solved.
Note: This issue was erroneously reported as fixed 
with firmware 2024.0.6 LTS. Now it has definitely 
been fixed.
WBM
The role “UserManager” did not have the permission for 
the LDAP configuration in the WBM as described in the 
documentation.
9.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
9.3 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Bash
PxC PSIRT Report: Some bash scripts that are allowed to 
be executed by users in the “plcnext” group or the 
“plcnext_firmware” user were vulnerable to unsafe envi-
ronment variable injection.
Security profile
– Correction of parameter “AllowTcpForwarding” of ssh 
configuration in security profile from “yes” to “no”.
– The sshd_config for the security profile missed the in-
clude mechanism from default configuration.
Curl
– CVE-2024-9681 
– CVE-2024-11053 
– CVE-2025-0167
FastCGI
– CVE-2025-23016
Glib
– CVE-2024-52533
Libxml2
– CVE-2025-27113
Libexpat
– CVE-2024-50602
Openssh
– CVE-2025-26465
– CVE-2025-26466
Openssl
– CVE-2024-9143
Openvpn
– CVE-2024-5594
Vim
– CVE-2024-41957
– CVE-2024-41965

<!-- page 23 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 23 / 101
10 Changes in firmware version 
2024.0.8 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.0 LTS or 
newer.
Select the latest template for firmware version 
2024.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2024.0.6 LTS and firmware version 2024.0.8 LTS.
All parts of the previously released version are included in 
the current version.
10.1 Error corrections
ANSI C
The ANSI C function “getBufferPtrByPortname()” created 
unnecessary copies of the buffer. As a consequence buf-
fers returned by a previous call to this function (to get the 
buffer of a different port) were not updated to the fieldbus. 
This bug has been fixed.
System watchdog
Sporadically a system watchdog could occur. A possible 
cause of these watchdogs could be found in the connector 
to the PLCnext Store, especially when the PLC was not 
connected to the store. The system watchdog was pre-
ceded by a SIGSEGV.
10.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
10.3 Security updates
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Nano
– CVE-2024-5742
OpenSSL
– CVE-2024-5535
– CVE-2024-6119
Python
– CVE-2024-6232 
– CVE-2024-7592
SSH
A DoS (Deny of Service) attack using LOIC (Low Orbital Ion 
Canon) at port 22 resulted in high RAM usage.

<!-- page 24 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 24 / 101
11 Changes in firmware version 
2024.0.6 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.0 LTS or 
newer.
Select the latest template for firmware version 
2024.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2024.0.5 LTS and firmware version 2024.0.6 LTS.
All parts of the previously released version are included in 
the current version.
11.1 New functions
SDK
The (previously internal) class 
“Arp::System::Commons::Threading::ConditionVariable” 
has been made available in the SDK. This class can be used 
to synchronize between multiple threads. The class 
“std::condition_variable” should not be used for synchro-
nization.
11.2 Error corrections
PLCnext Apps 
The PLCnext App “CODESYS Control for PLCnext SL” could 
not access Axioline I/O with firmware versions 2024.0.0 to 
2024.0.5. This bug has been fixed.
PROFINET
In the case that a module is configured on a PROFINET de-
vice whose submodules are configured in different APIs 
and alarms were received by the PROFINET controller for 
one or more of these submodules, the diagnostic process-
ing in the WBM entered an endless loop, which led to the 
high CPU load by a WBM task. This effect has been ob-
served with PROFINET devices which are connected via 
VXLAN tunnel to the PROFINET controller.
TLS2 FB
– After adding an instance of the function block 
TLS_SOCKET_2 to the project via Download Changes 
(“Write and Start Project Changes” in 
PLCnext Engineer) the PLC stops with a “Arp::Sys-
tem::Commons::Plc::NullReferenceException”. This 
problem occurs with PLCnext Engineer version 
2024.0.3 LTS. In combination with PLCnext Engineer 
version 2024.0.4 LTS or newer this issue has been 
solved.
– The TLS_*_2 FB could not detect some passive socket 
closed when “a cable got pulled”. The TLS_*_2 FB con-
tinued to show an active connection for quite some 
time, way beyond what the KeepAlive settings on the 
PLC. In combination with PLCnext Engineer version 
2024.0.4 LTS or newer this issue has been solved.
Note: This error was originally classified as fixed, 
but continued to occur. It was finally fixed with 
firmware versions 2025.0 and 2024.0.9 LTS.
– There has been a notable increase in CPU load when 
TLS_*_2 FB instances with PLCnext Engineer version 
2024.0.3 LTS are active. In combination with 
PLCnext Engineer version 2024.0.4 LTS or newer this 
issue has been solved.
– The error code “0xC204” (“The datagram is too long") 
could sporadically occur on the TLS_SEND_2 function 
block, although there was no length overrun in the ap-
plication. In combination with PLCnext Engineer ver-
sion 2024.0.4 LTS or newer this issue has been 
solved.
OPC UA client
When the OPC UA client configuration is loaded and 
“ns=0” is specified in the identifier of <LocalVariable> el-
ement or in the <NodeId> element of the <RemoteVari-
ableDescriptor>, a SIGSEGV (segmentation fault) could 
occur which led to a system watchdog.
OPC UA server
– Very sporadically a SIGSEGV (segmentation fault) 
could occur which led to a system watchdog. The 
SIGSEGV could occur when a a new PLC project was 
downloaded while a connected OPC UA client per-
formed a longer operation, e.g. writing a large array.
– With a large number of OPC UA variables, sporadically 
an unexpected segmentation fault could occur after 
some time of apparently normal operation.

<!-- page 25 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 25 / 101
11.3 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
11.4 Security updates
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Git
– CVE-2024-32002
OpenSSH
– CVE-2024-6387 
– CVE-2024-39894
OpenSSL
– CVE-2024-4603 
– CVE-2024-2511 
– CVE-2024-4741
SD card
With firmware versions from 2024.0.0 LTS to 
2024.0.5 LTS the notification 
“Security.Arp.Device.Interface.SdCardStatusSet” was not 
emitted when the support of the external SD card was ac-
tivated or deactivated on the WBM page “SD Card”.

<!-- page 26 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 26 / 101
12 Changes in firmware version 
2024.0.5 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.0 LTS or 
newer.
Select the latest template for firmware version 
2024.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2024.0.0 LTS and firmware version 2024.0.5 LTS.
All parts of the previously released version are included in 
the current version.
12.1 Changes
WBM
The WBM page “Security - SD Card” cannot be accessed 
and operated by the user role “Engineer”. It turned out 
that it is sufficient when roles “Admin” and 
“SecurityAdmin” can access and operate this WBM page.
12.2 Error corrections
ANSI C
Writing process data to a fieldbus via the “ANSI C” API did 
not work. This known issue has been fixed.
Alarms
A memory leak has been fixed in the alarm server. This 
leak could occur when alarms were viewed in the eHMI 
and the browser was closed abruptly (without deleting the 
created alarm subscription).
HMI
When retrieving variable values via the POST method of 
the REST API a memory leak may occur. To avoid this 
problem register and read the variables as a group or 
use the GET method of the REST API instead. 
This known issue has been fixed.
Network
In combination with AXC F XT ETH 1TX:
When DHCP was enabled for an ETH port and there was no 
link when the PLC booted, the PLC did not send any DHCP 
requests. This has not been observed for ETH ports with an 
integrated switch. 
Note: DHCP is only possible for ETH adapters without acti-
vated PROFINET function.
OPC UA client
If the OPC UA client was connected to another OPC UA 
server and this server was restarted, the OPC UA client did 
no longer update its monitored items. 
OPC UA server
Very sporadically a SIGSEGV (segmentation fault) could 
occur which led to a system watchdog. The stack trace in 
the Output.log file indicated that one or more methods of 
the class “Arp::Services::OpcUAServer::Internal::Infor-
mationModel::Common::SampleGroup” was involved. In 
many cases this error occurred when variables have been 
removed from or added to the list of monitored items, 
where in parallel other clients created or freed OPC UA 
sessions. The longer the list of monitored items, the more 
likely it was that the error occurred.
This known issue has been fixed.
Safety
In combination with an AXC F XT SPLC 1000 or 
AXC F XT SPLC 3000, a safety-related process data output 
can be connected to both a safety-related variable and a 
standard variable. In this case the value of the 
safety-related variable is copied to the safety-related pro-
cess data output as well as to the standard variable. With 
firmware version 2024.0.0 LTS the value was copied to the 
safety-related process data output but not to the standard 
variable. For this firmware version the following work-
around can be used: Create an additional safety-related 
variable in the safety program and assign the value of the 
already existing safety-related variable. In 
PLCnext Engineer remove the connection to the standard 
variable and create a new connection from the added 
safety-related variable to the standard variable.
This known issue has been fixed. 
12.3 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 27 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 27 / 101
13 Changes in firmware version 
2024.0.0 LTS 
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2024.0 LTS or 
newer.
Select the latest template for firmware version 
2024.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2023.6.0 and firmware version 2024.0.0 LTS.
All parts of the previously released version are included in 
the current version.
13.1 New functions
DataLogger
The recording of variables in the context of an IDLE task 
has been improved. Instead of recording each task cycle 
the recording time stamp is used to approximate to the 
sample rate. 
GDS
Concurrent data exchange from different CPU cores has 
been optimized. In particular 2 or more ESM tasks as-
signed to different ESM (CPU core) and exchanging data 
with the same I/O buffer could block each other. In worst 
case scenarios an ESM task watchdog could occur. The 
performance optimization of the I/O buffer minimizes the 
risk of an ESM task watchdog.
IEC 61131
Download Changes (“Write and Start Project Changes” in 
PLCnext Engineer) while variables are forced, is now sup-
ported. In combination with firmware 2024.0 LTS (or 
newer) PLCnext Engineer 2024.0 LTS (or newer) does no 
longer reset the force state implicitly before downloading 
changes. Now the forcing state is kept if variables, which 
are currently forced, do still exist as forcible variables in 
the changed project. Otherwise the firmware rejects the 
Download Changes command and emits a notification. In 
this case the user can check the list of forced variables 
in PLCnext Engineer and unforce variables that prevent 
downloading changes.
Licenses
The PLCnext firmware is capable of using licenses, which 
are managed by a license server in the network. Currently 
this feature can only be used with the PLCnext Simulation 
products because only the license “PLCnext ENG SIM” 
can be hosted on a license server (PC). For other PLCnext 
controllers this capability is only a preparation for future 
features. The access to the license server can be config-
ured via WBM. Currently if a license server is configured, 
no licenses can be accessed which are stored at the device 
or LIC SD card.
Proficloud
The Proficloud can be configured to send the values of the 
marked variables to an MQTT server instead of the 
Proficloud. This MQTT server can be in a local network or 
in the cloud. The MQTT server to be used, can be config-
ured in the WBM.
SD card
“Reset to default settings” can be configured to set the 
(external) SD card as enabled. This can be configured at 
the WBM page “SD card”. In previous firmware versions 
“reset to default settings” did not change the enabled/dis-
abled state of the (external) SD card.  
Note: The activation of the “Security Profile” implicitly dis-
ables the (external) SD card and configures “reset to de-
fault settings” to keep the enabled/disabled state.
Security
A LIC SD card can be encrypted to avoid unauthorized ac-
cess. Encryption can be started via WBM page “Security - 
SD Card”.
System
– If a system watchdog (SWD) occurs due to a fatal error 
that has caused a PLCnext process to die, the follow-
ing files are saved before the system is rebooted:    
– reason.log    
– kernel.log    
– sys.log 
If an LTTNG session is active, its trace is saved, too. 
These files are saved to the folder 
/opt/plcnext/watchdogDaemon/[timestamp] where 
[timestamp] is created from the time at which the SWD 
occurred. If more than 3 SWD occur, the oldest folder 
will be removed. If the PLC is rebooted due to the

<!-- page 28 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 28 / 101
hardware watchdog reset, it is not possible to save 
these files. This can happen if the hardware watchdog 
is no longer triggered by the firmware, for example 
due to a heavy, high-priority load on the system.
– In combination with firmware 2024.0 LTS (or newer), 
PLCnext Engineer (2024.0.1 LTS or newer) supports 
configurable alarms.
– Changes of PLC states are serialized and dedicated 
state transitions can be monitored with a timeout. 
This prevents from scenarios in which a low-priority 
task requests to change the PLC state (which can also 
occur implicitly, for example by calling the 
“RestartDevice()” method of 
“IDeviceControlService”) while the PLC Manager is 
performing another state transition (for example from 
“PlcState::Running to PlcState::Stop”).
WBM
The WBM page “Security - SD Card” can be accessed and 
operated by the user role “Engineer”, too. This became 
necessary by the optional encryption of the SD card.
13.2 Changes
Linux
– The OpenSSL library has been updated to version 3.0. 
The PLCnext firmware uses this version only. For com-
patibility reasons the previous OpenSSL library (ver-
sion 1.1.1) still exists in the file system. As this version 
is outdated, it will be removed in one of the next firm-
ware releases. For applications (including PLCnext 
Apps) which use the OpenSSL library, an update is 
recommended as soon as an application version is 
available, which uses OpenSSL 3.0.
– LTTng has been updated to version 2.13.9 and there 
has been a significant change in the “lttng-ust” (LTTng 
user space tracing). If an application/library is instru-
mented with LTTng user space tracing and has been 
compiled without using the “ArpTracing.cmake” sup-
port of the LTTng user space tracing in PLCnext SDK 
(available since FW 2022.6), the instrumented appli-
cation/library cannot be loaded any longer by the firm-
ware (“undefined symbol” is reported in 
Output.log). In that case the instrumentation of LTTng 
user space tracepoint in the application/library has to 
be changed to use the “ArpTracing.cmake” support of 
the PLCnext SDK and it needs to be recompiled. 
Matlab Simulink applications, which use the 
“PLCN_EnableLTTNG” compile option, have to be 
compiled with PLCnext Target for Simulink v2.3 or 
newer.
– Library “paho-mqtt-c” has been updated to version 
1.3.13.
OPC UA
– The OPC UA client and server use the OpenSSL library 
to validate X.509 certificates using the OpenSSL 
flag X509_V_FLAG_X509_STRICT. As firmware 
2024.0 LTS is updated to OpenSSL 3.0, the X.509 cer-
tificate validation became more strict, especially for 
non self-signed certificates. This may cause the server 
to return the error “BadSecurityChecksFailed” on cli-
ent connection attempts. Make sure that, according to 
OPC UA Part 6, client issuer as well as client applica-
tion X.509 certificates are conform to RFC 5280, es-
pecially to the sections listed below. This applies to 
self-signed certificates as well as user-managed cer-
tificates.
– 4.1.1.2 signatureAlgorithm
– 4.1.2.6 Subject
– 4.2.1.1 Authority Key Identifier
– 4.2.1.2 Subject Key Identifier
– 4.2.1.3 Key Usage
– 4.2.1.6 Subject Alternative Name
– 4.2.1.9 Basic Constraints
– In the NamespaceArray of the OPC UA server the in-
dex of namespace http://phoenixcontact.com/Opc-
Ua/PubSubConfiguration has changed from index 8 to 
index 2. This namespace is optional and it appears 
only if the feature “OPC UA PubSub” is activated on 
the WBM page “System Services”. Currently the firm-
ware does not provide anything in that namespace, it 
is only a preparation for future extensions.
13.3 Error corrections
Axioline
Some Axioline modules (for example analog outputs) pro-
vide status information in their process data. In case of a 
module error (for example loss of power supply) these 
process data inputs are filled with an error code. However, 
in certain situations these process data inputs returned 
“0” instead of the error code. This error has been cor-
rected. Only process data inputs of modules connected to 
the controller's local bus have been affected.  Not affected 
are retrieving module errors via PDI request as well as dis-
playing these errors at the WBM page “Diagnostics - Local 
Bus”.

<!-- page 29 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 29 / 101
ESM
– If two ESM tasks cause a task watchdog at (nearly) the 
same time, the event task “Arp.Plc.Esm.OnException” 
was executed twice. Additionally, the PLC was at-
tempted to be stopped twice in parallel. This failed 
and the PLC had to be rebooted. This error has been 
corrected and the event task as well as the PLC stop is 
now executed only once.
– In some situations calling the function block “GET_-
EXCEPTION_INFOS” in the event task 
“Arp.Plc.Esm.OnException” caused an exception. 
This has been fixed. In additon to update to firmware 
2024.0 LTS or newer, the PLC project has also to be 
re-compiled using PLCnext Engineer 2024.0.1 LTS or 
newer.
– In combination with PLC IDLE task and Axioline con-
figured to use that IDLE task as “Trigger Task”, the 
PLC project stops after some time due to a task watch-
dog. After that the PLC had to be rebooted.
EtherNet/IP
Sporadically the activated “EtherNet/IP” component 
could block a PLC state change after project download.
GDS
It was possible to force a variable with a value of an inap-
propriate data type.
IEC 61131
– When breakpoints are set in the IEC 61131-3 pro-
gram, the “PlcState::Debugging” flag was reset in the 
transition from “PLC STOP” to “PLC HOT START” and 
then set again when changing from “PLC Running” to 
“Debugging”. The fieldbus output values could be 
switched on again for a short time period when the 
PLC was in the state “Running”.
– “Download Changes” (“Write and Start Project Chang-
es” in PLCnext Engineer) implicitly creates a backup 
of the current project. If “Download Changes” is not 
possible (for any reason), the current project is re-
stored from this backup. If “Download All” (“Write and 
Start Project” in PLCnext Engineer) is performed im-
mediately after a rejected or failed “Download Chang-
es” attempt, the PLC is reset. Resetting conflicted 
with restoring and ended in an I/O exception. The 
firmware now keeps the state flag “Running | DcgNot-
Possible” until the restoring process has been fin-
ished. Depending on the project size, the restoring 
process may take several seconds. Note 
that PLCnext Engineer 2023.9 (or newer) checks this 
state before it offers the “Download All” option.
– In case of large projects and an extensive use of cer-
tain firmware function blocks, an exception could oc-
cur after a “Download Changes” attempt (“Write and 
Start Project Changes” in PLCnext Engineer). The fol-
lowing is reported in the Output.log: “SetupPlc(chang-
ing) with out of memory error - GC heap of the 
application domain”. The firmware function blocks 
have been updated in PLCnext Engineer version 
2023.0.6 LTS and in 2024.0 LTS (or newer).
– An exception after “Download Changes” (“Write and 
Start Project Changes” in PLCnext Engineer) has been 
triggered if the function block “AR_STATISTIC_ITER-
ATE” was enabled and generated new values. To fix 
this bug, re-compile and download the project using 
PLCnext Engineer 2024.0 LTS (or newer).
– In the function “MOVE” that is used with the function 
“EN/ENO”, a value of a multi-element-variable was 
assigned to a wrong address. To fix this bug, re-com-
pile and download the project using PLCnext Engineer 
2024.0 LTS (or newer).
– In a C# eCLR Library the runtime created a vectored 
exception when calling “File.Exists(null)”.
OPC UA client
The GDS client could not access PLC variables (attribute 
“LocalVariable” in XML element “eUAClientNodeMap-
ping”) if “Visibility of variables” is set to “None” in the 
OPC UA configuration of PLCnext Engineer.
OPC UA server
– A fatal exception could occur if “IndexRange” is used 
when accessing a variable that is not of type array or 
of type string.
– After the OPC UA server started with a changed proj-
ect the server might return “BadNodeIdUnknown” 
when a client tried to continue monitoring an existing 
subscription item.
– Subscriptions did not work after a warm or cold start 
with project changes.
– A sporadic fatal exception could occur in case of OPC 
UA session creation and login.
– If several elements of a string array are subscribed us-
ing “IndexRange”, a fatal error occurred and the PLC 
stopped.

<!-- page 30 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 30 / 101
PROFINET
– If a “write record” could not be processed immediate-
ly by the PROFINET stack, it was buffered. When a 
new transmission attempt was made, it was then in-
correctly sent as a “read record” packet.
– The RSC service 
“IAcyclicCommunicationService::RecordWrite()” has 
a timeout in which the profinet device has to re-
spond. In some cases this timeout was too short and 
has been increased to 15s. The IEC function block 
“WRREC” internally uses this service, too.
– A PROFINET device with a device access point (DAP) 
starting at “Slot 1” could not be accessed via the 
“AR_MGT” function block.
– An inconsistent “SF-LED” state could occur at the 
PROFINET controller, if in case of an activated net-
work port monitoring of a connected PROFINET 
switch the controller was plugged to another port 
during runtime and then plugged back to the original 
port.
– The PROFINET controller sent a “Write Request” with 
wrong lengths calculated in the “NDR header” when 
establishing the connection. This led to a 
“Write Response” error for PROFINET stations with 
very large parameter records (for example “PN/PB 
Gateway”).
– After PROFINET alarms of a certain severity occurred, 
these were not reset again for going alarms and re-
mained in the diagnostic memory. As a result they 
were displayed incorrectly in the WBM and it could 
also happen that the “SF-LED” remained active.
Proficloud
– A fatal exception occurred if the Proficloud compo-
nent with “Remanent Buffering” was enabled and the 
DataLogger component was manually disabled on the 
WBM page “System Services”.
– If a Proficloud TSD connection was lost, the logging 
was flooded with an unnecessary number of messag-
es.
– If a Proficloud connection was disconnected, the con-
nection could not be deactivated in the WBM.
– When a physical connection to the Proficloud was in-
terrupted for several hours and re-established after-
wards, the component could not reconnect 
automatically to the Proficloud.
SPLC
In case of  a synchronization error in combination with the 
SPLC hardware, numerous synchronization timers could 
sporadically be created. This could result in a PLC task 
watchdog.
System
– After starting the PLCnext Engineer logic analysis, 
which contained an element of an array of struct, a 
system watchdog could occur sporadically.
– A system watchdog with reboot could occur while 
reading software information of a 
PLCnext Engineer project. This issue could occur if the 
manifest file in the PCWE directory is deleted after the 
“File::Exists” call but before the file is accessed by 
other operations. This could be the case during a 
“Download Changes” process (“Write and Start Proj-
ect Changes” in PLCnext Engineer).
– Sometimes an OPC UA client did not receive the last 
“UpdateStatus” message after a successful installa-
tion of a firmware update. The last message informs 
about the reboot of the device (100 %) but the client 
only saw the “copy rootfs” message (90 %).
– If the controller was in the standard PLC status 
“ready/blocked” after a system watchdog, a “FATAL - 
Exception” was triggered if the “General Data (SPLC)” 
page of the SPLC was opened in the WBM.
WBM
– The “User Partition” value that was displayed on the 
WBM page “Cockpit” did not match the value of the 
global IEC 61131 system variable 
“USER_PARTITION.MEM_USAGE”.
– The memory partition was displayed in the WBM in 
“MiB” but shown with the unit “MB”. Now it is calcu-
lated as MB.
13.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 31 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 31 / 101
13.5 Security updates
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Curl
– CVE-2023-38039
– CVE-2023-46219
– CVE-2023-46218
– CVE-2023-38545
– CVE-2023-38546
DBus
– CVE-2023-34969 
– CVE-2022-42010
– CVE-2022-42011 
– CVE-2022-42012
File
– CVE-2022-48554
GDS
Security notifications for write access were not deacti-
vated if a new PLC project was loaded without activation.
GLib
– CVE-2023-29499 
– CVE-2023-32636 
– CVE-2023-32643 
– CVE-2023-32611 
– CVE-2023-32665
Glibc
– CVE-2023-5156 
– CVE-2023-4911 
GnuTLS
– CVE-2024-0553 
– CVE-2024-0567
GRPC
– CVE-2023-33953 
– CVE-2023-32731 
– CVE-2023-32732 
– CVE-2023-4785 
– CVE-2023-44487
Libcap
– CVE-2023-2603
Libssh
– CVE-2023-6004
Network
With firmware version 2023.0.7 LTS and 2023.6, booting 
with an active security profile and the network link 
“AXC F XT ETH 1TX” plugged in at the same time was not 
possible.
NTP
– CVE-2023-26551 
– CVE-2023-26552 
– CVE-2023-26553 
– CVE-2023-26554 
– CVE-2023-26555
– Any content could be injected into the NTP configura-
tion file via the WBM configuration of the NTP service 
if a line break was inserted in the comment field.
NVT
– CVE-2022-29900 
– CVE-2022-29901
OPC UA
The manual firmware update procedure via an OPC UA 
server did not work as documented.
OpenSSH
– CVE-2023-48795 
– CVE-2023-51384 
– CVE-2023-51385
OpenSSL
– CVE-2023-5363 
– CVE-2023-4807 
– CVE-2023-3817

<!-- page 32 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 32 / 101
Perl
– CVE-2023-47100
Python
– CVE-2022-40897
– CVE-2023-40217
Procps
– CVE-2023-4016
SQLite
– CVE-2023-7104
SqashFS
– CVE-2021-41072
Sudo
– CVE-2023-42465
Tcpdump
With the call “sudo tcpdump” it was possible to read the 
contents of files without read rights.
UM
The “User Manager” accepted a newly created PLCnext 
user with the name “plcnext_firmware”. The “UID” and 
the access rights were identical with the internal user “plc-
next_firmware”. 
Vim
– CVE-2023-5441 
– CVE-2023-5344 
– CVE-2023-5535
– CVE-2023-4781 
– CVE-2023-4734 
– CVE-2023-4733 
– CVE-2023-4736 
– CVE-2023-4735 
– CVE-2023-4750 
– CVE-2023-4738 
– CVE-2023-4752 
– CVE-2023-4751
– CVE-2023-48231 
– CVE-2023-48237 
– CVE-2023-48706
– CVE-2023-46246
Zlib
– CVE-2023-45853

<!-- page 33 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 33 / 101
14 Changes in firmware version 
2023.6.1
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2023.6 or new-
er.
Select the latest template for firmware version 
2023.6 in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2023.6.0 and firmware version 2023.6.1.
All parts of the previously released version are included in 
the current version.
14.1 Error corrections
C++ API
– The class “TlsSocket2” now reloads the Trust Store 
(including Certificate Revocation List) before a new 
handshake (renegotiation). This is required for the 
IEC 62351-3 certification.
– Developers that used the external/customer SDK ver-
sion 2023.x LTS were unable to use the 
“PImpl pattern” due to the missing file 
“Arp/System/Core/PimplPtr.inl”. 
14.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 34 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 34 / 101
15 Changes in firmware version 
2023.6.0 
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2023.6 or new-
er.
Select the latest template for firmware version 
2023.6 in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
If you use a left-alignable functional safety exten-
sion module with your controller, the following safe-
ty-related firmware versions must be used:
– AXC F XT SPLC 1000: 01.01.0000
– AXC F XT SPLC 3000: 02.10.0006
This section describes changes made between firmware 
version 2023.0.0 LTS and firmware version 2023.6.0.
All parts of the previously released version are included in 
the current version.
15.1 New functions
C++ API
The new class TlsSocket2 was implemented. As a further 
development of  the class TlsSocket, this new class offers 
additional methods to support security requirements of 
IEC 62351-3.
IEC 61131-3
– The IEC 61131-3 non-standard function 
“GET_MICROSECONDS” is supported. To use this fea-
ture PLCnext Engineer 2023.6 (or newer) with a proj-
ect template for this firmware or newer is required.
– The IEC 61131-3 non-standard function block 
“NETLOAD_LIMITER_STATISTIC” supports the ac-
cess to the statistics of the netload limiter. To use this 
feature PLCnext Engineer 2023.6 (or newer) with a 
project template for this firmware or newer is re-
quired.
– Namespaces in IEC 61131-3 POUs are supported. To 
use this feature PLCnext Engineer 2023.6 (or newer) 
with a project template for firmware 2023.6 or newer 
is required.
INTERBUS
Notifications for a basic diagnosis of INTERBUS in combi-
nation with “AXC F XT IB” or “AXC F IL ADAPT” were 
added.
Linux
– CURL supports TFTP protocol (TFTP client)
– Podman was updated to version 4.4.3. This includes 
the update of related packages and requires to shift 
the network stack to “netavark” and “aadvard-dns.”
OPC UA
– Any variable known by the GDS can be read or written 
by the OPC UA client. In previous firmware versions 
only variables indicated with the “OPC” flag could be 
used by the OPC UA client.
– A project update for standard (non-safety) 
PLCnext Engineer projects is supported according to 
“DI SU Software Update Base Server Facet” and 
“DI SU Cached Loading Server Facet”. For this pur-
pose the user roles “Admin” and “SoftwareUpdate” 
now additionally allow the update of projects (besides 
firmware updates). In PLCnext Engineer 2022.9 (and 
newer) an export of an updated application can be 
generated (“Export PLCnext Engineer Software Pack-
age”/“Export PLCnext Engineer Software Package 
(with sources)”). The exported project files can be up-
loaded to the Device and Update Management App 
and from there assigned to further devices. Note that 
an appropriate version (newer than 23.0.1) of the De-
vice and Update Management App is required.
PROFINET
PROFINET diagnostic messages, which are sent in the USI 
format (User Structure Identifier) are printed in plain text 
(in English language) as notification and are displayed as 
well on the PROFINET diagnostics WBM page. 
PLCnext Engineer collects the required interpretation 
rules from the FDCML description of the used PROFINET 
devices and plain text messages that are related to the de-
vice's USI diagnosis. Both information are sent to the PLC 
as a part of the project. Additionally, an USI diagnosis can 
be converted to a plain text message via the new RSC ser-
vice “ITextLookup2”. To use this feature 
PLCnext Engineer 2023.6 or newer with a project template 
for this firmware version is required. Furthermore the 
used FDCML files need to contain the necessary USI diag-
nosis information. Currently the FDCML files delivered

<!-- page 35 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 35 / 101
with PLCnext Engineer (2023.6) installation do not contain 
this information.
SD card
When using the “AXC F XT SPLC 3000” the SD card is no 
longer mandatory.
15.2 Changes
Alarms
Alarm notifications (Arp.Services.Alarms.Log.*) are logged 
into a separate archive “alarms” (file: /opt/plcnext/proj-
ects/Default/Services/NotificationLogger/alarms.config).
Firewall
The firewall rules no. 8 (“SNMP”) and no. 9 (“PROFINET 
Uni-/Multicast Ports”) were removed from the default 
rules because PROFINET could almost not be used at all 
with an activated firewall using the default firewall rules of 
PLCnext. The rules could be misinterpreted that a 
PROFINET communication is possible even if the firewall 
is activated. 
At https://security.plcnext.help you can find information 
on how to configure the firewall to enable PROFINET com-
munication. 
IEC 61131-3
When “Download Changes” (“Write and Start Project 
Changes” in PLCnext Engineer) cannot be executed suc-
cessfully a notification is emitted. The warning 
“Arp.Plc.Domain.DownloadChanges.Refused” indicates 
that “Download Changes” could not be performed (for ex-
ample not possible in real-time operation) or is not sup-
ported due to improper preconditions (for example task 
configuration has changed). In these cases “Download 
All” (“Write and Start Project” in PLCnext Engineer) would 
work.  The error “Arp.Plc.Domain.Download-
Changes.Failed” indicates that the project is erroneous. In 
this case also “Download All” won't work. This change also 
resolves the known issue “Sporadically a 
PLCnext Engineer project may reject “Download changes” 
without giving a reason.”.
Notifications
– The names of some notifications were changed, new 
notifications were added, and some less helpful noti-
fications were removed. For more details refer to the 
notification topics at https://www.plcnext.help.
Notifications of severity “Internal” are no longer 
logged by default.
– If during power on no proper value can be read from 
the RTC clock (for example due to a long time without 
power) a notification is emitted.
SDK installer
The names of the SDK installer files were simplified. They 
consist, separated by “-” (minus), of the article name, “li-
nux-sdk” or  “mingw-sdk” and the version name. The file 
extension was not changed(.sh for Linux and .tar.gz for 
Windows/mingw). The file names of the firmware con-
tainer were adapted, too. The file name consists, sepa-
rated by “-“ (minus), of the article name, the version name 
and version number (incl. build number). The file exten-
sion .rauc was not changed.
WBM
On the PLCnext Store page, the display of the connection 
and registration status was improved, including a recon-
nect button. 
15.3 Error corrections
Axioline
After an unexpected termination of the PLCnext Runtime 
process it could happen that parameterized output substi-
tute values for the local Axioline bus were not output but 
set to zero.
C#
The C# method “System.IO.Path.Combine()” used “\” 
(backslash) instead of “/” (slash) as delimiter in paths. The 
code of this method is downloaded via PLCnext Engineer 
to the PLC. To fix this bug, the template has to be up-
dated in the PLCnext Engineer project (replace controller) 
to a PLC with firmware 2023.6 (or newer).
ESM
– A cyclic ESM task configured to trigger the Axioline 
bus did not trigger the Axioline bus. Instead the ESM 
used a calculated update interval. Now the Axioline 
bus is triggered by the configured ESM task.
– The ESM sporadically detected a task watchdog in 
combination with temporary high system load at lower 
priority and usage of IEC function blocks that internal-
ly initiate RSC services. This issue has been fixed.
GDS
The update of GDS connectors is also performed when the 
PLC is started (cold, warm, or hot restart). This ensures 
that initial values or retained values of OUT ports are for-

<!-- page 36 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 36 / 101
warded to their connected IN ports before the task of the 
IN port is executed.
IEC 61131-3 and C#
– The handling of the heap memory has been optimized. 
This includes allocation of heap (new operator as well 
as implicitly, for example by using string or other ref-
erence data types) as well as the Garbage Collector. 
These optimizations result in less time blocked by mu-
texes. Blocking by mutexes can prevent high priority 
tasks from execution and in rare cases caused an ESM 
task watchdog. These effects occurred in a very sto-
chastic manner.
– The firmware did not handle variables of array data 
types and the usage of VAR_IN_OUT correctly. When 
such variables were used in a DataLogger session or in 
the “Logic Analyzer” of PLCnext Engineer the PLC de-
tected a software watchdog (SWD). The PLC was re-
booted and a cold start had to be performed (hereby 
retentive variables were set to their initial values).
OPC UA
– The OPC UA server did not provide data when sub-
scribing to multiple matrices within a subscription. 
However, if only one matrix was subscribed, it worked. 
If a 2D matrix of type string was subscribed, the vari-
able update of a previously subscribed 2D int matrix 
froze. This condition could only be removed by resub-
scribing to the 2D int matrix. This bug (known issue) 
has been fixed.
– If a matrix for monitoring was used, various unexpect-
ed results occurred when using “IndexRange” and 
“String” as data type:  
– When initially reading out the matrix after logging 
in, a “DataChange” event with several changes 
was erroneously triggered.  
– If a “DataChange” event was performed after wri-
ting, the strings in the matrix were truncated.  
– Sporadically a “Segmentation Fault” occurred 
when reading out the matrix. 
This bug (known issue) has been fixed. 
– Using the value “0” as NamespaceIndex in the config-
uration of OPC UA client could lead to a fatal error. 
This bug (known issue) has been fixed.
– In case of a warm start of the PLC, subscriptions from 
the “clientconfig.xml” had not been loaded and creat-
ed.
– OPC  UA client: Several memory leaks in case of read 
or write subscriptions were fixed.
Proficloud
Application update via Proficloud: If there was an empty 
directory inside the ZIP archive of a software package the 
extraction failed.
PROFINET
– When starting the firmware, the PROFINET communi-
cation sporadically ran into a timeout. In combination 
with the left-alignable extension module 
“AXC F XT SPLC 1000” the Safety I/O modules 
were consequently passivated even though the 
PROFINET communication was re-established after 
the timeout.
– After resetting the PLC with attached left-alignable 
extension module “AXC F XT ETH 1TX” to factory de-
faults, both ETH adapters got the same PROFINET 
name. With firmware 2023.6 and newer “-pnc” is ap-
pended to the name of the PROFINET controller and 
“-pnd” is appended to the name of the PROFINET de-
vice. If no “AXC F XT ETH 1TX” is present, the 
PROFINET name is reset to “axcf2152-pnc”.
– When the PROFINET controller established a connec-
tion to a PROFINET device, the order of parameters 
during DCP Connect Request was changed in some 
cases with firmware 2022.6.3. This change has been 
reverted because at least one PROFINET device type 
(equipped with an old firmware) did not connect with 
this changed order.
– Due to an internal timer overflow a connection to 
some PROFINET devices could not be re-established 
after the controller operated longer than ~21 days.
– PROFINET device: A wrong answer to a PN-Read Re-
quest (Slot/Subslot/Index 0/0/0x8029) with too small 
RecordDataLength (e.g. 1024) was generated for the 
Read Response.
RSC services
The execution of the method “IDirectoryService::Create()” 
with an already existing path did not return the expected 
“FileSystemError::AlreadyExist” value.
SDK
The class “SecurityNotificationPayload” was missing in 
the SDK. The following header files were added. 
– “Arp/System/NmPayload/Security/SecurityNoti-
ficationPayload.hpp” 
– “Arp/System/NmPayload/Security/SecurityNoti-
ficationInfo.hpp”
SPLC
In combination with the left-alignable extension module 
“AXC F XT SPLC 3000” (item no. 1160157) a cycle time of

<!-- page 37 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 37 / 101
20 ms becomes effective although a “Safety PLC cycle 
time” greater than 20 ms is configured.
System
– When the NTP daemon is disabled, the hardware clock 
drifts significantly, and it is only resynchronized with 
the system clock at the start of the reboot sequence.
– The text messages of a loaded safety-relevant project 
in the notifications and “Output.log” showed incorrect 
CRC information.
– The file “/var/log/daemon.log” could become very 
large and in worst case it could cause an “out of mem-
ory” situation. This file is now considered by “logro-
tate” and therefore can no longer become that large.
– The “paho” library was updated from version 
“v1.3.10” to “v1.3.12”.  This update solves several in-
compatibilities with the IEC 61131-3 “IIoT_Li-
brary_V4.x”. In particular, it fixes a “system 
watchdog” in combination with “MQTT-Client FB” in 
case of a failed MQTT connection.
WBM
– If many PROFINET devices are used and the button to 
jump to the tree node is pressed in the “Device List” 
tab of the “Diagnostics - PROFINET” page, the “Tree 
View” tab was opened but often it was not automati-
cally scrolled to the desired device.
– In the “Device List” tab of the “Diagnostics - 
PROFINET” page the link to the device‘s web page 
was only shown if the connection to the device could 
be established during project load. Now the 
PROFINET device is regularly checked if it offers a 
web page.
– In some cases the “Diagnostics - PROFINET” page of 
the WBM displayed a wrong IP address (e.g. 
“10.10.10.1”) for the PROFINET controller.
– The display of the used and free memory of the user 
partition was optimized at the “Cockpit” page of the 
WBM.
– At the “Password Policy” tab of the WBM page “User 
Authentication” the description of the “password re-
use” settings could possibly be misinterpreted and 
has therefore been corrected. 
– The “Change Password” dialog did not handle special 
characters correctly.
15.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
15.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
Curl
– CVE-2022-43551
– CVE-2022-43552
– CVE-2023-27533
– CVE-2023-27534
– CVE-2023-28320
– CVE-2023-28321
– CVE-2023-28322
– CVE-2023-28319 
– CVE-2023-23914
– CVE-2023-23916
– CVE-2023-23915 
C-ares
– CVE-2022-4904 
– CVE-2023-32067 
– CVE-2023-31147 
– CVE-2023-31130 
– CVE-2023-31124
Freetype
– CVE-2023-2004
Firewall
It was possible to establish an SSH connection at boot 
time of the PLC before the firewall is started. This connec-
tion remained active even when the firewall is activated 
and configured to block this connection.

<!-- page 38 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 38 / 101
Git
– CVE-2023-22490 
– CVE-2023-25652 
– CVE-2023-29007
– CVE 2022-41903 
– CVE-2022-23521
Kernel
– CVE-2022-1012
Libxml2
– CVE-2022-40303 
– CVE-2016-3709 
– CVE-2023-28484 
– CVE-2023-29469
N-curses
– CVE-2023-29491
Network
In the case of an attack with a high network load, network 
communication could be permanently interrupted despite 
an activated firewall and activated Netload Limiter. This 
could only be remedied by a restart of the controller.
OpenSSL
– CVE-2023-2650 
– CVE-2023-0464 
– CVE-2023-0465 
– CVE-2023-0466
– CVE-2023-0286 
– CVE-2022-4304  
– CVE-2023-0215 
– CVE-2022-4450 
– CVE-2023-0216
Podman
– CVE-2022-2989
Python
– CVE-2022-45061 
– CVE-2023-24329
Rsync
– CVE-2022-29154
SNMP
– CVE-2022-44792 
– CVE-2022-44793
Sqlite
– CVE-2022-46908
– CVE-2022-35737
Strongswan
– CVE-2023-26463 
Sudo
– CVE-2023-22809 
– CVE-2023-27320 
– CVE-2023-28486 
– CVE-2023-28487
Syslog
– CVE-2022-38725
Tar
– CVE-2022-48303
Vim
– CVE-2022-4141 
– CVE-2022-4292 
– CVE-2023-0049 
– CVE-2023-0054 
– CVE-2023-2426 
– CVE-2023-2609 
– CVE-2023-2610

<!-- page 39 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 39 / 101
16 Changes in firmware version 
2023.0.7 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2023.0 LTS or 
newer.
Select the latest template for firmware version 
2023.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file. 
This section describes changes made between firmware 
version 2023.0.0 LTS and firmware version 2023.0.7 LTS.
All parts of the previously released version are included in 
the current version.
16.1 Error corrections
ESM
– The ESM sporadically detected a task watchdog in 
combination with temporary high system load at lower 
priority and usage of IEC function blocks that internal-
ly initiate RSC services.
– If the PLC rejected a “Download changes” command 
(“Write and Start Project Changes” executed by 
PLCnext Engineer), for example because the change 
could be performed in real time, the PLC was rebooted 
due to a system watchdog. 
Network
In case of an attack with high network load, network com-
munication could be permanently interrupted despite an 
activated firewall and activated Netload Limiter. This 
could only be remedied by a restart of the controller.
OPC UA
– OPC UA client: Several memory leaks in case of read 
or write subscriptions were fixed.
– Using the value 0 as NamespaceIndex in the configu-
ration of OPC UA client could lead to a fatal error.
Proficloud
When Proficloud was configured to cache values (WBM 
setting “Remanent Buffering Enabled”) and the connec-
tion between PLC and Proficloud was broken, the con-
sumed memory increased. If this situation continued for 
too long, this could even cause a “System Watchdog”.
PROFINET controller
– Due to an internal timer overflow a connection to 
some PROFINET devices could not be re-established 
after the controller operated longer than ~21 days.
– When the PROFINET controller established a connec-
tion to a PROFINET device, the order of parameters 
during DCP Connect Request was changed in some 
cases with firmware 2022.6.3. This change has been 
reverted because at least one PROFINET device type 
(equipped with an old firmware) did not connect with 
this changed order.
System
– The file “/var/log/daemon.log” could become very 
large and in worst case causes an out of memory situ-
ation. This file is now considered by “logrotate” and 
therefore can no longer become that large.
– Update of “paho” library from version “v1.3.10” to 
“v1.3.12”. 
This update solves several incompatibilities with the 
IEC 61131-3 “IIoT_Library_V4.01”. In particular, it 
fixes a “system watchdog” in combination 
with “MQTT-Client FB” in case of a failed MQTT con-
nection.
WBM
The “Change Password” dialog did not handle special 
characters correctly.
16.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
16.3 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt

<!-- page 40 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 40 / 101
C-ares
– CVE-2022-4904 
– CVE-2023-32067 
– CVE-2023-31147 
– CVE-2023-31130 
– CVE-2023-31124
Curl
– CVE-2022-43551 
– CVE-2023-38545 
– CVE-2023-38546
– CVE-2022-43552 
– CVE-2023-23914 
– CVE-2023-23916 
– CVE-2023-23915 
– CVE-2023-28320 
– CVE-2023-28321 
– CVE-2023-28322 
– CVE-2023-28319 
– CVE-2023-27533 
– CVE-2023-27534
Firewall
It was possible to establish an SSH connection at boot 
time of the PLC before the firewall was started. This con-
nection remained active even when the firewall was acti-
vated and configured to block this connection.
Freetype
– CVE-2023-2004
Git
– CVE 2022-41903 
– CVE-2022-23521
– CVE-2023-22490 
– CVE-2023-29007
Glibc
– CVE-2023-4813 
– CVE-2023-5156 
– CVE-2023-4911
Libxml2
– CVE-2022-40303 
– CVE-2023-28484 
– CVE-2023-29469
Ncurses
– CVE-2023-29491
OpenSSL
– CVE-2023-0286 
– CVE-2022-4304  
– CVE-2023-0215 
– CVE-2022-4450 
– CVE-2023-0216
– CVE-2023-2650
– CVE-2023-0464
– CVE-2023-0465
– CVE-2023-0466
– CVE-2023-3817
Rsync
– CVE-2022-29154
Strongswan
– CVE-2023-26463
Sqlite
– CVE-2022-46908
Syslog-NG
– CVE-2022-38725
Tar
– CVE-2022-48303
User Manager
With activated “Security Profile” the role “Engineer” erro-
neously also had the rights of the role “SafetyEngineer”.

<!-- page 41 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 41 / 101
17 Changes in firmware version 
2023.0.0 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2023.0 LTS or 
newer.
Select the latest template for firmware version 
2023.0 LTS in the PLCnext Engineer project.
In order to update to firmware version 2023.0.0LTS 
or newer at least a firmware version 2022.0 LTS or 
newer must be installed on the PLC. Older firmware 
versions will not accept the *.rauc firmware update 
file.
This section describes changes made between firmware 
version 2022.9.0 and firmware version 2023.0.0 LTS.
All parts of the previously released version and changes 
made in 2022.0.8 LTS are included in the current version.
17.1 New functions
Axioline
– Diagnostic information sent from an Axioline module 
to the Axioline master are now logged to the “Out-
put.log” file and sent as a new notification “Arp.Io.Ax-
ioline.Device.*”. Thus, the history can be inspected in 
the notification log via WBM or PLCnext Engineer. Er-
rors reported during start-up of the Axioline bus by an 
Axioline module have been logged to the “Output.log” 
file. Now these errors are logged additionally as new 
notification “Arp.Io.Axioline.Parameterization.Er-
ror”, respectively “Arp.Io.Axioline.Configuration.Er-
ror”. Such errors were difficult to find before, 
especially with 
IO-Link modules.
– The Axioline master firmware has received a mainte-
nance update.
Cyber Security
– The “Security Profile” can now be activated without li-
cense.
– The TLS socket classes (C++) support CRLs, session 
renegotiation and session resumption (partially sup-
ports IEC 62351).
– The TLS socket classes (C++) support querying the 
certificate used by the peer during the TLS hand-
shake (partially supports IEC 62351).
– Additional security notifications of the system status 
are logged during the start-up of the PLCnext firm-
ware.
– The new user role “SafetyEngineer” is supported.
– The new user role “SafetyFirmwareUpdater” is sup-
ported.
– The project integrity check results are visualized to 
the user in the WBM (when “Security Profile” is acti-
vated).
HMI
The display of a “System Use Notification” when logging in 
to HMI applications is now supported.
IEC 61131-3
The “DEVICE_INFO” function block is now supported in 
user applications (PLCnext Engineer 2023.0 LTS or 
newer).
OPC UA
The “Minimum UA Client Profile” has been implemented. 
Currently only manual configuration is supported (config-
uration via PLCnext Engineer is in progress).
PLCnext Store
New file formats (*.PlcNextRaC, *.PlcNextRaU, 
*.PlcNextRaR) for offline licensing in combination with 
the PLCnext Store are supported.
PROFINET
– Adjustable process data widths for the built-in PROF-
INET device in combination with the GSDML configu-
ration are now supported. Instead of the previous 
fixed value of 512 bytes, you can now select from a 
predefined set of values between 2 and 512 bytes.
– The PROFINET controller is recertified according to 
PROFINET specification version 2.42 and Net Load 
Class II.
– The PROFINET device is recertified according to 
PROFINET specification version 2.42 and Net Load 
Class II.
RSC
The RSC service “IDeviceStatusService” is extended to 
read additional information. The  items “Status.Mem-
ory.Usage.Percent.Actual”, “Status.RunStopSwitch.Sup-
ported” and “Status.RunStopSwitch.Position” have been 
added.
SPLC
The left-alignable extension module AXC F XT SPLC 3000 
(item no. 1160157) is supported.

<!-- page 42 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 42 / 101
WBM
– The new “Netload Limiter” tab on the page “Network” 
now supports the display of “NetLoadLimiter” statis-
tic values and the user configuration for each network 
interface.
– The “General Data” page now provides additional arti-
cle information on the safety PLC.
– The generation of the new private key “RSA 
2048 Hardware protected key” is now supported in 
“Add Identity Store”, “Key Type” on the “Certificate 
Authentication” page.
– A new WBM page “Cockpit” is provided.
– WBM users can change their own password directly 
via the new “Cockpit” page.
17.2 Changes
ESM
The maximum task latency in multi core applications (by 
using C++ or IEC 61131-3 programs in different tasks on 
different ESM) has been reduced significantly.
Linux/SDK
– Some PLCnext SDK header files included the name-
space “Arp::System::Commons::Threading” by acci-
dent. This has now been corrected. In order to 
eliminate compiler errors, C++ projects created by the 
customer may need to include the namespace explic-
itly (e.g. statement “using Arp::System::Com-
mons::Threading;”) or use the fully qualified name by 
preceding the name of the related types with 
“Arp::System::Commons::Threading::”.
– LDAP (libldap) has been updated to version 2.5.12. 
This version does no longer depend on “libg-
crypt20.so”. Therefore, “libgcrypt” is no longer part of 
the PLCnext Linux.
System
The feature “reset to default setting” now considers OCI 
containers. The folders below will now be removed: 
– /media/rfs/rw/var 
– /media/rfs/rw/data
17.3 Error corrections
C++
RSC services that return values as 'out' parameters of an 
array data type and are called from C++ code, now clear 
the array before writing any value.
ESM
– Sporadically it could happen that the ESM event task 
“Interbus cycle end” influenced the running INTER-
BUS by a runtime difference, if the system time of the 
controller was changed during operation. This could 
lead to a stop of the INTERBUS master.
– The LOGIC ANALYZER in PLCnext Engineer did not log 
any variable values if an ESM task of type “IDLE” has 
been selected. This occurred with firmware version 
2022.6 and 2022.9 and has been fixed for firmware 
version 2023.0.0 LTS. 
IEC 61131-3
– In case no task was configured to update the Axioline 
output data, Axioline outputs could cause standing 
outputs for a short time in the context of a task with 
linked Axioline ports if the task was stopped by a 
breakpoint set in PLCnext Engineer.
– When debugging IEC code using breakpoints in 
PLCnext Engineer, the PLC stopped with an exception.
– Using the C# method “DateTime.Now” in a static class 
could in some cases cause an error when downloading 
the project.
– If both SRL controllers (system redundancy) were in 
“backup” state (both with “force primary = false”), the 
system variables of the PLC's PROFINET device were 
reset.
– When using the AXC F 2152 as PROFINET device in 
SRL mode (system redundancy) the system variable 
“PND_S1_Data_Length” was set to 0 when the PLC 
was stopped. When the PLC was started again, the 
variable remained 0.
Network
AXC F 2152 with AXC F XT ETH 1TX:
Parallel access of multiple instances to the network 
adapter port status could result in error messages or ex-
ceptions.
Notifications
C# call stack after unhandled exception was doubled in 
“Notification.log”.
OPC UA
– When an eCLR component variable (IEC 61131-3 re-
source global variable) was configured to publish 
'Arp.Plc.Eclr/PLC_CRC_PRJ' via “PubSub”, an excep-
tion occurred during start-up. The “PubSub” compo-
nent and the “UA Server” could apparently not be 
reached afterwards.

<!-- page 43 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 43 / 101
– Project update via OPC UA: If the controller was in the 
“PreparedForUpdate” state, no activation of a down-
loaded boot project was possible. This was also not 
indicated by an error message.
– Some file transfer issues were fixed, e.g. “Writable” 
attribute was always true and PLC crash when remov-
ing permissions.
PROFINET
– If the “MaintenanceItem: Demanded” and the “Prop-
erty Flag” “Maintenance Demanded” both occurred in 
the same PROFINET alarm frame, the alarm was not 
displayed in the PROFINET bus diagnostics in the 
WBM.
– In connection with a set PROFINET cycle time of 1ms, 
the PROFINET controller could experience increased 
latency. This behavior was caused by an unfavorable 
timing during the communication processing of the 
process data. 
– During the startup parameterization of a subordinate 
IO-Link master at an “AXL F BK PN TPS” bus coupler, 
the error message “0xA002” (wrong module found) 
could occur.
– When reading the “ModuleDiffBlock” with the function 
block “GET_MODULE_DIFF_BLOCK” it could happen 
that the states “WRONG_MODULE” and 
“NO_MODULE” were not returned. The error occurred 
when there is a module difference but no submodule 
difference. With “WRONG_MODULE” and “NO_MOD-
ULE” there is no submodule difference and therefore 
the difference was incorrectly not saved.
– If a bus coupler was operated via the PROFINET con-
troller as a subordinate device without connected I/O 
modules, the “SF” LED was not activated. The bus 
coupler reports an “SF” and the PROFINET diagnos-
tics in the WBM also shows this state, but neither the 
status LED nor the system variable “PNIO_SYS-
TEM_SF” indicated this.
– The “MaxSupportedRecordSize” from the GSDML de-
scription of a PROFINET device will now be evaluated 
and interpreted accordingly by the PROFINET control-
ler. Special cases that e.g. “MaxSupportedRecord-
Size” of a PROFINET device is greater than the 
maximum record size of the PROFINET controller will 
be handled correctly.
RSC
When calling the “IDeviceInfoService” 
“General.Hardware.VersionMajor” or “General.Hard-
ware.VersionMinor”, the device responded with “ident not 
found” in the “Output.log” file.
SD card
The detection whether the SD card is plugged in was cor-
rected. This previously caused problems in combination 
with the left-alignable extension module 
AXC F XT SPLC 1000.
Status LEDs
– The “SF” LED was not disabled after the last diagnosis 
disappears with the specifier 
“All subsequent disappears”.
– The LED flashing behavior related to PROFINET did 
not match the description in the manual when wire 
break and network error were triggered in quick suc-
cession.
System
– When installed apps requested a restart of the firm-
ware, it could sporadically happen that this restart 
was not performed properly.
– It could sporadically happen that the PLC went into an 
error state during “download changes”. Even down-
loading the project did not solve the error state. The 
PLC had to be rebooted.
User Manager
– Deleting all entries in “Blocked Passwords” in the 
WBM under “Security”, “User Authentication”, “Pass-
word Policy” did not work. After “Apply and reboot”, 
all default entries were still present.
– The security notification “ResetUserRolesFailed” 
could not be triggered.
WBM
– The “Additional value” in the PROFINET diagnostics 
of a device was displayed unformatted.
– The “Additional value” in the PROFINET diagnostics of 
a device was displayed with wrong error code.
– Incorrectly parameterized modules were not always 
displayed as faulty in the “Tree View” of the PROF-
INET diagnostics.
– A “Link down” error was shown in the PROFINET diag-
nostics for a device, although a “Disappear” alarm has 
already been received.
– Very long DNS names were displayed unclearly in the 
PROFINET diagnostics for a device.
– On the WBM page “Network” in the “Configuration” 
area, LAN interfaces and ports were displayed 
incorrectly.
– Different “escape” behavior on different WBM pages 
has now been unified.

<!-- page 44 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 44 / 101
– Some long diagnostic texts in the context of PROF-
INET device diagnostics were truncated.
– Errors occurred in the WBM Axioline diagnostics when 
displaying different Axioline base profiles (e.g. module 
2.0 or 3.0 profile).
17.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
17.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
BusyBox
– CVE-2022-30065
Curl
– CVE-2022-32207 
– CVE-2022-32206 
– CVE-2022-32208 
– CVE-2022-32205
– CVE-2022-35252 
– CVE-2022-42915 
– CVE-2022-42916
Dpkg
– CVE-2022-1664
E2fsprogs
– CVE-2022-1304
Git
– CVE-2022-29187
– CVE-2022-39260
– CVE-2022-39253
Gnutls
– CVE-2022-2509
HMI
– Hardening against DoS attacks. 
– Hardening against memory leak problems in case of 
network attacks.
Libtirpc
– CVE-2021-46828
Libxml2
– CVE-2022-40304
Libexpat
– CVE-2022-40674 
– CVE-2022-43680
Linux
– CVE-2022-1015 
– CVE-2022-1016
Logrotate
– CVE-2022-1348
OpenSSL
– CVE-2022-2097
Python
– CVE-2022-42919
SSH
– CVE 2002-20001 
The following vulnerable DHE KEX algorithm(s) of the 
openSSH server have been completely removed: 
– diffie-hellman-group14-sha256 
– diffie-hellman-group16-sha512 
– diffie-hellman-group18-sha512 
– diffie-hellman-group-exchange-sha256
StrongSwan
– CVE-2022-40617

<!-- page 45 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 45 / 101
Sudo
– CVE-2022-43995
User Manager
– By mistake, the “SecurityToken” when creating and 
modifying users was always “0000000” in the securi-
ty notifications.
– Hardening of Trust and Identity Stores.
Vim
– CVE-2022-1927 
– CVE-2022-1942 
– CVE-2022-2129 
– CVE-2022-2175 
– CVE-2022-2182 
– CVE-2022-2183 
– CVE-2022-2343 
– CVE-2022-2207 
– CVE-2022-2210 
– CVE-2022-2344 
– CVE-2022-2304 
– CVE-2022-2345 
– CVE-2022-2231 
– CVE-2022-2287 
– CVE-2022-2284 
– CVE-2022-2289 
– CVE-2022-2288 
– CVE-2022-2264 
– CVE-2022-2206 
– CVE-2022-2257 
– CVE-2022-2208 
– CVE-2022-2285 
– CVE-2022-2286 
– CVE-2022-2257
– CVE-2022-2522 
– CVE-2022-2571 
– CVE-2022-2580 
– CVE-2022-2581 
– CVE-2022-2598
– CVE-2022-3234 
– CVE-2022-3235 
– CVE-2022-3256 
– CVE-2022-3278 
– CVE-2022-3296 
– CVE-2022-3297 
– CVE-2022-3324 
– CVE-2022-3352 
– CVE-2022-3705
WBM
– Umlauts in the password of the “User Manager” were 
not handled correctly. The password rule for upper 
and lower case was not followed. This could lead to 
unintentionally weaker passwords.
– Hardening of WBM against Cross-Site-Scripting.
Zlib
– CVE-2022-37434

<!-- page 46 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 46 / 101
18 Changes in firmware version 
2022.9.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.9 or new-
er.
Select the latest template for firmware version 
2022.9 in the PLCnext Engineer project.
This section describes changes made between firmware 
version 2022.6.0 and firmware version 2022.9.0.
All parts of the previously released version and changes 
made in 2022.0.8 LTS are included in the current version.
18.1 New functions
OPC UA
OPC UA supports ReverseConnect. PLCnext Engineer 
2022.9 (or newer) and the related template are required 
for the configuration of this feature.
Proficloud
– The update of the application via Proficloud is sup-
ported. In PLCnext Engineer 2022.9 (and newer) an 
export of an updated application can be generated 
(“Export PLCnext Engineer Software Package”/“Ex-
port PLCnext Engineer Software Package (with sourc-
es)”). The exported files can be uploaded to the 
Proficloud and from there assigned to further devices. 
Note that Proficloud will support this feature in a fu-
ture version.
– In case the connection between the Proficloud and 
the PLC is interrupted, the data can now be cached 
permanently in the PLC and sent after reconnection. 
The feature can be enabled and configured via the 
“Proficloud Services” page in the WBM.
18.2 Changes
OPC UA
The “ManufacturerUri” has been renamed again from 
“http://www.phoenixcontact.com” to 
“http://phoenixcontact.com”.
18.3 Error corrections
PROFINET
– When loading the project, an exception could occur if 
the following applied: A submodule with different in-
put and output data width with corresponding data 
ports was registered to the controller’s PROFINET de-
vice via the bus configuration of the superior 
PROFINET controller.
– Setting values of “maxSlots” or “maxSubslots” in the 
PROFINET settings files were not effectively adopted.
HMI
When changes made in the HMI project were applied with 
“Download Changes”, a “SIGSEGV” exception could occur 
that resulted in a PLC system watchdog (SWD).
WBM
When updating an older firmware version to version 
“2022.6.0” or “2022.6.1”, WBM access was not possible 
after the reboot. The only remedy was to restart the con-
troller again.
18.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
18.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
 The following DHE KEX algorithm(s) of the openSSH 
server will be removed in a future firmware release: 
– diffie-hellman-group14-sha256 
– diffie-hellman-group16-sha512 
– diffie-hellman-group18-sha512 
– diffie-hellman-group-exchange-sha256
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt

<!-- page 47 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 47 / 101
Curl
– CVE-2022-32207
– CVE-2022-32206
– CVE-2022-32208
– CVE-2022-32205
Vim
– CVE-2022-2522 
– CVE-2022-2571 
– CVE-2022-2580
– CVE-2022-2581 
– CVE-2022-2598

<!-- page 48 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 48 / 101
19 Changes in firmware version 
2022.6.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.6 or new-
er.
Select the latest template for firmware version 
2022.6 in the PLCnext Engineer project.
19.1 New functions
OPC UA
– The PubSub feature was extended with the following 
facets:
– Subscriber UADP Dynamic Data or Events Facet
– Publisher UADP Dynamic Data or Events Facet
– Subscriber UADP Flexible Layout Facet
– Publisher UADP Flexible Layout Facet
– The OPC UA server supports references to nodes in its 
own address space according to 
“https://reference.opcfoundation.org/Core/docs/
Part17/A.2/”.
PROFINET
In case of module differences, the notification 
“Arp.Io.PnC.ArReady” contains information about the 
“ModuleDiffblock” which has been sent by the PROFINET 
device. The module difference is also displayed on the 
PROFINET page in the “Diagnostics” area of the WBM.
Security
– An integrity check for PLCnext Engineer projects was 
implemented. The action in case of an integrity breach 
can be configured (“Warning” mode is enabled by de-
fault, “Error” mode can be configured). 
Note: If the integrity check is active, any project is 
checked while loading. This means that an integrity 
breach is also detected for projects without the hash 
code, e.g. projects that are created with a 
PLCnext Engineer version prior to 2022.6. The notifi-
cation payload will report: “Manifest file 'PCWE.mani-
fest.config' does not exist.”.
– During startup a notification is emitted which lists all 
installed PLCnext apps.
– The syslog configuration has been extended to include 
events logged by “podman”.
WBM
– The TLS version and a cipher suite can be selected on 
the “Web Services” page.
– If a password expiration is configured, the WBM 
shows a warning after login indicating when the pass-
word will expire within the configured period.
– On the page “License Management” the UUID of the 
PLC is shown if a license is stored on the PLC.
19.2 Changes
ESM
The handling of the “Idle” task by the ESM has been opti-
mized. The resulting cycle time is shorter and the idle task 
is now executed more often. 
GDS
The GDS has been optimized so that less time is required 
to execute the GDS connectors.
Linux/SDK
– GCC compiler has been upgraded from version 9.3 to 
version 11.2. When executed on Microsoft Windows 
with MinGW, the feature “pre-compiled header” does 
not work due to this update (gcc reports an internal er-
ror).
– By accident some PLCnext SDK header files included 
the namespace “std”. This has now been corrected. In 
order to eliminate compiler errors, C++ projects creat-
ed by the customer may need to include the name-
space explicitly (i.e. statement “using std;”) or use the 
fully qualified name by preceding the name of the re-
lated types with “std::”.
– During refactoring of some PLCnext RSC services, type 
aliases were removed. This also happened inside the 
“IDataLoggerService2” which utilizes the “VariableIn-
fo” class from namespace “Arp::Plc::Gds::Ser-
vices”. Before the refactoring this class was 
introduced into the “Arp::Services::DataLogger::Ser-
vices” namespace by the “VariableInfo.hpp” file, lo-
cated in the same directory as the 
“IDataLoggerService2.hpp”. By now, the “VariableIn-
fo” class is not directly included in the 
“Arp::Services::DataLogger::Services” namespace 
but used as a type alias inside the “IDataLoggerSer-
vice2” interface. This means, applications that used 
the “VariableInfo.hpp” before the refactoring of the 
“IDataLoggerService2” now have to include the fol-
lowing statement in order to compile successfully:     
“using VariableInfo = Arp::Services::DataLogger::Ser-
vice::IDataLoggerService2::VariableInfo;”

<!-- page 49 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 49 / 101
PROFINET
The PROFINET PRL (Phoenix Redundancy Layer) is no lon-
ger supported with firmware version 2022.6.
SD Card
The partitioning of “SD FLASH 8GB PLCNEXT MEM-
ORY LIC (item no. 1151112)” and “SD FLASH 32GB PLC-
NEXT MEMORY LIC (item no. 1151111)” has been 
changed. The PLCnext firmware has been adopted to this 
partitioning.
WBM
– A security notification “Security.Arp.System.Um.Sys-
temUseNotificationSet” is issued when the “System 
Use Notification” is changed via WBM.
– When the “Security Profile” is enabled the 
“User Authentication” cannot be disabled.
– Details about the “ModuleDiffBlock” are displayed on 
the PROFINET page in the “Diagnostics” area of the 
WBM. In particular the Module ID of the module that is 
physically present at the device is displayed.
19.3 Error corrections
ESM
If an ESM task had a fatal error and exited immediately, an 
unhandled follow-up exception led to a deadlock of the 
application.
PLCnext Engineer
When setting date/time via PLCnext Engineer and immedi-
ately shutting off the power supply, the date/time setting 
did not become effective.
PROFINET
– When cyclic tasks at all ESM (cores) were used and 
these tasks had an execution duration (ESM_DA-
TA.ESM_INFOS[..].TASK_INFOS[..].MAX_EXEC_DU-
RATION) longer than the configured Monitor time of a 
PROFINET device (in PLCnext Engineer: Profinet de-
vice in the PLANT area → interface node → Settings tab 
→ Monitor time), this PROFINET device connection 
could be terminated and re-established. This bug has 
been fixed.
– When a superior PROFINET controller attempted to 
set an IP address of the PROFINET device of the 
PLCnext controller while the system was booting, the 
firmware could crash (SIGSEGV). 
WBM/Security
– The option “Exclude admin users from timeout” did 
not work, the admin cannot be excluded. This option 
can be set at the “Session Configuration” tab of the 
WBM page “User Authentication”.
– with AXC F XT ETH 1TX:
On the WBM page “Network” in the “Configuration” 
area, LAN interfaces and ports were displayed incor-
rectly.
19.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
19.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
 The following DHE KEX algorithm(s) of the openSSH 
server will be removed in a future firmware release: 
– diffie-hellman-group14-sha256 
– diffie-hellman-group16-sha512 
– diffie-hellman-group18-sha512 
– diffie-hellman-group-exchange-sha256
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
BusyBox
– CVE-2022-28391
C-ares
– CVE-2021-3672

<!-- page 50 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 50 / 101
Curl
– CVE-2022-22576
– CVE-2022-27778 
– CVE-2022-27779 
– CVE-2022-27782
– CVE-2022-27774
– CVE-2022-27776
– CVE-2022-30115
– CVE-2022-27780
– CVE-2022-27781
– CVE-2022-27775 
Cyrus SASL
– CVE-2019-19906
– CVE-2022-24407
GLIBC
– CVE-2022-23218
– CVE-2022-23219
Kernel
– CVE-2018-12207
Libxml
– CVE-2022-29824
– CVE-2022-23308
Ncurses
– CVE-2022-29458
Nginx
– CVE-2021-3618
OpenSSL
– CVE-2022-0778
OpenVPN
– CVE-2022-0547
Podman
– CVE-2022-1227
– CVE-2022-27649
Protobuf
– CVE-2021-22570
Python
– CVE-2021-29921
Rsync
– CVE-2020-14387
SSH
– CVE 2002-20001 (fixed, if Security Profile is enabled)
SSL
– CVE-2011-1473
– CVE-2011-5094
Vim
– CVE-2022-1381
– CVE-2022-1420
– CVE-2022-1733
– CVE-2022-1796
– CVE-2022-1621
– CVE-2022-1616
– CVE-2022-1619
– CVE-2022-1629
– CVE-2022-1735
– CVE-2022-1769
– CVE-2022-1785
– CVE-2022-1620
– CVE-2022-1674
– CVE-2022-1771
– CVE-2022-1886
– CVE-2022-1851
– CVE-2022-1898
– CVE-2022-1720
Zlib
– CVE-2018-25032
CSV
– Sanitized the output (CSV file) of the notifications ex-
port in the WBM in order to prevent CSV injection soft-
ware attack from CVE-2014-3524.
HMI
– In some cases requests via the “REST” interface to 
variables of data type “STRING” that are not marked 
as “HMI” could cause the PLC to crash.
IPv6
– Fixed IPv6 firewall rules despite IPv6 is not fully sup-
ported yet.

<!-- page 51 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 51 / 101
OPC UA
– Unified Automation reported several security risks for 
the OPC UA SDK 1.7.6 and before. All reported issues 
are fixed with the update of OPC UA SDK version 
1.7.7.
System
– It was possible to get admin rights partially via a re-
configuration of the user roles “Engineer” or 
“Commissioner”.
WBM
– Hardening the input validation of user names in 
“User Authentication”.
– Hardening of Cross-Site-Request-Forgery (CSRF) at-
tack in user based web management.

<!-- page 52 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 52 / 101
20 Changes in firmware version 
2022.3.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.3 or new-
er.
Select the latest template for firmware version 
2022.3 in the PLCnext Engineer project.
20.1 New functions
Articles
Basic support of the left-alignable extension module 
for net measurement and protection AXC F XT PMP-
1000VAC (item no. 1307473).
20.2 Changes
Notification
Performance optimization in the “CreateNonBlockingNoti-
ficationRegistration2” mechanism. Now the “SendNotifi-
cation()” method call in the real-time context is faster and 
needs much less CPU time.
20.3 Error corrections
ESM/INTERBUS
With firmware version 2022.0.4 LTS or earlier, an ESM 
event task could be executed only up to 2,147,483,648 
times (1,024³x2) after power on. This affected mainly the 
“Interbus cycle end” ESM event task. This task is available 
for the AXC F controllers in combination with the 
“AXC F IL ADAPT” or  “AXC F XT IB” extension modules. 
With firmware version 2022.3, this issue is solved.
HMI
With firmware versions 2022.0 LTS and earlier, the HMI 
server stopped when the password of a user who was not 
(or no longer) assigned any “EHmiLevel*” role has been 
changed in the HMI. To recover from this situation the PLC 
needed to be rebooted. This bug has been fixed.
20.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
20.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
LIBEXPAT
– CVE-2022-25235 
– CVE-2022-25236 
– CVE-2022-25313 
– CVE-2022-25314 
– CVE-2022-25315

<!-- page 53 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 53 / 101
21 Changes in firmware version 
2022.0.10 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.0.1 LTS or 
newer.
Select the latest template for firmware version 
2022.0.0 LTS in the PLCnext Engineer project.
This section describes changes made between firmware 
version 2022.0.8 LTS and firmware version 
2022.0.10 LTS.
21.1 Error corrections
INTERBUS
If many INTERBUS devices were connected, it could hap-
pen that the asynchronous communication services (mail-
box) stopped due to an internal buffer overflow. The PLC 
needed to be restarted. This bug has been fixed.
21.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 54 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 54 / 101
22 Changes in firmware version 
2022.0.8 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.0.1 LTS or 
newer.
Select the latest template for firmware version 
2022.0.0 LTS in the PLCnext Engineer project.
22.1 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
22.2 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
BusyBox
– CVE-2022-28391
Curl
– CVE-2022-22576
– CVE-2022-27778
– CVE-2022-27779
– CVE-2022-27782
– CVE-2022-27774
– CVE-2022-27776
– CVE-2022-30115
– CVE-2022-27780
– CVE-2022-27781
– CVE-2022-27775 
– CVE-2022-32207
– CVE-2022-32206
– CVE-2022-32208
– CVE-2022-32205
Cyrus SASL
– CVE-2019-19906
– CVE-2022-24407
HMI
Hardening against DoS attacks. 
IPv6
Fixed IPv6 firewall rules despite IPv6 is not fully sup-
ported yet.
LIBEXPAT
– CVE-2022-25235
– CVE-2022-25236
– CVE-2022-25313
– CVE-2022-25314
– CVE-2022-25315
LIBXML
– CVE-2022-29824
– CVE-2022-23308
OpenSSL
– CVE-2022-0778
OPC UA
Unified Automation reported several security risks for the 
OPC UA SDK 1.7.6 and before. All reported issues are 
fixed with the update of OPC UA SDK version 1.7.7.
OpenVPN
– CVE-2022-0547

<!-- page 55 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 55 / 101
Vim
– CVE-2022-1381 
– CVE-2022-1420
– CVE-2022-1733
– CVE-2022-1796
– CVE-2022-1621
– CVE-2022-1616
– CVE-2022-1619
– CVE-2022-1629
– CVE-2022-1735
– CVE-2022-1769
– CVE-2022-1785
– CVE-2022-1620
– CVE-2022-1674
– CVE-2022-1771
– CVE-2022-1886
– CVE-2022-1851
– CVE-2022-1898
– CVE-2022-1720
– CVE-2022-1154
– CVE-2022-0943
– CVE-2022-1160
– CVE-2022-1381
– CVE-2022-0729
– CVE-2022-0572 
– CVE-2022-1420
– CVE-2022-0696
– CVE-2022-0685 
– CVE-2022-0714 
– CVE-2022-0361 
– CVE-2022-0368 
– CVE-2021-3973 
– CVE-2021-3796 
– CVE-2021-4166 
– CVE-2022-1733 
– CVE-2022-1796 
– CVE-2022-1621 
– CVE-2022-1616 
– CVE-2022-1619 
– CVE-2022-1629 
– CVE-2022-1735 
– CVE-2022-1769 
– CVE-2022-1785 
– CVE-2022-1620 
– CVE-2022-1674 
– CVE-2022-1771 
– CVE-2022-1886 
– CVE-2022-1851 
– CVE-2022-1898 
– CVE-2022-1927 
– CVE-2022-1942 
– CVE-2022-1720 
– CVE-2022-2129 
– CVE-2022-2175 
– CVE-2022-2182 
– CVE-2022-2183 
– CVE-2022-2343 
– CVE-2022-2207 
– CVE-2022-2210 
– CVE-2022-2344 
– CVE-2022-2304 
– CVE-2022-2345 
– CVE-2022-2208 
– CVE-2022-2231 
– CVE-2022-2287 
– CVE-2022-2285 
– CVE-2022-2284 
– CVE-2022-2286 
– CVE-2022-2289 
– CVE-2022-2288 
– CVE-2022-2264 
– CVE-2022-2206 
– CVE-2022-2257
ZLib
– CVE-2018-25032

<!-- page 56 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 56 / 101
23 Changes in firmware version 
2022.0.4 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.0.1 LTS or 
newer.
Select the latest template for firmware version 
2022.0.0 LTS in the PLCnext Engineer project.
23.1 Error corrections
The following errors have been rectified:
eHMI
Depending on the history of firmware versions installed on 
a particular PLC, it could happen that a web browser could 
no longer connect to the PLCnext Engineer HMI on the PLC 
after updating to firmware 2022.0 LTS.
Network
After a reboot or power reset, a connection/link with the 
built-in Ethernet adapters could sporadically not be estab-
lished due to autonegotiation problems. This behavior 
occured mainly in combination with some switches 
and when using short cables.
System
– If the PROFINET controller was deactivated, an un-
wanted notification was emitted (“A subscriber sub-
scribed to not registered notification name: 
Arp.Io.PnC.Alarm”).
– After a power-up and subsequent cold start of the PLC 
project, a “fatal error” could occur very sporadically in 
the controller, followed by a restart triggered by the 
“system watchdog”. This only affected projects with 
Axioline local bus process data linked in the GDS.
WBM
The PROFINET diagnosis in the WBM did not recognize 
some dedicated module/submodule diagnosis (USI for-
mat). As a consequence the related modules/submodules 
were indicated as “Ok” although a diagnosis alarm was ac-
tive.
23.2 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.

<!-- page 57 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 57 / 101
24 Changes in firmware version 
2022.0.3 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2022.0.1 LTS or 
newer.
Select the latest template for firmware version 
2022.0.0 LTS in the PLCnext Engineer project.
24.1 New functions
Linux/OS/Docker
The local gRPC server was integrated for the first time. 
With this first step gRPC offers a kind of standardized open 
source, programming language independent, local inter-
face to most of the published RSC services.
OPC UA
– Controller to controller (C2C) data exchange via UDP 
protocol has been implemented according to 
the OPC UA Publish and Subscribe specification. 
“Publisher UDP UADP Periodic Fixed Profile” and 
“Subscriber UDP UADP Periodic Fixed Profile” are 
supported. Signing and encryption are not supported 
yet. The communication can be configured via 
PLCnext Engineer (from version 2022.0.1 LTS). The 
feature can be enabled via WBM. If enabled, it can be 
evaluated during a 4 hours trail-period. Otherwise a li-
cence (item no. 1392702) must be purchased from 
the PLCnext Store.
– A firmware update is supported according to 
“DI SU Software Update Base Server Facet” and 
“DI SU Cached Loading Server Facet”. For this pur-
pose the new user role “SoftwareUpdate” has been 
introduced. This is a preparation for managing and up-
dating the standard (non-safety) firmware (*.rauc) by 
a Device and Update Management Service (DaUM), 
which will be released as an app for PLCnext in 2022.
WBM
– Password complexity rules and session properties can 
be configured on the WBM page “User Authentica-
tion”.
– NTP servers can be configured on the new WBM page 
“Date and Time”.
PROFINET
– PROFINET diagnostic information for modules and 
submodules are logged as notifications (Notification 
Logger). Additionally this information is shown on the 
“Profinet” page in the “Diagnostics” area of the 
WBM. Furthermore, in case of a PROFINET error, the 
WBM page displays a plain text in English language 
along with the corresponding error code. The plain 
text is issued for both, PROFINET standardized and 
vendor-specific error codes at the module or submod-
ule level.  PLCnext Engineer 2022.0.1LTS or newer (a 
template for firmware 2022.0 LTS or newer has to be 
used as well) collects the corresponding texts from 
the device description file (FDCML resp. GSDML) of the 
related PROFINET devices. The collected texts are 
part of the downloaded project.
– Support of PROFINET “ModuleDiffBlock” information 
with RSC service “IArConfigurationService” and 
IEC 61131-3 function block 
“GET_MODULE_DIFF_BLOCK” (PLCnext Engineer 
2022.0.1 LTS and newer). The WBM already displays 
a module difference in the tree view and also shows 
the message “wrong module” in the device details of 
the PROFINET diagnosis.
Cyber Security
– Security-related notifications are logged to a dedicat-
ed notification archive. Additionally these notifica-
tions are forwarded to the Linux syslog. In the WBM 
the Linux syslog client can be configured to forward its 
log messages to one or more syslog servers.
– A “Security Profile” can be activated via WBM. This re-
quires a license as described in the topic 
“Security Profiles” in the “Security” section of 
https://www.plcnext.help. When the 
“Security Profile” is activated, the PLC is rebooted and 
set into a secure state. This includes deleting the proj-
ect, resetting nearly all configurations and deactivat-
ing potentially insecure system services. Possible use 
cases and security contexts are described in the 
Security Info Center 
(https://security.plcnext.help). If these conditions are 
met, the certification by “TÜV Süd” according to the 
security standard IEC 62443-4-2 can be applied.
24.2 Changes
GDS
In case of GDS configuration errors, all errors are collected 
into a single notification. The previous firmware versions 
only stated the first configuration error and stopped fur-
ther reading of the configuration files. 
C++/SDK
Due to a minor cleanup of the namespaces, some missing 
used statements may cause an error when compiled with 
an SDK version 2022.0 or newer. This may occur in follow-
ing cases:

<!-- page 58 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 58 / 101
1. If the classes “Arp.System.Commons.Console” or 
“Arp.System.Commons.Environment” are used, in-
sert a “using namespace Arp::System::Commons;” 
statement as a remedy. 
2. If any class of the “Arp.System.Commons.Excep-
tions” namespace is used, there are two remedies:  
If the dedicated exception header file has been in-
cluded, insert a “using namespace Arp::Sys-
tem::Commons::Exceptions;” statement as a 
remedy.  
If the general header file “Arp/System/Commons/Ex-
ceptions.h” has been included, insert a “using name-
space Arp;” statement as a remedy.
Netload Limiter
– The “Netload Limiter” function is supported. With the 
“Netload Limiter” function you can limit the network 
traffic to prevent the controller from stopping in case 
of network storms.
– The “Netload Limiter” is actived by default. For the 
built-in Ethernet interface (X1/X2), a limit of 32 pack-
ets per millisecond is configured initially.
HMI
For projects compiled with PLCnext Engineer 
2022.0.1 LTS (and newer) with a template for firmware 
2022.0 LTS (and newer), the system variable HMI_STA-
TUS was replaced by the system variable HMI_STATUS2. 
It was replaced because the member HMI_STATION_-
NUM has been added to the HMI_STATUS_STRUCT and as 
a consequence the new data type HMI_STATUS2 needed 
to be implemented in PLCnext Engineer.
PROFINET
Reduction of frequent and for end users unhelpful mes-
sages in the log file “Output.log”. This mainly concerns 
messages in the PROFINET context.
24.3 Error corrections
The following errors have been rectified:
Axioline
Sporadically and in rare cases the Axioline local bus did 
not start. This has been observed mainly when a firmware 
2021.6 or 2021.9 has been used and an Axioline Smart El-
ement module was used as first Axioline module. Restart-
ing Axioline did resolve the situation. This workaround is 
no longer necessary.
SPLC
AXC F 2152 with AXC F XT SPLC 1000
– When in PLCnext Engineer the interval time of the 
“SafetyTask” has been changed and the project is 
downloaded to the PLC, it could happen that the SPLC 
went into failure state (FS). Afterwards the PLC need-
ed to be rebooted.
– The resolution of the safelog (visible in the “Safety PLC 
log messages” view of PLCnext Engineer) has been 
changed from seconds to milliseconds.
Network
With heavy network load, CPU load problems could occur 
due to a great volume of logging messages.
IEC 61131-3
– When a function block programmed in SFC (Sequen-
tial Function Chart) was changed in PLCnext Engineer, 
these changes could not be sent to the PLC using 
“Download Changes” due to an exception. This error 
only occurred with firmware 2021.9
– In rare cases, the PLC could not be restarted after 
stopping when using PLCnext Engineer. The problem 
only occurred when a cold and warm start were per-
formed and a PROFINET controller was used. The 
problem did not occur during a hot start. The PLC had 
to be rebooted.
– In rare cases, when the firmware rejected a 
“Download Changes” command, the project was 
damaged and had to be downloaded again.
System
– After a power reset, the firmware could sporadical-
ly not be started properly and a System Watchdog oc-
cured.
– In rare cases, the PLC could run immediately into an 
ESM task watchdog after a power reset.
PROFINET
A timer overflow in the PROFINET stack that occurred 
after 49 days was fixed. This mainly affected protocols like 
DCP during connection establishment or the cyclic LLDP 
neighbor discovery. 
PROFIBUS
AXC F 2152 with AXC F XT PB
When a configured PROFIBUS device could not be found 
during the system start, it was not indicated by the related 
PROFIBUS system variable. This could only be detected by 
a blinking LED of the AXC F XT PB.

<!-- page 59 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 59 / 101
Retain
Retain variables inside a function block that have been 
added by a “Download Changes” command have been 
stored in the retentive memory with the value 0. As a con-
sequence, the value was set to 0 after stop and warm start 
. This error occurred since firmware version 2021.0 LTS.
Notifications
After a connection loss when displaying notifications in the 
PLCnext Engineer cockpit, it could happen that the display 
of notifications in the WBM generally no longer worked. 
Only the error message “Lost connection to Controller! 
(timeout)” was displayed.
24.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
24.5 Security updates
As part of the OpenSSH update from “8.4p.1” to 
“8.8p1” (or newer), “SHA1” will be disabled in a fu-
ture firmware release.
BusyBox will be disabled in a future firmware release 
and replaced by other packages if necessary.
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
SSL
– CVE-2021-3712
– CVE-2021-3711
– Deprecated encryption versions “TLSv1.0” and 
“TLSv1.1” were allowed over certain ports.
Strongswan
– CVE-2021-41990
– CVE-2021-45079
Open SSH
– CVE-2016-20012
Open VPN
– CVE-2020-15078
Nettle
– CVE-2021-3580 
– CVE-2021-20305
GIT
– CVE-2021-40330
– CVE-2021-21300
GLIBC
– CVE-2021-35942
– CVE-2020-6096
– CVE-2020-29562
GNUTLS
– CVE-2021-20231
– CVE-2021-20232
– CVE-2020-24659
LIBSSH2
– CVE-2019-17498
LIBXML2
– CVE-2021-3517
– CVE-2021-3518
– CVE-2021-3537
PERL
– CVE-2020-10878
– CVE-2020-10543
– CVE-2020-12723
TAR
– CVE-2021-20193
NGINX
– CVE-2021-23017
NET-SNMP
– CVE-2019-20892

<!-- page 60 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 60 / 101
GMP
– CVE-2021-43618
Python
– CVE-2019-20907
LIBEXPAT
– CVE-2021-45960
– CVE-2022-22824
– CVE-2022-22823
– CVE-2022-22822
– CVE-2022-22825
– CVE-2021-46143
– CVE-2022-22826
– CVE-2022-22827
– CVE-2022-23852
– CVE-2022-23990
CURL
– CVE-2021-22946
– CVE-2020-8169
– CVE-2021-22926 
– CVE-2020-8177 
– CVE-2021-22922 
– CVE-2021-22947 
– CVE-2021-22897 
– CVE-2021-22925 
– CVE-2021-22923 
– CVE-2021-22898
BusyBox
– CVE-2021-42374 
– CVE-2021-42386 
– CVE-2021-42380 
– CVE-2021-42381 
– CVE-2021-42379 
– CVE-2021-42384 
– CVE-2021-42378 
– CVE-2021-42382 
– CVE-2021-42385 
The documented CVEs were not fixed via an update of 
BusyBox. Instead, the affected BusyBox components 
have been removed: The following config switches 
have been switched off (“not set”): 
CONFIG_FEATURE_SEAMLESS_LZMA=y 
CONFIG_ASH=y 
CONFIG_AWK=y 
In the case of “AWK” it makes no difference as this 
tool is also integrated from the core utils library. The 
shell “ASH” and the “LZMA” algorithms (i.e. for unzip) 
are no longer supported.
– CVE-2018-1000500
OPC UA
– CVE-2021-45117
BASH
– CVE-2019-18276
Network
DoS attacks over network could lead to a PLC project stop 
caused by the ESM Task Watchdog.
LDAP
A change from the registered “Cipher Suite” to the default 
value in the LDAP configuration did not work.
PROFINET
– The public “IConfigurationService” could be used by 
mistake in the C++ SDK without authorization.
– The data length at the 
“IAcyclicCommunicationService::RecordWrite” was 
not checked properly. This could result in memory be-
ing read beyond the vector boundary and sent as re-
cord data.

<!-- page 61 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 61 / 101
25 Changes in firmware version 
2021.9.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2021.9.0 or 
newer.
Select the latest template for firmware version 
2021.9.0 in the PLCnext Engineer project.
25.1 New functions
System
The binding of licenses for certain extension functional-
ities is now also possible in connection with an inserted 
SD card with corresponding license. 
This works exclusively with the following SD cards: 
– SD FLASH 8GB PLCNEXT MEMORY LIC 
(item no. 1151112) 
– SD FLASH 32GB PLCNEXT MEMORY LIC 
(item no. 1151111) 
– SD FLASH PLCNEXT MEMORY LIC CFG 
(item no. 1308064)
Linux/OS/Docker
The Docker engine Podman was integrated for the first 
time. With this step Podman is exclusively available for 
use in context of PLCnext Store apps.
PROFIBUS
Support of the left-alignable PROFIBUS master extension 
module AXC F XT PB (item no. 1091657).
DataLogger
The DataLogger has been improved to emit more notifica-
tions.
PLCnext Store
Extension of PLCnext Store support with the following 
subjects: 
– Specifying the ContainerID for license operations. 
– Report active ContainerIDs to the PLCnext Store. 
– Transfer SD card slot status to the PLCnext Store. 
– In addition to licenses bound to the device, licenses 
can now also be bound to the LIC SD cards.
OPC UA
The OPC UA server of the controller has been certified ac-
cording to OPC UA version 1.0.4.
25.2 Error corrections
The following errors have been rectified:
System
In rare cases, the controller did no longer recognize the 
SD card after an interruption of the power supply. All LEDs 
flashed and the controller could not be connected via 
Ethernet. Only some 2 GB SD cards were affected by this.
PLCnext Store
If an app created a file with write permissions in the tem-
porary files directory (“/var/tmp/appsdata/“), these write 
permissions were removed after a system reboot. As a re-
sult, the app could no longer write to the file.
GDS
If with firmware 2021.6.0 a fieldbus I/O of data type Bit-
string or OctetString was connected to a program port of 
data type ARRAY, only the value of the first ARRAY ele-
ment was transferred. The remaining elements were not 
copied.
OPC UA
When using a custom information model namespace the 
“BrowseName” was not returned to the OPC UA client.
25.3 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
– Retain variables
– If a requested warm start is not possible to exe-
cute via PLCnext Engineer, an implicit cold start is 
automatically executed. The retain variables are 
set to their initialization value.
– After a system watchdog, only a cold start can be 
performed when the controller is started. The re-
tain variables are set to their respective initializa-
tion values.
From firmware 2021.0 LTS and newer a dedicated 
state of the retain values can be restored from a 
backup.
– If firmware version 2020.0 LTS or later is down-
graded to 2019.9 or older and then upgraded 
again to firmware version 2020.0 LTS or later, a 
cold start is performed. The retain variables are 
set to their initialization value.
– EthernetIP
If the firewall is activated via WBM, the operation of

<!-- page 62 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 62 / 101
EthernetIP is no longer possible.
This can be remedied by subsequently activating the 
ports:
– Incoming connections: port 44818
– Outgoing connection: port 2222
– PLCnext CLI version
The PLCnext CLI version used must match the cur-
rent SDK for this version. Downward compatibility 
cannot be guaranteed. 
– Configuration changes to safety nodes
With attached AXC F XT SPLC 1000:
Only a complete recompilation and redownload of the 
standard and safety project guarantees a consistent 
adoption of configuration changes to safety nodes in 
the bus structure of the standard project.
– Firmware downgrade
After downgrading the firmware, it is recommended to 
reset to “Default setting type 1”. This is not necessary 
when updating the firmware.
– WBM error message
If the PLCnext system firmware has not started up 
properly, the WBM displays the error message 
“Bad Gateway 502”.
– Task name
If “Event”, “EventTask”, “ServiceTask” or “Globals” is 
used as the name of a task, an error condition of the 
controller occurs when the project is downloaded. It 
occurs because these names are already used inter-
nally as class name.
– DHCP
DHCP can only be switched on for Ethernet adapt-
ers that are not assigned as PROFINET controllers 
or PROFINET devices. To make the settings effective 
in the network, the device must be restarted.
– Variables
The content of the variables “ESM_DATA.ESM_IN-
FOS[*].ESM_TICK_COUNT” and “ESM_DATA.ES-
M_INFOS[*].ESM_TICK_INTERVAL” is permanently 
set to 0. 
– Error during program download
During a PLCnext Engineer program download 
(both total and changes), the web server returns an 
error 503 (busy) for requests to the HMI pages. 
– DataLogger
If two or more DataLogger sessions are configured 
to write to the same database, only the data of one 
session will be transferred to the database on the SD 
card at the end. As of firmware 2021.9 the user re-
ceives a notification indicating which session is re-
corded. 
– Retain data
Using the maximum quantity structures of the retain 
data can increase the task duration of the using task. 
This can trigger a task watchdog for time-critical ap-
plications. 
– STRING variables
Access to long STRING variables outside the applica-
tion is limited to 511 bytes. This concerns reading and 
writing via the RSC services “IDataAccessService” 
and “ISubscriptionService”. These services are used 
by OPC UA, PLCnext Engineer HMI and the online 
functions of PLCnext Engineer, among others. 
From firmware version 2021.6: The same applies for 
WSTRING variables. Please note that WSTRING vari-
ables are converted to UTF8 when accessed via RSC 
services.
– “Download Changes“
Sporadically a PLCnext Engineer project may re-
ject “Download changes” without giving a reason.
– Restart after app installation
Sporadically it can happen that a restart of the firm-
ware requested by an app installation does not work 
properly. If the firmware does not start up correctly, 
the controller can be restarted by one of the following 
3 possible actions: 
– Restart of the firmware via SSH 
(/etc/init.d/plcnext restart)
– Reboot of the controller via SSH 
– Power reset of the controller
– Local time zone setting
Setting local time zones is not fully supported.
– “Link” and “Active” LEDs
The “Link” and “Active” LEDs on the network interfac-
es “X1” and “X2” are not active when a “10BaseT” 
connection is used.
– PROFINET cycle time
The use of a PROFINET cycle time of 1 ms leads to a 
deviation of the jitter behavior required by the control-
ler certification. 
Operation in this state is possible, but not recom-
mended.
– Language standard C++ 17
With the SDK version 2021.6 the language standard 
C++ 17 has been set in the compiler options 
("-std=c++17"). The firmware itself is also compiled 
with this option set. Besides some general C++ issues 
related to this C++17 standard, the following issue is 
related to PLCnext: 
C++ 17 introduces the data type “std::byte” which is 
unfortunately not compatible with “Arp::byte”. There-
fore, if the namespaces “std” and “Arp” are both ac-

<!-- page 63 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 63 / 101
tive the compilation results in an error.  In this case 
existing C++ sources have to be adjusted so that they 
explicitly use “Arp::byte” (e.g. by adding “using byte = 
Arp::byte;“).
– Communication errors
Sporadic communication errors may occur between 
PLCnext Engineer and the controller. A reboot of the 
controller solves the problem.
– Unexpected behavior using the Select() method
The Select() method of the classes Arp::System::Com-
mons::Ipc::IpcSocket, Arp::System::Com-
mons::Net::Socket 
and Arp::System::Commons::Net::TlsSocket returns 
true, when the socket is shut down. Compared to BSD 
sockets, this behavior is unexpected. As this is a lega-
cy method it is now remarked as deprecated. In fu-
ture, additionally a new method Poll() will be 
implemented.
– System crash caused by user components
If a user component causes a crash before the system 
watchdog is activated, the firmware terminates and 
the controller is available via SSH only. 
Note: The system watchdog is activated just before 
the IControllerComponent::Start() method is invoked. 
– License operations, such as adding or removing a li-
cense, include cryptographic operations and hence 
shall only be performed if the PLC is stopped. This 
may avoid side effects due to preempting the license 
operations by tasks running with higher priority. 
25.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
WBM
– Deprecated SSL/TLS protocols in nginx web server 
have been disabled. 
Only TLS v1.2 and v1.3 are now enabled.
– The post-payload of the “WebConfiguration.cgi?Set
HttpsCertificateIdentityStore” function could be 
modified in a way that could potentially be exploited 
via reflected XSS (cross-site scripting).
LDAP
– The LDAP “GroupMappings” were compared 
with “case sensitivity”  on the controller, although the 
“case sensitivity” support was disabled on the LDAP 
server. No error message indicating this fact was 
thrown. Now when the firmware reads in its LDAP 
server configuration, the LDAP “GroupMappings” 
were converted to lower case.
– The cipher list setting for the LDAP TLS configuration 
for the server connection was not properly applied. As 
a result, the highest possible encryption method was 
not always selected for the communication.

<!-- page 64 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 64 / 101
26 Changes in firmware version 
2021.6.0
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2021.6.0 or 
newer.
Select the latest template for firmware version 
2021.6.0 in the PLCnext Engineer project.
The versions “TLS v1.0/v1.1” in the context of the 
web server are supported in this firmware version, 
but will be disabled in one of the future firmware ver-
sions. The deactivation may cause connection prob-
lems with old browsers. There are no effects on the 
TLS function block functionality.
26.1 New functions
WBM
– The WBM has been extended by a page to activate and 
deactivate “System Services”.
– It is now possible to edit the IP configuration via WBM. 
Therefore the former display page 
“Network Configuration” has been renamed to 
“Network” and was moved from the “Information” to 
the “Configuration” area. It depends on the user role 
whether the IP settings can be edited or only viewed.
SPNS
– Support of the left-alignable safety-related extension 
AXC F XT SPLC 1000 (order no. 1159811).
IEC 61131
– The data type WSTRING has been added for 
IEC 61131-3 applications programmed with 
PLCnext Engineer version 2021.3 (or newer). Corre-
spondingly the data type StaticWString<> has been 
added in C++ as template class. This data type is sup-
ported by IEC Runtime, GDS, Data Logger, 
OPC UA Server and HMI.
– The new function block family UDP_SOCKET_2, 
UDP_SEND_2 and UDP_RECEIVE_2 supports sending 
of UDP broadcast datagrams. 
The new function block family TLS_SOCKET_2, 
TLS_SEND_2 and TLS_RECEIVE_2 supports program-
ming a TCP/TLS server which can communicate with 
more than one TCP/TLS client at the same time. These 
function blocks can be used in combination with 
PLCnext Engineer versions newer than 2021.6.0.
GDS
The link ability between process data (Octet String) and 
variables of the user application was extended.
HMI
The PLC state “Force Mode” is now displayed by the 
“DBG” LED (debug LED) or a display flag. Besides debug 
states (e.g. triggered by breakpoints), the DBG LED (re-
spectively its corresponding element on the touch screen 
display) now also shows when the variables are forced.
DataLogger
– The DataLogger has been extended: By specifying the 
name of an ESM task, the values of all configured vari-
ables will be sampled within this task. This con-
cerns resource-global variables and component ports 
as well as variables instantiated within a program as-
sociated to any ESM task. 
– The DataLogger supports the configuration for trig-
gered data logging.
System
The binding of licenses for certain extension functional-
ities is now also possible in connection with an inserted SD 
card with corresponding license. This works exclusively 
with the following SD cards: 
– SD FLASH 8GB PLCNEXT MEMORY LIC 
(order no. 1151112) 
– SD FLASH 32GB PLCNEXT MEMORY LIC 
(order no. 1151111)
PLCnext Store
PLCnext Store and app installation improvements:
– The installation of apps without reboot is supported.
– Apps can be downloaded with improved speed.
26.2 Changes
System
– Linux kernel was updated to version 5.4 LTS.
– “Paho” libraries were updated to the following ver-
sions:
– paho-mqtt-c: 1.3.8 
– paho-mqtt-cpp: 1.2.0
– The PLC project download performance was im-
proved.
– When setting the IP address, subnet mask or gateway, 
the value “255.255.255.255” is now rejected as inval-
id. Previously the firmware did not boot (a reset to de-
fault setting type 1 was required.)

<!-- page 65 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 65 / 101
26.3 Error corrections
The following errors have been rectified:
GDS/RSC
During the implementation of WSTRING, the behavior of 
the IGdsDataAccess service has been changed with re-
gards to writing a value to a variable or port of data type 
STRING or StaticString<>. If in previous firmware versions 
the value was longer than the capacity of the variable/port, 
only as much bytes as provided by the variable have been 
copied. Additionally a warning message has been written 
to the Output.log file. 
With firmware 2021.6 in this case the service method re-
turns DataAccessError::StringLengthExceeds, no bytes 
are copied, and no warning message is emitted. The same 
handling has been implemented for data type WSTRING.
WBM
– A difference in the network configuration was not de-
tected and displayed in the WBM if, for example, a 
change was made by a “DCP” configuration via net-
work.
– The representation of hex values in the WBM was par-
tially inconsistent.
– After an update from firmware versions 2020.6.x and 
older to firmware versions 2021.0.x, it was possible 
that the adopted WBM certificate could not be 
changed afterwards. A reset to default setting type 1 
was necessary to be able to change the certificate.
– When setting a new user password in WBM, an errone-
ous error message occurred if the new password was 
entered first in the field “Confirm Password” and then 
in “New Password”.
– In the text field “Tip of the day” inconsistent use of 
punctuation marks occurred.
– In the text field “Edit System Use Notification” there 
was an inconsistent display of previously saved char-
acters when editing again.
IEC 61131
– If an application was stopped by a breakpoint, the 
fieldbus process data could queue for one cycle when 
stepping on.
– The IEC 61131 runtime system could enter an unde-
fined error state when downloading a PLC project that 
happened to use the same type names that were al-
ready used internally. This caused ambiguities. This 
applied, for example, to program/task/instance or 
function block names.
– In firmware versions 2021.0.x it could happen that af-
ter an update of older firmware versions the error 
message “Task 'Globals' already defined.” could oc-
cur when restarting the existing boot project. As a re-
sult, the project could not start properly due to an 
incompatible ESM configuration.
– In connection with a PLC project which uses almost 
the entire number of possible retain variables, a PLC 
task watchdog could sporadically occur after a restart 
of the controller.
– The controller went into the FAIL state after frequent 
cold starts of the PLC project. Before each call of the 
OPC UA server, a warning from the root is displayed: 
“Enumerator: Too many open files”. After that a 
“CRITICAL” log from the OPC UA server is displayed.
PROFINET
– An incompatibility of Engineer apps with the possibili-
ty to switch off PROFINET controller/device was fixed. 
Inconsistency errors occurred when trying to switch 
off the PROFINET device only.
– When shutting down the system, internal thread ex-
ceptions could sporadically occur when terminating 
the process. This could cause the system to stop re-
sponding.
Network
In case the “dhcp” option was configured in the “inter-
faces” configuration file, it could happen that the manual 
“DHCP Gateway” setting was overwritten.
SDK/C++
It was not possible for the “StaticString” class to com-
pletely empty the contained pre-initialized “CHAR” array. 
With firmware 2021.6 the methods Clear() and IsEmpty() 
have been added.
System
– Starting with firmware versions 2020.9.x, numerous 
unhelpful logging outputs of the “rngd daemon” could 
occur in the log file “/var/log/debug”. This led to very 
large logging files.
– During the system startup, the PLCManager loads the 
projects and checks whether a system watchdog has 
occurred before the controller is started. If C++ pro-
grams or components are part of the project, their 
constructors are executed during the loading process 
of the PLC project. If the project was reloaded after a 
system watchdog has occurred, this could lead to re-
peated crashes and restarts that result in an endless 
loop.

<!-- page 66 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 66 / 101
– After setting PROFINET device diagnosis (SF LED on) 
the SF LED remained on, even if the diagnostic event 
was already completed and no longer pending.
– When restarting the controller, some informative 
messages were erroneously written to the log as type 
“ERROR”.
– After activating the MRP function, it was not shown as 
activated when reading back the status. After restart-
ing the controller it was deactivated again.
PROFICLOUD
– In case the PLC lost the connection to the internet, the 
link to Proficloud.io was not being re-established au-
tomatically. To return to online mode with 
proficloud.io, the PLC required a reboot or a restart of 
the ProficloudV3 services via WBM.
– If the connection to the Internet was lost, the WBM 
page of ProficloudV3 could not be accessed as long as 
the Internet connection remains lost.
– When writing log messages too quickly one after the 
other, it could happen that not all log messages were 
displayed in the cloud or some had the same 
timestamp.
– When a large number of data points could not be sent 
due to a network link failure, stopping of the TSD ser-
vice was severely delayed.
– Sending significantly more than 50 configured data 
points could take an unexpectedly long time. With 
firmware 2021.6 the performance has been improved 
so that one PLC can send the values of up to 300 vari-
ables to the Proficloud.
OPC UA
– When an OPC UA client tried to call a function without 
required arguments, the PLC crashed.
– If an OPC UA client tried to browse an array of struct 
with children of kind array of primitive types where the 
index is out of range, the PLC could crash. 
– Certain changes to security policies were applied only 
after a restart.
DataLogger
– During data logging in connection with the display of 
HMI data trend it could happen that memory was not 
released again.
– A “Download changes” command of the PLC project 
did not work if a “Rocks DB” session (HMI trending) of 
the DataLogger was active at the same time.
ESM
– Sporadically it could happen that a higher priority task 
together with a lower priority task on the same ESM 
core had a startup delay that should not have hap-
pened according to the priority.
– Sporadically, it could happen that when starting the 
PLC project, the task runtime was extended during the 
first cycle.
26.4 Known limitations and errors
The known limitations and errors can be found in the 
PLCnext Info Center at:
https://www.plcnext.help/te/Known_issues.htm
Here you will find a constantly updated overview of 
all known issues.
– Retain variables
– If a requested warm start is not possible to exe-
cute via PLCnext Engineer, an implicit cold start is 
automatically executed. The retain variables are 
set to their initialization value.
– After a system watchdog, only a cold start can be 
performed when the controller is started. The re-
tain variables are set to their respective initializa-
tion values.
From firmware 2021.0 LTS and newer a dedicated 
state of the retain values can be restored from a 
backup.
– If firmware version 2020.0 LTS or later is down-
graded to 2019.9 or older and then upgraded 
again to firmware version 2020.0 LTS or later, a 
cold start is performed. The retain variables are 
set to their initialization value.
– EthernetIP
If the firewall is activated via WBM, the operation of 
EthernetIP is no longer possible.
This can be remedied by subsequently activating the 
ports:
– Incoming connections: port 44818
– Outgoing connection: port 2222
– PLCnext CLI version
The PLCnext CLI version used must match the cur-
rent SDK for this version. Downward compatibility 
cannot be guaranteed. 
– Firmware downgrade
After downgrading the firmware, it is recommended to 
reset to “Default setting type 1”. This is not necessary 
when updating the firmware.

<!-- page 67 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 67 / 101
– WBM error message
If the PLCnext system firmware has not started up 
properly, the WBM displays the error message 
“Bad Gateway 502”.
– Task name
If “Event”, “EventTask”, “ServiceTask” or “Globals” is 
used as the name of a task, an error condition of the 
controller occurs when the project is downloaded. It 
occurs because these names are already used inter-
nally as class name.
– DHCP
DHCP can only be switched on for Ethernet adapt-
ers that are not assigned as PROFINET controllers 
or PROFINET devices. To make the settings effective 
in the network, the device must be restarted.
– Variables
The content of the variables “ESM_DATA.ESM_IN-
FOS[*].ESM_TICK_COUNT” and “ESM_DATA.ES-
M_INFOS[*].ESM_TICK_INTERVAL” is permanently 
set to 0. 
– Error during program download
During a PLCnext Engineer program download 
(both total and changes), the web server returns an 
error 503 (busy) for requests to the HMI pages. 
– DataLogger
If two or more DataLogger sessions are configured 
to write to the same database, only the data of one 
session will be transferred to the database on the SD 
card at the end. The user does not receive a message 
that not all data can be saved. 
– Retain data
Using the maximum quantity structures of the retain 
data can increase the task duration of the using task. 
This can trigger a task watchdog for time-critical ap-
plications. 
– STRING variables
Access to long STRING variables outside the applica-
tion is limited to 511 bytes. This concerns reading and 
writing via the RSC services “IDataAccessService” 
and “ISubscriptionService”. These services are used 
by OPC UA, PLCnext Engineer HMI and the online 
functions of PLCnext Engineer, among others. 
From firmware version 2021.6: The same applies for 
WSTRING variables. Please note that WSTRING vari-
ables are converted to UTF8 when accessed via RSC 
services.
– “Download Changes“
Sporadically a PLCnext Engineer project may re-
ject “Download changes” without giving a reason.
– Restart after app installation
Sporadically it can happen that a restart of the firm-
ware requested by an app installation does not work 
properly. If the firmware does not start up correctly, 
the controller can be restarted by one of the following 
3 possible actions: 
– Restart of the firmware via SSH 
(/etc/init.d/plcnext restart)
– Reboot of the controller via SSH 
– Power reset of the controller
– Local time zone setting
Setting local time zones is not fully supported.
– “Link” and “Active” LEDs
The “Link” and “Active” LEDs on the network interfac-
es “X1” and “X2” are not active when a “10BaseT” 
connection is used.
– PROFINET cycle time
The use of a PROFINET cycle time of 1 ms leads to a 
deviation of the jitter behavior required by the control-
ler certification. 
Operation in this state is possible, but not recom-
mended.
– Language standard C++ 17
With the SDK version 2021.6 the language standard 
C++ 17 has been set in the compiler options 
("-std=c++17"). The firmware itself is also compiled 
with this option set. Besides some general C++ issues 
related to this C++17 standard, the following issue is 
related to PLCnext: 
C++ 17 introduces the data type “std::byte” which is 
unfortunately not compatible with “Arp::byte”. There-
fore, if the namespaces “std” and “Arp” are both ac-
tive the compilation results in an error.  In this case 
existing C++ sources have to be adjusted so that they 
explicitly use “Arp::byte” (e.g. by adding “using byte = 
Arp::byte;“).
– Communication errors
Sporadic communication errors may occur between 
PLCnext Engineer and the controller. A reboot of the 
controller solves the problem.
– Unexpected behavior using the Select() method
The Select() method of the classes Arp::System::Com-
mons::Ipc::IpcSocket, Arp::System::Com-
mons::Net::Socket 
and Arp::System::Commons::Net::TlsSocket returns 
true, when the socket is shut down. Compared to BSD 
sockets, this behavior is unexpected. As this is a lega-
cy method it is now remarked as deprecated. In fu-
ture, additionally a new method Poll() will be 
implemented.

<!-- page 68 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 68 / 101
– System crash caused by user components
If a user component causes a crash before the system 
watchdog is activated, the firmware terminates and 
the controller is available via SSH only. 
Note: The system watchdog is activated just before 
the IControllerComponent::Start() method is invoked. 
26.5 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
SSL
– CVE-2020-1971
– CVE-2021-3449 
– CVE-2021-3450
– When updating the OpenSSL version from 1.1.1i to 
1.1.1k in firmware version 2021.0.5, the “scrypt” 
function for generating hash values was no longer 
supported.
RAUC
– CVE-2020-25860
HTTP
– A DoS attack on port 80 using HTTP frames could lead 
to a real-time impact on the PLC runtime.
– CVE-2021-23017
WBM
– A XSS attack was reflected in a JSON response. This 
might leave content consumers vulnerable to attacks 
if they do not appropriately handle the data (re-
sponse).
– A string entered in “Edit System Use Notification” 
could be executed on the login page of the controller.
– Cross-site scripting (XSS) exploitation could occur 
when setting the certificate for the Identity Store.
System
– The “execute bit” of the PLCnext log files (and data-
base files) was mistakenly set. 
– When starting the operating system (or the “rngd“-
service), the CPU usage consistently spiked to 100% 
for several seconds.
– CVE-2021-3156
– CVE-2020-8492

<!-- page 69 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 69 / 101
27 Changes in firmware version 
2021.0.5 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2021.0.2 LTS or 
newer.
Select the latest template for firmware version 
2021.0.0 LTS in the PLCnext Engineer project.
27.1 Changes
System
“Paho” libraries were updated to the following versions:
– paho-mqtt-c: 1.3.8 
– paho-mqtt-cpp: 1.2.0
27.2 Error corrections
The following errors have been rectified:
System
An unusually high amount of logging entries in the log file 
/var/volatile/log/auth.log could cause the system to crash 
after some time.
GDS
Firmware version 2021.0 LTS rejected a GDS connection 
between a port variable of a C++ component and a port 
variable of a program instance. As a consequence the pro-
gram did not start.
PLCnext Store
– During offline installation of licenses a reboot is rec-
ommended. If this reboot has been performed by 
switching off the power, the license files on the con-
troller could be lost.
– If a controller has been updated from a firmware ver-
sion older than 2020.3 to a firmware version 2020.3 
or newer, the folder /opt/plcnext/config in the overlay 
partition sporadically got wrong access rights. As a 
consequence it was not possible to install licenses. In 
the past, a reset to “Default setting type 1“ had to be 
performed as workaround. Firmware version 
2021.0.5 LTS corrects the access rights.
ESM
With firmware version 2021.0 LTS the execution of tasks 
sporadically did not obey the task priorities, when a code 
worksheet was displayed in the online mode of 
PLCnext Engineer.
DataLogger
During the writing of large databases and simultaneous 
unexpected system restart due to a voltage interruption or 
a system watchdog, an invalid state of the database could 
occur. As a result, the system could not restart properly 
afterwards.
27.3 Known limitations and errors
– The app “MQTT_Client_Library” version 2 
(Build 20210205), which is available in the 
PLCnext Store, is not compatible with firmware ver-
sion 2021.0.5 and will cause a system watchdog 
which reboots the controller. Please contact the con-
tributor of the app (PLCnext Store) for any questions 
and potential fixes.
– In addition, the known errors and limitations from 
firmware version 2021.0.2 LTS also exist in this firm-
ware version.
See section 29.3 “Known limitations and errors”on 
page 71.
27.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
SSL
– CVE-2021-3449 
– CVE-2021-3450
RAUC
– CVE-2020-25860

<!-- page 70 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 70 / 101
28 Changes in firmware 
version 2021.0.3 LTS
All changes described in section 29 “Changes in 
firmware version 2021.0.2 LTS” on page 71 are also 
valid for this firmware version.
28.1 Error corrections
The following errors have been rectified:
System
The bug fixing of firmware version 2021.0.2 LTS concern-
ing the logging of information into files located at “tmpFS” 
has been reworked. As of firmware version 2021.0.3 LTS 
the following applies: 
Logging information into files located at “tmpFS” occupied 
too much RAM. Consequently the System Watchdog re-
started the controller. Now the following files are regularly 
checked: 
– /var/log/debug
– /var/log/error
– /var/log/messages
– /var/log/syslog
– /var/log/auth.log
– /var/log/kern.log
– /var/log/user.log
– /var/log/cron.log
– /var/log/btmp
– /var/log/wtmp
If one of the files is too large, it will be moved to the 
backup. The backups are located in the same folder and 
“.1” is appended to the backup file name. This will over-
write existing backups.

<!-- page 71 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 71 / 101
29 Changes in firmware 
version 2021.0.2 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2021.0.2 LTS or 
newer.
Select the latest template for firmware version 
2021.0.0 LTS in the PLCnext Engineer project.
29.1 New functions
PROFINET
– PROFINET controller certification according to 
PROFINET specification version 2.4.1 and 
Net Load Class II.
– PROFINET device certification according to 
PROFINET specification version 2.4.1 and 
Net Load Class II.
29.2 Error corrections
The following errors have been rectified:
PROFINET
– After a restart of the device by voltage reset it could 
happen that the PROFINET controller could not estab-
lish a connection to all PROFINET devices. 
This occurred when connecting with large numbers of 
PROFINET devices.
– Minor problems were solved, which occurred when a 
superseded PROFINET controller requested to check 
the MRP configuration of the PROFINET device.
– Minor problems in the representation of device specif-
ic information via LLDP were solved.
– Sporadic link problems were solved that occurred 
with a PROFINET device which only offers 100 Mbit 
full-duplex/half-duplex.
– In combination with AXC F XT ETH 1 TX:
If autonegotiation of remote devices is deactivated, 
the default speed option of the interface is 100 Mbit 
half-duplex. 
In that case an existing PROFINET connection has not 
been aborted.
System
– Logging information into files located at “tempFS” oc-
cupied too much RAM. Consequently the 
System Watchdog restarted the controller. 
Now the following files are regularly checked: 
– /var/log/debug
– /var/log/error
– /var/log/messages
– /var/log/syslog
– /var/log/auth.log
– /var/log/kern.log 
– /var/log/user.log 
If one of the files is too large it will be moved to the 
backup. This will overwrite existing backups.
– With firmware version 2021.0 LTS a reset to 
“Default setting type 1” was not possible when exe-
cuted by pressing the reset button of the controller.
SDK/C++
The SDK related to firmware version 2021.0LTS redefines 
the “std::make_unique” function, thus creating a conflict 
when compiling existing code. 
Use the SDK related to firmware version 2021.0.2 LTS in-
stead.
Network
– In case the “dhcp” option was configured in the “in-
terfaces” configuration file, it could happen that the 
manual “DHCP Gateway” setting was overwritten.
– The Ethernet connection froze after a few minutes 
when the controller is connected to another port that 
is configured to 100 Mbit full-duplex without autone-
gotiation. 
29.3 Known limitations and errors
– Firmware update
The firmware update removes the following files so 
that the contents are lost:   
– /opt/plcnext/projects/Default/Plc/Eclr/
Default.eclr.config   
– /opt/plcnext/projects/Default/Plc/Gds/
Default.gds.config   
– /opt/plcnext/projects/Default/Plc/Meta/
Default.meta.config   
– /opt/plcnext/projects/Default/Plc/Plm/Plm.con-
fig   
– /opt/plcnext/projects/Default/Plc/Esm/
Default.esm.config   
– /opt/plcnext/projects/Default/Plc/Esm/
ServiceTask.esm.config   
– /opt/plcnext/projects/Default/Plc/Esm/
Globals.esm.config 
These files are not edited by PLCnext Engineer nor are 
they intended to be modified by the user.

<!-- page 72 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 72 / 101
– In addition, the known errors and limitations from 
firmware version 2021.0 LTS also exist in this firm-
ware version. 
See section 30.3 “Known limitations and errors” on 
page 76.
29.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
SSL
– CVE-2020-1971
SNMP
– The SNMP “Get” call of “OID .1.3.6.1.2.1.2.2.1.6.0” 
for network interface used as PROFINET controller or 
device caused the firmware to crash.

<!-- page 73 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 73 / 101
30 Changes in firmware 
version 2021.0 LTS
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2021.0 LTS.
Select the latest template for firmware version 
2021.0 LTS in the PLCnext Engineer project.
30.1 New functions
Articles
With this firmware version the following articles are sup-
ported for the first time:
– AXC F XT EXP (Order No. 1139999)
IEC 61131
– Backup and restore of GDS retain variables is 
supported.
– The priority of the Linux thread representing an ESM 
task of type “IDLE” has been increased. It is now just 
below the lowest ESM priority (15). This results in less 
jitter and faster execution of the associated program 
instances due to less interruptions. 
As a consequence the IDLE task can now interrupt the 
“Globals” task which updates system variables and 
IEC 61131-3 resource global variables that are con-
nected with I/O. To prevent this Phoenix Contact rec-
ommends to select appropriate “update tasks” in the 
PLCnext Engineer project.
WBM
– Security related product information is available via 
links in the “Help” menu in the header of the WBM and 
in the “Tip of the day” section on the start page.
– IO-Link diagnostic information is available in the 
Axioline tree view on the “Local Bus” page.
– The “System Use Notification” can be edited on the 
“User Authentication” page in the “Security” area. 
– The “System Use Notification” is displayed when log-
ging in to WBM or PLCnext Engineer.
– The HTTPS certificate can be configured on the 
“Web Services” page to avoid browser security warn-
ings.
PROFINET
The PROFINET controller and device can be enabled and 
disabled separately via configuration file.
Proficloud
“Proficloud V3 TSD service” is supported and replaces the 
“Proficloud TSD service”. Hereby the change from 
“www.proficloud.net“  to “www.proficloud.io” is neces-
sary.
OPC UA
The following topics apply to projects created with 
PLCnext Engineer 2021.0 LTS for a controller of firmware 
2021.0 LTS:
– The new security policies 
“AES 128 SHA256 RSA OAEP” and 
“AES 256 SHA256 RSA PSS” are supported. These 
policies can be selected in the OPC UA configuration.
– When the UA server checks the certificate of the con-
necting client, the “ApplicationURI” from the client's 
“ApplicationDescription” has to match to the 
“SubjectAlternateURI” in the client's certificate. This 
check is performed by default for new projects as well 
as when an older controller is replaced by a controller 
of firmware 2021.0 LTS in the PLCnext Engineer proj-
ect. 
If necessary the check can be suppressed by deacti-
vating the “Check application URI against client certif-
icate” checkbox in the OPC UA configuration in 
PLCnext Engineer.
– When the UA server is configured to use a “self-
signed” certificate, the trust store “OpcUA-configu-
rable” is used. The client certificate is checked against 
the Trust List and the Certificate Revocation List is ap-
plied. This applies to new projects as well as when an 
older controller is replaced by a controller of firmware 
2021.0 LTS in the PLCnext Engineer project. Previous 
versions used the trust store “Empty” as default and 
no client authentication was applied. If necessary the 
former default can be applied by deactivating the 
“Use the truststore for client authentication” check-
box in the OPC UA configuration in PLCnext Engineer.
– The “SubscriptionKind” can now be selected in the 
OPC UA configuration in PLCnext Engineer. The op-
tions “Direct Read”, “High Performance” and “Real 
Time” are available. “Direct Read” is set as default for 
new projects as when an older controller is replaced 
by a controller of firmware 2021.0 LTS in the 
PLCnext Engineer project.
The previous default “Real Time” can be selected if re-
quired.
PLCnext Store
Multiple controller types are supported in the app exten-
sion (“app_info.json“). 
During the installation of the app, the extension checks if 
the version of the app is suitable for the controller used.

<!-- page 74 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 74 / 101
HMI
– Trending data services in interaction with the 
PLCnext Engineer HMI trending functionality are sup-
ported.
– Multiple project languages in interaction with 
PLCnext Engineer HMI language settings are support-
ed.
Docker
For Docker support a possible co-existence of “iptables” 
and “nftables” is useful. Therefore the default firewall 
configuration has been adjusted. 
The names of the following tables and chains have been 
changed:
For compatibility with existing firewall configurations, the 
new settings also contain the old names as “deprecated-
Name”.
IO-Link
The IO-Link system integration refers to all types of IO-
Link master modules from Phoenix Contact which can be 
driven by the PLCnext controllers via PROFINET or Axio-
line:
– AXL F IOL8 2H (Order No. 1027843)
– AXL SE IOL4 (Order No. 1088132)
– AXL F IOL8 2H (Order No. 1027843)
– AXL SE IOL4 (Order No. 1088132)
– AXL E PN IOL8 DI4 M12 6M (Order No. 2701519)
– AXL E PN IOL8 DI4 M12 6P (Order No. 2701513)
– IOL MA8 PN DI8 (Order No. 1072838)
Note: A support by PLCnext Engineer is planned for ver-
sion 2021.3.
30.2 Error corrections
The following errors have been rectified:
WBM
– When displaying the network settings, an empty page 
could be displayed if a parameter could not be read. 
Now the page is displayed completely and affected 
parameters are shown as “N/A”.
– When adding a new user in the user administration, 
the entered password was not deleted if the process 
was cancelled with “Cancel”.
– When using the Internet Explorer for LDAP configura-
tion, a new LDAP server entry could not be created 
successfully.
– Spelling mistakes in various messages of the WBM 
have been corrected.
– If an INTERBUS peripheral error occurred that was re-
solved and acknowledged by the application, the 
“Local Bus (Interbus)” page was not reset and the er-
ror was still displayed.
– After downloading a PLC project, the name of the proj-
ect was not immediately displayed in the WBM. The 
page had to be refreshed in the browser by the user.
– Conflicting error messages occurred when entering in-
valid characters on the “Certificate Authentication” 
page.
IEC 61131
– The system could sporadically crash during the “Write 
and Start Project Changes” process if the 
PLCnext Engineer HMI component was reading vari-
ables at the same time. This fix has the following ef-
fects on the “Write and Start Project Changes” 
process: 
– GDS: Services respond with status 
“CurrentlyUnavailable“
– OPC UA: It is not possible to update values and 
browse variables 
– PLCnext Engineer HMI: Use replacement value 
“0“
– Exceptions in connection with managed C# code used 
in the PLC project were not handled correctly. This 
could cause the IEC 61131 runtime to stop respond-
ing. 
Now the exception is shown/listed including the call 
stack.
Old name New name
FILTER plcnext_filter
input plcnext_input
output plcnext_output
basic_filter plcnext_basic_filter
user_input plcnext_user_input
user_output plcnext_user_output

<!-- page 75 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 75 / 101
– An unexpected PLC task watchdog could occur in a 
low-priority task with a very long cycle time in connec-
tion with cold, warm and hot restart.
– When reading the eCLR error catalog with 
PLCnext Engineer, the firmware of the standard con-
troller (SIGSEGV) could sporadically crash. This sub-
sequently raised a software watchdog.
– After starting the PLC project, the system variables for 
the system time were only maintained with a delay. 
As a result, the value “0” was displayed for several cy-
cles.
– PROFINET plug alarms could not be reported via the 
function block “RECV_ALARM”.
– The cyclical call of the function block “AR_STATIS-
TIC” led to a very high system load up to the sporadic 
reduction of the PROFINET communication.
– When executing the function blocks “RDREC” and 
“WRREC” in fast succession, it could happen that the 
corresponding PROFINET AR was removed and the 
function blocks could not process any further ser-
vices. Corresponding error messages were issued.
PROFINET
– Under various project conditions, PROFINET perfor-
mance could deteriorate or unexpected connection 
failures could occur. 
Extensive PROFINET performance optimizations have 
been made to eliminate this behavior.
– When reading the PROFINET device of the controller 
via PLCnext Engineer, it could happen that the match-
ing module “I/O 512” could not be determined.
– The system variable “PNIO_CONFIG_STATUS” did 
not match the documented behavior. The corrected 
behavior now shows the value 3 after a successful 
connection setup. Bit 0 (Ready) and Bit 1 (Active) are 
set.
– No more DCP or DCERPC frames were sent after 
changing the local date or time of the controller. As a 
result, PROFINET could not function properly.
– The PROFINET controller performance was improved.
RSC
The RSC service “Write DeviceSettings” with the parame-
ter “Rtc.Date” had not considered leap years and had re-
jected corresponding settings with “OutOfRange”.
System
– When restarting the PLCnext firmware after a software 
reset, an exception could occur very sporadically. This 
meant that the firmware could not be started properly.
– Sporadically it could happen that a remoting based 
communication (such as that of PLCnext Engineer) 
could not be established if connection requests were 
already sent to the controller during the boot phase.
– During the reboot of the controller a system watchdog 
could occur very sporadically. Especially when trig-
gering the reboot via SSH terminal the current retain 
data of the PLC project could be lost.

<!-- page 76 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 76 / 101
– An SD card that was removed during operation trig-
gered a stop of the PLC project, although the support 
of an external SD card was deactivated in the WBM 
configuration.
– The status LED on the device was blinking with the 
wrong frequency in case of a removed external SD 
card. It has been corrected according to the descrip-
tion.
– Reading “Status.Memory.Usage.Percent” via RSC in-
terface was only possible with the user role “Admin”.
– If an app with temporary data was installed but not 
started and then the controller was restarted, the 
folder previously created for the app was deleted. As 
a result, the app could not access the folder after 
starting.
– The cold start event task was no longer executed 
during a cold start of the PLC project if a change was 
previously made that caused a cold start (e.g. change 
of project name).
– The basic CPU usage of the system was improved.
– The default text of the “System Use Notification” was 
improved. The “System Use Notification” is displayed 
when logging in to the controller (e.g. WBM or PLCnext 
Engineer).
– The file name of the firmware update container was 
changed. 
Now the complete firmware version is considered.
OPC UA
– With certain method calls the status “Bad” of the 
OPC UA server could occur during download changes 
of the PLC project.
– Due to an unfavorable startup sequence of the 
OPC UA component it could happen that certain 
alarms could not be detected in time.
– Browsing from a node to a child node and back did not 
work.
– When a value which shall be written to a STRING vari-
able exceeds the maximum length of this variable, 
then writing is rejected with the error code 
“Bad_OutOfRange”. 
In previous versions the UAserver truncated the value 
to the maximum length of the variable.
30.3 Known limitations and errors
– Retain variables
– If a requested warm start is not possible to exe-
cute via PLCnext Engineer, an implicit cold start is 
automatically executed. The retain variables are 
set to their initialization value.
– After a system watchdog, only a cold start can be 
performed when the controller is started. The re-
tain variables are set to their respective initializa-
tion values.
From firmware 2021.0 LTS a dedicated state of 
the retain values can be restored from a backup.
– Retain handling
With extended retain handling in the context of this 
firmware, the retain variables are reinitialized by a 
cold start when downgrading to firmware 2020.3 or 
older. A previous saving of the retain variables by the 
user is not supported with firmware 2020.6 and older. 
– Retain variable behavior in case of firmware down-
grade
If firmware 2020.0 LTS or later is downgraded to 
2019.9 or older and then upgraded again to firmware 
version 2020.0 LTS or later, a cold start is per-
formed. The retain variables are set to their initializa-
tion value.
– PLCnext CLI version
The PLCnext CLI version used must match the current 
SDK for this version. Downward compatibility cannot 
be guaranteed.
– EthernetIP
If the firewall is activated via WBM, the operation of 
EthernetIP is no longer possible.
This can be remedied by subsequently activating the 
ports:
– Incoming connections: port 44818
– Outgoing connection: port 2222
– Firmware downgrade
After downgrading the firmware, it is recommended to 
reset to “Defaultsetting type 1”. This is not necessary 
when updating the firmware.
– PROFINET PRL support
Firmware version 2021.0.0 LTS is the last version 
which supports PROFINET PRL (Phoenix Redundancy 
Layer). 
Future versions will no longer support this feature.
– Firmware startup
If the PLCnext system firmware has not started up 
properly, the WBM displays the error message 
“Bad Gateway 502”.

<!-- page 77 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 77 / 101
– Task name
If “Event”, “EventTask” or “Globals” is used as the 
name of a task, an error condition of the controller oc-
curs when the project is downloaded. 
This is because “Event”, “EventTask” and “Globals” 
are already used internally as class name.
– DHCP
DHCP can only be switched on for Ethernet adapt-
ers that are not assigned as PROFINET controllers 
or PROFINET devices. To make the settings effective 
in the network, the device must be restarted.
– Variables
The content of the variables “ESM_DATA.ESM_IN-
FOS[*].ESM_TICK_COUNT” and “ESM_DATA.ES-
M_INFOS[*].ESM_TICK_INTERVAL” is permanently 
set to 0. 
– HMI pages during program downloads
During a PLCnext Engineer program download (both 
total and changes), the web server returns an error 
503 (busy) for requests to the HMI pages.
– Multiple DataLogger Sessions
If two or more DataLogger sessions are configured to 
write to the same database, only the data of one ses-
sion will be transferred to the database on the SDcard 
at the end. The user does not receive a message that 
not all data can be saved. 
– Retain data
Using the maximum quantity structures of the retain 
data can increase the task duration of the using task. 
This can trigger a task watchdog for time-critical ap-
plications. 
– Crash during startup phase
The system watchdog is not yet active during the 
startup phase if you start C++ extensions very early. If 
the user code causes a crash during this phase, this 
can lead to an endless boot loop.
You can solve the problem by removing the SD card 
before rebooting.
– STRING variables
Access to long STRING variables outside the applica-
tion is limited to 511bytes. This concerns reading and 
writing via the RSC services “IDataAccessService” 
and “ISubScriptionService”. These services are used 
by OPC UA, PLCnext Engineer HMI and the online 
functions of PLCnext Engineer, among others.
– “Download Changes“
Sporadically a PLCnext Engineer project may reject 
“Download changes” without giving a reason.
– Uninstalling Solution Apps
When a Solution App is uninstalled by the 
PLCnext Store, it can happen that the controller then 
no longer reacts to any actions by the PLCnext Store, 
although it reports the status “online”. A system 
watchdog was also sporadically observed. This behav-
ior has not been observed when using the offline de-
activation in the WBM for uninstalling a solution app.
– LAN gateway settings
AXC F 2152 in combination with AXC F XT ETH 1TX 
extension module: If there are several 
“Default Gateway” settings, only the setting of the 
first network interface is applied. The settings of other 
LAN adapters are ignored. Only one “standard gate-
way” is supported internally.
– Local time zone setting
Setting local time zones is not fully supported.
– “DBG” LED
The “DBG” LED should signal if a variable has been set 
via forcing in debug mode in the PLC project. 
This behavior is currently not supported. Despite forc-
ing the variable, the “DBG” LED remains off.
– “Link” and “Active” LEDs
The “Link” and “Active” LEDs on the network interfac-
es “X1” and “X2” are not active when a “10BaseT” 
connection is used.
– PROFINET cycle time
The use of a PROFINET cycle time of 1 ms leads to a 
deviation of the jitter behavior required by the control-
ler certification. 
Operation in this state is possible, but not recom-
mended.

<!-- page 78 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 78 / 101
30.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
WBM
– CVE-2020-12517
System
– CVE-2020-12518
Shell
– CVE-2020-12519
LLDP
– CVE-2020-12521

<!-- page 79 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 79 / 101
31 Changes in firmware 
version 2020.6.1
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2020.6.
Select the latest template for firmware version 
2020.6.1 in the PLCnext Engineer project.
31.1 New functions
WBM
The connection to existing LDAP(S) servers can be config-
ured in WBM.
GDS
Enhanced Retain Handling:
When changes to retain variables are transferred to the 
controller via “Download All”, no implicit cold start is per-
formed. As many retain values as possible are retained. 
This behavior of the retain variables corresponds to the 
“Download Changes” behavior, where all variables are re-
tained even if the project is changed at runtime.
To avoid data inconsistencies with retain variables, the re-
tain variables are always initialized by an implicit cold start 
after a project change (project name). In the previous firm-
ware versions a warm start was only carried out if the re-
tain variables were exactly the same.
IEC 61131
– Improvement of jitter and latency for programs with 
IEC 61131 or C# context.. 
– New system variable “USER_PARTITION” to display 
the load of the user partition with the following ele-
ments: 
– MEM_TOTAL 
– MEM_FREE
– MEM_USED
– MEM_USAGE
PROFINET
Support of Fast Startup (FSU) by the PROFINET controller 
(up to 16 FSU devices).
OPC UA
– User comments on the confirmation and acknowl-
edgement of alarms via OPC UA are supported. The 
comments are also entered in the “Notification Log-
ger”.
– Basic support for loading new user-specific informa-
tion models into the OPC UA server.
DataLogger
New RSC-API “IDataLoggerService2” for application of 
the DataLogger. The triggered logic analysis in 
PLCnext Engineer is based on this API.
Network
Support of a DHCP basic functionality for IP address allo-
cation.
SDK/C++
The GCC compiler has been updated from version 8.3 to 
version 9.3. All newly created applications are now com-
piled on this basis.
PROFICLOUD
PROFICLOUD V3 basic support (firmware update from the 
cloud).
31.2 Error corrections
The following errors have been rectified:
WBM
– The call of WBM pages could sporadically lead to a 
PROFINET connection termination.
– When configuring new firewall rules in WBM, not all 
available network interfaces were displayed.
– There was no character limitation when entering user 
or password. After 64 or 128 bytes the input string 
was cut off without error message. 
– A notification field of a message was displaced in the 
“Notifications” menu when switching languages.
– Certain UTF-8 special characters could not be entered 
in the “Username” input field in the 
“User Authentication” menu.
An empty error message was displayed.
– In the “Certificate Authentication” menu, the key type 
“RSA TPM 2048” was displayed in the “Add Identity 
Store” entry by mistake.

<!-- page 80 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 80 / 101
IEC 61131 
– A “Fatal Exception” could occur if the project was to 
be restarted after debugging the project while follow-
ing a certain procedure.
– If a PLCnext Extension component (ACF or PLM) or a 
PLCnext Engineer Shared Native Library was to be 
linked against a non-existent “shared object library”, 
a crash could occur.
– From this version on, the block “RTC_S” returns the 
local time, provided a time zone with root rights has 
been set before.
In previous versions, the UTC time was always re-
turned.
DataLogger
– The project could not be loaded if an exception was 
thrown due to too many configured variables in a Dat-
aLogger session.
In this case the notification “Arp.Services.DataLog-
ger.Error” is now displayed. The project is loaded 
without starting the incorrectly configured DataLogger 
session.
– The firmware could not be accessed if the parameter 
“maxFileSize” was too large during a DataLogger ses-
sion that writes to a volatile sink.
PROFINET
– When loading projects that were created with 
PLCnext Engineer 2020.3, a notification 
“Arp.Io.PnC.ConfigurationWarning” with the severity 
“Warning” can be triggered. The PayLoadString is 
“Parsed FSParameterUUID '{}' has invalid format. Pa-
rameter will be ignored. Please check engineering 
and/or device description”.
This problem has been fixed in PLCnext Engineer 
2020.6 or later.
– The PROFINET connection setup could take a relative-
ly long time if many nodes were used.
– The PROFINET controller could only process 10 RPC 
requests at a time. So far “nca_server_too_busy” was 
reported back to the PROFINET devices. Some devic-
es did not repeat their RPC request.
The PROFINET controller can now accept up to 
45 RPC requests simultaneously.
– The controller sporadically had incorrect IP settings 
after a DCP factory reset was requested by the higher-
level PROFINET controller.
– After switching off MRP, an AXCF 2152 was no longer 
accessible as a device.
GDS
– In case of fatal error (e.g. SIGSEGV) in a C++ program, 
a system watchdog could be triggered cyclically. Un-
der certain circumstances this could also be caused 
by a faulty GDS configuration.
– When using the Write functions of the 
“IDataAccessService” RSC service, the variable could 
not be overwritten correctly if the data type of the 
overwrite value did not match the data type of the 
variable to be overwritten.
RSC
When using certain RSC services simultaneously, an ex-
ception in “CommonRemoting” or a “Protocol violation” 
ERROR could occur.
ESM
In rare cases the detected watchdog of an ESM task was 
not handled correctly. Thereupon the firmware was termi-
nated.
System
– During system startup, a system watchdog could be 
triggered if, for example, a higher-level PROFINET 
controller changed the IP settings via DCP protocol.
– With the C++ function “Directory::Clear(path)” from 
the namespace “Arp.System.Commons.Io” a directo-
ry could not be cleared as long as it was viewed with 
WinSCP.
– Names of NTP servers could not be set if they con-
tained more than 2 dots.
– Under certain operating conditions cyclic error mes-
sages were entered in conjunction with LLDP. These 
messages are not errors and were therefore reclassi-
fied as debug information.
– When setting the IP address via DCP, an error mes-
sage was erroneously entered in the “Output.log”, al-
though the setting was successful.
INTERBUS
With the AXC F 2152 in conjunction with the 
AXC F IL ADAPT extension module, the error “SYSFAIL” 
could occur when working with breakpoints. If, after work-
ing with breakpoints in a project, the program continued 
running without entering a breakpoint again, the “SYS-
FAIL” signal was not reset. Although the fieldbus contin-
ued to run, process data exchange was no longer possible.

<!-- page 81 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 81 / 101
Docker
An issue related to calling the Docker “exec” command to 
install or configure a Docker Container was fixed. So far 
only the Docker “run” command could be used.
31.3 Known limitations and errors
– Retain variables
– If a requested warm start is not possible to exe-
cute via PLCnext Engineer, an implicit cold start is 
automatically executed. The retain variables are 
set to their initialization value.
– After a system watchdog, only a cold start can be 
performed when the controller is started. The re-
tain variables are set to their respective initializa-
tion values.
– PLCnext CLI version
The PLCnext CLI version used must match the current 
SDK for this version. Downward compatibility cannot 
be guaranteed.
– EthernetIP
If the firewall is activated via WBM, the operation of 
EthernetIP is no longer possible.
This can be remedied by subsequently activating the 
ports:
– Incoming connections: port 44818
– Outgoing connection: port 2222
– DHCP
DHCP can only be switched on for Ethernet adapters 
that are not assigned as PROFINET controllers or 
PROFINET devices. To make the settings effective in 
the network, the device must be restarted. In general, 
when DHCP is switched on, the current IP settings are 
not yet displayed in the WBM and on the display, but 
the static settings last set are displayed.
– Retain handling
With extended retain handling in the context of this 
firmware, the retain variables are reinitialized by a 
cold start when downgrading to firmware 2020.3 or 
older. A previous saving of the retain variables by the 
user is currently not supported. 
– Variables
The content of the variables “ESM_DATA.ESM_IN-
FOS[*].ESM_TICK_COUNT” and “ESM_DATA.ES-
M_INFOS[*].ESM_TICK_INTERVAL” is permanently 
set to 0. 
– HMI pages during program downloads
During a PLCnext Engineer program download (both 
total and changes), the WebServer returns an error 
503 (busy) for requests to the HMI pages. 
– Multiple DataLogger Sessions
If two or more DataLogger sessions are configured to 
write to the same database, only the data of one ses-
sion will be transferred to the database on the SDcard 
at the end. The user does not receive a message that 
not all data can be saved. 
– Internal network interface
Sporadically, frequent calls of PROFINET Read or 
Write REC may cause communication to the corre-
sponding AR to be disturbed and a connection termi-
nation may occur.
– Retain data
Using the maximum quantity structures of the retain 
data can increase the task duration of the using task. 
This can trigger a task watchdog for time-critical ap-
plications. 
– STRING variables
Access to long STRING variables outside the applica-
tion is limited to 511bytes. This concerns reading and 
writing via the RSC services “IDataAccessService” 
and “ISubScriptionService”. These services are used 
by OPC UA, PLCnext Engineer HMI and the online 
functions of PLCnext Engineer, among others. 
– SDK
The SDK only works with PLCnextCLI 2020.0 or later, 
not with older versions (both PLCnext CLI 2019.x and 
PC WORX Target for Simulink 2019.x).
– If the controller is rebooted using the Linux command 
“sudo reboot” or the RSC service 
“IDeviceControlService::RestartDevice()” (also used 
by the “Reboot” button in the PLCnext Engineer cock-
pit), a system watchdog may occur in rare cases. This 
means that only a cold start is possible when the con-
troller is subsequently booted, i.e. all retain variables 
are reinitialized.
This behavior does not occur when the operating volt-
age is switched off and then booted.
– Crash during startup phase
The system watchdog is not yet active during the 
startup phase if you start C++ extensions very early. If 
the user code causes a crash during this phase, this 
can lead to an endless boot loop.
You can solve the problem by removing the SD card 
before rebooting.
– PROFINET name
If firmware 2020.6 is downgraded to an older version, 
the PROFINET name is lost.
– Debugging of IEC 61131 code
When debugging IEC 61131 code with activated

<!-- page 82 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 82 / 101
breakpoints, display errors may occur in the call se-
quence function and variable contents.
– “Download Changes“
Sporadically a PLCnext Engineer project may reject 
“Download changes” without giving a reason.
– RTC setting
After setting a local time zone, unexpected results 
may occur when reading out times from different con-
texts (RTC-S FB, OPC UA, SPNS LOG).
– Restriction for Device Info service
The “DI - Device Info - Status.Memory.Usage.Per-
cent” service no longer returns a value with the fol-
lowing roles: 
– “Engineer“
– “Commissioner“
– “Service“
– “DataViewer“
– “DataChanger“
– “Viewer“
– “UserManager” 
– Controller in error state
When using “Event” as name of a program, an error 
condition of the controller occurs when downloading 
the project. “Event” is already used internally as class 
name.
– Firmware downgrade
After downgrading the firmware, it is recommended to 
reset to “Default setting type 1”. This is not necessary 
when updating the firmware.
– Retain variable behavior with firmware downgrade
If firmware 2020.0 or later is downgraded to 2019.9 
or older and then upgraded again to firmware version 
2020.0 or later, a cold start is performed. 
The retain variables are set to their initialization value.
– Bus behavior after power failure
If an Axioline bus contains a power terminal and a 
Smart Elements module with empty slots, the bus will 
not restart after a power failure.
– AXC F 2152 with extension module AXCF XT ETH 1TX
If both network adapters are configured with the same 
“Subnet Mask”, the PROFINET controller functionality 
will not work as desired. A proper connection setup is 
not possible.
– Uninstalling Solution Apps
When a Solution App is uninstalled by the 
PLCnext Store, it can happen that the controller then 
no longer reacts to any actions by the PLCnext Store, 
although it reports the status “online”. A system 
watchdog was also sporadically observed. This behav-
ior has not been observed when using the offline de-
activation in the WBM for uninstalling a solution app.
– Task watchdog 
A task watchdog may sporadically occur with a low-
priority PLC task with a cycle time in the range of sec-
onds if the running PLC project was stopped and 
immediately restarted with a cold/warm/hot start.
– After resetting the controller there is no TrustStore 
with the name “proficloudv3”. The TrustStore is nec-
essary for the update via ProficloudV3.
Workaround: Re-create the TrustStore in the WBM of 
the controller.
– Gateway settings LAN2
AXC F 2152 in combination with AXC F XT ETH 1TX 
extension module: If there are several 
“Default Gateway” settings, only the setting of LAN1 
is used. The settings of other LAN adapters are ig-
nored.
31.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
OpenSSL
– CVE-2020-1967
Python
– CVE-2020-8492
System
– Activation of security-relevant compiler flags (e.g. to 
prevent unauthorized introduction of executable 
code).
– Correction of a problem that RSC-Services of fieldbus 
components could be used without authentication.
OpenSSL
– The outdated OpenSSL version 1.0.2 is no longer sup-
ported. Instead, the current OpenSSL version 1.1.1 is 
used.

<!-- page 83 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 83 / 101
32 Changes in firmware 
version 2020.3.1
To be able to use all new functions of the firmware, 
you need PLCnext Engineer version 2020.3.
Select the latest template for firmware version 
2020.3.1 in the PLCnext Engineer project.
32.1 New functions
System
You can now set the parameters for the NTP time server 
protocol in PLCnext Engineer.
DCP flashing
DCP flashing for PROFINET controllers/devices of the 
PLCnext Control family has been implemented.
PROFINET diagnostics
The PROFINET controller provides diagnostic information 
as function block “ARStatistik”.
New functions in WBM
– Display and download of the notification log
The notifications are displayed in the WBM on a sepa-
rate page.
– Extended Ethernet display
The WBM provides an extended display of information 
about the Ethernet configuration of all available LAN 
interfaces.
Docker
“Docker” is supported for all articles of the PLCnext family. 
Additionally the “Balena Engine” is supported. (“nftables” 
configuration, “cgroups” are mounted at boot time).
OPC UA server
– Configurable “subscription type” 
The component can now be configured using the con-
figuration file “PCWE.opcua.config”, e.g. using the 
PLCnext Engineer software.
– Support of “DateTime“
The data type “DateTime” is supported via OPC UA in 
any nesting, e.g. Structs, ArraysOf ..., Simple Var, FBs 
etc.
Linux
The packages for “rsync” for file synchronization are sup-
ported.
32.2 Error corrections
The following errors have been rectified:
– System files
System files modified with “root” access could pre-
vent proper reboot after a firmware update.
– Axioline
In conjunction with the AXC F XT IB module, the con-
tents of the diagnostic parameter registers in the sys-
tem variables were swapped.
– WBM
– Some WBM diagnostic pages were not displayed 
correctly with Internet Explorer.
– On the WBM page for network configuration, the 
name “Baud rate” was incorrect. This was 
changed to "Data rate".
– A WBM session of a logged on user was never ter-
minated if a page with cyclically updated data was 
open.
– An eHMI user could never log out completely. 
– IEC 61131
An error could occur when restoring the retain data af-
ter a reboot.
This behavior only occurred in the PLCnext Engineer 
project if program instances were moved to another 
ESM task.
– DataLogger
After a firmware update, logging into the DataLogger 
database did not work anymore if the database design 
had changed.
– RSC
Synchronous execution of RSC services without secu-
rity context was not supported and could lead to an 
unexpected error message.

<!-- page 84 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 84 / 101
32.3 Known limitations and errors
– Retain variables
– If a warm start is requested via PLCnext Engineer 
and this is not possible internally, an implicit cold 
start is automatically executed. The retain vari-
ables are set to their initialization value.
– After a system watchdog, only a cold start can be 
performed when the controller is started. The re-
tain variables are set to their initialization values.
– Special characters
When using UTF8 special characters (Unicode) for the 
user name and password, the length restriction (user 
name = 64 bytes, password = 128 bytes) can take ef-
fect, although the maximum character length was not 
used. This reason is that the number of bytes and not 
the number of characters is limited in the RSC service.
– OpenSSL
For security reasons, applications should no longer be 
linked against the outdated OpenSSL version 1.0.2.
– PLCnCLI version
The PLCnCLI version used must match the current 
SDK for this version. Backward compatibility cannot 
be guaranteed.
– GNU compiler
With the GNU compiler types GCC (8.3.0, 9.2.1) used, 
a quadratic increase in compilation time and memory 
consumption on the desktop PC is observed when 
very large structures are used.
Note this behavior if you use a large number of ports in 
PLCnext applications (e.g. connection of a very large 
number of Simulink signals).
– EthernetIP
If the firewall is activated via WBM, the operation of 
EthernetIP is no longer possible.
This can be remedied by subsequently activating the 
ports:
– Incoming connections: port 44818
– Outgoing connection: port 2222
– System variables
The system variables
ESM_DATA.ESM_INFOS[*].ESM_TICK_COUNT and 
ESM_DATA.ESM_INFOS[*].ESM_TICK_INTERVAL are 
no longer supported.
Now, the value of the variables is always 0.
– Error during program download
During a program download (both complete and mod-
ifications) in PLCnext Engineer, the WebServer returns 
error 503 (busy) for requests to the HMI pages.
– DataLogger
If two or more DataLogger sessions are configured to 
write to the same database, only the data from one 
session is transferred to the database on the SD card. 
You will not receive a message that not all data can be 
saved.
– Debugging
After debugging a PLCnext Engineer project with 
breakpoints, the project may stop after restarting.
– PROFINET connection setup
The PROFINET connection setup can take a long time 
in combination with a very large PROFINET structure.
– PROFINET Read/Write
Frequent calls of PROFINET Read or Write REC may 
disturb the communication to the corresponding AR. 
A connection termination may occur.
– Increased task duration caused by retain data
If the maximum retain data volume is used, the dura-
tion of the task may increase. A task watchdog could 
be triggered in time-critical applications.
– STRING variables
Access to long STRING variables outside the applica-
tion is limited to 511bytes. This concerns reading and 
writing via the RSC services “IDataAccessService” 
and “ISubScriptionService”.
These services are used by OPC UA, 
PLCnext Engineer-HMI and the online functions of 
PLCnext Engineer, among others.
– SDK and PLCnCLI
The SDK only works with PLCnCLI 2020.0 or later, not 
with older versions (both PLCnCLI 2019.x and 
PC Worx Target for Simulink 2019.x).
– Reboot via Linux shell
After rebooting the controller via the Linux shell, a sys-
tem watchdog may occur in rare cases. When the con-
troller is subsequently booted, only a cold start is 
possible. This initializes all retain variables.
This behavior only occurs when rebooting via the Li-
nux shell. No system watchdog was observed when 
the controller lost power.
– OpenSSL update
Updating the OpenSSL version 1.0.2 to version 1.1.1 
can lead to problems with existing C++ applications 
that are based on this and run in the same process 
(e.g. function extensions). Phoenix Contact recom-

<!-- page 85 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 85 / 101
mends paying attention to possible updates in the 
PLCnext Store.
In the event of incompatibility, the firmware may not 
start up.
– Switching off MRP
After switching off MRP, a restart of the AXC F 2152 is 
required in order for it to work properly.
– Bus behavior after power failure
If an Axioline bus contains a power terminal and a 
Smart Elements module with empty slots, the bus will 
not restart after a power failure.
– Crash during startup phase
The system watchdog is not yet active during the 
startup phase if you start C++ extensions very early. If 
the user code causes a crash during this phase, this 
can lead to an endless boot loop.
You can solve the problem with a “factory reset”.
– PROFINET name
If firmware 2020.3 is downgraded to an older version, 
the PROFINET name is lost.
– Debugging IEC 61131 code
When debugging IEC 61131 code with activated 
breakpoints, display errors may occur in the call se-
quence function and variable contents.
– “Download Changes” 
Occasionally “Download Changes” may be rejected in 
a PLCnext Engineer project without stating a reason. 
32.4 Security updates
The following security updates have been made in this re-
lease. For more information about the specified CVE num-
bers, see:
–  https://nvd.nist.gov/vuln
–  https://cert.vde.com 
Information on the Phoenix Contact “PSIRT” can be found 
at:  https://www.phoenixcontact.com/psirt 
git
– CVE-2019-19604
– CVE-2019-1387
– CVE-2019-1348 
vim
– CVE-2019-20079
sqlite3
– CVE-2019-19646
– CVE-2019-19645
– CVE-2019-16168
– CVE-2019-8457

<!-- page 86 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 86 / 101
33 Changes in firmware version 
2020.0.1 LTS
In interaction with this firmware the following points 
are not necessary:
– Update of PLCnext Engineer
– Update of SDK files for high-level language appli-
cations
33.1 Error corrections
The following problems have been fixed:
– A problem that led to cyclical connection terminations 
of the PROFINET application relationships (AR). This 
behavior occurred depending on the cycle times of the 
ESM tasks.
– A problem that caused an incorrect recovery of the 
retain data after a reboot of the controller. This behav-
ior only occurred if program instances in the PLC proj-
ect were moved to another ESM task.
– A problem that caused the controller to stop booting 
after resetting the controller to factory default type 2 
(factory default). In this state the BOOT LED flashes 
red (2 Hz). The LED D is permanently yellow.
– A problem that was possible in conjunction with 
OPC UA. Scalar data types could be written with the 
wrong data type. This could lead to incorrect data in 
the IEC project when overwriting with larger data 
types. The error code “StatusCodes.BadTypeMis-
match” would be expected here.
34 Changes in firmware version 
2020.0 LTS
If you changed system files via a “root” access, the 
controller might not start up correctly after a firm-
ware update.
– In this case, reset the controller to default setting 
type 1.
34.1 New functions
Offline installation of apps from the PLCnext Store
You can install apps downloaded from the PLCnext Store 
via the WBM of the controller without Internet connection 
and activate the corresponding licenses.
DataLogger improvements
– When configuring the DataLogger, you can specify the 
percentage of data to be deleted when the database 
reaches its maximum size (attribute “deleteRatio”).
– You can configure the data format of time and date 
(attribute “tsfmt”).
For more detailed information on configuring the Da-
taLogger, please refer to the “PLCnext Technology” 
user manual.
The user manual can be downloaded at 
phoenixcontact.net/product/2404267. 
Axioline Smart Elements
The controller supports Axioline Smart Elements.
Implementation of the “SysV IPC” Linux extension
With this extension, you can use the three IPC techniques 
(semaphore, message queue, and shared memory) of 
“SysV”.
OpenSSL update to version 1.1.1
The OpenSSL library has been updated to version 1.1.1.
Recommended:
Use version 1.1.1 of the OpenSSL library.
The older version 1.0.2 of the OpenSSL library is still 
part of the firmware for reasons of downward com-
patibility.
Docker software support
Options for support of the Docker software have been en-
abled in the Linux kernel.

<!-- page 87 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 87 / 101
34.2 Error corrections
– Task execution
Sporadically a task was not executed correctly in the 
given cycle.
This error has been rectified.
– eHMI visualization after “Download Changes” 
After downloading program changes to the controller, 
the eHMI visualization could only be used after re-
loading the page in the browser.
This error has been rectified.
– Data exchange with PROFICLOUD
If variable values from an ESM1 task and from an 
ESM2 task were to be transferred to PROFICLOUD at 
the same time, the data exchange with PROFICLOUD 
was interrupted.
This error has been rectified.
– Accessing an undefined element in the array
When accessing an undefined element within a multi-
dimensional array (“Array of Array” or “Array of 
Struct”) with OPC UA, the controller broke down.
This error has been rectified.
– Length limitation of strings
If strings with a length of more than 2993 bytes were 
created, access with OPC UA or RSC services of the 
GDS could cause the controller to break down.
This error has been rectified. As part of the error cor-
rection, the length of a string was limited to a maxi-
mum of 511 bytes.
34.3 Known limitations and errors
– Mixed operation of different OpenSSL versions
If the use of existing C++ applications (Function Ex-
tensions) results in mixed operation of the OpenSSL 
versions 1.0.2 and 1.1.1, the controller does not boot.
Recommended: If you are using an app of the type 
"Function Extension" from the PLCnext Store, check 
whether an update is already available in the PLCnext 
Store.
– Automatic cold start
If you initiate a warm start in PLCnext Engineer and 
this is not possible internally, a cold start is performed 
automatically, i.e., the retain variables are reinitial-
ized.
– Cold start after system watchdog
After a system watchdog, a cold start is performed.
– System watchdog after reboot via shell
If you restart the controller via the shell, the system 
watchdog is triggered sporadically.
– Limitation of password and username
The length of the password is limited to 64 bytes and 
the length of the user name is limited to 128 bytes. 
Note that the entered characters are UTF-8 encoded, 
i.e. one character can occupy up to four bytes (e.g. 
umlauts).
– PLCnCLI version and SDK version
The PLCnCLI version must match the current SDK ver-
sion (2020.0.0). Downward compatibility cannot be 
ensured.
– One database for several DataLogger sessions
If you configure two or more DataLogger sessions to 
write to the same database, only the data from one 
session is transferred to the database on the SD card. 
There is no message that not all of the data can be 
stored.
– STOP of the controller after debugging
After setting breakpoints in debug mode, the control-
ler can switch to the STOP state when the project is re-
started.
– PROFINET connection setup
In the case of very large PROFINET quantity struc-
tures, the PROFINET connection setup can take sev-
eral minutes.
– PROFINET connection interruptions
Frequent calls of the “Read Record” and “Write Re-
cord” function blocks can occasionally interrupt the 
PROFINET connection.
– EtherNet/IP™
If you enable the controller firewall in the WBM, 
EtherNet/IP™ is no longer available.
To be able to use EtherNet/IP™ with enabled firewall, 
you have to activate the ports for incoming and outgo-
ing connections subsequently (port 44818 and 
port 2222).
– C++ projects
C++ projects that were created using “WorkerThread” 
in SDK version 2019.0 LTS have to be compiled again 
using an SDK version ≥ 2019.3.
Otherwise, the “WorkerThread” is not loaded after re-
start of the application.
– Copying configuration files
If you use the Linux command “scp” without the op-
tion “-p” to copy configuration files from a Linux PC to 
the directory /opt/plcnext/projects on the controller, 
the file permissions are partly set incorrectly.

<!-- page 88 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 88 / 101
Remedy:
After copying the configuration files, use the Linux 
command “chmod” to set the file permissions in such 
a way that the firmware can delete the configuration 
files in case of “Download Changes” (group: “plcnext” 
, owner: “plcnext_firmware”).
– Large amount of retain data
In projects with a large amount of retain data, the PLC 
task watchdog infrequently triggers.
– Error message on HMI display
While a program or program changes are being down-
loaded to the controller, the “503 (busy)” error mes-
sage is displayed on a connected HMI display.

<!-- page 89 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 89 / 101
35 Changes in firmware version 2019.9
If you changed system files via a “root” access, the 
controller might not start up correctly after a firm-
ware update.
In this case, reset the controller to default setting 
type 1.
35.1 New functions
New function in the WBM
A diagnosis for the local bus is available in the WBM.
PROFINET System Redundancy Layer (SRL)
In operation as PROFINET controller or PROFINET device 
the controller now supports PROFINET SRL.
Forcing GDS variables
You can now force GDS variables and thus the I/Os con-
nected via PROFINET or Axioline F.
PROFINET controller: Behaviour of the BF-C LED
If you do not configure a PROFINET device or interrupt the 
connection using the "AR_MGT" function block, the BF-C 
LED remains switched off.
35.2 Error corrections
– Freezing of the outputs
A high CPU load and frequent PROFINET disconnec-
tions could cause the outputs to freeze.
This error has been rectified.
– Delay of a variable value during the start of the con-
troller
If 24 V voltage was applied to a digital input of the 
Axioline F local bus and the signal was transmitted 
with a global variable or a port link into the application, 
there could be a delay of several cycles. The error oc-
curred during the start of the controller.
This error has been rectified.
– Changing the IP address via DCP
Changing the IP address via DCP could affect the real-
time of the project and trigger the PLC task watchdog.
This error has been rectified.
– CPU load after PROFINET connection setup
After many PROFINET connections had been estab-
lished, the controller could reach 100 % CPU load and 
the firmware could no longer react.
This error has been rectified.
– Resetting the IP address via DCP
If there was a connection to at least one configured 
PROFINET participant, the PLC task watchdog could 
be triggered when the IP address was reset via DCP.
This error has been rectified.
– Setting breakpoints in debug mode
If a breakpoint was set in debug mode, the PLC task 
watchdog could be triggered.
This error has been rectified.
– Error of the Notification Logger
If an error occurred during a restart of the controller, 
the Notification Logger was not automatically config-
ured and notifications were not displayed in 
PLCnext Engineer.
This error has been rectified.
35.3 Known limitations and errors
When using SafetyBridge Technology, note the 
following:
To ensure reliable operation in conjunction with 
SafetyBridge Technology, make the following set-
tings in PLCnext Engineer.
“/ Profinet” editor group, “Interface List” editor:
Reduction ratio: 8 (or higher)
Monitor factor: 6 (or higher)
– System variables
The system variables
ESM_DATA.ESM_INFOS[*].ESM_TICK_COUNT and 
ESM_DATA.ESM_INFOS[*].ESM_TICK_INTERVAL are 
no longer supported.
Now, the value of the variables is always 0.
– Copying configuration files
If you use the Linux command “scp” without the op-
tion “-p” to copy configuration files from a Linux PC to 
the directory /opt/plcnext/projects on the controller, 
the file permissions are partly set incorrectly.
Remedy:
After copying the configuration files, use the Linux 
command “chmod” to set the file permissions in such 
a way that the firmware can delete the configuration 
files in case of “Download Changes” (group: “plcnext” 
, owner: “plcnext_firmware”).
– Deinstalling a licensed app from the PLCnext Store
The deinstallation of a licensed app via the PLCnext 
Store is not possible if you manually deleted the li-
cense from the controller beforehand.
– Large amount of retain data
In projects with a large amount of retain data, the PLC 
task watchdog infrequently triggers.

<!-- page 90 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 90 / 101
– Error message on HMI display
While a program or program changes are being down-
loaded to the controller, the "503 (busy)" error mes-
sage is displayed on a connected HMI display.
– C++ projects
C++ projects that were created using “WorkerThread” 
in SDK version 2019.0 LTS have to be compiled again 
using an SDK version ≥ 2019.3.
Otherwise, the “WorkerThread” is not loaded after re-
start of the application.
– EtherNet/IP™
If you enable the controller firewall in the WBM, 
EtherNet/IP™ is no longer available.
To be able to use EtherNet/IP™ with enabled firewall, 
you have to activate the ports for incoming and outgo-
ing connections subsequently (port 44818 and 
port 2222).

<!-- page 91 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 91 / 101
36 Changes in firmware version 
2019.0.4 LTS
When using SafetyBridge Technology, note the 
following:
To ensure reliable operation in conjunction with 
SafetyBridge Technology, make the following set-
tings in PLCnext Engineer.
“/ Profinet” editor group, “Interface List” editor:
Reduction ratio: 8 (or higher)
Monitor factor: 6 (or higher)
Firmware version 2019.0.4 LTS offers the same features 
as firmware version 2019.0 LTS, but the error described 
below has been rectified.
36.1 Error corrections
– Freezing of the outputs
A high CPU load and frequent PROFINET disconnec-
tions could cause the outputs to freeze.
This error has been rectified.
37 Changes in firmware version 
2019.6.3
When using SafetyBridge Technology, note the 
following:
To ensure reliable operation in conjunction with 
SafetyBridge Technology, make the following set-
tings in PLCnext Engineer.
“/ Profinet” editor group, “Interface List” editor:
Reduction ratio: 8 (or higher)
Monitor factor: 6 (or higher)
Firmware version 2019.6.3 offers the same features as 
firmware version 2019.6, but the error described below 
has been rectified.
37.1 Error corrections
– Freezing of the outputs
A high CPU load and frequent PROFINET disconnec-
tions could cause the outputs to freeze.
This error has been rectified.

<!-- page 92 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 92 / 101
38 Changes in firmware version 2019.6
If you changed system files via a “root” access, the 
controller might not start up correctly after a firm-
ware update.
In this case, reset the controller to default setting 
type 1.
38.1 New functions
PROFINET stack
The PROFINET controller/device stack was updated from 
version 6.2 to version 6.3:
– MRP Client function
– SRL S2 function
MRP (Media Redundancy Protocol)
You can use the controller as a Media Redundancy Client 
(MRC) in an MRP ring. The MRC is activated and configured 
via the higher-level controller and PDEV objects.
Only the default domain 0xFFFFFFFF is supported.
DataLogger
The DataLogger transfers real-time date from the GDS 
(Global Data Space) to an SQL based database for record-
ing and storage.
The scope of functions of the DataLogger was extended:
– New recording modes:
– Storage in case of changes
– Continuous
– Historical data can be called within a defined period of 
time.
For more detailed information on the DataLogger, 
please refer to the “PLCnext Technology” user man-
ual.
Updating Axioline F I/O data
The behavior for updates of Axioline F I/O data was 
changed:
If you do not select a trigger task, the firmware automati-
cally calculates an interval for updating the Axioline F I/O 
data from the interval times of all available cyclic tasks. 
Event or idle tasks are not taken into account for the calcu-
lation. If no cyclic task is available, the data of the 
Axioline F modules is updated every 500 µs.
As an alternative to a cyclic task, you can select an idle 
task for updating Axioline F I/O data.
Interval times for cyclic tasks
The interval time of a cyclic task now has to be at least 
1 ms.
For projects that were created using an earlier firmware 
version and contain cyclic tasks with interval times <1 ms, 
the PLC task watchdog might trigger.
TON_R_LTIME, TP_R_LTIME and TOF_R_LTIME 
function blocks
The time accuracy of the TON_R_LTIME, TP_R_LTIME and 
TOF_R_LTIME function blocks was improved. Now, also 
times < 1 ms can be recorded.
To be able to use the improved time accuracy of the func-
tion blocks in existing projects, you have to compile the 
project again and transfer it to the controller.
New functions in the WBM
– On the “Profinet” page, the PROFINET topology is dis-
played in tree view.
– You can activate the support of an external SD card via 
the WBM.
If you deactivate the support of an SD card, and the SD 
card is then inserted into the controller, the SD card is 
not recognized during the initialization phase of the 
controller. Therefore, the data from the internal pa-
rameterization memory is not automatically copied to 
the SD card.
– The name of the PLCnext Engineer project running on 
the controller is displayed.
– On the “License Management” page, you can view the 
licenses of the apps from the PLCnext Store that are 
installed on the controller.
OPC UA Historical Access (HA)
The integrated OPC UA server (eUA) supports access to 
historical data (OPC UA Historical Access Specification).

<!-- page 93 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 93 / 101
PROFINET controller/device function
– Now, you can select if an application relation (AR) is to 
be established while the boot project is being loaded.
– The DNS names of the PROFINET controller and the 
PROFINET devices can now be set via the 
“IConfigurationService” RSC service.
Via the RSC interface, the functions Read(), Write(), 
GetControllerName() und GetDeviceNames() are now 
available.
For more detailed information on RSC (Remote Ser-
vice Calls), please refer to the “PLCnextTechnology” 
user manual.
38.2 Error corrections
– HTTPS connection
After 20 minutes, the connection of an HTTPS client to 
the HTTPS server used to be disconnected automati-
cally.
This error has been rectified.
– Static_String array in C++ programs
In an array of the type Static_String (C++), the array 
size was miscalculated.
This error has been rectified.
– Disconnection from the HMI web server
After the DISABLE system variable of the
HMI_CONTROL data structure was set to TRUE, and 
this way, the connection to the HMI web server was 
set, the PLCnext Engineer HMI web server and the cli-
ent were able to connect nevertheless.
This error has been rectified.
– Controller breakdown in the PROFINET network
If in a larger PROFINET network, the IP address of a 
PROFINET device was changed, the controller used to 
break down.
This error has been rectified.
– PROFINET diagnostic state in the WBM
If the application relation (AR) of a PROFINET device 
was disabled, a wrong diagnostic state was displayed 
on the “Profinet” page in the WBM.
This error has been rectified.
– AXC F 2152 as a PROFINET device
The AXC F 2152 could not be operated as a PROFINET 
device under PROFINET controllers from third-party 
manufacturers.
This error has been rectified.
– SINT type process data elements
Linking SINT type process data elements led to a run-
time error in the application program (LED FAIL).
This error has been rectified.
– Reading out OPC UA subscriptions
Reading out OPCUA subscriptions via the “UAExpert” 
tool was not possible.
This error has been rectified.
– OPC UA: “IecTime” data type variables
“IecTime” data type variables were not displayed cor-
rectly.
This error has been rectified.
– OPC UA: Index based monitoring
Independent of the index set, all data of an array was 
output during index based monitoring.
This error has been rectified.
– OPC UA: Index calculation
Access to an array of the data type StaticString result-
ed in errors in index calculation.
This error has been rectified.
– Traces in the format YYYYMMDD
For traces in the format YYYYMMDD, sometimes the 
leading 0 was missing for the day.
This error has been rectified.
– Setting breakpoints
Setting breakpoints in extensive ST code worksheets 
resulted in controller freezing.
This error has been rectified.
– Event task “Cold Start” 
In the following cases, the event task “Cold Start” was 
not executed:
– After resetting the controller to default setting 
type 1 or 2
– After SFTP transmission of the project and subse-
quent reboot of the controller
This error has been rectified.
– Installed apps from the PLCnext store
Resetting the controller to default setting type 1 or 2 
resulted in licensing conflicts for apps from the 
PLCnext store that were installed on the controller.
This error has been rectified.

<!-- page 94 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 94 / 101
38.3 Known limitations and errors
– System variables
The system variables
ESM_DATA.ESM_INFOS[*].ESM_TICK_COUNT and 
ESM_DATA.ESM_INFOS[*].ESM_TICK_INTERVAL are 
no longer supported.
Now, the value of the variables is always 0.
– C++ projects
C++ projects that were created using “WorkerThread” 
in SDK version 2019.0 LTS have to be compiled again 
using an SDK version ≥ 2019.3.
Otherwise, the “WorkerThread” is not loaded after re-
start of the application.
– EtherNet/IP™
If you enable the controller firewall in the WBM, 
EtherNet/IP™ is no longer available.
To be able to use EtherNet/IP™ with enabled firewall, 
you have to activate the ports for incoming and outgo-
ing connections subsequently (port 44818 and 
port 2222).
– HMI applications
You cannot access an HMI application while a 
PLCnext Engineer project is downloaded to the con-
troller.
In this case, an error message is displayed in the web 
browser.
– Copying configuration files
If you use the Linux command “scp” without the op-
tion “-p” to copy configuration files from a Linux PC to 
the directory /opt/plcnext/projects on the controller, 
the file permissions are partly set incorrectly.
Remedy:
After copying the configuration files, use the Linux 
command “chmod” to set the file permissions in such 
a way that the firmware can delete the configuration 
files in case of “Download Changes” (group: “plcnext” 
, owner: “plcnext_firmware”).
– Deinstalling a licensed app from the PLCnext Store
The deinstallation of a licensed app via the PLCnext 
Store is not possible if you manually deleted the li-
cense from the controller beforehand.
– Availability of network services
In case of frequent and fast linkUp and linkDown in 
large PROFINET quantity structures, the controller 
can infrequently reach 100% CPU load. In this case, 
network services are no longer available.
– Restart of a project
For projects with extremely long task cycle times (e.g., 
15000 ms), the restart of the project after a project 
download can take several minutes.
– Setting network settings via DCP
Setting network settings via DCP can affect the real-
time of the project. For watchdog times < 10 ms, this 
can infrequently result in a triggering of the PLC task 
watchdog.
– SafetyBridge Technology
Reliable operation in conjunction with SafetyBridge 
Technology is not ensured.
If you want to use SafetyBridge Technology, use the 
controller with firmware version 2019.3.

<!-- page 95 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 95 / 101
39 Changes in firmware version 2019.3
39.1 New functions
PRL (Phoenix Redundancy Layer)
The PROFINET device functionality has been extended to 
include the PRL function (Phoenix Redundancy Layer).
EtherNet/IP™ device function
You can use the controller as an EtherNet/IP™ device.
Dynamic bus configuration
The controller supports the dynamic bus configuration of 
the Axioline F local bus.
Left-alignable INTERBUS master
The controller now supports left-alignment of the 
INTERBUS AXC F XT IB master (Order No. 2403018).
PLCnext Store: New app types
The controller supports the execution of the app types 
“function extension” , “runtime” , “library” , and “solution 
app” .
39.2 Known limitations and errors
– Static_String array in C++ programs
The array sizes are incorrectly calculated in 
Static_String-type arrays (C++), meaning that access 
to the second element contained in the array and to 
those following is incorrect.
String arrays in IEC 61131 programs are not affected 
by this.
– AXC F 2152 as a PROFINET device
The AXC F 2152 cannot be operated as a PROFINET 
device under PROFINET controllers from third-party 
manufacturers.
– Monitor time of PROFINET data
The PROFINET data monitor time must be at least 
24 ms. The monitor time is the product of “Reduction 
ratio” and “Monitor factor” (in PLCnext Engineer: 
“Profinet” editor group, “Interface list” editor).
Figure 1 Monitor time
– Metrics that can be transferred to the PROFICLOUD
You can transfer up to 194 variable values as metrics 
into the PROFICLOUD.
– Very high CPU utilization
The online connection to PLCnext Engineer may be in-
terrupted when the controller CPU utilization is very 
high.
The connection interruption is indicated in 
PLCnext Engineer without any indication of the cause.
– Setting breakpoints is not supported
Setting breakpoints in debug mode results in the con-
troller becoming unreachable.

<!-- page 96 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 96 / 101
40 Changes in firmware version 
2019.0 LTS
Please note:
Updating to firmware version 2019.0 LTS will reset 
the controller to factory default setting type 1. Any 
application-specific data and projects on the con-
troller will be deleted.
40.1 New functions
Download changes
The controller now supports the “Download Changes” 
function. With the “Download Changes” function, program 
changes can be transferred to the controller during opera-
tion without interruption.
This is subject to the following conditions:
– You have not made any changes to the bus configura-
tion.
– You have not changed the process data assignment.
– You have not changed the properties of the existing 
tasks (e.g., task type, interval, watchdog).
– You have not deleted any tasks or added any new 
tasks.
Left-alignment of Axioline F extension modules
The controller now supports left-alignment of the 
Axioline F AXC F XT ETH 1TX extension module 
(left-alignable Ethernet interface, Order No. 2403115).
New functions in the WBM
New functions are now available in the web-based man-
agement (WBM), e.g., PROFINET diagnostics and firewall 
configuration.
Declaring retentive data
You can now also declare variables from C++ programs as 
retentive data in PLCnext Engineer.
Updating Axioline F I/O data
You can now specify the refresh interval for Axioline F I/O 
data. This is done by selecting which task triggers the 
Axioline F I/O data update in the PLCnext Engineer project.
To do this, proceed as follows:
• Double-click on the “Axioline F (x)” node in the 
“PLANT” area.
The “/ Axioline F” controller editor group opens.
• Select the “Trigger task” view in the “Settings” editor.
• In the drop-down list, select the task that is to trigger 
the Axioline F I/O data update.
Figure 2 Select Trigger task
If you do not select a task, the update will occur by default 
every 50 ms.

<!-- page 97 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 97 / 101
40.2 Known limitations and errors
– AXC F 2152 as a PROFINET device
The AXC F 2152 cannot be operated as a PROFINET 
device under PROFINET controllers from third-party 
manufacturers.
– Downloading PC Worx Engineer projects to the 
controller
You can only download PLCnext Engineer projects to 
the controller with firmware version 2019.0 LTS that 
were created and compiled in PLCnext Engineer ver-
sion 2019.0 LTS. Projects that you created in 
PC Worx Engineer must be re-created in 
PLCnext Engineer.
If you download a PC Worx Engineer project to the 
controller with firmware version 2019.0 LTS, the proj-
ect will not run on the controller. However, no error 
message is displayed in PLCnext Engineer. 
Please note:
The PC Worx Engineer software has been renamed 
to PLCnext Engineer:
Name up to Version 7.2.3: PC Worx Engineer
Name starting from Version 2019.0 LTS: 
PLCnext Engineer
– Monitor time of PROFINET data
The PROFINET data monitor time must be at least 
24 ms. The monitor time is the product of “Reduction 
ratio” and “Monitor factor” (in PLCnext Engineer: 
“Profinet” editor group, “Interface list” editor).
Figure 3 Monitor time
– Metrics that can be transferred to the PROFICLOUD
You can transfer up to 194 variable values as metrics 
into the PROFICLOUD.
– Exceeding CPU system limits
Exceeding the CPU system limits for the controller 
may result in an interruption of the online connection 
to PLCnext Engineer.
The connection interruption is indicated in 
PLCnext Engineer without any indication of the cause.
– Setting breakpoints is not supported
Setting breakpoints in debug mode results in the con-
troller becoming unreachable.

<!-- page 98 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 98 / 101
41 Changes in firmware version 1.2.0
41.1 New functions
Design of a PLCnext Inline station
As an alternative to an Axioline F station, you can now set 
up a PLCnext Inline station using the controller. To do so, 
you need the AXC F IL ADAPT Inline adapter terminal (Or-
der No. 1020304). You can directly install the Inline mod-
ules in series on the adapter terminal.
License verification
When an SD card is used, the controller now verifies if the 
SD card contains a Phoenix Contact license. You can only 
use the controller together with an appropriate 
Phoenix Contact SD card.
41.2 Notes on firmware downgrades and resetting 
the controller
For performing firmware downgrades, please note 
the following:
Downgrade to a firmware version  1.0.2
After downgrading to a firmware version  1.0.2, you can 
only use the controller with an SD card. Using it without an 
SD card is possible starting from firmware version 1.1.0.
– Ensure that the SD card has been inserted before 
switching the controller on, in order that the controller 
can use it.
– Only use an SD card provided by Phoenix Contact.
Downgrade to firmware version 1.0.0
After downgrading to firmware version1.0.0, you can only 
use the reset button of the controller while an application 
is running.
Resetting the controller to default setting type 2 is not 
possible.
For resetting the controller to default setting 
type 2, please note the following:
When restoring to default setting type 2, the firmware of 
the controller is also reset to the delivery state. Controllers 
with a firmware version  1.0.2 can only be used with an 
SD card. Using them without an SD card is possible starting 
from firmware version 1.1.0.
– Ensure that the SD card has been inserted before 
switching the controller on, in order that the controller 
can use it.
– Only use an SD card provided by Phoenix Contact.
41.3 Known limitations and errors
– Time-outs during the communication with PCP devic-
es
If more than eight PCP devices are connected at the 
same time, time-outs can occur during the communi-
cation between the controller and the PCP devices.
– Maximum permissible number of Axioline F local bus 
devices
Currently, a maximum of 30 Axioline F local bus devic-
es is supported.
– Interrupting the PROFINET communication
When transmitting files via SFTP to the controller, the 
PROFINET communication is interrupted.
– Function of the reset button
When the controller is reset to default setting type 2, 
all LEDs light up after approx. 30 s.
To actually restore the controller to default setting 
type 2, you need to press and hold the reset button for 
another 2 s after all LEDs have lit up.

<!-- page 99 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 99 / 101
42 Changes in firmware version 1.1.0
Please note:
After the update to firmware version 1.1.0, the con-
troller has to be restarted.
42.1 New functions
Use of SD card now optional
The SD card is now optional and is no longer mandatory for 
operating the controller.
– Operation without SD card:
All data is saved on the internal parameterization 
memory. If you make changes to files and directories 
on the internal parameterization memory, the Linux 
operating system generates an overlay filesystem 
from the changed files and directories.
– Operation with SD card:
If you use an SD card, all application-specific data 
(e.g. network configuration, project bus configuration, 
etc.) is saved to the SD card.
Two cases of SD card use can be distinguished:
1) There is no overlay filesystem on the SD card:
If there is an overlay filesystem on the internal pa-
rameterization memory, it is copied to the SD 
card.
2) There already is an overlay filesystem on the SD 
card:
If there is an overlay filesystem on the internal pa-
rameterization memory, it is not copied to the SD 
card.
The controller accesses the overlay filesystem on 
the SD card. The overlay filesystem on the internal 
parameterization memory is deleted.
Please note:
The SD card is recognized during initialization of the 
controller. If you insert the SD card during operation, 
the SD card will not be detected.
Make sure that the SD card has been inserted before 
you switch on the controller.
Memory expanded
– The program memory of the controller has been ex-
panded from 4 MB to 8 MB.
– The data memory of the controller has been expanded 
from 8 MB to 16 MB.

<!-- page 100 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 Phoenix Contact 100 / 101
43 Changes in firmware version 1.0.2
Please note:
After an update from firmware version 1.0.0 to firmware 
version 1.0.2, high-level language programs created with 
the Phoenix Contact SDK version 1.0.0 will no longer be 
executable. In this case, proceed as follows:
• Download the latest version of the Phoenix Contact 
SDK from phoenixcontact.net/products and install it.
• Compile existing high-level language programs with 
the latest version of the Phoenix Contact SDK.
When updating from firmware version 1.0.1 to firmware 
version 1.0.2, this procedure is not necessary.
43.1 Error corrections
– PROFINET configuration
The controller was stopped when transmitting a 
PC Worx Engineer project with a faulty PROFINET 
configuration to the controller.
This error has been rectified.
43.2 Known limitations and errors
– Controller breakdown
In some rare cases the controller may break down. In 
case of a controller breakdown, power is disconnect-
ed to the I/O modules contained in the bus configura-
tion.

<!-- page 101 -->

AXC F 2152 – CHANGE NOTES
108427_en_51 101 / 101Phoenix Contact GmbH & Co. KG • Flachsmarktstraße 8 • 32825 Blomberg • Germany
phoenixcontact.com
44 Changes in firmware version 1.0.1
Please note:
After an update from firmware version 1.0.0 to firmware 
version 1.0.1, high-level language programs created with 
the Phoenix Contact SDK version 1.0.0 will no longer be 
executable. In this case, proceed as follows:
• Download the latest version of the Phoenix Contact 
SDK from phoenixcontact.net/products and install it.
Compile existing high-level language programs with the 
latest version of the Phoenix Contact SDK.
44.1 Error corrections
– Task processing time
The programmed maximum task processing time was 
exceeded by occasional task processing time outliers. 
The ESM watchdog was triggered.
This error has been rectified.
– User authentication
A user authentication security vulnerability was 
patched.
– Requested memory
An error occurred when memory was requested from 
a C++ program. The requested memory was not re-
leased again.
This error has been rectified.
– Data Access Service
An error in the Data Access Service (online view in the 
“Data List” editor in PC Worx Engineer) has been rec-
tified.
– Subscription service
During data query via OPC UA, an error occasionally 
occurred in the subscription service.
This error has been rectified.

