import numpy as np

class MarketEnv:
    def __init__(self, seed=42):
        self.rng = np.random.default_rng(seed)
        self.reset()

    def reset(self):
        self.t = 0
        self.state = np.array([0.0, 0.0])  # [price_dev, order_imbalance]
        return self.state.copy()

    def step(self, action):
        # action in {-1,0,1}: sell/hold/buy equivalent pressure
        shock = self.rng.normal(0, 0.5)
        self.state[1] = 0.8*self.state[1] + action + shock   # imbalance
        self.state[0] = 0.9*self.state[0] + 0.1*self.state[1]  # price deviation responds

        # reward: small for stability (penalize |price_dev|, |imbalance|), small bonus for correct counter-action
        reward = - (abs(self.state[0]) + 0.5*abs(self.state[1]))
        done = self.t > 200
        self.t += 1
        return self.state.copy(), reward, done, {}
