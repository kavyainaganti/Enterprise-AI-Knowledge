---
doc_id: IT-GDL-004
title: Data Classification, Handling and Retention Guideline
category: IT Guidelines
department: Information Technology
doc_type: guideline
version: "2.0"
status: approved
effective_date: 2026-04-01
review_date: 2027-03-31
owner: CISO (Farhan Siddiqui)
approver: CIO (Sanjay Kulkarni)
sensitivity: internal
allowed_roles: [employee, hr, it, finance, marketing, project_manager, product_manager]
applies_to: All information created, received or held by Veltrix in any format
related_docs: [IT-GDL-001, IT-GDL-002, IT-GDL-003, IT-GDL-005, CMP-003, HR-POL-004, OPS-004, OPS-005]
source_reference: Fictional academic sample guideline for Veltrix Systems Pvt. Ltd.; retention periods are illustrative and refer in general terms to the Companies Act, 2013 and the Digital Personal Data Protection Act, 2023
contradiction_example: false
conflicts_with: []
---

# Data Classification, Handling and Retention Guideline

## 1. Purpose

Not all information needs the same protection. A published blog post can be shared with anyone, while salary data or a customer's database must be tightly controlled. This guideline gives every employee a simple four-level scheme for classifying information, explains how each level must be stored, shared and destroyed, and sets out how long common types of records are kept. Applying it consistently protects customers and colleagues, keeps Veltrix compliant, and makes systems such as the AI knowledge assistant safer, because access rules depend on correct labels.

## 2. Scope

The guideline covers information in every form: documents, spreadsheets, emails, chat messages, database records, source code, recordings, printed paper and information held by vendors on Veltrix's behalf.

## 3. The four classification levels

| Level | Meaning | Typical examples |
|---|---|---|
| **Public** | Approved for release to anyone | Website content, published blog posts, press releases, public job adverts |
| **Internal** | For use inside the company; low harm if leaked | Most policies, the org chart, internal announcements, holiday calendar |
| **Confidential** | Could harm customers or the company if leaked; shared on a need-to-know basis | Customer data, financial reports, project plans, contracts, product roadmaps, source code |
| **Restricted** | Severe harm if leaked; named individuals only | Salary and bank details, passwords and keys, investigation files, board papers, identity documents, health information |

When in doubt, choose the higher level and ask the information owner.

### 3.1 Who classifies

The person who creates or receives information is responsible for classifying it. The information owner (usually the head of the function that holds it) may reclassify it. Information is Internal by default unless marked otherwise.

### 3.2 Labels in the document library

Documents in the company policy library and the AI knowledge assistant carry a sensitivity label in their metadata. The labels map to the classification levels as follows:

| Metadata label | Classification level | Access |
|---|---|---|
| internal | Internal | All roles |
| restricted | Confidential | Owner role plus named other roles |
| confidential | Restricted | Owner role only |

The metadata labels are used by the access-control system; the classification levels are used in day-to-day language. Both refer to the same scheme.

## 4. Handling rules

| Action | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Store | Anywhere | Company systems | Company systems with access controls | Approved systems only; access logged |
| Share internally | Freely | Freely | Need to know | Named individuals approved by the owner |
| Share externally | Freely | Not without owner approval | Only under a signed NDA, via approved file sharing | Only with CISO and owner approval, encrypted |
| Email | Allowed | Internal recipients | Internal or NDA recipients; check addresses twice | Encrypted email or secure link only |
| Print | Allowed | Allowed | Collect immediately; no printing at home | Avoid; if essential, collect immediately and shred after use |
| Personal devices | Allowed | Only via managed apps | Not allowed | Not allowed |
| Public AI tools | Allowed | Not allowed | Not allowed | Not allowed |
| Disposal | Normal | Normal deletion | Secure deletion; paper in shredding bins | Secure deletion with record; paper shredded |

Note that only Public data may be entered into public AI tools; this rule is repeated in IT-GDL-001 and IT-GDL-005.

### 4.1 Quick reference for common items

| Item | Classification | Reason |
|---|---|---|
| This guideline and most company policies | Internal | Useful only inside the company; low harm if leaked |
| Team meeting notes | Internal | Unless they discuss customers, finances or people issues |
| A customer's support ticket with user names | Confidential | Contains customer and personal data |
| Monthly management P&L | Confidential | Financial information not yet public |
| Signed customer contract | Confidential | Commercial terms |
| Employee salary or bank details | Restricted | Sensitive personal and financial data |
| HR investigation report | Restricted | Highly sensitive personal information |
| Production database credentials | Restricted | Gives access to customer data |
| Approved press release after publication | Public | Already released |

Classification can change over time. A press release is Internal while in draft and becomes Public only when it is published; financial results become Public only after the company announces them.

## 5. Personal data

Personal data about employees, candidates and customers' users is at least Confidential. Sensitive personal data such as health information, bank details, identity numbers and biometric data is Restricted. Collecting, using and sharing personal data must also follow the Data Protection and Privacy Policy (CMP-003), which requires a lawful purpose and limits use to that purpose.

## 6. Retention schedule

Information must be kept for as long as it is needed for its purpose or required by law, and then securely deleted. The table below sets standard periods. Where a law requires a longer period, the law prevails.

| Record type | Retention period | Owner |
|---|---|---|
| Accounting records, invoices, vouchers | **8 years** after the end of the financial year | Finance |
| Employee personnel file, including disciplinary records | **7 years** after the employee leaves | HR |
| Payroll records | 8 years after the end of the financial year | Finance (Payroll) |
| Background verification reports | **2 years** after the employee leaves | HR |
| Unsuccessful candidate data | **12 months** after the hiring decision (HR-POL-004) | HR |
| Customer data in production systems | Deleted **within 90 days** of contract end, unless the contract says otherwise | Product / Engineering |
| Contracts | 8 years after expiry | Legal |
| Mailboxes of leavers | Archived for **3 years**, then deleted | IT |
| System and security logs | **1 year** | IT / Security |
| AI knowledge assistant conversation logs | **90 days** (IT-GDL-005) | IT |
| Backups | **35 days**; monthly copies kept for 12 months | IT |
| CCTV footage | **30 days** (OPS-004) | Facilities |
| Visitor logs | 1 year | Facilities |
| Superseded policies | 7 years after supersession, marked as superseded (OPS-005) | Policy owner |

### 6.1 Legal hold

When Legal issues a legal hold (for example because of a dispute or investigation), the affected records must not be deleted even if their retention period has ended. The hold overrides this schedule until Legal lifts it in writing.

### 6.2 Deletion

Deletion must be secure: electronic records are deleted using the system's standard deletion, with cloud storage set to permanently purge after the retention period; devices are wiped to the NIST 800-88 standard before reuse or disposal; paper is placed in locked shredding bins. Deletion of Restricted records is recorded in a deletion log.

## 7. Data owners and custodians

- **Information owner:** decides the classification, approves access and external sharing, and confirms retention.
- **Custodian (usually IT):** operates the systems that store the information and applies the technical controls.
- **User:** handles the information according to its classification.

## 8. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| All employees | Classify what they create; handle information according to the rules in section 4 |
| Information owners | Approve access and external sharing; review classification annually |
| IT | Provide storage, encryption, backup and deletion capabilities; apply labels in systems |
| Security team | Monitor for data leakage; approve Restricted external sharing with the owner |
| Legal | Issue and lift legal holds; advise on statutory retention |
| Data Protection Officer | Oversee personal data handling under CMP-003 |

## 9. Exceptions

Exceptions to handling rules (for example sending Restricted data to a regulator through a channel they require) must be approved in advance by the CISO and the information owner and recorded in the security exception register.

## 10. Worked examples

**Example 1 - roadmap to a partner.** A product manager wants to send the product roadmap (Confidential) to an implementation partner. This is allowed only if a signed NDA is in place, and only through the approved file-sharing tool with link expiry.

**Example 2 - salary sheet.** An HR analyst needs to send a salary file (Restricted) to the payroll vendor. This requires owner and CISO approval and an encrypted channel; the analyst must not attach it to a normal email.

**Example 3 - candidate CV from last year.** A recruiter finds CVs of unsuccessful candidates from 14 months ago in a shared folder. These have passed the 12-month retention period and must be deleted unless the candidates agreed to longer retention.

**Example 4 - public AI tool.** A marketer wants to paste a draft press release (not yet published, so Internal) into a public AI tool to improve the wording. This is not allowed; only Public data may be used. The internal AI assistant can be used instead.

## 11. Frequently asked questions

**Q: What are the four classification levels?**
A: Public, Internal, Confidential and Restricted.

**Q: Is customer data Confidential or Restricted?**
A: Customer data is at least Confidential; sensitive items such as identity numbers or health data are Restricted.

**Q: How long are accounting records kept?**
A: 8 years after the end of the financial year.

**Q: How long are employee records kept after someone leaves?**
A: 7 years, except background verification reports, which are kept for 2 years.

**Q: How long are AI assistant conversation logs kept?**
A: 90 days.

**Q: What happens to records under legal hold?**
A: They must not be deleted until Legal lifts the hold, even if the retention period has ended.

**Q: What does the "restricted" label in document metadata mean?**
A: It corresponds to the Confidential level: the owner role and named other roles can access it.

## 12. Related documents and references

- IT-GDL-001 Acceptable Use of IT Resources Guideline; IT-GDL-002 Identity, Password and Access Management Guideline; IT-GDL-003 Incident Reporting and Response; IT-GDL-005 AI Assistant and Generative AI Usage Guideline
- CMP-003 Data Protection and Privacy Policy
- HR-POL-004 Recruitment and Selection Policy
- OPS-004 Facilities, Office Access and Workplace Safety Procedure
- OPS-005 Document Control and Policy Management Procedure
- External: Companies Act, 2013 (books of account); Digital Personal Data Protection Act, 2023

## 13. Revision history

| Version | Date | Change |
|---|---|---|
| 1.3 | 2024-04-01 | Four-level classification introduced |
| 2.0 | 2026-04-01 | Retention schedule merged into this guideline; metadata label mapping added |
