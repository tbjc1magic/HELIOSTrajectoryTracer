from scipy.interpolate import interp1d
import Constants
import math
import json

class TrajectoryManager:

    def __init__(self):
        self.Trajectories = []
        self.StartCondition = []
        self.Interpolators = []
        return

    def OpenFile(self, fname):

        with open(fname) as f:
             self.StartCondition = json.load(f)

        return

    def CalculateTrajectories(self):
        '''
        v:m/s;
        thetalab:degree;
        philab:degree;
        charge:electron(+);
        mass:atomic u;
        B: T;
        Resolution: the number of points to be showing up
        '''

        for one in self.StartCondition:
            v = TrajectoryManager.Ek2v(one['mass'],one['Ek'])
            Xpos,Ypos,Zpos = self.CalculateOneTrajectory(v,one['theta'],one['phi'],one['charge'],one['mass'], one['B'])
            self.Trajectories.append([Xpos,Ypos,Zpos])

        return

    def CalculateOneTrajectory(self, v, thetalab, philab, charge, mass, B, Resolution =100):

        '''
        v:m/s;
        thetalab:degree;
        philab:degree;
        charge:electron(+);
        mass:atomic u;
        B: T;
        Resolution: the number of points to be showing up
        '''

        Pcharge = charge *Constants.e
        Pmass_tmp = mass* Constants.u
        Pmass = Pmass_tmp/math.sqrt(1-v*v/(Constants.c*Constants.c))
        thetalab = math.radians(thetalab)
        philab = math.radians(philab)
        Vpp = v*math.cos(thetalab)
        Vpr = v*math.sin(thetalab)

        OrbitRadius = Pmass * Vpr/(Pcharge*B)
        OrbitTime =  2*math.pi*Pmass/(Pcharge*B)

        print OrbitRadius,v
        Zpos = []
        Xpos = []
        Ypos = []

        for i in xrange(Resolution):
            TimeStep = OrbitTime/Resolution
            OrbitTheta = float(i)/Resolution*math.pi*2
            Rtmp = OrbitRadius*2*math.sin(OrbitTheta/2)
            Alphatmp = OrbitTheta/2+philab
            Xtmp = Rtmp* math.cos(Alphatmp)
            Ytmp = Rtmp* math.sin(Alphatmp)
            Ztmp = TimeStep*Vpp*i

            Zpos.append(Ztmp)
            Xpos.append(Xtmp)
            Ypos.append(Ytmp)

        return Xpos, Ypos, Zpos

    def CreateInterpolation(self):
        for oneX, oneY, oneZ in self.Trajectories:
            oneSplineX = interp1d(oneZ,oneX,kind='cubic')
            oneSplineY = interp1d(oneZ,oneY,kind='cubic')
            self.Interpolators.append({'XSpline':oneSplineX,'YSpline':oneSplineY})

        return

    def GetPosition(self, z):

        xpos = []
        ypos = []
        for one in self.Interpolators:
            try:
                xpos.append(one['XSpline'](z))
                ypos.append(one['YSpline'](z))
            except:
                pass

        return xpos,ypos

    @staticmethod
    def Ek2v( m, Ek):
        """unit:m(atomic u),Ek(MeV),v(m/s)"""
        m  = m*Constants.u
        Ek = Ek*Constants.MeV

        ratio_tmp = Ek/(m*Constants.c*Constants.c)
        v= Constants.c*math.sqrt(1-1/((ratio_tmp+1)*(ratio_tmp+1)))
        return v
