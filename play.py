import torch
import random

BATCHSIZE = 1

def calcDist(tensor: torch.tensor):
  pass



X = torch.tensor([], dtype=torch.double)
Y = torch.tensor([], dtype=torch.double)
def getSample():
  return torch.tensor([[random.uniform(0, 1), random.uniform(0, 1)]], dtype=torch.double)  
#print(t2)

for i in range(BATCHSIZE):
  s = getSample()
  X = torch.cat((X, s), dim=0)

for i in X:
  s = calcDist(i)
  print(s)
#print(X)


