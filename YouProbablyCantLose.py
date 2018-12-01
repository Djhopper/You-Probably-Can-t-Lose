import numpy as np
import matplotlib.pyplot as plt


def doGame(numTrials, startMoney, numTosses):
    money = np.full(numTrials, float(startMoney))
    for i in range(numTosses):
        money += money * 0.2 * (2*np.random.binomial(1, 0.6, numTrials) - 1)
    return money


#run simulation
sampleSize = 1000000
timePerToss = 15 #assumed average time to do a toss, measured in seconds
numTosses = 30 * 60 / timePerToss
endMoney = doGame(sampleSize, 25, int(numTosses))
#get heights for bar chart
bust = np.count_nonzero(np.where(endMoney < 2))/sampleSize
down = np.count_nonzero(np.where((endMoney < 25) & (endMoney>=2)))/sampleSize
poor = np.count_nonzero(np.where((endMoney < 100) & (endMoney>=25)))/sampleSize
better = np.count_nonzero(np.where((endMoney < 250) & (endMoney>=100)))/sampleSize
maxed = np.count_nonzero(np.where(endMoney >= 250))/sampleSize
#plot bar chart
x = np.arange(5)
plt.bar(x, [bust, down, poor, better, maxed])
plt.xticks(x, ('bust', 'down', 'poor', 'better', 'maxed'))
plt.show()
