##2: Information Privacy Concepts


### 2.1 Terminology

1. **Privacy:** Two general characteristics of privacy are the right to be left alone—that is, free from being observed or disturbed—and the ability to control the information released about oneself.
2. **Information Privacy:** ight of individuals to control or influence what information related to them may be collected and stored and by whom and to whom that information may be disclosed.
3. **PII (Personally Identifyable Information):**
    * Name, such as full name, maiden name, mother’s maiden name, or alias
    * Personal identification number, such as Social Security number (SSN), passport number, driver’s license number, taxpayer identification number, patient identification number, and financial account or credit card number
    * Address information, such as street address or email address
    * Asset information, such as Internet Protocol (IP) or media access control (MAC) address or other host-specific persistent static identifier that consistently links to a particular person or to a small, well-defined group of people
    * Telephone numbers, including mobile, business, and personal numbers
    * Personal characteristics, including photographic images (especially of the face or other distinguishing characteristic), x-rays, fingerprints, or other biometric image or template data (e.g., retinal scan, voice signature, facial geometry)
    * Information identifying personally owned property, such as vehicle registration number or title number and related information
    * Information about an individual that is linked or linkable to one of the above (e.g., date of birth, place of birth, race, religion, weight, activities, geographic indicators, employment information, medical information, education information, financial information)
4. **PbD (Privacy By Design):** to take privacy requirements into account throughout the system development process, from the conception of a new IT system through detailed system design, implementation, and operation.
   * The practice of considering privacy safeguarding measures at the time of the design of the system; that is, designers should consider privacy compliance during the design phase for systems processing PII rather than address compliance only at a subsequent stage.
5. **Privacy Engineering:** involves taking account of privacy during the entire life cycle of ICT (information and communications technology) systems, such that privacy is and remains an integral part of their function. 
   * A specialty discipline of systems engineering focused on achieving freedom from conditions that can create problems for individuals with unacceptable consequences that arise from the system as it processes PII.
   * Privacy engineering focuses on implementing techniques that decrease privacy risks and enables organizations to make 'purposeful' decisions about resource allocation and effective implementation of controls in information systems.
   * WHY? Such techniques decrease risks related to privacy harms and enable purposeful decisions about resource allocation and effective implementation of controls.
6. **System Owner:**  the person or organization having responsibility for the development, procurement, integration, modification, operation, maintenance, and final disposition of an information system. The system owner needs to identify the standards and regulations that apply and develop an overall plan for privacy milestones during system development. It is also important to ensure that all key stakeholders have a common understanding, including privacy implications, considerations, and requirements. This planning activity enables developers to design privacy features into the project.
9. **Usability:** refers to the ease of use of privacy features.
10. **Utility:** refers to the functionality available for databases containing PII with privacy protection in place. Both concepts need to be considered through the design, implementation, and operation of IT systems containing PII.

## 2.2 Privacy By Design

1. Proactive not reactive / Prevenative, not Remedial
   - Prevent problems before they arise. Wear a seatbelt, shoulder check.
   - Assess the potential vulnerabilities in a system and the types of threats that may occure, and select the proper tequniques/controls/configs to protect the system(s)
2. Privacy is the Default Setting
   - Only process the data that is nessisary.
   - Protect our users PII during collection, storage, use, and transmission.
3. Privacy is Embedded into Design
   - Should be core, organic functions, not added on after design is complete.
   - Should ne integral to both the design and architecture of IT systems and to buisness practices.
4. Full Functionallity. It's a posative sum game, not a zero sum game.
   - No degrading. Not system functionality, nor security measures
   - Avoid Tradeoffs. Tradeoffs are usually lazy or the product of shit code.
5. E2E Security Lifecycle Protection
   - Protect the PII from birth to death. Through collection, retinition, and destruction.
   - No gaps! None! Not in the protection nor the accountability.
   - ensures the confidentiality, integrity, and availability of PII throught the lifecycle
   - Use encryption, access controls, logging methods, and secure destruction.
6. Visibility and Transparency
   - People have a right to know what their daya is being used for.
   - Accountability: The organization should clearly document responsibility for all privacy-related policies and procedures.
   - Openess: The organization should provide information about the policies and practices related to managing PII, as well as the individuals and groups accountable for protecting PII within the organization. The concept of openness includes a clearly defined organizational privacy policy for internal distribution as well as a privacy notice available to outsiders, such as web users.
   - Compliance: The organization should have compliance and redress mechanisms 
7. Respect for User Privacy 
   - The organization must view privacy as primarily being characterized by personal control and free choice. Key aspects of this principle are the following:
   -  Consent: Except where otherwise mandated by law, each individual should be empowered with consent for the collection, use, or disclosure of PII.
   - Accuracy: The organization is responsible for ensuring that any PII that it maintains is accurate and up-to-date.
   - Access: Individuals should be able to access any PII maintained by an organization, be informed of its uses and disclosures, and be able to challenge its correctness.
   - Compliance: The organization should have compliance and redress mechanisms.

## 2.3 Privacy By Design - Policy

Planning and Policy are a big part of design. Shocker.
 * identify the standards and regulations that apply and develop an overall plan for privacy milestones during system development. 
 * Inform/educate all key stakeholders have understanding, including privacy implications, considerations, and requirements. 

**Expected Output:**
1. Set of supporting documents that provide a record of the agreed planning decisions
2. How these decisions conform to overall corporate privacy policy
3. How these decisons are related to theoverall development of the information system.

This planning activity enables developers to design privacy features into the project.

## 2.4 (PIA) Privacy Impact Assesment Privacy Risk Assesment
It's all about the money baybe.

Refernce the heck outta these: 
1. NIST SP 800-53 Security and Privacy Controls for Information Systems and Organizations
2. SO 29151 Code of Practice for Personally Identifiable Information Protection


### Four Elements
1. **Privacy-related asset:** Anything that has value to the organization and that therefore requires protection. With respect to privacy, the primary asset is PII of employees, customers, patients, business partners, and so on. This category also includes intangible assets such as reputation and goodwill. 
2. **Privacy threat:** A potential for violation of privacy, which exists when there is a circumstance, a capability, an action, or an event that could violate privacy and cause harm to an individual. That is, a threat is a possible danger that might exploit vulnerability. A related term is threat action, which is a realization of a threat—that is, an occurrence in which a vulnerability is exploited as a result of either an accidental event or an intentional act.
3. **Privacy vulnerability:** A flaw or weakness in a system’s design, implementation, or operation and management that could be exploited by a threat action to violate the system’s privacy policy and compromise PII.
4. **Privacy controls:** The management, operational, and technical controls (i.e., countermeasures) prescribed for an information system to protect PII and ensure that the organization’s privacy policy is enforced.

### Three Steps

1. Determine the harm, or impact, to individuals and the organization of a privacy violation. For each privacy-related asset, determine the possible threats to that asset. Then determine the impact to individuals if their privacy rights are violated and the impact to the organization, in terms of cost or lost value, if a threat action occurs.
2. Determine the likelihood of a privacy incident, where a privacy incident is defined as an occurrence that actually or potentially violates the privacy of PII or that constitutes a violation or an imminent threat of violation of privacy policies, privacy procedures, or acceptable use policies. For each asset, three factors determine the likelihood: the relevant threats to the asset, the vulnerability of the asset to each threat, and the privacy controls currently in place that reduce the likelihood that each threat will cause harm.
3. Determine the level of risk as the combination of the cost if the privacy incident occurs and the likelihood that that incident occurs.

## 2.5 Privacy Controls:
1. Removing the threat source
2. Changing the likelihood that the threat can exploit a vulnerability by reducing or eliminating the vulnerability or by changing the amount of PII collected or the way it is processed
3. Changing the consequences of a privacy event

### Privacy Control Integration Plan:
1. Identifying key privacy roles that will be active throughout the system design and implementation
2. Identifying standards and regulations that apply
3. Developing an overall plan for privacy milestones during system development
4. Ensuring that all key stakeholders have a common understanding, including privacy implications, considerations, and requirements
5. Describing the requirements for integrating privacy controls within the system and the process for coordinating privacy engineering activities with overall system development

This stage should also produce a detailed architecture that incorporates privacy features and controls into the system design. Expected outputs include:
1. A schematic of privacy integration that provides details on where, within the system, privacy is implemented and, if applicable, where privacy mechanisms are shared by multiple services or applications
2. A list of shared services and resulting shared risk
3. Identification of common controls used by the system

## 2.6 Privacy Engineering
Implementation, Deployment, and Ongoing Operations.
Needs technical capabilities, and management Processes.

The three pillars (goals):
1. Incorporate functionality and management practices to satisfy privacy requirements
2. Prevent compromise of PII
3. Mitigate the impact of breach of personal data

Don't Forgettii:
1. Security risk assessment: 
   * A security risk is an expectation of loss expressed as the probability that a particular threat will exploit a particular vulnerability with a particular harmful result. 
   *  Security risk assessment is a process that systematically
      * (a) identifies valuable system resources and threats to those resources, 
      * (b) quantifies loss exposures (i.e., loss potential) based on estimated frequencies and costs of occurrence. 
   * Thus, risk assessment follows two parallel paths. 
     * First, for each threat to a resource, the value of the resource is assessed and the potential impact, or cost, 
       if the threat to that resource becomes a successful threat action.
     * Second, based on the strength of a threat, the probability of the threat becoming an actual threat action, and the vulnerability of the resource, a likelihood of a successful threat action is determined. Finally, the potential impact of the threat and the likelihood of its success are factors in determining the risk.
2. Risk management: 
   * NIST SP 800-37 (Risk Management Framework for Information Systems and Organizations) states that risk management includes a disciplined, structured, and flexible process for organizational asset valuation; security and privacy control selection, implementation, and assessment; system and control authorizations; and continuous monitoring.
   * It also includes enterprise-level activities to help better prepare organizations to execute the RMF at the system level. 
   * an iterative process:
       * Assess risk based on assets, threats, vulnerabilities, and existing controls. From these inputs determine impact and likelihood and then the level of risk. This is the risk assessment component described in the preceding bullet.
       * Identify potential security controls to reduce risk, prioritize their use, and select controls for implementation.
       * Allocate resources, roles, and responsibilities and implement controls.
       * Monitor and evaluate risk treatment effectiveness.
3. Privacy requirments:
   * hese are system requirements that have privacy relevance. System privacy requirements define the protection capabilities provided by the system, the performance and behavioral characteristics exhibited by the system, and the evidence used to determine that the system privacy requirements have been satisfied. 
4. Privacy impact assessment: Define how PII is handled
   * (i) to ensure handling conforms to applicable legal, regulatory, and policy requirements regarding privacy
   * (ii) to determine the risks and effects of collecting, maintaining, and disseminating information in identifiable form in an electronic information system
   * (iii) to examine and evaluate protections and alternative processes for handling information to mitigate potential privacy risks. 
5. Privacy engineering and security objectives: confidentiality, integrity, and availability

## 2.7 Privacy Implementation
* configure and enable system privacy features
* should perform developmental testing of the technical and privacy features PRIOR to SYSTEM integration

## 2.8 System Implementation
* occures at deployment
* privacy control settings are enabled
* privacy features are integrated
* Output: verified list of operational privacy controls integrated into the completed system documentation.

## 2.9 Privacy Testing and Eval
1. Functional Testing - Privacy mechanisms are tested under operational conditions to determine if function works according to requirements
2. Pen test - Mimic real world attacks, identify ways to circumvent the privacy features of an application, system, or network.
3. End User testing - Testing in "the real world" by intended audience.

## 2.10 Auditing
* Continuously Monitor the System
1. Auditing
   * Independant Examination of Records and Activities to ensure compliance with policy/controls/operations
   * reccomend (strongly) changes
2. Incident Response
   * mitigation of violations of security policies and reccomended practices..

it is likely that the most economically valuable electronic asset is aggregations of information on individuals

## 2.11 Privacy vs Security -TODO!!
1. Accountability
   * Security:
   * Privacy
