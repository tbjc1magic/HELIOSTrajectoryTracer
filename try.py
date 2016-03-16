import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import pyplot as plt

import Constants
from TrajectoryManager  import TrajectoryManager
print Constants.MeV

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

TM = TrajectoryManager()
TM.OpenFile('StartCondition.json')
#TM.OpenFile('aa.json')
TM.CalculateTrajectories()
for OneTr in TM.Trajectories:
    ax.plot(OneTr[0],OneTr[1],OneTr[2])
plt.show()
