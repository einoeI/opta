---
title: "OWASP IoT Security Testing Guide (ISTG)"
url: "https://github.com/OWASP/owasp-istg"
type: standard
trust: primary
accessed: 2026-11-09
published: 2024-06-01
owasp_ot: [2,5,10]
version: "ISTG v1.0.1 (latest GitHub release); main branch at c7602460d2, 2026-08-02"
license: "CC BY-SA 4.0"
---

## Summary
A penetration testing methodology for IoT devices built on a device model, an attacker model and a test case catalogue.
Project page: https://owasp.org/projects/iot-security-testing-guide (OWASP Incubator project).
It is designed to supplement existing pentest workflows and is applicable to embedded controllers at component level.
`published` is the v1.0.1 release date; the checklists on the main branch have been updated since.

## Key facts
- OWASP lists it as an incubator project, with leaders Aaron Guzman and Luca Pascal Rotsch.
- Latest GitHub release is v1.0.1 (2024-06-01); v1.0.0 was 2024-03-01. The latest main-branch commit is c7602460d2, 2026-08-02, "Update checklists".
- Test case catalogue components: Processing Units (ISTG-PROC), Memory (ISTG-MEM), Firmware (ISTG-FW, with Installed Firmware and Update Mechanism specialisations), Data Exchange Services (ISTG-DES), Internal Interfaces (ISTG-INT, with I2C and UART), Physical Interfaces (ISTG-PHY), Wireless Interfaces (ISTG-WRLS), User Interfaces (ISTG-UI).
- Concepts, models and test steps are based on a master's thesis by Luca Pascal Rotsch; test cases derive from WSTG, FSTM, MSTG and published IoT hacking books.
- The methodology integrates with existing workflows; the documentation demonstrates integration with the BSI penetration testing model without workflow changes.
- Test cases form a hierarchy (component, optional specialisation, category, test case) with identifiers such as ISTG-FW-INFO-001, which can be cited in reports.

## Verbatim
- "serves as a supplement, which can be used with pre-existing penetration testing workflows and frameworks"

## Relevance
- Inference: the identifier scheme and component model could structure firmware and hardware test items in a device profile.
- Inference: the sections read contain no OT availability or process-safety controls; test cases need OT gating before use against a live controller. Only the README and the methodology chapter's first 70 lines were read.
