from utils import cope_galai_cal

c = cope_galai_cal()
norm_ask, norm_bid, norm_spread = c.bid_ask_norm_dist(mu=100, sigma=10, pi=0.3)
exp_ask, exp_bid, exp_spread = c.bid_ask_exp_dist(lambda_value=0.0075, pi=0.01)

print(f"Spread equilibrium normal distribution: {norm_spread:.3f}")
print(f"Ask normal distribution: {norm_ask:.3f}")
print(f"Bid normal distribution: {norm_bid:.3f}")

print(f"\nSpread equilibrium exponential distribution: {exp_spread:.3f}")
print(f"Ask exponential distribution: {exp_ask:.3f}")
print(f"Bid exponential distribution: {exp_bid:.3f}")
