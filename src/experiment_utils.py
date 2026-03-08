def compute_uplift(control_rate, treatment_rate):
    absolute_uplift = treatment_rate - control_rate
    relative_uplift = absolute_uplift / control_rate
    return absolute_uplift, relative_uplift


def estimate_additional_conversions(total_users, absolute_uplift):
    return total_users * absolute_uplift