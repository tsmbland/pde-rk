"""
180725
m0008
Testing random parameter sets on cluster

Normal simulation followed by PAR-1 RNAi simulation

"""

import M as x
import Models.m0008b as m0008b
import sys

x.datadirec = '../working/Tom/ModelData'

# Base parameter set
p0 = m0008b.Params(Da=0, kon_a=0.0085, koff_a=0.0054, ra=1, Dp=0, kon_p=0.0474, koff_p=0.0073, kon_p_2=0.0474,
                   kd_f=1, kd_b=1, rp=1, L=67.3,
                   xsteps=500, psi=0.174, Tmax=10000, deltat=0.01, starts=[0, 1.56, 0, 0, 0, 1, 0])

# Free parameters
params = ['ra', 'kon_p', 'kon_p_2', 'kd_f', 'kd_b', 'rp']
ranges = [[0.01, 1], [0.001, 0.1], [0.01, 1], [0.01, 1], [0.01, 1], [0.01, 1]]

# Standard simulation + analysis
x.alg_parsim_rand_clust(m=m0008b.Model(p0), params=params, ranges=ranges, nsims=960, jobid=7, subjobid=2, cores=32,
                        compression=0, node=int(sys.argv[1]))
x.batch_analysis(7, 2, funcs=x.all_analysis)
x.save_scores_batch(7, 2)

# Retesting in PAR-1 RNAi mode + analysis
x.alg_parsim_clust_duplicate(m=m0008b.Model(p0), changes={'rp': 0}, oldjobid=7, oldsubjobid=2, newjobid=7,
                             newsubjobid=3,
                             cores=32, node=int(sys.argv[1]), compression=0)
x.batch_analysis(7, 3, funcs=x.all_analysis)
x.save_scores_batch(7, 3)