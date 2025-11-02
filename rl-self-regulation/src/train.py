import argparse, json, os
from env import MarketEnv
from agent import TabularAgent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=200)
    ap.add_argument("--outdir", type=str, default="runs")
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    env = MarketEnv()
    ag = TabularAgent()

    rewards = []
    for ep in range(args.episodes):
        s = env.reset(); total = 0
        done = False
        while not done:
            a = ag.act(s)
            s2, r, done, _ = env.step(a)
            ag.learn(s, a, r, s2, done)
            s = s2; total += r
        rewards.append(total)

    out = {"episodes": args.episodes, "avg_reward": float(sum(rewards)/len(rewards))}
    with open(os.path.join(args.outdir, "agent.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("Saved model summary to runs/agent.json")

if __name__ == "__main__":
    main()
