import numpy as np

class TabularAgent:
    def __init__(self, bins=7, actions=3, alpha=0.1, gamma=0.98, eps=0.1):
        self.bins = bins; self.actions = actions
        self.alpha = alpha; self.gamma = gamma; self.eps = eps
        self.q = np.zeros((bins, bins, actions))

    def _disc(self, s):
        # discretize continuous state into bins
        d = np.clip(((s+5)/10*self.bins).astype(int), 0, self.bins-1)
        return tuple(d)

    def act(self, s):
        if np.random.rand() < self.eps: return np.random.randint(self.actions)
        i,j = self._disc(s)
        return np.argmax(self.q[i,j])

    def learn(self, s, a, r, s2, done):
        i,j = self._disc(s); i2,j2 = self._disc(s2)
        best_next = 0 if done else np.max(self.q[i2,j2])
        td = r + self.gamma*best_next - self.q[i,j,a]
        self.q[i,j,a] += self.alpha*td
