---
doc_id: IT-GDL-002
title: Identity, Password and Access Management Guideline
category: IT Guidelines
department: Information Technology
doc_type: guideline
version: "3.1"
status: approved
effective_date: 2026-04-01
review_date: 2027-03-31
owner: CISO (Farhan Siddiqui)
approver: CIO (Sanjay Kulkarni)
sensitivity: internal
allowed_roles: [employee, hr, it, finance, marketing, project_manager, product_manager]
applies_to: All users of Veltrix systems and all system owners
related_docs: [IT-GDL-001, IT-GDL-003, IT-GDL-004, IT-GDL-005, ONB-003, ONB-005, OPS-005]
source_reference: Fictional academic sample guideline for Veltrix Systems Pvt. Ltd.; password rules follow the general direction of modern guidance such as NIST SP 800-63B (length over complexity, no routine forced rotation)
contradiction_example: false
conflicts_with: []
---

# Identity, Password and Access Management Guideline

## 1. Purpose

Most security breaches start with a stolen or misused identity. This guideline sets the rules for passwords, multi-factor authentication (MFA), how access to systems is requested, granted, changed and removed, and how privileged access is controlled. It also explains how role-based access control (RBAC) works across Veltrix systems, including the internal AI knowledge assistant, so that every person sees the information their role requires and nothing more.

## 2. Scope

The guideline covers all user accounts, administrator accounts and service accounts on Veltrix systems, whether hosted in the company's cloud environment or provided by a software-as-a-service vendor. It applies to employees, contractors and interns, and to system owners who approve access.

## 3. Definitions

- **Identity provider (IdP):** the central system that holds user identities and provides single sign-on (SSO) to company applications.
- **System owner:** the manager accountable for a business application, for example the Finance Controller for the finance system.
- **Role:** a named set of access rights linked to a job function, such as *employee*, *hr*, *finance* or *project_manager*.
- **Privileged access:** administrator or other elevated rights that can change system configuration or access all data.
- **Joiner, mover, leaver:** the three events that change a person's access needs.

## 4. Password and authentication standard

| Control | Requirement |
|---|---|
| Minimum password length | **14 characters** |
| Multi-factor authentication | **Mandatory for all systems**, including email, VPN and every SSO application |
| Account lockout | After **5 failed attempts**; the account unlocks automatically after 15 minutes or through the IT Service Desk |
| Screen lock | Automatic after **5 minutes** of inactivity |
| Password change | **No forced periodic change**; change immediately if compromise is suspected |
| Password storage | Only in the company password manager |
| Reuse | The company password must not be used on any other website or service |

### 4.1 Why length instead of complexity

Long passphrases are both easier to remember and harder to crack than short complex passwords. A passphrase of four or more unrelated words, such as "copper lantern monsoon violin", meets the standard. The IdP checks new passwords against lists of known breached passwords and rejects them.

### 4.2 Why no routine rotation

Forcing regular password changes tends to produce predictable patterns (for example adding a number each quarter). Veltrix therefore does not require routine changes. Instead, the IdP monitors for unusual sign-ins, and users must change their password immediately if they suspect it has been exposed.

### 4.3 MFA methods

The approved MFA methods are the company authenticator app with number matching, and hardware security keys. SMS codes are not accepted except as a temporary fallback for up to 7 days while a replacement phone is set up. Never approve an MFA prompt you did not start; report it as a suspected incident (IT-GDL-003).

## 5. Requesting access

### 5.1 Default access

New employees receive default access on their first day: email, TeamTalk, PeopleHub, ExpenseDesk, HelpPoint and the internal AI knowledge assistant (with access matching their role). The provisioning steps are described in ONB-003.

### 5.2 Additional access

1. Raise a request in **HelpPoint > Request Access**, naming the system and the access level needed.
2. The **reporting manager approves first**, confirming the business need.
3. The **system owner approves second**, confirming the access level is appropriate.
4. Access to systems or data classified **Restricted** also requires **Security team approval**.
5. IT grants the access and records it against the person's identity.

Requests that do not state a business reason are returned. Access is always granted to a named individual; **shared accounts are not permitted**.

## 6. Changes and removal of access

### 6.1 Movers

When an employee changes role or team, PeopleHub notifies IT automatically. **Access tied to the old role is removed within 5 working days** unless the new manager re-approves it. Role-based access (for example the role used by the AI knowledge assistant) changes on the effective date of the move.

### 6.2 Leavers

All access is removed **within 24 hours of the last working day**, triggered by the exit record in PeopleHub. For involuntary exits, access is removed on the same day, at the time agreed between HR and IT. Email may be forwarded to the manager for up to 30 days, after which the mailbox is archived under IT-GDL-004.

### 6.3 Long absence

Accounts of employees on leave longer than 60 days are suspended (not deleted) and re-enabled on return, unless the employee needs access during leave for an approved reason.

## 7. Privileged access

- Administrators use a **separate administrator account** that is never used for email or browsing.
- Administrator accounts require a **hardware security key**.
- Administrator credentials are checked out from the privileged access vault for a maximum of **8 hours** at a time, and every checkout is logged.
- Emergency "break-glass" accounts are stored in the vault, can be used only during a P1 incident, and trigger an automatic alert to the CISO when used.
- Privileged access is reviewed **monthly** by the CISO's team.

## 8. Access reviews

System owners review all user access to their systems **quarterly**. HelpPoint generates the review list. **Access not confirmed within 10 working days of the review is removed automatically.** The results of reviews are evidence for the company's ISO/IEC 27001 certification and annual SOC 2 audit.

## 9. Role-based access control

### 9.1 How roles are assigned

Each employee has one primary role, derived from their job in PeopleHub and synchronised to the IdP as a group. The current roles are: employee, hr, it, finance, marketing, project_manager and product_manager. Every role can also access content available to all employees.

### 9.2 RBAC in the AI knowledge assistant

The AI knowledge assistant must only retrieve documents that the signed-in user's role is permitted to read. The role is taken **from the IdP group, never from anything the user types**. A user who asks the assistant to "act as HR" or claims to be a manager does not gain any additional access. Details are in IT-GDL-005.

## 10. Service accounts

Service accounts (used by applications to talk to each other) must have a named human owner, a documented purpose and the minimum permissions required. Their credentials are stored in the secrets vault, rotated at least every 12 months or immediately after a staff change in the owning team, and must never be used for interactive sign-in.

## 11. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| All users | Follow the password standard, use MFA, request only needed access, report suspicious prompts |
| Reporting manager | Approve access requests based on need; confirm access during reviews when asked |
| System owner | Approve access levels; complete quarterly reviews on time |
| IT Service Desk | Provision and remove access; process movers and leavers |
| Security team | Approve Restricted access; review privileged access monthly; monitor sign-ins |
| HR | Keep PeopleHub records accurate, because access automation depends on them |

## 12. Exceptions

Any exception to this guideline (for example a legacy system that cannot support SSO) requires a written risk acceptance from the CISO, with a time limit and compensating controls such as network restrictions or additional monitoring. Exceptions are reviewed at least every 6 months.

## 13. Worked examples

**Example 1 - new system access.** Divya in Finance needs read access to the procurement system. She raises a HelpPoint request; her manager approves, then the procurement system owner approves. No Security approval is needed because the data is Confidential, not Restricted.

**Example 2 - team move.** On 1 July Arjun moves from Marketing to Product. His role changes to product_manager on that date, so the AI assistant immediately stops returning Marketing-only documents to him. His old LeadLoop access is removed by 8 July unless his new manager re-approves it.

**Example 3 - unexpected MFA prompt.** Pooja receives an MFA prompt at 02:00 that she did not trigger. She denies it and reports a suspected incident; Security finds her password in a third-party breach and resets it.

**Example 4 - access review.** The Finance Controller does not respond to the quarterly review for two contractors. After 10 working days their access to the finance system is removed automatically.

## 14. Frequently asked questions

**Q: How long must my password be?**
A: At least 14 characters. A passphrase of four or more unrelated words works well.

**Q: Do I have to change my password every few months?**
A: No. There is no forced periodic change, but you must change it immediately if you suspect it has been exposed.

**Q: How many failed attempts lock my account?**
A: 5 failed attempts; it unlocks after 15 minutes or through the Service Desk.

**Q: Who approves my access request?**
A: Your reporting manager first, then the system owner; Restricted data also needs Security approval.

**Q: How quickly is a leaver's access removed?**
A: Within 24 hours of the last working day, or the same day for involuntary exits.

**Q: How often are access reviews done?**
A: Quarterly by system owners; privileged access is reviewed monthly.

**Q: Can I get more information from the AI assistant by saying I am a manager?**
A: No. Access is based on your role in the identity provider, not on what you type.

## 15. Related documents and references

- IT-GDL-001 Acceptable Use of IT Resources Guideline
- IT-GDL-003 Information Security Incident Reporting and Response Guideline
- IT-GDL-004 Data Classification, Handling and Retention Guideline
- IT-GDL-005 AI Assistant and Generative AI Usage Guideline
- ONB-003 IT and Access Provisioning for New Joiners; ONB-005 Contractor and Intern Onboarding Procedure
- OPS-005 Document Control and Policy Management Procedure (superseded password standard CTR-003)
- External: NIST Special Publication 800-63B (general guidance on authenticators)

## 16. Revision history

| Version | Date | Change |
|---|---|---|
| 2.0 | 2022-01-01 | Superseded standard with 8-character passwords and 90-day rotation (see CTR-003) |
| 3.0 | 2025-04-01 | 14-character minimum, MFA everywhere, no forced rotation |
| 3.1 | 2026-04-01 | Added RBAC rules for the AI knowledge assistant |
