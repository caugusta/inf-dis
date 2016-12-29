import numpy as np
import scipy
from scipy import spatial
import json
import collections
import sys

def create_pop(meanval, sigmaval, pop):
	x_pos, y_pos = np.random.multivariate_normal(meanval, sigmaval, pop).T
	dist_mat = np.asarray(zip(x_pos, y_pos))
	pdistance = scipy.spatial.distance.pdist(dist_mat)
	full_mat = scipy.spatial.distance.squareform(pdistance)

	#Save the population
	with open('23Dec_population.txt', 'w') as f:
		xyarray = np.array([x_pos, y_pos])
		xyarray = xyarray.T
		np.savetxt(f, xyarray, fmt=['%f', '%f'])

	return full_mat

#http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
def checkEqual(lst):
	return lst[1:] == lst[:-1]

def neigh_epidemic(pop, susc, trans, inf_period, eps, full_mat):

        susceptible = list(range(1, pop + 1))
        infectious = {}
        t = 1
        while not checkEqual(susceptible): #while there are still susceptible individuals (while susceptible is not all 0s)
                if t == 1:
                        inf_1 = int(np.random.randint(1, pop, size=1))
                        infectious[inf_1] = t
                        inf_times = t
                        susceptible[inf_1-1] = 0
                else:
                        for ind in susceptible:
                                if ind != 0:
                                        inf_times = [i for i in infectious.values() if ((t - inf_period <= i and (i < t)))]
                                        t_times = set(range(1, t)) #from 1 to t-1
                                        infset = set(inf_times)
                                        if not t_times.intersection(infset):
                                                return infectious
                                        l1 = [infectious.values().index(i) for i in inf_times]
                                        inf_indivs = [infectious.keys()[i] for i in l1]
					dist1 = [full_mat[ind-1, j-1] for j in inf_indivs]
                                        distset = [i for i in dist1 if i < trans] #r is trans
                                        probinf = 1 - np.exp(-susc*(sum(distset) + eps))
					#print 'sum(distset) is', sum(distset)
                                        if probinf >= np.random.uniform(0, 1):
                                                infectious[ind] = t
                                                susceptible[ind-1] = 0
                                else:
                                        continue
                t += 1
        return infectious



def exp_epidemic(pop, susc, trans, inf_period, eps, full_mat):
	
     	susceptible = list(range(1, pop + 1))
        infectious = {}
        t = 1
        while not checkEqual(susceptible): #while there are still susceptible individuals (while susceptible is not all 0s)
                if t == 1:
                        inf_1 = int(np.random.randint(1, pop, size=1))
                        infectious[inf_1] = t
                        inf_times = t
                        susceptible[inf_1-1] = 0
                else:
                        for ind in susceptible:
                                if ind != 0:
                                        inf_times = [i for i in infectious.values() if ((t - inf_period <= i and (i < t)))]
                                        t_times = set(range(1, t)) #from 1 to t-1
                                        infset = set(inf_times)
                                        if not t_times.intersection(infset):
                                                return infectious
                                        l1 = [infectious.values().index(i) for i in inf_times]
                                        inf_indivs = [infectious.keys()[i] for i in l1]
                                        dist1 = [np.exp(-trans*full_mat[ind-1, j-1]) for j in inf_indivs]
                                        probinf = 1 - np.exp(-susc*(sum(dist1) + eps))
                                        if probinf >= np.random.uniform(0, 1):
                                                infectious[ind] = t
                                                susceptible[ind-1] = 0
                                else:
                                        continue
                t += 1
        return infectious	

def powerlaw_epidemic(pop, susc, trans, inf_period, eps, full_mat, write=True):

	susceptible = list(range(1, pop + 1))
	infectious = {}
	t = 1
	while not checkEqual(susceptible): #while there are still susceptible individuals (while susceptible is not all 0s)
		if t == 1:
			inf_1 = int(np.random.randint(1, pop, size=1))
			infectious[inf_1] = t
			inf_times = t
			susceptible[inf_1-1] = 0
		else:
			for ind in susceptible:
				if ind != 0:
					inf_times = [i for i in infectious.values() if ((t - inf_period <= i and (i < t)))]
					t_times = set(range(1, t)) #from 1 to t-1
					infset = set(inf_times)
					if not t_times.intersection(infset):
						return infectious
					l1 = [infectious.values().index(i) for i in inf_times]
					inf_indivs = [infectious.keys()[i] for i in l1]
					dist1 = [(full_mat[ind-1, j-1])**(-trans) for j in inf_indivs]
					probinf = 1 - np.exp(-susc*(sum(dist1) + eps))
					if probinf >= np.random.uniform(0, 1):
						infectious[ind] = t
						susceptible[ind-1] = 0
				else: 
					continue
		t += 1
	return infectious #(infectious, inf_count_per_time)

def inf_per_count_time(infectious):

	inf_count = {} 
	c_1 = 0
	for t in range(1, np.max(infectious.values())+1): #to the max time
		inf_count[t] = np.sum(1 for i in infectious.values() if i==t)
	return inf_count #e.g. {2:3} means 3 people became infectious at time 2

#Comment this out - for testing only

#if __name__ == '__main__':
#
#    #Uncomment this to read in the population instead of creating one
#    with open('23Dec_population.txt', 'r') as f:
#           xy = np.loadtxt(f)
#    #print 'x, y', xy[0:pop]
#    x_pos = [item[0] for item in xy]
#    y_pos = [item[1] for item in xy]
#    dist_mat = np.asarray(zip(x_pos, y_pos))
#    pdistance = scipy.spatial.distance.pdist(dist_mat)
#    full_mat = scipy.spatial.distance.squareform(pdistance)
#
#    pop = 625
#    susc = 0.3
#    inf_period = 2
#    eps = 0.01
#    trans = 1.0
#    n1 = neigh_epidemic(pop, susc, trans, inf_period, eps, full_mat)
#    print n1
#    print len(n1)
#    print len(n1.values())
#    if len(n1) >= 10 and max(n1.values()) >= 10:
#	n2 = inf_per_count_time(n1)
#    	print n2
