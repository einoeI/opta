---
title: "Security checklist (PLCnext Technology devices)"
url: "https://security.plcnext.help/se/Security_checklist.htm"
type: vendor-doc
trust: primary
accessed: 2026-11-09
published: 2026-08-17
owasp_ot: [3,5,6,9,10]
version: "Revision 024"
---

## Summary
Phoenix Contact's checklist of required configuration steps for secure operation of PLCnext Technology devices. It has four sections: initial setup, environmental requirements, account management and controller-specific settings. It is a configuration checklist; it states no port numbers and no firmware versions. It does name the system services an operator may enable, which makes it a useful cross-check on the port list.

## Key facts
- The page was published/reviewed 2026-08-17 at Revision 024.
- It applies to "PLCnext Technology devices" generally; it is not specific to the AXC F 2152 or to any firmware release.
- Named system services: HMI, PROFINET, OPC UA, Modbus TCP, PLCnext Store, Proficloud.
- Services are to be enabled only as required, restricted to required use cases, and risk-assessed per service before activation.
- User setup: create initial users, assign roles (examples: SecurityEngineer, Engineer, Operator), and do not use default credentials in productive operation.
- TLS: configure TLS, generate the HTTPS certificate in the WBM, install or accept it in the client browser.
- Basic hardening: SD card settings and encryption, basic firewall settings, netload limiter. Extended firewall settings are a separate environmental step.
- Logging: security logging, plus central logging as an environmental requirement.
- Software: define a software update configuration, install signed apps, risk-assess each app before installation.
- Backup: configure a backup mechanism and verify backup and restore procedures.
- Accounts: password complexity and validity rules, authentication error handling, session behavior, optional Active Directory/LDAP connection.
- Controller-specific: check PLCnext Control-specific settings, physical access protections, plan periodic security maintenance.

## Verbatim
- "This checklist summarizes the required configuration steps for the secure operation of PLCnext Technology devices."
- "Required system services are enabled (e.g. HMI, PROFINET, OPC UA, Modbus TCP, PLCnext Store, Proficloud)"
- "For each system service, a risk assessment has been proceeded before activation"
- "Default credentials are not used for productive operation"

## Relevance
Source for hardening checks in the check catalog (OWASP OT #5, #10). Establishes Modbus TCP as a service that exists on these devices, although the port list omits it (see `plcnext-port-list`). Inference: PLCnext Store, Proficloud and app installation are attack-surface items absent from the current device profile.
