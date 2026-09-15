# AI Architecture RACI — Reference Operating Model

Status: **DESIGNED — REFERENCE RACI / ADAPT TO ORGANIZATION**

Purpose: clarify accountability across business, architecture, data, security, platform, model/AI engineering, operations and governance. Titles vary by organization; responsibilities are the important part.

Roles:

- **BO** — Business Owner / Product Owner
- **SA** — AI Solution Architect
- **EA** — Enterprise Architect / Design Authority
- **DATA** — Data/Knowledge Owner or Data Architect
- **SEC** — Cybersecurity / IAM / Privacy
- **AIENG** — AI/ML/GenAI Engineering
- **PLAT** — Cloud/OpenShift/AI Platform Engineering
- **OPS** — SRE / Operations / Run
- **RISK** — Risk / Compliance / Legal / Responsible AI governance
- **FIN** — FinOps / Procurement where applicable

Legend: `R` Responsible, `A` Accountable, `C` Consulted, `I` Informed.

| Activity / Decision | BO | SA | EA | DATA | SEC | AIENG | PLAT | OPS | RISK | FIN |
|---|---|---|---|---|---|---|---|---|---|---|
| Define business outcome / KPI | A/R | C | I | C | I | I | I | I | C | C |
| Decide whether AI is justified | A | R | C | C | C | C | I | I | C | C |
| Select architecture pattern | C | A/R | C | C | C | C | C | C | C | C |
| Define FR/NFR | C | A/R | C | C | C | C | C | C | C | C |
| Define target architecture | I | A/R | C | C | C | C | C | C | C | I |
| Approve architecture | I | R | A | C | C | I | I | I | C | I |
| Define data classification / residency | C | C | C | A/R | C | I | I | I | C | I |
| Define corpus / knowledge governance | C | C | I | A/R | C | C | I | I | C | I |
| Approve provider/model eligibility | I | R | C | C | C | C | C | I | A/C | C |
| Model selection/evaluation methodology | C | A | I | C | C | R | C | C | C | C |
| Prompt/RAG/agent design | I | A | I | C | C | R | C | C | C | I |
| AI Gateway / policy architecture | I | A/R | C | C | R | C | C | C | C | I |
| IAM / authorization / secrets | I | C | I | I | A/R | C | C | C | C | I |
| HITL policy for sensitive actions | A/C | R | C | I | C | C | I | C | A/C | I |
| Threat model / security assessment | I | C | I | C | A/R | C | C | C | C | I |
| Privacy / Responsible AI assessment | C | C | I | C | C | C | I | I | A/R | I |
| Model/data/license review | I | C | I | C | C | R/C | I | I | A/C | C |
| Platform/runtime selection | I | A/C | I | I | C | C | R | C | I | C |
| Capacity/performance budget | I | A | I | I | I | C | R | C | I | C |
| FinOps budget / showback | C | C | I | I | I | C | C | I | I | A/R |
| Evaluation acceptance criteria | A/C | R | I | C | C | R | I | C | C | I |
| Go-live readiness | C | R | A/C | C | C | C | C | R | C | C |
| Operational SLO / alert / runbook | I | C | I | I | C | C | C | A/R | I | I |
| Incident response ownership | I | C | I | I | C | C | C | A/R | C | I |
| Model/prompt/index rollback | I | C | I | C | C | R | C | A/C | I | I |
| Risk acceptance | C | C | C | C | C | C | C | C | A | I |
| Retirement / deletion | A/C | R | C | A/C | C | C | C | R | C | I |

## AI Solution Architect responsibilities

The SA is not expected to personally implement every component. The SA is expected to:

1. translate business capability into architecture requirements;
2. select and justify patterns;
3. own the coherent end-to-end solution design;
4. identify NFRs, constraints and risks;
5. define interfaces and boundaries across data/model/platform/security/operations;
6. make trade-offs explicit through ADRs;
7. identify where POC evidence is actually required;
8. ensure evaluation, resilience, security, cost and operability are designed before go-live;
9. coordinate specialists without substituting for their accountability;
10. present the decision package to Design Authority/stakeholders.

## Separation of responsibilities

- **Data/Knowledge Owner** remains accountable for data meaning, quality, classification, retention and authorized use.
- **Security** remains accountable for security controls and security acceptance.
- **Risk/Compliance** remains accountable for regulatory/Responsible AI acceptance where applicable.
- **Platform/Ops** remains accountable for operational platform/SRE responsibilities.
- **Business Owner** remains accountable for business value and acceptable business risk.
- **Architecture** does not silently assume accountability owned by these functions; it integrates their requirements into a coherent design.

## Minimum governance gates

1. Use-case intake and business justification.
2. Data/security/privacy classification.
3. Architecture pattern and NFR review.
4. Model/provider evaluation and placement eligibility.
5. Risk/threat/Responsible AI review.
6. POC/evidence gate only where uncertainty remains.
7. Production readiness/SRE/rollback review.
8. Architecture approval with conditions/exceptions recorded.
9. Periodic re-evaluation after model/provider/data or regulation changes.
