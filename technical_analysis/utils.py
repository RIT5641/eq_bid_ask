import numpy as np
from scipy.stats import norm
from scipy.optimize import fsolve

class cope_galai_cal:
    def __init__(self):
        pass

    def bid_ask_norm_dist(self, mu:float, sigma:float, pi:float):
        #mu = 100    # Valor medio del activo
        #sigma = 10  # Desviación estándar del valor
        #pi = 0.3    # Prob trader informado

        def expected_profit(S):
            a = mu + S / 2
            b = mu - S / 2

            z_a = (a - mu) / sigma
            z_b = (mu - b) / sigma

            E_V_gt_a = mu + sigma * norm.pdf(z_a) / (1 - norm.cdf(z_a))
            E_V_lt_b = mu - sigma * norm.pdf(z_b) / norm.cdf(z_b)

            profit_ask = (1 - pi) * (a - mu) + pi * (a - E_V_gt_a)
            profit_bid = (1 - pi) * (mu - b) + pi * (E_V_lt_b - b)

            expected_profit = 0.5 * (profit_ask + profit_bid)
            return expected_profit
        initial_guess = 1.0
        spread_equilibrium = fsolve(expected_profit, initial_guess)[0]

        # Calcular precios de bid y ask
        ask = mu + spread_equilibrium / 2
        bid = mu - spread_equilibrium / 2

        #print(f"Spread de equilibrio: {spread_equilibrium:.4f}")
        #print(f"Precio Ask: {ask:.4f}")
        #print(f"Precio Bid: {bid:.4f}")
        return ask, bid, spread_equilibrium

    def bid_ask_exp_dist(self, lambda_value:float=0.5, pi:float=0.3):
        # Desarrollar
        # Valor esperado
        EV = 1 / lambda_value

        def expected_profit(S):
            a = EV + S / 2
            b = EV - S / 2

            E_V_gt_a = a + 1 / lambda_value
            E_V_lt_b = EV - (b*np.exp(-lambda_value*b)) / (1 - np.exp(-lambda_value*b))

            profit_ask = (1 - pi)*(a - EV) + pi*(a - E_V_gt_a)
            profit_bid = (1 - pi)*(EV - b) + pi*(E_V_lt_b - b)

            return 0.5 * (profit_ask + profit_bid)
        initial_guess = 1.0
        spread_equilibrium = fsolve(expected_profit, initial_guess)[0]
        ask = EV + spread_equilibrium / 2
        bid = EV - spread_equilibrium / 2

        #print(f"Spread de equilibrio: {spread_equilibrium:.4f}")
        #print(f"Precio Ask: {ask:.4f}")
        #print(f"Precio Bid: {bid:.4f}")
        return ask, bid, spread_equilibrium


