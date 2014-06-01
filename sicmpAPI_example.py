from sicmpAPI import SicmpAPI
res = SicmpAPI().is_compromised('myprivatemail@mypersonaldomain.com')
print res  # False
res = SicmpAPI().is_compromised('test@test.com')
print res  # True
