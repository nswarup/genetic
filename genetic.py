__author__ = 'nishaswarup'

from random import random, randint
from math import pi, sin, cos,sqrt
import sys

# Define variables
npoints = 4
population = 100
spheres = []
keep = .3
rdom = .1
trials = 3000
progress = 20  # how often we print progress


# Initialize population array
def initialize(input_population):
    for p in xrange(population):
        # Add a new sphere
        new_sphere = []
        for q in xrange(npoints):
            # Add random points to sphere, using spherical coordinates
            rand_theta = random() * 2 * pi
            rand_phi = random() * pi
            new_sphere.append((rand_theta, rand_phi))
        input_population.append(new_sphere)
    return input_population


# Return distance, given two points in spherical coordinates
def distance((a, b), (c, d)):
    return sqrt(2 - 2*(sin(b)*sin(d)*cos(a-c) + cos(b)*cos(d)))


# Return potential energy of a sphere
def calc_potential(input_sphere):
    v = 0
    for r in xrange(len(input_sphere)):
        for s in xrange(r+1, len(input_sphere)):
            v += 1./distance(input_sphere[r], input_sphere[s])
    return v


if __name__ == __main__:
    # Initialize spheres
    spheres = initialize(spheres)
    for n_trial in xrange(trials):
        # Find potentials. Potentials will be an array of tuples: (potential of the sphere, index in the spheres array)
        potential = []
        for n in xrange(population):
            potential.append((calc_potential(spheres[n]), n))
        # Sort by potential
        potential = sorted(potential)

        # Do crosses (uniform crossover)
        for n in xrange(int(keep * population), int(population - population * rdom)):
            # Choose two random spheres from the best
            n1 = potential[randint(0, keep * population)][1]
            n2 = potential[randint(0, keep * population)][1]
            sphere1 = spheres[n1]
            sphere2 = spheres[n2]
            sphereNew = []
            # Uniform crossover
            for x in xrange(npoints):
                if randint(0, 1) == 0:
                    sphereNew.append(sphere1[x])
                else:
                    sphereNew.append(sphere2[x])
            spheres[potential[n][1]] = sphereNew
        # Add a few random spheres
        for n in xrange(int(population - population * rdom), population):
            sphere = []
            for y in xrange(npoints):
                theta = random() * 2 * pi
                phi = random() * pi
                sphere.append((theta, phi))
            spheres[n] = sphere
        if n_trial % progress == 0:
            sys.stdout.write("\r" + str(n_trial * 100 / trials) + "% done")
            sys.stdout.flush()
    sys.stdout.write("\r100% done\n")

    # After all trials are over, return the best potential
    potential = sorted(potential)
    print "The minimum potential of " + str(npoints) + " point charges is " + str(potential[0][0])