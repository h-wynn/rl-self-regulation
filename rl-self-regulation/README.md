# RL Simulation of Self-Regulating Agents
Toy environment for studying stability vs. reward trade-offs in autonomous systems.

## What this shows (for Mila reviewers)
- Clear problem framing: stability under order-imbalance shocks
- Simple Q-learning–style agent with constraint-aware reward
- Evaluation beyond accuracy: episode stability, constraint violations, recovery time

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/train.py --episodes 200
python src/evaluate.py --model runs/agent.json
```
