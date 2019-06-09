import numpy as np
#variable = np.array(["Hagen",2,3])
theurlpage1 = "".join([markt_site, "dies-und-das.html?sl=60400"])
theurlpage2 = "".join([markt_site, "dies-und-das-Part2.html?sl=60400&nPart=2"])
theurlpage3 = "".join([markt_site, "dies-und-das-Part3.html?sl=60400&nPart=3"])
theurlpage4 = "".join([markt_site, "dies-und-das-Part4.html?sl=60400&nPart=4"])
theurlpage5 = "".join([markt_site, "dies-und-das-Part5.html?sl=60400&nPart=5"])

theurl = ([theurlpage1, theurlpage2, theurlpage3])

for i in theurl:
    print (i)
