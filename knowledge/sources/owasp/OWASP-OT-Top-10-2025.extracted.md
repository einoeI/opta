<!-- Extracted from OWASP-OT-Top-10-2025.pdf by extract_pdf.py (pypdf) on 2026-11-10. Working copy: check against the PDF before quoting. -->

<!-- page 1 -->

OTTop10
TheTop10Operational
TechnologySecurityRisks
2025 Edition
PROJECT LEADERS
Andreas Happe
Felix Eberstaller
Simon Rommer
Siegfried Hollerer ot.owasp.org

<!-- page 2 -->

OTTop10
OperationalTechnologySecurityRisks
OWASPOperationalTechnology(OT)Top10,2025Edition
Version: 2025.0.0‑127‑g3616452
Available online athttps://ot.owasp.org. This is a living document and is updated as the OT
threatlandscapeevolves.
PartoftheOWASPOTTop10Project:
https://owasp.org/www‑project‑operational‑technology‑top‑10/
Project leaders (in alphabetical order): Andreas Happe, Felix Eberstaller, Simon Rommer,
SiegfriedHollerer.
Copyright©TheOWASPFoundation
Thisworkislicensedunderthe CreativeCommonsAttribution‑ShareAlike4.0InternationalLicense(CC
BY‑SA 4.0). For any reuse or distribution, you must make the license terms of this work clear to others.
OWASP® isaregisteredtrademarkoftheOWASPFoundation,Inc.

<!-- page 3 -->

OWASPOTTop10
Contents
I. Introduction 1
OWASPOTTop10 2
Aim&Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
TargetAudience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
HowtoUseThisDocument . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
TheTop10List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
ProjectLeaders(inAlphabeticalOrder) . . . . . . . . . . . . . . . . . . . . . . . . . 4
CopyrightandLicense . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Summary 5
TheTop10ataGlance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
II. OperationalTechnology(OT) 7
DefiningtheDomain: CPS,OT,andICS 8
ThePurdueModel: OrganizingSystemsbyFunction . . . . . . . . . . . . . . . . . . 9
TheIT/OTConvergence: DefiningFunctionalContext . . . . . . . . . . . . . . . . . . 11
ExampleOTArchitectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Stakeholders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
SafetyandSecurity 14
AvailabilityisParamount . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
SafetyandSecurityCulture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
OTforITSecurityPeople 16
UnderstandingtheCulturalDivide . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
TheRealityofOTSystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
TheMitigation‑FirstApproach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
WhenMitigationsFail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
TheCascadeEffect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
IncidentResponseChallenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
ThePathForward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
SecurityforOT:WhyIsItProblematic? 22
TheHistoricalContext . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
TheTurningPoint: StuxnetandBeyond . . . . . . . . . . . . . . . . . . . . . . . . . 22
CurrentChallenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
CommonProblemsandFalseAssumptionsAboutOTSecurity . . . . . . . . . . . . 23
AdvantagesofSecurity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2025Edition iii

<!-- page 4 -->

OWASPOTTop10
RelatedFrameworks,Standards,andRegulations 30
Frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
StandardsofOtherOrganizations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
Regulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
ExistingVulnerabiltyLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
MappingTable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
III. TheTop10 34
TheOWASPOperationalTechnologyTop10 35
StructureofEachTop10Item . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
1. UnknownAssetsandUndocumentedServices 37
2. (Accessible)DeviceswithKnownVulnerabilities/Issues 41
3. InadequateSupplyChainManagement 45
4. LossofAvailability 49
5. InsufficientAccessControl 53
6. MissingIncidentDetection/ReactionCapabilities 57
7. BrokenZonesandConduitsDesign 62
8. MissingAwareness 65
9. SelectionofComponents/ProtocolsWithInsufficientSecurityCapabilities 69
10.MissingHardening 72
IV. WheretoStart 76
What’snextandWheretoStart? 77
ForexistingSystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
FornewSystems/Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
PrepareforIncidents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
AdditionalReading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
V. AbouttheProject 79
AboutOWASP 80
2025Edition iv

<!-- page 5 -->

OWASPOTTop10
CommunityandContributing 81
HowtoContribute? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
EmpiricalDataContribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
HowtoTestYourChangesLocallyBeforeSubmitting . . . . . . . . . . . . . . . . . . 81
ListofOurContributors 83
RelatedOWASPProjects 84
OWASPIoTTop10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
OWASPTop10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
VI. Appendix 85
Mappingtable 86
1. UnknownAssetsandUnmanagedExternalAccess . . . . . . . . . . . . . . . . . . 86
2. DeviceswithknownVulnerabilities/Issues . . . . . . . . . . . . . . . . . . . . . . 86
3. InadequateSupplier/SupplyChainManagement . . . . . . . . . . . . . . . . . . 86
4. LossofAvailability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
5. InsufficientAccessControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
6. MissingIncidentDetection/ReactionCapabilities . . . . . . . . . . . . . . . . . . 88
7. BrokenZonesandConduitsDesign . . . . . . . . . . . . . . . . . . . . . . . . . . 88
8. MissingAwareness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
9. InsufficientSecurityCapabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
10. MissingHardening . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
Glossary 91
2025Edition v

<!-- page 6 -->

PartI
Introduction

<!-- page 7 -->

OWASPOTTop10 OWASPOTTop10
CommunityandContributing
Please don’t hesitate to contact the OWASP OT Top 10 project with your questions com‑
ments, and ideas, either publicly by adding issues or providing commits onour github
page. Please join theOWASP OT Top 10 Slack Channelto chat. You can get a free invita‑
tiontotheOWASPslackserverthrough thiswebsite.
Wedoavideoconferenceeveryfirstmondayofamonthfrom4pmto5pmCET/CESTusing
https://meet.google.com/gwi‑vhxz‑rjr. Wealsoprovidean publicicscalendarseries that
youcanaddtoyourcalendar.
Ifyouwanttocontribute, pleaseseeour contributingguide. Basically, all workhappens
public on github and through merge‑requests. If you plan a larger change, it is always a
goodideatotalkwithusduringoneoftheMonthlymeetingsfirst.
OWASPOTTop10
Operational Technology (OT) encompasses a wide variety of programmable systems and de‑
vices that have direct or indirect interactions with the physical environment. These technolo‑
giesareintegraltonumeroussectorssuchasmanufacturing,energy,transportation,medical,
andutilities, wheretheyplayacrucialroleintheoperationandmanagementofphysicalpro‑
cesses.
As OT systems become more interconnected and integrated with Information Technology (IT)
networks,theyfaceincreasedvulnerabilitytolarge‑scalecyberattacks. Thisintegration,while
beneficial for operational efficiency and data sharing, exposes OT systems to the same cyber
threatsthattypicallytargetITenvironments.
TherisksassociatedwithOTareparticularlysignificantbecausethesesystemscontrolphysical
processes. UnlikeITenvironments,wherecyberattacksprimarilyimpactdata,breachesinOT
systems can lead to catastrophic outcomes, including physical damage, safety hazards, and
disruptionstocriticalinfrastructure. Therefore, securing OTsystemsis paramounttoprevent
potentiallysevereconsequences. ThesignificanceofsafeguardingOTenvironmentscannotbe
overstated. These systems are integral to the functionality of critical infrastructure, and thus
society.
Despitetheirimportance,OTsystemsoftenlacktherobustcybersecuritymeasuresmorecom‑
monlyfoundinITenvironments. Thisisprimarilyduetothelegacynatureofmanyindustrial
controlsystems(ICS)andthehistoricalprioritizationofoperationalgoals. InOT,securityprin‑
ciplesfollowtheCIAtriad‑Confidentiality,Integrity,andAvailability‑butwithadifferentem‑
phasisthanIT.Availabilityandsafetyaretypicallythehighestpriorities,asdowntimeorunsafe
conditionscanleadtosevereoperational,financial,orevenphysicalconsequences. Confiden‑
tiality and integrity, while still important, often take a secondary role compared to ensuring
continuous and safe operations. This difference in prioritization has shaped the design and
securitypostureofOTsystemsovertime.
2025Edition 2

<!-- page 8 -->

OWASPOTTop10 OWASPOTTop10
Aim&Objective
Thegoalofthe OWASPOperationalTechnology(OT)Top10 istoraiseawarenessaboutthe
topsecurityrisksandvulnerabilitiesspecifictoOperationalTechnology(OT)environments. By
providingactionablerecommendations,weaimtoimprovethesecuritypostureofOTsystems
andprotectcriticalinfrastructurefromcyberthreats.
Scope
ThescopeincludesallthedevicesintheOT‑domain. Thisincludesdevicesthatarepartofthe
core functionality of the system (CNC machines, SCADA systems, centrifuges, insulin pumps,
HVAC,…)aswellasallrelateddevices(HMI,barcodescanner,surveillancecamerasontheshop
floor,virtualizationserversandVMswithcorefunctionality,…). OfficeITandedgedevicesthat
arenotdirectlyrelatedtothemainOTpurposearenotinscope.
TargetAudience
Thisdocumentisintendedforprofessionalsinvolvedinthedevelopment,integration,andoper‑
ationofOTsystems,includingsystemdevelopers,integrators,andoperators. Italsoprovides
value to development managers, product owners, QA professionals, program managers, and
anyoneengagedinbuildingormaintainingsoftwarecomponentsforOTenvironments.
While developers can proactively create secure components, integrators are often limited to
implementingmitigations. Recognizingthisdistinctionisimportantforapplyingtheguidance
effectively.
ThegoalistomakethesegroupsawareoftheuniquesecuritychallengesinOTenvironments
andtherisksthatcan(andlikelywill)ariseifsecurityisoverlooked. Awarenessmeasuresmay
come from internal policies or supply chain requirements, and this document supports both
approaches.
HowtoUseThisDocument
The primary purpose of this document is to raise awareness of common security problems in
the OT space and provide a foundation for addressing them. It introduces developers and in‑
tegratorstotheOTworldanditsspecificrequirements,helpingthemanticipatevulnerabilities
andapplymitigations.
Readersshouldusethisdocumentas:
• Anawarenesstool forunderstandingcriticalOTsecurityrisks.
• Areferenceguide forbestpracticesandmitigations.
• A foundation for policy and supply chain requirements, helping organizations align
internalguidelineswithexternalmandates.
2025Edition 3

<!-- page 9 -->

OWASPOTTop10 OWASPOTTop10
• Astartingpoint,notacompletesolution ‑whiletheTop10risksarecritical,theyarenot
exhaustive. Additionalrisksmayexist,andorganizationsshouldbuildacomprehensive
securitystrategybeyondthislist.
TheTop10List
Duringthediscussions,weagreedupontheitemsofthetop10listwhiletherespectiveranking
was highly subjective. Items 1 to 4 were selected as the Top 4 because there was consensus
that these are fundamental for OT security, items 5 to 9 were all deemed to be of similar high
importance,andthefinalitemisnotasecurityissuebyitselfbutwouldhavepreventedmany
oftheincidentsreportedfromthefield.
TheSummarygivesyoualltenitemswithonesentenceeach, TheTop10 hasthefullchapters.
ProjectLeaders(inAlphabeticalOrder)
• AndreasHappe
• FelixEberstaller
• SiegfriedHollerer
• SimonRommer
CopyrightandLicense
This document is released under the Creative Commons Attribution‑ShareAlike 4.0 Interna‑
tionallicense. Foranyreuseordistribution,youmustmakeitcleartoothersthelicenseterms
ofthiswork.
2025Edition 4

<!-- page 10 -->

OWASPOTTop10 Summary
Summary
OTrunsthephysicalprocesseswealldependon: powerplants, productionlines, watertreat‑
ment,medicaldevices. Theyarebuiltforavailabilityandsafety,operatedfordecades,andnow
connected to office IT, their vendors, and often the internet. When things go wrong in IT, the
usualimpactisdataloss;whenthingsgowronginOT,productionstops,equipmentisdamaged,
andpeoplecanbehurt. Thetenitemsbelowaretherisksandmissingpracticesourcontribu‑
torskeeprunninginto,notindividualvulnerabilities.
TheTop10ataGlance
TheTop4,onwhichtherewasconsensusthattheyarefundamental:
1. UnknownAssetsandUndocumentedServices : Ifyoucannotseeit,youcannotpatch,
segment,ormonitorit;undocumentedservicesandforgottenremoteaccessarehowin‑
trudersreachtheprocess.
2. Devices with Known Vulnerabilities: Exposed devices with known vulnerabilities are
easy, high‑value OT targets. A single exploited PLC, HMI, or RTU can bypass upstream
defensesandthreatentheprocess.
3. Inadequate Supply Chain Management: Vendors, integrators, and maintenance
providers already have privileged access, so attackers use them to scale one compro‑
miseacrossmanyoperators.
4. LossofAvailability : AvailabilityistheprimaryOTrequirement. Outagescanresultfrom
malware,unsafechanges,integrityfailures,orfaultyupdates.
Thenextfive,alldeemedtobeofsimilarhighimportance:
5. InsufficientAccessControl : Shared passwords, missing roles, and remote access with‑
outMFAturnonestolencredentialintoapathtotheprocess.
6. Missing Incident Detection/Reaction Capabilities: Without logging, monitoring, and
testedresponse,intrusionspersistunseenformonthsandescalatefromsmallincidents
tomajoroutages.
7. Broken Zones and Conduits Design: Flat networks let one compromised host reach
many systems. The right zone design matches how the plant actually communicates
andlimitstheblastradius.
8. Missing Awareness: Controls must be understood and supported by operators. When
staff do not know why a security measure exists, it is bypassed or disabled to keep pro‑
ductionrunning.
9. InsufficientSecurityCapabilities : OTsystemslastdecades;equipmentorprotocolsse‑
lected without authentication, encryption, or update capability create legacy risks that
arehardtoremediatelater.
Notasecurityissuebyitself,butitwouldhavepreventedmanyreportedincidents:
2025Edition 5

<!-- page 11 -->

OWASPOTTop10 Summary
10. Missing Hardening: Hardening does not eliminate vulnerabilities, but it raises the cost
ofexploitation. Inourexperience,lackofhardeningiswhatturnedavulnerabilityintoa
breach.
2025Edition 6

<!-- page 12 -->

PartII
OperationalTechnology
(OT)

<!-- page 13 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
DefiningtheDomain: CPS,OT,andICS
Whenwetalkaboutsecuringindustrialenvironments, itisimportanttorecognizethatnotall
digital systems are created with the same goals in mind. Traditional IT focuses on data ‑ how
it is stored, processed, moved, and protected. Operational environments revolve around the
physicalprocesses. Tounderstandthislandscape,ithelpstoimaginethreelayers,eachnested
withintheother.
Cyber‑Physical Systems (CPS)are integrated systems combining computation, networking,
and physical processes. This category is expansive and includes everything from an au‑
tonomousvehiclenavigatingtraffictotheinterconnectedsensorsandcontrollersthatregulate
asmartcity.
WithinCPSlies OperationalTechnology(OT) ,amorespecializeddomainfocusedspecifically
onindustrial, utility, andcriticalinfrastructureenvironments. OTencompassesthemachines,
controlsoftware,andcommunicationnetworks. Thesesystemsarebuilttokeepessentialpro‑
cessesrunningsafely,reliably,andoftencontinuously.
Within the OT domain,Industrial Control Systems (ICS)represent a major subset compris‑
ingtechnologies. ICSreferstothespecificcomponentsthatcarryoutcontrolfunctionsonthe
shopfloororwithinanindustrialprocess. ThisincludesProgrammableLogicControllers(PLCs)
thatopenandclosevalves,SupervisoryControlandDataAcquisition(SCADA)systemsthatsu‑
pervise entire facilities, and Human–Machine Interfaces (HMIs) that operators use to monitor
temperatures,pressures,andproductionflows.
ICS architectures form the backbone of industrial operations and are often used interchange‑
ablywiththetermOTincybersecuritycontexts.
Figure1: Cyber‑physicalsystems,OTandICS
Overall,OTsystemsareessentialfortheoperationofmanyindustries,andtheyfaroutnumber
InformationTechnology(IT)systemsinuse. OTsecurityproblemsintheseindustriescanhave
majorimpactsonthesocietyandsurroundingenvironment.
2025Edition 8

<!-- page 14 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
ThePurdueModel: OrganizingSystemsbyFunction
The Purdue Reference Model provides a functional hierarchy commonly used to describe and
segmentOTenvironments. Itseparatessystemsbasedontheiroperationalroleandtheirprox‑
imitytothephysicalprocess,enablingclearersecurityboundariesandcommunicationpaths.
Whileinitiallydeployedinthe1990s, thePurdueModeltodayexistsinmanyslightlymodified
versions, but in general there are 6 separate levels and additional DMZs between them. The
image below shows these levels starting with Level 0 (the actual physical field devices) up to
Level5,wheretheenterpriseITresides.
Figure2: PurdueModelArchitectureExample(source: LimesSecurity)
Levels0–1: DirectInteractionwiththePhysicalProcess
Levels0and1includesystemsthatinterfacedirectlywithphysicalequipment. Interruptionsor
compromiseatthislayerhaveimmediate,real‑timeoperationalimpact.
• Level 0 – Field Devices.This level consists of sensors, actuators, valves, motors, and
otherfielddevicesthatmonitororaffectphysicalparameterssuchastemperature,pres‑
sure,flow,orposition.
• Level 1 – Process Control.This level contains devices that read data from Level 0 and
issuecontrolcommands. Commontechnologiesinclude:
– ProgrammableLogicControllers(PLCs): Smallcomputersthatexecutethelogic
torunamachine.
2025Edition 9

<!-- page 15 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
– RemoteTerminalUnits(RTUs): SimilartoPLCsbuttypicallydeployedacrosslong
distancesorremoteinfrastructure(e.g.,pipelines).
– Intelligent Electronic Devices (IEDs):Specialized control and protection equip‑
ment,usedprimarilyinelectricpowersystems.
Levels2–3: IndirectInteractionandOperationalManagement
Levels 2 and 3 provide supervisory and operational functions. These systems do not control
hardwaredirectlybutcommunicatewithLevel1devicestomonitororadjusttheprocess.
• Level2–SupervisoryControl. Systemsatthislevelprovidetheinterfaceforhumansto
interactwiththemachines.
– Human–Machine Interfaces (HMIs):Localized operator screens for viewing pro‑
cessstatesandissuingmanualcommandstospecificmachines.
– Supervisory Control and Data Acquisition (SCADA) Systems:Aggregated super‑
visoryplatformsthatcollectdatafrommultiplecontrollers(PLCs/RTUs)toprovide
centralizedvisibilityacrossanentirefacilityordistributedenvironment.
• Level3–OperationsManagement. Systemsinthislayermanageproductionworkflows
andfacilityoperationsacrossthesite. Typicalexamplesinclude:
– Manufacturing Execution Systems (MES):Coordinate production processes, ma‑
terialflows,andoperationaltracking.
– BuildingAutomationSystems(BAS): SupportinfrastructuresuchasHeating,Ven‑
tilation, and Air Conditioning (HVAC), lighting, and environmental controls within
industrialsites.
WhilethecoreofOTsitsat Levels0–3, thePurdueModelextendsintothecorporateworld. It
isimportanttonotethatthisisnotastrict, universalblueprint, butareferencemodeltohelp
definetrustboundaries.
• Level3.5–IT/OTDMZ(DemilitarizedZone). Thisisthemostcriticalsecurityboundary.
It acts as a “buffer” between IT and OT. Since most security incidents originate in the IT
environment (e.g., phishing), this layer prevents an infection from spreading directly to
thecontrollersatLevel1.
• Level4–LocalBusinessNetwork. Thelocalofficenetworkattheplantsite(e.g.,local
engineeringworkstationsorsite‑specificERP).
• Level 5 – Enterprise.The corporate headquarters network, where centralized services
likeemailandglobalHRsystemsreside.
• Level 5+ – Internet & Internet DMZ.External connections, cloud‑based analytics, and
remotevendoraccess.
2025Edition 10

<!-- page 16 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
TheIT/OTConvergence: DefiningFunctionalContext
In modern industrial settings, the distinction between IT and OT is not defined by the hard‑
ware itself, but by thefunctionthe device performs and thecontextin which it operates. This
isknownasIT/OTconvergence‑wheretraditionalITcomponentsareusedtomanagephysical
processes.
TodetermineifasystembelongsintheOTdomain, considerthefollowing“litmustest”ques‑
tions:
1. PhysicalImpact: If the device fails or is compromised, does it directly affect a physical
processorlifesafety?
2. Environment: Is the device located on the factory floor or within a secured industrial
network(Levels0–3)?
3. PrimaryGoal: Isthesystem’smostcriticalrequirementAvailability(keepingtheprocess
running)ratherthanConfidentiality(protectingdata)?
Example: TheVideoCamera
ConsiderastandardIPvideocamera. Ifthatcameraisinstalledinacorporatelobbytomonitor
forunauthorizedvisitors,itisatraditional ITasset. Failureresultsinalossofrecordsbutnoim‑
pactonbusinessoperations. However,ifthatsamemodelofcameraisplacedonafactoryfloor
toallowanoperatortomonitorahigh‑pressurefurnaceoraroboticassemblycell,itbecomes
acritical OTasset.
ExampleOTArchitectures
AtypicalOTsystemconsistsofcontrolloops, human‑machineinterfaces(HMI)andremotedi‑
agnosticsandmaintenancetoolslikedepictedintheimagebelow.
2025Edition 11

<!-- page 17 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
Figure3: ComponentsofanOTSystem(source: NISTSP800‑82r3,p.11)
A control loop is meant – as the name suggests – to control some kind of process. To do so,
the loop employs a combination of sensors, actuators and controllers. Sensors measure cer‑
tainphysicalpropertiesliketemperatureorpressureandsendthese controlledvariables tothe
controller. Thiscomponentactsasthebrainoftheloop. Byinterpretingthesentinformation
basedonacontrolalgorithmandtargetsetpoints,so‑called manipulatedvariables arecreated.
These are sent to the actuators, which are the components that directly manipulate the con‑
trolledprocessaccordingtothecommandsofthecontroller.
Forexample,asensorthatmeasuresthetemperatureofaboilersendsthecontrolledvariable
temperatureto the controller. If the controller determines that the measured temperature is
below the set target, he instructs an actuator to activate the heater rod of the boiler until the
temperaturematchesthesettargettemperatureagain.
Thisprocesscanmostlybemonitoredandmanipulatedbyhumanoperatorsviatheso‑called
HMI.InourexampletheHMImaybeallowstheoperatorstochangethetargettemperatureand
to observe the current state of the boiler. Finally, remote diagnostics and maintenance tools
canbeusedincaseofabnormaloperationofthesystemorsolution.
Stakeholders
AchievingrobustsecurityinOTenvironmentsrequiresclosecollaborationbetweenseveralkey
parties. The international standard for OT security,IEC 62443, identifies four primary roles,
eachwithdistinctresponsibilitiesandsecuritychallenges:
• Asset Owner:The entity that operates the industrial facility (e.g., a power plant or fac‑
tory). They are responsible for the overall security of the environment and are usually
theoneswhoimplementhigh‑leveldefenseslikenetworksegmentation.
2025Edition 12

<!-- page 18 -->

OWASPOTTop10 DefiningtheDomain: CPS,OT,andICS
• ProductSupplier: Thecompanythatdevelopsandmanufacturesthecomponents,such
as PLCs, HMIs, or networking hardware. They are responsible for “security‑by‑design,”
ensuringthehardwareandsoftwareareresilientbeforetheyreachthecustomer.
• IntegrationServiceProvider(Integrator): Thepartythatassemblesindividualcompo‑
nents into a complete automation solution tailored for a specific site. They ensure that
thedifferentpartsworktogethersecurelywithintheowner’sinfrastructure.
• MaintenanceServiceProvider: Theentity(oftenanexternalvendor)responsibleforthe
ongoingupkeepofthesystems. Theyareacriticalsecuritylinkbecausetheyfrequently
requireremoteorphysicalaccesstothe“heart”ofthecontrolsystem.
OT security challenges are different for these stakeholders, which is also reflected in the dif‑
ferentstandardsoftheIEC62443series. Forexample,anoperatordoesnothaveaccesstothe
developmentprocessofthespecificcomponentandthuscannotimplementsecuritymeasures
atthesourcecodelevel.
Ontheotherhand, theoperatormoreorlesscanshape theintendedenvironmentwherethe
solution is employed and therefor is capable of introducing mitigating measures like strong
networksegmentation.
As the impact of security failures in OT can be tremendous, there is anincreasing number of
lawsandregulations governingthedevelopmentandoperationofOTsystemsanddevices. Ex‑
amplesaretheEuropeanNIS2andtheCyberResilienceAct(CRA),theUSEO14028ortheChina
CybersecurityLaw.
2025Edition 13

<!-- page 19 -->

OWASPOTTop10 SafetyandSecurity
SafetyandSecurity
AlthoughthereisanincreasingconvergenceofITandOTandregularITsystemsarejustaswell
usedinOTenvironments,therearenonethelessfundamentaldifferencesinsecuritygoalsand
securityculture. Whenassessingthesecurityimpactofsecurityvulnerabilities,ITsecuritypeo‑
pleoftenrefertothe“CIAtriad”. TheacronymisbuiltfromthestartinglettersofConfidenciality,
IntegrityandAvailability.
Whilein IT commonlyconfidentialityand integrityareparamount, confidentialityismostlyof
lesser importance in OT as it is often employed in more or less physically restricted environ‑
ments. ThemostimportantgoalinOTissafety,ashumanscangetharmed orevenworse
getkilledwhenOTsystemsanddevicesmalfunction.
Thisisfurthercomplicatedbythefact,thate.g.inGermanSafetyandSecurityareactuallythe
same world (“Sicherheit”), leading to too many “lost‑in‑translation” effects even while using
thesamelanguage.
AvailabilityisParamount
Besidesthat,availabilityisparamount. Beitproductionsite,beitcriticalenergyinfrastructure
– many OT environments cannot afford even the smallest downtime. This also is reflected in
security testing of OT, where many tools that are commonly deployed in IT environments can
carryasignificantriskifnotusedcarefullyinOT.
For example, a simple port and service scan with the well‑known toolnmap is a common ap‑
proach to start off the enumeration in a penetration test. While this is totally fine in most IT
systems, there are many PLCs that can crash if they receive such packets. This is mainly due
to their highly specific intended usage in certain processes and the resource constraints that
comewiththem. Additionally,duetospecialrequirementslikereal‑timecapabilitiesmanypro‑
prietaryprotocolsareusedtocomplementstandardprotocols. Thismakesthetestingprocess
harderingeneralasthereislesscrossoverbetweendifferentenvironments.
Worst‑CaseScenarios
ThefocusonsafetyandavailabilityisalsoreflectedinOTworst‑casescenarios. WhileinITloss
ofdataconfidentialityormanipulationofdataisoftencatastrophic,OTworst‑casesarelossof
view(LOV)andlossofcontrol(LOC).LOVdescribesascenariowheretheoperatorsdonothave
visibilityorcorrectvisibilityofwhatishappeningwiththeprocess. Sothesystemsstilloperate,
butitisunknownwhattheyarecurrentlydoingandiftheyareactuallydoingtherightthing.
AnexampleforLOVwaswhenStuxnetmanipulatedmonitoringofIranianoperatorstomislead
themthinkingthateverythingwasworkingcorrectly. LOC,asthenameimplies,meansthatthe
operators cannot control the process and its systems anymore more, making them unable to
respondtopossibleunsafeoperations.
2025Edition 14

<!-- page 20 -->

OWASPOTTop10 SafetyandSecurity
CIA‑TriadinITandOT
IntraditionalITsystems,weoftenemphatiseConfidencialityandIntegrity. Forexample,when
youlookataweb‑shop,itisimportantthatnosensitiveuserdata(suchaspasswordsororders)
areexposed(confidenciality)andthatinvoicescannotbechangedbyattackerssothattheypay
lessmoney(integrity). Availabilityisoftenonlyanafter‑thought: iftheshopisdown,it’sdown.
Thecompanymightnotmakeanymoneyfromorders,buttheywillnotbesuedduetoexposed
passwordsorloosemoneythroughmaliciouslyalteredinvoices.
TheOTworldworksdifferently. Hereavailabilityisparamount: theworstcaseifoftenthat,e.g.,
apowerplantisnotproducinganypoweranymore(availabiliity)andthisismoreseverethan
exposingfinancialdataofthepowerplantcompany(confidenciality).
Sometimes, this differentiation is not as clear‑cut: imagine an attacker can alter transmitted
usagedata(integrity)andthroughthatmisleadsapowerplanttoover‑orunder‑producepower
(availability).
SafetyandSecurityCulture
While security culture is shifting in OT and is undeniably growing in importance due to an
increasing number of regulations and cyberattacks, this culture shift unfortunately is quite
slow.
UnlikeITsystemswiththeirshortlifetime,OTsystemsareusedfor15to20years.
Aspatchingisoftennotpossibleduetotheresourcereasonsandpossibleoutagesmentioned
before,therearemanyvulnerablelegacysystemsandinsecureprotocolsinactiveuseforyears
tocome. Especiallythoseprotocolssometimeshavetobecompletelyredesigned,assecurity
was not an issue when they first were conceived. Also the mindset of the engineers and their
organizationsoftentimesisnotthesameyetasofITengineers.
Whilehavingaverygoodunderstandingofthepreventionofaccidentsandthereforerequired
safety measures, the notion that there are indeed attackers deliberately causing such “acci‑
dents”isnotaswidespreadasmuchasitisneededyet.
Additionally,manycompaniesarenotasopentovulnerabilitydisclosuresasmostITcompanies
yet. Fortunately, this is also currently changing and more and more OT organizations see the
valueintransparentandproactivehandlingofdiscoveredvulnerabilities.
2025Edition 15

<!-- page 21 -->

OWASPOTTop10 OTforITSecurityPeople
OTforITSecurityPeople
ThisintroductionexplainswhyOTsecuritylooksthewayitoftenlooks,specificallyforITsecu‑
rityprofessionalswhomaybeencounteringoperationaltechnologyenvironmentsforthefirst
time.
UnderstandingtheCulturalDivide
Allprofessionalcommunitieshavetheirownworkcultureandmindset,andpeopleonlywork‑
inginITsecuritymaynotevenbeawareofthecultural“waters”inwhichthey“swim”. OTisa
separateculture andthingsworkratherdifferentlythanintraditionalITenvironments.
When IT security people look at OT scenarios, some misconceptions often occur, sometimes
leadingtowell‑intentionedbutimpracticalsuggestionslike:
“Whydon’tyoujustupdatecomponents?”
“Whydon’tyoureplacetheseinsecureprotocols?”
“Justbuynewhardware!”
While these solutions work perfectly in IT environments,the situation and requirements
within the OT world are fundamentally differentfrom typical IT requirements. Under‑
standing those differences helps to understand how many OT security challenges came to
be.
TheRealityofOTSystems
SomeofthefundamentalconceptualdifferencesintheOTworldinclude:
Decades,NotYears
• Longlifetimeofproducts : decadesratherthanyearsofoperationallife
• Think about this:Remember computer security thirty years ago? Limited encryption,
basic authentication, minimal network protections? This is our current security level in
someOTsetupstoday.
TheUpdateParadox
• Hard to Update: it’s rather hard to update a power plant. To do this you might need a
sparepowerplanttobridgethelossofpowergeneratedbythecurrently‑being‑updated
facility
2025Edition 16

<!-- page 22 -->

OWASPOTTop10 OTforITSecurityPeople
• Inothercriticaldomains,suchaslife‑sustainingmedicaldevices,updatesmightnoteven
bepossiblewithoutdirectlyendangeringusers
• Everydowntimemustbemeticulouslyplanned inadvance,unlikeITsystemsthatcan
bepatchedandrebootedquickly
ProtocolLimitationsbyDesign
• Lack of Integrity‑Protection or encrypted Protocols: due to the long lifetimes, many
OTprotocolsneithersupportencryptionnorintegrityprotection
• Within manufacturing environments, encryption is actually not a desired feature as it
makesnetworkmonitoringandtroubleshootingsignificantlymorecomplex
• Whenaproductionlinegoesdown,operatorsneedimmediatevisibilityintowhat’shap‑
pening
These are operational realities within the field with which we have to deal. Very often, we do
notworkingreenfieldprojectsbuthavetoadaptexistingsystemswhileimprovingsecurity. The
alternative‑replacingalllegacyOTsystemsimmediately‑isneithereconomicallyfeasible
noroperationallysafe.
Additional challenges includevendors not providing security updatesfor legacy systems and
deviceslackingproperaccesscontrolmechanisms byoriginaldesign.
Whenyoulookintorecentnews,OTsecurityincidentsareontherise. Whileitwouldbeprefer‑
able to have a perfectly secure solution, sadly we’re currently only catching up and thus any
substantialsecurityimprovementiswelcome.
TheMitigation‑FirstApproach
As shown above, in the OT world we often have to deal with potentially inherently insecure
devicesthatmightnotbeupdatedorupgraded. Thefundamentalapproachbecomes:
Ifwecannotmakethedevicesthemselvessecure,wetrytopreventattackersfromaccess‑
ingtheminthefirstplace.
Thisistypicallyaccomplishedthroughmitigationssuchas:
NetworkSeparation
• Air‑gappednetworkswherepossible
• VLANsandnetworksegmentation
• StrictfirewallrulesbetweenITandOTnetworks
2025Edition 17

<!-- page 23 -->

OWASPOTTop10 OTforITSecurityPeople
PhysicalSecurityControls
• Lockedcontrolroomsandequipmentcabinets
• Badgeaccesssystemsandrestrictedaccesstoindustrialfloors
• Beingableto‘lockaway’devicesandtheirnetworkshelpscompensateforprotocolswith‑
outintegrityorconfidentialityprotections
Theseremediationsarenota“getoutofjailfree”cardandimposelimitationsaswellasmain‑
tenance burden. Please note that we would prefer to have secure devices (or even zero‑trust
enableddevices)butuntilthen,oftenthosemitigationsaretheonlywayofkeepingcriticalin‑
frastructureoperational.
TheRiskCalculationProblem
As risk is typically calculated by“Risk = Likelihood × Impact”and these mitigations would
theoreticallyreducethelikelihoodtozero,weshouldbeabletoclosethecase,right?
Sadly,NO. Thisiswherethefragilityoftheapproachbecomesapparent.
WhenMitigationsFail
Theoverallarchitectureof“protectinginsecuredevicesbypreventingattackersfromaccessing
them”hasacriticalweakness: itbreaksdowncompletelyifattackersfindawaytobypass
theseprotections.
Whatcouldgowrongwithourmitigations? Considerthesereal‑worldscenarios:
TheInsiderThreat
• Your system depends upon no one introducing malware into an internal network, but
usersattachinfectedUSBsticks
• Stuxnetcasestudy: Evenair‑gappedsystemsprovedvulnerablewhentheattackvector
camefromwithin( stuxnet)
NetworkSegmentationFailures
• Missingnetworksegmentationbetweenfactoryfloorandofficenetworksleadstonumer‑
ousincidents
• Many reported “OT incidents” are actually ransomware attacks that originated in
attachedITinfrastructureandspreadduetopoornetworkboundaries
2025Edition 18

<!-- page 24 -->

OWASPOTTop10 OTforITSecurityPeople
PhysicalSecurityBreaches
• Problems with physical security allow unauthorized personnel to access factory floors
anddirectlymanipulatecontrolsystems
• UnlikeITsystemsprotectedbymultipleauthenticationlayers,OTdevicesoftenassume
anyonewithphysicalaccessisauthorized
ManagementInterfaceVulnerabilities
• ITprofessionalsuseBMCforout‑of‑bandadministration
• SimilarremotemanagementcapabilitiesinOTnetworkscanprovideattackerswithdirect
pathwaysfromITtoOTnetworks,bypassingtraditionalsecuritycontrols( ifsimilarthings
areusedwithinOTnetworks )
TheCascadeEffect
If attackers successfully compromise the perimeter, we typically encounter recurring major
problems:
InherentDeviceVulnerabilities
• Theinsecuredevicesare,bydesign,easytoexploit
• Communication between devices can be intercepted and altered due to lack of encryp‑
tionorintegrityprotection
• Defaultcredentialsandweakauthenticationarecommon
LargeBlastZones
• Attackers can use compromised devices to further propagate and pivot into other ‘se‑
cured’networksanddevices
• Trustrelationshipsbetweensystemsassumeallconnecteddevicesarelegitimate
• Networkprotocolsdesignedforoperationalefficiencyfacilitaterapidcompromiseprop‑
agation
OperationalImpact
• UnlikeITsystems,OTcompromisescanaffectphysicalprocesses
• Safetysystemsmaybetargetedorinadvertentlyaffected
• Productiondowntimehasimmediatefinancialandpotentiallysafetyimplications
Fragility is a major concern, so considering downstream implications when mitigations fail is
critical. Monitoring to detect compromise and defense in depth become essential addi‑
tionallayers.
2025Edition 19

<!-- page 25 -->

OWASPOTTop10 OTforITSecurityPeople
IncidentResponseChallenges
Comparedtowell‑maintainedtraditionalITsystems, OTsystemsoftendisplayaseverelack
ofrecoverability. Veryoften,compromisedorganizationsarenotabletoeffectivelyreacttoor
recoverfromincidents.
Thislimitationstemsfromseveralfactors :
BackupandRecoveryGaps
• Missingbackups/disasterrecoveryplansforcriticalcontrolsystems
• MissingconfigurationbackupsforOTdevices,makingrestorationdifficultorimpossible
• Undefinedprocessesforalertreporting/handling
• Limitedtestingofrecoveryproceduresduetooperationalconstraints
The“Reboot”Problem
Traditional IT incident response relies on the ability to “easily” reboot systems, reimage ma‑
chines,andrestorefromknown‑goodbackups. ThisassumptionbreaksdowninOTenviron‑
ments.
You can reboot your computer or server, but rebooting a whole factory or connected power
stationrequires:
• Coordinatedshutdownprocedures
• Safetysystemverification
• Gradualrestartprocesses
• Extensivetestingbeforereturningtofulloperation
Example:Achemicalplantcannotsimply“restart”afterasecurityincident. Eachsystemmust
be carefully verified, safety interlocks tested, and processes gradually brought back online to
preventequipmentdamageorsafetyhazards.
ThePathForward
Wehopethisintroductionexplainswhyweoftenhavetomakecompromisestoachievemean‑
ingful security improvements in OT environments. In legacy settings, this mostly means de‑
pendinguponmitigationssuchasnetworksegmentationandphysicalaccessmanagement.
2025Edition 20

<!-- page 26 -->

OWASPOTTop10 OTforITSecurityPeople
While newer systems will eventually alleviate many of these problems,we still have to deal
with legacy systems to keep existing critical infrastructure running.The alternative ‑ re‑
placingalllegacyOTsystemsimmediately‑isneithereconomicallyfeasiblenoroperationally
safe.
TheDoubleMeaningofCompromise: Compromisehas anothermeaningin this context. Of‑
tenweover‑relyonmitigationsandwhenthosearenotupheld,oursystemsbecomecompro‑
mised. If there are no additional defense‑in‑depth measures in place, the potential fallout is
immenseasfurthercompromisablesystemsareoftenwithintheblastradius. Thismakesaddi‑
tionalhardeningevenmoreimportantthanintraditionalITsystems.
KeyTakeawayforITSecurityProfessionals: Understanding these unique constraints is the
first step toward contributing meaningfully to OT security solutions that work within opera‑
tionalrealityratherthanagainstit.
Gettingcriticalinfrastructuresecurewillbequiteajourney. Butthatisnoexcusefornot
startingthisjourneyrightnow.
The path to OT security requires bridging two worlds ‑ the methodical, safety‑focused culture of
operationswiththeadaptive,threat‑focusedmindsetofcybersecurity.
2025Edition 21

<!-- page 27 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
SecurityforOT:WhyIsItProblematic?
While the term “operational technology” (OT) is fairly new, originating in the early 2000s, the
underlying technology is not. Ranging back to mechanical control systems, industrial control
systems(ICS)forexamplehavecomealongway.
PLCs were already introduced in the 1960s, predating the first personal computer (the Ap‑
ple 1 in 1976) by over a decade. Also, the integration with SCADA, starting in the 1980s, took
placeatthesametimeastheInternetwasjustbeginningtobecomeestablishedmorebroadly.
Thislong‑standinghistorycreatedaveryspecificcultureamongsttheengineersandoperators
designingandusingsuchsystems,comingwithitsowntenets,viewsandbestpractices.
TheHistoricalContext
Naturally,attheonsetofOT,maliciousattackerswerenotaproblemtobethoughtof–atthat
time they weren’t even for IT. But even when cyber‑attacks finally materialized increasingly,
theysparedOTbylarge. Thetechnologywas:
• Difficulttounderstand
• Evenmoredifficulttogetaccessto
• Systemsdidnotfeaturethekindofconnectivitytheydotoday
• TheattacksurfacewasfarbiggerandmorerewardingontheITside
It should come to no surprise therefore that in comparison tosafety – which was and is
paramount in OT – security was never a large concern historically. With operators coming
mainlyfromanengineeringbackground,theyalsodidnotpickuptheculturalsecuritychanges
thathavemanifestedintheITcommunityoverthelastdecades.
TheTurningPoint: StuxnetandBeyond
Forquitealongtimethisdidnotprovetobeproblematic,attacksalmostexclusivelytargetedIT
systems. Butthen,in2010,thediscoveryofStuxnetsentshockwavesthroughthesecurity
community,puttingICSandsoonOTingeneralinanever‑increasingfocus.
OverhalfacenturyaftertheintroductionofthefirstPLCs,therateofoccurrenceofICS‑related
attacksandmalwarestartedtorisesteeplythroughoutthe2010swiththetimebetweenattacks
everdecreasingsince.
2025Edition 22

<!-- page 28 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
NotableAttacks:
• Industroyer(2016)
• TRITON(2017)
• Industroyer2(2022)
These are just some of the most infamous attacks, showcasing how security incidents can de‑
gradesafetyandavailability –thetraditionaltopconcernsinOT.
CurrentChallenges
While cultural security issues mentioned above still persist (but are decreasing), OT often suf‑
fersfromadditionalstructuralandorganizationalproblemswhentryingtotacklethegrowing
threatfrommaliciousactors.
KeyIssues:
• Manyorganizationssimply cannoteasilyupdate orsubstitutevulnerablesystemslikeit
ismostlypossibleinIT
• Theadage “neverchangearunningsystem” becomesevenmoretruewhendealingwith
criticalinfrastructure
• Systemshavea verylonglifetime ,exposingthemtooutdatedsoftwareandsubsequent
knownvulnerabilities
Example:Itissimplynotpossibletoshutdownawholepowerplantonshortnoticetoinstall
anemergencypatchforanewlydetectedvulnerability.
All these factorsand more– growingthreatlandscape, increasingconnectivityin OTformore
efficient management and operation, insufficient security – have lead governments and regu‑
latorybodiesaroundtheworldtointroducelegislationeffectivelyforcingtheOTcommunityto
evolvetheirsecuritycultureandposturelikeIThasdoneoverthelasttwodecades.
CommonProblemsandFalseAssumptionsAboutOTSecurity
Changing cultures and even more so carefully engineered complex and critical systems like
power plants, production sites and traffic control systems has the potential to cause friction
and problems. This is totally understandable, as even in IT the introduction of new security
technologyandmeasurescancreatemajorpainpointsinthebeginning.
2025Edition 23

<!-- page 29 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
Important: Neglecting security for a short‑time saving of money and effort is a perfect
setup for even more complications in the future when legislation tightens or if an actual
attackhappens.
Thinkaboutitthisway: Whensecuritymeasuresareplannedandintroduced, youdictatethe
circumstances, the execution time and potential downtimes. But when you have to respond
toasecurity‑relatedincidentthecircumstancesdictateeverything. Youthenhaveverylimited
sayindowntimes,requiredresourcesandaboveallthetimewhenithastohappen.
Securityvs.Safety
“Wedonotneedsecurity,wehavemorethanenoughsafetymechanismsinplace”
Asacknowledgedbefore, safetyisparamount –andwithgoodreason! Anexplodingturbine
affectingthelivesofoperatorsarounditisundeniablymoreseriousthanafileserverinanoffice
gettingencryptedbyransomware.
LookingatsafetyinOTrevealshowdiligentlytheOTculturetreatsrisktolife. Mostofthetime,
therearemultiplelayersofsafetymechanismsensuringthateveninfaceoffailureofonelayer,
anotheroneintervenes.
Defense in Depth This concept, commonly referred to as“defenseindepth” , is also highly
relevanttoOTsecurity. Buteveninfaceoftheseintricatesafetymechanisms,thinkaboutcases
wheresafetysystemsareexplicitlytargetedbymaliciousactorstopreventthemfromkicking
in.
CaseStudy: RecalltheaforementionedTRITONmalwarethatexplicitlytargetedthesafetysys‑
temsofapetrochemicalplant.
KeyInsight: Securityisanactiveenablerofsafety. Ifsecurityiscompromised,thiscanposea
directthreattosafetysystemsandmechanisms. Therefore,safetyandsecuritycannotbeseen
asredundantbutare twosidesofthesamecoin tryingtoachievethesamegoal–keepingthe
systemsrunninginasafestate.
Securityvs.Availability
“Wecannotharden/updatesystemstomakethemsecureaswecannotaffordthedowntime”
Systemavailabilityisonlysecondtosafetyinmostcases,sonaturallymanysystemscannotsim‑
plybetakendowntointroduceupdatesorchangeconfigurations. Thisisoftenhardtograspfor
2025Edition 24

<!-- page 30 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
securityprofessionalscomingfromanITbackground. Everydowntimehastobemeticulously
plannedinadvance.
Butthisdoesnotmeanthatdowntimesareimpossibleingeneral. Theydohappen! Every
componentneedsmaintenanceatsomepointintimeandOTstaffisusuallyhighlyexperienced
toalignsuchmaintenancedowntimeswithbusinessgoalsandpossiblyexistingregulatoryre‑
quirements.
Solution: Security Roadmap These time frames should therefore also be used to introduce
security‑relevant topics. To do so, asecurityroadmap detailing what measure can be imple‑
mentedatwhatmaintenancedowntimehastobecarefullycrafted.
Assaidbefore,thisisyouradvantagewhenyoutacklesecurityinapro‑activeway– youdecide
onwhensomethinghappens!
PatchManagementChallenges Ofspecialconcernispatchmanagement,as:
1. Patchesareusuallyreleasedmoreoftenthantherearemaintenancedowntimes
2. Oldersystemsoftendonotreceivepatchesatall
Solutions:
• Establishaprocessratingtheseverityofapatch
• Alignupdatesandtheirurgencywithmaintenancetasks
• Moreuncriticalpatchescanbepostponedtoalaterpointintime
• Forcriticalemergencypatches,makeplansinadvance(oftentogetherwithsuppliers)
• Use“defenseindepth”approachforsystemsthatcannotbepatched
TrustingtheBlastZones
“Our systems are isolated so there is no way to access them anyway. We therefore do not
needfurthermeasures”
Physical security and isolation are often a major strength in OT environments, far surpassing
typical IT environments in that regard. Nonetheless,relyingonaccesscontrolalonecanbe
deceptive.
Surely, most environments won’t face the kind of intricacy and effort of nation‑state attacks
like Stuxnet (which breached air‑gapped systems), but just think about a scenario where an
employeeplugsinaUSBstickthatisprivatelyowned. Ifthestickisinfectedwithmalware,your
OTenvironmentcanbecompromisedsoon– withoutanyconnectiontotheoutside!
Solution: Thisisagoodcasefor“defenseindepth”again: Physicalaccesscontrolandnetwork
segmentationarebothimportantfactorsinacomprehensivesecuritystrategy. Withoutthem,
2025Edition 25

<!-- page 31 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
thestrategycanbarelybecalledcomprehensive, butontheirowntheyalsoarenotsufficient
formodernthreatlandscapes.
Securityvs.Performance
“Wecannotaffordtohaveanydelaysinnetwork/system/etc. performancecausedbysecurity
technology”
Thiscanindeedbeamajorproblem. EspeciallyOTprotocolsoftencatertoveryspecificperfor‑
mancerequirementslike real‑timecommunication. Asmostoftheseprotocolsarequiteold,
securitywasnottakenintoaccountduringcreation.
CurrentState:
• Somenewerprotocolswithsecurityfeatures(like OPCUA)
• Someolderonesoffersecurityextensions(like PROFINET)
• Oftennotsupportedbyvendorsornotapplicabletocertaintasks
Alternative Approaches: If the protocol layer cannot be secured, then other mitigations
like:
• Carefulnetworksegmentation
• Monitoringsystems
cansignificantlyimprovesecurityposture. EspeciallyastheOTsecuritymarketisevergrowing,
moreandmorevendorsarecomingupwithspecificOTsecurityproductstakingintoaccount
thecomplexrequirementsofmanyOTenvironments.
ExperienceNote: Duringtheyears‑longexperienceoftheauthorsofthisdocument,therewas
neverthecasethattherewerenopossiblesecurityimprovementsfortheenvironment. Secu‑
rityisnota“onesizefitsall”productbuthastobe tailoredtoeverysystemandenvironment ,
tofindthebestpossiblebalancebetweensecurityandperformance/availability.
KnowledgeGaps
“Weareengineers,wedonothaveknowledgeaboutsecurity”
This is also described in the beginning above. OT staff has in general a completely different
backgroundandviewonsecurity/safetythanITstaff. Whilethisatfirstseemstobeahindrance,
itdoesnothavetobethatway .
2025Edition 26

<!-- page 32 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
TheValueofOTKnowledge In‑depthOT‑specificknowledgeiscrucialin:
• SecuringOTenvironments
• Detectingandrespondingtosecurityincidents
• Craftingtailoredsecuritystrategies
Typically,theengineersworkingwiththesystemsarethefirsttonoticestrangebehavior,being
theprimarysourceof(human)detection ofattacks. Theyalsoknowthespecificcharacteris‑
tics,therequirementsandtheprocessescomingwiththeirsystems.
BridgingtheGap Thelackofsecurityknow‑howcanbetackledinseveralways:
Option 1: Collaboration ApproachIf there already is security personnel and no specific OT
security team is planned, a closer collaboration between IT and OT staff can lead to greater
understandingonbothsides.
• IT security staff can come up with viable solutions for OT security problems once they
graspthedifferencebetweenITandOT
• OTstaffdonothavetobecomein‑depthsecurityexperts
• EnableOTpersonneltothinklikeanattackerandseepotentialvulnerabilitiesbeforehand
• OTpersonnelalreadyworkwith(safety)riskseveryday,sotherequiredmentaleffortis
oftennotthathigh
Option 2: Training and EducationThere is a steady increase in educational material for OT
security:
• FreedocumentsontheInternet
• Instructor‑ledtrainingprograms
• SpecificOTsecurityteams(requirestimeandmoneyinvestment)
Important:Givingadditionalsecuritytaskstoanalreadyoverworkedstaffisarecipefordisas‑
ter. Managementmustensurethatthereareenoughresourcesforthoseresponsible. Security
isnotsomethingthatcanbedonebesides!
SecuritybyObscurity
“Weareasmallpowerplant/productionsite/orsimilar. Nobodywillmaketheefforttoattack
us”
ThisisasentimentthatisoftenalsosharedbyIT. Plainandsimple,thisisadangerousfallacy
thatdoesnotresembleongoingthreats.
2025Edition 27

<!-- page 33 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
CurrentThreatLandscape:
• Whilesophisticatednation‑stateattacksaffectonlyaverysmallsubsetofallOTenviron‑
ments
• Threatreportsshowawarenessofmaliciousactors(criminal,hacktivists)forOTisonthe
rise
• Rudimentarymalwarecanleadtodisruptionandavailabilityissues
• RiseofOTransomware ‑atypeofmalwarethathasbeenhauntingITforyears
Opportunistic Attacks In general, more and more OT incidents do not happen because of a
specificinterestinthetarget,butdueto:
• Opportunism
• Chancetoextortmoney
• Amplifyacertainpoliticalmessage
byattackingacoincidentallyvulnerableOTenvironment(e.g.,newlyvulnerableremoteaccess
solutionsthathavetobereachableovertheInternet).
ProblemswiththeSupplyChain
“Evenifwewanttointegratesecuritymore,manyofoursuppliersdonotfeaturesecurityin
theirproducts”
Yes,thiscanbeaproblem. Whileregulationsforcemoreandmorevendorstoconsidersecurity
intheirnewproducts,thisdoesnothelpwithalreadyexistingsystems.
However: Security can be done in many ways and as described before, there are security
workaroundsforalmostallproblems. “Defenseindepth”isagainthekeyword tolookfor.
Example Approach: If there is no security control for one specific component (e.g., a PLC),
thentheadditionallayersofaDiDapproachcanprovidesecurityby:
• MonitoringthenetworkofthePLCs
• Restrictingaccesstothisnetworksegment
• Providingstrictaccesscontrolforengineeringviadedicatedandisolatedworkstations
• Andsoon…
2025Edition 28

<!-- page 34 -->

OWASPOTTop10 SecurityforOT:WhyIsItProblematic?
AdvantagesofSecurity
Allinall,whensecurityisdonetherightway,itshouldneverbeahindrance,but anenablerto
aresilient,availableandsafeOTenvironment .
Whileameticulouslytailoredsecuritystrategyensurescompliancewithexistingandupcoming
legislationandregulations,trulylivingthestrategybringsmanyoperationaladvantages:
KeyBenefits:
Higher confidence in safetyof systems as deliberate attacks against safety systems is made
moredifficult
Moreresilientinfrastructure leadingtolessdowntimeofsystemsincaseofanincident
Greaterinsightinexistingassets asaresultofneededanalysesofstatusquo
Easiermanageabilityofnetworks duetoappropriatesegmentation
Moreinsightintonetworktraffic duetoincreasedmonitoring–notonlysecurity‑relatedinci‑
dentscanbedetectedandhandledfaster
Securityandsafetyworkingtogetherforamoreresilientoperationaltechnologyenvironment.
2025Edition 29

<!-- page 35 -->

OWASPOTTop10 RelatedFrameworks,Standards,andRegulations
RelatedFrameworks,Standards,andRegulations
While this document explores the unique challenges in OT networks and systems, there are
establishedstandardsbothfrom OWASPandotherorganizationsthatcanprovideusefulinfor‑
mationforsuppliers,integratorsandoperatorsalike.
Additionally, like mentioned in the introduction, there is also a number of frameworks, laws,
andregulations.
Frameworks
MITREATT&CKFramework
TheMITREATT&CKframeworkisacomprehensiveknowledgebaseofcyberadversarytactics,
techniques and procedures (TTPs). It is widely used in cybersecurity to help understand, de‑
tectandrespondtocyberattacks. TheMITREATT&CKframeworkisalivingframeworkthatis
regularlyupdatedbasedonreal‑worldobservationsofattackerbehaviour. Itprovidesastruc‑
tured way to describe how attackers operate, with a focus on how they compromise systems
andmovethroughanetwork.
StandardsofOtherOrganizations
IEC62443
IEC62443is theseriesofstandardsforOTenvironments. Theseriesaimstodevelopcybersecu‑
rityrobustnessandresilienceintheindustrialcontrolsystemsandtheirenvironments. Itoffers
severalstandardsforoperators,integratorsandsuppliers,forexample:
Operators:
• IEC62443‑2‑1 SecurityprogramrequirementsforIACSassetowners
• IEC62443‑2‑4 RequirementsforIACSserviceproviders
Integrators:
• IEC62443‑2‑4 RequirementsforIACSserviceproviders
• IEC62443‑3‑2 Securityriskassessmentandsystemdesign
• IEC62443‑3‑3 Systemsecurityrequirementsandsecuritylevels
Suppliers:
• IEC62443‑4‑1 Secureproductdevelopmentlifecyclerequirements
• IEC62443‑4‑2 TechnicalsecurityrequirementsforIACScomponents
2025Edition 30

<!-- page 36 -->

OWASPOTTop10 RelatedFrameworks,Standards,andRegulations
NISTSP800‑82r3
NIST’sSpecialPublication800‑82Revision3“GuideToOperationalTechnology(OT)Security”
offers comprehensive guidelines on how to securely deploy and operate OT systems and de‑
vices. ThedocumentprovidesanoverviewofOTandtypicalarchitecturesandsystemtopolo‑
gies, looks and common OT threats and vulnerabilities and also gives recommendations on
mitigationsforidentifiedrisks. Duetothis,thepublicationisespeciallyrelevantforoperators
andintegrators.
NISTCybersecurityFramework(NISTCSF)
NIST CSF is a framework introduced by NIST to standardize the approach to managing cyber
riskacrosssectors. In2024thesecondversionwasreleased. CSFisapplicabletoITaswellas
OTandthereforeisahelpfulresourceforalloperators.
ISO/IEC27000
TheISO/IEC27000standardseries–bestknownforthe27001standard–definesrequirements
toestablishaninformationsecuritymanagementsystem(ISMS).WhileISO/IEC27001includes
those definitions and controls in its annex, ISO/IEC 27002 provides proven guidelines on how
to implement those controls. Widely established in IT environments, ISO/IEC 27000 series
nonetheless can be valuable for operators and integrators, as many of the processes and
the security management from IT can also be adopted to OT. This becomes even more true,
whenITandOTsecurityareintegratedinaholisticapproachtosecuritythroughoutthewhole
organization.
NERCCIP
NERCCIP,shortfor NorthAmericanElectricReliabilityCorporationCriticalInfrastructureProtec‑
tion,isaseriesofstandardsregulatingthecybersecurityofbulkelectricsystem(BES)inNorth
America. ComplianceismandatoryforBESoperatorsinthecontinentalUnitedStates;theCana‑
dian provinces of Alberta, British Columbia, Manitoba, New Brunswick, Nova Scotia, Ontario,
Quebec,andSaskatchewan;andtheMexicanstateofBajaCaliforniaNorte.
TISAX
Trusted Information Security Assessment Exchange(TISAX) is anotherstandardforinformation
security management systems. Originally based on ISO/IEC 27001 and adopted for the auto‑
motive industry, TISAX nowadays is quite different to ISO/IEC 27001. In 2024, version 6.0 was
released. TISAXisonlyapplicabletostakeholdersactiveintheautomotivesector.
2025Edition 31

<!-- page 37 -->

OWASPOTTop10 RelatedFrameworks,Standards,andRegulations
IEC62351
IEC62351isdevelopedbyIECTC57(Technicalcommittee)andisaseriesofstandardsforthe
securityofpowersystemcontrolcentersandcommunicationnetworks. Especiallyrelevantfor
suppliersandintegratorsintheenergysector.
Regulations
EUNIS2Directive
NIS 2, superseding NIS 1, is a EU‑wide legislation aiming at improving the overall level of cy‑
bersecurity in the European Union. Published in 2022, all EU member states must adopt the
directivethroughnationallawstartingwith17October2024. Allenterprisesandorganizations
in scope of NIS 2 are required to fulfill technical and organizational security measure (details
have to be defined by the member states) and are subjected to strict mandatory reporting in
caseofincidentswithsignificantimpact. Allmediumandlarge‑sizedcompaniesmeetingacer‑
tain threshold in 18 critical sectors are included in the scope of NIS 2. It is therefore a highly
relevantlegislationforoperators.
EuropeanCyberResilienceAct(CRA)
TheCRAisanupcominglegislation(asof2024),whichintendedgoalistostrengthenthedevel‑
opmentofsecureproductsthatareplacedontheEUmarket. Inscopeareallproductswithdigi‑
talelementswhoseintended,orreasonablyforeseeableuseincludesadirectorindirectlogical
orphysicaldataconnectiontoadeviceornetwork. TheCRAdefinesessentialrequirementsfor
secure design, development and production, requirements on the vulnerability handling pro‑
cessesputinplacebymanufacturers,rulesfortheplacingonthemarketofaffectedproducts
andrulesonmarketsurveillanceandenforcementofallmentionedrequirements. CRAapplies
towhoeverbringsanaffectedproductintotheEUmarket.
EUMachineryRegulation
ThenewEUMachineryRegulationwillcomeintoforceon14January2027andwillreplacethe
currentlyexistingMachineryDirective2006/42/EC.Theregulationsetsrequirementsforthesafe
manufacture, commissioning, operation and maintenance of machines and associated prod‑
ucts,wheresafetyandsecurityarebothstressed. Itwillaffectoperators,integrators,suppliers
aswellasimportersanddistributors.
EURadioEquipmentDirective
TheRadioEquipmentDirective(RED)regulatestheplacingofradioequipmentontheEUmar‑
ket for manufacturers and importers. Additional to existing requirements concerning safety,
2025Edition 32

<!-- page 38 -->

OWASPOTTop10 RelatedFrameworks,Standards,andRegulations
radioperformanceandelectromagneticcompatibility,anextendingrequirementaimingtoim‑
provecybersecurity,privacyanddataprotectionofradioequipmentwillcomeintoforceon1
August2025.
ExistingVulnerabiltyLists
Issuer Title Description
BSI ICSSecurityTop9threats
andcountermeasures2022
Focusonimpactandvectors
(malware,phishing,DDoS,
sabotage)
CISA TopTenCybersecurity
Misconfigurations
ENISA PowerSectorDependencyon
TimeService
ratherspecific
ENISA TransportThreatLandscape
ENISA Cybersecurityandresilience
forSmartHospitals
ENISA ENISAThreatLandscape
2023
Figure8(Page16),givesa
per‑sectorattackoverview
MappingTable
AMappingtable linkingtheOWASPOTTop10itemstosomeofthementionedrelevantstandard
andregulationrequirementsisprovided.
2025Edition 33

<!-- page 39 -->

PartIII
TheTop10

<!-- page 40 -->

OWASPOTTop10 TheOWASPOperationalTechnologyTop10
TheOWASPOperationalTechnologyTop10
During the discussions, we agreed upon the items of the top 10 list while the respective rank‑
ing was highly subjective. We selected the Top 4 items as there was consensus that these are
fundamentalforOTsecurity:
1. UnknownAssetsandUnmanagedExternalAccess
2. DeviceswithknownVulnerabilities/Issues
3. InadequateSupplier/SupplyChainManagement
4. LossofAvailability
Thenextfiveitemswerealldeemedtobeofsimilarhighimportance:
5. InsufficientAccessControl
6. MissingIncidentDetection/ReactionCapabilities
7. BrokenZonesandConduitsDesign
8. MissingAwareness
9. Components/ProtocolswithInsufficientSecurityCapabilities
Thefinalitemisnotasecurityissuebyitselfbutwouldhavepreventedmanyoftheincidents
reportedfromthefield. WethusincludeditasfinalitemintheTop10list:
10. MissingHardening
StructureofEachTop10Item
EachentryintheOWASPOTTop10willbeaccompaniedbyashortdescription,publicincidents
exploitingthatentry,recommendedmitigationandcountermeasures,aswellasreferencesand
toolingtoassistinaddressingtheidentifiedrisks.
Field Description
Name Name/TitleoftheItem
Description Showdescriptionoftheitem
Rationale Whydidwefindthisitemimportantenough
forinclusion?
KnownAttacks/Examples Whataredocumentedattacksthatutilized
therespectiveTop10item?
2025Edition 35

<!-- page 41 -->

OWASPOTTop10 TheOWASPOperationalTechnologyTop10
Field Description
Mitigation/Countermeasures Therewillbemultiplelevels: 1)designand
implementationlevelmitigationsfor
developers/builders;2)operational
mitigationsforintegrators,e.g.,air‑gapping
systems
NextActionableSteps Whatcanbedonetoidentifyand/ormitigate
theissue?
References Relevantstandards,LinkstoTools,and
BackgroundInformation
Methodology
The project started Autumn 2024 with a meeting of the OWASP OT Top 10 leaders and subse‑
quent announcements to the community. During monthly meetings we discussed potential
Top10itemsandtheirrelevance. Startingwith2025,weincreasedthefrequencytoonemeet‑
ingeverytwoweekstofinalizethealphaversion.
In addition to the expert opinions, we also gathered empirical data from both offensive and
defensivecompaniesandexperts. Thisdatawasusedtovalidatetheproposedtop10listand
ensurethatitaccuratelyreflectsthecurrentstateofOTsecurity.
2025Edition 36

<!-- page 42 -->

OWASPOTTop10 1.UnknownAssetsandUndocumentedServices
1 UnknownAssetsandUndocumentedServices
Arguablythebiggestthreattoanetwork(ITandOT)isunmanagedandunknownassets. This
caneitherbeunknownassetsthatarepluggedintoyourlocalOTnetwork, orundocumented
services(intheworst‑caseavailablefromthepublicinternetand withoutsufficientaccesscon‑
trol.
Thereisanoverlapwiththe MissingIncidentDetection/ReactionCapabilities asincidentdetec‑
tiondependsuponhavingacompleteinventoryoftheenvironment. Ifwedonotknowwhatis
inourenvironment,wecannotdetectifsomethingishappeningtoit.
1.1. Description
UnknownassetsaredevicesorsystemsinanOTenvironmentthatarenotproperlyidentifiedor
documented. These assets can include legacy systems, unmanaged devices, or unauthorized
connectionsthatarenotaccountedforintheorganization’sinventory.
Thisisyourtypical“shadowIT”problem,butintheOTworld,itcanbeevenmoredangerous.
Unknownassetscanbeanythingfromaroguedeviceconnectedtothenetworktoanundocu‑
mentedservicerunningonaserver. Theseassetscanintroducevulnerabilitiesandweaknesses
intothesystem,makingiteasierforattackerstogainaccessandmovelaterallywithinthenet‑
work.
These assets are mostly already or will become outdated over time and introduce vulnerabil‑
ities and weaknesses into the system. Such assets can for example be used as initial access
pointsintothenetwork,forprivilegeescalation,establishingpersistenceorlateralmovement.
Havingafullinventoryofassetsthatnotonlyincludesdevicesbutalsoestablishedremoteac‑
cess,deployedprivilegesandotherservicesiscrucialtounderstandingtheenvironmentweare
workingwith.
Undocumentedservicescanbeanyservicethatisnotproperlydocumentedormanaged,such
as remote access solutions, cloud services, or third‑party applications. These services can in‑
troduce vulnerabilities and weaknesses into the system, making it easier for attackers to gain
accessandmovelaterallywithinthenetwork.
Aspecialcaseofundocumentedservicesareunmanagedexternalmaintenanceaccounts. They
are often used for increased convienience but offer adversaries ample attack opportunities.
Thiscanbeseenasacaseof missingawareness.
UnmanagedExternalAccess
Unmanaged external access refers to connections to the OT environment that are not prop‑
erly controlled or monitored. This can include remote access solutions, such as TeamViewer
2025Edition 37

<!-- page 43 -->

OWASPOTTop10 1.UnknownAssetsandUndocumentedServices
orVPNs,thatarenotdocumentedormanagedbytheorganization. Theseunmanagedconnec‑
tionscanprovideattackerswithawaytobypasssecuritycontrolsandgainunauthorizedaccess
totheOTenvironment.
UnmanagedAccessforMaintenance
Unmanagedaccess for external personnel refers to situations where third‑party vendors, con‑
tractors, or maintenance personnel have access to from within the OT environment without
proper oversight or documentation. This can lead to unauthorized changes, vulnerabilities,
andpotentialsecuritybreaches.
Anexamplewouldbethird‑partycontractor(thatisconnectedtotheinternalnetworkthrough
VPN) that has access to the OT environment for maintenance purposes but does not follow
proper security protocols or does not have their access documented. This can lead to unau‑
thorizedchanges,vulnerabilities,andpotentialsecuritybreaches.
1.2. Rationale
Historyhasshownthatundocumentedassetscanbeusedbyattackersforeverythingfromini‑
tialaccess,viapriviledgeescalationuptocompletingtheactiononobjectives. Hardeningand
segmentation measures can only be complete if all the assets are known and under consider‑
ation. Getting an overview of my networkis alwaysand therefore the mostcrucial stepwhen
startingwithasecurityprogram. ItisalsothefundamentalprerequisiteforeveryISMS,CSMS,
andotherframeworks.
1.3. KnownAttacks/Examples
• Stuxnet
• Triton
• WannaCry
• ColonialPipelineHack : Theattackersgainedaccesstothesystembymeansofacompro‑
misedpasswordforadisusedVPNaccount.
• Someone tried to poison a Florida city by hijacking its water treatment plant via
TeamViewer,sayssheriff
• CISAandtheEnvironmentalProtectionAgency(EPA)warnedwaterfacilitiestodaytose‑
cureInternet‑exposedHumanMachineInterfaces(HMIs)fromcyberattacks.
1.4. Mitigation/Countermeasures
DesignandImplementation
• OT‑environemtsarestaticbydesign. Duringthebuildingphase,thedesignerorintegra‑
tornormallyprovidesadetaileddescriptionoftheenvironment. Changestotheenviron‑
2025Edition 38

<!-- page 44 -->

OWASPOTTop10 1.UnknownAssetsandUndocumentedServices
mentmustbedocumented. Itiscrucialtohavethedocumentationprocessaspartofthe
changeprocessorchangemanagementpolicy.
• Ifonestartswithanalreadyexistingenvironment,thefirststeptoacompleteassetinven‑
tory can be to take a pen and a piece of paper, go through the location and write down
everydevicethatcanbeseen. Thisisnotonlyrestrictedtomanufacturingorpowerplants,
butalltypesofenvironmentsweareworkingin.
Operational
• mitigations for integrators/builders: Provide the documentation to the customer/asset
owner.
• Implement asset discovery and inventory management tools to identify and document
allassetsintheOTenvironment.
• Regularlyscanandmonitorthenetworkforneworunknowndevices.
• Performport/trafficmonitoring.
• Enforce strict access controls and authentication mechanisms to prevent unauthorized
devicesfromconnectingtothenetwork. Alsoassumeroguedevices/servicesinthenet‑
workwhendesigningsecuritymeasures.
1.5. NextActionableSteps
• ConductathoroughinventoryofalldevicesandsystemsintheOTenvironment.
• Implementnetworkscanninganddiscoverytoolstoidentifyunknownassets.
• EstablishaprocessfordocumentingandmanagingchangestotheOTenvironment.
• Regularlyreviewandupdatetheassetinventorytoensureaccuracyandcompleteness.
1.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
• Followingadditionalstandardsarerelevant:
– NERCCIPID.AMAssetManagement
– NERCCIPPR.ACIdentityManagementandAccessControl
– NIST 1800‑23 Energy Sector Asset Management: For Electric Utilities, Oil & Gas In‑
dustry
– NIST1800‑5ITAssetManagement
2025Edition 39

<!-- page 45 -->

OWASPOTTop10 1.UnknownAssetsandUndocumentedServices
Tooling
• NetworkScanningandDiscoveryTools: : NmapisthestandardOSSactivenetworkscan‑
ning tool. Be aware that it can be intrusive and may disrupt operations in a production
environment. Shodan is a web‑based search engine that can help identify devices con‑
nectedtotheinternet,includingthoseinOTenvironments.
• NetworkMonitoringTools: : WiresharkisanOSSnetworkprotocolanalyzerthatcancap‑
tureandanalyzenetworktraffic,helpingtoidentifyunknowndevicesandservices.
2025Edition 40

<!-- page 46 -->

OWASPOTTop10 2.(Accessible)DeviceswithKnownVulnerabilities/Issues
2 (Accessible)DeviceswithKnownVulnerabilities/Issues
Attackers love to find software/hardware with known vulnerabilities, especially if exploits are
already available. Given a sufficiently devastating vulnerability, all other defenses are naught
andtheattackercantakeoverthedevice.
Thiscanbeusedforinitialaccess,e.g.,whenexploitingpublicfacingservicessuchasVPNs,or
canbeusedwithinthetargetnetworkforLateral‑MovementorPrivilege‑Escalation.
2.1. Description
Ifanattackerisabletoaccessasystemwithknownexploitablevulnerablecomponents,most
other defense mechanisms are useless. The attacker will be able to take over the system, the
onlydefensesthatremainarethose thatreducethe pwneddevice’sblastradius, i.e., reduces
thesystemsthatanattackercanattack“out‑going”fromthecomproiseddevice.
In traditional IT, the typical recommendation is to upgrade. This does not work in OT due to
safetyconcerns,mandatoryupdatetime‑windows,andgenerallylongerlifetimesofusedcom‑
ponents. ComparedtoIT,OTworksataglacialpace.
Asupdatesaresometimesnotpossible,mitigationssuchasnetworksegregationareused. This
preventsvulnerablesystemstobecomeaccessibletoattackers. Alas,thesecounter‑measures
do not solve the problem: if there is a vulnerability within the counter‑measure, the original
vulnerabilitycanstillbeexploited. ThisoftenmakesOTsystems veryvulnerableagainstunex‑
pected admin accessorbadly designed zones: once the attacker is in the network, they have
accesstoexploitablesystemsandcancommencefromthere.
WhyCan’tWeJustUpgradeAlltheSystems?
ToreiterateonthespecialproblemsthattheOTworldfaces,wewanttogivealistofcommonex‑
cuses/reasongiventhatcouldpreventaneasyimplementationofavulnerabilitymanagement
system:
Youdon’tjustupgradeamedicaldeviceorpowerplant : thisisnotyourtypicaldesktopPC
where you are annoyed if an update breaks your system for a couple of days, this is critical
infrastructure upon which lifes potentially depend upon. Imagine you are depending upon a
digitalpacemakerorinsulinpump: wouldyoujustupdateit(withoutmakingsurethatitwill
notnegativlyimpactyou)?
Problems with the supply chain: compared to traditional IT, in the OT world we have fewer
vendors. This gives vendors power over customers, which can lead to a lack of motivation to
providesecurityupdatesornotifyifsecurityproblemswerediscovered.
2025Edition 41

<!-- page 47 -->

OWASPOTTop10 2.(Accessible)DeviceswithKnownVulnerabilities/Issues
Usageoflegacydevices : duetothelonglifetimesofOTsystems,manydevicesarestillinuse
thatweredesignedwithoutsecurityinmind. Thiscanleadtoasituationwherethedeviceisnot
able to be updated or patched, even if a vulnerability is discovered. This is especially true for
legacysystems,wherethevendormaynolongerbeinbusinessormaynothavetheresources
toprovideupdates.
MissingSecurityAwarenessontheOTside : whilesafetyisawellunderstoodandimplement
concept in OT, security is often not. This can lead to a situation where the operators do not
understandtheimportanceofsecurityupdatesanddonotprioritizethem. Thiscanbeduetoa
lackofknowledgeorunderstandingoftherisksinvolved,oritcanbeduetoalackofresources
ortimetoimplementthem.
Unknown devices and shadow infrastructure: if you don’t even know about a device, how
shouldyouknowthatyouneedtoupdateit?
Pleasenote,thatthisshows(primarilytoITsecuritypeople)whyupgradingisnotassimpleas
inotherdomainsbut doesnotmeanthatwe(asOT)canuseanyofthisasanexcusefornot
havingupdateproceduresinplace .
VulnerabilityMangement?
InsufficientormissingvulnerabilitymanagementpracticesinanOTenvironmentcanleavesys‑
temsexposedtoknownsecurityvulnerabilities. Notinstallingsecuritypatcheseventually,will
leadtoanamplificationeffectwhen(notif)theattackeriswithinthesystem.
EvenifalltheissuesmentionedinthelastsectiondonotapplyforanOTsystem, securityup‑
datesareveryoftennotapplied. Thereasonforthatis missingvulnerabilitymanagement .
2.2. Rationale
Vulnerabledevicesbad. Especiallyincriticalinfrastructure.
2.3. KnownAttacks/Examples
• APT44isapersistentandoperationallymatureadversarythatusesdiverseinitialaccess
methods ranging from common vectors such as phishing, credential harvesting, and
knownvulnerabilityexploitationtotargetedsupplychaincompromises.
• VoltTyphoontypicallygainsinitialaccesstotheITnetworkbyexploitingknownorzero‑
dayvulnerabilitiesinpublic‑facingnetworkappliances
• Sensitivenuclearinformation(SNI),theindustry’sspecialclassificationsystem,wasleft
vulnerableinpartbecauseoftheuseof“obsolete”technologyincludingWindows7and
Windows2008,Lawrencesaid.
2025Edition 42

<!-- page 48 -->

OWASPOTTop10 2.(Accessible)DeviceswithKnownVulnerabilities/Issues
2.4. Mitigation/Countermeasures
DesignandImplementation
• Trytopreventvulnerabilititesfromaccessingthesystem( OWASPSAMM2)
• Test hardware/software before deploying them in the field (OWASP IoT Security Testing
Guide,OWASPFirmwareSecurityTestingMethodology )
• Informcustomersaboutsecurityupdates. ProvideSBOMs.
• Don’tdependuponsecurity‑by‑obscurity.
• Usememory‑safeprogramminglanguagesandutilizesecurity‑featuresofframeworks.
Operational
• Make mandatory vulnerabilty notifications and remediation part of your supplier con‑
tracts.
• Keepanup‑to‑dateassetregisterwithhardware/softwareversions.
• Test hardware/software before deploying them in the field (OWASP IoT Security Testing
Guide,OWASPFirmwareSecurityTestingMethodology )
• Establish a vulnerability management program that includes regular vulnerability scan‑
ning,patchmanagement,andremediationprocesses: Prioritizecriticalsecurityupdates
andpatchesforOTsystemstoaddresshigh‑riskvulnerabilities.
• Implementnetworksegmentationandaccesscontrolstolimittheimpactofsecurityvul‑
nerabilities.
2.5. NextActionableSteps
• Inventarizeyourdevicesandservices
• gatherSBOMsandcheckforknownvulnerabilities
• testyourdevicesandservicesforknownvulnerabilitiesifpossible(pen‑testing)
• createarisk‑basedtreatmentplan,startwithmitigationsthathavethehighestimpact
• rinseandrepeat
2.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
2025Edition 43

<!-- page 49 -->

OWASPOTTop10 2.(Accessible)DeviceswithKnownVulnerabilities/Issues
Backgroundinformation
• OWASPmaintainsthe OWASPIoTSecurityTestingGuide aswellasthe OWASPFirmware
SecurityTestingMethodology ,bothofwhichprovideguidanceonhowtotestforvulner‑
abilitiesinIoTandfirmwaresystems.
• SoftwareBillofMaterials(SBOM)‑CISA describesacomponent’sdependenciesandvul‑
nerabilities in a machine‑readable format. This can be used to track known vulnerabili‑
tiesinyoursoftwaresupplychain.
Tooling
• shodan.ioallowsyoutosearchfordevicesconnectedtotheinternet,includingthosewith
knownvulnerabilities.
• OWASPdependency‑check allowsyoutoscanyouJavaprojectsforknownvulnerabilities
in dependencies. It is typically called manually during software development, but can
also be integrated into CI/CD pipelines.OWASP dependency‑trackaccepts SBOMs and
canbeusedtoperiodicallytrackknownvulnerabilitiesinyoursoftwaresupplychain. It
cannotifyyouwhennewvulnerabilitiesarediscovered.
2025Edition 44

<!-- page 50 -->

OWASPOTTop10 3.InadequateSupplyChainManagement
3 InadequateSupplyChainManagement
SupplyChainCompromise occurwhenadversariestargetweaknessesinanorganisation’ssup‑
plychain‑whetherit’shardware,softwareorservicesprovidedbythirdparties. Insteadofcom‑
promising the target directly, attackers exploit the relationship of trust between the organisa‑
tionanditsvendorsorcontractorstogainaccesstosensitiveOTsystems.
InthecontextofOT,thesupplychainmayinvolvecomplexvendorecosystems,includingsoft‑
wareprovidersforSCADAsystems,hardwaremanufacturersforindustrialequipment,ormain‑
tenanceservices. Anattackerinfiltratesthesesupplychainlinkstogainaccesstooperational
technology,bypassingtraditionalcybersecuritydefences.
3.1. Description
It is vital to protect OT supply chains, given their critical role in enabling modern society to
functionandgenerateeconomicprosperity. Thesesupplychainsfacilitatetheproduction,dis‑
tribution,andmaintenanceofessentialOTproducts,systems,andservicesthatunderpinvari‑
oussectors,includinghealthcare,finance,transportation,andnationalsecurity. Thefollowing
phasesofthelifecycleofOTcomponentsorsystemshavetobeconsideredwhendealingwith
OTsupplychains:
• Design(e.g.,requirementsspecificationandarchitecture)
• Developmentandproduction(e.g.,rawmaterialprocurementandtesting/qualityassur‑
ance)
• Distribution(e.g.,logisticsandtransportation)
• Acquisition,(e.g.,retailandsales)
• Deployment(e.g.,installationandconfiguration)
• Maintenance(e.g.,useandsupport,especiallyprovisioningofupdates)
• Disposal/decommissioning
3.2. Rationale
Dragos concluded in theirglobal oil and gas cyber threat perspectivein August 2019 that the
growingthreatofsupplychainattacksandvendorcompromisesallowsnewavenuesforactivity
groupstocompromiseITandOTenvironmentsalike.
Furthermore, examples like SolarWinds Orion and Crowdstrike threat detection software
demonstrated the scalability of supply chain issues, affecting numerous victims at the same
timebytheverysameissue.
2025Edition 45

<!-- page 51 -->

OWASPOTTop10 3.InadequateSupplyChainManagement
3.3. KnownAttacks
• SolarWindsOrionCompromise . TheSolarWindscompromisewasasophisticatedsupply
chain cyber operation that was discovered in December 2020. The cyber operation in‑
volvedtheinjectionofmaliciouscodeintotheSolarWindsOrionsoftwarebuildprocess,
which was then distributed through a standard software update. The cyber actors also
used password spraying, token theft, API abuse, spear phishing and other supply chain
attackstocompromiseuseraccountsandleveragetheirassociatedaccess.
• CrowdStrikeCompromise. In2024,acontentupdateforCrowdStrike’sFalconsensorsoft‑
warecausedglobalsystemdisruptions. The“BlueScreenofDeath”(BSOD)wastriggered
by a “Named Pipes” update intended to improve threat detection. An error in the up‑
datefile’sformattingledtotheCrowdStrikedriveraccessinganon‑existentmemoryad‑
dress, triggering the BSOD. This affected numerous industries, including airlines, which
canceledordelayedflights; healthcare, whichexperiencedissueswithmedicalrecords;
andemergency911callcenters,ofwhichupto100intheUSreporteddowntime. Theout‑
agedisruptedbusinessesrelyingonOTandconventionalIT,highlightingthewidespread
dependencyonreliabletechnologicalservices.
• Dragonfly. A cyber espionage campaign against a range of targets, primarily in the en‑
ergy sector, provided the attackers with the capability to carry out sabotage operations
againsttheirvictims. Theattackerswereabletoinfiltrateanumberofstrategicallysignifi‑
cantorganisationsforthepurposeofespionage. Hadtheychosentoutilisethesabotage
capabilitiesattheirdisposal,theycouldhavepotentiallycauseddamageordisruptionto
theenergysupplyintheaffectedcountries.
• NotPetya. ItwasbelievedthatthesoftwareupdatemechanismofM.E.Doc—aUkrainian
taxpreparationprogramthat,accordingtoF‑SecureanalystMikkoHyppönen,“appears
tobedefacto”amongcompaniesdoingbusinessinthecountry—hadbeencompromised
tospreadthemalware. AnalysisbyESETfoundthatabackdoorhadbeenpresentinthe
updatesystemforatleastsixweekspriortotheattack,describingitasa“thoroughlywell‑
plannedandwell‑executedoperation”. ThedevelopersofM.E.Docdeniedthattheywere
entirelyresponsibleforthecyberattack,statingthattheytoowerevictims.
• Denmark’sTrainNetworkFrozenDuetoCyberattackonSubcontractor .
3.4. Mitigation/Countermeasures
Establish aSupply Chain Managementthat includes policies and procedures to ensure all de‑
vicesandcomponentscomefromtrustedsuppliersandaretestedtoconfirmtheirintegrity.
DesignandImplementation
• Itisvitalthatmanufacturersofconnectablesoftwareandhardwareproductsensurethat
suchproductsaredevelopedinlinewithsecurity‑by‑defaultandsecurity‑by‑designprin‑
ciples,andthattheirsecurityismaintainedduringasupportperiod.
2025Edition 46

<!-- page 52 -->

OWASPOTTop10 3.InadequateSupplyChainManagement
• Productsshouldundergoathird‑partyconformityassessmentbeforetheycanbeplaced
onthemarket.
• Considerimplementingamulti‑vendorstrategy.
Operational
• Adedicatednotificationprocedureshouldbeestablishedintheeventofasevereincident
oranactivelyexploitedvulnerabilityinaproductthatmayaffectmultipleparties.
• It is imperative to undertake a thorough evaluation of the risk profile exhibited by sup‑
pliersonaregularlybasis. Thisevaluationshouldbeusedtodeterminethenecessityof
reducingtheriskposedbysuppliersdeemedtobehigh‑risk. Ifthecircumstancesneces‑
sitate,itisalsocrucialtoimposerestrictionsonortoexcludesuppliersconsideredtobe
high‑risk.
• Promotion of information exchange, awareness and training addressing supply chain
risks.
• Includesupplychainattacksintheregularincident,emergency,andcrisismanagement
plansandexercises.
3.5. NextActionableSteps
• Checkonaregularbasisthatcriticalsuppliershaveappropriateandproportionatecyber
securityriskmanagementmeasuresinplacetomanageidentifiedsupplychainsecurity
risks. Thismaybeconductedbysupplierassessmentsorrequiringrelevantcertifications
(e.g.,IEC62443‑4‑1,IEC62443‑4‑2).
• Ensurethatrelevantentitiesareresilienttosupplychainthreatsbyconductingprepared‑
nessorstresstests.
• Createtestplatformsorsandboxenvironmentsforsecuretesting.
3.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
Backgroundinformation
• NoteableCWSs: thefollowingCommonWeaknessEnumerationidenifierarehighlyrele‑
vanttothisTop10item:
– CWE‑912: HiddenFunctionalitydescribesanassetthatincludesfunctionalitywhich
is undocumented, not specified, and not accessible through any interface or com‑
mandsequencethatisapparenttotheasset’susersoradministrators.
2025Edition 47

<!-- page 53 -->

OWASPOTTop10 3.InadequateSupplyChainManagement
– CWE‑1361: ICS Supply Chainis a weakness category describes ICS supply chain
risks in general. Weakness in this category address for instance theIT/OT Conver‑
gence/Expansion,Common Mode Frailties,Poorly Documentedor Undocumented
Features,and OTCoutnerfeitandMaliciousCorruption .
2025Edition 48

<!-- page 54 -->

OWASPOTTop10 4.LossofAvailability
4 LossofAvailability
Availability, esp. in the context of Safety, is paramount and well‑understood in the OT world.
However,someaspectsofavailabilityarestillproblematic,e.g.,integrityispartofavailability.
Pleasenotethatwetalkaboutprotecting“our”infrastructurefromDDoSanddonottalkabout
becomingpartofabotnetafteracompromise(whichisalsoproblematic,butratherasubpart
ofMissingIncidentDetection/ReactionCapabilities )
4.1. Description
Availabilityisthepropertyofbeingaccessibleandusableupondemandbyanauthorizedentity.
InthecontextofOT,availabilityiscrucialasmanysystemsaredesignedtooperatecontinuously
andcannotbeeasilypatchedorupdatedwithoutcausingdowntime.
IntheOTdomain,availabilityisoftenregardedasthemostcriticalsecuritypropertyduetoits
directimpactonsystemfunctionalityandsafety. Ifasystemisnotavailable,itcannotperform
itsintendedfunction,whichcanleadtosafetyhazardsandotherissues. Additionally,thereis
anecdotalevidenceofOTcomponentscrashingduringnetworkscans,underscoringtheimpor‑
tanceofmaintainingavailability.
Denial‑of‑ServiceAttacks
Denial‑of‑Service (DoS) attacks are a common threat to availability. These attacks can take
manyforms,includingnetworkflooding,resourceexhaustion,andapplication‑layerattacks.
InthecontextofOT,DoSattackscandisruptcriticalsystemsandservices,leadingtosignificant
downtimeandpotentialsafetyhazards. Itisimportanttonotethatwecareabouttheprotec‑
tion of the OT system itself: if a connected cloud‑managed system becomes target of a DoS
attack and becomes not available while the OT system/process is still available, this is not an
OTavailabilityproblemforus.
Real‑TimeCommunicationSafety
One special aspect of availability in OT is the need for real‑time communication safety. Many
OTsystemsrelyon real‑timecommunicationprotocolstoensurethatdatais transmittedand
processed in a timely manner, e.g., for controlling medical devices or factory automations. If
theseprotocolsaredisrupted,itcanleadtodelaysorfailuresincriticalprocesses.
TypicalITnetworkprotocolssuchasTCP/IParenotdesignedforreal‑timecommunicationand
can introduce latency and jitter that can disrupt the operation of OT systems. Therefore, spe‑
cialized protocols and hardware are often needed to ensure real‑time communication safety
2025Edition 49

<!-- page 55 -->

OWASPOTTop10 4.LossofAvailability
inOTenvironments. Thus,real‑timecommunicationsafetyisacrucialaspectofavailabilityin
OT.
AvailabilityandIntegrity
The well known CIA triad (Confidentiality, Integrity, Availability) is often misinterpreted in the
contextofOT.Whileintegrityisoftenseenasaseparateproperty,itisactuallyacrucialaspect
ofavailability.
Imagineasensornetworkthatisusedtomonitorthetemperatureofacriticalprocess. Adirect
attackagainstavailabilitywouldbethedestructionoftheconnectedsensors. Butifanattacker
wouldperformanIntegrityattack,e.g.,floodsthesensornetworkwithfaketemperaturedata,
thenthesensornetworkitselfisstillavailablebutitssolegoal(providingacorrecttemperature
reading)iscompromisedandthusdestroystheavailabiltyoftheoverallsystem.
To protect against integrity attacks, typically cryptographic measures such as signatures or
MACs are used. However, these measures can introduce performance overhead and may not
besuitableforallOTsystems. Forexample, somelegacysystemsmaynothavetheprocessing
powerormemory tosupportcryptographicalgorithms.
AvailabilityandSoftwareUpdates
In the context of OT, software updates are often seen as a risk to availability. This is because
many OT systems are designed to operate continuously and cannot be easily patched or up‑
datedwithoutcausingdowntime. However,softwareupdatesarealsocrucialfor maintaining
thesecurityandintegrityofOTsystems .
The2024 CrowdStrike incidentis a recent example of how software updates can impact avail‑
ability. Inthiscase,automaticEDRupdatescausingsignificantdisruptioninmultipleOT‑areas,
e.g.,gasstationsandhospitals.
4.2. Rationale
• availabilityisparamountforthesafetyofOTsystems
• theimpactofintegrityonavailabilityisoftenoverlooked
• recentincidentssuchastheCrowdStrikeincidentshowthatevennon‑malicioussoftware
updatescanhaveasignificantimpactonavailability
4.3. KnownAttacks/Examples
• On Feb. 24, 2022, the night before the Russian government launched its full‑scale
invasion, Russian‑backed hackers targeted thousands of modems linked to Viasat,
the U.S.‑based satellite and internet communications company, and relied on by the
Ukrainian military. The attack — attributed to the Russian government by the United
2025Edition 50

<!-- page 56 -->

OWASPOTTop10 4.LossofAvailability
States and its allies — relied on a piece of malware that researchers with SentinelLabs
dubbed“AcidRain.”
• Stuxnet: both as an attack against availability and as an example of violating integrity
withfakedata.
4.4. Mitigation/Countermeasures
DesignandImplementation
• performariskassessmenttoidentifypotentialavailabilitythreatsandvulnerabilitiesin
OTsystems
• implementredundancyandfailovermechanismstoensurecontinuousoperationincase
ofafailureorattack
• use specialized real‑time communication protocols and hardware to ensure real‑time
communicationsafety
• implement cryptographic measures such as signatures or MACs to protect against
integrity attacks, while considering the performance overhead and suitability for the
specificOTsystem
Operational
• regularly test the implemented redundancy and failover mechanisms, e.g. during
plannedmaintenancewindows,toensuretheystillworkwhenneeded
4.5. NextActionableSteps
• performariskassessmenttoidentifypotentialavailabilitythreatsandvulnerabilitiesin
OTsystems
4.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
• The BSI Industrial Control System Security: Top 10 threats and countermeasures 2022
containsmultiplethreatsdirectlyrelatedtoavailability,e.g.,“Sabotage”,“(D)DoSattacks”,
“Technicalfailureandforcemajeure”.
2025Edition 51

<!-- page 57 -->

OWASPOTTop10 4.LossofAvailability
Backgroundinformation
• PLCs: To Scan or Not to Scan? (youtube, 20.6.2024): presentation analyzing the impact
of active scanning as well as OT‑specific targeted scanning on PLCs, showing that even
benignscanscancausecrashesanddisruptavailability.
2025Edition 52

<!-- page 58 -->

OWASPOTTop10 5.InsufficientAccessControl
5 InsufficientAccessControl
AccessControlisacriticalaspectofsecurityinanysystem,butitisespeciallyimportantinOper‑
ationalTechnology(OT)environments. Insufficientaccesscontrolcanleadtounauthorizedac‑
cesstosensitivesystemsanddata,producingseriousconsequencesforsafetyandsecurity.
Thisisanintricateproblemthattouchesonmultiplelevelsofsecurity,includingphysical,orga‑
nizational,andtechnicalmeasures.
5.1. Description
AccessControlistheprocessofrestrictingaccesstosystemsanddatatoauthorizedusers. Ac‑
cessControlisperformedonmultiplelevels:
• Organizational: Organizational access control measures, such as policies and proce‑
dures, are designed to ensure that only authorized personnel have access to sensitive
systems and data. If an organisation has no written down access matrix (which em-
ployee is allowed to operate what? ),implementingtherespectivetechnical
accesscontrolsystemisnotpossible.
• Technical: Technicalaccesscontrolmeasures,suchasauthenticationandauthorization
mechanismsmustbeimplementedwithintheusedcomponents. Thisismostlyatopicfor
systemdesignersandimplementors. Duringoperation,theseavailabletechnicalaccess
controlmeasuresmustbeusedandenforcedbytheoperatorsandemployees.
• Physical: Physicalaccesscontrolmeasures,suchaslocksandsecurityguards,areoften
thefirstlineofdefenseagainstunauthorizedaccessinOTenvironments. However,they
areoftenover‑reliedupon,leadingtoafalsesenseofsecurity.
ParticularitiesofOT
Emergency Situations Access Control and Safety can be conflicting. A good example is the
useofemergencystopbuttons. Inanemergencysituation,itiscriticalthattheemergencystop
button can be activated quickly and easily. However, this can lead to a situation where unau‑
thorized personnel can also activate the emergency stop button, leading to potential safety
hazards.
Another good example are medical devices in hospitals: you do not want to have a password
promptwhenadoctorwantstouseadefibrillator
Legacy Systems Old systems often have onlylimited security functions. Many (legacy) de‑
vicesdonotsupportauthenticationorauthorization. Asaresult,unauthorizedaccessispossi‑
ble.
2025Edition 53

<!-- page 59 -->

OWASPOTTop10 5.InsufficientAccessControl
Legacy devices often also offer no connection to a central identity management system. This
makesitdifficulttomaintainandrespondtochangesintheorganization’sresponsibilitieson
anongoingbasis
OrganizationalLevel
Onanorganizationallevel,poorlydefinedaccesscontrolcanresultin“privilegecreep,”where
usersaccumulatemoreaccessthannecessaryfortheirjob,potentiallygrantingthemaccessto
systemsanddatatheyshouldnothave.
Awelldesignedaccesscontrolsystemshouldincorporatethefollowingprinciples:
• Role‑BasedAccessControl : Usersshouldbeassignedrolesbasedontheirjobresponsi‑
bilities. Thiscanhelptoensurethatusersonlyhaveaccesstothesystemsanddatathat
theyneedtoperformtheirjobandpreventsprivilegecreep,whereusersaccumulateac‑
cessrightsovertime.
• LeastPrivilege: Users/rolesshouldonlyhaveaccesstothefunctionsanddatatheyneed
toperformtheirjob.
• SeparationofDuties : More than one person is required to perform a task. This should
beimplementedforcriticaltasks.
• ClearTrustBoundaries : Toallowforanalysis, trustboundaries havetobedefined. This
isespeciallyimportantintheOTworld, wherethePurdueModelisoftenusedtodefine
trustboundaries.
• OngoingEmployeeTraining : Veryoften,OTpersonnelarenotawareofthesecurityim‑
plications of their actions. This can lead to a situation where a system is not properly
securedbecausetheoperatorsdonotknowhowtodoit.
• DeactivatingAccounts: Whenauserleavesthecompany,theiraccountshouldbedeac‑
tivated.
ImplementationLevel
• arecontrolsinplace? aretheywellimplementedandconfiguredaccordingtobestprac‑
tices?
• given that we want to control access for, e.g., externally reachable adminitrative inter‑
faces (VPN servers, web‑panels), are implemented controls sufficient? Having a remote
managementsolutionwithoutmandatoryandenforcedmulti‑factorauthenticatorisnot
state‑of‑the‑artin2025. Norwasitin2024. Norbefore.
• havedefaultpasswordsbeenchanged? arethereanydefaultaccountsthathavenotbeen
disabled?
• havecontrolsbetested? aretheyworkingasintended?
• havephysicalaccesscontrolassumptionsbeendocumentedandtested? Itiseasierthan
somepeoplethinktogetonafactoryfloor.
2025Edition 54

<!-- page 60 -->

OWASPOTTop10 5.InsufficientAccessControl
• non‑repudiation: the system should be able to prove who did what. This principle is
brokenifthere’sashareduser/passwordlistfordevicesonthefactoryfloor.
5.2. Rationale
Theprevalenceof:
• sharedpasswordlists
• over‑dependencyonphysicalsecurity
• initialattackvector: remoteaccesswithoutmulti‑factorauthentication
5.3. KnownAttacks/Examples
• Afterquittinghisjobattheplantatthebeginningof2019,hethenusedtheremotelogin
systemagainonMarch27,2019,toshutdowntheplantandoneofitstreatmentfilters..
• ColonialPipelineHack : Theattackersgainedaccesstothesystembymeansofacompro‑
misedpasswordforadisusedVPNaccount.
5.4. Mitigation/Countermeasures
DesignandImplementation
• thinkaboutapplyingzero‑trustprinciples
• definethedifferentsystems,howtheyinteracts,andtheresultinginterfaces(trustbound‑
aries)
• definetherolesthatareneededtointeractwiththesystems
– Defineaminimalroleconcept.
– e.g.onasensor
* administrator‑>configuration
* simpleuser‑>onlyreadonlyaccesstomeasuringdata
• Implementarole‑basedaccesscontrol(RBAC)system
• Implementmulti‑factorauthentication
Operational
• Usetheprovidedfeaturesimplementedbythevendors
• Changepasswordanddefaultuser.
• performperiodicaccountreviewstocounterpermissioncreep
• Implementaprocessfordeactivatingaccountswhenauserleavesthecompany
2025Edition 55

<!-- page 61 -->

OWASPOTTop10 5.InsufficientAccessControl
5.5. NextActionableSteps
• Issensitiveinformationaccessibleviatheavailableinterfaces?
• Istherearoleconceptforthedevices/systemsandhasthisbeenimplemented?
5.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
BackgroundInformation
• PhysicalAccessControl
– Disablingunnecessaryservicesandprotocols
– WhyDisablingunusednetworkportsiscrucialinOTenvironents
2025Edition 56

<!-- page 62 -->

OWASPOTTop10 6.MissingIncidentDetection/ReactionCapabilities
6 MissingIncidentDetection/ReactionCapabilities
Thelongeranattackerisabletopenetratethenetworkunnoticed,thehigheristheprobability
thattheattackercompromisesOT.Thisalsoappliesifincidentreactionisslowortechnicallyin‑
adequate. Withoutloggingandmonitoring,breachescannotbedetected. An OTcybersecurity
reportanalysingtrendsin2024 showsthat45%ofserviceengagementshavealackofvisibility
acrossOTnetworks,makingdetections,triage,andresponseincrediblydifficultatscale.
Adversaries may seek to causeLoss of Control, whereby operators are unable to issue com‑
mands,evenwhenthemaliciousinterferencehassubsided.
Another motivation for attackers may beLoss of Productivity and Revenueby disrupting or
damaging the availability and integrity of control system operations, devices and related pro‑
cesses.
Furthermore,Loss of Protectionleading to the compromise of the functions of protective sys‑
tems designed to prevent the effects of faults and abnormal conditions may be a motivation.
This can result in equipment damage, prolonged process disruption and hazards to person‑
nel.
Finally, Loss of Safetyleading to the compromise the functions of safety systems, which are
designedtoensurethesafeoperationofaprocesswhenunacceptableordangerousconditions
occurmaybearesultofaattack. Adversariesmaytargetanddisablesafetysystemfunctionsas
aprerequisiteforsubsequentattacksortoallowfutureunsafeconditionstogounchecked.
6.1. Description
Incident detection and reaction capabilities provide security countermeasures applied when
proactive countermeasures did not prevent an attack. The following items introduce vulnera‑
bilitiesinthiscategory:
• Auditableevents,suchaslogins,failedlogins,andexecutedcommandsorscripts,arenot
logged.
• Warningsanderrorsgenerateno,inadequate,orunclearlogmessages.
• LogsofFirmware,OS,applications,andAPIsarenotmonitoredforsuspiciousactivity.
• Logsareonlystoredlocally.
• Appropriatealertingthresholdsandresponseescalationprocessesarenotinplaceoref‑
fective.
• Technicalsecuritytests(e.g.,penetrationtests,vulnerabilityscans,andmanualsecurity
testing)donottriggeralerts.
• The application cannot detect, escalate, or alert for active attacks in a reasonable short
timeframe.
2025Edition 57

<!-- page 63 -->

OWASPOTTop10 6.MissingIncidentDetection/ReactionCapabilities
6.2. Rationale
Without logging and monitoring, breaches cannot be detected. An OT cybersecurity report
analysingtrendsin2024showsthat45%ofserviceengagementshavealackofvisibilityacross
OTnetworks,makingdetections,triage,andresponseincrediblydifficultatscale.
6.3. KnownAttacks
• UkraineElectricPowerAttacks . TheUkraineElectricPowerAttackwasanoperationwhich
aimstotargetanddisrupttransmissionanddistributionsubstationswithintheUkrainian
powergrid.
• TritonSafetyInstrumentedSystemAttack . TheTritonSafetyInstrumentedSystemAttack
wasacampaignthattookadvantageoftheTritonmalwareframeworktotargetapetro‑
chemical organisation. The malware and techniques employed in this campaign were
designedtoinfiltratespecificTriconexSafetyControllerswithintheenvironment. Thein‑
cidentwaseventuallyexposedduetoasafetytripthatoccurredasaresultofanissuein
themalware.
• LockerGogaransomwareinfectsindustrialandmanufactoringcompanies. InMarch2019,
NorskHydrowassubjectedtoacyberattackthatutilisedtheLockerGogaransomwareto
encryptitscomputerfiles. Inresponse, the aluminium andrenewableenergy company
transitionedtomanualoperationsandmaintainedtransparencywiththepublicregard‑
ing its progress towards recovery. The security industry has expressed high regard for
NorskHydro’stransparencythroughoutthediscoveryandrecoveryprocess.
6.4. Mitigation/Countermeasures
ImplementNetworkIntrusionPrevention . Atnetworkboundaries,trafficshouldbeblockedus‑
ingintrusiondetectionsignatures. Whenitcomestoindustrialcontrolenvironments,network
intrusionpreventionshouldbeconfiguredsothatitwillnotdisruptprotocolsandcommunica‑
tionsresponsibleforreal‑timefunctionsrelatedtocontrolorsafety.
DesignandImplementation
• Ensure all login, access control, and server‑side input validation failures can be logged
with sufficient user context to identify suspicious or malicious accounts and held for
enoughtimetoallowdelayedforensicanalysis.
• Ensurethatlogsaregeneratedinaformatthatlogmanagementsolutionscaneasilycon‑
sume.
• Ensure log data is encoded correctly to prevent injections or attacks on the logging or
monitoringsystems.
2025Edition 58

<!-- page 64 -->

OWASPOTTop10 6.MissingIncidentDetection/ReactionCapabilities
Operational
• Ensure that the generated logs are anlayzed and alerts are triggerd, if an event seems
suspicious.
• The implementation of intrusion detection signatures at network boundaries is impera‑
tivefortheeffectivepreventionofunauthorisedaccess. Inthecontextofindustrialcon‑
trol environments, the configuration of network intrusion prevention should be config‑
uredinawaythatitdoesnotdisrupttheprotocolsandcommunicationsthatareessential
forreal‑timefunctionsrelatedtocontrolorsafety.
• DevSecOpsteamsshouldestablisheffectivemonitoringandalertingsuchthatsuspicious
activitiesaredetectedandrespondedtoquickly.
• Establishoradoptanincidentresponseandrecoveryplan,suchasNationalInstituteof
StandardsandTechnology(NIST)800‑61r2orlater.
6.5. NextActionableSteps
• Performregularincidentdetectionandresponseexerciseswherebothtechnicalandor‑
ganizationalaspectsaretested.
• Exampleoftestingtechnicalaspects: Generateharmlesstest‑malwareandplaceitatan
asset on the system under consideration (SUC). Verify, if the upload on that asset is al‑
ready blocked or at least alarmed. If not, execute the test‑malware and place it some‑
where else in the SUC. If the upload to the asset is already blocked, encrypt or encode
themalware(withseveraliterations,ifneeded)anduploadittotheassetagaintotestif
host‑baseddetectionisalsoworkingbesidesnetwork‑baseddetection.
• Exampleoftestingorganizationalaspects: Performatabletopexercisesimulatinganin‑
cident or emergency. Test especially communication flows, responsibilities of the staff,
coordination of conducting incident response, and the on‑demand acquisition of foren‑
sicknowledge(ifnotin‑house)duringtheexercise.
6.6. References
Standards
Applicablestandardrequirementsarelistedinthe providedmappingtableintheappendix .
Backgroundinformation
• NoteableCWSs: thefollowingCommonWeaknessEnumerationidenifierarehighlyrele‑
vanttothisTop10item:
– CWE‑223: OmissionofSecurity‑relevantInformation . Theproductfailstorecordor
displayinformationthatisessentialforidentifyingthesourceornatureofanattack,
orforassessingwhetheranactionissafe.
2025Edition 59

<!-- page 65 -->

OWASPOTTop10 6.MissingIncidentDetection/ReactionCapabilities
– CWE‑532: InsertionofSensitiveInformationintoLogFile . Theproductlogssensitive
information,e.g.;passwords,hashes,orcredentials.
– CWE‑778: Insufficient Logging. When a security‑critical event occurs, the product
eitherfailstologtheeventoromitskeydetailsinthelog.
• NotableMITREATT&CKframeworkdatasources : ApplicationLogs areeventscollected
bythird‑partyservices,suchasmailservers,webapplicationsorotherappliances,rather
than by the native operating system or platform.Network Trafficis data transmitted
acrossanetwork(e.g.theweb,DNS,email,files,etc.) thatiseithersummarised(e.g.Net‑
Flow)and/orcapturedasraw,analysabledata(e.g.PCAP).
Tooling
• SimulatingAttacks:itishighlyrecommendedtoverifyone’sattackdetectioncapabilities.
Commonapproachesare:
– Eicarmalwaretestfile . TheEICARAnti‑VirusTestFile,alsoknownastheEICARTest
File,isacomputerfiledevelopedbytheEuropeanInstituteforComputerAntivirus
Research(EICAR)andtheComputerAntivirusResearchOrganisation(CARO)totest
howcomputerantivirusprogramsrespond.
– Metasploitframework. TheMetasploitFrameworkisamodular, Ruby‑basedpene‑
tration testing platform that allows you to write, test and execute exploit code. It
containsa suiteof toolsfor testingsecurity vulnerabilities, enumerating networks,
executingattacksandevadingdetection. Atitscore,theframeworkisacollectionof
commonlyusedtoolsthatprovideacompleteenvironmentforpenetrationtesting
andexploitdevelopment.
• Host‑centricLoggingandMonitoringTools allowforthecollectionandanalysisoflogs
fromindividualhosts,suchasservers,workstations,andnetworkdevices:
– GraylogisafreeSIEMtoolenablingcentrallogmanagement.
– WazuhisanopensourceunifiedXDRandSIEMprotectionforendpointsandcloud
workloads.
• Network‑centricLoggingandMonitoringTools areusedtomonitornetworktrafficand
detectanomaliesormaliciousactivities:
– Snortisaopen‑sourceintrusionpreventionsystem(IPS).SnortIPSusesaseriesof
rulestohelpdefinemaliciousnetworkactivity,identifyingpacketsthatmatchthese
rules and generating alerts for users. Snort can also be deployed in line to block
thesepackets. Snorthasthreeprimaryuses: Itcanbeusedasapacketsniffer,like
tcpdump; as a packet logger, which is useful for debugging network traffic; or as
a full‑blown network intrusion prevention system. Snort can be downloaded and
configuredforpersonalandbusinessuse.
2025Edition 60

<!-- page 66 -->

OWASPOTTop10 6.MissingIncidentDetection/ReactionCapabilities
– Suricatais a open‑source network analysis and threat detection software used by
privateandpublicorganisations,aswellasbeingembeddedbyvendorstoprotect
theirassets.
2025Edition 61

<!-- page 67 -->

OWASPOTTop10 7.BrokenZonesandConduitsDesign
7 BrokenZonesandConduitsDesign
Havingasoundsegmentationconceptmitigatesalreadyalotofothersecurityrisks. Thismakes
having proper segmentation and secured interfaces between the segments even more impor‑
tant. Ontheotherhand,acomplexdesignmightintroduceerrorsandloopholesinthedesign.
Therefore,the“correct”designisnotthemostcomplex,ormicrosegmented,buttheonethat
fulfillsalltheneedswithoutbeingoverlycomplex.
7.1. Description
OTassets(likePLCs,SafetyPLCs,HMIs,Historians)shouldbegroupedaccordingtotheirsecu‑
rityrequirementsinzones. Thezonesitselfcanbedefinedviaarisk‑basedapproach(e.g.Threat
and Risk Analysis). The objective is to balance operational feasibility (e.g. limited resources)
with security considerations (e.g., avoiding overexposure of critical assets). Conduits are con‑
trolled communication paths between those zones. Within conduits, communication should
be regulated using standard segmentation and segregation controls, such as firewalls and ac‑
cesscontrollists(ACLs). Segmentationistheprocessofdividinganetworkintosmallerparts,
where the network segments itself should be aligned to the zones defined earlier. Common
designerrorsinclude:
• Missing demilitarized Zone (DMZ) between IT and OT: Direct connections from IT to OT
zonesandviceversaarepossiblewithoutorwithoutproperrestriction.
• Overly broad IP and port ranges in access control lists: ACLs are configured with broad
IPandportranges,permittingentirenetworksegmentstoestablishconnectionsacross
portrangesratherthanenforcingper‑hostrestrictions.
• Multi‑homed‑devices: Multi‑homeddeviceshavenetworkinterfacesinmultiplenetwork
zonesandmayallowlateralmovement,eitherthroughintentionallyenabledroutingca‑
pabilitiesorifthedeviceiscompromised.
• Possiblecommandandcontrolchannels: ProtocolssuchasIMAPandDNSwithintheOT
network introduces the risk of unintended command and control channels, which may
beusedforlateralmovementordataexfiltration.
• Hardwaredebuginterfacesactasbackdoorsintozones: WhendebuginterfaceslikeJTAG
or SWD are forgotten to be deactivated, they can act as an entry point into otherwise
highlysecuredzones. Bygainingaccesstoe.g.adeviceontheshopfloorviaphysicalac‑
cess, thisenablesanattackertopotentiallymovelaterallytoothersystemsinthesame
zoneandcompromiseitcompletely.
• Forgotten remote access: While remote access via different protocols and solutions is
moreorlessanecessityinmostmodernOTenvironments,theytoocanactaseffectiveby‑
passesfordefinedzoneaccesscontrolswhennotconsideredfromthestartandisolated
2025Edition 62

<!-- page 68 -->

OWASPOTTop10 7.BrokenZonesandConduitsDesign
accordingly. By acting as kind of an out‑of‑bound conduit that was not defined before‑
hand,thiscanresultinapotentialpointofentryintoaotherwisehighlyisolatedzone.
7.2. Rationale
ThemostcommonentryintoOT‑zonescomesfromITenvironments. Forhardwaredevicesthe
most common entry is via debugging interfaces. After getting entry into the system, without
segmenting networks and isolating services, an attacker has full access to the network. Un‑
fortunately, in realty networks are very flat. Segmentation or networks and services enables
implementationofcoreprincipleslike“defenseindepth”and“leastprivilege”.
7.3. KnownAttacks/Examples
• CyberRiskIntelligence: Iran‑LinkedAttackonU.S.WaterTreatmentFacility
• Russia‑backedhackinggroupsuspectedofattackonUSwatersystem
• Havinge.g.,yourRDPconnectionsexposedtotheinternetcanhavesevereconsequences
asseenwithEternalBlue( WhatIsEternalBlueandWhyIstheMS17‑010ExploitStillRele‑
vant?).
7.4. Mitigation/Countermeasures
DesignandImplementation
IEC62443‑3‑2suggestsafullmethodologyfortheestablishmentofzonesandconduits. While
detailscanbefoundthere,ashortsummaryshouldbegivenatthispoint:
1. Identification of the System under Consideration (SuC): Identify all systems (hard‑
ware and software), network devices and communications links that should be secured
byzonesandconduits.
2. Performaninitialcybersecurityriskassessment : A high level risk assessment helps
inidentifyingpossiblethreatsandworstcaserisksfortheassetsintheSuC.Thisallows
prioritizationofavailableresourceswheretheyareneededmost.
3. PartitionoftheSUCintozonesandconduits : Assetsaregroupedinsegmentsonbasis
of the results of the initial risk assessment. Further criteria that can influence grouping
arecriticalityofassets,physicaland/orlogicallocation,functionalityorrequiredaccess
(“Least Privilege”). Conduits are then to be defined between zones. They should be as
tightlycontrolledandminimizedaspossible.
4. Checkifinitialriskexceedstolerablerisk : IftheresultsofStep2exceedthetolerable
risk of the organization, an additional detailed risk assessment (Step 5) should be con‑
ducted. Otherwise,Step5canbeomitted.
5. Performadetailedcybersecurityriskassessment : Foreachzoneandconduit,amore
granular threat and risk assessment should be executed. This process should result in
2025Edition 63

<!-- page 69 -->

OWASPOTTop10 7.BrokenZonesandConduitsDesign
appropriate risk reduction measures and aims to identify any gaps in controls already
putinplace.
6. Document cyber security requirements, assumptions and constraints: All technical
requirements for each zone and conduits, all assumptions made during the whole pro‑
cessandallconstraints(legacysystems,technologicalissues,budgetaryissues)mustbe
documentedforfulltransparency.
7. Getassetownerapproval : Ownersofaffectedassetshavetoreviewandapproveresults
oftheprocess.
Operational
• Once zones and conduits are implemented, the have to be steadily monitored and
reassessed for further improvements and adaptions. Especially network and system
changescanrequireadaptionsintheestablishedzoningconcept.
7.5. NextActionableSteps
• Inventorizeyourassets(includingallrequiredinterfaces)
• Monitoryournetworkstogetinsightsinwhatsystemscommunicatewitheachother
• Followthestepsoutlinedabove
• Formoreinformation,consultIEC62443‑3‑2
7.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
Tooling
• BloodhoundforADtreebuilding
• nmapforenvironmentscanning
• Network monitoring tools for traffic analysis (especially useful for determination of
neededconduits)
2025Edition 64

<!-- page 70 -->

OWASPOTTop10 8.MissingAwareness
8 MissingAwareness
It’snotenoughtohavesecuritycapabilities,theyneedtobeused. Ifnooneisawareofpotential
security issues and how the respective security capabilities can help, employees will not use
themandthusfinallyuseless.
8.1. Description
Securityawarenessistheunderstandingandknowledgeofsecurityrisks,threats,andbestprac‑
tices within an organization. It involves educating employees about potential security vulner‑
abilities and how to mitigate them. In many cases, organizations have security capabilities in
place,butemployeesarenotawareofthemordonotknowhowtousethemeffectively.
Thereisaconnectionto DeviceswithMissingCapabilities : weneedbothdeviceswithsecurity
capabilities and the knowledge to use them. If either is missing, the security capabilities are
useless.
Thesamegoesforsecuritypolicies: iftherearepoliciesinplace,buttheyarenotlived,theyare
ultimatelyuseless. Thiscanbeduetoalackofknowledgeorunderstandingofthepolicies,or
itcanbeduetoalackofresourcesortimetoimplementthem. Thebestwaytocounteractthis
istomakeemployeesunderstandwhythesecuritypolicieswerecreatedandhowtheyprotect
theirdailywork.
AddSecurityRequirementstoTenders
Very often security is an afterthought leading to problems such as insecure designs that are
expensivetofix,aswellasmissingresourcesforsecurity. Thisisespeciallyproblematicinthe
OTworldwithitslong‑runninglifetimes: ifsecurityisnotpartofthedesignprocess, fixescan
becomeprohibitivelyexpensiveandapplyingthosefixeswillleadtodowntimes.
A good way to counteract this is to add security requirements to tenders. By including these
requirementsintenders, organizationscanensurethatsecurityisconsideredfromtheoutset
oftheproject. Makingsecuritytestsapartofacceptancetestsalsogivesthe“customer”more
leveragewhennegotiatingsecurityfixeswiththevendor.
OTandITAreOftenNotIntegrated
OT and IT are often not integrated, leading to a lack of communication and understanding
between the two teams. This can result in security gaps and vulnerabilities that are not ad‑
dressed.
2025Edition 65

<!-- page 71 -->

OWASPOTTop10 8.MissingAwareness
ITsecurity people oftenwonderwhy evenbasicsecurity hygiene is notappliedin OTenviron‑
ments. Thiscanbeduetoalackofunderstandingoftheuniquechallengesandrequirements
ofOTsystems. WhileOTpeopleareinpossessionofthegroundtruth,theyoftenwonderwhy
securityisnowbeingpushedintotheirenvironments.
Many OT systems are designed to operate continuously and cannot be easily patched or up‑
datedwithoutcausingdowntime. Thiscanleadtoacultureof“ifitain’tbroke,don’tfixit”that
canleavesystemsvulnerabletoattacks.
SecuritybyObscurityDoesNotWorkintheLongRun
Securitybyobscurityisthepracticeofkeepingsecuritymeasuressecretinordertoprotectthem
fromattackers. Thiscanincludeusingproprietaryprotocols, customhardware, orothertech‑
niquesthatarenotwidelyknownorunderstood. Theideaisthatifattackersdonotknowhow
thesystemworks,theywillnotbeabletoexploitit.
However, this approach is flawed. Attackers can often reverse‑engineer systems or find other
waystodiscovervulnerabilities,evenifthedetailsofthesystemarenotpubliclyavailable. Se‑
curitybyobscuritycancreateafalsesenseofsecurityandleadtocomplacencyinaddressing
vulnerabilities.
This approach is often used in OT environments, where systems are not well documented or
understood. However, this approach is not effective in the long run, as attackers can still find
waystoexploitvulnerabilities.
Securitybyobscuritycanbeusedtomakeanattacker’sjobmoredifficult,butitshouldnotbe
relieduponasthesolemeansofprotection.
SecurityCapabilitiesAreUselessIfNotUsed
InOT,weoftenhavetheinitialproblemoflong‑lived componentswithmissingcapabilities ,but
even if we have the needed capabilities, they are often not used. This can be due to a lack of
knowledgeorunderstandingofthecapabilities.
Educatingemployees(inthesenseof“explainingthereasonsforthemeasurestaken”andnot
“preachingsecurity”)thusisofhighimportancetoensurethatsecuritycapabilitiesareusedef‑
fectively. Thisincludesprovidingtrainingandresourcestohelpemployeesunderstandhowto
usesecuritycapabilities, aswellascreatingacultureofsecurity awarenesswithin theorgani‑
zation.
Examplesofsecurityproblemsintroducedbymissingawarenessinclude:
• everythingconfigurationrelated
• missingencryptionevenifavailable
• availableJTAG/SWDinterfaceleftenabledonproductiondevices
• Intentionalmisconfigurationforeaseofuse,e.g.,leavingrtu’sinuploadmode
2025Edition 66

<!-- page 72 -->

OWASPOTTop10 8.MissingAwareness
TrainingBeyondCompliance
Trainingmustevolvebeyondcompliancecheckboxestopreparepersonnelforreal‑worldsce‑
narioswherecyberincidentscanappearasequipmentfailures. The“greyzone”betweenme‑
chanicalfailureandcyberattackpresentsaparticularchallenge‑operatorsmustquicklydeter‑
minewhetherthey’refacingacomponentfailureoracyberattack.
Third‑PartyBlindSpot
A critical gap exists in extending cybersecurity awareness to contractors, vendors, and third‑
party technicians. These individuals often have privileged access to OT systems but operate
with little‑to‑no cybersecurity awareness. Thissupply chain vulnerabilityis increasingly ex‑
ploitedbythreatactors,asthirdpartiesmayhaveelevatedorunrestrictedaccesswithfarless
securitytrainingcomparedtoin‑housepersonnel.
8.2. Rationale
Thebesthardwarewiththebestsecuritycapabilitiesisuselessifnooneisawareofthemand
howtousethem. Educatingemployeesaboutsecurityrisksandbestpracticescanhelpmitigate
vulnerabilitiesandimproveoverallsecurityposture.
8.3. KnownAttacks/Examples
• The Register: Iranian hacktivists .. likely broke into the facilities by using default pass‑
wordsforinternet‑accessiblePLCs
• ColonialPipelineHack : Theattackersgainedaccesstothesystembymeansofacompro‑
misedpasswordforadisusedVPNaccount.
• TRISIS:TheTriconexSIScontrollerhadthekeyswitchin‘programmode’duringthetime
oftheattackandtheSISwasconnectedtotheoperationsnetworkagainstbestpractices.
InaproperconfigurationandwiththecontrollerplacedinRunmode(programchanges
not permitted) the attackers would face a more difficult challenge implementing the at‑
tack.
8.4. Mitigation/Countermeasures
DesignandImplementation
• capturesecurityrequirementsinthedesignprocess
• explainOT‑specificsecurityrequirementstosoftwaredevelopers(ifdevelopmentispart
oftheimplementation/designprocess)
2025Edition 67

<!-- page 73 -->

OWASPOTTop10 8.MissingAwareness
Operational
• addsecurityrequirementstotenders
• makesecuritytestspartofacceptancetests
• createacultureofsecurityawareness
• provide training and resources to employees to help them understand and use security
capabilitieseffectively
• implementsecuritypoliciesandproceduresthatareeasytounderstandandfollow
• integratecybersecurityintoexistingsafetyprograms(HSSE)
• conductlivesimulationexercisesthattestresponsetoambiguousincidents
• extendtrainingrequirementstothird‑partycontractorsandvendorsbeforegrantingac‑
cess
• developrole‑basedtrainingtailoredtospecificoperationalroles
8.5. NextActionableSteps
• addsecurityrequirementstotenders
• createacultureofsecurityawareness: helpemployeesunderstandwhythesecuritycon‑
trolstakenareimportantfortheirwork
• provide training and resources to employees to help them understand and use security
capabilitieseffectively
• integratecybersecurityawarenessintoexistingsafetytrainingprograms
• implementlivesimulationexercisesforambiguousincidentresponse
8.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
Backgroundinformation
• TRISIS:AnalyzingSafetySystemTargetingMalware(usingarchive.org)
2025Edition 68

<!-- page 74 -->

OWASPOTTop109.SelectionofComponents/ProtocolsWithInsufficientSecurityCapabilities
9
SelectionofComponents/ProtocolsWithInsufficient
SecurityCapabilities
Giventhe long, potentiallymulti‑decades, lifetimesof OTsystem, itbecomesunderstandable
why OT components become legacy systems over time. Many of the mentioned countermea‑
surestrytodealwiththeexistenceoflegacysystems.
Whendesigningnewsystems,however,thebestwaytodealwithlegacysystemsistonotuse
theminthefirstplace. Ifwedesignnewsystemsthereshouldbeslackforfuturesecurityfea‑
tures.
This Top 10 items is related tomissing awareness. While missing awareness is about the lack
ofknowledgeaboutsecurityfeatures,thisitemisaboutthelackofsecurityfeaturesinthefirst
place.
9.1. Description
We define legacy systems as systems with security and cryptography capabilities that do not
conform to current best practices. This includes systems that are not able to be updated or
patched,aswellassystemsthatarenotabletobereplaced.
Don’tUseLegacySystemsforNewDeployments
Obviously,ifyouaredesigninganewsystem,youshouldnotuselegacysystems. Thisisespe‑
cially true for systems that are not able to be updated or patched. If you are designing a new
system,youshouldusesystemsthatareabletobeupdatedorpatched.
Deployments are seldom new green‑field installations. Most of the time, new systems are de‑
ployedinexistingenvironments(thinkaboutthelonglifetimesofOTsystems). Ifnewcompo‑
nentsareaddedtoanexistingenvironment,theyoftenhavetoconformandinteractwiththe
existingenvironment,oftenmandatingusageoflegacyprotocols. Ifthisisthecase,itwouldbe
preferabletousecomponentsthat(whiletheyprovidethelegacyfeatureset)alsoincorporate
capabilitiesforstate‑of‑the‑artsecurityfeaturessothattheinstallationcanbeupdatedinthe
future.
Don’tUseLegacyProtocolsifPossible
Components commonly use standardized protocols to communicate with each other or with
othersystems. Whendesigninganewsystem,chosenprotocolsshouldheedbestsecurityprac‑
ticesandlegacyprotocolsshouldbeavoidediffeasible.
Legacyprotocolsoftenhavesecurityissues:
2025Edition 69

<!-- page 75 -->

OWASPOTTop109.SelectionofComponents/ProtocolsWithInsufficientSecurityCapabilities
• Theyoftenlackintegrityprotectionandthus canleadtoavailabilityproblems .
• Theydonotofferthoroughor sufficientauthenticationmechanisms andthuscanleadto
unauthorizedaccesstosystemsanddata.
• Theyhaveweakbuilt‑insecurityfeatureslikebasicBluetooth.
9.2. Rationale
• giventhelonglifetimesofOTsystems,partsofthembecominglegacysystemswillhap‑
pen
• thereiseconomicpressuretouseexistinglegacysystemsfornewdeployments:w
• thereisalackofawarenessaboutthesecurityimplicationsofusinglegacysystems
9.3. KnownAttacks/Examples
• Industroyer (also known as CrashOverride) caused the 2016 power outage in Kyiv by
speaking the legitimate IEC 60870‑5‑104, IEC 61850, and OPC DA protocols directly to
substation equipment. No vulnerability was needed: IEC 60870‑5‑104 and IEC 61850
(without the IEC 62351 profiles) provide neither authentication nor integrity protec‑
tion, so they execute every syntactically valid command from a host that can reach
them; OPC DA relies on DCOM authentication, which Industroyer satisfied from an
already‑compromisedhost.
• INCONTROLLER(alsoknownasPIPEDREAM)isanattacktoolkitdiscoveredin2022that
abuses legitimate functions of Modbus, CODESYS, and OPC UA to discover, manipulate,
anddisableSchneiderElectricandOMRONSysmacPLCsandOPCUAservers. Itwasde‑
velopedasanoffensivecapabilityand,asof CISAAA22‑103A,hadnotbeenobservedde‑
ployedinattacks.
9.4. Mitigation/Countermeasures
DesignandImplementation
• don’tuselegacysystemsorprotocolsfornewdeployments
• usecomponentsthatareabletobeupdatedorpatched
• incorporatesomeslackforfuturesecurityfeaturesinnewdesigns
Operational
Sadly, there are no operational countermeasures that can be applied to legacy systems. The
best way to deal with legacy systems is to not use them in the first place. If you have to use
legacysystems,youcantrytomitigatetherisksbyapplyingthefollowingcountermeasures:
• isolatelegacysystemsfromtherestofthenetwork
2025Edition 70

<!-- page 76 -->

OWASPOTTop109.SelectionofComponents/ProtocolsWithInsufficientSecurityCapabilities
• monitorlegacysystemsforunusualactivity
• applycompensatingcontrolstomitigatetherisksoflegacysystems
• applycompensatingcontrolstomitigatetherisksoflegacyprotocols
9.5. NextActionableSteps
• evaluatethecomponentsandprotocolsusedinyoursystems
• identifylegacysystemsandprotocolsinyourenvironment
• evaluatethesecuritycapabilitiesofthesesystemsandprotocols
• if possible, replace legacy systems and protocols with state‑of‑the‑art components and
protocols
• ifreplacementisnotpossible,applycompensatingcontrolstomitigatetherisksoflegacy
systemsandprotocols
9.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
2025Edition 71

<!-- page 77 -->

OWASPOTTop10 10.MissingHardening
10 MissingHardening
Hardening is usually done to make a system more secure, typically by reducing or restricting
features which inherently reduces a system’s attack surface. Another form of hardening is en‑
ablingadditionallayersofsecuritysothatanattackerhastoovercomemultiplehurdlestogain
accesstoasystem.
10.1. Description
Hardeningistheprocessofsecuringasystembyreducingitssurfaceofvulnerability. Thiscan
be achieved by removing unnecessary services, closing unused ports, and applying security
patches. Hardening is an essential step in securing any system, as it reduces the number of
potentialentrypointsforattackers.
Another way of hardening is to apply additional layers of security, such as firewalls, intrusion
detection systems, and encryption. These additional layers can help protect against attacks
even if the underlying system is compromised. In the context of OT, hardening is particularly
importantduetotheuniquechallengesandrequirementsofthesesystems. OTsystemsareof‑
tendesignedtooperatecontinuouslyandcannotbeeasilypatchedorupdatedwithoutcausing
downtime.
ApplyEstablishedHardeningGuidelines
Hardeningguidelinesareestablishedbestpracticesforsecuringsystemsandnetworks. These
guidelinesprovideaframeworkforidentifyingandmitigatingvulnerabilities,andtheycanhelp
organizationsimplementeffectivesecuritymeasures.
Some well‑known hardening guidelines include the Center for Internet Security (CIS) bench‑
marks or the Defense Information Systems Agency (DISA) Security Technical Implementation
Guides(STIGs).
DisableDefaultAccountsandPasswords
DefaultaccountsandpasswordsareoftenusedinOTsystems,andtheycanposeasignificant
securityriskifnotproperlymanaged. Attackerscaneasilyexploitthesedefaultcredentialsto
gainunauthorizedaccesstosystemsandnetworks. Itisessentialtodisableorchangedefault
accounts and passwords during the hardening process to reduce the risk of unauthorized ac‑
cess.
2025Edition 72

<!-- page 78 -->

OWASPOTTop10 10.MissingHardening
10.2. Rationale
InclusionofhardeningintheOWASPOTTop10wasapointofseriousdiscussion.
Hardeningitselfdoesnotreduceaconcretevulnerabilitybutmakesmeaningfulexploitationof
vulnerabilitiesharderforattackers.
Empiricaldata,gatheredduringthedevelopmentoftheOWASPOTTop10,showedthatmissing
hardeningwasacommonpartofsuccessfulexploitsandcomprehensivehardeningwouldhave
preventedsuccessfulexploitation.
Giventherequirementofnon‑stopoperationofmanyOTsystems,hardeningiscrucialasital‑
lowsforcontrolledupdatesafterasecurityissuehasbeenidentified(astheadditionalsecurity
layersupholdthesecurityoftheoverallsystem).
10.3. KnownAttacks/Examples
• Stuxnet: DisablingUSBportscouldhaveavoidedinitialcompromise.
• NotPetya: Propernetworksegmentationandhardeningcouldhavelimitedthespreadof
themalware.
10.4. Mitigation/Countermeasures
Mitigationandcountermeasurescanbeappliedalongthesupplychain. Startingfromtheven‑
dorovertheintegratortotheassetowner.
DesignandImplementation
Toensurerobustsoftwaresecurityacrossthedevelopmentlifecycle,componentsuppliers,and
integrators—mustadoptproactivecountermeasures:
• Disable unnecessary services and interfaces (e.g. USB ports, insecure protocols like Tel‑
net,webserver,JTAG/SWDinterfaces)
• Startwithestablishedhardeningbenchmarksandgraduallyrelaxcontrolsonlyasneces‑
sarytoensureyourcomponentorsystemfunctionsproperly
• IncludeApplicationallow‑listingifpossible
• Provideyourcomponentorsystemwithasecuredefaultconfiguration
• Provideahardeningguidelineforyourcomponentorsystemtocustomers
Operational
Operatorsplayacriticalroleinmaintainingthesecurityandresilienceofdeployedsystems. To
reduceriskandensureoperationalintegrity,thefollowingcountermeasuresareessential:
2025Edition 73

<!-- page 79 -->

OWASPOTTop10 10.MissingHardening
• Makesurehardeningisreappliedaftermaintenance
• Requestdocumentationofhardeningmeasures
• Includehardeningrequirementsinthetender,ideallywiththeintegratorprovidingtheir
ownhardeningconcept
• MakesurehardeningisactuallyimplementedwithaPentestorsomekindofCybersecu‑
rityAcceptanceTest(duringSAT/FAT)
10.5. NextActionableSteps
Tobeabletoimplementsensiblemeasuresonecouldfollowthesesteps:
• identifyapplicablehardeningguidelinesforyourenvironment: Everyenvironmentisdif‑
ferentandthereforehasdifferentneedsandpriotitizesdifferenttopics. Findingtheright
measuresforthesystemunderconsiderationisthefirstandmostcrucialstepwhentrying
toimprovethesecuritypostureofasystem.
• implement hardening guidelines: After identifying the shortcomings, hardening guide‑
linesfortheinsecuresystemscanhelptoprovideagoodbaselinetoimprovefrom.
• disabledefaultaccountsandpasswords: Defaultcredentialsarecommonlyusedandmis‑
used way of getting access to permissions that should normally be behind proper safe‑
guards.
10.6. References
Standards
• Applicable standard requirements are listed in theprovided mapping table in the
appendix.
• OT‑specifichardeningguidesareoftenprovidedbythesystemintegratororproductsup‑
plier,forexample:
– “SystemHardeningforSubstationAutomationandProtection” forSICAM/SIPROTEC,
which includes hardening measures at the solution level as well as for individual
components.
• Severalorganizationsprovideconfigurationbaselinesandbenchmarksforcommonsys‑
tems:
– The Center for Internet Security (CIS)offers Benchmarks for various systems,
including operating systems, network devices, and commonly used applications.
In OT environments, relevant benchmarks cover operating systems, network
infrastructure,andsupportingapplications.
– The Defense Information Systems Agency (DISA)publishes Security Technical
Implementation Guides (STIGs), which define configuration standards for secur‑
ing Department of Defense (DoD) IT systems and are also widely adopted in other
2025Edition 74

<!-- page 80 -->

OWASPOTTop10 10.MissingHardening
sectors.
– MicrosoftSecurityBaselines recommendsecuritysettingsforWindowsoperating
systemsandMicrosoftapplications.
Backgroundinformation
• BSIIT‑SecurityinderIndustrie(german)
• https://en.wikipedia.org/wiki/Hardening_(computing)
• https://en.wikipedia.org/wiki/Defense_in_depth_(computing)
Tooling
• TenableNessus/OpenVAS,withcomplianceScanning
• MicrosoftSecurityComplianceToolkit
2025Edition 75

<!-- page 81 -->

PartIV
WheretoStart

<!-- page 82 -->

OWASPOTTop10 What’snextandWheretoStart?
What’snextandWheretoStart?
Sobasically, you’vereadthroughtheTop10 listandarenowwonderinghowtobestproceed
fromhere. Thisisacommonquestion,andwewanttohelpyougetstarted.
There’san actionable next steps sectionwithineachTop10item. Thisshouldgiveyou
agoodideawhataresuitablenextstepsforyou. Thiscanbeabitoverwhelming,sowewantto
giveyouabitofadditionalhigh‑levelguidance.
ForexistingSystems
So you already have a system in place and are now wondering how to improve it. After going
throughtheTop10list,youeitherfeelabitinsecureaboutyourcurrentsituationoryouhave
identifiedsomeareasthatneedimprovement. Thisisagoodthing,asitmeansyouareaware
oftheissuesandcannowstartworkingonthem.
Ontheotherhand,youmightfeeloverwhelmedbytheamountofworkthatneedstobedone.
Thisisalsoacommonfeeling.
Usingacontinouslyimprovementapproachcanhelpyoutonotgetoverwhelmedandtomake
steadyprogress(whilebeingalignedtocommonISO/IECstandards). Herearesomestepsyou
cantake:
1. Don’tpanic. Wewouldlovetohavegreen‑fieldsystemsbutwehavetoworkandimprove
withwhatwe’recurrentlyworkingwith.
2. Assessyoursituation. Youcanusethelistof actionable next steps fromtheTop
10itemsforthis.
3. Selectlow‑hangingfruitsandimprovethem,maybecombineupdatesintoyourexisting
maintenancecycle
4. Gobacktostep2
FornewSystems/Components
Ifyouareintheprocessofdesigninganewsystemorcomponent, youhavetheadvantageof
being able to start with security in mind from the very beginning. This is often referred to as
“securitybydesign”.
Ifyouarecurrentlyinprogressofbuyinganewsystemorcomponent:
• addsecurityrequirementstoyourtendersandincorporatesomeslackforfutureupdates
• donotselectprotocols/componentswithknownsecurityissues. Ifinsecureprotocolsare
currentlymandatory(duetoexistingcomponentsthatthenewcomponentmustinteract
with),selectcomponentsthatadditionallyoffersecureprotocolssothatyouwillhavean
upgradepathinthefuture
2025Edition 77

<!-- page 83 -->

OWASPOTTop10 What’snextandWheretoStart?
PrepareforIncidents
Incidentswillhappen,nomatterhowwellyouprepare. Thebestyoucandoistobeprepared
forthem. Thisincludes:
• Createincidentresponseplansandperformreadinesstraining. Youwillbestressedout
duringanincidentandwanttohavegoodplansandroutinestofallbackto.
• Fosterasecurityculturewithinyourorganization. Thisisalong‑termprocess,butitwill
pay off in the end. Make sure that everyone is aware why security is important for their
respectivetasksinsteadofmandatingsecuritytop‑down.
• talkwithyourvendors/suppliersabouttheirsecuritypracticesandhowtheyhandleinci‑
dents. Thiswillhelpyoutounderstandtheircapabilitiesandhowtheycansupportyou
incaseofanincident.
AdditionalReading
• NISFactsheet
• NISTCSF2.0
2025Edition 78

<!-- page 84 -->

PartV
AbouttheProject

<!-- page 85 -->

OWASPOTTop10 AboutOWASP
AboutOWASP
TheOpenWorldwideApplicationSecurityProject (OWASP)isanopencommunitydedicatedto
enabling organizations to develop, purchase, and maintain applications and APIs that can be
trusted.
AtOWASP,you’llfindfreeandopen:
• Applicationsecuritytoolsandstandards
• Cuttingedgeresearch
• Standardsecuritycontrolsandlibraries
• Complete books on application security testing, secure code development, and secure
codereview
• Presentationsand videos
• Cheatsheetsonmanycommontopics
• Chaptersmeetings
• Events,training,andconferences
AllOWASPtools,documents,videos,presentations,andchaptersarefreeandopentoanyone
interestedinimprovingapplicationsecurity.
Weadvocateapproachingapplicationsecurityasapeople, process, andtechnologyproblem,
becausethemosteffectiveapproachestoapplicationsecurityrequireimprovementsinthese
areas.
OWASP is a new kind of organization. Our freedom from commercial pressures allows us to
provideunbiased,practical,andcost‑effectiveinformationaboutapplicationsecurity.
OWASPisnotaffiliatedwithanytechnologycompany,althoughwesupporttheinformeduseof
commercialsecuritytechnology. OWASPproducesmanytypesofmaterialsinacollaborative,
transparent,andopenway.
The OWASP Foundation is the non‑profit entity that ensures the project’s long‑term success.
Almost everyone associated with OWASP is a volunteer, including the OWASP board, chapter
leaders, project leaders, and project members. We support innovative security research with
grantsandinfrastructure.
2025Edition 80

<!-- page 86 -->

OWASPOTTop10 CommunityandContributing
CommunityandContributing
Pleasedon’thesitatetocontacttheOWASPOTTop10projectwithyourquestions,comments,
andideas,eitherpubliclybyaddingissuesorprovidingcommitson ourgithubpage .
Please join theOWASP OT Top 10 Slack Channelto chat. You can get a free invitation to the
OWASPslackserverthrough thiswebsite.
We do a video conference every first Monday of the month from 4pm to 5pm CET/CEST using
https://meet.google.com/gwi‑vhxz‑rjr . Wealsoprovidea publicICScalendarseries thatyou
canaddtoyourcalendar.
HowtoContribute?
All development is public and happens on github. If you want to contribute, please fork the
repository, make your changes, and then submit a pull request. We will review your changes
andprovidefeedbackasneeded.
If you plan a larger change, it is always a good idea to talk with us during one of the Monthly
meetingsfirst. Thiswaywecandiscussyourideasandprovidefeedbackbeforeyoustartwork‑
ingonthechanges. Thiscansaveyoualotoftimeandeffort,anditcanalsohelpustoensure
thatyourchangesarealignedwiththegoalsoftheproject.
YoufindthesourcecodeofthecurrentversionoftheOWASPOTTop10inthe docs/directory
within the git repository. When you checkour open issues on github, you can see that some
issuesaretaggedwith help wanted or good first issue . Choosetheseifyouwantto
helpouttheproject!
EmpiricalDataContribution
TheOWASPOTTop10arecreatedbybothdiscussionswithexpertsaswellasthroughanalysisof
empiricaldata(e.g.,incidentreports,vulnerabilitydatabases,etc.). Wearelookingforempirical
data that can help us to identify the most relevant risks and vulnerabilities in the OT domain.
This includes data from incident reports, vulnerability databases, and other sources that can
provideinsightsintothesecuritylandscapeofOTsystems.
If you have empirical data that you would like to contribute, please contact us through email
(Andreas Happe). If you are able to contribute data, please make sure that it is appropriately
anonymized.
HowtoTestYourChangesLocallyBeforeSubmitting
Ifyoucanrunpython,youcanlocallyruntheOWASPOTTop10websitelocally. Werecommend
thistotestyourchangesbeforepushingthemtogithub.
2025Edition 81

<!-- page 87 -->

OWASPOTTop10 CommunityandContributing
Todothis,wewilluse venv tocreatealocalpythonenvironmenttoinstalltheneeded mkdocs
package.
# creates and activates a new python environment in a new `venv`
directory↪
$ python3 -m venv venv
$ source venv/bin/activate
# install the mkdocs package
$ pip install mkdocs-material
# switch into your checked-out OWASP OT Top 10 directory
$ cd owasp-ot-top10
# run the local webserver
$ mkdocs serve
# now you can point your browser to http://localhost:8000 and check
# how your changes will look like
2025Edition 82

<!-- page 88 -->

OWASPOTTop10 ListofOurContributors
ListofOurContributors
TheOTTop10wouldn’tbepossiblewithoutourawesomecontributorsandreviewers. Weuse
theGitHubcontributorsfeature toautomaticallytrackcontributionstotherepository. Hereis
alistofourmaincontributors:
Contributor Company Connectthrough
AndreasHappe LinkedIn
SiegfriedHollerer FederalMinistryofthe
Interior,Austria
LinkedIn
SimonRommer OMICRONelectronics LinkedIn
FelixEberstaller LimesSecurity
NinoFürthauer LimesSecurity
SixtusLeonhardsberger LimesSecurity
mfd2007
MarleinevanKampen
MariiaD.
2025Edition 83

<!-- page 89 -->

OWASPOTTop10 RelatedOWASPProjects
RelatedOWASPProjects
OWASP is a volunteer‑driven organization. Those volunteers contributed many useful docu‑
ments,andthissectionpointstosomerelatedOWASPdocumentsandprojects:
OWASPIoTTop10
TheincreasingintroductionofIoTdevicesinOTenvironments(IndustrialIoT,IIoT)comeswith
many of the security problems that are known from common IoT. This makes OWASP IoT Top
10avaluableresourceespeciallyforsuppliersandintegrators,butforoperatorsaswell.
InOTweoftenanalyzewholefactoryfloorsorpowerplants,situatingourlistofTop10vulnera‑
bilitiesonahigherconceptionallevel. Inaddition,OTisburdenedwithlonglifetimesandprob‑
lematic update cycles placing a greater importance on defense‑in‑depth measures like good
networksegregation.
(I)IoTisapartofOT,butOTisbroaderinscopeandutilizedIoTdeviceswithin. Thisdifference
inscopeisreflectedintheTopVulnerabilitylist: whenusingtheIoTTop10,only2outofthe10
topvulnerabilitiesdirectlymapontotheOTdomain(I4andI5).
OWASPhostsmultipleprojectsthataimto increasethesecurityofIOTprojects .
OWASPTop10
The best known OWASP standard, the Top 10 of web application security, is also relevant for
OT.Suppliersandintegratorsdevelopingsoftwareinformofwebapplications,e.g.forcontrol
systems with a web interface can find useful information on how to avoid the most common
vulnerabilitiesinwebapplications–evenwhentheyareusedinanindustrialenvironment.
Incontrast,thisdocumentisfocusedondefensivetechniquesandcontrolsasopposedtorisks.
Eachcontrolinthisdocumentwillmaptooneormoreitemsintherisk‑basedOWASPTop10.
Thismappinginformationisincludedattheendofeachcontroldescription.
2025Edition 84

<!-- page 90 -->

PartVI
Appendix

<!-- page 91 -->

OWASPOTTop10 Mappingtable
Mappingtable
The following tables map each OWASP OT top 10 item to relevant standard and legislative re‑
quirements.
1. UnknownAssetsandUnmanagedExternalAccess
Standard/Law Requirement‑IDs
IEC62443 FR2
IEC62443‑2‑1:2019 CM1,NET3.X
IEC62443‑3‑2:2020 ZCR1,ZCR3.6
IEC62443‑3‑3:2020 SR2.X,SR7.8
NISTSP800‑82:v3 CM‑8,AC‑20,AC‑17,CM‑2
NISTCSF2.0 ID.AM,PR.AA,PR.IR‑01
MITREATT&CK M0800,M0801,M0804,M0807,M0813,M0918,
M0922,M0926,M0932
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.7,11.X,12.1,12.2,12.4
2. DeviceswithknownVulnerabilities/Issues
Standard/Law Requirement‑IDs
IEC62443 FR3,FR4
IEC62443‑3‑2:2020 ZCR5.2
IEC62443‑3‑3:2020 SR3.X,SR4.X
NISTSP800‑82:v3 SI‑2,RA‑5,CM‑6
NISTCSF2.0 ID.RA‑01,ID.IM,PR.PS,DE.CM‑09
MITREATT&CK M0916,M0934,M0942,M0945,M0948
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.5,6.6,6.10
3. InadequateSupplier/SupplyChainManagement
2025Edition 86

<!-- page 92 -->

OWASPOTTop10 Mappingtable
Standard/Law Requirement‑IDs
IEC62443‑2‑1:2019 ORG1.6
IEC62443‑3‑2:2020 ZCR5.X
NISTSP800‑82:v3 SR‑2,SR‑3,SR‑5,SR‑6
NISTCSF2.0 GV.OC‑03,GV.OC‑04,GV.OC‑05,GV.SC,
ID.RA‑10
MITREATT&CK M0817
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
5.X,6.1,6.2
4. LossofAvailability
Standard/Law Requirement‑IDs
IEC62443 FR7
IEC62443‑2‑1:2019 DATA1.3,DATA1.4,SPE8
IEC62443‑3‑3:2020 SR7.X
NISTSP800‑82:v3 CP‑2,CP‑7,CP‑9,CP‑10
NISTCSF2.0 GV.OC‑04,GV.OC‑05,GV.SC‑07,GV.SC‑08,
PR.AA‑02,PR.IR‑02,PR.IR‑03,PR.IR‑04,DE.CM,
RC.RP‑01,RC.RP‑02,RC.RP‑04
MITREATT&CK M0803,M0811,M0812,M0815,M0953
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
4.X,6.4,13.1,13.2
5. InsufficientAccessControl
Standard/Law Requirement‑IDs
IEC62443 FR1,FR2
IEC62443‑2‑1:2019 SPE2
IEC62443‑3‑3:2020 SR1.X,SR2.X
NISTSP800‑82:v3 AC‑2,AC‑3,AC‑6,AC‑5
NISTCSF2.0 ID.IM‑01,ID.IM‑03,PR.AA,PR.PS‑05,PR.IR‑01
2025Edition 87

<!-- page 93 -->

OWASPOTTop10 Mappingtable
Standard/Law Requirement‑IDs
MITREATT&CK M0800,M0801,M0804,M0807,M0813,M0918,
M0922,M0926
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.7,11.X,13.3
6. MissingIncidentDetection/ReactionCapabilities
Standard/Law Requirement‑IDs
IEC62443 FR6
IEC62443‑2‑1:2019 ORG2.2,SPE7
IEC62443‑3‑2:2020 ZCR5.1,SR6.X
NISTSP800‑82:v3 IR‑4,SI‑4,AU‑6,IR‑6
NISTCSF2.0 GV.SC‑08,ID.IM‑04,DE.CM,DE.AE,RS.X
MITREATT&CK M0919,M0931
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
3.X
7. BrokenZonesandConduitsDesign
Standard/Law Requirement‑IDs
ISO27001Annex A.8.22
IEC62443 FR5
IEC62443‑2‑1:2019 SPE3
IEC62443‑3‑2:2020 ZCR3.X,SR5.X
NISTSP800‑82:v3 SC‑7,AC‑4,SC‑2
NISTCSF2.0 ID.IM,PR.IR‑01
MITREATT&CK M0930,M0935,M0937
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.7,6.8
8. MissingAwareness
2025Edition 88

<!-- page 94 -->

OWASPOTTop10 Mappingtable
Standard/Law Requirement‑IDs
IEC62443‑2‑1:2019 ORG1.4
IEC62443‑3‑3:2020 SR7.6,SR7.7
NISTSP800‑82:v3 AT‑2,AT‑3
NISTCSF2.0 PR.AT
MITREATT&CK M0917
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
8.1,8.2,12.5
9. InsufficientSecurityCapabilities
Standard/Law Requirement‑IDs
IEC62443‑2‑4:2024 SP.03.03
IEC62443‑3‑2:2020 ZCR5.X
IEC62443‑4‑2:2020 CCSC2
NISTSP800‑82:v3 PM‑1,CA‑2,CA‑7
NISTCSF2.0 ID.RA‑01,ID.IM,PR.AA‑02,PR.PS‑01,PR.PS‑02,
PR.PS‑03,PR.PS‑06
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.3,6.5,6.10,12.2
10. MissingHardening
Standard/Law Requirement‑IDs
IEC62443‑2‑1:2019 ORG1.5
IEC62443‑2‑1:2024 COMP1.1
IEC62443‑2‑4:2024 SP.02.03
IEC62443‑3‑3:2024 X
IEC62443‑4‑1:2018 SG‑3
IEC62443‑4‑2 X
NISTSP800‑82:v3 CM‑6,CM‑7,SI‑3,SC‑28
NISTCSF2.0 PR.PS
2025Edition 89

<!-- page 95 -->

OWASPOTTop10 Mappingtable
Standard/Law Requirement‑IDs
MITREATT&CK M0806,M0818,M0921,M0924,M0927,M0928,
M0934,M0936,M0938,M0942,M0944,M0949,
M0950,M0951,M0954
EUNIS2DirectiveCommissionimplementing
RegulationC(2024)7151‑ANNEX
6.3,6.9,9,12.3
2025Edition 90

<!-- page 96 -->

OWASPOTTop10 Glossary
Glossary
Asset Anassetrefers to any physical or digital component that plays a role in the operation,
control,ormonitoringofindustrialprocesses. Theseassetsarecriticaltothefunctioning
ofsystemsinsectorslikemanufacturing,energy,transportation,andutilities.
Awareness (Security)Awarenessreferstotheknowledgeandunderstandingthatindividuals
withinanorganizationhaveaboutpotentialsecuritythreatsandthebehaviorsrequired
to prevent or respond to them. It’s a critical component of an organization’s overall cy‑
bersecuritystrategy.
BSI TheBundesamtfür Sicherheitinder Informationstechnik,orFederalOfficeforInformation
Security—isGermany’scentralauthorityforcybersecurityandinformationsecurity.
CIS TheCenterfor InternetSecurityanditsCISControls—asetofbestpracticestosecuresys‑
tems,includingindustrialenvironmentslikeSCADAandICS.
CNC Computer Numerical Control machines are automated tools used in manufacturing for
taskslikedrilling,milling,andcutting.
Contributors Acontributorissomeonewhoaddsvaluetoaproject,organization,oreffortby
providingwork,ideas,resources,orsupport. Thiscanincludewriting,coding,designing,
funding,orofferingexpertise.
CVE ACommonVulnerabilitiesand Exposuresisapubliclydisclosedcybersecurityvulnerabil‑
itywithauniqueidentifier.
cyberattacks Acyber attackis a deliberate attempt by an adversary to damage, disrupt, or
gainunauthorizedaccesstocomputersystems,networks,ordata.
cyberphysicalsystem A Cyber‑Physical System is a system that integrates computing, net‑
working,andphysicalprocesses.
DCS ADistributedControlSystem is an automated control system used in industrial environ‑
mentstomanageprocesses.
DISA TheDefenseInformationSystemsAgencyisaU.S.DepartmentofDefense(DoD)agency
thatprovidessecure,reliableITandcommunicationssupporttomilitaryoperations.
FAT AFactoryAcceptanceTestisaqualityassuranceprocessconductedatthemanufacturer’s
sitetoverifythatequipmentorsystemsmeettherequiredspecificationsbeforedelivery.
Hardening (System)hardeningistheprocessofsecuringasystembyreducingitsattacksur‑
face.
HMI A Human‑Machine Interface is a user interface that allows humans to interact with ma‑
chines,systems,ordevices.
HVAC HVAC stands forHeating,Ventilation, andAirConditioning—a system used to regulate
indoorclimateandairquality.
IDS AnIntrusionDetectionSystemisacybersecuritytoolthatmonitorsnetworkorsystemac‑
tivityforsignsofmaliciousbehaviororpolicyviolations.
IEC IEC stands for theInternationalElectrotechnicalCommission, a global organization that
develops and publishes international standards for electrical, electronic, and related
technologies.
2025Edition 91

<!-- page 97 -->

OWASPOTTop10 Glossary
IEC62443 IEC 62443 is a series of international standards focused on cybersecurity for indus‑
trialautomationandcontrolsystems(IACS).
ISO27001 ISO/IEC27001isaninternationalstandardformanaginginformationsecurity(man‑
agementsystems).
IT InformationTechnologyreferstotheuseofcomputers,networks,andsoftwaretomanage
andprocessinformation.
NERC‑CIP NorthAmericanElectricReliabilityCorporation– CriticalInfrastructureProtection
is a set of mandatory cybersecurity standards designed to protect the Bulk Electric Sys‑
tem(BES)inNorthAmerica.
NIDS ANetworkIntrusionDetectionSystemisasecuritytoolthatmonitorsnetworktrafficfor
suspiciousactivityorknownthreats.
NIS NIS standsforNetwork andInformationSystemsDirective, a European Union regulation
aimedatimprovingcybersecurityacrosscriticalinfrastructuresectors.
NIST TheNationalInstituteof Standardsand Technology,aU.S.federalagencythatdevelops
standards,guidelines,andbestpracticesforscience,technology,andcybersecurity.
OT OperationalTechnologyreferstohardwareandsoftwaresystemsthatmonitorandcontrol
physicaldevices,processes,andinfrastructure.
OWASP OWASPstandsforthe OpenWorldwideApplicationSecurityProject,anonprofitorga‑
nizationfocusedonimprovingsoftwaresecurity.
SAT A SiteAcceptanceTest is a process used to verify that a system or equipment functions
correctlyinitsactualoperatingenvironment.
SCADA SupervisoryControland DataAcquisition,asystemusedtomonitorandcontrolindus‑
trialprocessesremotely.
Segmentation Network segmentation is the practice of dividing a computer network into
smaller, isolated segments or subnets. This improves security, performance, and
manageabilitybycontrollingtrafficflowandlimitingaccessbetweensegments.
SIS Safety Instrumented Systems are automated systems designed to prevent hazardous
events in industrial processes by taking a process to a safe state when predetermined
conditionsareviolated.
STIG ASecurityTechnicalImplementationGuide is a set of cybersecurity configuration stan‑
dardsdevelopedbytheDefenseInformationSystemsAgency(DISA).STIGsareusedpri‑
marilybytheU.S.DepartmentofDefense(DoD)andaffiliatedorganizationstosecureIT
systems,software,andnetworksagainstcyberthreats.
Supplychain Asupplychain isthenetworkofpeople,organizations,resources,activities,and
technologies involved in the creation and delivery of a product or service from the sup‑
pliertothecustomer.
Vulnerabilities A vulnerabilityis a weakness or flaw in a system, software, or network that
canbeexploitedbyathreatactortogainunauthorizedaccess,causedamage,ordisrupt
operations.
2025Edition 92

<!-- page 98 -->

The OWASP Operational Technology Top 10
ot.owasp.org
Licensed under Creative Commons Attribution‑ShareAlike 4.0 Interna‑
tional. OWASP® is a registered trademark of the OWASP Foundation, Inc.

