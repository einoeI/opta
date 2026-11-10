# OT/ICS source scouting map and routine (verified 2026-11-10)

How verification was done: every URL below was fetched with curl on 2026-11-10 (HTTP status, content type, newest item date). "Feed OK" means HTTP 200, a parseable RSS/Atom body, and items dated 2025 or 2026. The newest item date found is given as "last item". Verified feeds are in `ot-feeds.opml` in this folder (57 outlines, XML checked). Value for this project: **H** = check every week, **M** = check every month, **L** = only when needed.

Legend per entry: what it is for | how often it publishes (from feed dates) | cost | trust | feed | value.

## 1. Advisories and machine-readable feeds

### Takeaway
Advisories are the highest-value, lowest-effort category. All of them are free and primary, and most have working RSS. For the AXC F 2152, the essential feeds are CERT@VDE (Phoenix Contact and CODESYS vendor feeds) and the CISA ICS feed. Schneider and Rockwell have no RSS that could be verified, but their advisories also appear in the CISA ICS feed.

### Cited Findings
- **CISA ICS Advisories**: the US government's ICS advisory stream, covering all vendors | several per week (last item 2026-11-03) | free | primary | Feed OK `https://www.cisa.gov/cybersecurity-advisories/ics-advisories.xml` (6 MB file) | **H** — [feed](https://www.cisa.gov/cybersecurity-advisories/ics-advisories.xml)
- CISA ICS Medical Advisories: feed OK, last item 2026-10-21 | **L** — [feed](https://www.cisa.gov/cybersecurity-advisories/ics-medical-advisories.xml)
- **cisagov/CSAF** on GitHub: the CSAF JSON versions of the CISA ICS advisories | commits every few days (last 2026-11-06) | free | primary | Atom OK `https://github.com/cisagov/CSAF/commits/develop.atom` | **M** (for automation) — [repo feed](https://github.com/cisagov/CSAF/commits/develop.atom)
- **CERT@VDE**: German coordinating CERT for automation vendors (Phoenix Contact, WAGO, Beckhoff, CODESYS and others) | weekly (all-vendor feed last item 2026-11-06) | free | primary | feeds OK: all advisories `https://certvde.com/de/advisories/feeds/rss/`; Phoenix Contact `.../vendor/phoenixcontact/feeds/rss/` (last item 2026-11-04); CODESYS (2026-10-22); WAGO (2026-11-06); Beckhoff (2026-02-12) | **H** — [all](https://certvde.com/de/advisories/feeds/rss/), [phoenixcontact](https://certvde.com/de/advisories/vendor/phoenixcontact/feeds/rss/)
- The CERT@VDE bulletins feed is alive (last item 2026-11-06) but the file is about 18 MB, so it is left out of the OPML. The CERT@VDE blog feed's newest item is 2024-01-22, so it counts as dead. — [bulletins](https://certvde.com/de/bulletins/feeds/rss/), [blog](https://certvde.com/de/blog/feeds/rss/)
- Phoenix Contact CSAF provider metadata is hosted by CERT@VDE (JSON, HTTP 200). The PSIRT page `https://www.phoenixcontact.com/psirt` is live (HTTP 200) and has no feed of its own. CERT@VDE is the channel for its advisories. — [CSAF metadata](https://phoenixcontact.csaf-tp.certvde.com/.well-known/csaf/provider-metadata.json), [PSIRT](https://www.phoenixcontact.com/psirt)
- **BSI / CERT-Bund WID**: German Warn- und Informationsdienst, mostly IT products with some OT | daily (last item 2026-11-10) | free | primary | feed OK `https://wid.cert-bund.de/content/public/securityAdvisory/rss` | **M** (high volume, so filter by keyword) — [feed](https://wid.cert-bund.de/content/public/securityAdvisory/rss)
- BSI Cyber-Sicherheitswarnungen (CSW): feed OK, last item 2026-11-06 | **M**. The BSI list of feeds is at `DE/Service-Navi/Abonnements/RSS/rss_node.html`. The older `RSSNewsfeed.xml` and `RSSNewsfeed_WID.xml` paths return 404. — [CSW feed](https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed/RSSNewsfeed_CSW.xml), [BSI feed list](https://www.bsi.bund.de/DE/Service-Navi/Abonnements/RSS/rss_node.html)
- **Siemens ProductCERT**: Atom feed OK, monthly Patch Tuesday batches (last item 2026-11-06). The file is about 2 MB | free | primary | **M** (high if Siemens is in scope). The CSAF provider metadata at `/productcert/csaf/provider-metadata.json` returns 200, while `/.well-known/csaf/` returns 403. — [feed](https://cert-portal.siemens.com/productcert/rss/advisories.atom), [CSAF](https://cert-portal.siemens.com/productcert/csaf/provider-metadata.json)
- **ABB PSIRT**: RSS OK (last item 2026-11-09). A CSAF TLP:WHITE ROLIE feed is also available (JSON, HTTP 200) | **M** — [RSS](https://psirt.abb.com/rss/abbrssfeed.xml), [CSAF](https://psirt.abb.com/csaf/abb-csaf-feed-tlp-white.json)
- **Schneider Electric**: the notifications page lists a separate CSAF JSON for each advisory and an email subscription (`/cybersecurity/notification-contact`). No RSS or CSAF index is listed. The newest notice was SEVD-2026-314-01 on 2026-11-10. curl got 403 (bot block); WebFetch worked. | **M** via email or CISA — [page](https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp)
- **Rockwell Automation**: the advisories page returned 403 to both curl and WebFetch. **Unverified**; rely on the CISA ICS feed — [page](https://www.rockwellautomation.com/en-us/trust-center/security-advisories.html)
- **Claroty Team82 Disclosure Dashboard**: RSS OK (last item 2026-11-10). Lists vulnerabilities Team82 has disclosed | free | primary (vendor research) | **H** — [feed](https://claroty.com/team82/disclosure-dashboard/feed)
- **CISA KEV**: a JSON catalog (HTTP 200, about 1.8 MB), not RSS. Poll it or diff it monthly | **M** — [JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- **ENISA EUVD**: the web UI is live, and the public JSON API endpoints `/api/lastvulnerabilities`, `/api/exploitedvulnerabilities` and `/api/criticalvulnerabilities` all return HTTP 200 JSON. No RSS was found | free | primary (EU) | **M** — [EUVD](https://euvd.enisa.europa.eu/), [API sample](https://euvdservices.enisa.europa.eu/api/exploitedvulnerabilities)
- CERT-EU security advisories: RSS OK (last item 2026-10-23) | **L** — [feed](https://cert.europa.eu/publications/security-advisories-rss)

### Inferences
- The minimum set for the AXC F 2152 is CERT@VDE Phoenix Contact plus CODESYS. PLCnext ships a CODESYS-related runtime option, but this should be checked against the product docs in the KB. Add CISA ICS for the wider OT scope.
- The CSAF and JSON endpoints are for scripts (for example, a monthly diff), not for the RSS reader.

### Gaps
- No RSS was confirmed for Rockwell, Schneider, Beckhoff's own site or WAGO's own site. Beckhoff and WAGO are covered through CERT@VDE.
- The EUVD has no RSS. Whether a third-party EUVD feed exists was not checked.

## 2. Threat intel and vendor research labs

### Takeaway
Feeds were confirmed for Kaspersky ICS CERT, Dragos (partial), Forescout, Microsoft TI and Google/Mandiant. No feed was found for Nozomi, TXOne, Armis or Otorio. For technical OT vulnerability research, the best signal comes from Claroty Team82's disclosures, Forescout Vedere Labs and Kaspersky ICS CERT. Dragos is strongest on threat groups and its annual Year in Review. Microsoft and Mandiant are general threat intel that covers OT only occasionally.

### Cited Findings
- **Kaspersky ICS CERT**: ICS threat landscape reports and vulnerability research | about 2 to 4 items a month (last 2026-11-05) | free | primary for its own research | feed OK | **M**. Note: a Russian vendor; check any restrictions in your company — [feed](https://ics-cert.kaspersky.com/feed/)
- **Dragos**: `https://www.dragos.com/blog.rss` exists but holds only a few items, and the newest (2026-08-10) is an industrial ransomware quarterly. Treat it as partial; the website blog has more. The Year in Review page is live (HTTP 200); it is annual and free with a form | **H** once a year, otherwise **M** — [feed](https://www.dragos.com/blog.rss), [YIR](https://www.dragos.com/year-in-review/)
- The Dragos YouTube channel has a feed (last item 2026-11-06) — [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UC3Ii8YoD6qKJQ1KGYu4RXYw)
- A Dale Peterson blog post titled "Dragos' Post Acquisition Product Strategy" appears in his feed. This points to a corporate change at Dragos that was not otherwise verified — [Dale Peterson feed](https://dale-peterson.com/feed/)
- **Forescout**: the site-wide feed is OK (last item 2026-11-06) and mixes marketing with Vedere Labs research. `/research-labs/feed/` returned a near-empty body | **M** — [feed](https://www.forescout.com/feed/)
- **Microsoft Threat Intelligence** topic feed: OK (last 2026-11-10). OT coverage is rare | **L** — [feed](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/feed/)
- **Google Threat Intelligence (Mandiant)**: feed OK (last 2026-11-02). OT coverage is occasional | **L** — [feed](https://cloudblog.withgoogle.com/topics/threat-intelligence/rss/)
- **Nozomi Networks Labs**: the blog is live, but `/rss.xml`, `/feed`, `/blog/feed` and `/labs/feed` all return 404. No feed | **M** — check manually each month — [blog](https://www.nozominetworks.com/blog)
- **TXOne**: the blog is live, `/feed` returns 404, and only a sitemap exists. No feed | **L** — [blog](https://www.txone.com/blog/)
- **Armis** and **Otorio**: both returned 403 (bot protection) to every request. **Unverified** — [Armis](https://www.armis.com/research/), [Otorio](https://www.otorio.com/)

### Inferences
- Signal versus marketing: CVE disclosures and technical write-ups (Team82 dashboard, Vedere Labs, Kaspersky ICS CERT) are primary, technical material. Ransomware quarterlies, "state of OT" reports and product posts are secondary and partly marketing. Only cite their numbers with the methodology noted.
- The coverage of Microsoft and Mandiant does not justify a weekly check. Their OT pieces show up in Industrial Cyber and SecurityWeek anyway.

### Gaps
- Nozomi, TXOne, Armis and Otorio would need a page-change watcher or an Inoreader web feed. This was not tested.
- Whether Otorio is still independent was not verified.

## 3. Conferences with free recordings or papers

### Takeaway
Most conference archives can be followed as YouTube channel feeds, which works well. Confirmed live channels: S4, SANS ICS, ICS Village, CS3STHLM, TROOPERS, hardwear.io, DEF CON, Black Hat and media.ccc.de. Academic venues (USENIX, NDSS, IEEE S&P) publish open papers once a year, so a calendar reminder is enough.

### Cited Findings
- **S4x** (Miami, annual, the leading OT conference): the site and feed are OK (last item 2026-11-05). The YouTube feed is OK (last 2026-10-04); talks come out after the conference | free videos, paid event | **H** — [site feed](https://s4xevents.com/feed/), [YouTube](https://www.youtube.com/feeds/videos.xml?channel_id=UC5MdLu7ji_eyGiTfigk75lQ)
- **SANS ICS** YouTube (summit talks and webcasts): feed OK (last 2026-10-05) | **H** — [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCXJoSUuG6wQ_9NymBpZP2FQ)
- SANS ICS Summit page: the guessed URL `/mlp/ics-summit/` returned 404, and the SANS blog has no RSS (`/blog/feed/` returns 404). The blog page itself is live and shows ICS posts, such as "SANS 2026 State of ICS/OT Security Report" — [blog](https://www.sans.org/blog)
- **DEF CON ICS Village**: the site is live, and the YouTube feed is OK (last 2026-10-07) | **M** — [site](https://icsvillage.com/), [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCI_GT2-OMrsqqglv0JijHhw)
- DEF CON main channel: feed OK (last 2026-11-08). Black Hat: feed OK (last 2026-11-08). Both are high volume and mostly non-OT, so filter by keyword | **L** — [DEF CON](https://www.youtube.com/feeds/videos.xml?channel_id=UC6Om9kAkl32dWlDSNlDS9Iw), [Black Hat](https://www.youtube.com/feeds/videos.xml?channel_id=UCJ6q9Ie29ajGqKApbLqfBOg)
- **CS3STHLM** (Stockholm, ICS-focused, successor of 4SICS): the website timed out from this host, but the YouTube feed is OK (last 2026-10-22) | **H** — [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCkD15o_9eJxUc9eeHtWSQ6Q)
- **TROOPERS** (Heidelberg): the site is live. The official channel is TROOPERScon, whose feed titled "TROOPERS IT Security Conference" is OK (last 2026-10-03). Recent titles are AD, Kubernetes and AI topics, so the ICS track is not visible in recent uploads. The @WEareTROOPERS handle resolves to an unrelated channel, so do not use it | **M** — [site](https://troopers.de/), [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCPY5aUREHmbDO4PtR6AYLfQ)
- **hardwear.io**: site live; YouTube channel linked from the site, feed OK (last 2026-10-25). Hardware and embedded attacks, relevant to PLC hardware | **M** — [site](https://hardwear.io/), [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UChwYb9xc9tZXquQxu4G0l_g)
- **Chaos Communication Congress / media.ccc.de**: `updates.rdf` is OK (last 2026-10-08) and the YouTube mirror feed is OK (last 2026-11-06). Free, with German-language talks. Watch for 39C3/40C3 in late December | **M** — [updates](https://media.ccc.de/updates.rdf), [YouTube](https://www.youtube.com/feeds/videos.xml?channel_id=UC2TXq_t06Hjdr2g_KdKpHQg)
- Academic venues: USENIX Security (conference pages live, papers open access), NDSS (site live, HTTP 200) and the IEEE S&P index (live) | annual | free papers | primary | no feed; read the accepted-paper lists once a year | **M** — [USENIX Sec 25](https://www.usenix.org/conference/usenixsecurity25), [NDSS](https://www.ndss-symposium.org/), [IEEE S&P index](https://www.ieee-security.org/TC/SP-Index.html)

### Inferences
- The YouTube RSS route (`/feeds/videos.xml?channel_id=`) is the cheapest way to watch conference archives, and it needs no Google account.
- Black Hat and USENIX papers and slides are the most citable primary sources. Videos count as secondary unless the speaker is the original researcher.

### Gaps
- ACM CPSS / CPSIoTSec, ESORICS CyberICPS/CPS4CIP: not fetched. Track them via dblp or the proceedings once a year.
- Black Hat's own briefings archive and the 4SICS legacy archive were not checked.

## 4. Academic search

### Takeaway
arXiv is the only academic source that could be verified as a no-account feed. Two API queries (industrial control and PLC within cs.CR) work and have 2026 items. Google Scholar alerts and Semantic Scholar need an account and could not be verified. dblp's search API returned an HTTP 202 challenge.

### Cited Findings
- arXiv cs.CR daily RSS: OK (2026-11-10). It has hundreds of items a day, too many to read unfiltered | **L** — [feed](https://rss.arxiv.org/rss/cs.CR)
- arXiv API Atom queries (submitted-date order): `abs:"industrial control" AND cat:cs.CR` (newest 2026-11-05) and `abs:PLC AND cat:cs.CR` (newest 2026-09-29) both work | free | papers are preprints, so treat them as primary but not peer-reviewed | **H** — [ICS query](http://export.arxiv.org/api/query?search_query=abs:%22industrial%20control%22+AND+cat:cs.CR&sortBy=submittedDate&sortOrder=descending&max_results=20), [PLC query](http://export.arxiv.org/api/query?search_query=abs:PLC+AND+cat:cs.CR&sortBy=submittedDate&sortOrder=descending&max_results=20)
- Semantic Scholar API: HTTP 429 (rate limited). dblp search API: HTTP 202 challenge page. Neither was verified — [S2](https://api.semanticscholar.org/graph/v1/paper/search?query=PLC+security&limit=1), [dblp](https://dblp.org/search/publ/api?q=industrial%20control%20security&h=3&format=json)
- Research groups (sites live, no feed checked): Fraunhofer AISEC (200), Fraunhofer IOSB (200), Sandia (200), SUTD iTrust (200; datasets page live). INL returned 403 (bot block) — [AISEC](https://www.aisec.fraunhofer.de/), [IOSB](https://www.iosb.fraunhofer.de/), [Sandia](https://www.sandia.gov/), [iTrust datasets](https://itrust.sutd.edu.sg/itrust-labs_datasets/)

### Inferences
- Suggested Google Scholar alerts (to be set up manually; email): `"programmable logic controller" security`, `PLCnext OR "Phoenix Contact"`, `"IEC 62443" penetration`, `ICS honeypot OR "OT network" attack`. One more option is a "cited by" alert on a key paper, for example the GRFICS paper.
- RWTH, RUB (Horst Görtz Institute) and TU Darmstadt were not fetched. Follow their papers through Scholar author alerts instead of their websites.

### Gaps
- Google Scholar alerts and Semantic Scholar feeds were not verifiable without an account.
- The German university groups were not fetched (RWTH, RUB, TU Darmstadt).

## 5. Standards bodies and German/EU institutions

### Takeaway
NIST and BSI have working feeds. ISA, ISAGCA, IEC, ENISA, VDE/DKE, VDMA, ZVEI and Plattform Industrie 4.0 have live sites but no feed that could be found. These suit a monthly or quarterly manual check. The NIST "Drafts Open for Comment" feed is the best way to catch comment calls such as SP 800-82r4.

### Cited Findings
- **NIST CSRC Drafts Open for Comment**: feed OK (built 2026-11-10; latest listed item 2026-06-12). The old `metafeeds/*.rss` URLs return 404 | **H** (comment deadlines) — [feed](https://csrc.nist.gov/CSRC/media/feeds/pubs/drafts-open-for-comment.xml)
- NIST Cybersecurity Insights blog: feed OK (last 2026-10-27) | **L** — [feed](https://www.nist.gov/blogs/cybersecurity-insights/rss.xml)
- **Allianz für Cybersicherheit** (BSI): feed OK (last 2026-11-09). German events and publications | **M** — [feed](https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed/ACS_RSSNewsfeed.xml), [site](https://www.allianz-fuer-cybersicherheit.de/)
- BSI Presse/Veranstaltungen: feed OK (last 2026-11-03) | **L** — [feed](https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed/RSSNewsfeed_Presse_Veranstaltungen.xml)
- ENISA: `/rss`, `/rss.xml` and `/news/rss` all return 404. The publications page is live | **M** quarterly manual — [publications](https://www.enisa.europa.eu/publications)
- ISA (news page live; `/rss` returns 404), ISAGCA (site live; `/blog/rss.xml` returns 404), IEC (202 bot challenge), DKE (200), VDMA (200), ZVEI (200), Plattform Industrie 4.0 (200): no feeds found | **L–M** — [ISA news](https://www.isa.org/news-press-releases), [ISAGCA](https://gca.isa.org/), [DKE](https://www.dke.de/de), [VDMA](https://www.vdma.eu/), [ZVEI](https://www.zvei.org/), [PI4.0](https://www.plattform-i40.de/)

### Inferences
- For German and EU standards, a quarterly manual pass is enough. Changes to IEC 62443 and to CRA implementation also show up in Industrial Cyber and heise.

### Gaps
- The IEC TC65 news page was not reachable because of a bot challenge.

## 6. Communities, newsletters, podcasts

### Takeaway
News aggregators are useful for discovery but count as secondary. Always follow them back to the advisory or paper. The strongest signal: Industrial Cyber (high volume, OT-only), SecurityWeek ICS/OT, Dale Peterson and S4, and Mike Holcomb's YouTube for learning. Reddit is noisy but sometimes surfaces practitioner tooling. ICS Pulse could not be reached.

### Cited Findings
- **Industrial Cyber**: OT-only news, several items a day (last 2026-11-10) | free | secondary | feed OK | **H** (skim) — [feed](https://industrialcyber.co/feed/)
- **SecurityWeek ICS/OT** category: OK (last 2026-11-06). Its weekly "ICS Patch Tuesday" roundups are useful | **H** — [feed](https://www.securityweek.com/category/ics-ot/feed/)
- Security Affairs ICS-SCADA: OK (last 2026-11-09) | **L** — [feed](https://securityaffairs.com/category/ics-scada/feed)
- Control Global: only the home-section feed exists (OK, last 2026-11-09). `/rss` returns 404. Mostly control-engineering content | **L** — [feed](https://www.controlglobal.com/__rss/website-scheduled-content.xml?input=%7B%22sectionAlias%22%3A%22home%22%7D)
- heise Security (German): OK (last 2026-11-10) | **M** — [feed](https://www.heise.de/security/rss/news-atom.xml). CERT.at blog (German): OK (last 2026-11-05) | **L** — [feed](https://www.cert.at/cert-at.de.blog.rss_2.0.xml)
- **Dale Peterson** blog: OK (last 2026-11-04), opinion and strategy | **M** — [feed](https://dale-peterson.com/feed/). **Unsolicited Response** podcast (Libsyn): OK, but the newest episode is 2026-05-27, so it publishes slowly | **L** — [feed](https://unsolicitedresponse.libsyn.com/rss)
- **Mike Holcomb (utilsec)** YouTube: OK (last 2026-11-08). A "Getting Started in OT/ICS Cybersecurity 2026" series is running. His channel text mentions a newsletter, but no newsletter URL was confirmed | **M** — [feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCKO03V8KB-kgWedXTFdaEHA)
- Reddit r/ICS: OK (latest posts 2026-09/11). r/SCADA: OK (2026-11-09). r/PLC: HTTP 429, not verified. These are noisy | **L** — [r/ICS](https://www.reddit.com/r/ICS/.rss), [r/SCADA](https://www.reddit.com/r/SCADA/.rss)
- SANS Internet Storm Center: feed OK (daily), general IT | **L** — [feed](https://isc.sans.edu/rssfeed_full.xml)
- **ICS Pulse**: the connection failed for both `/` and `/feed/`. **Unverified**, possibly down — [site](https://www.icspulse.com/)
- OWASP OT Top 10: the site `ot.owasp.org/v/2025/` is live (200). The guessed GitHub repo `OWASP/www-project-ot-top-10` returns 404, so no feed was confirmed — [site](https://ot.owasp.org/v/2025/)
- isssource.com has a live feed, but item dates jump from 2026 back to 2024, so it was left out.

### Inferences
- Signal: Industrial Cyber, SecurityWeek ICS, S4/Dale, Holcomb, heise. Noise: Reddit, Control Global, Security Affairs and the general ISC feed.
- LinkedIn groups and Discord servers cannot be fed into RSS and need a login. Keep them out of the routine, or allow 10 minutes a month for them.

### Gaps
- The Discord and LinkedIn communities, the OWASP OT Slack channel and Holcomb's newsletter were not verified because they need a login or have no URL.

## 7. Code and data

### Takeaway
GitHub `commits.atom` and `releases.atom` are the zero-cost way to watch code. Active repos (2026): ATT&CK STIX data, ICSNPP, Orange awesome-industrial-protocols, ITI ICS-Security-Tools, EMBA, GRFICSv3. Static archives (ICS-pcap last commit 2020, HAI dataset last commit 2023) are reference material and do not need a feed.

### Cited Findings
- MITRE ATT&CK `attack-stix-data` releases: OK (last 2026-11-05). The ATT&CK Medium blog, with release notes: OK (2026-11-10) | **H** for version bumps — [releases](https://github.com/mitre-attack/attack-stix-data/releases.atom), [blog](https://medium.com/feed/mitre-attack)
- cisagov/ICSNPP (Zeek ICS parsers): commits OK (2026-10-22). The icsnpp-modbus releases feed is OK (last 2025-09-03). The icsnpp-s7comm releases feed is empty | **M** — [ICSNPP](https://github.com/cisagov/ICSNPP/commits.atom)
- Orange-Cyberdefense/awesome-industrial-protocols: commits OK (2026-10-20) | **H** — [feed](https://github.com/Orange-Cyberdefense/awesome-industrial-protocols/commits.atom). ITI/ICS-Security-Tools: OK (2026-11-01) | **M** — [feed](https://github.com/ITI/ICS-Security-Tools/commits.atom). hslatman awesome list: OK but slow (2025-10-10) | **L** — [feed](https://github.com/hslatman/awesome-industrial-control-system-security/commits.atom)
- EMBA (firmware analysis): releases OK (2026-11-03). GRFICSv3: commits OK (2026-10-20) | **M** — [EMBA](https://github.com/e-m-b-a/emba/releases.atom), [GRFICSv3](https://github.com/Fortiphyd/GRFICSv3/commits.atom)
- automayt/ICS-pcap: last commit 2020-01-03 (static archive). icsdataset/hai: last commit 2023-06-06. The hai-dataset.org domain did not connect. The SUTD iTrust datasets page (SWaT/WADI, available on request) is live | **L** — [ICS-pcap](https://github.com/automayt/ICS-pcap/commits.atom), [HAI](https://github.com/icsdataset/hai), [iTrust](https://itrust.sutd.edu.sg/itrust-labs_datasets/)
- The PLCnext GitHub organisation page is live (200). The guessed repo feed `PLCnext/PLCnext_Tutorials` returned 404, so the correct repo name is needed — [org](https://github.com/orgs/PLCnext/repositories)

### Inferences
- GitHub topic pages (`/topics/ics`, `/topics/scada`, `/topics/plc`) have no feeds. A monthly GitHub search sorted by "recently updated" (for example `topic:ics-security pushed:>2026-10-01`) is the low-effort alternative.

### Gaps
- GitHub topic search and Wireshark dissector releases were not checked.

## 8. Training and certification bodies

### Takeaway
These are reference pages, not things to scout. Check them once a year, or when a decision is coming up.

### Cited Findings
- GIAC GICSP and GRID certification pages are live (200) | paid | **L** — [GICSP](https://www.giac.org/certifications/global-industrial-cyber-security-professional-gicsp/), [GRID](https://www.giac.org/certifications/response-industrial-defense-grid/)
- ISA/IEC 62443 Cybersecurity Certificate Program page is live (200) | paid | **L** — [ISA](https://www.isa.org/certification/certificate-programs/isa-iec-62443-cybersecurity-certificate-program)
- INL CCE: the URL guessed from its usual path, `inl.gov/national-security/cce/`, and inl.gov itself returned 403 (bot block). **Unverified** — [INL](https://inl.gov/)

### Inferences
- These sources add no knowledge-base value beyond a single entry each. Leave them out of the feed reader.

### Gaps
- INL CCE could not be verified.

## 9. The scouting routine

### Takeaway
Import `ot-feeds.opml` into one RSS reader, triage for 30 minutes each week and do a 60-minute monthly pass. Every candidate goes into an inbox file first and gets promoted to the knowledge base only through a fixed triage rule. Expected total: about 3 hours a month.

### Cited Findings
- The OPML here contains only feeds verified on 2026-11-10 (57 outlines, XML parses). — local file `ot-feeds.opml`
- Inoreader is live and has its own blog feed. The free tier has not been checked — [Inoreader](https://www.inoreader.com/)

### Inferences
**Tooling (pick one):**
- FreshRSS (self-hosted, Docker, GDPR-friendly, filter rules and keyword search). This fits a German company that does not want reading data in a US SaaS. Feedly and Inoreader are the zero-maintenance option; their keyword filters for high-volume feeds may be paid. *(Not verified in this pass.)*
- Make the high-volume feeds (WID, CISA all, arXiv cs.CR, DEF CON, Black Hat, Industrial Cyber) usable with keyword filters: `PLCnext|Phoenix Contact|AXC F|CODESYS|Modbus|PROFINET|OPC UA|IEC 62443|PLC|SCADA|ICS`.
- Email alerts go to a dedicated folder: Google Scholar alerts (section 4), the Schneider notification subscription and the GovDelivery or CSRC email if wanted.
- Non-feed sources (Nozomi, TXOne, ENISA, ISA/ISAGCA, VDMA/ZVEI, Rockwell): a monthly manual bookmark folder, or a FreshRSS "web scraping" / Inoreader "web feed" (not tested).

**Cadence and time budget:**
- *Weekly (30 min, e.g. Monday):* section 1 advisories (CERT@VDE Phoenix Contact/CODESYS first), Team82 dashboard, Industrial Cyber and SecurityWeek ICS headlines, arXiv queries. Mark anything relevant as "to inbox"; read nothing in depth yet.
- *Monthly (60 min, first Monday):* threat intel, YouTube channels, NIST drafts, BSI/ACS, GitHub feeds, KEV diff, EUVD exploited list, manual bookmarks (Nozomi, ENISA, ISA). Process the inbox (below).
- *Yearly / event-driven:* the Dragos YIR (Q1), S4x videos (spring), DEF CON/Black Hat (Aug–Sep), 3xC3 (Dec–Jan), USENIX/NDSS/S&P accepted-paper lists, and the SANS ICS survey.
- *Quarterly (15 min):* re-run the feed-health check (curl loop, newest-item date) and drop feeds with nothing new in 12 months, as the CERT@VDE blog showed.

**Inbox step (so links do not rot):**
- One file, `research_notes/inbox.md` (or `knowledge-base/_inbox.md` if the KB owner agrees), with one line per candidate: `- [ ] 2026-11-10 | <url> | <found via feed name> | <one-line why> | OWASP OT #?`.
- Process it once a month. Each line ends as *promoted* (a KB entry is written), *merged* (a fact added to an existing entry) or *dropped* (with a one-word reason). Delete processed lines. If a line is still open after two monthly cycles, drop it.

**Triage rule (promote to the KB only if all of these hold):**
1. **Primary first:** if a secondary item (news, blog) points to an advisory, paper or repo, promote the primary source and cite the secondary only as `found_via`.
2. **Relevance:** it maps to at least one OWASP OT Top 10 item (`owasp_ot` field), or to the AXC F 2152 / PLCnext / CODESYS stack, or it changes an existing KB fact (a new version or a withdrawn standard).
3. **Recency:** published or updated in the last 24 months, unless it is a foundational standard or dataset.
4. **Durability:** the URL is stable (an advisory ID, DOI, arXiv ID or tagged release), not a live dashboard.
5. **Not duplicate:** no existing KB entry covers it (check `INDEX.md`). Otherwise update that entry.
6. **Clean source:** no leaked or paid-content copies and no exploit-trading forums. Vendor marketing counts as `trust: secondary`.

### Gaps
- FreshRSS, Feedly and Inoreader feature or pricing details were not verified in this pass.

## 10. Fit to the existing project

### Takeaway
The current frontmatter (`url`, `trust`, `accessed`, `published`, `status`, `reason`, `version`) already records most of the provenance. Adding one optional field, `found_via`, would close the scouting loop. Keep `ot-feeds.opml` in the repo, but outside `knowledge-base/`.

### Cited Findings
- Existing KB entries use `title, url, type, trust, accessed, published, owasp_ot`, plus optional `status`, `reason`, `version`, `license` and `local_file`. `INDEX.md` is generated by `build_index.py` — local files `/home/greberl/ot-pentesting/knowledge-base/owasp/owasp-isvs.md`, `/home/greberl/ot-pentesting/knowledge-base/articles-talks/youtube-utilsec-channel.md`, `/home/greberl/ot-pentesting/knowledge-base/INDEX.md`
- The KB already has `certvde-rss-feeds.md`, which documents the CERT@VDE feed and CSAF endpoints (41 vendor slugs, 46 trusted providers). This map does not duplicate it; the OPML adds the four most relevant vendor feeds — `/home/greberl/ot-pentesting/knowledge-base/vuln-data/certvde-rss-feeds.md`

### Inferences
- Provenance mapping: `url` is the source itself, `trust` is primary or secondary, `accessed` is the scouting date and `published` is the recency check. Proposed: `found_via: "<feed name or URL>"`, an optional field showing which feed or secondary article surfaced the entry. Whether `build_index.py` needs a change for it was not checked; unknown keys are probably ignored, but this should be checked.
- Store `ot-feeds.opml` under version control (here, or in a `scouting/` folder next to `knowledge-base/`). Re-export it from the reader when feeds change, so the feed list keeps its own history. Do not put it in `knowledge-base/`, which holds one entry per source.
- The feed-health curl loop used for this pass (status, newest item date) could later become a small script next to `build_index.py`. It is not needed until the OPML grows.

### Gaps
- Whether `build_index.py` tolerates new frontmatter keys was not checked; the task said not to touch the KB.
