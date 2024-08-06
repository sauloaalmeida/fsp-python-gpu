import fsp.methods.distance.torch as method_torch

def cdist(A, B):
    return method_torch.cdist(A,B,"cuda").cpu().numpy()

def cdist_dm1(A, B):
    return method_torch.cdist_dm1(A,B,"cuda").cpu().numpy()

def pdist_dm1(A):
    return method_torch.pdist_dm1(A, "cuda").cpu().numpy()