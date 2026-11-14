---
doc_id: IT-GDL-001
title: Acceptable Use of IT Resources Guideline
category: IT Guidelines
department: Information Technology
doc_type: guideline
version: "3.0"
status: approved
effective_date: 2026-04-01
review_date: 2027-03-31
owner: CIO (Sanjay Kulkarni)
approver: CISO (Farhan Siddiqui)
sensitivity: internal
allowed_roles: [employee, hr, it, finance, marketing, project_manager, product_manager]
applies_to: All employees, interns, contractors and anyone using Veltrix devices, accounts or networks
related_docs: [IT-GDL-002, IT-GDL-003, IT-GDL-004, IT-GDL-005, HR-POL-002, HR-POL-005, ONB-003]
source_reference: Fictional academic sample guideline for Veltrix Systems Pvt. Ltd.; structure informed by common ISO/IEC 27001 control themes
contradiction_example: false
conflicts_with: []
---

# Acceptable Use of IT Resources Guideline

## 1. Purpose

Veltrix gives its people laptops, accounts, software, networks and collaboration tools so they can do their jobs well. These resources also hold customer data and company secrets, so how they are used directly affects the company's security and reputation. This guideline explains what is expected when using company IT resources, what is permitted for personal use, what is prohibited, and how monitoring works. It is written in plain language so that every employee can follow it without technical knowledge.

## 2. Scope

The guideline covers every person who uses Veltrix IT resources: employees, interns, contractors and visitors given temporary access. "IT resources" include company laptops and phones, email, TeamTalk, PeopleHub, ExpenseDesk, HelpPoint, BuyRight, LeadLoop, TrackWise, cloud storage, office networks and Wi-Fi, the VPN, printers, and any software licensed by the company. It also covers personal devices when they are used to access company email or chat (section 7).

## 3. Key principles

1. **Business purpose:** IT resources are provided for company work. Limited personal use is allowed as described in section 6.
2. **Least privilege:** use only the access you need for your role, and only for its intended purpose.
3. **Protect information:** handle data according to its classification (IT-GDL-004).
4. **Accountability:** you are responsible for activity carried out with your account and device.
5. **Report quickly:** suspected problems are reported immediately, even if you are not sure.

## 4. Company devices

### 4.1 Issue and refresh

Each employee receives a company laptop on the first day of employment (see ONB-003). Laptops are refreshed every **4 years**, or earlier if repair would cost more than 40% of the price of a replacement. Additional equipment, such as a second monitor, can be requested through HelpPoint and is approved by the reporting manager.

### 4.2 Required protections

Company laptops are set up with full-disk encryption, an endpoint detection and response (EDR) agent, automatic updates and device management. Employees must not disable, uninstall or bypass these protections. Laptops lock automatically after **5 minutes** of inactivity; employees should lock the screen manually (Windows key + L, or Control + Command + Q on a Mac) whenever they step away.

### 4.3 Care of devices

- Do not leave a laptop unattended in a car, café or public place.
- Carry laptops in hand luggage when flying.
- Do not allow family members or friends to use a company device.
- Return all devices on your last working day (see HR exit procedures).

### 4.4 Lost or stolen devices

A lost or stolen device must be reported **within 1 hour** of discovery by raising a **P1 ticket** through the IT hotline. IT will remotely lock and wipe the device. Delay in reporting increases the risk to customer data and is treated as a breach of this guideline. For theft, the employee should also file a police report, which is needed for insurance.

## 5. Software and services

### 5.1 Installing software

Software may be installed only from the **Self-Service Portal** or through a HelpPoint request. Requests for new software are reviewed by IT for licensing, security and compatibility. Browser extensions are treated as software: only extensions on the approved list may be installed.

### 5.2 Cloud services and file sharing

Company files must be stored in the company's approved cloud storage, not on personal cloud accounts. Sharing files externally is allowed only through the approved file-sharing tool with link expiry turned on, and only for data classified Public or, under a signed NDA, Confidential (IT-GDL-004).

### 5.3 Generative AI tools

The internal AI knowledge assistant is the only approved tool for working with Confidential data. **Public AI tools may only be used with Public data.** Details are in the AI Assistant and Generative AI Usage Guideline (IT-GDL-005).

### 5.4 Removable storage

USB storage devices are blocked on company laptops by default. If a business need exists (for example delivering a file to a customer who cannot receive it electronically), the CISO may approve an exception for up to 30 days. Approved devices must be encrypted.

## 6. Reasonable personal use

Light personal use is permitted when it:
- happens mostly during breaks;
- does not interfere with work or consume significant network resources;
- does not involve illegal, offensive or sexually explicit material;
- does not involve running a private business, gambling or cryptocurrency mining;
- does not involve storing large personal files, such as personal photo libraries, on the company laptop.

Personal banking, booking a doctor's appointment or reading the news during lunch are examples of acceptable personal use. Employees should not expect privacy for personal content stored on company devices (see section 9).

## 7. Personal devices (BYOD)

Employees may access **company email and TeamTalk only** from a personal smartphone, through the company-managed mobile apps, with MFA enabled and a device screen lock of at least 6 digits. Company data must not be downloaded or stored outside the managed apps. Personal laptops and tablets must not be used to access company systems. If a personal phone with company apps is lost, the employee must report it within 1 hour so IT can remove company data from the managed apps; personal data on the phone is not affected.

## 8. Prohibited activities

The following are never permitted:
- sharing passwords, MFA codes or security keys with anyone, including IT staff;
- accessing or attempting to access systems or data without authorisation;
- copying Confidential or Restricted data to personal email, personal storage or unmanaged devices;
- disabling security software or using tools to bypass network controls, such as unapproved VPNs or proxies;
- installing pirated or unlicensed software;
- sending harassing, discriminatory or defamatory messages;
- using company resources for political campaigning or for commercial activity unrelated to Veltrix;
- connecting unknown devices (for example a found USB drive) to a company laptop.

Breaches are handled under the Employee Conduct and Disciplinary Policy (HR-POL-005). Deliberate data theft or deliberate disabling of security controls may be gross misconduct.

## 9. Monitoring and privacy

Company systems are monitored to protect security, for example through malware detection, login records and data-loss prevention alerts. Monitoring is carried out by the Security team in line with applicable law. **The content of personal communications is not reviewed except during a security or HR investigation approved jointly by the CISO and the CHRO.** Monitoring data is Restricted and retained according to IT-GDL-004.

## 10. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| All users | Follow this guideline, protect devices and credentials, report incidents promptly |
| Reporting manager | Approve reasonable equipment requests, reinforce the guideline in the team |
| IT Service Desk | Provide devices and software, respond to tickets within the priority targets in IT-GDL-003 |
| Security team | Operate monitoring, approve exceptions where delegated, investigate incidents |
| CIO | Own this guideline and the IT environment |
| CISO | Approve security exceptions, including removable storage |

## 11. Exceptions

Exceptions must be requested through HelpPoint under *Security Exception*, stating the business reason, duration and compensating controls. The CISO decides. Exceptions are time-limited (normally no more than 6 months) and are recorded in the security exception register.

## 12. Worked examples

**Example 1 - laptop left in a cab.** Anil realises at 21:10 that he left his laptop in a taxi at 20:30. He must raise a P1 through the IT hotline before 21:30 (within 1 hour of discovering the loss), and then file a police report.

**Example 2 - customer file on USB.** A government customer requires a dataset on encrypted USB. The project manager requests a removable-storage exception; the CISO approves it for 10 days with an encrypted company USB drive.

**Example 3 - personal laptop.** Sneha's company laptop is being repaired, so she wants to log in to LeadLoop from her personal laptop. This is not allowed. IT provides a loaner laptop.

**Example 4 - browser extension.** Rahul wants a grammar-checking browser extension. Because it is not on the approved list and reads page content, he must request it through HelpPoint for IT review.

## 13. Frequently asked questions

**Q: How quickly must I report a lost laptop?**
A: Within 1 hour, by raising a P1 ticket through the IT hotline.

**Q: Can I use my personal phone for work email?**
A: Yes, through the company-managed mobile apps with MFA and a 6-digit screen lock.

**Q: Can I use my personal laptop for work?**
A: No. Personal laptops and tablets must not be used to access company systems.

**Q: How often are laptops replaced?**
A: Every 4 years, or earlier if repair would cost more than 40% of a replacement.

**Q: Can I use a USB drive?**
A: USB storage is blocked by default; the CISO can approve an exception for up to 30 days.

**Q: Will IT read my personal messages?**
A: Not unless the CISO and CHRO jointly approve an investigation.

**Q: Where can I install software from?**
A: Only from the Self-Service Portal or through a HelpPoint request.

## 14. Related documents and references

- IT-GDL-002 Identity, Password and Access Management Guideline
- IT-GDL-003 Information Security Incident Reporting and Response Guideline
- IT-GDL-004 Data Classification, Handling and Retention Guideline
- IT-GDL-005 AI Assistant and Generative AI Usage Guideline
- HR-POL-002 Hybrid Work and Attendance Policy; HR-POL-005 Employee Conduct and Disciplinary Policy
- ONB-003 IT and Access Provisioning for New Joiners

## 15. Revision history

| Version | Date | Change |
|---|---|---|
| 2.0 | 2024-04-01 | Added BYOD rules for email and chat |
| 3.0 | 2026-04-01 | Added generative AI section and removable-storage exception process |
