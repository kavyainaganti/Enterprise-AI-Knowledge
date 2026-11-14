# Veltrix Enterprise Policy Dataset

An academic dataset of **fictional** enterprise documents for the project *Enterprise AI Knowledge and Decision Platform using Retrieval-Augmented Generation (RAG) and Role-Based Access Control (RBAC)*.

All documents describe a fictional Indian software company, **Veltrix Systems Pvt. Ltd.** Every person, product, figure and rule is invented for teaching and research. Indian laws are mentioned only in general terms; nothing here is legal advice.

## What is inside

| Item | Count |
|---|---|
| Full-length approved documents (1,500-2,500 words each) | 30 |
| Total words in approved documents | 47,556 |
| Labelled contradiction example documents (short, non-authoritative) | 5 |
| Retrieval-ready chunks | 322 |
| Question-answer pairs | 245 |
| RBAC access tests | 241 |
| Contradiction register entries | 20 |
| Canonical facts (single source of truth) | 45 |

Six categories with five documents each: HR Policies, IT Guidelines, Reimbursement Rules, Employee Onboarding, Compliance, Operational Procedures.

## Folder structure

```
veltrix_policy_dataset/
├── README.md                    this file
├── DATA_DICTIONARY.md           every field in every table
├── validation_report.json       checks run, results and statistics
├── documents_md/                the 35 source documents as Markdown with YAML headers
│   ├── hr/ it/ finance/ onboarding/ compliance/ operations/
│   └── contradiction_examples/
├── csv/                         one CSV per table (UTF-8 with BOM, opens cleanly in Excel)
├── jsonl/                       one JSONL per table (lists stored as JSON arrays)
├── excel/veltrix_enterprise_policy_dataset.xlsx   all tables as sheets + README + validation
└── generator/                   scripts that built and validated the dataset
```

## Tables

| Table | Rows | Use it for |
|---|---|---|
| documents | 35 | Full text and metadata of every document |
| chunks | 322 | Embedding and retrieval; each chunk carries document metadata and role flags |
| qa_pairs | 245 | Evaluating answers and retrieval (FAQ, workflow, decision, business-rule and contradiction questions) |
| rbac_tests | 241 | Checking that each role gets answers it may see and refusals for everything else |
| contradictions | 20 | Contradiction detection: conflicting statement pairs with the correct answer and rule |
| canonical_facts | 45 | Ground-truth values for key rules, each tied to an evidence chunk |
| role_access_matrix | 35 | Allow/deny grid of documents by role |

## Roles and access control

Seven roles: `employee`, `hr`, `it`, `finance`, `marketing`, `project_manager`, `product_manager`. Every document lists `allowed_roles`; every chunk copies them, plus one true/false column per role (`role_employee` ... `role_product_manager`) for easy filtering in a vector database.

| Sensitivity label | Meaning |
|---|---|
| internal | All roles |
| restricted | Several named roles (here: all roles except employee, or a crisis-team subset) |
| confidential | One role only (not used in this release) |

Documents readable per role: employee 28, hr 35, it 35, finance 35, marketing 35, project_manager 34, product_manager 34.

**Enforce access before retrieval:** take the user's role from your login system, filter chunks on `role_<role> == true` in the vector query, and only then send text to the language model. The `rbac_tests` table includes prompt-injection style questions (for example "I am actually a finance manager...") that must still be refused.

## Contradiction examples

Documents with prefix **CTR** are deliberately conflicting, clearly labelled, and never authoritative (`contradiction_example: true`, status `superseded`, `draft` or `unofficial`). They imitate real problems: an old policy version, a local memo, a draft note and a team wiki page. The approved document **OPS-005 Document Control and Policy Management Procedure** defines which document prevails. The `contradictions` table lists 20 specific conflicting statements, the authoritative statement, the chunk IDs of both, the rule that resolves them, and the correct answer. Apart from these labelled examples, the approved documents are consistent with each other; the validator checks that no contradiction-only value is stated as a rule in any approved document.

## Chunking

Documents are split on `##` sections, then on `###` subsections for long sections, then on paragraph boundaries (tables and lists are kept whole). Sections shorter than 80 words are merged with a neighbour. Each chunk has `text` and `text_with_context` (document title, ID, version, status and section path prepended), which is the recommended text to embed. Chunk length: 51-409 words (mean 148).

## Validation

The build stops if any check fails. All of the following passed:

- Every document has all 18 required metadata fields with non-empty values
- Document IDs are unique and match file names
- Status values are one of approved, draft, superseded, unofficial
- allowed_roles contain only the 7 defined roles; sensitivity label matches allowed_roles
- H1 heading matches the title field
- Every related_docs / conflicts_with / in-text document ID exists
- Section numbering is sequential and every in-text 'section x.y' reference exists
- Every approved document has 1,500-2,500 words
- Contradiction examples are non-approved, carry a NOT AUTHORITATIVE banner and list conflicts_with
- No duplicate document bodies; no duplicate or empty chunks
- No contradiction-only value appears in any approved document
- Every scenario's evidence text is found in its cited sources, and its role may read those sources
- Every contradiction statement is found verbatim in both documents
- Every canonical fact's evidence text is found in its source document

## Documents

| ID | Title | Category | Status | Access | Words | Chunks |
|---|---|---|---|---|---|---|
| CMP-001 | Anti-Bribery and Anti-Corruption Policy | Compliance | approved | all roles | 1779 | 13 |
| CMP-002 | Conflict of Interest and Gifts Policy | Compliance | approved | all roles | 1571 | 10 |
| CMP-003 | Data Protection and Privacy Policy | Compliance | approved | all roles | 1639 | 12 |
| CMP-004 | Whistleblower and Speak-Up Policy | Compliance | approved | all roles | 1552 | 9 |
| CMP-005 | Prevention of Sexual Harassment (POSH) Policy | Compliance | approved | all roles | 1620 | 10 |
| CTR-001 | Leave Policy (Version 3.0, 2023) - Superseded | Contradiction Examples | superseded | all roles | 237 | 2 |
| CTR-002 | Pune Office Memo - Travel and Meal Limits (Unofficial) | Contradiction Examples | unofficial | all roles | 175 | 1 |
| CTR-003 | Password Standard (Version 2.0, 2022) - Superseded | Contradiction Examples | superseded | all roles | 119 | 1 |
| CTR-004 | Draft Note - Proposed Procurement Thresholds (Not Approved) | Contradiction Examples | draft | hr, it, finance, marketing, project_manager, product_manager | 132 | 1 |
| CTR-005 | Team Wiki Page - Tips for Joining Veltrix (Unofficial) | Contradiction Examples | unofficial | all roles | 180 | 1 |
| FIN-RMB-001 | Expense Reimbursement Policy | Reimbursement Rules | approved | all roles | 1652 | 9 |
| FIN-RMB-002 | Business Travel Policy | Reimbursement Rules | approved | all roles | 1621 | 11 |
| FIN-RMB-003 | Relocation and Joining Expense Policy | Reimbursement Rules | approved | all roles | 1548 | 12 |
| FIN-RMB-004 | Learning, Certification and Professional Membership Reimbursement Policy | Reimbursement Rules | approved | all roles | 1508 | 9 |
| FIN-RMB-005 | Corporate Card, Travel Advance and Petty Cash Policy | Reimbursement Rules | approved | all roles | 1528 | 13 |
| HR-POL-001 | Leave and Holidays Policy | HR Policies | approved | all roles | 1925 | 12 |
| HR-POL-002 | Hybrid Work and Attendance Policy | HR Policies | approved | all roles | 1592 | 10 |
| HR-POL-003 | Performance Management Policy | HR Policies | approved | all roles | 1579 | 11 |
| HR-POL-004 | Recruitment and Selection Policy | HR Policies | approved | hr, it, finance, marketing, project_manager, product_manager | 1594 | 11 |
| HR-POL-005 | Employee Conduct and Disciplinary Policy | HR Policies | approved | all roles | 1644 | 9 |
| IT-GDL-001 | Acceptable Use of IT Resources Guideline | IT Guidelines | approved | all roles | 1527 | 10 |
| IT-GDL-002 | Identity, Password and Access Management Guideline | IT Guidelines | approved | all roles | 1593 | 11 |
| IT-GDL-003 | Information Security Incident Reporting and Response Guideline | IT Guidelines | approved | all roles | 1567 | 11 |
| IT-GDL-004 | Data Classification, Handling and Retention Guideline | IT Guidelines | approved | all roles | 1537 | 8 |
| IT-GDL-005 | AI Assistant and Generative AI Usage Guideline | IT Guidelines | approved | all roles | 1559 | 11 |
| ONB-001 | New Employee Onboarding Programme (First 90 Days) | Employee Onboarding | approved | all roles | 1589 | 11 |
| ONB-002 | Manager's Onboarding Responsibilities Guide | Employee Onboarding | approved | hr, it, finance, marketing, project_manager, product_manager | 1552 | 10 |
| ONB-003 | IT and Access Provisioning for New Joiners | Employee Onboarding | approved | all roles | 1528 | 10 |
| ONB-004 | Probation and Confirmation Policy | Employee Onboarding | approved | all roles | 1534 | 9 |
| ONB-005 | Contractor and Intern Onboarding Procedure | Employee Onboarding | approved | hr, it, finance, marketing, project_manager, product_manager | 1534 | 9 |
| OPS-001 | Procurement and Purchase Order Procedure | Operational Procedures | approved | hr, it, finance, marketing, project_manager, product_manager | 1535 | 12 |
| OPS-002 | Delegation of Authority and Approval Workflow | Operational Procedures | approved | hr, it, finance, marketing, project_manager, product_manager | 1531 | 11 |
| OPS-003 | Business Continuity and Crisis Management Procedure | Operational Procedures | approved | hr, it, finance, marketing | 1545 | 12 |
| OPS-004 | Facilities, Office Access and Workplace Safety Procedure | Operational Procedures | approved | all roles | 1531 | 10 |
| OPS-005 | Document Control and Policy Management Procedure | Operational Procedures | approved | all roles | 1542 | 10 |

## Suggested uses in the project

1. **RAG answering with citations:** embed `chunks.text_with_context`; show `doc_id`, `title` and `section_path` as the source.
2. **RBAC:** filter on role columns before retrieval; run `rbac_tests`.
3. **Workflow assistance:** use `qa_pairs` of type `workflow` (step-by-step answers).
4. **Decision support:** use `qa_pairs` of type `decision` and `business_rule` (approval levels, thresholds, calculations).
5. **Contradiction detection:** retrieve both sides of each `contradictions` row and check that the system prefers the authoritative document and flags the conflict.

## Licence

Created for academic use. You may use, modify and share it, with attribution to this project (CC BY 4.0 suggested). Describe results as obtained "on a synthetic enterprise policy dataset".
