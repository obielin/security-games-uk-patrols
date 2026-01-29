# Security Games for Patrol Optimisation (UK Case Study)

This repository develops a **game-theoretic framework for patrol allocation** using a **Stackelberg security game** formulation, grounded in real UK crime data. The project moves beyond predictive hotspotting by explicitly modelling the **strategic interaction between defenders and adversarial offenders**.

The work is structured as a reproducible, research-oriented case study with an emphasis on transparency, auditability, and responsible use.

---

## Research Question

How can limited patrol resources be allocated across geographic zones such that expected crime risk is minimised **under adversarial response**, while respecting operational and fairness constraints?

---

## Method Overview

- Defender (leader) commits to a **mixed patrol strategy** across spatial zones.
- Attacker (follower) observes this strategy and best-responds by selecting a target.
- Payoffs are derived from empirically observed crime intensity.
- Strategies are computed using Stackelberg equilibrium concepts.

Planned extensions include:
- Robust optimisation under payoff uncertainty
- Bounded-rational attacker models
- Fairness-aware constraints on patrol allocation

---

## Data Sources

Primary data source:
- **UK Police Data API** (street-level crime and outcomes)
  - https://data.police.uk/docs/method/crime-street/

Initial case study area:
- **Westminster (London, UK)** — selected due to consistently high recorded crime activity, providing a realistic stress-test for patrol optimisation strategies.

All analysis operates on **aggregated geographic zones** derived from public data. No personal or identifiable data is processed.

---

## Evaluation Criteria

- Expected risk reduction relative to baseline patrol strategies
- Sensitivity to uncertainty in crime intensity estimates
- Stability of strategies under budget constraints
- Distributional analysis of patrol allocation across zones

---

## Repository Structure

- `notebooks/` — reproducible experiments (data ingestion → zoning → game solving)
- `src/` — reusable modules (API client, zoning logic, game solver)
- `data/` — local artefacts (excluded from version control)

---

## Responsible Use

This project is intended for **research and decision-support purposes only**.  
Any operational deployment would require governance, human oversight, and periodic review to mitigate bias, misuse, or unintended harm.

---

## Roadmap (Planned Daily Commits)

- Day 1: Repository scaffold, research framing, reproducibility baseline
- Day 2: UK Police API ingestion and Westminster data extraction
- Day 3: Spatial zoning and risk surface construction
- Day 4: Stackelberg baseline solver and patrol strategies
- Day 5: Novel extension (robust or behavioural attacker model)
- Day 6: Fairness and constraint analysis
- Day 7: Results synthesis and reproducibility polish

---

## License

MIT License (recommended for public research repositories)
