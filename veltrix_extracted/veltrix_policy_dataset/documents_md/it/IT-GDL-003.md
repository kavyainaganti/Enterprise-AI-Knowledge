---
doc_id: IT-GDL-003
title: Information Security Incident Reporting and Response Guideline
category: IT Guidelines
department: Information Technology
doc_type: guideline
version: "2.4"
status: approved
effective_date: 2026-04-01
review_date: 2027-03-31
owner: CISO (Farhan Siddiqui)
approver: CIO (Sanjay Kulkarni)
sensitivity: internal
allowed_roles: [employee, hr, it, finance, marketing, project_manager, product_manager]
applies_to: All employees and contractors (reporting); IT and Security teams (response)
related_docs: [IT-GDL-001, IT-GDL-002, IT-GDL-004, CMP-003, OPS-003, HR-POL-005]
source_reference: Fictional academic sample guideline for Veltrix Systems Pvt. Ltd.; refers in general terms to CERT-In incident reporting directions (2022)
contradiction_example: false
conflicts_with: []
---

# Information Security Incident Reporting and Response Guideline

## 1. Purpose

Incidents will happen in any organisation; what matters is how quickly they are noticed, reported and contained. This guideline tells every employee how to recognise and report an IT or security incident, and tells the IT and Security teams how incidents are prioritised, communicated, resolved and reviewed. Fast, honest reporting is always better than silence: **nobody is disciplined for reporting a genuine mistake promptly**, such as clicking a phishing link.

## 2. Scope

The guideline covers service incidents (systems unavailable or degraded), security incidents (threats to confidentiality, integrity or availability of information), and personal data breaches. It applies to all company systems, devices and data, including data held by vendors on the company's behalf.

## 3. What to report

Report immediately if you notice or suspect any of the following:
- a lost or stolen laptop, phone or access card;
- an email that asks for your password, payment, or urgent action and looks unusual (phishing);
- an MFA prompt you did not start;
- files that have been encrypted or renamed unexpectedly, or a ransom message;
- data sent to the wrong recipient, including emails with attachments;
- a system that is down, very slow, or behaving strangely;
- someone using another person's account or badge;
- a vendor telling you they have had a breach that may involve Veltrix data.

If you are unsure whether something is an incident, report it anyway.

## 4. How to report

| Situation | Channel |
|---|---|
| Suspected security incident, lost device, outage affecting many people | **IT hotline** (staffed 24x7) - this creates a P1 or P2 ticket |
| Phishing email | Use the **Report Phishing** button in the email client; do not forward the email |
| Other IT problems and requests | **HelpPoint** portal |
| Personal data breach | IT hotline **and** inform the Data Protection Officer (see CMP-003) |

When reporting, give your name, the system or device affected, what you saw, when it started, and what you have already done. Do not try to investigate a security incident yourself, do not delete suspicious emails or files, and do not power off an infected laptop - disconnect it from the network instead (turn off Wi-Fi) and wait for instructions.

## 5. Priority levels for IT incidents

| Priority | Definition | First response | Resolution target |
|---|---|---|---|
| P1 | Company-wide outage or security breach | **15 minutes** | **4 hours** |
| P2 | A department or critical system degraded | **1 hour** | **8 hours** |
| P3 | A single user blocked | **4 hours** | **3 business days** |
| P4 | A request or minor issue | **1 business day** | **10 business days** |

The Service Desk sets the priority based on impact and urgency, not on who reports the issue. A reporter can ask for re-prioritisation if the impact is greater than first understood. The company target is that **95% of incidents** are resolved within their resolution target each quarter.

## 6. Security incident severity

Security incidents are additionally given a severity by the Security team.

| Severity | Example | Who is notified | Deadline |
|---|---|---|---|
| SEV-1 | Confirmed breach of customer or Restricted data; ransomware | CISO, CIO, CEO and Legal | **Within 1 hour** of confirmation |
| SEV-2 | One compromised user account; malware on a single device | CISO | **Within 4 hours** |
| SEV-3 | Phishing reported but not clicked; minor policy violation | Security team queue | Next business day |

### 6.1 External reporting

Where an incident is reportable under the CERT-In directions, the Security team notifies CERT-In **within 6 hours** of detection. Notification to customers, regulators and affected individuals is decided by Legal and, for personal data, by the Data Protection Officer under CMP-003. Employees must never contact customers, regulators or the media about an incident themselves.

## 7. Response process

1. **Log and triage.** Every incident is logged in HelpPoint. For P1, the on-call engineer and IT Operations Manager are paged immediately.
2. **Communicate.** For P1 incidents, updates are posted in the TeamTalk incident channel **every 30 minutes**; for P2, **every 2 hours**. Updates say what is known, what is being done, and when the next update will come.
3. **Contain.** Isolate affected devices, disable compromised accounts, block malicious senders or addresses, and preserve evidence.
4. **Eradicate and recover.** Remove the cause, restore from clean backups where needed, and confirm normal service with affected users.
5. **Close.** The ticket is closed only after the reporter or service owner confirms resolution.
6. **Review.** P1 and P2 incidents require a **post-incident review within 5 working days**. SEV-1 and SEV-2 security incidents also require a lessons-learned review **within 10 working days**.

### 7.1 Out-of-hours incidents

Outside business hours (before 08:00 or after 20:00 IST, weekends and holidays), the IT hotline routes calls to the on-call engineer. P1 and P2 incidents are handled immediately with the same targets as during the day. P3 and P4 tickets raised out of hours are picked up at the start of the next business day, and their response clock starts then.

### 7.2 Ransomware and malware

If a laptop shows a ransom message or files are being encrypted, the user must disconnect from the network at once, leave the device powered on, and call the IT hotline. Security isolates the device through the EDR console, checks file shares for spread, and blocks related indicators across the company. Ransom payments are never made without a decision by the CEO on the advice of the CISO and Legal; the company's position is that it does not pay ransoms.

### 7.3 Customer-facing incidents

When an incident affects Veltrix Insight, Veltrix Flow or Veltrix Connect for customers, the status page is updated within 30 minutes of a P1 being declared, and Customer Success informs affected key accounts. Wording for customer communication is approved by the incident lead and, for security incidents, by Legal. A written incident summary is offered to affected customers within 5 working days of resolution.

## 8. Post-incident review

The review is blameless: its aim is to improve systems, not to find someone to punish. It records the timeline, impact, root cause, what went well, what could be improved, and preventive actions with owners and dates. Preventive actions are tracked in HelpPoint until complete. Where a review finds deliberate policy violation, the matter is referred to HR under HR-POL-005 separately from the review.

## 9. Evidence handling

Logs, disk images and relevant emails are preserved before any device is wiped. The Security team maintains chain-of-custody records for evidence that may be needed in legal proceedings. Evidence is classified Restricted and retained according to IT-GDL-004.

## 10. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| All employees | Report incidents immediately; follow instructions; preserve evidence; keep incident details confidential |
| IT Service Desk | Log, prioritise and route incidents; communicate with reporters |
| On-call engineer | Respond to P1 and P2 incidents out of hours |
| IT Operations Manager | Lead P1 incident response; chair post-incident reviews |
| Security team | Investigate security incidents; set severity; handle evidence |
| CISO | Lead SEV-1 and SEV-2 incidents; decide on CERT-In notification |
| Data Protection Officer | Assess personal data breaches and notification duties (CMP-003) |
| Legal | Decide on customer and regulator communication |

## 11. Exceptions

There are no exceptions to the duty to report. Response timelines may be varied by the CISO during a major crisis declared under the Business Continuity and Crisis Management Procedure (OPS-003), in which case the crisis management team sets communication intervals.

## 12. Worked examples

**Example 1 - phishing click.** Harsha clicks a link in an email that looked like a parcel notification and enters her password. She realises the mistake ten minutes later and calls the IT hotline. Security disables her sessions, resets her password and classifies the event as SEV-2. Because she reported promptly, no disciplinary action follows.

**Example 2 - outage.** The VPN fails at 09:20, affecting about 300 remote users. The Service Desk logs a P1. First response must happen by 09:35 and resolution is targeted by 13:20. Updates are posted every 30 minutes.

**Example 3 - wrong recipient.** Manish emails a spreadsheet of customer contact details to the wrong external address. This is a potential personal data breach: he calls the IT hotline and informs the Data Protection Officer, and does not contact the recipient himself.

**Example 4 - single user.** Lata cannot open ExpenseDesk but colleagues can. This is a P3: first response within 4 hours, resolution within 3 business days.

## 13. Frequently asked questions

**Q: Will I get into trouble for reporting that I clicked a phishing link?**
A: No. Prompt reporting of genuine mistakes is never disciplined.

**Q: What is the response time for a P1 incident?**
A: First response within 15 minutes and resolution targeted within 4 hours.

**Q: What should I do with a suspicious email?**
A: Use the Report Phishing button; do not forward or delete it.

**Q: Should I switch off an infected laptop?**
A: No. Disconnect it from the network and wait for instructions.

**Q: How soon must CERT-In be notified of a reportable incident?**
A: Within 6 hours of detection, by the Security team.

**Q: When is a post-incident review required?**
A: For every P1 and P2 incident, within 5 working days.

**Q: How often are updates posted during a P1?**
A: Every 30 minutes in the TeamTalk incident channel.

## 14. Related documents and references

- IT-GDL-001 Acceptable Use of IT Resources Guideline
- IT-GDL-002 Identity, Password and Access Management Guideline
- IT-GDL-004 Data Classification, Handling and Retention Guideline
- CMP-003 Data Protection and Privacy Policy
- OPS-003 Business Continuity and Crisis Management Procedure
- HR-POL-005 Employee Conduct and Disciplinary Policy
- External: CERT-In directions on cyber incident reporting (2022)

## 15. Revision history

| Version | Date | Change |
|---|---|---|
| 2.0 | 2024-04-01 | Combined service and security incident guidance |
| 2.4 | 2026-04-01 | Added personal data breach reporting and blameless review principle |
