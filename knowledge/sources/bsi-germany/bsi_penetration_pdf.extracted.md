<!-- Extracted from bsi_penetration_pdf.pdf by extract_pdf.py (pypdf) on 2026-11-10. Working copy: check against the PDF before quoting. -->

<!-- page 1 -->

Study 
A Penetration Testing Model 
Exploits 
Hackers 
Viruses 
Security

<!-- page 2 -->

Study: A Penetration Testing Model 
Contents 
1	 Introduction and Objectives of this Study ........................................................................ 4
1.1 Introduction to Penetration Testing......................................................................... 4
1.2 Methodology and Structure of this Study................................................................ 5
2	 IT Security and Penetration Testing ................................................................................. 6
2.1 Threats..................................................................................................................... 6
2.2 IT Security Measures............................................................................................... 8
2.3 Devising Penetration Tests...................................................................................... 8
2.4 Penetration Testing Procedures ............................................................................... 9
3	 Classification and Objectives of Penetration Testing ..................................................... 10
3.1 Starting Points and Access Channels for Penetration Tests .................................. 10
3.2 Objectives of Penetration Testing ......................................................................... 11
3.3 Limits of Penetration Testing................................................................................ 13
3.4 Classification......................................................................................................... 13
3.5 Multistage Approach ............................................................................................. 17
4	 Legal Issues..................................................................................................................... 18
4.1 Legal Reasons for Penetration Testing.................................................................. 18
4.2 Legal Framework for Penetration Testing............................................................. 27
4.3 Important Terms in Contracts Between Penetration Tester and Client................. 30
5	 General Requirements..................................................................................................... 36
5.1 Organizational Requirements................................................................................ 36
5.2 Personnel Requirements........................................................................................ 39
5.3 Technical Requirements........................................................................................ 41
5.4 Ethical Issues......................................................................................................... 42
6	 A Penetration Testing Methodology............................................................................... 44
6.1 Requirements for a Penetration Testing Methodology.......................................... 44
Federal Office for Information Security - 2 -

<!-- page 3 -->

Study: A Penetration Testing Model 
6.2 The Five Phases of a Penetration Test................................................................... 44
6.3 Approach ............................................................................................................... 47
6.4 Modules for the Test Procedures........................................................................... 48
6.5 Module Descriptions ............................................................................................. 53
6.6 Penetration Test Documentation ........................................................................... 79
7	 Performing Penetration Tests.......................................................................................... 80
7.1 Preparation............................................................................................................. 80
7.2 Reconnaissance ..................................................................................................... 82
7.3 Analysis of Information / Risks............................................................................. 83
7.4 Active Intrusion Attempts ..................................................................................... 83
7.5 Final Analysis / Clean-Up ..................................................................................... 84
Glossary............................................................................................................................... 86
Bibliography........................................................................................................................ 90
Appendix ............................................................................................................................. 92
A.1 OSSTMM .............................................................................................................. 92
A.2 NIST Guideline on Network Security Testing...................................................... 93
A.3 ISACA Switzerland – Testing IT Systems Security With Tiger Teams ............... 93
A.4 Penetration Testing Certification........................................................................... 95
A.5 I and E Modules and Their OSSTMM Equivalents ............................................ 100
A.6 Checklists and Documentation Forms................................................................. 102
A.7 Tools 108
Federal Office for Information Security - 3 -

<!-- page 4 -->

Study: A Penetration Testing Model 
1 Introduction and Objectives of this Study 
This s tudy on “A Pe netration Testing Model ” add resses th e use of penetration tes ting in sec urity­
relevant IT systems. The security of systems that are linked to public networks can b e compromised 
by unauthorized, and usually anonymous, attempts to access them. This situation calls for test methods 
that ar e dev ised f rom the a ttacker’s pe rspective to e nsure t hat te st conditions are a s r ealistic as 
possible. 
Technically speaking, a penetration test is the controlled attempt at p enetrating a computer system or 
network from “outside” in order to detect vulnerabilities. It employs the same or similar techniques to 
those used in a genuine attack. Appropriate measures can then be taken to eliminate the vulnerabilities 
before they can be exploited by unauthorized third parties. 
This study is aimed at businesses and institutions whi ch of fer, or ar e pl anning to off er, pen etration 
tests. I t pre sents a structured app roach to pen etration testing tha t f acilitates - and can ens ure - the 
efficient and focused performance of such tests. The study is also designed to provide assistance with 
selection criteria to decision-makers in pr ivate and public entities who ar e planning to commission a 
penetration test. 
This study is not a guide to hacking networks and systems, which is why the authors have consciously 
refrained from including deta iled t echnical instructions a nd d escriptions o f t he tools us ed in 
penetration testing. 
1.1 Introduction to Penetration Testing 
By using public networks businesses and public authorities are exposed to numerous risks. Public and 
private entities are often unable to grasp the full extent of today’s complex communication structures 
and frequently have little or no control over them. Enterprises and public authorities connect to the 
internet, thereby y ielding som e of the ir responsibility (e.g . av ailability of ex ternal servers and 
networks), but also exposing themselves to new threats which need to be tackled appropriately. 
- 4 - Federal Office for Information Security

<!-- page 5 -->

Study: A Penetration Testing Model 
1.2 Methodology and Structure of this Study 
The structure of this study follows that of the penetration testing process, from a request for a proposal 
to test completion, including the necessary documentation. As a result, the methodology itself and its 
application are described at the end  of the study. Th is m eans t hat the re ader can either be g uided 
through a defined process or go straight to the chapters of interest. 
This study does not have to b e read in a particular order to be u nderstood, provided that the reader 
possesses the relevant specialist knowledge. 
The first chapter of this study contains a general introduction to the sub ject of penetration testing. It 
includes a definition of target groups and a description of the structure of this study. For the interested 
reader, the second chapter contains a brief introduction to IT security. 
The third chapter is an attempt at positioning penetration testing within the testing and auditing system 
by its goals (“what goals can be achieved with penetration tests?”), definitions (“what distinguishes a 
penetration test from an audit?”), and classifications (“what criteria should a penetration test fulfill?”). 
The fourth chapter deals with legal issues, with the focus more on civil law than criminal law aspects. 
The underlying conditions and o rganizational, personnel and technical requirements are add ressed in 
the fifth chapter, with special emphasis on “ethical” issues to highlight the limits of penetration testing 
and the appropriateness of the means. 
Once a ll the p rerequisites fo r p enetration testing have been di scussed, the methodology and 
documentation of such tests are described in detail. 
For ease of comprehension, we e xplain h ow th e m ethod i s im plemented in t he sev enth c hapter 
“performance o f pe netration t ests”. I n k eeping w ith the p ractical na ture of this s tudy, the re ader is 
given instr uctions on how to follow t he i ndividual steps t o f acilitate their application in pub lic or 
private entities. 
Information that is of interest but not directly related to the subject can be found in the appendix. The 
reader is provided with details about penetration test certification, further methodological information 
and suggestions for forms to be used. 
Federal Office for Information Security - 5 -

<!-- page 6 -->

Study: A Penetration Testing Model 
2 IT Security and Penetration Testing 
Penetration testing can reveal to w hat extent the s ecurity of I T systems is t hreatened by  attacks by 
hackers, crackers, etc., and whether the security measures in place are currently capable of ensuring IT 
security. For a clearer picture of the risks to I T security, this chapter begins with a summary of the 
current threats, describing the most common intruder profiles and widespread techniques for attacking 
IT systems. This is followed by a brief account of typical IT security measures, some of which can be 
tested with penetration tests. Finally, the process of devising penetration tests is explained. 
2.1 Threats 
A joint study by the U S Computer Security Institute (CSI) and the FBI [CSI02, p. 11] found that in 
2001 the companies questioned had sustained average losses of US$4.5m from information theft as a 
result of c omputer c rime. I ntruders can  hav e a r ange of m otives f or c arrying out a ttacks on I T 
infrastructure. The major intruder groups and their motives are outlined below. 
2.1.1 Intruder Profiles 
In the m edia, the term “hacker” is used to refer to any perso n w ho i ntrudes in to o ther I T sy stems 
without authorization. However, a f iner distinction is often made between “hackers”, “crackers” and 
“script kiddies”. Whereas “hackers” are regarded as being experimentally-minded programmers who 
target security loopholes in I T sy stems for technical reasons, “cr ackers” a re p eople wi th c riminal 
energy who exploit weak points of IT systems to gain illegal advantages, social attention or respect. 
“Script kiddies” are usually intruders lacking in-depth background knowledge and driven by curiosity 
who mainly direct attack tools downloaded from the internet against arbitrary or prominent targets. 
Crackers p ossessing priv ileged k nowledge abou t t he o rganization t hey are at tacking are te rmed 
“insiders”. I nsiders are of ten frustrated (former) em ployees of an organization who use the ir 
knowledge of internal affairs to harm that organization. The danger posed by insiders is particularly 
great because they are familiar with the technical and organizational infrastructure and may already 
know about existing vulnerabilities. 
In addition to the categories described above, industrial espionage also poses a serious threat. The aim 
of industrial espionage is to gain knowledge of business secrets such as innovative technical designs, 
strategies and ideas that help in gaining a com petitive edge and to u se such information for personal 
benefit. 
- 6 - Federal Office for Information Security

<!-- page 7 -->

Study: A Penetration Testing Model 
2.1.2 Methods 
There are several ways of m anipulating or damaging IT sy stems and of pr eparing an a ttack on I T 
systems. 
� Network-based attacks 
“Network-based attacks” are at tacks on ne twork com ponents, computer sy stems and/o r 
applications using network protocol functionalities. This kind of at tack exploits vulnerabilities or 
inadequacies in hardware and software in order to prepare or carry out attacks. 
Network-based att acks in clude po rt scanning, I P spoofing , sni ffing, ses sion hi jacking, DoS 
attacks, buffer overflow and  fo rmat st ring at tacks, as w ell as a ll other e xploitation of 
vulnerabilities in operating systems, application systems and network protocols. 
� Social engineering 
Social engineering attacks are attempts to m anipulate people with privileged knowledge to make 
them reveal security-related information such as pa sswords to t he a ttacker. Fo r in stance, an 
attacker could pretend to be an IT employee of an organization and trick an unsuspecting user into 
revealing his n etwork password. The range of possible attack scenarios is particularly wide with 
this technique. In its broadest sense, social engineering can also cover situations in which security­
related information is obtained by extortion. 
� Circumvention of physical security measures 
There can be no IT security without the physical security of the technical infrastructure. If physical 
security measures can be d efeated and physical access to IT systems gained, it is usually only a 
matter of time before an attack on or manipulation of stored applications and data can take place. 
An example is the unauthorized entry into the computer center of an organization and the removal 
of a hard disk on w hich confidential data are stored. This category also includes the searching of 
waste for documents with sensitive security-related information (dumpster diving). 
Federal Office for Information Security - 7 -

<!-- page 8 -->

Study: A Penetration Testing Model 
2.2 IT Security Measures 
Measures to  im prove I T secur ity ar e ne eded to c ombat the threats described above. However, one 
hundred-percent security can n ever be attained. Org anizational m easures, suc h as IT security 
organization an d es calation rules, a nd t echnical m easures, s uch as access controls, encryption and 
firewalls, are employed to establish a certain level of IT security. 
In line with the company IT security policy, all such measures are described in an IT security concept 
that is valid for the entire organization. 
If the org anization be ing tes ted i s unab le t o p resent a sec urity con cept or security pol icies, it is 
doubtful whether penetration testing is meaningful, especially when the I T landscape is complex. In 
such c ases, I T secu rity could  pro bably be im proved far m ore efficiently by first dev ising and 
implementing an appropriate security concept. 
2.3 Devising Penetration Tests 
The term “penetration test” and the m ethods used for tes ting were established in 1995 when the first 
Unix-based vulnerability scanner “SATAN” [Venema95] wa s i ntroduced. At that t ime the pr ogram 
was the first tool that was able to automatically scan computers to identify vulnerabilities. 
Nowadays, there are a number of freeware and commercial vulnerability scanners, most of which have 
an updatable database of known hardware and software vulnerabilities. These tools are a convenient 
way of iden tifying vulnerabilities in the systems being tested and therefore of determining the risks 
involved. Ordinarily, the information provided by such tools comprises a technical description of the 
vulnerability and also gives instructions as to how to eliminate a weak point by altering configuration 
settings. 
In addition, a l arge num ber of freeware tools fo r c arrying out or p reparing att acks on internet 
computers and networks can be found on the internet. 
- 8 - Federal Office for Information Security

<!-- page 9 -->

Study: A Penetration Testing Model 
2.4 Penetration Testing Procedures 
The procedure for penetration testing should follow the steps described below. 
1. Research information about the target system 
Computers th at can b e ac cessed ov er the in ternet m ust hav e an o fficial I P addre ss. Fre ely 
accessible databases provide information about the IP address blocks assigned to an organization. 
2. Scan target systems for services on offer 
An attempt is made to conduct a po rt s can of the c omputer(s) b eing t ested, op en por ts be ing 
indicative of the applications assigned to them. 
3. Identify systems and applications 
The nam es and v ersion of op erating systems and applications in the ta rget systems can be 
identified by “fingerprinting”. 
4. Researching Vulnerabilities 
Information about vulnerabilities of specific operating systems and applications can be researched 
efficiently using the information gathered. 
5. Exploiting vulnerabilities 
Detected v ulnerabilities c an be used to o btain un authorized access to the sy stem or to pre pare 
further attacks. 
The quality and value of a penetration test depends primarily on the extent to which the test caters to 
the client’s personal situation, i.e. how much of the tester’s time and resources are spent on detecting 
vulnerabilities related to the IT infrastructure and how creative the tester’s approach is. This process 
cannot be covered in the general description above, which is why there are huge differences in the 
quality of penetration testing as a service. 
Federal Office for Information Security - 9 -

<!-- page 10 -->

Study: A Penetration Testing Model 
3 Classification and Objectives of Penetration Testing 
This chapter outlines the possible starting poin ts an d acc ess cha nnels f or a pen etration test, the I T 
security and pro tection measures that can be tested, and how the tests differ from general IT security 
reviews and IT audits. 
3.1 Starting Points and Access Channels for Penetration Tests 
Typical starting points or points of attack for a penetration test are firewalls, web servers, RAS access 
points (e.g. modems, remote maintenance access points), and wireless networks. Given their function 
as a gateway between the internet and the company network, firewalls are obvious targets for attack 
attempts and starting points for penetration tests. Web servers have a h igh risk potential because of 
their m anifold functions a nd t he r esulting v ulnerabilities. O ther servers that offer serv ices tha t are 
accessible externally, such as e-mail, FTP and DNS, should be included in the test, as should “normal” 
workstations. 
3.1.1 Testable IT Security Measures 
A penetration test should test bo th l ogical I T s ecurity m easures su ch a s pas swords, and  phy sical 
measures such as access control systems. Frequently only logical controls are tested as this can usually 
be done remotely via th e net work whic h m akes the te sts le ss time-consuming, and beca use the 
probability of attacks on logical IT controls is thought to be far greater. 
3.1.2 Penetration Testing, IT Security Audit, IT Audit 
“Crackers” a im to acc ess p rotected d ata or m aliciously disru pt data processing. Unlike penetration 
testing, the purpose of security audits and IT audits is to g enerally examine the IT infrastructure in 
terms of its com pliance, efficiency, eff ectiveness, e tc. They  ar e no t necessarily aimed at detecting 
vulnerable points. For instance, a p enetration test does not involve verifying whether in the event of 
hardware damage certain data could be restored with a regular backup; it only checks whether such 
data could be accessed. This could also be done in a security audit or an IT audit, but normally from a 
different perspective and not in the technical depth characteristic of a penetration test. 
- 10 - Federal Office for Information Security

<!-- page 11 -->

Study: A Penetration Testing Model 
3.2 Objectives of Penetration Testing 
For a s uccessful penetration test that meets the client’s expectations, the cle ar definition of goals is 
absolutely essential. If g oals canno t b e at tained or cannot be  ach ieved e fficiently, the tester s hould 
notify the client in the preparation phase and recommend alternative procedures such as an IT audit or 
IT security consulting services. 
Client goals that can be attained by penetration testing can be divided into four categories: 
1. Improving security of technical systems 
2. Identifying vulnerabilities 
3. Having IT security confirmed by an external third party 
4. Improving security of organizational and personnel infrastructure 
The result of an IT penetration test should therefore be more than just a list of existing vulnerabilities; 
ideally it should also suggest specific solutions for their elimination. 
Below the four goal categories are discussed, with examples. 
3.2.1 Improving Security of Technical Systems 
Most pen etration tests are com missioned w ith the o bjective of improving the secu rity of technical 
systems. The tests are confined to technical systems such as firewalls, routers, web servers, etc., with 
organizational and personnel infrastructure not being explicitly tested. One example is a p enetration 
test to expressly check whether unauthorized third pa rties a re ab le to a ccess sy stems w ithin th e 
company’s LAN from the internet. Possible test results or findings are unnecessary open firewall ports 
or vulnerable versions of internet applications and operating systems. 
3.2.2 Identifying Vulnerabilities 
In contrast to the other three goals, identification is the actual objective of the test. For example, before 
combining two LANs in the wake of a company merger, the new LAN can be tested to see whether it 
is possible to penetrate it from outside. If this can be done in the penetration test, action has to be taken 
to secure the interface before the merger, or the two networks should not be combined at all. 
3.2.3 Having IT Security Confirmed by an External Third Party 
A penetration test can also be conducted to obtain confirmation from an independent external third 
party. It is important to note that a penetration test only ever reflects the situation at a particular point 
in time and cannot therefore yield assertions about the level of security that are valid in the future. 
Federal Office for Information Security - 11 -

<!-- page 12 -->

Study: A Penetration Testing Model 
Nevertheless, regular penetration testing may be suitab le for demonstrating the increased security of 
customer data in a webshop or other internet application. 
3.2.4 Improving Security of Organizational and Personnel Infrastructure 
Apart from testing the t echnical infrastructure, a pe netration test can also test the organizational and 
personnel in frastructure, to m onitor es calation p rocedures, for instance, w ith the scope and/or 
aggressiveness o f the tests b eing in creased st ep by  st ep. Social engineering techniques, such as 
requesting passwo rds ov er th e te lephone, can b e em ployed to asse ss the lev el of general secu rity 
awareness and the effectiveness of security policies and user agreements. 
The scope of such tests needs to be defined precisely in advance (see also section 5.4 Ethical Issues). 
- 12 - Federal Office for Information Security

<!-- page 13 -->

Study: A Penetration Testing Model 
3.3 Limits of Penetration Testing 
As the techniques used by potential attackers rapidly become more sophisticated and new weak points 
in cu rrent applications and IT systems ar e re ported almost da ily, one sing le pen etration tes t cannot 
yield an assertion about the level of security of the tested systems that will be valid for the future. In 
extreme cases , a new security loophole m ay mean tha t a successful at tack could take pl ace 
immediately after a penetration test has been completed. 
However, this in no way means that penetration tests are useless. Thorough penetration testing is no 
guarantee that a successful attack will not occur, but it does substantially reduce the probability of a 
successful attack. Because of the rapid pace of developments in IT, the effect of a penetration test is, 
however, relatively short-lived. The m ore protection the systems require, the more often penetration 
testing shou ld b e don e in order to r educe the probability of a successful attack to a lev el tha t is 
acceptable for the company. 
A penetration test cannot replace the usual IT security tests, nor is it a substitute for a general security 
policy, etc. A n authorization or data backup concept, for instance, can only be tested effectively and 
efficiently in other ways. A penetration test supplements established review procedures and tackles the 
new threats. 
3.4 Classification 
What criteria can be used to describe a penetration test, or what distinguishes one penetration test from 
another? D istinguishing fe atures, su ch as the ex tent of the systems tes ted, th e cau tiousness or 
aggressiveness of testing, etc., that characterize a specific penetration test have to be adapted to sui t 
the goal of the test to ensure efficient and effective testing with a calculated risk. Figure 1 shows a 
classification of possible penetration tests. On the left are six criteria for defining penetration tests, on 
the right are the various values for the criteria summarized in a compact tree diagram. 
Federal Office for Information Security - 13 -

<!-- page 14 -->

Study: A Penetration Testing Model 
Figure 1: Classification of penetration tests 
An appropriate penetration test – to meet the client’s goals - has to be defined on the basis of the above 
criteria. It should be noted that not all possible combinations are useful tests even though the criteria in 
the classification have been k ept as distinct as possible. An aggressive test is usually identified very 
quickly and is th erefore no t ideal i n com bination w ith st ealth techniques. S imilarly, an ov ert 
penetration test is not sui table, for example, for obt aining confidential information from employees 
warned in advance by means of social engineering techniques. 
The six criteria and their possible values are discussed below: 
1.	 Information base: What is the penetration tester’s initial level of knowledge about the target 
network or object? 
A fundamental distinction is made between black-box testing, without any insider knowledge, 
and white-box testing, where the tester has insider knowledge: 
1.	 A black-box test realistically simulates an attack by a typical internet hacker. The hacker has 
to research the necessary information in publicly available databases or make inquiries as an 
outsider. 
- 14 - Federal Office for Information Security

<!-- page 15 -->

Study: A Penetration Testing Model 
2.	 In a white-box test an attack by a (former) employee or external service provider with detailed 
knowledge in ce rtain areas. Th e ex tent o f suc h k nowledge can range f rom lim ited, e .g. as 
possessed by an employee who has wo rked in the company for only a short time, to in-depth 
system knowledge, such as t hat gained by an ext ernal IT service provider who has installed 
security-relevant systems. 
2. Aggressiveness: How aggressive is the penetration tester during testing? 
To allow a s ufficiently f ine d istinction, four lev els o f ag gressiveness are defined for the 
purposes of this study: 
�	 With th e l owest lev el th e tes t objects a re investigated passively on ly, i.e. any 
vulnerabilities that are detected are not exploited. 
�	 With the second level – cautious – identified vulnerabilities are only exploited when, 
to the best of the tester’s knowledge, the system being tested will not suffer as a result, 
e.g. using known default passwords or trying to access directories on a web server. 
�	 With the next level – calculated – the tester also attempts to exploit vulnerabilities 
that m ight resu lt in sy stem disrup tions. T his inc ludes, for ins tance, automatically 
trying out p asswords a nd ex ploiting k nown buffe r ov erflows in p recisely iden tified 
target systems. Before taking such steps, the tester considers how likely they are to be 
successful and how serious the consequences would be. 
�	 With th e h ighest level – aggressive – the tester tr ies to exploit all potential 
vulnerabilities, e.g . buf fer ov erflows a re u sed even on ta rget sy stems that are not 
clearly identified, or security systems are deactivated by deliberate overloading (denial 
of service (DoS)) attacks. The tester has to be aware that, in addition to the systems 
being tested, neighboring systems or network components might also fail as a result of 
these tests. 
3. Scope: Which systems are to be tested? 
When a penetration test is being carried out for the first time, a full test is advisable to ensure 
that no security loopholes are overlooked in systems that have not been tested. 
The time required for a penetration test is normally directly related to the scope of the systems 
to be investigated. Identical and near-identical systems can often be investigated in a s ingle 
test, but as soon as there are different configurations, each sy stem will need to be dealt with 
separately: 
�	 If only a speci fic sub-network, system or se rvice is to be tested, for the purposes of 
this study the penetration test is termed focused. This test scope is appropriate after a 
modification or extension of  the system landsca pe, for instance. Su ch a test can, of 
Federal Office for Information Security - 15 -

<!-- page 16 -->

Study: A Penetration Testing Model 
course, only provide information about the system that was tested; it canno t provide 
general information about IT security. 
�	 In a limited penetration test, a limited number of sy stems or services are examined. 
For example, all systems in the DMZ, or systems comprising a functional unit can be 
tested. 
�	 A full test covers all available systems. It should be noted that even in a complete test 
certain systems, e.g. outsourced and externally hosted systems, might not be able to be 
tested (see Section 5.1). 
4. Approach: How “visible” is the team during testing? 
If, in addition to the primary security systems, second ary sy stems - such as an I DS, or 
organizational or personnel structures (e.g. escalation procedures) - are to be tested, the testing 
approach will have to be adapted accordingly: 
�	 The penetration tests carried out on secondary security systems and existing escalation 
procedures should – at least in the beginning – be covert, i.e. in the initial survey stage 
only m ethods th at a re n ot di rectly ide ntifiable a s a ttempts a t a ttacking the sy stem 
should be employed. 
�	 If the covert approach fails to generate a reaction, or a white-box test is carried out in 
collaboration with those responsible for the system, overt methods, such as extensive 
port scans with a direct connection, m ay be em ployed. T he c lient’s s taff m ay be 
included in the team conducting an overt white-box test. This is particularly advisable 
with highly critical systems because it means that the testers are able to react faster to 
unexpected problems. 
5. Technique: What techniques are used for testing? 
In a conventional penetration test, systems are attacked via the network only. In addition, other 
types of physical attacks and social engineering techniques can be used to attack systems. 
�	 A network-based penetration test i s th e no rmal proc edure, an d s imulates a typical 
hacker attack. Most IT networks currently use the TCP/IP protocol, which is why such 
tests are also called IP-based penetration tests. 
�	 Apart from TCP/IP networks there are other communication networks that can also 
be used for staging an at tack. T hese include telephone an d f ax ne tworks, wi reless 
networks for mobile communication, e.g . base d on I eee 802.11 (b) and, in future, 
bluetooth technology, too. 
�	 Nowadays, secu rity sy stems such a s f irewalls e tc., are wide spread, and t he 
configurations of such systems usually afford a high level of security, which means 
- 16 - Federal Office for Information Security

<!-- page 17 -->

Study: A Penetration Testing Model 
that it is extremely difficult, if not impossible, to defeat such systems in an attack. It is 
often easier and quicker to obtain the desired or necessary data by circumventing these 
systems in a d irect physical at tack. A phy sical a ttack can, fo r example, involve 
directly acce ssing data at a non-password pro tected workstation after gaining 
unauthorized access to the building and/or server rooms. 
�	 People ar e f requently the w eakest link in the secu rity chain, which is why social 
engineering techniques that exploit inadequate security skills or insufficient security 
awareness are often successful. Such tests are appropriate after the introduction of a 
general security policy, for example, to assess the extent of its implementation and/or 
acceptance. False assumptions about the supposed effectiveness of a security policy 
often result in security risks that, provided that the situation is assessed accurately, can 
be m itigated by tak ing addit ional action. S ections 5.4  Et hical I ssuesand 4.2 Legal 
Framework for Penetration Testing discuss in detail how far such tests can go. 
6. Starting point: Where is the penetration test carried out from? 
The starting point of the penetration test, i.e. the point where the penetration tester connects 
his computer to the network or w here his attacking attempts originate can be either inside or 
outside the client’s network or building. 
�	 Most hack er attacks a re s taged v ia the network’s connection to the in ternet. A 
penetration test from the outside is therefore able to detect and evaluate the potential 
risk of such an a ttack. T ypically, the firewall, systems in the DMZ and RAS 
connections are investigated in such tests. 
�	 In a penetra tion test from the inside, the tester does not normally have to ov ercome 
firewalls or entry controls to access internal networks. Therefore a test from the inside 
can assess the effects of an error in the firewall configuration, a successful attack on 
the firewall, or of an attack by persons with access to the internal network. 
3.5 Multistage Approach 
In order to m inimize risks, a combination of the different penetration tests shown in the classification 
is often advisable. For instance, a cautious, covert black-box test can be carried out from the outside in 
a first step, followed by an aggressive, overt white-box test from the in side. This approach combines 
the advantages of a black-box test - a realistic simulation of a g enuine attack - with the b enefits of a 
white-box test in terms of efficiency and damage limitation. 
Federal Office for Information Security - 17 -

<!-- page 18 -->

Study: A Penetration Testing Model 
4 Legal Issues 
The legal issues that have to be  considered when co nducting penetration tests can be subdivided into 
three types: 
�	 Legal issues that can induce or motivate a business or a public authority to conduct a 
penetration test. 
�	 Legal reg ulations a nd pr inciples that the tester sho uld ob serve when conducting 
penetration tests and which should be clarified with the client prior to testing. 
�	 Legal asp ects whi ch fo rm the basis of the cont ract between client and penetration 
tester. 
4.1 Legal Reasons for Penetration Testing 
While there are no laws that require a c ompany or public  authority to com mission penetration tests, 
there are binding legal provisions relating to 
� security handling and the availability of data relevant to tax and commercial law, 
� treatment of personal data, 
� the establishment and organization of an internal control system. 
In order to p rotect com pany data, companies o ften take m easures to g uarantee the availability, 
confidentiality and integrity of data or to ensure access for authorized persons only. These mesaures 
include security conce pts, authorization co ncepts and fir ewall systems. However, establishing these 
kinds of security sy stems is no g uarantee t hat th e leg al re quirements a re m et. R ather, th e sy stem’s 
compliance w ith th e l egal re quirements and s tipulations m ust b e che cked for each invidual cas e. 
Penetration tests are a suitable means of verifying the effectiveness of such measures in certain areas. 
The most important legal regulations which have to be ob served when establishing and m aintaining 
security and authorization systems are presented below in context for use in implementing penetration 
tests. 
4.1.1 German Commercial Code (HGB) 
Sec. 238 (1) of the Ge rman Com mercial Code (HGB) stipulates that an e ntrepreneur k eep h is/her 
books in accordance with the Generally Accepted Accounting Principles (GoB) or in accordance with 
the Generally Accepted Principles of C omputer-Assisted A ccounting Sy stems (G oBS) ( interpretive 
letter of the Federal Ministry of F inance to the supreme tax a uthorities of the states of November 7, 
1995). 
- 18 - Federal Office for Information Security

<!-- page 19 -->

Study: A Penetration Testing Model 
Section Four of the GoBS contains the regulations regarding the internal control system (ICS) of an 
enterprise: 
�	 No. 4.1: “An I CS usual ly ref ers to all com plementary and in terconnected co ntrols, 
measures and arrangements which s erve th e fo llowing purp oses: se curing and 
protecting existing assets and information from losses of all kinds. […]” 
Section Five GoBS contains provisions relating to data security: 
�	 No. 5.1: “The strong dependence of an enterprise on its stored information makes an 
in-depth data security concept essential for compliance with the GoBS. [...]” 
�	 No. 5.3: “ This information must be protected from loss and auth orized modification. 
[...]” 
�	 No. 5.5.1: “Information must be protected against unauthorized modification through 
effective access controls. [...]” 
The provisions listed above illustrate the high demands on data security which are put on enterprises. 
These legal requirements can  only  be m et by  hav ing an I T secur ity concep t ( called “dat a security 
concept” in GoBS terminology) that is part of an internal control system. A penetration test can help 
verify on a sampling basis whether a security concept of this type meets the high legal requirements. 
4.1.2 Law on Control and Transparency in Business (KonTraG) 
Since the Law on Control and Transparency in Bus iness (KonTraG) came into force in May 1998, 
management boards of s tock co rporations ar e r equired to establish a risk m anagement sy stem and 
carry out extended reporting to the supervisory board. Sec. 91 (2) of the German Stock Corporation 
Act ( AktG) was revised as follows: 
�	 Sec. 91 (2) Ak tG: “The m anagement board must tak e appropriate measures; in 
particular, set up a monitoring system for early recognition of developments posing a 
risk to the going concern. [...]” 
Due to the “spillover effect” this change in the regulations also applies to the management of a limited 
liability company (GmbH). 
The legislation does not stipulate how such a risk management system should actually be set up. The 
Act doe s, howev er, state that a risk management system must conta in elements such  as an ea rly 
warning sy stem, an in ternal monitoring system including an audit a nd con trolling. [And ersen99, 
Federal Office for Information Security - 19 -

<!-- page 20 -->

Study: A Penetration Testing Model 
p. 20]. Here, penetration tests are an appropriate way of testing the IT-related part of the early warning 
system or parts of the audit. 
4.1.3 German Banking Act (KWG) 
Banks and other o rganizations in the financial se rvices se ctor a re su bject to the regulations o f th e 
German B anking A ct (K WG). O ne special fea ture of the G erman B anking A ct is that the F ederal 
Financial Supervisory Agency is enti tled to conduct audits at all financial services institutions which 
may extend to all business areas of the company. 
Sec. 44 (1) contains the following regulation: 
�	 “[...] The Fe deral F inancial Su pervisory Agency may carry out audi ts at the 
institutions even if there is no special reason for them and transfer the execution of the 
audits to the Deutsche Bundesbank. [...].” 
The area of internet security can be subject to an audit pursuant to Sec. 44 (1) KWG , particularly at 
banks which make their financial services available online. 
It is therefore advisable that these banks carry out penetration tests before an audit of this kind in order 
to test the security of the internet applications used, identify vulnerabilities and issue recommendations 
on action for remedying any deficits. 
4.1.4 Ordinances and Pronouncements of the Federal Financial Supervisory Agency 
(BAFin) 
The Fede ral Fin ancial Superv isory Ag ency (prev iously k nown as the Fede ral Banking Supervisory 
Office - BAFin) is legally autho rized to i ssue ord inances and publish pron ouncements th at affect 
banks and o ther f inancial s ervices p roviders th at come under BAFi n sup ervision. T he following 
pronouncement is particularly interesting in relation to penetration testing: 
“Statement Covering Minimum Requirements for the Trading Activities of Credit Institutions”, which 
defines the requirements f or the risk management sy stem and th e org anization of the internal audit 
function. 
It contains the following statements on the risk management system: 
�	 No. 3.1 Sy stem Requir ements: “[ ...] [ The r isk m anagement sy stem] should  be 
incorporated into an overall risk monitoring and management structure covering as far 
as possible all the bank’s areas of business and should facilitate the identification and 
analysis of comparable risks from nontrading activities. [...]” 
- 20 - Federal Office for Information Security

<!-- page 21 -->

Study: A Penetration Testing Model 
�	 No. 3.4 Operational Risks: “[...] A written contingency planning has to ensure, among 
other things, that in the event of the breakdown of the technical equipment necessary 
for trading activities, back-up facilities can be deployed at short notice. In addition, 
precautions are to be taken to cope with possible software errors and with unforeseen 
staff absences. The procedures, documentation requirements, data processing systems 
and contingency plans in use for the trading activities are to be regularly reviewed.” 
Penetration testing puts a bank in a be tter position to j udge the potential effects of an attack. They 
allow a definite statement to be made on the fuctionality of the risk mangement system. 
The statement contains the following requirements in relation to the organization of the internal audit 
function: 
�	 No. 5 Audi ting: “Com pliance w ith th e m inimum requirem ents i s to be ch ecked a t 
irregular, appropriate intervals by the internal auditors. The main audit areas should be 
subjected t o a risk-oriented aud it at least once  a y ear. Ea ch subdivision of the 
minimum requirements is to be audited at least at three-yearly intervals; the audit rota 
is to be documented in an audit plan. 
The main audit areas are as follows: 
� Changes in the IT systems.” 
Penetration tests can provide effective support for risk-oriented monitoring of the main audit areas in 
an IT audit. 
4.1.5 Federal Data Protection Act (BDSG) 
Both state and federal law contain legal provisions relating to data protection, governing the treatment 
of personal data by public and non-public bodies. 
In accordance with Sec. 1 II BDSG, the Federal Data Protection Act (BDSG) applies to the collection, 
processing and use of personal data by 
1. public bodies of the Federation, 
2. public bodies of the states, insofar as data protection is not governed by state legislation […], 
3.	 private bodies insofar as they process or use data in data processing systems or in or from data 
files, or collect data for use in such systems or files […]. 
�	 Sec. 9 (1) BDSG t echnical and organizational measures: “Public and private bodi es 
processing personal data either on their own be half or on b ehalf of others shall take 
Federal Office for Information Security - 21 -

<!-- page 22 -->

Study: A Penetration Testing Model 
the technical and organizational measures necessary to ensure the im plementation of 
the provisions of this Act, in particular the requirements set out in the annex to this 
Act.” 
The ann ex r eferred t o in this Act contains requirements r elating to adm ission co ntrols, 
access controls, relaying controls, input controls, task controls and availability controls. 
�	 Sec. 9a BDSG data protection audit: “For improved data protection and data security, 
providers of data processing systems and prog rams and da ta processing bodies may 
have their data protection concept and their technical equipment tested and evaluated 
by independent and registered experts and publish the result of the examination. [...]” 
Penetration tests can be used in a data protection audit as an efficient audit tool for asserting whether 
the regulations have been implemented and whether the data protection concept is effective. 
Note: EU Data Protection Directive (95/46/EU) 
The BDSG was amended on May 18, 2001 to implement the EU Da ta Protection Directive 94/46/EU 
in Germany. 
Article 17 (1) of the Directive emphasizes the necessity of a security concept for companies in the EU: 
“Member States shall provide that th e con troller m ust implement appro priate t echnical a nd 
organizational m easures to p rotect p ersonal da ta ag ainst accidental or unlawful destruction or 
accidental lo ss, a lteration, un authorized di sclosure o r ac cess, in  par ticular w here the pro cessing 
involves the transmission of data over a network, and against all other unlawful forms of processing. 
[...]” 
An additional amendment to th e BDSG is anticipated with the implementation of the European Data 
Protection Directive for E lectronic Communication (2002/58/EU), which will lead to adjustments in 
the processing of personal data and protection of privacy in telecommunications in response to recent 
developments in the markets and technologies for electronic communication services. 
�	 Article 4 (1 ) [security]: “The provider of a public electronic communications service 
must take appropriate technical and organizational measures to saf eguard security of 
its se rvices, if nec essary in conjunction with the prov ider of the public 
communications network with respect to network security. [...]” 
The Directive provides for implementation by October 31, 2003 at the latest. 
- 22 - Federal Office for Information Security

<!-- page 23 -->

Study: A Penetration Testing Model 
4.1.6 Treaty on Media Services (MDStV) 
The Treaty on M edia Se rvices is a imed at c reating a uni form fram ework for the v arious use s of 
information and communication services which are designed for a general audience. 
The MD StV is m ainly g eared towards enterprises that of fer m edia s ervices com mercially. A 
distinction is made between “distribution services” and “service providers”. A distribution service is 
the p rovider of a m edia se rvice (e.g. te leshopping). A se rvice provider enables access to a media 
service. When an enterprise or an authority provides its employees with internet access it also becomes 
a service provider and must observe the regulations of MDStV. 
The following paragraphs can be seen as relating to penetration tests from an auditing perspective: 
�	 Sec. 13 (2) MD StV [prov ider’s obligations]: “Th e provider o f m edia se rvices m ust 
make technical and organizational provisions to ensure that […] 3. the user can use 
media services protected from the knowledge of third parties. [...]” 
�	 Sec. 17 MDStV [data protection audit]: “To improve data protection and data security, 
providers of media services can have their data protection concept and their technical 
equipment tested and evaluated by independent and registered experts and publish the 
result of the examination. [...]” 
Penetration te sts can  be u sed specifically to te st both the def ined technical and organizational 
provisions and the data protection concept. 
4.1.7 Teleservices Act (TDG) and Teleservices Data Protection Act (TDDSG) 
The Teleservices Act is intended for services providers that “make their own teleservices or those of 
third parties available f or us e o r prov ide ac cess to their use. ” A  t eleservice i s, f or ex ample, an 
individual communication service or an interactive ordering facility. As such,  every organization that 
publishes information on an internet website, for example, or provides an e-mail contact address is a 
services provider. 
The Teleservices Data  Pro tection Act  se ts ou t a legal framework for data protection, within which 
services providers are permitted to collect, process and use the personal data of users. 
�	 Sec. 4 (4) TDDSG [ services p roviders’ o bligations]: “T he se rvices prov ider m ust 
make technical and org anizational p rovisions to e nsure t hat [… ] t he us er can u se 
teleservices protected from the knowledge of third parties.” 
Federal Office for Information Security - 23 -

<!-- page 24 -->

Study: A Penetration Testing Model 
Here, penetration tests could likewise be used as a control tool for monitoring the effectiveness of the 
data protection concept. 
4.1.8 The Telecommunications Act (TKG) 
This A ct i s in tended for commercial pr oviders of telecommunications s ervices. I t m ainly affec ts 
telephone com panies and internet se rvice p roviders. Companies in which em ployees use the ir 
telephone connection or their internet access at their workplace for private purposes are also deemed 
providers of telecommunications services and therefore fall under the scope of the Act. [LfDN99] 
One of the ob jectives of the Tel ecommunications A ct (TKG) is t o m aintain telecommunications 
secrecy in the field of telecommunications. 
�	 Sec. 85 (2) TKG  [telecommunications secrecy]: “Whosoever commercially provides 
or assists in the provision of telecommunications services shall be obliged to maintain 
telecommunications secrecy. [...] 
�	 Sec. 87 (1) TKG  [pro tective technical precautions]: “Whosoever operates 
telecommunications systems serving the commercial provision of telecommunications 
services shall take appropriate technical precautions or o ther measures with regard to 
telecommunications and data processing systems operated for such purpose in order to 
protect […] 
2. program-controlled te lecommunications and d ata proc essing sy stems 
against unauthorized access, […] 
4. telecommunications and data processing systems against external attack and 
the effects of natural disasters.” 
Here too, penetration tests can be implemented to test the IT security concept. 
4.1.9 Criminal Law 
Computer crime has r isen exorbitantly over the last few years. Overall, however, the possibilities for 
imposing sanctions under criminal law are limited and the creation of new criminal offenses has not 
yet led to any reduction in computer crime. The range of criminal offenses currently set out in German 
criminal law is meager and fails to offer any effective protection in terms of general crime prevention. 
In addition to this, it is often difficult to provide evidence of the offenses. 
The prov isions of the G erman C ivil Code [“Strafgesetzbuch”: St GB] th at a re relevant to com puter 
crime are mainly in t he sections “V iolation of the Realm of P ersonal Privacy and C onfidentiality”, 
“Fraud and Breach of Trust”, “Falsification of Documents” and “Damage to Property”. 
- 24 - Federal Office for Information Security

<!-- page 25 -->

Study: A Penetration Testing Model 
The fo llowing prov ides a sum mary of the criminal offenses which can be com mitted thr ough 
unauthorized access to data processing systems. 
�	 Sec. 202a (1) StGB [data espionage]: “Whoever, without authorization, obtains data 
for himself or another, which was not intended for him and w as specially protected 
against unauthorized access, shall be punished with imprisonment for not more than 
three years or a fine.” 
This c riminal of fense p rimarily prot ects all sto red dat a and dat a in transfer against unauthorized 
access; the criminal act is the obtaining of data. 
Section 263a StGB [computer fraud]: “Whoever, with the intent of obtaining for himself or a third 
person an unlawful material benefit, damages the assets of another by influencing the result of a data 
processing operation through incorrect configuration of a program, use of incorrect or incomplete data, 
unauthorized use of data or other unauthorized influence on the order of events, shall be punished with 
imprisonment for not more than five years or a fine.” 
The manipulation of a data processing procedure with the intent of obtaining for oneself or for a third 
person an unlawful material benefit is punishable. The c riminal offense contained in Sec. 263a StGB 
further requires the of fender to hav e acted intentionally and with the aim of obtaining an unlawful 
material benefit for himself or for a third person. 
�	 Sec. 268 (1) StGB [ falsification of technical recordings]: “Whoever, for purposes of 
deception in legal relations 1.) produces a counterfeit technical recording or falsifies a 
technical recording; or 2 .) uses a counterfeit or fa lsified technical recording, shall be 
punished with imprisonment for not more than five years or a fine.” 
Pursuant to Sec. 268 (2) StGB, technical recordings refer to “a representation of data, measurements or 
calculations, conditions or sequences of events, which, in whole or in part, is produced automatically 
by a technical device, allows the object of the recording to be recognized either generally or by experts 
and is intended as proof of a legally relevant fact”. The criminal offense of Sec. 268 (1) StGB is the 
production of a counterfeit technical recording, the falsification of a technical recording or the use of a 
counterfeit or falsified technical recording. However, to commit the criminal offense of S ec. 268 (1) 
StGB, the offender must also act in order to deceive in legal relations or, pursuant to Sec. 270 StGB, 
influence the data processing by means of falsification. 
Federal Office for Information Security - 25 -

<!-- page 26 -->

Study: A Penetration Testing Model 
�	 Sec. 269 (1) StGB [ falsification of leg ally relevant data]: “Whoever, in ord er to 
deceive in legal relations, stores or modifies legally relevant data in such a way that a 
counterfeit or falsified document would exist upon its retrieval, or uses data stored or 
modified in such a m anner, shall be pu nished with imprisonment for not more than 
five years or a fine.” 
The above comments on Sec. 268 (1) StGB are also relevant here. 
�	 Sec. 303 a (1 ) StGB [alteration of d ata]: “W hoever unlawfully deletes, suppresses, 
renders unusable or alters data shall be punished with imprisonment for not more than 
two years or a fine.” 
These paragraphs make the un lawful deletion, sup pression, rendering unusab le or al teration of  data 
punishable by law. 
�	 Section 30 3b StGB [computer sabo tage]: “Whoever in terferes with dat a processing 
which is of material significance to the business or enterprise of another or a public 
authority by 1.) com mitting an act unde r Section 303a; or 2.) destroying, damaging, 
rendering unusable, removing or altering a d ata processing system or a da ta carrier, 
shall be punished with imprisonment for not more than five years or a fine.” 
4.1.10 European Convention on Cybercrime 
The European Convention on C ybercrime was adopted by the Minister Committee of the European 
Council on November 8, 2001 w ith the aim of p roviding laws and p rocedures for the eradication of 
computer crime. It was signed by Germany and other  member states of the European Council. It is, 
however, yet to be ratified. 
Chapter Two of the Cybercrime Convention describes cases (measures to be taken at a national level) 
that a country must make punishable with regard to eradicating computer crime. 
The parts of the Convention that are relevant for pe netration testing are Titles 1 and 2 of Section 1 
[substantive criminal law]. 
�	 Title 1: Offenses against the confidentiality, integrity and availability of computer data 
and systems 
- 26 - Federal Office for Information Security

<!-- page 27 -->

Study: A Penetration Testing Model 
o	 Article 2: Illegal access/unauthorized intrusion into computer systems and 
networks 
o Article 3: Illegal interception/unauthorized interception of network traffic 
o Article 4: Data interference/unauthorized alteration of data 
o Article 5: System interference/impairment or sabotage of computer systems 
o	 Article 6: Misuse of d evices/possession and  m isuse o f sy stems and tools 
that are suitable for carrying out an action as in Article 2-5. This article does 
not, however, refer to the unauthorized use of security tools that are used for 
protective purposes, such as penetration tests. 
� Title 2: Computer-related offenses 
o Article 7: Computer-related forgery 
o Article 8: Computer-related fraud 
Article 6 of  the C onvention makes part icularly cle ar that the a uthorized use of hacker and secu rity 
tools does not conflict with the purpose of the article. Neither does the Cybercrime Convention intend 
to hinder the work of a penetration tester by making his ac tivity punishable under law. However, the 
Convention is yet to be implemented in German law. 
4.2 Legal Framework for Penetration Testing 
During a penetration test, the tester carries out actions that, if performed without the client’s consent, 
may contravene present law. 
4.2.1 Criminal Law 
The penetration tester will usually not commit a c riminal of fense s ince he do es no t a ct w ith the 
necessary inten tions –  such  as that o f unl awful en richment. Mo reover, such ac ts of intrusion, the 
content and scope of which has been agreed on with the client, is justified by the approval of the latter. 
The exact definition of the scope of action by the client and the tester is therefore decisive (cf. 4.3.3 
“Subject of the ag reement”). Once the actual scope of action has been defined, it is helpful to obtain 
the necessary approval in the form of a separate declaration by the client prior to commencing testing. 
The following provisions are also significant with regard to the client’s approval: 
Federal Office for Information Security - 27 -

<!-- page 28 -->

Study: A Penetration Testing Model 
Access Control Services Protection Act (ZKDSG) 
The ZKDSG regulates the p rotection of access-controlled services a nd ac cess con trol s ervices. A n 
access-controlled services is, among other things, a teleservice within the meaning of Sec. 2 TDG or a 
media service within the meaning of Sec. 2 MDStV. An access control service is a technical process or 
facility that enables the authorized use of an access-controlled service. 
By adopting this law, the legislator wanted to guarantee the protection of fee-attracting services such 
as pay TV against the unauthorized manipulation of security mechanisms. 
�	 Sec. 3 Z KDSG [prohibition of commercial intervention to circumvent access control 
services]: “1.) The production, import and distribution of circumvention facilities for 
commercial purposes, 2.) the pos session, te chnical installation, maintenance and 
exchange of circumvention facilities for commercial purposes and 3.) the promotion 
of circumvention facilities are prohibited.” 
An access-controlled service is, for example, a password-protected WWW or FTP server. The purpose 
of a penetration test is to circumvent an existing security mechanism. This means that as soon as tools 
are used to perform the pe netration test (circumvention facilities), an infringement of the ZKDSG is 
unavoidable. A  pe netration t ester w ill a lso n ormally fulf ill th e cr iterion o f t he u se of  hack er and 
security tools for business purposes. Accordingly, a penetration tester who has an exploit for remotely 
accessing a password-protected web server could be committing an offence and may face a f ine of up 
to EUR 50,000.  [Emmert02, p.6] In such c ases it is advisable to obt ain the re levant permission from 
the authorized user in case of any acts that could constitute a criminal offense. 
The Telecommunications Act (TKG) 
The following provisions of the TKG could be relevant for a penetration tester: 
�	 Sec. 65 (1) [abuse o f t ransmitting equipment]: “I t sha ll b e p rohibited to ow n […] 
transmitting equipment […] which, by its form, simulates another object […] and, due 
to su ch c ircumstances, i s par ticularly suitable to i ntercept the non- publicly spoken 
words of another person without such person detecting this.” 
�	 Sec. 86 TKG [prohibition to intercept, obligation of operators of receiving equipment 
to maintain s ecrecy]: “Interception by  m eans of r adio equ ipment of m essages n ot 
intended for that radio equipment shall not be permitted. [...]” 
- 28 - Federal Office for Information Security

<!-- page 29 -->

Study: A Penetration Testing Model 
These regulations p rohibit ac tions that a re pe rformed dur ing penet ration tests, such as the use of 
network sn iffers fo r intercepting network traffic, unless the authorized use r ha s g iven his /her pr ior 
permission. 
Proposal for a Council Framework Decision on Attacks Against Information Systems 
On April 19, 2002, the European Commission issued a proposal for a Council Framework Decision on 
attacks on information systems. T he f ramework decis ion is a imed at b ringing in line t he v arious 
member states’ criminal law provisions for attacks on information systems and improving cooperation 
between the authorities. 
It comprises 14 articles, of which articles 3 and 4 contain details on criminal offenses: 
�	 Article 3 [illegal access to information systems]: “Member States shall ensure that the 
intentional access, without right, to the whole or any part of an information system is 
punishable a s a c riminal of fence w here it is c ommitted 1.) against any part of an 
information system which is  sub ject to sp ecific p rotection m easures; or 
2.) with the intent to c ause dam age to a natural or legal person; or 
3.) with the intent to result in an economic benefit.” 
�	 Article 4 [illegal interference with information systems]: “Member States shall ensure 
that th e fo llowing in tentional conduct, w ithout right, is p unishable a s a criminal 
offence: 
(a) the serious hindering or i nterruption of the func tioning of an info rmation system 
by inputting, transmitting, damaging, deleting, deteriorating, altering, suppressing or 
rendering inacc essible computer da ta; 
(b) the d eletion, d eterioration, a lteration, su ppression o r rendering inaccessible of 
computer data on an information system where it is committed with the in tention to 
cause damage to a natural or legal person.” 
Further developments in the framework decision remain to be seen. However, we can already say that 
a penetration tester who acts at the consent of his client and remains within the scope of action defined 
by the client, will remain unpunishable after the framework decision has come into force since he will 
normally lack the intention to commit a punishable act or his act would be justified due to the approval 
of the authorized user. 
4.2.2 Works Constitution Act (BetrVG) 
If a com pany that c ommissions a pen etration te st h as a  work s coun cil, i t s hould be no ted that the 
works council has a right to be informed (Sec. 80 II BetrVG). With respect to the regulation in Sec. 87 
Federal Office for Information Security - 29 -

<!-- page 30 -->

Study: A Penetration Testing Model 
(1) No. 6 BetrVG, the  work s coun cil sho uld be i nvolved in the p lanning of the p enetration t esting 
process. 
�	 Sec. 87 (1) No. 6 Bet rVG [rights of codetermination]: “The works council shall […] 
codetermine on the following matters: 
o	 the introduction and application of technical equ ipment fo r m onitoring the 
behavior or performance of the employees.” 
The purpose of p enetration t ests i s t o che ck the e ffectiveness of existing secu rity fac ilities. A 
penetration test can also se rve as a  too l f or assessing the p erformance of  em ployees. For  exam ple, 
social engineering techniques are used explicitly to examine the behavior of employees. 
But even when it is not the main purpose of a penetration test to monitor or assess the performance of 
employees, the results of a p enetration test are generally suited to doing just that. According to the 
Federal L abor Co urt (“ Bundesarbeitsgericht”), w hat i s dec isive is w hether o r no t th e eq uipment is 
objectively suit able fo r m onitoring, reg ardless o f whe ther th e em ployer pur sues th is o bjective and 
actually evaluates the data obtained in the monitoring process. We strongly recommend involving the 
works council at an early stage, even when its approval is not required for certain test procedures. 
4.3 Important Terms in Contracts Between Penetration Tester and Client 
4.3.1 What Type of Contract is a Penetration Test Contract? 
A penetration test is n ormally a se rvice for rem uneration. As op posed to a con tract fo r work  and 
services, the agreed service only is due, but no particular economic outcome. 
4.3.2 General Terms and Conditions 
If the tester has general terms and conditions, these must be included in the contract. The client must 
have been made aware of them and agree to their validity. 
4.3.3 Subject of the Contract 
In addition to the purpose of the penetration test, the parties must define in the contract the nature and 
scope of the tools and techniques to be used. 
Key elements of the subject of the contract are: 
� Objective(s) of the penetration test 
- 30 - Federal Office for Information Security

<!-- page 31 -->

Study: A Penetration Testing Model 
The con tract should c learly s tate t he ob jective be ing pur sued by the organization 
commissioning the pe rformance of  a pe netration t est. T he most com mon objectives 
relevant here are: 
o Increasing the security of the technical systems, 
o	 Identifying vulnerability as a criterion for making decisions (e.g. for investments 
or the suitability of products), 
o Obtaining certification/confirmation from an external third party, 
o Increasing the security of the organizational/personnel infrastructure. 
There is a de tailed ov erview of p ossible ob jectives in section 3.2 of this stu dy 
“Objectives of penetration testing”. 
� Nature of the penetration test 
Reference should be made to the type of penetration test to be performed (see section 
3.4 of this study “Classification”). The following classification criteria may be used: 
o Information base (black-box or white-box test) 
o Aggressiveness (passive/scanning to aggressive) 
o Scope (full, limited or focused) 
o Approach (covert or overt) 
o	 Technique (network-based, other communications, phy sical ac cess, so cial 
engineering) 
o Starting point (from the outside or the inside) 
By making these k inds of specifications the tes ter avoids unne cessary 
misunderstandings and risks right from the start and ensures that the penetration test is 
tailored to the client’s n eeds. I n addit ion, the s cope of the client’s app roval, whi ch 
should be obtained as a precaution from a criminal law perspective, is defined. 
� Techniques to be used and excluded 
The individual techniques used in a penetration test are to be described in more detail 
where this i s bo th pos sible a nd a ppropriate. I n part icular, any  soc ial engineering 
Federal Office for Information Security - 31 -

<!-- page 32 -->

Study: A Penetration Testing Model 
techniques and active tests of ac cess con trols to b e em ployed shou ld b e des cribed. 
Because soc ial eng ineering tec hniques are by nature problematic and possibly 
unethical, it is appropriate to specify a cl ear framework for th em (e.g . av oiding 
incitement o f em ployees t o beh ave unet hically). A n active test of acc ess cont rols 
attempts to circumvent physical security measures, which can be regarded as burglary. 
An expl anation of the circumstances un der which the tes t is to tak e place is also 
necessary in this respect. 
It is also important to exclude attacking techniques which are expressly not to be used. 
Such techniques should also be defined in the contract, stating the reasons for the ir 
exclusion. 
4.3.4 Client 
Particularly conc erning the a pproval re quired for taking potentially damaging measures during the 
testing process, it is important that the cont ract is signed by a legal representative of the cl ient. This 
means that only a person authorized to represent him, e.g. for a trading company, the general manager, 
an authorized signatory or another person with a similar individual authorization, such as the head of 
the IT department, may commission the performance of the penetration test. 
Before performing the penet ration test, the penetration tester should request appropriate evidence to 
satisfy himself that the client’s representative is authorized to represent him. 
4.3.5 Tester 
If the tes ter intends to contract out parts of the test, an “opening clause” should be included in the 
contract. However, since areas relevant to security are affected, the cl ient will not norm ally agree to 
this k ind of open ing clause. It is the refore helpful to name the subc ontractor when the cont ract is 
concluded. This ens ures th at o nly the se p ersons are auth orized to perform the tes t procedures. 
Appointing executing parties is particularly important when unconventional testing procedures such as 
social engineering or the circumvention of physical security measures have been planned, since this 
protects both parties and helps avoid misunderstandings. 
4.3.6 Written Form 
All terms of the contract must be agreed in writing. In addition, the parties should expressly agree to a 
requirement of writing, which should cover all subsidiary agreements. 
- 32 - Federal Office for Information Security

<!-- page 33 -->

Study: A Penetration Testing Model 
4.3.7 The Client’s Obligations 
In the interests of the penetration tester, the contract should set out the client’s legal duty to cooperate 
in as much detail as possible. The following elements should be taken into account: 
� Provision of information depending on the nature of the penetration test 
Depending on the nature of the penetration test, the penetration tester may be rel iant 
on ext ensive inf ormation f rom the cl ient. Fo r ex ample, a whi te-box tes t r equires 
information o n D NS nam es, I P addresse s, se curity policies, system configurations, 
firewall rules, e scalation pro cedures, et c. The penetration tes ter should the refore 
provide the client with a list of the required information before concluding the contract 
and agree in the contract that all required information be made available in time. 
� Information from potentially affected third persons 
During normal data traffic on public networks, a penetration test also uses third party 
systems (e.g. the c ommunication server of a provider, the web server of a mainframe 
computer). Since it is impossible to  exc lude im pairing the p erformance o f t hese 
systems, w e a dvise gi ving a dvance not ification of  t he penetration tests to a ny third 
persons who m ay be aff ected. Th ese information dut ies cou ld b e de legated to the 
client as it is in a better position to estimate which third parties could be affected by 
the tests. 
� Protective measures for unforeseeable system failure 
Since it cannot be completely ruled out that systems are impaired during testing such 
that data is lost, it is in the client’s own interests to create data backups of the high-risk 
and r elevant sy stems w here this h as no t a lready been done in fulfillment of the 
Generally Acce pted Pr inciples o f Com puter-Assisted Accounting Sy stems (GoBS). 
Data backups ensure that the d ata can be recovered i f ne cessary and m itigate the 
potentially adverse effects of data loss. 
4.3.8 The Tester’s Obligations 
In the client’s interests, the tester should be assigned the following obligations: 
� Secrecy 
In the cours e of a pen etration test, a pen etration tester m ay gain acc ess to highly 
sensitive information on vulnerabilities in the client’s network. This information must 
not be made available to third pe rsons so  as to reduce th e r isk to the client t o a 
Federal Office for Information Security - 33 -

<!-- page 34 -->

Study: A Penetration Testing Model 
minimum. The tester should therefore be b ound to observe secrecy in r espect of the 
information m ade av ailable to h im as w ell as the information w hich cam e to his 
knowledge in the course of testing. 
� Compliance with licensing regulations 
The te ster is responsible fo r com plying with l icensing reg ulations when using 
commercial security tools. Since the royalties for the use of security tools are normally 
charged on to the client, the client should be provided with a clear breakdown of these 
charges. 
� Documenting the testing procedures and results 
The nature and scope of the docum entation of the te sting procedures and the results 
should be s pecified in the contract. Th e t ester should be obliged to p rovide precise 
documentation of his testing procedures. This ensures that the techniques he has used 
can be traced in the event of damage. In addition, the parties should agree to the form 
in which the results should be presented (report, presentation, reports and analyses of 
the security tools used). 
� General duty of due care 
The penetration tester must exercise due care while performing testing procedures. For 
example, it would be grossly negligent if the pen etration tester were to “accidentally” 
attack the system of an un involved third party because he had confused a DNS name. 
The contract should therefore stipulate that the penetration tester must apply due care 
in the performance of his activity with respect to potential damage he may cause. 
4.3.9 Execution of the Contract 
A start and finish date should be specified for the contract. The penetration test must be carried out 
within this period of time. This ensures that penetration attempts which occur after this period can be 
clearly identified as real attacks by third parties, thus avoiding any misunderstandings. It should b e 
noted that the penetration tester is authorized to perform his tests in the agreed period of time only. 
4.3.10 Special Right to Terminate 
During the course of penetration testing, circumstances may arise which could hinder the progress of 
the tests (for example, a crucial system crashes and necessitates extensive manual tidying-up work). A 
- 34 - Federal Office for Information Security

<!-- page 35 -->

Study: A Penetration Testing Model 
special r ight to terminate can be included in the contract fo r c ases suc h as these. I n addi tion, th e 
general rules for terminating contracts for services apply, particularly Sec. 627 (2) BGB. 
4.3.11 Limitation of Liability 
When the parties are agreeing on limitations of liability, they should note that a limitation of liability 
can on ly be leg ally ag reed to  w ithin th e l imits of  th e G eneral Terms and C onditions o f Tra de Act 
(AGB-Gesetz). A limitation of the tester’s liability for gross negligence and intent and a disclaimer of 
liability for damages resulting from defects or indirect damage are normally possible as long as there 
is no culpable infringement of a significant contractual obligation. 
Federal Office for Information Security - 35 -

<!-- page 36 -->

Study: A Penetration Testing Model 
5 General Requirements 
In addition to the leg al fram ework, there are a number of general requirements pertaining to 
organization, personnel and technical matters for the performance of penetration tests. 
5.1 Organizational Requirements 
The fo llowing org anizational r equirements should be  cla rified with the cl ient in the run-up to a 
planned penetration test. 
� Who, apart from the client, will be affected either directly or indirectly by the penetration test? 
In addition to the client’s system, the sy stems of th e prov ider, wh ich m ay ev en be phy sically 
located on the client’s premises while being administered by the provider, are often affected by the 
penetration test. In order to avoid misunderstandings, the provider should therefore be notified of 
the planned penetration test. Some testing steps, e.g. DoS tes ts, can, due to their high bandwidth 
requirements or n on-standard da ta packages, also lead to disruptions to providers’ network 
components and should therefore be discussed in detail beforehand with the providers. 
If certai n fu nctions hav e bee n ou tsourced (e.g . webhosting the WW W server), the sy stems 
involved shou ld be excluded f rom the pen etration test. I f the se sy stems are i ncluded in the 
penetration test, written approval must for this be sought from the system operator or outsourcing 
operator. 
The tester must note that he is responsible for the security of IT systems, including outsourced 
systems, e.g. for the integrity of the accounting data, and that this responsibility cannot be simply 
transferred to the outsourcing service provider. 
� Have the liability risks received appropriate consideration? 
The pen etration tester sho uld have l iability ins urance w ith sufficient c over to insure himself 
against possible claims for damages of third parties. Although care should be taken to minimize 
potential risks for third party systems before testing, disruptions to third party systems cannot be 
completely ruled out. 
� What needs to be considered in respect of the time of testing? 
Penetration tests can impair the functionality of pr oduction systems. Since the aim of a test is to 
detect vulnerabilities, but without endangering orderly operations, the actual attacks should take 
place at a time agreed to by both p arties. This should be considered in the planning stage in the 
run-up to the penetration tests. Penetration tests often take place in a period of several days. Times 
should be chosen at which ne ither c rucial p rocessing is pe rformed nor h igh v olumes of onl ine 
- 36 - Federal Office for Information Security

<!-- page 37 -->

Study: A Penetration Testing Model 
orders, for instance, are processed on the target system. Consideration can be shown for the time at 
which the attacks are carried out in white-box tests only. With black-box approaches, information 
on the level of criticality and system utilization at certain times is not normally available. 
� What needs be done in the event of system failure or other emergency? 
In case the system fails de spite care be ing exer cised dur ing tes ting, or in c ase of a nother 
emergency, e.g. a serious disruption of the system, contingency measures will need to be defined. 
The contract must at least specify who to  not ify and w hen i n ca se o f a s uspected or i dentified 
failure or disruption. In addition, the kinds of faults that have to be reported should be defined. 
The following “disruptions” can be distinguished: 
o Complete system failure 
o Partial failure of certain subsystems 
o Incorrect responses from the system 
o Large increase in the length of the system’s response times 
o Countermeasures being taken in response to a covert penetration test 
o Attacks of third parties on the system 
� Which of the client’s employees are affected by the penetration test? 
The number of employees affected by testing will depend on the scope and nature of the test. A 
penetration test limited to a test system will only be able to affect the administrators and the users 
of the test system. As well as the system users, a test which also examines production systems can, 
in ex treme cases, also a ffect all em ployees w ho a re in some way reliant on the res ults of the 
systems being tested, or hinder them in their work. If social engineering techniques are to be used 
in the penetration te st, the part ies should ag ree on t he em ployees who m ay be targ eted du ring 
testing and the extent to which this is permissible. 
� How much time and cost will the penetration test involve for the client? 
The client must expect possible impairment to his IT systems as a result of the penetration test 
which m ay resul t in irregularities in op erations. I t is therefore nec essary to take steps before a 
penetration test in o rder t o k eep th e e ffects of potential di sruptions to a m inimum. T hese m ay 
include, for exam ple, a ssigning an em ployee to monitor th e pen etration te st from the cl ient’s 
perspective and w ho can halt testing i f ne cessary. The cl ient should als o consider making 
(additional) backups before a penetration test i s pe rformed. I t is als o ne cessary to adopt an 
contingency plan (if there is not one already) and escalation procedures which facilitate both an 
orderly course of action and the introduction of suitable coutermeasures. If the white-box approach 
Federal Office for Information Security - 37 -

<!-- page 38 -->

Study: A Penetration Testing Model 
is chosen for the penetration test, additional information and professional contact partners must be 
made available to the penetration tester. 
� How much time and effort will the penetration test require of the tester? 
In order to b e able to assess whether a service provider can adequately perform a penetration test 
and i f so, the approximate expe nse tha t this would inv olve, the time and effort requi red of the 
tester to perform the penetration test must f irst be  quan tified. T he fo llowing aspe cts should b e 
considered: 
o Objective and scope of the penetration test 
The te ster a nd t he c lient jointly def ine the n ature o f t he pe netration t est and the tes t 
procedures to be performed in line with the objective of the penetration test. Depending on 
the nature and scope of the penetration tests, it may be possible to determine the resources 
the penetration tester will need to use (hardware, software, suitable employees) before the 
actual start of testing. 
o The size of the infrastructure to be tested 
The size of the infrastructure is often expressed in the number of IP addresses that are to 
be tested. Generally, it is not possible to specify the time a tester will need to spend on the 
penetration t esting of a n ind ividual sy stem since this dep ends on t he m odel and the 
configuration of the system, the experience and dedication of the tester as well as on other 
factors. Another factor is whether the system to be te sted is located in a logical segment 
whose gateway to a public network is p rotected by a c entral firewall, or whether it is a 
divided infrastructure with several different gateways to public networks. As these factors 
are difficult to quantify, we can only derive the very general statement that the greater the 
number of systems and the larger the infrastructures to be tested, the more time and effort 
is required of the tester. 
o The complexity of the infrastructure to be tested 
The complexity of t he infrastructure to b e te sted i s a further im portant fa ctor t hat 
influences the time and effort the penetration tester has to expend. Typical services that 
are offered on the internet are the re trieval of websites (HTTP), downloads (FTP) and e­
mail communication. Vulnerabilities in applications that support these services are often 
known as such services a re v ery com mon; they  ar e publ ished at m any places on the 
internet. I f a com pany or publ ic authority lim its i tself to such widespread services, an 
infrastructure with a low level of complexity can be a ssumed. T he amount o f time and 
manpower involved in p erforming a pene tration test should therefore be relatively small. 
If complex e-commerce solutions or interactive applications are used in addition, it will 
- 38 - Federal Office for Information Security

<!-- page 39 -->

Study: A Penetration Testing Model 
take long er to locate vulnerabilities and a h igher deg ree of expe rtise may be needed to 
exploit them. This means that the penetration tester will need to allow for a longer period 
of time and more experienced personnel for performing the penetration test. 
5.2 Personnel Requirements 
Penetration tests must be tailored to the client’s individual situation and thus do not lend them selves 
well to standardization. Therefore, a penetration test can only follow a rigid pattern to a certain extent. 
As such, penetration tests should only be performed by persons with many years of ex perience in IT 
security. 
The following skills are necessary for an expert performance of penetration tests: 
� Knowledge of system administration/operating systems 
This k nowledge i s ne cessary fo r ev aluating w eaknesses in the oper ating systems of the target 
systems and also facilitates the handling of the systems used in the penetration test. 
� Knowledge of TCP/IP and, if applicable, other network protocols 
Since data traffic on the internet is handled by T CP/IP, which ha s also become the s tandard i n 
LANs, in- depth k nowledge of this pr otocol is essential. K nowledge of TCP/IP is c losely 
connected with knowledge of other networks and of the OSI reference model. 
� Knowledge of programming languages 
To b e in  a po sition to exploit v ulnerabilities in applications and systems, knowledge of a 
programming language is adv antageous. While there are a r ange of ready tools as scr ipts or with 
graphical user interfaces, security gaps such as bu ffer ov erflows et c. c an on ly be eff ectively 
exploited when the tester has the necessary programming knowledge. 
� Knowledge of IT security products such as firewalls, intrusion detection systems 
Since security ar rangements suc h as firewalls or intrusion de tection sy stems are  ex tremely 
common nowadays, the penetration tester should know how these security arrangements work and 
follow the latest reports on security g aps in I T se curity prod ucts. I t is e ssential to h ave an 
overview of th e common products on the market in the field of IT security (for firewalls see e.g. 
[BSI01]). 
� Knowledge of how to handle hacker tools and vulnerability scanners 
In addition to s ome basic k nowledge, expe rience in h andling hack er tools a nd v ulnerability 
scanners is necessary for performing penetration tests. Skills in the handling of these tools should 
be obtained through practical experience. Over the course of time, among the m ultitude of tools 
Federal Office for Information Security - 39 -

<!-- page 40 -->

Study: A Penetration Testing Model 
available, certain products have achieved a wide distribution (e.g. nmap for port scans, Lophtcrack 
for Windows passwords). Commercial tools can be used fo r pe rforming an eff icient t est and 
freeware tools can be employed to d emonstrate the relatively simple performance of such tests. 
The efficiency of the penetration test depends heavily on how experienced the penetration tester is 
in handling these tools. 
� Knowledge of applications/application systems 
Many v ulnerabilities a re loca ted in the appl ications rather th an the op erating sy stem softw are. 
They sp an th e en tire range of application systems, rang ing from insufficiently secured macro 
functions in word processing programs to vulnerabilities of internet browsers through scripting, to 
buffer overflow errors in large d atabase sy stems, as examples. T he t ester should t herefore b e 
familiar with as many types of applications as p ossible. Detailed knowledge of c ommonly used 
applications is p articularly im portant, since the risk of h ackers and crackers h ere is g enerally 
particularly high. 
� Creativity 
In addition to the high professional requirements, creativity is an important quality in a penetration 
tester. Since a qualified penetration test can on ly fol low a rigid p attern to  a l imited e xtent, th e 
question of how to p roceed a t a particular p oint wi ll undoubtedly ari se dur ing the course of a 
penetration t est w hen it at fi rst sig ht seem s impossible to further compromise a system. This 
problem can be ap proached by  clev erly com bining the information a tester has obtained, the 
vulnerabilities he h as identified and  th e to ols and m ethods av ailable t o him. By exercising his 
intelligence, a c reative pe netration t ester should t herefore b e be tter po sitioned to perform a 
“successful” t est th an a penetration tester who m erely re lies on the re sults of his tool s when 
performing the test. Creativity should, however, never lead to an unsystematic or even chaotic test 
which is not subsequently traceable. 
- 40 - Federal Office for Information Security

<!-- page 41 -->

Study: A Penetration Testing Model 
5.3 Technical Requirements 
The following technical requirements must be m et before the penetration tester can perform the test 
procedures: 
� Access to public networks 
Access to the internet or the public telephone network is an important precondition for performing 
the p enetration t est si nce m ost a ttacks are launched over the se communication channels. A 
sufficiently high-capacity internet connection should therefore be available. Here it is important to 
note that vulnerability scanners in particular require a high bandwidth. The efficiency of testing 
therefore depends for one thing on the available line capacity . 
� Availability of suitable auditing tools 
The penetration tester must have suitable tools at his disposal for performing the tests. Many of 
these tools can be downloaded from the i nternet f ree of c harge. T ools such  as v ulnerability 
scanners, however, often attract extremely high royalties (usually depending on the number of IP 
addresses to be s canned). An efficient test requires the “right” tools rather than large numbers of 
tools. The tester knows the effects and side-effects of the tools and is often able to assess a large 
number of results quickly and differentiate false statements from true ones. 
Federal Office for Information Security - 41 -

<!-- page 42 -->

Study: A Penetration Testing Model 
� Local test network 
The various tools must be tested in a local test network before use in a real penetration test. These 
kinds of tes ts als o allow the penetration tester to fam iliarize himself with hack er too ls and 
vulnerability scanners a nd wi th t he r esults they produc e. If the systems of the te st netwo rk are 
suitably configured, they also allow vulnerabilities in the systems to be tested and verified. 
5.4 Ethical Issues 
In addition to the conditions outlined above, there are also a number of ethical issues that need to be 
considered before starting penetration testing. The parties should, for one thing, clarify whether and to 
what ex tent the u se o f soc ial eng ineering tec hniques is justified. T hey sho uld also di scuss w hether 
vulnerabilities that have been identified as such in a penetration test need to or may be exploited. 
First, however, the parties should m ake quite clear that a p enetration test ca n ev er on ly be a 
commissioned activity. Any proactive behavior, i.e. launching an at tack attem pt wi thout a m andate 
should always be considered an attack and is to be rejected. 
5.4.1 The Use of Social Engineering Techniques 
The following gives an outline of why social engineering is so successful in order to decide whether 
the use of such techniques is justified in a pene tration test. The techniques work because all human 
beings pos sess ce rtain characteristics o r w eaknesses that c an be exploited. T hese include positive 
characteristics such as the tendency to be amiable, have a feeling of moral obligation and be helpful, as 
well as less positive qualities such as being opportunistic and unwilling to assume responsibility. 
Almost all employees would, for example, provide the “new boss” with confidential information at 
his/her re quest i f he  or she a cts se lf-confidently and a ppears g enuine. Pe ople do this ou t of a 
willingness to help on the one hand, and out of a sense of duty, but also, on the other hand, as a result 
of opportunistic considerations. These kinds of weaknesses can only be counteracted by providing all 
employees with regular training. One could, however, also contend that social engineering techniques 
are successful because of insufficient or inappropriate security measures. If, for e xample, passwords 
are issued automatically and a re so complicated that they are almost impossible to memorize, many 
users will make a note of them in “safe” places. Or they often forget their passwords and request new 
passwords, which is also a good starting point for social engineering. 
Since the use of social engineering techniques has a direct influence on the client’s employees in that 
they assess their reliability or security awareness, they could make those involved apprehensive. This 
could be all the more so when social engineering techniques are performed without prior warning and 
are subsequently explained. 
- 42 - Federal Office for Information Security

<!-- page 43 -->

Study: A Penetration Testing Model 
Even when the p enetration t est result repo rt does not inc lude any information or nam es, and no 
personal information on the improper conduct of certain employees is transmitted orally to the client, 
these techniques can still make employees feel insecure. 
These are the reasons why many security experts reject the use of social engineering in s ecurity tests 
or only deem them appropriate when security requirements are very high. [Kabay00] 
The use of social engineering therefore needs to be considered very carefully. The tester should always 
inform the client of the possible consequences of social engineering and state that this technique will 
most probably succeed if users are given no prior training and that this could have adverse affects on 
employees. 
5.4.2 Exploiting Vulnerabilities 
A vulnerability in an application or an operating system which can then be exploited to take over a 
system will normally be identified before the system is actually compromised. Here, the tester should 
consider whether this last step of exploiting the vulnerability needs to be carried out in order to verify 
it, or whether it is sufficient to merely point out the existence of the vulnerability. This question can 
only be resolved by keeping in mind the defined objective of the test and the conditions derived from 
this. If the penetration test is to be as realistic and informative as possible, it may be appropriate not to 
impose any limits on the ag gressiveness o f t esting proce dures. I f, on t he o ther hand,  a po tential 
disruption to operations is to be av oided as far as possible, vulnerabilities should not be actively 
exploited. I n this case, th e result of the penetration test would be the iden tification of existing 
vulnerabilities and no evidence of a successful penetration would be provided. 
Federal Office for Information Security - 43 -

<!-- page 44 -->

Study: A Penetration Testing Model 
6 A Penetration Testing Methodology 
This c hapter introduces a m ethodology for pene tration testing, div ided into five phases. This 
methodology takes account of the issues discussed above and was developed for general applicability. 
The methodology is ba sed on a structured procedure for performing penetration tests which acts as a 
basis for devising individual action plans for specific penetration tests. 
6.1 Requirements for a Penetration Testing Methodology 
The methodology describes and structures the performance of a commissioned penetration test. A test 
should always be receptive to th e c lient’s ob jectives and c are m ust be t aken not to n eglect th is 
perspective. This m eans, for  ex ample, ou tlining th e test steps required t o ach ieve t his ob jective or 
explaining whether a penetration test is suitable for achieving them at all. A methodology should also 
include measures for complying with the legal provisions (see e.g. [ISACA_CH99]) and for observing 
the conditions regarding organization and personnel for performing penetra tion t ests. It should t ake 
account of the limited time available and must include an assessment of the pot ential risk or a cost­
benefit analysis. 
A module-based approach such as the OSSTMM [Herzog02] is advisable for grouping individual test 
steps since this allows the steps inv olved i n a p enetration t est to be c ategorized th ematically. Thi s 
gives the te st a c lear f ramework and al so a llows th e t ester t o devise a sui table penetration tes t by 
selecting or excluding certain modules. 
For f inancial reasons, an a ctual p enetration t est wi ll no t normally make use of al l possible te st 
modules. While th is wou ld e nsure a fully com prehensive te st, it wo uld also be extremely tim e­
consuming and the reby be n either reconcilable with the client’s objectives nor with specific security 
requirements. When security requirements are par ticularly high, the test should be as comprehensive 
as possible. This means that all or most modules must be applied and all of the client’s systems must 
be included in the test. If security requirements are low, certain modules can be left out and /or only 
exposed or externally visible systems tested. Financial considerations should determine the scop e of 
the p enetration t est. The costs an d r isks of the testing act ivities m ust be  weig hed up against t he 
potential costs and risks which could be incurred in the event of an attack. 
6.2 The Five Phases of a Penetration Test 
The following introduces the five ph ases of a pen etration te st b ased on the c onsiderations ou tlined 
above. The individual phases take place successively: 
Phase 1: Preparation; it is d ifficult to  fu lfill the c lient’s expectations w ithout tho rough 
preparation, such as reaching an ag reement on the objectives of the penetration test. At the 
- 44 - Federal Office for Information Security

<!-- page 45 -->

Study: A Penetration Testing Model 
start of a penetration test the client’s objectives must be c larified with him and de fined. The 
performance of a p enetration test without taking full account of the relevant legal provisions 
could have consequences under criminal or civil law. The tester must therefore ensure that the 
test pr ocedures ar e no t g oing to infringe legal provisions or con tractual ag reements. The 
failure of a p roduction system could also lead to recourse demands as a result of pene tration 
techniques which have not b een ag reed t o or risks assoc iated with th e t echniques use d that 
were no t m ade k nown, which is why  the procedure and its risk s must be dis cussed and 
documented. 
All details agreed to should be put in writing in the contract. 
Phase 2: Reconnaissance; after the objectives, scope, procedures, emergency measures etc have 
been defined taking account of the legal and organizational aspects and other conditions, the 
tester can start gathering information on the target. This phase is the passive penetration test. 
The aim is to obtain a complete and detailed overview of the systems installed, including areas 
open to attack or known security shortcomings. Depending on the number of computers or the 
size of the netw ork to be examined, the tes t steps may be extremely time-consuming. If, for 
example, a class C network (256 possible IP addresses) behind a firewall has to be fully tested, 
a full port scan (all 65536 ports) may take several weeks depending on the setting. While these 
long test steps are usually performed automatically, the time required for them still needs to be 
taken into account in the planning. Thus a penetration test can take 20 days, for example, with 
the abovementioned test lasting several weeks. 
Phase 3: Analyzing information and risks; a successful, transparent and economically efficient 
procedure must analyze and assess the information gathered before the test steps for actively 
penetrating the system – which are often extremely time-consuming - can be performed. The 
analysis must include the defined goals of the penetration test, the potential risks to the system 
and the estimated time required for evaluating the potential security flaws for the subsequent 
active pene tration a ttempts. Th e targets in  pha se 4 a re then se lected on t he ba sis of t his 
analysis. From the list of identified systems the tester may, for ex ample, choose to test only 
those which contain known potential vulnerabilities due to their configuration or the identified 
applications/services or those about which the tester is particularly knowledgeable. 
In a penetration test for which the number of target systems has been clearly defined in phase 
2, this selection means that the number of target systems for phase 4 is automatically reduced. 
The restrictions must be comprehensively documented and justified since in addition to the 
desired improvement in efficiency, they also lead to a reduction in the informative value of the 
penetration test and the client needs to be made aware of this. 
Federal Office for Information Security - 45 -

<!-- page 46 -->

Study: A Penetration Testing Model 
Phase 4: Active in trusion a ttempts; finally, the  se lected systems are actively ass ailed. T his 
phase entails the highest risk within a penetration test and should be performed with due care. 
However, only this phase reveals the extent to which the supposed vulnerabilities identified in 
the reconnaissance phase present actual risks. This phase must be p erformed if a verification 
of potential vulnerabilities is required. F or sy stems w ith v ery hig h av ailability or int egrity 
requirements, the potential effects need to be carefully considered before performing critical 
test procedures, such as the utilization of buffer overflow exploits. 
In a white-box test, a patch may need to be installed on critical systems before performing the 
test to prevent system failure. The test will probably not b e able to locate any vulnerabilities, 
but will document the security of th e sy stem. U nlike a h acking att ack, how ever, the 
penetration test is not complete – it will be continued. 
Phase 5: Final analysis; as well as the individual test steps, the final report should contain an 
evaluation of the vulnerabilities located in the form of potential risks and recommendations for 
eliminating th e v ulnerabilities and r isks. T he re port must g uarantee the transparency of the 
tests and the vulnerabilities it disclosed. The findings and resultant risks for IT security should 
be discussed in detail with the client after the conclusion of the test procedures. 
- 46 - Federal Office for Information Security

<!-- page 47 -->

Study: A Penetration Testing Model 
6.3 Approach 
Figure 2 illustrates a five-phase approach to penetration testing. T he penetration test documentation 
should be compiled du ring phases  1 to  5 and not just as part of the final analysis i n phase 5. This 
ensures that th e t est st eps and results of  al l ph ases are documented and makes the penetration tes t 
transparent and traceable. 
Figure 2: Five-phase penetration testing procedure 
In spite of attempts to keep the methodology as g eneral as possible, situations may arise in practice 
which c all fo r dev iations from the p rocedure de tailed he re. All steps taken that deviate fr om the 
methodology detailed here should be documented and justified separately. 
Federal Office for Information Security - 47 -

<!-- page 48 -->

Study: A Penetration Testing Model 
6.4 Modules for the Test Procedures 
The approach described abov e doe s no t con tain ex plicit test p rocedures, i t m entions on ly the 
performance of I and E modules. Based on the OSSTMM [Herzog02], the different testing procedures 
which can be carried out in a penetration test have been grouped together in modules. The test objects 
are only accessed in phase 2 – “Reconaissance” and phase 4 – “A ctive intrusion”. The modules have 
been di vided into t wo cl asses a ccordingly, I modu les fo r r econnaissance a nd E m odules fo r 
penetration attempts. The modules have been d ivided up so that each of the steps belong to the same 
values o f pen etration testing clas sification criteria. The  pe rformance of p ort sc ans, for example, is 
divided into a module for covert port scans and a module for overt port scans, and the firewall testing 
is divided into modules for testing from the outside and from the inside. 
- 48 - Federal Office for Information Security

<!-- page 49 -->

Study: A Penetration Testing Model 
6.4.1 Reconnaissance Modules 
Table 1 contains a list of the reconnaissance modules I 1 to I  22. T he testing steps contained in the
modules ar e des cribed in Se ction 6.5.1 a nd th e equ ivalent OSS TMM m odules are l isted in the
appendix (A.6.1).
No. Module 
I 1 Analysis of Published Data 
I 2 Covert Queries of Basic Network Information 
I 3 Overt Queries of Basic Network Information 
I 4 Stealthy Port Scans 
I 5 Noisy Port Scans 
I 6 Application Identification 
I 7 System Identification 
I 8 Covert Router Identification 
I 9 Overt Router Identification 
I 10 Covert Firewall Identification 
I 11 Overt Firewall Identification 
I 12 Vulnerability Research 
I 13 Application Interface Identification 
I 14 Collecting Information for Social Engineering 
I 15 Collecting Information for Computer-Based Social Engineering 
I 16 Collecting Information for Personal Social Engineering 
I 17 Wireless Communications Testing (Scanning Only) 
I 18 Telephone System Testing (Identification) 
I 19 Voicemail System Testing (Identification) 
I 20 Fax System Testing (Identification) 
I 21 Analysis of Physical Environment 
I 22 Access Control Identification 
Table 1: List of reconnaissance modules 
Federal Office for Information Security - 49 -

<!-- page 50 -->

Study: A Penetration Testing Model 
6.4.2 Modules for Active Intrusion Attempts 
Table 2 is a list of the modules E 1 to E 23 for active intrusion attempts. The testing steps contained in 
the modules are described in 6.5.2 and the equivalent OSSTMM modules are l isted in the appendix 
(A.6.2). 
No. Module 
E 1 Covert Verification of Actual Vulnerabilities 
E 2 Overt Verification of Actual Vulnerabilities 
E 3 Overt Queries of Basic Network Information 
E 4 Covert Router Testing 
E 5 Overt Router Testing 
E 6 Test of Trust Relationships Between Systems 
E 7 Covert Firewall Test From Outside 
E 8 Overt Firewall Test From Outside 
E 9 Testing the Firewall From Both Sides 
E 10 IDS System Testing 
E 11 Intercepting Passwords 
E 12 Password Cracking 
E 13 Test of Susceptibility to Denial of Service Attacks 
E 14 Computer-Based Social Engineering 
E 15 Direct, Personal Social Engineering With Physical Access 
E 16 Indirect, Personal Social Engineering Without Physical Access 
E 17 Wireless Communications Testing 
E 18 Testing Administrative Access to the Telephone System 
E 19 Voicemail System Testing 
E 20 Testing Administrative Points of Access to the Fax System 
E 21 Modem Testing 
E 22 Active Test of Access Controls 
E 23 Test of Escalation Procedures 
Table 2: List of modules for active intrusion attempts 
- 50 - Federal Office for Information Security

<!-- page 51 -->

Study: A Penetration Testing Model 
6.4.3 Extendability 
If future developments demand new testing steps, the list of modules can be extended. All steps to be 
performed in a new m odule m ust be long to the s ame classification cr iteria otherwise, due to the 
exclusion principle, the module cannot be integrated into the methodology. 
6.4.4 Exclusion Principle 
The modules are selected according to a negative exclusion principle rather than a p ositive selection 
principle. Based on the selected classification, the m odules whi ch ca nnot be p erformed due to t he 
selected approach are excluded from the tests. If a module is not excluded, the test steps contained in it 
must be carried out, which helps to ensure a com prehensive pen etration te st. I f a m odule i s t o be 
excluded for other reasons, these reasons must be set out and documented. 
After the objectives of the penetration test have been defined, the appropriate test is selected using the 
classification system (see Section 3.4) and taking account of the legal and organizational aspects. The 
chosen classification t hen de termines v ia the exclusion principle which modules for reconnaissance 
and for active penetration cannot be performed. The classification system is shown again in Figure 3, 
stating the modules to be excluded for each of the criteria. 
The choice of information base – whi te-box or b lack-box – does no t di rectly affe ct t he choice o f 
modules. Howev er, in a whi te-box tes t, d epending on th e doc uments available, a num ber of tes t 
procedures can be discarded and replaced by “reading up”. 
Federal Office for Information Security - 51 -

<!-- page 52 -->

Study: A Penetration Testing Model 
Figure 3 : Exclusion of modules based on classification 
This procedure is illustrated below. If, for instance, the following penetration test is to be performed: 
Criterion Value Excluded I modules Excl. E modules 
1. Information base: black-box - -
2. Aggressiveness: cautious - E 13 
3. Scope: focused - -
4. Approach: covert I 3, 5, 9, 11 E 2, 5, 8, 10, 23 
5. Technique network-based I 14-22 E 14-23 
6. Starting point: from the outside - E 9, 23 
I m odules 3, 5, 9, 11, 13-22 are ex cluded, a s a re E m odules 2, 5, 6, 8-10, 14 -23. T he remaining 
modules must be performed in the penetration test. 
- 52 - Federal Office for Information Security

<!-- page 53 -->

Study: A Penetration Testing Model 
6.5 Module Descriptions 
6.5.1 Description of Reconnaissance Modules 
This section outlines the descriptions of the reconnaissance modules I 1 to I 22. Each module includes
a brief description, the expected results, the requirements, the testing steps to be performed, and the
associated risks.
I 1. Analysis of Published Data 
The tester tries to obtain as much information as possible about the target organization. In particular, 
he attempts to gather information about the company, its employees and the technology used. 
Expected results: Done 
� Company profile � 
� Profile of employees � 
� Survey of the technology used by the organization � 
� Survey of the organization’s partnerships and strategies � 
Requirements: 
None 
Test steps: Effort 
� Search for information on the organization’s homepage low 
� Research in public databases low 
� Research relevant information in news groups medium 
Risks: 
None 
Federal Office for Information Security - 53 -

<!-- page 54 -->

Study: A Penetration Testing Model 
I 2. Covert Queries of Basic Network Information 
Basic information about the network to be tested as a basis for a penetration test is obtained in 
stealthy or covert queries. 
Expected results: Done 
� Domain names � 
� IP address ranges � 
� Host names � 
� IP addresses � 
� Description of server functions � 
� ISP information � 
� Contact partners (admin-c) � 
Requirements: 
IP address/IP range or domain/server names 
Test steps: Effort 
� Query public databases (Whois, Ripe, Arin) low 
� Query name servers (caution is required as attempted zone transfer 
could be detected) 
medium 
� Examine information in e-mail headers low 
� Scan HTML information of the websites offered to find external links 
or comments 
medium 
� Scan news groups for postings by the target organization’s employees low 
� Scan the target organization’s job vacancies for information about the 
IT environment 
low 
Risks: 
None 
- 54 - Federal Office for Information Security

<!-- page 55 -->

Study: A Penetration Testing Model 
I 3. Overt Queries of Basic Network Information 
Basic information about the network to be tested is gathered as a basis for a penetration test. 
Expected results: Done 
� Domain names � 
� IP address ranges � 
� Host names � 
� IP addresses � 
� Description of server functions � 
� ISP information � 
� Contact partners (admin-c) � 
Requirements: 
IP address/IP range or domain/server names 
Test steps: Effort 
� Query public databases (Whois, Ripe, Arin) low 
� Query name servers, with a zone transfer attempt low 
� Ping scan of the IP range, neighboring IP addresses and common host 
names 
low 
� Examine information in e-mail headers low 
� Scan websites to find internal links or comments medium 
� Scan news groups for postings by the target organization’s employees low 
� Scan the target organization’s online/offline job vacancies for 
information about the IT environment 
low 
Risks: 
None 
Federal Office for Information Security - 55 -

<!-- page 56 -->

Study: A Penetration Testing Model 
I 4. Stealthy Port Scans 
A stealthy port scan is run on all identified devices in order to identify which services each device 
offers, with which operating system. 
Expected results: Done 
� Information on the services offered by the device � 
� Identification of the operating system � 
Requirements: 
Knowledge of basic network information 
Test steps: Effort 
� Perform a port scan that is impossible or difficult to detect, e.g. by 
setting suitable parameters when using port scanning tools or by 
making queries at long intervals. 
medium 
Risks: 
The port scan could be detected. 
I 5. Noisy Port Scans 
A port scan is run on all identified devices in order to identify which services each device offers, 
and with which operating system. 
Expected results: Done 
� Information on the services offered by the device � 
� Identification of the operating system � 
Requirements: 
Knowledge of basic network information 
Test steps: Effort 
� Perform a normal port scan. medium 
Risks: 
None 
- 56 - Federal Office for Information Security

<!-- page 57 -->

Study: A Penetration Testing Model 
I 6. Application Identification 
The tester attempts to identify applications and services that can be accessed over the internet. 
Expected results: Done 
� Identification of server services offered (e.g. HTTP, FTP, NNTP) � 
� Identification of applications offered (e.g. web mail, online banking, e­
commerce software) 
� 
Requirements: 
Results from a previous port scan. 
Test steps: Effort 
� Evaluate the results of the port scan medium 
� Identify publicly available internet applications, such as online 
banking 
low 
Risks: 
None 
I 7. System Identification 
The tester attempts to obtain information about the operating system, the patch level status and the 
system’s hardware. 
Expected results: Done 
� Information about the operating system � 
� Information about the patch level status � 
� Information about the hardware � 
Requirements: 
Knowledge of basic network information 
Test steps: Effort 
� Perform a port scan with system detection/IP packet analysis medium 
� Analyze banner information medium 
Risks: 
The systems could crash or their performance could be impaired. 
Federal Office for Information Security - 57 -

<!-- page 58 -->

Study: A Penetration Testing Model 
I 8. Covert Router Identification 
The tester attempts to identify the routers used by the target organization, their functionality within 
the network as well as the operating system used, the manufacturer and the router model by making 
stealthy or covert queries. 
Expected results: Done 
� IP addresses of the routers � 
� Function of the routers in the network � 
� Operating system, manufacturer and router model � 
Requirements: 
Knowledge of basic network information Results of the stealthy port scans and system identification 
Test steps: Effort 
� Trace routes cautiously with a “trace route” command medium 
� Analyze the routed IP packets medium 
Risks: 
The attempt to identify routers could be detected. 
I 9. Overt Router Identification 
The tester attempts to identify the routers used, their role within the network and the operating 
system of the routers used by the target organization. 
Expected results: Done 
� IP addresses of the routers � 
� Role of the routers in the network � 
� Operating systems of the routers � 
Requirements: 
Knowledge of basic network information. Results of the noisy port scans and system identification 
Test steps: Effort 
� Trace routes using a “trace route” command medium 
� Analyze the routed IP packets medium 
Risks: 
None 
- 58 - Federal Office for Information Security

<!-- page 59 -->

Study: A Penetration Testing Model 
I 10. Covert Firewall Identification 
The tester attempts to identify the firewalls: 
o type/form (packet filter, dual or single-homed, application gateway etc.) 
o model (manufacturer, version, configuration access, etc.) 
o configuration (open ports, open protocols, etc.) 
Expected results: Done 
� IP addresses and/or DNS names of the firewall components (firewall 
hosts, application gateway, etc.) 
� 
� Firewall operating systems � 
� IP addresses of other components of the firewall configuration 
(internal and external routers) 
� 
� Model and patch level of the firewall software � 
Requirements: 
Knowledge of basic network information, results of stealthy port scans 
Test steps: Effort 
� Banner lookup of the firewall components low 
� Direct port scan of the firewalls medium 
� Trace routes using a “trace route” command medium 
Risks: 
The attempt to identify the firewalls could be detected. 
Federal Office for Information Security - 59 -

<!-- page 60 -->

Study: A Penetration Testing Model 
I 11. Overt Firewall Identification 
The tester attempts to identify the firewalls: 
o type/form (package filter, dual or single-homed, application gateway, etc.) 
o model (manufacturer, version, configuration access, etc.) 
o configuration (open ports, open protocols, etc.) 
Expected results: Done 
� IP addresses and/or DNS names of the firewall components (firewall 
hosts, application gateway, etc.) 
� 
� Firewall operating systems � 
� IP addresses of other components of the firewall configuration 
(internal and external routers) 
� 
� Model and patch level of the firewall software � 
Requirements: 
Knowledge of basic network information, results of noisy port scans 
Test steps: Effort 
� Banner lookup of the firewall components low 
� Direct port scan of the firewalls medium 
� Trace routes using a “trace route” command medium 
Risks: 
None 
I 12. Vulnerability Research 
The obtained information (open ports, applications, operating systems) is analyzed for vulnerabilities, 
with a range of tools being used. 
Expected results: Done 
� Extended list of the patch levels of systems and applications � 
� List of potential vulnerabilities � 
Requirements: 
In-depth knowledge of open ports, services offered, applications and operating systems used. 
Test steps: Effort 
� Use state of the art vulnerability scanners (see A.7) medium 
� Query up-to-date vulnerability databases (see A.7) medium 
� Scan mailing lists/underground FTP archives, IRC servers and news 
groups on hacking/exploits 
high 
Risks: 
The use of vulnerability scanners can cause the devices being tested or the network components 
used to crash or have other adverse effects on them. 
- 60 - Federal Office for Information Security

<!-- page 61 -->

Study: A Penetration Testing Model 
I 13. Application Interface Identification 
The interfaces which have been identified and can be accessed on the internet, particularly those 
between self-developed systems, are examined for potential vulnerabilities. This can involve DMZ 
applications, which can access applications in the company network via an interface (e.g. accessing 
the system with online transactions) and applications within the company network. 
Expected results: Done 
� List of potential vulnerabilities the application interfaces (e.g. 
web servers, ERP system). 
� 
� Knowledge about any existing interfaces between the different 
applications. 
� 
Requirements: 
Information on the applications and systems used, the results of the port scans 
Test steps: Effort 
� Scan the services offered on the homepage, such as database queries, 
for potential vulnerabilities. 
high 
Risks: 
None 
I 14. Collecting Information for Social Engineering 
Obtaining information for social engineering, provided either knowingly or unknowingly by the 
organization. 
Expected results: Done 
� Identification of the relevant departments � 
� List of people who work in the relevant departments � 
� Names, job descriptions, e-mail addresses of potential target persons � 
� Organizational charts of the target organization showing the different 
hierarchical levels and management positions (heads of department, 
etc.) 
� 
� Form of e-mail addresses, internal mailing lists and typical senders of 
internal mailings 
� 
Requirements: 
Company name, name of the institution 
Test steps: Effort 
� Analyze information on the target organization’s website. low 
� Analyze information in the press or databases high 
� Search news groups for e-mail addresses of employees and 
applications of the target organization published in postings 
medium 
Risks: 
None 
Federal Office for Information Security - 61 -

<!-- page 62 -->

Study: A Penetration Testing Model 
I 15. Collecting Information for Computer-Based Social Engineering 
Obtaining information for computer-based social engineering, provided either knowingly or 
unknowingly by the organization. 
Expected results: Done 
� List of IT systems and IT applications used in the different 
departments 
� 
Requirements: 
Results of I 14: Information on departments/people/the organization, etc. 
Test steps: Effort 
� Analyze the target organization’s website for information on operating 
systems and applications 
low 
� Search the organization’s job vacancies for information about its IT 
systems 
high 
� Research support forums for postings by the target organization’s 
employees 
medium 
� Identify the e-mail programs of the target organization/employees on 
the basis of headers 
low 
Risks: 
None 
I 16. Collecting Information for Personal Social Engineering 
Obtaining information for personal social engineering, provided either knowingly or unknowingly by 
the organization. 
Expected results: Done 
� List of the service companies that work for the target organization � 
� List of the target organization’s major customers � 
� Information on the location of the different departments within the 
buildings 
� 
Requirements: 
Results of I 14: Information on departments/people/the organization, etc. 
Test steps: Effort 
� Analyze the contact information on the target organization’s website low 
� Analyze the contact or customer information in the press or databases medium 
� Observe the target organization’s building high 
� Identify service companies by making telephone inquiries medium 
Risks: 
None 
- 62 - Federal Office for Information Security

<!-- page 63 -->

Study: A Penetration Testing Model 
I 17. Wireless Communications Testing (Scanning Only) 
The tester checks whether a WLAN is operated. If the existence of a WLAN is verified, the key data 
is collected. 
Expected results: Done 
� Verification of the existence of a WLAN � 
� Identification of the model and the points of access to the WLAN � 
� Type of connection (authenticated or nonauthenticated) � 
� Geographic spread of the WLAN � 
� Examination of the use and type of encryption technology � 
Requirements: 
None 
Test steps: Effort 
� Attempt to connect to the WLAN medium 
� Intercept traffic on the WLAN high 
� War walking/war driving (to determine the spread of the WLAN) medium 
Risks: 
None 
I 18. Telephone System Testing (Identification) 
The tester attempts to identify the type of telephone system and how to access it. 
Expected results: Done 
� Identification of the telephone system � 
� Identification of the remote access points for maintenance purposes � 
Requirements: 
Number range 
Test steps: Effort 
� Place test calls to telephone numbers with the target organization’s 
number range 
medium 
� Analyze the signals of the telephone system very high 
� Search the product documentation of the telephone system for preset 
maintenance access numbers/standard passwords 
medium 
Risks: 
None 
Federal Office for Information Security - 63 -

<!-- page 64 -->

Study: A Penetration Testing Model 
I 19. Voicemail System Testing (Identification) 
The tester attempts to find out whether a mailbox system is being used. If the existence of a mailbox 
system can be verified, further information is collected. 
Expected results: Done 
� Verification of the existence of a mailbox system � 
� Verification of the possibility of accessing the mailbox from the public 
telephone network 
� 
� List of the accessible mailboxes identified � 
Requirements: 
None 
Test steps: Effort 
� Place test calls to telephone numbers with the target organization’s 
number range 
medium 
� Search the product documentation of the telephone system for details 
of the mailbox system 
medium 
Risks: 
None 
I 20. Fax System Testing (Identification) 
The tester attempts to find out which fax machines are used by the target organization and which 
systems control them 
Expected results: Done 
� List of the fax machines � 
� List of the systems that control the fax machines and their operating 
systems 
� 
Requirements: 
Telephone number range(s) 
Test steps: Effort 
� Place test calls to telephone numbers with the target organization’s 
number range 
medium 
� Use a war dialer with system identification components high 
� Search product documentation of the fax machines for external 
maintenance access points 
medium 
Risks: 
The attack could be detected. 
- 64 - Federal Office for Information Security

<!-- page 65 -->

Study: A Penetration Testing Model 
I 21. Analysis of Physical Environment 
The area surrounding the company premises is examined with regard to organizational processes and 
interfaces. 
Expected results: Done 
� Map of building/surrounding area � 
� List of visible rooms � 
� List of rooms which could be bugged (with electroacoustic or video 
devices) 
� 
� List of organizational processes (deliveries etc.) � 
Requirements: 
None 
Test steps: Effort 
� Observe company premises and the surrounding area medium 
� Observe procedures for delivery, cleaning, visitors, etc. high 
Risks: 
None 
I 22. Access Control Identification 
The access controls to the company premises and critical areas (e.g. computer center, server rooms) 
as well as the possibilities for circumventing these are identified. 
Expected results: Done 
� List of ways to gain access � 
� List of access controls in place � 
� Authentification procedure for members of the organization and guests � 
� Ways of circumventing the security measures � 
Requirements: 
Map of the building/site 
Test steps: Effort 
� Observe company premises and the surrounding area medium 
� Analyze access controls with a view to effectiveness and ways of 
circumventing them 
high 
Risks: 
None 
Federal Office for Information Security - 65 -

<!-- page 66 -->

Study: A Penetration Testing Model 
6.5.2 Description of Active Intrusion Modules 
This section describes the modules for active intrusion attempts, E 1 to E 23. Each module includes a 
brief description, t he ex pected results, the requirements, th e t esting st eps to be  pe rformed, and th e 
associated risks. 
E 1. Covert Verification of Actual Vulnerabilities 
The actual threat potential of the vulnerabilities identified is examined by attempting to exploit the 
vulnerability with the aim of compromising the system. 
Expected results: Done 
� Extended list of the patch levels of systems and applications � 
� List of actual vulnerabilities � 
� List of the potential vulnerabilities which were unable to be verified 
using stealth techniques 
� 
Requirements: 
Results of I 12: List of potential vulnerabilities 
Test steps: Effort 
� Use state-of-the-art vulnerability scanners (see A.7), but only perform 
scans which are difficult or impossible to detect. The number of scans 
performed from one IP address must be strictly limited or the time 
between scans varied, etc. 
medium 
� Manual verification of the remaining vulnerabilities, such as tests of 
buffer overflow exploits, etc. 
high to 
very high 
Risks: 
Systems could crash while exploiting vulnerabilities or their performance could be impaired. 
Attempts to exploit identified vulnerabilities could be detected. 
- 66 - Federal Office for Information Security

<!-- page 67 -->

Study: A Penetration Testing Model 
E 2. Overt Verification of Actual Vulnerabilities 
The actual threat potential of the vulnerabilities identified is examined by attempting to exploit the 
vulnerability with the aim of compromising the system. 
Expected results: Done 
� Extended list of the patch levels of systems and applications � 
� List of actual vulnerabilities � 
� List of the potential vulnerabilities which were unable to be verified 
using stealth techniques 
� 
Requirements: 
Results of I 12: List of potential vulnerabilities 
Test steps: Effort 
� Use state-of-the-art vulnerability scanners (see A.7) medium 
� Manual verification of the remaining vulnerabilities, such as tests of 
buffer overflow exploits, etc. 
high to 
very high 
Risks: 
Systems could crash while exploiting vulnerabilities or their performance could be impaired. 
E 3. Verification of Actual Vulnerabilities in Application Interfaces 
The actual threat potential of the vulnerabilities identified in communications (interfaces), e.g. while 
accessing a database via a web server, are examined by attempting to exploit the vulnerability with 
the aim of compromising the system. 
Expected results: Done 
� Extended list of the patch levels of systems and applications � 
� List of the actual vulnerability in the application interfaces � 
Requirements: 
Results of I 12 and I 13: Detailed system descriptions and a list of application interfaces 
Test steps: Effort 
� Use state of the art vulnerability scanners (see A.7) medium 
� Manual verification of the remaining vulnerabilities, such as tests of 
buffer overflow exploits, etc. 
high to 
very high 
Risks: 
Systems could crash while exploiting vulnerabilities or their performance could be impaired. 
Attempts to exploit identified vulnerabilities could be detected. 
Federal Office for Information Security - 67 -

<!-- page 68 -->

Study: A Penetration Testing Model 
E 4. Covert Router Testing 
The identified routers are examined for vulnerabilities and for ways in which they can manipulated. 
Expected results: Done 
� Information on router ACLs � 
� Information on router configuration � 
� Administrative access to routers � 
Requirements: 
Results of I 8: List containing detailed information on identified routers 
Test steps: Effort 
� Attempt to log into the router using standard passwords. Brute force 
attacks should not be attempted since these are easy to detect (e.g. by 
an IDS) and the test should be covert (stealth test). 
medium 
� Identify router ACLs using appropriate tools (firewalking). The tester 
should take care that the test is stretched over a long period of time in 
order to make it more difficult to identify the attack. 
high 
� Check the reaction of the router to fragmented and spoofed packets 
that can be created using a packet generator. The tester should take 
care that the test is stretched over a long period of time in order to 
make it more difficult to identify the attack. 
very high 
Risks: 
The attack could be detected. 
The performance of the router could be impaired. 
- 68 - Federal Office for Information Security

<!-- page 69 -->

Study: A Penetration Testing Model 
E 5. Overt Router Testing 
The identified routers are examined for vulnerabilities and for ways in which they can manipulated. 
Expected results: Done 
� Information on router ACLs � 
� Information on router configuration � 
� Administrative access to routers � 
Requirements: 
Results of I 9: List containing detailed information on identified routers 
Test steps: Effort 
� Attempt to log into the router using standard passwords and brute force 
attacks 
medium 
� Identify the router ACLs using appropriate tools (firewalking) very high 
� Check the reaction of the router to fragmented and spoofed packets 
that can be created using a packet generator 
very high 
Risks: 
The performance of the router could be impaired. 
E 6. Test of Trust Relationships Between Systems 
The tester attempts to obtain unauthorized access through trust relationships between systems, e.g. by 
exploiting trusted hosts during user authentication. 
Expected results: Done 
� List of trust relationships between systems � 
� Gleaning unauthorized information � 
� Unauthorized access to files or systems � 
Requirements: 
Results of I 6 and I 7: Descriptions of systems and applications 
Test steps: Effort 
� Analyze the information available in relation to potential dependencies 
and trust relationships between systems 
high 
� Attempt to obtain access using spoofing IP addresses or other 
authentication features 
very high 
Risks: 
The performance of the systems could be impaired. 
Federal Office for Information Security - 69 -

<!-- page 70 -->

Study: A Penetration Testing Model 
E 7. Covert Firewall Test From Outside 
The tester attempts to circumvent the firewall system, i.e. to create a network connection to the 
secured network segment from the outside. The tester can also attempt, for example, to gain control 
of the firewall system or exploit misconfigurations. 
Expected results: Done 
� List of firewall rules that can be inferred externally � 
� Verification of the identified firewalls vulnerabilities � 
� List of the systems that can be reached behind the firewall � 
Requirements: 
Results of I 9: Information on the firewall components used 
Test steps: Effort 
� Identify firewall rules using appropriate tools (firewalking) high 
� Try to reach systems behind the firewall very high 
� Check the reaction of the firewall to fragmented and spoofed packets 
that can be created using a packet generator 
very high 
Risks: 
The performance of the firewall system could be impaired. 
The attack on the firewall could be detected by the firewall’s log function, for example. 
E 8. Overt Firewall Test From Outside 
The tester attempts to circumvent the firewall system, i.e. to create a network connection from the 
outside to the protected network segment. The tester can attempt, for example, to gain control of the 
firewall system or exploit misconfigurations. 
Expected results: Done 
� List of firewall rules that can be inferred externally � 
� Verification of the identified firewalls vulnerabilities � 
� List of the systems that can be reached behind the firewall � 
Requirements: 
Results of I 10: Information on the firewall components used 
Test steps: Effort 
� Run a vulnerability scanner on the firewall system hosts (firewall host, 
external router, internal router) 
medium 
� Identify firewall rules using appropriate tools (firewalking) high 
� Try to reach systems behind the firewall very high 
� Check the reaction of the firewall to fragmented and spoofed packets 
that can be created using a packet generator 
very high 
Risks: 
The performance of the firewall system could be impaired. 
- 70 - Federal Office for Information Security

<!-- page 71 -->

Study: A Penetration Testing Model 
E 9. Testing the Firewall From Both Sides 
Examination of the firewall by simultaneously testing both sides of the firewall. An externally placed 
system sends packets, an internally placed system analyzes the packets that arrive, and vice versa. 
Expected results: Done 
� List of firewall rules � 
� Verification of the identified vulnerabilities of the type of firewall in 
use 
� 
� Exhaustive list of the systems that can be reached behind the firewall � 
Requirements: 
Results of I 10: Information on the firewall components used and network access to a point behind 
the firewall. 
Test steps: Effort 
� Test whether (possibly using tunneled protocols) unauthorized 
connections from the internal network to the internet can be created 
high 
� Run a vulnerability scanner on the firewall system hosts (firewall host, 
external router, internal router) from inside 
medium 
� Identify firewall rules using appropriate tools (firewalking from both 
sides) 
high 
� Check the reaction of the firewall to fragmented and spoofed packets 
that can be created using a packet generator 
very high 
Risks: 
The performance of the firewall system could be impaired. 
Federal Office for Information Security - 71 -

<!-- page 72 -->

Study: A Penetration Testing Model 
E 10. IDS System Testing 
This is a test of whether an existing IDS registers the potential attacks and sounds the alarm. 
Expected results: Done 
� IDS model � 
� Reaction of the IDS to different types of attack � 
� Statement on the performance of the IDS � 
Requirements: 
Detailed information about systems and f irewalls. Facility for m onitoring whether the IDS system 
sounds the alarm. 
Test steps: Effort 
� Stage attacks that gradually become louder on the network of the target 
organization 
low to 
very high 
� Evaluate the reaction of the IDS to the attacks very high 
� Compare attack and IDS log files high 
Risks: 
These test steps can impair the performance of the target organization’s network. 
E 11. Intercepting Passwords 
The tester attempts to intercept passwords by using interception tools (network sniffers, backdoors, 
etc.). 
Expected results: Done 
� Passwords in plain language � 
Requirements: 
Appropriate sy stem rig hts ar e ne eded to install interception tools. T hese can be ob tained over a 
previously identified vulnerability. Data protection legislation must be observed. 
Test steps: Effort 
� Obtain rights for installing interception tools on appropriate systems very high 
� Install interception tools on appropriate systems high 
� Record and analyze network traffic on transferred passwords high 
Risks: 
The necessary installation of interception tools on appropriate systems can impair the performance 
of these systems. 
The necessary installation of interception tools on appropriate systems could make these systems 
accessible to non-authorized third persons. 
- 72 - Federal Office for Information Security

<!-- page 73 -->

Study: A Penetration Testing Model 
E 12. Password Cracking 
The tester uses different methods to attempt to find a password which allows privileged access to a 
system/application. 
Expected results: Done 
� Passwords in plain language � 
Requirements: 
Password f iles t hat con tain th e en crypted pas swords m ust be available for per forming offline 
attacks, e.g. from E 11 or provided by the c lient. It must be possible to connect to the pro tected 
systems to perform online attacks. 
Test steps: Effort 
� Check the password files using appropriate tools (offline) medium 
to very 
high 
� Carry out online attacks if no password file is available for an offline 
attack 
high 
� Manual test of standard passwords or frequently used passwords medium 
Risks: 
User accounts could be locked if a maximum number of incorrect password entries has been defined 
in the application/operating system being tested. 
E 13. Test of Susceptibility to Denial of Service Attacks 
The tester examines the extent to which the system is susceptible to a denial of service attack. 
Expected results: Done 
� List of systems that are prone to DoS attacks � 
Requirements: 
Systems susceptible to DoS attacks (web servers, mail servers, etc.) must be available. 
Test steps: Effort 
� Analyze the results of module I 12 Vulnerability Research medium 
� Carry out a DoS attack using various techniques medium 
to very 
high 
Risks: 
Even when the test reveals that the affected system is not susceptible to a DoS attack, a large-scale 
distributed DoS attack (DdoS), which would hardly be feasible for a tester, could still be successful. 
The performance of the tested system or involved network components could be impaired or may 
crash. 
Federal Office for Information Security - 73 -

<!-- page 74 -->

Study: A Penetration Testing Model 
E 14. Computer-Based Social Engineering 
The tester attempts to influence a person in order to obtain system rights by using appropriate 
computer-based manipulation techniques, e.g. by exploiting curiosity or helpfulness. 
Expected results: Done 
� Access to the organization’s network or systems � 
� List of system and application passwords � 
Requirements: 
Results of I 6, I 7, I 13 – I 16: Information on target systems, applications and people 
Test steps: Effort 
� Contact the target person by e-mail medium 
� Trick target persons into installing special programs (e.g. keyloggers). medium 
to high 
� Ask target persons to enter user names and passwords using falsified 
system messages 
medium 
to high 
Risks: 
The attack could be recognized and cause the target person to worry. 
The special programs could disrupt operations. 
E 15. Direct, Personal Social Engineering With Physical Access 
The tester attempts to elicit confidential information by making direct contact with a person who has 
access to privileged information (e.g. by visiting him/her). The tester attempts to persuade the target 
person to reveal information by feigning a relationship of trust. The target person can be an employee 
of the organization or another insider. 
Expected results: Done 
� Relevant information such as passwords, system configurations, etc. � 
Requirements: 
Results of I 7, I 14 – I 16: Information on target systems, applications and people 
Test steps: Effort 
� Make personal contact with the target person (e.g. pretending to be a 
service technician or new employee etc.) 
medium 
� Feign a relationship of trust to persuade the target person to surrender 
information (e.g. surrender a key or disclose passwords) 
high 
Risks: 
The attack could be recognized and cause the target person to worry. 
If the target person does surrender relevant information, this fact could impinge on the relationship 
between the target person and target organization once the penetration test is concluded and the 
person becomes aware of his/her misconduct, particularly when the said person is an employee of 
the target organization. 
- 74 - Federal Office for Information Security

<!-- page 75 -->

Study: A Penetration Testing Model 
E 16. Indirect, Personal Social Engineering Without Physical Access 
The tester attempts to find out secrets by contacting a person who is privy to privileged information 
by telephone. The tester attempts to persuade the target person to reveal information by feigning a 
relationship of trust. The target person can be an employee of the organization or another insider. The 
employee’s naivety and his/her need to be involved and willingness to help is exploited. 
Expected results: Done 
� Relevant information such as passwords, system configurations, etc. � 
Requirements: 
Results of I7, I14 - I16: Information on target systems, applications and people 
Test steps: Effort 
� Contact the target person by telephone or e-mail medium 
� Feign a relationship of trust to persuade the target person to surrender 
information (e.g. pretending to be an administrator, employee or 
distant superior, etc.) 
high 
Risks: 
The attack could be recognized and cause the target person to worry. 
If the person does surrender relevant information, this fact could impinge on the relationship 
between target person and target organization after the penetration test has been concluded and the 
said person is made aware of his/her misconduct (especially if he/she is an employee of the target 
organization). 
E 17. Wireless Communications Testing 
The tester attempts to obtain access to an existing WLAN. 
Expected results: Done 
� List of the vulnerabilities of the WLAN � 
Requirements: 
Results of I 17: Information on an installed WLAN 
Test steps: Effort 
� Analyze the results of module I 17 Wireless Communications 
Testing (Scanning Only) 
medium 
� Exploit potential vulnerabilities very high 
� Attempt to connect to a WLAN medium 
� Attempt to obtain access to the WLAN high 
� Attempt to obtain access to data in the WLAN very high 
Risks: 
The penetration test could impair the performance of the WLAN. 
Federal Office for Information Security - 75 -

<!-- page 76 -->

Study: A Penetration Testing Model 
E 18. Testing Administrative Access to the Telephone System 
The tester attempts to obtain administrative access to the telephone system. External maintenance 
points of access not protected by a static call-back procedure and preset standard passwords and 
PINs, in particular, pose a high risk. 
Expected results: Done 
� Administrative access to the telephone system � 
Requirements: 
Results of I 18: Information on the telephone system 
Test steps: Effort 
� Analyze the results of module I 18 Telephone System Testing 
(Identification) 
high 
� Attempt to obtain administrative access to the telephone system very high 
Risks: 
The test steps could impair the performance of the telephone system. 
E 19. Voicemail System Testing 
The tester attempts to circumvent the security functions of the mailbox system and gain access to 
mailboxes. 
Expected results: Done 
� Access to some mailboxes � 
Requirements: 
Results of I 19: Information about the voice mail system 
Test steps: Effort 
� Analyze the results of module I 19 Voicemail System Testing 
(Identification) 
medium 
� Test whether access can be gained using preset passwords/codes medium 
� Carry out other technical tests that require specialist knowledge of the 
telephone system model in use 
very high 
Risks: 
The basic rights of affected mailbox owners could be impaired (privacy protection). 
- 76 - Federal Office for Information Security

<!-- page 77 -->

Study: A Penetration Testing Model 
E 20. Testing Administrative Points of Access to the Fax System 
The tester attempts to circumvent the security functions of the fax system and obtain administrative 
access to the fax system. 
Expected results: Done 
� Administrative access to fax system � 
� Verification of vulnerabilities � 
Requirements: 
Results of I 20: Information on the fax system 
Test steps: Effort 
� Analyze the results of module I 20 Fax System Testing 
(Identification) 
medium 
� Carry out other technical tests that require specialist knowledge of the 
fax system in use 
very high 
Risks: 
The test steps could impair the performance of the fax system. 
E 21. Modem Testing 
The tester attempts to obtain access to the network of the target organization using non-secure 
modems to circumvent the firewall. 
Expected results: Done 
� List of “wild” modems � 
� List of the successful penetration attempts � 
Requirements: 
Telephone number ranges or list of modem telephone numbers 
Test steps: Effort 
� Use a war dialer (with system detection components) on the target 
organization’s number range 
high 
� Attempt to penetrate the network via the identified modem connections very high 
Risks: 
None 
Federal Office for Information Security - 77 -

<!-- page 78 -->

Study: A Penetration Testing Model 
E 22. Active Test of Access Controls 
The tester attempts to overcome access control mechanisms in order to obtain physical access to the 
buildings and rooms of the target organization. 
Expected results: Done 
� Obtaining access to protected areas � 
Requirements: 
Results of I 22: Information on access controls 
Test steps: Effort 
� Analyze the results of module I 22 Access Control Identification medium 
� Test whether access to the site/building of the target organization is 
granted 
medium 
� Test whether it is possible to enter the site/building of the target 
organization unnoticed 
medium 
� Carry out additional tests of whether access can be obtained to the 
server systems or desktop computers 
high 
Risks: 
If discovered, the attempt to gain access could make employees feel worried and/or call the police. 
E 23. Test of Escalation Procedures 
The tester checks to extent to which escalation procedures are complied with in the event of an attack 
and how effective the procedures are. 
Expected results: Done 
� Assessment of the proper functioning of the established escalation 
procedures in practice 
� 
Requirements: 
Means of monitoring the reactions of the client’s employees to the attempted attacks 
Test steps: Effort 
� Progressively “louder” types of attacks are performed on the network 
of the target organization in order to activate escalation procedures 
low to 
very high 
� The reports of the attacks performed are compared with the 
countermeasures introduced.The appropriateness of the 
countermeasures is assessed. 
medium 
Risks: 
These test steps can impair the performance of the target organization’s network. 
- 78 - Federal Office for Information Security

<!-- page 79 -->

Study: A Penetration Testing Model 
6.6 Penetration Test Documentation 
The scope and content of the documentation the tester delivers to the cl ient at the end of testing must 
be set out in the contract. The following may be included in a complete set of documents: 
� the contract, including the results and agreements negotiated in the preparatory talks (see 4.3), 
�	 documentation of the test steps completed for reconnaissance, e.g. using form A.6.1, the l og files 
of the tools used, including the list of vulnerabilities tested, 
� the system descriptions derived from these (see form A.6.3), 
� a list of potential vulnerabilities, broken down according to system with a brief description, 
�	 the results of the risk analysis (time/cost and priorities) and the systems or E modules selected on 
this basis for phase 4 (active intrusion attempts), 
�	 documentation of the modules completed for active intrusion attempts, e.g. using form A.6.2 and 
the log files of the tools used, 
� the individual results of the E modules including the list of verified vulnerabilities, and 
� a final report. 
If high demands are placed on the transparency of the penetration tests, further documentation may be 
required. Here, keyboard and mouse recorders as well as monitor or terminal logging utilities and/or 
network monitors/sniffers may be used. 
The ind ividual pa rts of the docum entation m ay contain h ighly sens itive in formation, su ch as 
passwords or open vulnerabilities. The entire documentation must therefore be tr eated confidentially. 
Moreover, th e parties must agree t o who f rom the c lient’s organization receives whi ch parts of the 
documentation. Certain parts, e.g. personal data, should be delivered to the the dat a protection officer 
only, and not to the IT department. 
Federal Office for Information Security - 79 -

<!-- page 80 -->

Study: A Penetration Testing Model 
7 Performing Penetration Tests 
This chapter describes, with examples, how penetration tests are conducted applying the methodology 
presented above. The steps contained in phases 1 to 5 are explained in detail, with potential problems 
being highlighted. This chapter also describes what documentation has to be prepared at which stage. 
7.1 Preparation 
Figure 4 : Phase 1 – preparing the penetration test: 
The preparation phase starts with defining the goal or goals of the penetration test. The tester and the 
client should jointly define goals so that both parties share the same understanding of the objectives. 
Possible g oals o f pen etration testing are to im prove the security of the te chnical systems, have IT 
security confirmed by an external third party, and increase the security of the organizational/personnel 
infrastructure (cf. Section 3.2). 
In accordanc e w ith th ese objectives, t he legalities o f t he pe netration t est (cf. Se ction 5.3) a nd the 
organizational, personnel and technical requirements (cf. Sections 4.2, 5.1 an d 5.2) w ill h ave to be 
observed and discussed by client and tester. 
With the aid of the classification (cf. Section 3.4), an appropriate test is then selected using the six 
criteria of information base, aggressiveness, scope, approach, technique and starting point. 
If a penetr ation test i s be ing car ried ou t fo r the first time the t est shou ld ideally cov er al l ex isting 
systems as vulnerabilities could remain in the systems that are not investigated. 
The amount of time to be spent on testing should ideally be estimated on the basis of the results of a 
prior assessment of p rotection requirements, applying, for example the methodology of th e Baseline 
Protection Manual (“Grundschutzhandbuch”). [BSI02] 
On the b asis of  th e cho sen c lassification, th e t ester sel ects the reco nnaissance and active intrusion 
attempt modules to be conducted by excluding the modules that can be left out (cf. 6.4.1). 
The risks for the client vary depending on the modules selected, and can rang e, for example, from 
postponing maintenance wo rk (low risk) to the p ermanent failure of an IT sy stem (hig h risk ). T he 
client and tester must discuss the likelihood that such risks will occur and their potential effects. As a 
- 80 - Federal Office for Information Security

<!-- page 81 -->

Study: A Penetration Testing Model 
result of the discussion the parties s hould de fine th e nec essary con tingency m easures fo r th e r isks 
which both parties are willing to take. When defining the con tingency measures, the parties should 
consider the time frame within which critical tests can be carried out and who will be responsible for 
the necessary measures. If the c hoice of modules involves unacceptable risks, a different penetration 
test will have to b e chosen, e.g. a les s aggressive approach for ac tive intrusion attempts, abandoning 
social engineering te chniques, or a r educed sc ope o f t he sy stems to be tes ted. If need be, the 
organizational and legal framework will have to be considered or discussed again at this stage. 
All the results of the preparation phase should be recorded in writing in a report and signed by both 
parties. The client can use this report to monitor the penetration tests, for example, and it can serve as 
a guideline for the tester. 
In addition, the extent of the documentation to be delivered after completion of the penetration test 
should be defined in the contract. The purpose of the documentation should be to allow the penetration 
testing process to be traced. A n ote on techniques for documenting penetration tests can be found in 
Section 6.6 , Appendix A.5.1 contains appropriate documentation forms. 
The preparation phase must culminate in a detailed plan stating precisely when which components are 
penetrated with which level of intensity. Escalation stages also need to be defined, i.e. contingency 
measures have to be devised for sen sitive sy stems, such as data ba ckups, al ternative sy stems and 
which service providers will need to be available. 
The test times should be defined roughly, at least for business-critical systems, to avoid disrupting the 
client’s operations, for instance. Another decision which may need to be m ade is which members of 
the functional departments will have to be informed about the test. 
Classifying data helps to define the intensity and approach for the tests (production servers are tested 
differently to test servers). If, for e xample, a c luster has to be tested, the parties will have to decide 
whether an audit would not be better for identifying vulnerabilities. In the cas e of self-developments, 
the support employees concerned should be involved in deciding which precautions are necessary and 
feasible. 
Finally, before the test is launched it should be clear how the results of the penetration test will be 
treated. A pos itive and c onstructive approach is helpful if the recommendations are to be translated 
into action to improve IT security infrastructure. 
Federal Office for Information Security - 81 -

<!-- page 82 -->

Study: A Penetration Testing Model 
7.2 Reconnaissance
Figure 5 : Phase 2 – reconnaissance 
Phase 2: Reconnaissance starts with an analysis of the preliminary information. In a black-box test, the 
preliminary in formation m ay be no m ore than an I P addre ss o r I P address blo ck. If detailed 
information h as b een m ade av ailable in a wh ite-box te st (su ch as ope rating system versions, 
applications used, etc.), the tester should start by analyzing this information and, if need be, request 
more information, such as system descriptions, network plans, etc. from the client to ensu re that the 
test is carried out as efficiently as possible. 
In the next step, the test procedures of the selected I modules are conducted. The tester is more or less 
free to choose t he o rder in wh ich th e m odules are com pleted. Only module I 12: “Vulnerability 
Research” has to b e ca rried o ut after the pre ceding I modules becau se it u ses the res ults of thos e 
modules, for example the list of available systems and pr ogram versions. The information gleaned is 
used in I  12 to id entify th e v ulnerabilities in the sy stems and app lications, w ith publ ic and  pr ivate 
databases being queried for known weak points and security loopholes. This procedure is illustrated by 
the following example: 
The tester has identified a server in the client’s DMZ, a potential target for the penetration test, as an e­
mail serv er and ha s f ound ou t the v ersion o f the e-mail server sof tware and the se rver’s oper ating 
system using  a banne r l ookup. Wi th this i nformation, the tes ter looks for pot ential vulnerabilities 
associated w ith this c ombination i n da tabases, mailing lists an d new sgroups, e tc. Vulnerability 
scanners can carry out some of these testing steps automatically, however, with unusual combinations 
they often come up against limiting factors and fail to report or overlook existing vulnerabilities. They 
are therefore no substitute for a manual search, but they can supplement and accelerate the process. 
At the end o f t he r econnaissance p hase th e t ester w ill hav e th e l og fil es o f th e I modules t hat are 
generated by vulnerability scanners, for instance, a description of the systems, and a list of potential 
vulnerabilities, all of which should be included in the penetration test documentation. 
- 82 - Federal Office for Information Security

<!-- page 83 -->

Study: A Penetration Testing Model 
7.3 Analysis of Information / Risks
Figure 6 : Phase 3 – analysis of information and risks 
The first step should be to assess the risks involved. Given the wealth of inf ormation that is usually 
obtained, it is im portant to an alyze and ev aluate th is information before g oing any  fu rther. T he 
evaluation has to include the defined goals, potential threats to the systems and the estimated cost of 
evaluating secu rity flaw s. V ulnerabilities c an be assessed ob jectively and the risk poten tial can b e 
established using the SANS Security Alert Consensus (SANS-SAC), for example, which is updated on 
a w eekly basis. The ev aluation w ill a lways be su bjective beca use the te ster’s experience and 
specialization, for instance, play a major role in estimating time and cost. 
Once the threat has been assessed, the tester should estimate the individual cost of a successful attack 
that exploits the potential vulnerabilities and weigh it up against its chances of success. A rough time 
schedule for the testing steps can be derived from the t imes stated in the module descriptions (time 
required: medium, high, very high). Priorities should then be defined on the basis of this comparison. 
The g reater the lik elihood of succ ess and the low er the time/cost required, the hig her the priority 
should be. The tester should document both the time/cost estimate and the priorities he sets. 
Based on the tester’s priorities, the targets and testing steps for the next stage, phase 4, can be chosen. 
The next testing steps should focus primarily on the IT systems which, after the evaluation of potential 
vulnerabilities, have been assessed as being high to medium priority, and on those test procedures that 
are m ost l ikely to b e suc cessful. Fo r th is, the se lected E m odules are lim ited fu rther (cf. 6.5.2). A 
written shortlist of systems and modules should be attached to the penetration test documentation and 
be discussed with the client prior to any active intrusion attempts. 
7.4 Active Intrusion Attempts 
Figure 7 : Phase 4 – carry out active intrusion attempts 
Federal Office for Information Security - 83 -

<!-- page 84 -->

Study: A Penetration Testing Model 
Once th e r elevant E m odules h ave been selected a nd prio ritized, in t his st age the I T systems are 
actively assailed. The tester systematically works through the attack attempts in order of their priority, 
the highest priority first. 
The client’s targets for penetration testing are usually particularly business-critical systems, so special 
care is called for i n ca rrying out intrusion attempts. T he contingency m easures m entioned in the 
preparation phase are absolutely essential i n th is stage. T hey dem and, fo r ex ample, th at intrusion 
attempts (on business-critical systems) be made outside working hours (i.e. at night or weekends) and 
that the responsible system administrators be present. 
The process is illustrated below taking module E 3 “Verification of actual vulnerabilities in application 
interfaces” as an example. 
In the reconn aissance ph ase a sp ecific se rver op erating sy stem w ith a w eb s erver appl ication was 
identified on a system that is used for online transactions and which accesses the com pany’s internal 
ERP system. The vulnerability search rev ealed a buf fer ov erflow v ulnerability fo r th e und erlying 
database in the ERP system. However, the firewall prevents direct access to the database. The tester 
now faces the challenge of finding out whe ther an o nline transaction that penetrates the firewall to 
exploit the vulnerability in the database system can be triggered by manipulating an HTTP link. 
Not until active penetration attempts are c arried ou t does  i t be come clea r whe ther th e po tential 
vulnerabilities id entified in t he reconnaissance phas e c an ac tually be exploited so that the se lected 
system can be pen etrated, for example. If the client asks for the potential vulnerabilities to be listed 
and also tested, both tester and client should carefully weigh up the possible consequences (e.g. system 
downtime). 
The documentation should detail both positive, i.e. successful active intrusion attempts, and negative 
results, i.e. unsuccessful penetration attempts. 
7.5 Final Analysis / Clean-Up 
Figure 8 : Phase 5 – final analysis and clean-up 
In this fi nal phase the results of each of the E m odules that were carried out are compiled in a final 
report. The final report should comprise a management summary describing the test engagement, key 
test results, and recommended action on an abstract level and is designed for top management. The 
main sect ion o f t he f inal report should con tain the d etailed po sitive an d neg ative test  f indings, as 
agreed. For the vulnerabilities, the re sults are ev aluated and prioritized, and the tester describes the 
- 84 - Federal Office for Information Security

<!-- page 85 -->

Study: A Penetration Testing Model 
ensuing risks so that the client knows which risks are relevant to his business operations. In addition, 
the report should contain recommendations on how the client can eliminate the vulnerabilities existing 
at the time of t he penetration test. The final report should also include an action plan for eliminating 
vulnerabilities, based on the priorities assigned to the results and drawn up together with the client. 
The action plan should contain a schedule for each critical vulnerability and name a person and/or area 
that is responsible for its elimination. 
The sensitive personal data obtained during penetration testing (cf. Section 6.6 ), such as passwords or 
private e-mails should not be included in the fin al report for data protection reasons; they should be 
handed over to a designated person, e.g. the data protection offer. However, the client must be able to 
trace the test results clearly, and a ll information gathered in the various phases must be included, at 
least as an appendix to the working papers. This includes, for instance, det ailed information on the 
tools used, work steps (which tool was used with which options), log files, work times (when were 
attacks carried out), etc. 
The tester has to remove any software, such as keyloggers, that may have been installed in the client’s 
IT sy stem in the cou rse of the penetration test o r any  oth er m odifications m ade to the cl ient’s IT 
systems, and restore the system to the state in which the tester found it prior to testing. 
Federal Office for Information Security - 85 -

<!-- page 86 -->

Study: A Penetration Testing Model 
Glossary
Term Explanation 
Back door A com puter pr ogram that es tablishes undocumented or secret acce ss to 
the computer via the network. 
Black-box test A penetration test in which the tester has no prior information about the 
network he/she is testing. 
Browser A program for presenting websites on the internet or intranet. 
CERT Computer Em ergency Response Team; a g roup of IT specialists who 
ward off attacks on IT systems. 
CGI Common Gateway Interface; program for processing data on a web server 
that has been transferred from a � browser. 
Cracker A person  who ob tains un authorized acc ess to o r m anipulates o ther I T 
systems, often with unlawful intentions. 
DDoS Distributed � Denial-of-Service; a DoS attack in which the target system 
is attacked by means of s imultaneous attacks on a n umber of distributed 
systems. 
Denial-of-Service (DoS) A cracker’s attacking method in wh ich he tries to impair the av ailability 
of an IT system by overloading it. 
DMZ De-Militarized Zone; a de coupled, isolated partial n etwork loca ted 
logically betw een an  in secure n etwork an d a ne twork that has to be 
protected and normally contains servers or services such as web servers 
and e-mail servers that can be accessed externally. 
DNS � Domain Name System 
Domain Name System A mechanism for turning computer names into � IP addresses. 
DoS � Denial-of-Service 
Escalation procedures Instructions on how to respond to a hacker attack. 
Filter rules Information for controlling a � firewall. 
Firewall Protection m easure be tween tw o c omputers w hen on e has a higher 
- 86 - Federal Office for Information Security

<!-- page 87 -->

Study: A Penetration Testing Model 
Term Explanation 
protection requirement. 
FTP File Transfer Protocol; application layer protocol for the transfer of files. 
GoBS Generally Acce pted Accounting Principles of Computer-Assisted 
Accounting Sy stems (Grundsätze ordn ungsgemäßer DV-ge stützter 
Buchführungssysteme); m inimum requir ements on the func tionality and 
control of data-processing systems derived from the German Commercial 
Code. 
Hacker A person  w ith a tech nical in terest in the fun ctionality of hardware and 
software and the refore has the know-how necessa ry for circumventing 
security arra ngements in har dware and software. Often no d istinction is 
made between a hacker and a � cracker in everyday language, while the 
distinction is normally upheld in specialist circles. 
Host Operator of a server. 
HTTP Hypertext Transfer Protocol; application l ayer pr otocol f or pre senting 
websites. 
IDS � Intrusion Detection System 
ICS � Internal Control System 
Internal Control System All measures that serve to minimize an organization’s risks, avert damage 
and secure its assets. 
Internet Service Provider � Provider 
Intrusion Detection 
System 
Security software that de tects n etwork-based at tacks and, if n ecessary, 
responds to them. 
IP address A num ber that  con sists o f fo ur blo cks of numbers between 0 and 255 
(written in decimals) and wh ich c an be used add ress a sy stem on the 
internet or intranet. 
ISP � Internet Service Provider 
LAN Local Area Network. 
Linux A free (� Open Source) Unix compatible operating system. 
News groups News and discussion forums on the internet. 
Open Source An ini tiative tha t p romotes th e f ree availability of so ftware and the 
Federal Office for Information Security - 87 -

<!-- page 88 -->

Study: A Penetration Testing Model 
Term Explanation 
disclosure of the corresponding source codes. 
OSI reference model Seven-layer m odel for demonstrating and standardizing communication 
between computer systems. 
Outsourcing Purchase of services (previously rendered in-house) from third parties. 
P2P Client Peer-To-Peer Client; a computer program for exchanging or downloading 
all manner of files. 
Packet filter Security layers 1 to 3 of the �OSI reference model. 
Provider Service provider, mostly offering access to the internet. A �host is also a 
provider in this sense. 
Router A network device that connects two or more networks. 
Vulnerability scanner Security so ftware w hich a llows sy stems to be ch ecked for potential 
software vulnerability and security gaps. 
Security policy A document that describes the security objectives of an organization in an 
abstract way. 
SMTP Simple Mail Transfer Protocol; an application layer protocol mainly used 
for transferring e-mails. 
Sniffer A tool for intercepting network traffic. 
Social engineering An att acking m ethod tha t en tails t ricking peop le to d isclose sensitive 
information (e.g. passwords) or otherwise manipulating them. 
Spoofing The attacking m ethod of a c racker who attempts to de ceive sy stems or 
persons through t echnical m anipulation (e.g. fak ing a fa lse I P address, 
faking a false DNS address etc.). 
TCP/IP A network protocol used on the internet and in internal networks. 
Tiger team A group of penetration testers. 
Trojan horse A prog ram that pe rforms harm ful functions i n th e ba ckground tha t g o 
unnoticed by the user (e.g. intercepting and transferring passwords). 
WAN Wide A rea N etwork; a n or ganization-wide ne twork t hat spans several 
different sites. 
War dialer A hacker tool that dials blocks of telephone numbers automatically and 
elicits information from the m achine t hat answ ers. O ften us ed fo r 
- 88 - Federal Office for Information Security

<!-- page 89 -->

Study: A Penetration Testing Model 
Term Explanation 
localizing unsecured modems. 
War walking To establish the existence and spread of WLAN networks. 
War driving � War walking from a vehicle. 
Web bug An invisible part of a website which enables a system not v isible to the 
user to intercept in formation on the user’s sy stem configuration (I P 
address, browser version etc.). 
Web server A computer that makes information available on the internet for retrieval. 
Web hosting Operation of a � web server on behalf of a customer. 
White-box test A penetration test in which the tester has prior information on the network 
he/she is testing. 
WLAN Wireless Local Area Network. 
Federal Office for Information Security - 89 -

<!-- page 90 -->

Study: A Penetration Testing Model 
Bibliography
[Andersen99]. Arthur Andersen, KontraG – Erläuterungen zu den wichtigsten Vorschriften 
und praktische Hinweise zur Umsetzung, 3rd edition 1999 
[Anonymous01] Anonymous: Der neue Hacker’s Guide, 2nd edition, Markt & Technik 2001 
[BSI02] IT Baseline Protection Manual (Das IT-Grundschutzhandbuch), May 2002, 
Bundesamt für Sicherheit in der Informationstechnik, 
http://www.bsi.de/gshb/index.htm 
[BSI01] Die BSI Firewallstudie II, 2001, 
http://www.bsi.de/literat/studien/firewall/fwstud.htm 
[CCC02] Chaos Computer Club, http://www.ccc.de/congress/2001/overview.de.html 
[CSEG02] CSEG Communications-Electronic Security Group, 
http://www.cseg.gov.uk/partnerships/pwi/check/index.htm 
[CSI02] CSI Computer Security Institute, 2002 CSI/FBI Computer Crime and Security 
Survey, http://www.gocsi.com 
[Discovery02] Discovery.com, 
http://www.discovery.com/area/technology/hackers/crunch.html 
[Emmert02] Emmert, Ulrich: Strafbare Sicherheits-Tools?, in KES Zeitschrift für 
Kommunikations- und EDV-Sicherheit, Vol. 2, Year 18. 2002, p.6-9 
Fuhrberg/Häger/Wolf: Internet-Sicherheit, 3rd edition., Hanser 2001[Fuhrberg01] 
[GIAC02] GIAC, 2002, http://www.giac.org 
[Herzog02] Herzog, Pete: Open Source Security Testing Manual OSSTMM, 2002, 
http://www.osstmm.org/ 
[ISACA02] Information Systems Audit and Control Association, 2002, 
http://www.isaca.org/ 
[ISACA_CH99] ISACA Switzerland: Sicherheitsüberprüfung von IT-Systemen mit Hilfe von 
Tiger Teams, 1999, http://www.isaca.ch 
[ISC02] International Information Systems Security Certifications Consortium, 2002, 
http://www.isc2.org/ 
[Kabay00] Kabay, Michel E.: Social engineering simulations, Network World Security 
Newsletter, Dec. 18, 2000, 
http://www.nwfusion.com/newsletters/sec/2000/00292157.html 
- 90 - Federal Office for Information Security

<!-- page 91 -->

Study: A Penetration Testing Model 
[Klevinsky02] Klevinsky/Laliberte/Gupta: Hack I.T. – a guide to security through penetration 
testing, 1st edition, Addison Wesley 2002 
Kurtz/McClure/Scambray: Das Anti-Hacker Buch, 3rd edition, MITP 2002[Kurtz02] 
[LfDN99] Landesbeauftragter für den Datenschutz Niedersachsen, Grundschutz durch 
Firewalls, 1999, http://www.lfd.niedersachsen.de 
[LfV98] Landesamt für Verfassungsschutz Baden-Württemberg: Wirtschaftsspionage – 
die gewerbliche Wirtschaft im Visier fremder Nachrichtendienste, 1998 
[NIST02] NIST Guideline on Network Security Testing, http://csrc.nist.gov 
[SANS] SANS Institute, http://www.sans.org 
[SANS-SAC] SANS Security Alert Consensus 
http://www.sans.org/newlook/digests/SAC.htm 
[Schneier01] Schneier, Bruce: Secrets & Lies – IT-Sicherheit in einer vernetzten Welt, 1st 
edition, Wiley 2001 
[Sptimes01] St. Petersburg Times: A history of hacking, 
http://www.sptimes.com/hackers/history.hacking.html, 2001 
[TLC02] TLC, 
http://tlc.discovery.com/convergence/hackers/articles/history_03_print.html 
[Venema95] Venema, Wietse: SATAN Security Administrator Tool for Analyzing 
Networks, http://www.fish.com/satan/ 
[Vosseberg01] Vosseberg, Thomas: Hackerz Book, 1st edition, Franzis 2001 
Federal Office for Information Security - 91 -

<!-- page 92 -->

Study: A Penetration Testing Model 
Appendix 
A.1 OSSTMM 
The Open Sou rce Security Methodology Manual (O SSTMM) [Herzog02] is a r elatively well k nown 
guideline on penetration testing methodology. The OSSTMM is the result of an initiative launched by 
Pete Herzog. This work is an open source project that lists the steps that have to be performed in a 
penetration test. Several authors constantly work on improving this model and make it available to the 
public. At the time of writing, the latest release of the OSSTMM is version 6.0 RC. T he aim of the 
OSSTMM is to set quality standards for penetration testing. The OSSTMM is aimed at IT security 
service providers who, if they perform penetration tests in accordance with the OSSTMM model, are 
authorized to display the OSSTMM logo on their test reports. 
The OSSTMM divides the area investigated in a penetration test into six sections: internet security, 
information security, physical security, communications s ecurity, wire less se curity, and social 
engineering. Each section ha s i ts own m odules dea ling with the relevant test a reas. Each  of these 
modules is explained briefly and th e anticipated results are listed. The modules consist of tasks to be 
completed by carrying out the individual testing steps. The OSSTMM also contains several templates 
for documenting the results of the testing steps in the various modules. 
There are two d ifferent approaches that can be taken in using the OSSTMM: either the modules are 
completed successively one a fter the o ther, o r, a lternatively, in dependent m odules a re car ried out 
simultaneously. 
The OSSTMM suggests a system of RAV s (risk assessment values) to measure how o ften modules 
should be repeated. For each module there is pair of values, consisting of t he “RAV cycle” and the 
“RAV deg radation”. The R AV cy cle v alue s tates the cycle (in day s) in which the test should be 
repeated. The RAV degradation value denotes, as a percentage, how much security deteriorates within 
this cycle, on the assumption that the original test was performed w ith due care by an exp erienced 
tester. The q uotient of  th e pa ir o f v alues i s us ed in  th e cal culation, i. e. each of the two values 
influences the other and could be replaced by a single value. 
This system was only introduced in the latest version (Version 2.0) of the OSSTMM and is therefore 
likely to be modified further in the open source process. What is more, RAVs are not at all indicative 
of ab solute security; th ey merely descr ibe a  re duction in security ov er tim e in relation to the lev el 
immediately after testing. 
The OSSTMM model does not address the objectives of  penetration testing. It is a k ind of g eneric 
work program that can be adapted to meet individual requirements. 
- 92 - Federal Office for Information Security

<!-- page 93 -->

Study: A Penetration Testing Model 
Modules o r t esting st eps are not ranked in or der of their p riority. Th is means that tes ts tha t detect 
widespread vulnerabilities are not performed with higher priority than other steps that could have only 
very limited chances of succeeding in penetrating a system. 
A.2 NIST Guideline on Network Security Testing 
Another penetration testing model worth m entioning is the “Guideline on N etwork Security Testing” 
by the Nat ional Institute of S tandards and Technology (NIST) [NIST02]. At the time of w riting, the 
document was still in the drafting stage. 
The Guideline describes a m ethodology for testing ne twork secu rity and i s a imed at org anizations 
wishing to inv estigate their ow n I T inf rastructure by self- assessment. T he task of ne twork secu rity 
testing is assigned a p lace in a system’s life cycle. In addition, selected methods for testing network 
security are presented. The Guideline does not c all a ll the m ethods i n th eir en tirety “penetr ation 
testing”; this term is reserved fo r on e of m any techn iques (o thers include ne tworking mapping or 
password cracking). The penetration testing technique is broken down into the successive phases of 
planning, discovery, attack and the parallel reporting phase. 
A.3 ISACA Switzerland – Testing IT Systems Security With Tiger Teams 
The Special Interest Group on Information S ecurity of th e S wiss I nformaticians S ociety and the 
ISACA ( Information Sy stems Audit and Con trol As sociation) S witzerland jointly published a 
pamphlet entitled “Sicherheitsüberprüfung von IT-Systemen mit Hilfe von Tiger Teams” (Testing IT 
Systems Securi ty with Tiger Teams). [I SACA_CH99] T he te rm “tig er team” re fers to  a g roup o f 
penetration testers. The pamphlet deals with penetration testing, splitting the process into four stages: 
� Acquisition, proposal and contract 
� Risk analysis 
� Testing 
� Report and presentation 
The work  is no t a coherent m ethodology since the v arious chapters were written by sub-working 
groups. 
The “acquisition, pr oposal and contract” chapter contains a d etailed description of important is sues 
that need to be clarified in a contract before carrying out a penetration test 
The “risk analysis” section contains a method for identifying and as sessing risks associated with the 
penetration test. 
Federal Office for Information Security - 93 -

<!-- page 94 -->

Study: A Penetration Testing Model 
The “testing” chapter comprises the tasks to b e completed in a p enetration test. The following tasks 
are covered: 
1. Carrier scan: scan for modems than be accessed from outside. 
2.	 Internet scan: scan for computer systems that can be accessed over the internet and their 
identification. 
3. Password cracking: testing passwords and password policies. 
4. Manual hacking: attempt to exploit the potential vulnerabilities identified in tasks 1 – 3. 
5. Intranet scan: similar to 2, except over the internal network. 
6. System scan: system analysis to identify general configuration and unnecessary services. 
7. Phreaking: testing systems connected with the telephone system. 
8.	 Analysis o f re lationships o f trust: r elationships o f t rust w ith bus iness p artners, 
customers and suppliers. 
The “r eporting” chap ter exp lains the elements required f or informative doc umentation a nd 
presentation of results. 
The “risk ana lysis” chapter con tains an i nteresting m ethod for prioritizing and se lecting tes t 
procedures to be carried out during the penetration test. An “overall risk” is identified in two steps and 
acts as a basis for deciding which techniques to employ. The steps are: 
� Analysis of system risk 
Evaluates how prone the system conce rned is to ha cker a ttacks, app lying the c riteria o f 
“threat” (how great is the potential threat to the system?), “hacker skills” (how skilled must a 
hacker be to exploit the risk?) and “internal/external” (is the threat from the inside and/or the 
outside relevant?). 
� Analysis of risk of hacker attacks 
Evaluates th e t ime requ ired fo r an attack and the prob ability that an appr opriate attack 
technique w ill succeed, together w ith a risk asse ssment of the ef fects of the attack. The 
outcome is a definite decision for or against the use of the technique. Available criteria are 
“chance of success” (how probable is it tha t the attack will be successful?), “effort required” 
(how t ime-consuming is the m ethod o f a ttack for the penetration tes ter?), and “ri sk 
assessment” (how serious are the potential effects of the attack on the system?). 
- 94 - Federal Office for Information Security

<!-- page 95 -->

Study: A Penetration Testing Model 
Viewed a s a w hole, the w ork deal s w ith i ssues su ch a s ri sk ana lysis and efficiency of penetration 
testing. The chapters on contracts and reporting also contain quite detailed comments on the essential 
content of contracts and documentation. 
Hacking techniques are described in the “testing" chapter. Efficiency is discussed at the beg inning of 
the chapter, but the concept is not elaborated further in a method for choosing individual tasks. 
A.4 Penetration Testing Certification 
A.4.1 The CSEG CHECK Certificate 
The CSEG (Com munications-Electronics Secu rity Group) is a British governmental auth ority that 
deals with aspects of IT security and provides advice to other authorities on issues of IT security. The 
CSEG has de fined a standard fo r I T sec urity serv ice p roviders by  int roducing ce rtification ca lled 
CHECK (Computer IT Health Check Service). The CHECK initiative is designed to allow authorities 
and companies to identify qualified providers of IT security tests (IT Health Check) using the CHECK 
seal of quality [CSEG02]. 
In order to ob tain C HECK c ertification, th e I T sec urity serv ice pr ovider m ust be a member of the 
CHECK service. The current annual membership fee is 7000 pounds Sterling. Membership includes 
participation in a one-day “C HECK Serv ice A ssault C ourse” t hat p rovides training in h acking 
methods and a  f inal exam . I f the par ticipant passes the exam, he/she and his/her com pany are 
authorized to perform IT health checks in accordance with the CHECK model. The CHECK seal of 
quality is essential for contracts in the public sector and is used for promotional purposes in the private 
sector. 
In order to be accepted into the CHECK service program, the following information must be disclosed 
to the CESG: 
� details on the business structure of the IT security service provider 
� details of the methodical approach for services 
� the number of projects carried out in the last 12 months 
�	 an (anonymized) copy of a report on a n I T hea lth check pro ject d etailing th e sub ject o f th e 
contract, test findings and results 
� details of contact partners for reference purposes 
� details of any other certifications (ISO 9000) 
Federal Office for Information Security - 95 -

<!-- page 96 -->

Study: A Penetration Testing Model 
�	 employee details: name, date of birth, nationality and curriculum vitae of all employees capable of 
performing IT health checks 
To date, the CHECK certificate is fairly well received in B ritain. One point of criticism is th at only 
one employee of an IT secur ity service provider n eeds to p ass th e exam  to ob tain f or h is/her 
organization the status of a CHECK-certified IT service provider. 
A.4.2 The ISC² CISSP Certificate 
The CISSP (Certified Internet Security Systems Professional) certificate is issued by the International 
Information Systems Security Certification Consortium (ISC²) [ISC02]. It is an exam that entitles the 
successful candidate to bear the CISSP title. 
The ISC² was founded by a group of IT security service providers in 1988. The main objective of the 
ISC² is t o es tablish s tandards in  th e f ield of I T s ecurity. T hese s tandards a re referred to a s C BKs 
(Common Body of Knowledge) and comprise a collection of information on the topic of IT security. 
The objective of the CISSP initiative is to create certificates which IT security consultants can use as 
evidence of their expertise. The CISSP program has been in existence since 1992. 
The exam covers the following areas: 
� Access protection mechanisms and methods 
� Application and system development 
� Contingency planning 
� Cryptology 
� Legal background, forensic methods and ethics 
� Security in current operations 
� Physical security 
� Security architectures and models 
� Security management 
� Telecommunications, network and internet security 
In addition to passing the exam, there are further conditions that must be fulfilled before becoming 
certified. For  exam ple, the CI SSP appl icant m ust pr ovide ev idence o f three years of professional 
- 96 - Federal Office for Information Security

<!-- page 97 -->

Study: A Penetration Testing Model 
experience in the field of IT security and a reference either from another certified CISSP or from his 
employer. He/she must also follow the ethical codex of the ISC² and pay regular fees to the ISC². 
The CI SSP exa m i s r elatively unk nown i n Ge rmany. T his is p robably because t he ISC² is not 
represented in Germany yet. The CISSP certificate is widely recognized in the USA. As yet, the ISC² 
has not published the exact number of CISSPs certified so far. 
The ISC² has rec ently also started to offer the SSCP (System Security Certified Practitioner) exam. 
This certificate differs from t he CISSP in t hat it caters to a target group of network administrators, 
while the CISSP certificate addresses a target group of security consultants/officers. The SSCP exam 
covers the following areas: 
� Access protection mechanisms 
� Administration 
� Monitoring 
� Risk, escalation procedures and startup processes 
� Cryptology 
� Data communication 
� Malignant program codes/malware 
We are currently unable to comment on the s pread of the SSCP certificate or the extent to which it is 
recognized. 
A.4.3 The SANS Institute GIAC Certificate 
The SANS (Sy stem Adm inistration, Ne tworking and Security) Institute is a renowned org anization 
that has made a name for itself through a number of publications in the field of IT security. Founded in 
1989, t he SA NS Institute pu blishes, for example, t he ann ual “SA NS Top Twenty”, a list of the 20 
most widespread vulnerabilities of IT systems. [SANS] 
The GIAC certification (Global Information Assurance Certification) has been in existence since 1999 
with the aim of allowing consultants to provide evidence of their expertise. 
The G IAC prog ram consists  of  a s eries o f individual exams and d iffers, ac cording to the SANS 
Institute, from other certificates, in that it tests both theoretical knowledge and its practical application. 
In addition, the GIAC exams also cover advanced technical areas. 
Federal Office for Information Security - 97 -

<!-- page 98 -->

Study: A Penetration Testing Model 
The objective of the certification is to obtain GSE status (GIAC Security Engineer) by passing a series 
of six exams. The GSE applicant must also write an essay on a topic relating to IT security which is 
then published on the SANS Institute homepage. 
As well as the exams required for the GSE, there are further additional GIAC exams in other areas of 
IT security. The GSE exams are as follows: 
� GSEC (GIAC Security Essentials) 
� GCFW (GIAC Certified Firewall Analyst) 
� GCIA (GIAC Certified Intrusion Analyst) 
� GCIH (GIAC Certified Incident Handler) 
� GCNT (GIAC Certified Windows Security Administrator) 
� GCUX (GIAC Certified Unix Security Administrator) 
According to t he GIAC homepage, 3600 pers ons were certified in accordance with GIAC when this 
study was being compiled. 
A.4.4 The ISACA CISA Certificate 
The Information Sy stems Audit and Con trol Association (ISACA) is the w orld as sociation o f ED P 
auditors and awards the CISA (Certified Information Systems Auditor) Certificate. The ISACA was 
founded in 1968 and now numbers 17,000 members in 101 countries. 
The objective of the CISA program is to create quality standards for IT auditors. In order to obtain the 
CISA title, the applicant must pass the CISA exam, have several years of professional experience in 
the area of IT audits and observe the ISACA’s code of conduct . 
The CISA exam contains questions from the following areas: 
� IT management, planning and organization 
� Technical infrastructure 
� IT security 
� Contingency planning 
� System development, selection, introduction and maintenance 
� Business process analysis and risk management 
- 98 - Federal Office for Information Security

<!-- page 99 -->

Study: A Penetration Testing Model 
There are currently 23,000 people worldwide who bear the CISA title. 
Federal Office for Information Security - 99 -

<!-- page 100 -->

Study: A Penetration Testing Model 
A.5 I and E Modules and Their OSSTMM Equivalents 
The tables below show I and E modules and their equivalents in the OSSTMM 2.0 RC 6. [Herzog02] 
Since the OSSTMM does not di fferentiate be tween co vert (stealthy) and overt ( noisy) te sts an d 
because some OSSTMM modules have been combined, it is not possible to achieve a 1:1 or N:1/1:N 
match. Instead, they have to be matched N:M. 
A.5.1 Reconnaissance Modules and Their Equivalents 
No. Module OSSTMM 2.0 RC 6 
I 1 Analysis of Published Data M 2.03 Document Grinding 
I 2 Covert Queries of Basic Network Information M 1.01 Network Surveying 
I 3 Overt Queries of Basic Network 
Information 
M 1.01 Network Surveying 
I 4 Stealthy Port Scans M 1.02 Port Scanning 
I 5 Noisy Port Scans M 1.02 Port Scanning 
I 6 Application Identification M 1.03 Services Identification 
M 1.06 Internet Application Testing 
I 7 System Identification M 1.04 System Identification 
I 8 Covert Router Identification M 1.07 Router Testing 
I 9 Overt Router Identification M 1.07 Router Testing 
I 10 Covert Firewall Identification M 1.09 Firewall Testing 
I 11 Overt Firewall Identification M 1.09 Firewall Testing 
I 12 Vulnerability Research M 1.05 Vulnerability Research 
I 13 Application Interface Identification M 1.06 Internet Application Testing 
I 14 Collecting Information for Social Engineering M 3.01 Request Testing 
M 3.02 Guided Suggestion Testing 
M 3.03 Trusted Persons Testing 
I 15 Collecting Information for Computer-Based 
Social Engineering 
-
I 16 Collecting Information for Personal Social 
Engineering 
M 3.01 Request Testing 
M 3.02 Guided Suggestion Testing 
M 3.03 Trusted Persons Testing 
I 17 Wireless Communications Testing (Scanning 
Only) 
M 4.01 Wireless Networks Testing 
M 4.02 Cordless Communications 
Testing 
M 4.04 Infrared Systems Testing 
I 18 Telephone System Testing (Identification) M 5.01 PBX Testing 
I 19 Voicemail System Testing (Identification) M 5.02 Voicemail Testing 
I 20 Fax System Testing (Identification) M 5.03 Fax Review 
I 21 Analysis of Physical Environment M 6.05 Location Review 
- 100 - Federal Office for Information Security

<!-- page 101 -->

Study: A Penetration Testing Model 
No. Module OSSTMM 2.0 RC 6 
I 22 Access Control Identification M 6.01 Access Controls Testing 
M 6.03 Monitoring Review 
A.5.2 Active Intrusion Modules and Their Equivalents 
No. Module OSSTMM 2.0 RC 6 
E 1 Covert Verification of Actual Vulnerabilities M 1.05 Vulnerability Research 
E 2 Overt Verification of Actual Vulnerabilities M 1.05 Vulnerability Research 
E 3 Verification of Actual Vulnerabilities in 
Application Interfaces 
M 1.06 Internet Application Testing 
E 4 Covert Router Testing M 1.07 Router Testing 
E 5 Overt Router Testing M 1.07 Router Testing 
E 6 Test of Trust Relationships Between Systems M 1.08 Trusted Systems Testing 
E 7 Covert Firewall Test From Outside M 1.09 Firewall Testing 
E 8 Overt Firewall Test From Outside M 1.09 Firewall Testing 
E 9 Testing the Firewall From Both Sides M 1.09 Firewall Testing 
E 10 IDS System Testing M 1.10 IDS Testing 
E 11 Intercepting Passwords M 1.12 Password Cracking 
E 12 Password Cracking M 1.12 Password Cracking 
E 13 Test of Susceptibility to Denial of Service 
Attacks 
M 1.13 Denial of Service Testing 
E 14 Computer-Based Social Engineering -
E 15 Direct, Personal Social Engineering With 
Physical Access 
M 3.01 Request Testing 
M 3.02 Guided Suggestion Testing 
M 3.03 Trusted Persons Testing 
E 16 Indirect, Personal Social Engineering 
Without Physical Access 
M 3.01 Request Testing 
M 3.02 Guided Suggestion Testing 
M 3.03 Trusted Persons Testing 
E 17 Wireless Communications Testing M 4.01 Wireless Networks Testing 
M 4.02 Cordless Communications 
Testing 
M 4.04 Infrared Systems Testing 
E 18 Testing Administrative Access to the 
Telephone System 
M 5.01 PBX Testing 
E 19 Voicemail System Testing M 5.02 Voicemail Testing 
E 20 Testing Administrative Points of Access to 
the Fax System 
M 5.03 Fax Review 
E 21 Modem Testing M 5.04 Modem Testing 
E 22 Active Test of Access Controls M 6.01 Access Controls Testing 
E 23 Test of Escalation Procedures M 6.03 Monitoring Review 
M 6.04 Alarm Response Review 
Federal Office for Information Security - 101 -

<!-- page 102 -->

Study: A Penetration Testing Model 
A.6 Checklists and Documentation Forms 
A.6.1 Checklist for Completing the I Modules 
No. Module Ref. no. Done 
I 1 Analysis of Published Data � 
I 2 Covert Queries of Basic Network 
Information 
� 
I 3 Overt Queries of Basic Network 
Information 
� 
I 4 Stealthy Port Scans � 
I 5 Noisy Port Scans � 
I 6 Application Identification � 
I 7 System Identification � 
I 8 Covert Router Identification � 
I 9 Overt Router Identification � 
I 10 Covert Firewall Identification � 
I 11 Overt Firewall Identification � 
I 12 Vulnerability Research � 
I 13 Application Interface Identification � 
I 14 Collecting Information for Social Engineering � 
I 15 Collecting Information for Computer-Based 
Social Engineering 
� 
I 16 Collecting Information for Personal Social 
Engineering 
� 
I 17 Wireless Communications Testing (Scanning 
Only) 
� 
I 18 Telephone System Testing (Identification) � 
I 19 Voicemail System Testing (Identification) � 
I 20 Fax System Testing (Identification) � 
I 21 Analysis of Physical Environment � 
I 22 Access Control Identification � 
- 102 - Federal Office for Information Security

<!-- page 103 -->

Study: A Penetration Testing Model 
A.6.2 Checklist for Completing the E Modules 
No. Module Ref. no. Done 
E 1 Covert Verification of Actual 
Vulnerabilities 
� 
E 2 Overt Verification of Actual 
Vulnerabilities 
� 
E 3 Verification of Actual Vulnerabilities in 
Application Interfaces 
� 
E 4 Covert Router Testing � 
E 5 Overt Router Testing � 
E 6 Test of Trust Relationships Between 
Systems 
� 
E 7 Covert Firewall Test From Outside � 
E 8 Overt Firewall Test From Outside � 
E 9 Testing the Firewall From Both Sides � 
E 10 IDS System Testing � 
E 11 Intercepting Passwords � 
E 12 Password Cracking � 
E 13 Test of Susceptibility to Denial of Service 
Attacks 
� 
E 14 Computer-Based Social Engineering � 
E 15 Direct, Personal Social Engineering With 
Physical Access 
� 
E 16 Indirect, Personal Social Engineering 
Without Physical Access 
� 
E 17 Wireless Communications Testing � 
E 18 Testing Administrative Access to the 
Telephone System 
� 
E 19 Voicemail System Testing � 
E 20 Testing Administrative Points of Access 
to the Fax System 
� 
E 21 Modem Testing � 
E 22 Active Test of Access Controls � 
E 23 Test of Escalation Procedures � 
Federal Office for Information Security - 103 -

<!-- page 104 -->

Study: A Penetration Testing Model 
A.6.3  Form for Collecting Server Information 
DNS name 
IP address 
Role 
Operating 
system 
Port Protocol Application Potential 
vulnerability 
Other information 
- 104 - Federal Office for Information Security

<!-- page 105 -->

Study: A Penetration Testing Model 
Federal Office for Information Security - 105 -

<!-- page 106 -->

Study: A Penetration Testing Model 
A.6.4 Form for Collecting Social Engineering Information 
Name 
Function 
E-mail 
Telephone 
Description of 
the attack 
Result 
- 106 - Federal Office for Information Security

<!-- page 107 -->

Study: A Penetration Testing Model 
A.6.5 Form for Collecting Further Information 
Area/module 
Description of the 
test procedure 
Result 
Federal Office for Information Security - 107 -

<!-- page 108 -->

Study: A Penetration Testing Model 
A.7 Tools 
The following table provides a list of hacker and security tools that can be used in penetration testing. 
Unless stated otherwise, the tools listed are freeware. The list does not compare the functionality of the 
tools and does not claim to be exhaustive. 
Name Particularities Platform Source 
Port scanners 
7th Sphere 
Portscanner 
Easy-to-use port scanner Windows http://www.computech.ch 
Nmap Port scanner with extended functions 
such as stealth scans or system 
recognition 
Unix, 
Windows 
http://www.insecure/nmap 
Strobe Fast TCP port scanner Unix ftp://suburbia.net/pub 
Super Scan Port scanner with an easy-to-operate 
user interface 
Windows http://www.computech.ch 
Vulnerability 
scanners 
Cerberus Internet 
Scanner 
Vulnerability scanner available either in 
a freeware version or a commercial 
version with extended functions. 
WinNT, 
Win2000 
http://www.cerberus­
infosec.co.uk/cis.shtml 
Happy Browse 
/THC 
Vulnerability scanner that creates a list 
of potential vulnerable spots, but 
without any guidelines for exploitation 
Windows http://www.pimmel.com/thcfiles.php3 
ISS Internet 
Scanner 
Commercial vulnerability scanner Win2000, 
WinXP 
http://www.iss.net 
Nessus Vulnerability scanner made up of client 
and server components 
Unix, 
Windows 
http://www.nessus.org 
Saint Commercial vulnerability scanner Unix http://www.wwdsi.com 
SARA Freeware version of the commercial 
vulnerability scanner Saint 
Unix http://www-arc.com/sara 
SATAN First-generation vulnerability scanner, 
now obsolete and no longer updated 
Unix http://www.fish.com/satan 
Xscan Vulnerability scanner that can be 
operated from the instruction line and 
via a GUI. 
Windows http://www.xfocus.org/programs.php 
- 108 - Federal Office for Information Security

<!-- page 109 -->

Study: A Penetration Testing Model 
Name Particularities Platform Source 
War dialers 
Phonesweep Commercial war dialer, requires 
specialist knowledge 
n.a. http://sandstorm.net/products/phoneswee 
p 
THC Scan Common war dialer for DOS/Windows DOS http://www.thehackerschoice.com 
ToneLoc Rather outdated war dialer DOS 
CGI scanners 
Whisker Tool for localizing security gaps in CGI 
scripts 
Unix http://sourceforge.net/projects/whisker 
WLAN scanners 
Kismet Tool for detecting and intercepting 
WLANs 
Unix http://www.kismetwireless.net 
Net Stumbler Tool for detecting WLANs Windows http://www.netstumbler.com 
Other scanning 
tools 
Cheops Supplies a graphical description of the 
scanned network 
Unix ftp://ftp.marko.net/pub/cheops 
Firewalk Tool for testing firewall rules Unix http://www.packetfactory 
Languard Port scanner with many additional 
functions 
Win95, 
WinNT 
http://www.gfi.com/downloads 
Sam Spade Universally implementable tool for 
obtaining information, incl. Whois and 
DNS queries 
Windows http://www.samspade.org 
Visualroute Supplies a graphical overview of traced 
routes 
Unix, 
Windows 
http://www.visualroute.com 
What’s running Supplies information on software 
running on a target computer 
Windows http://www.woodstone.nu/whats 
LAN sniffers 
Angst Enables sniffing in switched networks FreeBSD http://wiretapped.net 
Dsniff Dnisff contains a collection of 
programs that allow the interception of 
network traffic in switched networks 
Unix http://www.monkey.org 
Federal Office for Information Security - 109 -

<!-- page 110 -->

Study: A Penetration Testing Model 
Name Particularities Platform Source 
Ethereal A packet sniffer that can also interpret 
application layer information 
Windows, 
Unix 
http://www.ethereal.com 
Sniffit Specially designed to record application 
data and passwords 
Unix http://reptile.rug.ac.be/~coder/sniffit/sniff 
it.html 
Snort Intrusion detection system with a 
sniffer component 
Windows, 
Unix 
http://www.snort.org 
Tcpdump Packet sniffer for OSI layers 1 to 4 Unix http://www.tcpdump.org 
Windump Windows version of Tcpdump Windows http://winpcap.polito.it 
WLAN sniffers 
AirSnort This tool allows data recording in 
WLANS 
Linux http://sourceforge.net/projects/airsnort 
WEPCrack Can be used for cracking keys in 
WLANS 
Linux http://sourceforge.net/projects/wepcrack 
Password crackers 
Brutus Enables Telnet/FTP/Netbios/POP3 
passwords to be cracked 
Windows http://hobbie.net/brutus/brutus­
download.html 
Crack Allows Unix passwords to be cracked Unix http://www.users.dircon.co.uk/~crypto/ 
John the Ripper Tool for cracking NT and Unix 
passwords 
Unix, DOS, 
Windows 
http://www.openwall.com/john 
L0pht Crack For cracking Windows passwords Windows http://www.atstake.com 
Web Cracker For overcoming web authentications Windows http://www.packetstormsecurity.org 
Attacking tools 
Fragrouter Tool for fragmenting packets Unix http://www.packetstormsecurity.com 
Hping For testing firewall rules, many other 
options 
Unix http://www.hping.org 
Hunt Tool for performing a session hijacking 
attack 
Unix http://www.wiretapped.net 
IRPAS Collection of programs Unix http://phenoelit.de 
Jolt2 Tool for performing a DoS attack Unix http://www.securiteam.com/exploits/Jolt 
2_-_a_new_Windows_DoS_attack.html 
Nemesis Collection of tools for manipulating 
data packets 
Unix http://the.wiretapped.net 
- 110 - Federal Office for Information Security

<!-- page 111 -->

Study: A Penetration Testing Model 
Name Particularities Platform Source 
RafaleX Packet builder for manipulating 
IP/TCP/UDP packets 
Windows http://www.packx.net/packx 
Stacheldraht Tool for carrying out a distributed DoS 
attack (Ddos attack) 
Unix 
TFN2000 Tool for carrying out a distributed DoS 
attack (Ddos attack) 
Windows, 
Unix 
Trin00 Tool for carrying out a distributed DoS 
attack (Ddos attack) 
Unix 
Trojan horses 
Back Orifice Tools for remote operating a PC Windows http://www.cultdeadcow.com 
Netbus Tools for remote operating a PC Windows http://www.windowsecurity.com 
Sub Seven Tools for remote operating a PC Windows http://www.subseven.ws 
Other tools 
Datapipe.c Tool for rerouting connections and 
circumventing firewall rules 
Unix http://packetstormsecurity.nl/unix­
exploits/tcp-exploits 
Fpipe Reroutes connections to another port 
and circumvents firewalls 
Windows http://www.networkingfiles.com 
Netcat Universally implementable tool for 
manipulating TCP and UDP 
connections 
Windows, 
Unix 
http://www.atstake.com 
Federal Office for Information Security - 111 -

