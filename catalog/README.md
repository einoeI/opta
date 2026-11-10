# catalog/

Hand-maintained data the tool reads. Plain CSV/YAML, every row cites its source.

| File | What it is |
|---|---|
| `components.csv` | Components for the `otpa components --pick` picker, with CPE and the services they listen on. |
| `ot-ports.csv` | OT/ICS ports, generic and vendor lists. Run `python3 core/legacy/ot_ports.py --selftest` after editing. |

## ot-ports.csv

One row per port (or port range) and transport. The same port can appear more than once: once as a generic protocol and once in a vendor's own list.

| Column | Meaning | Example |
|---|---|---|
| `port` | First (or only) port number, 1-65535. | `34962` |
| `port_end` | Last port of a range; empty for a single port. | `34964` |
| `transport` | `tcp`, `udp`, `tcp/udp` or `udp/tcp` (first one listed is the usual one). | `tcp` |
| `service` | Short service name: the IANA name where one exists, otherwise the nmap or vendor name. | `mbap` |
| `description` | What runs there, plus caveats such as "IANA registers this port to an unrelated service". | `Modbus TCP (Modbus Application Protocol)` |
| `vendor` | Vendor, standards body or protocol family. | `ODVA` |
| `scope` | `generic` = applies to any OT network; `plcnext` = from the Phoenix Contact PLCnext port list. | `plcnext` |
| `state` | Vendor rows only: `standard` (open in the PLCnext Security Profile by default) or `activatable` (opens when the component is switched on). Empty for generic rows. | `activatable` |
| `nse_scripts` | Nmap / Digital Bond Redpoint scripts that probe this port, written `tool:script(categories)`, separated by `;`. Categories are the script's own NSE categories; `intrusive` means testbed-only under the project's safety policy. | `nmap:modbus-discover(discovery,intrusive)` |
| `source` | Which source(s) the row comes from. | `IANA registry + nmap/Redpoint portrules` |
| `source_url` | Link to the primary source. | IANA CSV, nmap script, vendor page |
| `accessed` | Date the source was read (YYYY-MM-DD). | `2026-11-10` |

Sources are described in `knowledge/knowledge-base/frameworks/iana-service-port-registry.md`, `knowledge/knowledge-base/tools/nmap-ics-nse-scripts.md`, `knowledge/knowledge-base/tools/digitalbond-redpoint.md` and `knowledge/knowledge-base/phoenix-contact/plcnext-port-list.md`. A port number alone never proves the protocol: confirm by passive capture or a protocol-aware probe.

## components.csv

One row per component. `otpa components --pick NAME@VERSION` matches `name` or an alias; SBOM components are matched by CPE or name to get `service` and `ports`.

| Column | Meaning | Example |
|---|---|---|
| `name` | Short lowercase name, used in `cves.csv`. | `openssh` |
| `aliases` | Other spellings (vendor change notes, SBOMs), separated by `;`. | `kernel;linux` |
| `cpe` | CPE `vendor:product`, checked to exist in the NVD CPE dictionary. | `openbsd:openssh` |
| `purl` | Package URL without version, only where OSV.dev can query it (not for plain C libraries). | `pkg:pypi/jinja2` |
| `service` | nmap service names this component serves, separated by `;`. Empty for libraries. | `ssh` |
| `ports` | Well-known default ports (IANA), `port/transport`, separated by `;`. | `22/tcp` |
| `source_url` | NVD CPE API query that confirms the CPE. | |
| `accessed` | Date checked. | `2026-11-10` |
