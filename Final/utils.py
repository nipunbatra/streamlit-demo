import torch

def compute_pdf(dist, x_range, support):
    pdf = torch.zeros_like(x_range, dtype=torch.float)

    if support:
        min_val, max_val = support
        mask = (x_range >= min_val) if min_val is not None else torch.ones_like(x_range, dtype=torch.bool)
        if max_val is not None:
            mask &= (x_range <= max_val)
    else:
        mask = torch.ones_like(x_range, dtype=torch.bool)

    pdf[mask] = dist.log_prob(x_range[mask]).exp()
    return pdf