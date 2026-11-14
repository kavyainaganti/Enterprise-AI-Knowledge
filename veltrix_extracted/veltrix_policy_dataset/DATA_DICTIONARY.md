# Data Dictionary

Lists (roles, related documents, sources) are separated by `;` in CSV and Excel, and stored as JSON arrays in JSONL.

## documents

| Field | Description |
|---|---|
| doc_id | Unique ID: prefix (HR-POL, IT-GDL, FIN-RMB, ONB, CMP, OPS, CTR) + 3 digits |
| title | Document title (matches the H1 heading) |
| category | One of the six categories, or Contradiction Examples |
| department | Owning department |
| doc_type | policy, guideline, procedure, guide, standard, memo or wiki |
| version | Version number (major.minor) |
| status | approved (authoritative), draft, superseded or unofficial |
| effective_date / review_date | ISO dates |
| owner / approver | Accountable owner and approving authority |
| sensitivity | internal (all roles), restricted (several roles), confidential (one role) |
| allowed_roles | Roles that may retrieve the document |
| role_<role> | true/false flag per role |
| applies_to | Who the document applies to |
| related_docs | Related document IDs (all validated to exist) |
| conflicts_with | For CTR documents, the approved documents they contradict |
| contradiction_example | true for labelled contradiction examples |
| source_reference | Provenance note (fictional sample; general legal references) |
| source_file | Path of the Markdown source |
| word_count | Words in the body (alphanumeric tokens) |
| chunk_count | Number of chunks produced |
| full_text | Full Markdown body |

## chunks

| Field | Description |
|---|---|
| chunk_id | `<doc_id>-C<nnn>` |
| doc_id, chunk_index | Parent document and position |
| section_path | Section heading(s) the chunk comes from; ` > ` = subsection, ` | ` = merged sections |
| chunk_type | overview, definition, policy_rule, procedure, responsibilities, exception, example, faq, references, revision_history |
| text | Chunk text (Markdown) |
| text_with_context | Text prefixed with document title, ID, version, status and section (recommended for embedding) |
| word_count, char_count, token_estimate | Size measures (tokens estimated as characters / 4) |
| prev_chunk_id, next_chunk_id | Neighbouring chunks for context expansion |
| title ... source_reference | Copied from the parent document |
| allowed_roles, role_<role> | Access control copied from the parent document |

## qa_pairs

| Field | Description |
|---|---|
| qa_id | `QA-nnnn` |
| qa_type | faq, workflow, decision, business_rule, contradiction |
| role | Role the question is asked as |
| question, expected_answer | Question and reference answer |
| source_doc_ids | Documents that contain the answer |
| answer_chunk_id | For FAQ items, the FAQ chunk containing the answer verbatim |
| evidence_chunk_id | Supporting non-FAQ chunk(s). For scenarios: chunks containing the validated evidence text. For FAQ items: auto-matched by word and number overlap (spot-check before relying on it) |
| allowed_roles | Roles permitted to see all sources |
| expected_behaviour | answer |

## rbac_tests

| Field | Description |
|---|---|
| test_id | `RBAC-nnnn` |
| role | Role of the user asking |
| question | Question to ask |
| source_doc_ids | Document needed to answer |
| expected_result | answer or deny |
| reason | Why |

## contradictions

| Field | Description |
|---|---|
| conflict_id | `C-nn` |
| topic | What the conflict is about |
| non_authoritative_doc / _status / _statement / _chunk_id | The CTR side of the conflict |
| authoritative_doc / _statement / _chunk_id | The approved side |
| resolution_rule | Precedence rule from OPS-005 that resolves it |
| correct_answer | The answer a system should give |

## canonical_facts

| Field | Description |
|---|---|
| fact_id | `F-nnn` |
| topic, value | The rule and its correct value |
| source_doc_id, evidence_text, evidence_chunk_id | Where the value is stated (validated) |

## role_access_matrix

One row per document with `allow` / `deny` for each of the seven roles.
