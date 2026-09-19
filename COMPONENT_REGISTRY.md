# Component Registry

This registry maps the current public-facing Equilibrium Stability Systems research components without transferring authority between repositories.

| Component | Repository / Surface | Visibility | Evidence status | Maturity | Claim boundary |
|---|---|---|---|---|---|
| Evidence Gate | https://github.com/lbkapcsolat-dotcom/evidence-gate | PUBLIC | VERIFIED_BOUNDED | RESEARCH_STAGE | Evidence classification and related bounded runtime/formal work only |
| EQ64 / Equilibrium Bridge | Evidence Gate research line | PUBLIC | EXPERIMENTAL | RESEARCH_STAGE | Finite-state admission and formal bridge research only |
| ALPHA Control Plane | private repository | PRIVATE | EXPERIMENTAL | RESEARCH_STAGE | No public implementation claim |
| ProofPath | https://github.com/lbkapcsolat-dotcom/proofpath-public | PUBLIC | VERIFIED_BOUNDED | RESEARCH_STAGE | Educational evidence assessment only |
| Tensor benchmark | https://github.com/lbkapcsolat-dotcom/tensor-cube-frozen40-benchmark | PUBLIC | VERIFIED_BOUNDED | RESEARCH_STAGE | Frozen 40-state benchmark only |

## Registry invariants

1. No component inherits another component's verification status.
2. No public listing implies production readiness.
3. Private components remain private unless separately and explicitly published.
4. Historical branch names, tags, or commits do not become current system authority by being referenced here.
5. A repository-specific claim ceiling always overrides any broader wording in this map.
