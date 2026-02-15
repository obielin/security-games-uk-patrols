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

## Model Formulation

This work involves formalising patrol allocation as a Stackelberg security game over spatial zones derived from empirical crime data.

Let:

Z = {1, ..., n} denote geographic patrol zones
V_i denote observed crime intensity in zone i (aggregated incident count)
x_i in [0, 1] denote patrol coverage probability in zone i
B denote total patrol resource budget
The defender (leader) commits to a mixed strategy x = (x_1, ..., x_n) subject to:

  - sum(x_i) <= B
  - 0 <= x_i <= 1

The attacker (follower), observing this strategy, selects the zone that maximises expected payoff:
  - i* = argmax_i (1 - x_i) * V_i

The defender anticipates this response and chooses x to minimise the worst-case residual risk:

  - min_x max_i (1 - x_i) * V_i

This formulation explicitly models strategic interaction between patrol allocation and adversarial targeting, rather than treating crime intensity as passive or purely stochastic.
Crime intensity V_i represents observed incident frequency under reporting constraints and should not be interpreted as intrinsic criminal propensity.

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

## Experimental Protocol

The repository follows a reproducible experimental pipeline:

- Data Ingestion
  - Retrieve street-level crime data via the UK Police Data API and construct a versioned sample dataset.

- Spatial Zoning
  - Partition the study region into fixed geographic grid cells.
  - Aggregate crime incidents within each cell to construct a zone-level risk surface.

- Risk Surface Construction
  - Estimate empirical crime intensity Vi for each zone.

- Baseline Strategy Computation
  - Compute Stackelberg patrol strategies under varying resource budgets.

- Baseline Comparisons
Compare against:
  - Uniform patrol allocation
  - Proportional-to-crime allocation
  - Greedy hotspot allocation

- Evaluation Metrics
  - Expected residual crime risk
  - Risk concentration across zones
  - Sensitivity to uncertainty in Vi

---

Distributional analysis of patrol allocation

## Repository Structure

- `notebooks/` — reproducible experiments (data ingestion → zoning → game solving)
- `src/` — reusable modules (API client, zoning logic, game solver)
- `data/` — local artefacts (excluded from version control)

---

## Responsible Use

This project is intended for **research and decision-support purposes only**.  
Any operational deployment would require governance, human oversight, and periodic review to mitigate bias, misuse, or unintended harm.

---

## License

MIT License (recommended for public research repositories)
