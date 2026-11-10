---
title: "Remote maintenance in industrial environments (BSI-CS 108)"
url: "https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/Download/download.html"
type: standard
trust: primary
accessed: 2026-11-10
published: 2015-01-12
owasp_ot: [1, 5, 7]
version: "BSI-CS 108, Version 1.00 – 12/01/2015"
local_file: "sources/bsi-germany/BSI-CS_RemoteMainrenance.pdf"
---

# BSI-CS 108: Remote maintenance in industrial environments

## Summary
Three-page BSI recommendation giving generic, state-of-the-art requirements for industrial remote maintenance solutions: architecture, secure communication, authentication and organisational requirements. It explicitly states that analogue/ISDN modem access and direct Internet connection of PLCs do not meet the state of the art. Read from the user's local PDF.

## Key facts
- Architecture (p.1): one consistent solution; remote maintenance component in a separate zone (DMZ), never bypassing firewalls; fine-grained access per IP and port rather than per network (e.g. 1:1 SSH instead of coupling networks via IPsec); connections initiated outbound from the company, or temporarily activated with secure authentication and a deactivation process; dedicated systems only.
- Secure communication (p.2): established protocols only (IPsec, SSH, TLS, current versions); AES with at least 196-bit keys recommended because of long service life (as written in the source; 192/256 are the standard AES sizes).
- Authentication (p.2): one user per account, no group accounts; two-factor preferred; enforceable password policy; detect brute force, but lock out only after about 20 failed attempts instead of three, because of availability and safety.
- Organisational (p.2-3): formal risk analysis, minimalism with documented business justification, processes for activation/deactivation.
- Read-only remote access (status, measured values) can use a push-only decoupling (e.g. a web or FTP server fed from the ICS network) rather than a maintenance channel (p.3).

## Verbatim
- "It is explicitly pointed out that established solutions on the basis of analogue or ISDN modems as well as the direct Internet connection of components such as programmable logic controllers (PLCs) do not comply with the state of the art." (p.1)
- "Unlike in conventional IT, such blocking, however, must be performed for example only after 20 instead of already after three failed attempts with regard to the special requirements in terms of availability and safety." (p.2)

## Relevance
Gives concrete, checkable criteria for the remote-access conduit (OWASP OT #1 unmanaged external access, #5 access control, #7 zones and conduits). The lockout threshold note matters for credential testing: brute-force checks against OT remote access can lock out operators. Dated 2015 (crypto references are old); cite with that caveat.
