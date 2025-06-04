import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve
from utils import cope_galai_cal

c = cope_galai_cal()
c.bid_ask_norm_dist(mu=100, sigma=10, pi=0.01)
c.bid_ask_exp_dist(lambda_value=0.0075, pi=0.01)
