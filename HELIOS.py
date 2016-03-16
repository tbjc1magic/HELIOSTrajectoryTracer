import math

__constant_u = 1.66e-27
__constant_MeV = 1.6e-13
__constant_e = 1.6e-19
__constant_c = 3.0e8

def trajectory(v, thetalab, charge, mass, B, Resolution =100):
    Pcharge = charge *__constant_e
    Pmass_tmp = mass* __constant_u
    Pmass = Pmass_tmp/math.sqrt(1-v*v/(__constant_c*__constant_c))

    Vpp = v*math.cos(thetalab)
    Vpr = v*math.sin(thetalab)

    OrbitRadius = Pmass * Vpr/(Pcharge*B)
    OrbitTime =  2*math.pi*Pmass/(Pcharge*B)

    print v,Vpr,thetalab/math.pi*180, charge, mass,B

    print "orbit:",OrbitRadius, OrbitTime
    Zpos = []
    Rpos = []

    for i in xrange(Resolution):
        TimeStep = OrbitTime/Resolution
        OrbitTheta = float(i)/Resolution*math.pi*2
        Rtmp = OrbitRadius*(1-math.cos(OrbitTheta))
        Ztmp = TimeStep*Vpp*i
        Rpos.append(Rtmp*100)
        Zpos.append(Ztmp*100)

    return Zpos, Rpos
