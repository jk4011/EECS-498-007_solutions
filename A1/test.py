import torch
from pytorch101 import slice_indexing_practice

x = torch.arange(6).view(2, 3)
print(x.repeat((2,1)))
