---
doc_id: IT-GDL-005
title: AI Assistant and Generative AI Usage Guideline
category: IT Guidelines
department: Information Technology
doc_type: guideline
version: "1.2"
status: approved
effective_date: 2026-04-01
review_date: 2027-03-31
owner: CIO (Sanjay Kulkarni)
approver: CISO (Farhan Siddiqui)
sensitivity: internal
allowed_roles: [employee, hr, it, finance, marketing, project_manager, product_manager]
applies_to: All employees and contractors who use the internal AI knowledge assistant or any generative AI tool for work
related_docs: [IT-GDL-001, IT-GDL-002, IT-GDL-004, OPS-002, OPS-005, CMP-003]
source_reference: Fictional academic sample guideline for Veltrix Systems Pvt. Ltd.
contradiction_example: false
conflicts_with: []
---

# AI Assistant and Generative AI Usage Guideline

## 1. Purpose

Veltrix provides an internal AI knowledge assistant that answers questions using company documents, explains business rules, guides people through workflows and supports decisions with evidence. Generative AI can save a great deal of time, but it can also be wrong, it can expose data if used carelessly, and it can be manipulated. This guideline explains how the assistant works, what it may and may not be used for, how its access controls protect information, and how employees should use public generative AI tools.

## 2. Scope

The guideline applies to the internal AI knowledge assistant and to any external generative AI service (chatbots, writing assistants, code assistants, image generators) used for Veltrix work, on any device.

## 3. How the internal assistant works

The assistant uses retrieval-augmented generation (RAG). When you ask a question:
1. The assistant identifies your **role from the identity provider** (IT-GDL-002).
2. It searches the company document library, **only among documents your role is permitted to read**.
3. It passes the most relevant passages to a language model, which writes an answer based on those passages.
4. It shows the **source documents and sections** it used, so you can check the answer.

Because access is filtered before retrieval, the assistant cannot use a document you are not allowed to see, even if your question mentions it. If the answer requires such a document, the assistant replies that it cannot share that information with your role and suggests contacting the owning team. It will not reveal the title or content of documents outside your access.

## 4. Approved uses

The assistant may be used to:
- find and explain company policies, procedures and rules;
- guide you step by step through a workflow, such as submitting an expense claim or requesting access;
- summarise long documents you have access to;
- compare options against a framework (for example the approval levels in the Delegation of Authority, OPS-002);
- draft internal emails, documents and meeting notes;
- answer questions about Confidential data that your role can access.

## 5. Decision support, not decision making

The assistant **supports decisions; it does not approve spend, hires, terminations, access requests or changes**. Approvals always follow the Delegation of Authority (OPS-002) and the relevant policy, and must be made by the accountable person in the proper system (for example BuyRight for purchases or PeopleHub for leave).

For decisions that significantly affect a person, such as hiring, performance ratings, disciplinary outcomes or terminations, the assistant may be used only to find the relevant rules; it must not be asked to evaluate or rank individuals.

## 6. Checking answers

AI answers can be incomplete or wrong. Before acting on an answer that matters:
- open the cited source and confirm the relevant section;
- check the document's version, status and effective date;
- if the answer has no source, treat it as unverified;
- report wrong answers with the thumbs-down button and a short comment, so the knowledge team can fix the content or the system.

### 6.1 Asking good questions

The assistant gives better answers when questions are specific. Include the situation, the amount or dates involved and what you need to decide. For example, instead of "travel rules?", ask "What is the hotel limit for a two-night business trip to Bengaluru, and who approves it?". For workflows, ask for the steps in order ("What are the steps to request access to the finance system?"). For decisions, ask the assistant to list the rule, the threshold and the approver, and to cite the source of each. If an answer seems to miss your situation, add the missing detail rather than repeating the same question.

## 7. Conflicting information

Sometimes two documents appear to say different things, for example an old memo and a current policy. The assistant is designed to prefer the **latest approved version** of a policy, following the precedence rules in the Document Control and Policy Management Procedure (OPS-005), and to point out the conflict instead of hiding it. Drafts, superseded versions, regional memos that were never approved, and wiki pages are **not authoritative**. If you find a conflict, report it to the policy owner named in the document so it can be corrected.

## 8. Prohibited uses

You must not:
- try to make the assistant reveal information outside your access, for example by claiming to be another role, asking it to "ignore previous instructions", or hiding instructions inside uploaded documents;
- upload documents to the assistant that you are not permitted to share;
- use the assistant's output in customer-facing material, contracts or regulatory submissions without human review and the normal approval process;
- ask the assistant for legal advice on matters that require the Legal team;
- use any AI tool to create content that is discriminatory, harassing, deceptive or that imitates a real person without consent.

Attempts to bypass access controls are treated as serious misconduct under HR-POL-005.

## 9. Public generative AI tools

- **Only Public data may be entered into public AI tools.** Internal, Confidential and Restricted information, including customer names, unreleased product details, source code and personal data, must never be entered (IT-GDL-004).
- Public AI tools may not be used to process personal data under CMP-003.
- Turn off chat history or model-training options where the tool allows it.
- New AI tools for team use must be requested through HelpPoint; IT reviews them under the vendor security assessment process before approval.

## 10. Logging and privacy

Conversations with the internal assistant are logged for security, quality improvement and audit, and the logs are kept for **90 days**. Logs are Restricted and can be reviewed only by the IT and Security teams for operational reasons, or as part of an investigation approved by the CISO and the CHRO. Company data used by the assistant is not used to train external models.

## 11. Labelling AI-generated content

Content intended for external publication (marketing material, blog posts, documentation) that was substantially drafted by AI must be reviewed by a human author, fact-checked, and approved through the usual content review process. Internal documents do not need a label, but the author remains accountable for accuracy.

## 12. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| All users | Use AI within this guideline; verify important answers; report errors and conflicts |
| Policy and document owners | Keep documents current and correctly labelled so that answers and access are accurate |
| Knowledge management team | Maintain the document library, metadata and assistant configuration; review feedback weekly |
| IT | Operate the assistant, logging and access integration |
| Security team | Test the assistant for access-control weaknesses and prompt-injection risks at least twice a year |
| CIO | Own this guideline and approve new AI capabilities |

## 13. Exceptions

Use of a public AI tool with non-Public data may be approved only where the vendor has a signed enterprise agreement that prevents training on company data and passes the security assessment. Such approvals are given by the CISO in writing and listed on the approved tools page.

## 14. Worked examples

**Example 1 - role boundary.** An employee in the employee role asks the assistant, "What are the salary bands for L5?" Salary bands are Restricted HR information. The assistant replies that it cannot share that information with the employee's role and suggests contacting HR. It does not confirm whether such a document exists.

**Example 2 - workflow assistance.** A project manager asks how to buy a Rs 3,00,000 software subscription. The assistant explains that a purchase order and three quotes are required, that the department head approves at this amount, and cites OPS-001 and OPS-002. The project manager then raises the request in BuyRight.

**Example 3 - conflict found.** A user asks about hotel limits in Pune and the assistant finds both the current Business Travel Policy and an old regional memo with a higher limit. It answers with the approved policy's limit, notes that the memo is unofficial, and cites both.

**Example 4 - public tool misuse.** A developer pastes proprietary source code into a public chatbot to debug it. This breaches the guideline because source code is Confidential. The developer should report it as an incident under IT-GDL-003.

## 15. Frequently asked questions

**Q: Can the assistant show me documents that my role cannot access?**
A: No. It searches only documents permitted for your role, and it will not reveal the title or content of others.

**Q: Can the assistant approve my purchase or leave request?**
A: No. It supports decisions, but approvals must be made by the accountable person in the proper system.

**Q: What should I do if the assistant gives an answer without a source?**
A: Treat it as unverified and check the relevant policy before acting.

**Q: How long are my conversations with the assistant kept?**
A: 90 days.

**Q: Can I use a public AI chatbot to summarise an internal report?**
A: No. Only Public data may be entered into public AI tools.

**Q: What happens when two documents conflict?**
A: The latest approved version prevails under OPS-005; drafts, memos and superseded versions are not authoritative.

## 16. Related documents and references

- IT-GDL-001 Acceptable Use of IT Resources Guideline; IT-GDL-002 Identity, Password and Access Management Guideline; IT-GDL-003 Incident Reporting and Response; IT-GDL-004 Data Classification, Handling and Retention Guideline
- OPS-002 Delegation of Authority and Approval Workflow; OPS-005 Document Control and Policy Management Procedure
- CMP-003 Data Protection and Privacy Policy

## 17. Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2025-07-01 | First release with the internal assistant pilot |
| 1.2 | 2026-04-01 | Added conflict handling, decision-support limits and prompt-injection rules |
