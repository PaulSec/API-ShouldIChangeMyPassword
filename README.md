ShouldIChangeMyPassword
=======================

(Unofficial) Python API for ShouldIChangeMyPassword Website.

This code has been developed to check compromised mails and is really easy to use: 

```python 
from sicmpAPI import SicmpAPI
res = SicmpAPI().is_compromised('myprivatemail@mypersonaldomain.com')
print res  # False
```

I am currently developing a multithreaded tool to load file and parallelize the process.
Stay tuned. 