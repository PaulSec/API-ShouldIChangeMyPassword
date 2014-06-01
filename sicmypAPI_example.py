from sicmypAPI import SicmypAPI
res = SicmypAPI().is_compromised('myprivatemail@mypersonaldomain.com')
print res  # False
res = SicmypAPI().is_compromised('test@test.com')
print res  # True
