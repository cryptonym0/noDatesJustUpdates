##1: Security and Cryptography Concepts

1. **Cybersecurity** is the prevention of damage to, unauthorized use of, exploitation of, and—if needed—the restoration of electronic information and communications systems, electronic communications services, wire communication, and electronic communication, including information contained therein, to ensure its availability, integrity, authentication, confidentiality, and nonrepudiation.
2. **Information Security** is the preservation of confidentiality, integrity, and availability of information. In addition, other properties, such as authenticity, accountability, nonrepudiation, and reliability, can also be involved.
3. **Network Security** the protection of networks and their services from unauthorized modification, destruction, or disclosure and provision of assurance that the networks perform their critical functions correctly, without harmful side effects.
4. **Cryptography** 1. The discipline that embodies the principles, means, and methods for the transformation of data in order to hide their semantic content, prevent their unauthorized use, or prevent their undetected modification. 2. The discipline that embodies the principles, means, and methods for the providing information security, including confidentiality, data integrity, non-repudiation, and authenticity.
5. **Cryptographic Algorithm** A well-defined computational procedure, pertaining to cryptography, that takes variable inputs, often including a cryptographic key, and produces an output.

### 1.1 The 5 main security objectives 

1. **Confidentiality** (data) the property that information is not made available or disclosed to unauthorized individuals, entities, or processes. A loss of confidentiality is the unauthorized disclosure of information.
2. **Integrity**
   - **data** ensures that data (both stored and in transmitted packets) and programs are changed only in a specified and authorized manner. A loss of data integrity is the unauthorized modification or destruction of information.
   - **system** ensures that a system performs its intended function in an unimpaired manner, free from deliberate or inadvertent unauthorized manipulation of the system.
3. **Accountability** goal that generates the requirement for actions of an entity to be traced uniquely to that entity. This supports nonrepudiation, deterrence, fault isolation, intrusion detection and prevention, and after-action recovery and legal action. Because truly secure systems are not yet an achievable goal, it must be possible to trace a security breach to a responsible party. Systems must keep records of their activities to permit later forensic analysis to trace security breaches or to aid in transaction disputes.
4. **Availability** ensures that systems work promptly and that service is not denied to authorized users. A loss of availability is the disruption of access to or use of information or an information system.
5. **Authenticity** being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or a message originator. This means verifying that users are who they say they are and that each input arriving at the system came from a trusted source.

### 1.2 The Game

....I suppose it isn't really a game from the defenders prospective. It's a battle of wits between
1. The attacker(s) who try to find holes. We only every really need to find one weakness or vulnerability to win.
    - Greed of companies is to the attackers benefits. We know it is unlikely that security is an integral part of the design process, and likely an afterthought.
    - 
2. The defenders who try to close these holes. Every hole must be closed to win. They must find and eliminate all vulnerabilities, preferably before the attacker(s) discover them.
    - It's tricky figuring out when and where a security measure should be used. Physical and Logical

### 1.3 The 5 Stages

1. **Reconnisance & Footprinting** Collect information about the target. IMO this is the most important part of hacking, but i'm just a bird so don;t take my word for it.
   Some of these can count for Scanning/Ennumeration as well.
    - Passive:
        - Personal Info:
          - Spend $8 on Collection #1
          - Social Media / Web Scraping
          - Checking links on sites, job titles, desciptions
          - Obituaries are suprisingly useful 
        - Footprinting:
            - Network, IP, DNS Records .ect
            - maltego
            - HTTPTrack
            - httrack
            - Black Widow
            - Teleport Pro
            - GNU Wget
            - Backstreet Browser
            - Wayback Machine
            - google dorking
    - Active:
        - Dumpster Diving 
        - Social Engineering
            - Honey Trap <3 
            - Pretexting
            - Whaling (also Phishing) (also vishing)
            - Watering Hole
            - Scareware  
            - IRL
            - legit email cx support or like.... apply to job openings
                - job interviews are a great way to learn about a stack
        - Blackmail
            - Baiting
            - Quid pro quo
        - Spice it up with IRL Crimes
            - B & E
            - Diversion Theft  
            - tailgating

2. **Scanning, and Ennumeration**
   This phase includes the usage of tools like dialers, port scanners, network mappers, sweepers, and vulnerability scanners to scan data. 
   - We looking for anything to help us break in:
     - computer names, IP addresses, user accounts.
   - test the network for other avenues of attacks
     - Kali Linux 
     - Maltego
3. **Gaining Access** We have enought info, and now we have options to gain access to the network.
    - If you're not in already it's usually phishing. (phone app, website email spoofing, Zmail, etc) Use bitly or tiny URL to mask your toolkit.
      the hacker sends an email asking the users to log in to a new Google portal with their credentials.  
    - Metasploit is always fun. Evil twin, Malcome in the middle
    - Generally all attacks fit into 6 categories though:
        - Passive:
            - **"release of message contents"**
              The act of an adversary in successfully eavesdropping on a communication, such as a telephone conversation, an electronic mail message, or a transferred file.
            - **Traffic Analysis**
            A form of attack in which the contents of transmitted data blocks are not examined. Assume that there was a way of masking the contents of messages or other information traffic so that adversaries, even if they captured the message, could not extract the information from the message. The common technique for masking contents is encryption. With encryption protection in place, an adversary might still be able to observe the pattern of these messages. The adversary could determine the location and identity of communicating hosts and could observe the frequency and length of messages being exchanged. This information might be useful in guessing the nature of the communication that was taking place.
        - Active:
            - **Replay** 
              involves the passive capture of a data unit and its subsequent retransmission to produce an unauthorized effect.
            - **Data Manipulation/Modification**
              simply means that some portion of a legitimate message is altered or that messages are delayed or reordered to produce an unauthorized effect. For example, a message stating “Allow John Smith to read confidential file Accounts” might be modified to say “Allow Fred Brown to read confidential file Accounts.”
            - **Masquerade**
              takes place when one entity pretends to be a different entity. A masquerade attack usually includes one of the other forms of active attack. For example, authentication sequences can be captured and replayed after a valid authentication sequence has taken place, thus enabling an authorized entity with few privileges to obtain extra privileges by impersonating an entity that has those privileges.
            - **DoS** 
                prevents or inhibits the normal use or management of communication facilities. Such an attack may have a specific target; for example, an entity may suppress all messages directed to a particular destination (e.g., the security audit service). Another form of service denial is the disruption of an entire network, either by disabling the network or by overloading it with messages so as to degrade performance.
4. **Maintaining Access**
    - zombie it
    - blend in with the locals
    - take over doormant accounts
    - collect what you need, quietly.
5. **Covering Your Footsteps**
    - always attack indirectly
    - never use your own MAC
    - vpn at least twice
    - clear the logs, temp files, emails
    - live in fear for the rest of your life 

### 1.4 Hackers hate Services and Mechanisms 
1. Services
    - **Authentication:** A person’s identity is determined before access is granted.
    - **Access Control:** Persons are allowed or denied access to resources for specific purposes.
    - **Data Confidentiality:** Information is only available to persons intended to use or see it.
    - **Data Integrity:** Information is modified only in appropriate ways by persons authorized to change it.
    - **Nonrepudiation:** A person cannot perform an action and then later deny performing the action.
    - **Availability Service:** Apps, services, and hardware are ready when needed and perform acceptably.
2. Mechanisms:
    - Cryptographic Algorithms. 
    - Access Control*: A variety of mechanisms that enforce access rights to resources.
    - Data Integrity*: This category covers a variety of mechanisms used to ensure the integrity of a data unit or stream of data units.
    - Digital Signatures: Data appended to, or a cryptographic transformation of, a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery.
    - Authentication Exchange: A mechanism intended to ensure the identity of an entity by means of information exchange.
    - Traffic Padding:  The insertion of bits into gaps in a data stream to frustrate traffic analysis attempts.
    - Routing Control: A control that enables selection of particular physically or logically secure routes for certain data and allows routing changes, especially when a breach of security is suspected.
    - Notarization: The use of a trusted third party to ensure certain properties of a data exchange.
    
### 1.5 Cryptography  

1. **Keyless:** An algorithm that does not use any keys during cryptographic transformations.
    * Crypto Hash Func:
       turns a variable amount of text into a small, fixed-length value called a hash value, hash code, or digest. A cryptographic hash function has additional properties that make it useful as part of another cryptographic algorithm, such as a message authentication code or a digital signature.
    * Psuedo-rand num gen:  produces a deterministic sequence of numbers or bits that has the appearance of being a truly random sequence. Although the sequence appears to lack any definite pattern, it will repeat after a certain sequence length. Nevertheless, for some cryptographic purposes, this apparently random sequence is sufficient.
2. **Single Key:** An algorithm in which the result of a transformation is a function of the input data and a single key, known as a secret key.
    * Block cipher symmetric encryption
    * Stream cipher symmetric encryption
    * Message Auth Code
3. **Double Key:** (PP) An algorithm in which, at various stages of the calculation, two different but related keys are used, referred to as the private key and the public key.
    * Asymmetric Encryption
        1.  An encryption algorithm takes as input some data to be protected and the private key and produces an unintelligible transformation on that data. A corresponding decryption algorithm uses the transformed data and the corresponding public key to recover the original data. In this case, only the possessor of the private key can have performed the encryption, and any possessor of the public key can perform the decryption.
        2.  An encryption algorithm takes as input some data to be protected and a public key and produces an unintelligible transformation on that data. A corresponding decryption algorithm uses the transformed data and the corresponding private key to recover the original data. In this case, any possessor of the public key can have performed the encryption, and only the possessor of the private key can perform the decryption.
    * Digital Signature Algorithm: A digital signature is a value computed with a cryptographic algorithm and associated with a data object in such a way that any recipient of the data can use the signature to verify the data’s origin and integrity. Typically, the signer of a data object uses the signer’s private key to generate the signature, and anyone in possession of the corresponding public key can verify the validity of that signature.
    * Key Exchange: is the process of securely distributing a symmetric key to two or more parties.
    * User Auth: authenticating that a user attempting to access an application or a service is genuine and, similarly, that the application or service is genuine.
    
### 1.6 Network Protocals

1. IPsec
2. TLS
3. SSH
4. HTTPS
5. IEEE 802.11i
6. S/MINE

### 1.7 Device Security

1. **Firewall**  A hardware and/or software capability that limits access between a network and a device attached to the network, in accordance with a specific security policy. The firewall acts as a filter that permits or denies data traffic, both incoming and outgoing, based on a set of rules based on traffic content and/or traffic pattern.
2. **Intrusion Detection** Hardware or software products that gather and analyze information from various areas within a computer or a network for the purpose of finding and providing real-time or near-real-time warning of attempts to access system resources in an unauthorized manner.
3. **Intrustion Prevention** Hardware or software products designed to detect intrusive activity and attempt to stop the activity, ideally before it reaches its target.
    * Vnet, Private IPs

