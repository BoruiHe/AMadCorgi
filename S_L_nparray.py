import numpy as np

a = np.load("HBR_LR0.001_BS4_S8_aNb.6N.6_lc.npz", allow_pickle = True)
print(a["a"])
print(a["b"])
# print(a["untrained"].shape,a["trained"].shape)

# b = np.load("HBR_LR0.001_BS8_S10_aNb.6N.6_U.npy", allow_pickle = True)
# print(b.shape)

# bb = np.load("HBR_LR0.001_BS8_S10_aNb.6N.6_UU.npy", allow_pickle = True)
# print(bb.shape)

# c = np.concatenate((b,bb),axis=0)
# cc = np.concatenate((b,bb),axis=0)
# print(c.shape)
# print(cc.shape)

# np.savez("HBR_LR0.001_BS4_S8_aNb.6N.6.npz", untrained = c, trained = cc)

