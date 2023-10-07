#ExampleGA.ipynb
#Example of Genetic Algorithm
#Jorge Luis Rosas Trigueros
#Last modified 6oct23 12:26

import ipywidgets as widgets

def create_button():
  button = widgets.Button(
    description='Next Generation',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Next Generation',
    icon='check' # (FontAwesome names without the `fa-` prefix)
  )
  return button

import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from IPython import display as display

from functools import cmp_to_key
#Chromosomes are 4 bits long
L_chromosome=16
N_chains=2**L_chromosome
#Lower and upper limits of search space
a=-20
b=20
crossover_point=int(L_chromosome/2)


def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

#Number of chromosomes
N_chromosomes=10
#probability of mutation
prob_m=0.75

F0=[]
fitness_values=[]

for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)

#binary codification
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    for p in range(L_chromosome):
        value+=(2**p)*chromosome[-1-p]

    return a+(b-a)*float(value)/(N_chains-1)



def f(x):
    return 0.05*x*x-4*math.cos(x)



def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v=decode_chromosome(F0[p])
        fitness_values[p]=f(v)


def compare_chromosomes(chromosome1,chromosome2):
    vc1=decode_chromosome(chromosome1)
    vc2=decode_chromosome(chromosome2)
    fvc1=f(vc1)
    fvc2=f(vc2)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


suma=float(N_chromosomes*(N_chromosomes+1))/2.

Lwheel=N_chromosomes*10

def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
##    print fraction
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
##    print fraction

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel

F1=F0[:]
n=0
# indexes=list(range(N_chromosomes))
def nextgeneration(b):
    global n
    display.clear_output(wait=True)
    display.display(button)
    F0.sort(key=cmp_to_key(compare_chromosomes) )
    print( "Best solution so far:")
    n+=1
    print( n,"f(",decode_chromosome(F0[0]),")= ", f(decode_chromosome(F0[0])) )

    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    fitness=[]
    # maxfv=max(fitness_values)
    # for fv in fitness_values:
    #   fitness.append(maxfv-fv+1)

    roulette=create_wheel()
    print (roulette)
    for i in range(0,int((N_chromosomes-2)/2)):
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        # p1=random.choices(indexes,weights=fitness)[0]
        # p2=random.choices(indexes,weights=fitness)[0]
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    graph_population(F1)
    #The generation replaces the old one
    F0[:]=F1[:]




xmax=400
ymax=400

xo=200
yo=200

s=10


N=100

global_fig = plt.figure()
ax = plt.axes()

def graph_f():
    xini=-20.
    xfin=20.
    x=np.linspace(xini,xfin,100)
    y=list(map(f,x))
    plt.plot(x,y)

def graph_population(F):
    x=list(map(decode_chromosome,F))
    graph_f()
    plt.plot(x,y_population,'go')

button=create_button()
button.on_click(nextgeneration)
display.display(button)

x=list(map(decode_chromosome,F0))
y_population=np.zeros(N_chromosomes)
graph_f()
plt.plot(x,y_population,'go')
F0.sort(  key=cmp_to_key(compare_chromosomes))
evaluate_chromosomes()


