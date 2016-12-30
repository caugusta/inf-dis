import numpy as np
from scipy import spatial
import json
import itertools
from utils import *

MAX_FAILED_ATTEMPS = 10

def write_neighbourhood_epidemics_redo(susc, trans, inf_period, eps, repetitions, pop):
    epi_list = []
    count_list = []
    new_susc = []
    new_trans = []
    new_inf_period = []
    new_eps = []
    count = 0

    parameters_product = itertools.product(inf_period, eps)
    for infectious_period, epsilon in parameters_product:
        while True:
                if trans < 50:
                        for rep in range(repetitions):
                                print 'neigh', trans, inf_period, eps, rep, count
                                for _ in range(MAX_FAILED_ATTEMPS):
                                    g1 = neigh_epidemic(
                                        pop, susc, trans,
                                        inf_period, eps, full_mat)

                                    if len(g1) >= 10 and max(g1.values()) >= 10:
                                        g2 = inf_per_count_time(g1)
                                        count += 1
                                        epi_list.append(g1)
                                        count_list.append(g2)
                                        new_susc.append(susc)
                                        new_trans.append(trans)
                                        new_inf_period.append(inf_period)
                                        new_eps.append(eps)
                                        break
                                else:
                                    transmissibility += 1
                                    if rep > 0:
                                        del epi_list[-rep:]
                                        del count_list[-rep:]
                                        del new_susc[-rep:]
                                        del new_trans[-rep:]
                                        del new_inf_period[-rep:]
                                        del new_eps[-rep:]
                                        count -=1
                                    break
                        else:
                            break
                else:
                        print 'no epidemic'
                        break
                        #return infectious

    paras =  np.array([
        np.asarray(new_susc),
        np.asarray(new_trans),
        np.asarray(new_inf_period),
        np.asarray(new_eps)
    ]).T
    print 'number of parameter rows', paras[:,0].shape
    with open('parameters_neighbourhood_Dec29_redo.txt', 'w') as newfile1:
        np.savetxt(newfile1, paras, fmt = ['%f', '%f', '%f', '%f'])

    with open('epidemics_neighbourhood_Dec29_redo.json', 'w') as newfile2:
        json.dump(count_list, newfile2)


def write_neighbourhood_epidemics(susc, trans, inf_period, eps, repetitions, pop):
    epi_list = []
    count_list = []
    new_susc = []
    new_trans = []   
    new_inf_period = []
    new_eps = []
    count = 0

    parameters_product = itertools.product(trans, inf_period, eps)
    for transmissibility, infectious_period, epsilon in parameters_product:
        while True:
		if transmissibility < 50:
			for rep in range(repetitions):
				print 'neigh', transmissibility, infectious_period, epsilon, rep, count
				for _ in range(MAX_FAILED_ATTEMPS):
				    g1 = neigh_epidemic(
					pop, susc, transmissibility,
					infectious_period, epsilon, full_mat)

				    if len(g1) >= 10 and max(g1.values()) >= 10:
					g2 = inf_per_count_time(g1)
					count += 1
					epi_list.append(g1)
					count_list.append(g2)
					new_susc.append(susc)
					new_trans.append(transmissibility)
					new_inf_period.append(infectious_period)
					new_eps.append(epsilon)
					break
				else:
				    transmissibility += 1
				    if rep > 0:
					del epi_list[-rep:]
					del count_list[-rep:]
					del new_susc[-rep:]
					del new_trans[-rep:]
					del new_inf_period[-rep:]
					del new_eps[-rep:]
					count -=1
				    break
			else:
			    break
		else:
			print 'no epidemic'
			break
			#return infectious

    paras =  np.array([
        np.asarray(new_susc),
        np.asarray(new_trans),
        np.asarray(new_inf_period),
        np.asarray(new_eps)
    ]).T
    print 'number of parameter rows', paras[:,0].shape
    with open('parameters_neighbourhood_Dec29.txt', 'w') as newfile1:
        np.savetxt(newfile1, paras, fmt = ['%f', '%f', '%f', '%f'])

    with open('epidemics_neighbourhood_Dec29.json', 'w') as newfile2:
        json.dump(count_list, newfile2)


def write_exponential_epidemics(susc, trans, inf_period, eps, repetitions, pop):
    epi_list = []
    count_list = []
    new_susc = []
    new_trans = []
    new_inf_period = []
    new_eps = []
    count = 0

    parameters_product = itertools.product(trans, inf_period, eps)
    for transmissibility, infectious_period, epsilon in parameters_product:
        while True:
            for rep in range(repetitions):
	        print 'exp', transmissibility, infectious_period, epsilon, rep, count
                for _ in range(MAX_FAILED_ATTEMPS):
                    g1 = exp_epidemic(
                        pop, susc, transmissibility,
                        infectious_period, epsilon, full_mat)

                    if len(g1) >= 10 and max(g1.values()) >= 10:
                        g2 = inf_per_count_time(g1)
                        count += 1
                        epi_list.append(g1)
                        count_list.append(g2)
                        new_susc.append(susc)
                        new_trans.append(transmissibility)
                        new_inf_period.append(infectious_period)
                        new_eps.append(epsilon)
                        break
                else:
                    transmissibility += 1
                    if rep > 0:
                        del epi_list[-rep:]
                        del count_list[-rep:]
                        del new_susc[-rep:]
                        del new_trans[-rep:]
                        del new_inf_period[-rep:]
                        del new_eps[-rep:]
                        count -=1
                    break
            else:
                break

    paras =  np.array([
        np.asarray(new_susc),
        np.asarray(new_trans),
        np.asarray(new_inf_period),
        np.asarray(new_eps)
    ]).T
    print 'number of parameter rows', paras[:,0].shape
    with open('parameters_exponential_Dec29.txt', 'w') as newfile1:
        np.savetxt(newfile1, paras, fmt = ['%f', '%f', '%f', '%f'])


    with open('epidemics_exponential_Dec29.json', 'w') as newfile2:
        json.dump(count_list, newfile2)

def write_powerlaw_epidemics(susc, trans, inf_period, eps, repetitions, pop):    
    epi_list = []
    count_list = []
    new_susc = []
    new_trans = []
    new_inf_period = []
    new_eps = []
    count = 0

    parameters_product = itertools.product(trans, inf_period, eps)
    for transmissibility, infectious_period, epsilon in parameters_product:
        while True:
            for rep in range(repetitions):
		print 'powerlaw', transmissibility, infectious_period, epsilon, rep, count
                for _ in range(MAX_FAILED_ATTEMPS):
                    g1 = powerlaw_epidemic(
                        pop, susc, transmissibility,
                        infectious_period, epsilon, full_mat)

                    if len(g1) >= 10 and max(g1.values()) >= 10:
                        g2 = inf_per_count_time(g1)
                        count += 1
                        epi_list.append(g1)
                        count_list.append(g2)
                        new_susc.append(susc)
                        new_trans.append(transmissibility)
                        new_inf_period.append(infectious_period)
                        new_eps.append(epsilon)
                        break
                else:
                    transmissibility += 1
                    # Cleanup because we failed too many times
                    if rep > 0:
                        # if we've already written an epidemic
                        # using this set of parameters
		    	del epi_list[-rep:]
                    	del count_list[-rep:]
                    	del new_susc[-rep:]
                    	del new_trans[-rep:]
                    	del new_inf_period[-rep:]
                    	del new_eps[-rep:]
                        count -=1
                    break
            else:
                # do not restart if we made it through the whole repetitions
                break

    paras =  np.array([
        np.asarray(new_susc),
        np.asarray(new_trans),
        np.asarray(new_inf_period),
        np.asarray(new_eps)
    ]).T
    print 'number of parameter rows', paras[:,0].shape
    with open('parameters_powerlaw_Dec29.txt', 'w') as newfile1:
        np.savetxt(newfile1, paras, fmt = ['%f', '%f', '%f', '%f'])


    with open('epidemics_powerlaw_Dec29.json', 'w') as newfile2:
        json.dump(count_list, newfile2)


if __name__ == "__main__":
    pop = 200 #each cluster will have 200 individuals
    susc = 0.3
    powerlaw_trans = [7.5, 8.5, 9.5]
    exp_trans = [0.3, 0.65, 0.9]
    neigh_trans = [1.0, 1.5, 2.0] #, 2.0] #2.0 was too high. 1.0 and 1.5 were successful.
    #neigh_trans = [7.5, 3.5, 2.4]
    inf_period = [2, 3]
    eps = [0., 0.01, 0.02, 0.05] #was 0, 0.01, 0.02, 0.05
    mean_val = np.array([[1., 1.], [5., 5.], [2., 2.]])
    sigma_val = np.array([[[1., 0.], [0., 1.]], [[1., 0.], [0., 1.]], [[1., 0.], [0., 1.]]])
    full_mat = create_clustered_pop(mean_val, sigma_val, pop)
    reps = 400
    #neigh_eps = [0.1, 0.2, 0.5, 0.7] 

    #Uncomment this to read in the population instead of creating one
    #with open('29Dec_clustered_population.txt', 'r') as f:
    #       xy = np.loadtxt(f)
    ##print 'x, y', xy[0:pop]
    #x_pos = [item[0] for item in xy]
    #y_pos = [item[1] for item in xy]
    #dist_mat = np.asarray(zip(x_pos, y_pos))
    #pdistance = scipy.spatial.distance.pdist(dist_mat)
    #full_mat = scipy.spatial.distance.squareform(pdistance)

    #redo_trans = 0.5

    write_powerlaw_epidemics(susc, powerlaw_trans, inf_period, eps, reps, pop)
    write_exponential_epidemics(susc, exp_trans, inf_period, eps, reps, pop)
    write_neighbourhood_epidemics(susc, neigh_trans, inf_period, neigh_eps, reps, pop) 
    #write_neighbourhood_epidemics_redo(susc, redo_trans, inf_period, eps, reps, pop)
