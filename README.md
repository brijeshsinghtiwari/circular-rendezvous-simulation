# Circular Rendezvous Simulation

A probabilistic simulation of two walkers moving on a circular track under uncertainty.

## Problem Statement

Two walkers move on a circular track of circumference C.

Each walker:
- starts at a random position,
- chooses a random direction,
- may reverse direction probabilistically,
- cannot reverse until traveling a minimum persistence distance D.

The objective is to study:

- Expected meeting time E[T]
- Effect of reversal probability p
- Ballistic vs diffusive behavior
- Persistent random walks
- Symmetry breaking in rendezvous search

---

## Mathematical Ideas

This project combines:

- Rendezvous search theory
- Persistent random walks
- Diffusion processes
- Monte Carlo simulation
- Stochastic motion on compact geometry

---

## Parameters

| Parameter | Meaning |
|---|---|
| C | Circumference of circle |
| p | Reversal probability |
| D | Minimum distance before turning |
| E[T] | Expected meeting time |

---

## Example Questions

- How does E[T] vary with p?
- Is there an optimal persistence distance?
- When does motion become ballistic vs diffusive?
- What happens if turning distances follow a Gaussian distribution?

---

## Example Plot

### E[T] vs p

![E[T] vs p](images/et_vs_p.png)

### E[T] vs D

![E[T] vs D](images/et_vs_d.png)

---

## Run

Install dependencies:

```bash
pip install -r requirements.txt