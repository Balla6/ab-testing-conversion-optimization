import numpy as np
import statsmodels.api as sm
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize


def run_two_proportion_z_test(control_success, control_total, treatment_success, treatment_total):
    successes = np.array([control_success, treatment_success])
    samples = np.array([control_total, treatment_total])

    z_stat, p_value = proportions_ztest(successes, samples)
    return z_stat, p_value


def compute_confidence_intervals(control_success, control_total, treatment_success, treatment_total):
    count = np.array([control_success, treatment_success])
    nobs = np.array([control_total, treatment_total])

    ci_low, ci_high = sm.stats.proportion_confint(count, nobs)
    return ci_low, ci_high


def run_power_analysis(control_rate, treatment_rate, power=0.8, alpha=0.05):
    effect_size = proportion_effectsize(treatment_rate, control_rate)
    analysis = NormalIndPower()

    required_sample_size = analysis.solve_power(
        effect_size=effect_size,
        power=power,
        alpha=alpha
    )

    return required_sample_size