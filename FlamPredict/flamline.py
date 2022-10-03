

from data import *
from fire import *
global compute
compute=0

fire=Fire(25000-1,25000,B,1,p,25000,25000,A)
fire=Fire(25000,25000-1,B,1,p,25000,25000,A)
fire=Fire(25000+1,25000,B,1,p,25000,25000,A)
fire=Fire(25000,25000+1,B,1,p,25000,25000,A)
fire=Fire(25000-1,25000-1,B,1,p,25000,25000,A)
fire=Fire(25000+1,25000-1,B,1,p,25000,25000,A)
fire=Fire(25000+1,25000+1,B,1,p,25000,25000,A)
fire=Fire(25000-1,25000+1,B,1,p,25000,25000,A)
# print(B)