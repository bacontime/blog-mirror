---
title: Dual Scale Solar System
parent: Science and Nature
---

Let's say you want to make a nice little graphic of the solar system. 

If you make the sizes and distances of the objects to scale, then either you can't see anything:

Or your image has to be massive. (Though it's always a fun school activity to make a model of the Solar System on a sports field.)

You could ignore the distances, and just throw the planets into a loose pile, but then you lose the sense of how far apart things are.

Simple solution: make the sizes and distances to scale, but make them *different scales*.
That gives us a nifty image like this:




Here are the implementation details.

We can get the distances from the sun for various planets here.
And we can also get their equatorial radii.

The we need two scaling factors to determine how big things are on our image.

Planets are depicted on the image with radius of P cm / r_earth.
Orbits depicted with radius D cm / AU



### First Constraint: Mercury Falling into the Sun

The Sun has a radius of 


