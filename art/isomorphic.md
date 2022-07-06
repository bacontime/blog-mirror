---
title: Isomorphic Keyboards
parent: Hidden
has_children: false
---

Art and Culture

I am confused about the permutations of the hex layout actually.



# Isomorphic Musical Keyboards

## Note layouts where relative physical position matches relative pitch.

If the ratio of frequencies between two notes is a power of two, then the notes sound very similar, 
and in musical notation, are labelled with the same letter. 
220hz, 440hz, 880hz - these are all "A" notes.
The interval between one frequency and its double is called an "octave".

In Twelve-tone Equal Temperament, the most common musical system today,
each octave is split up into 12 logarithmically spaced intervals.
Each note has a frequency 2^(1/12) times the previous note.
This interval is also called a "semitone".

A standard piano keyboard is arranged so that 
moving 1 key to the right increases the pitch by 1 semitone.
Moving 12 keys to the right increases the pitch by 1 octave.

But the keys on a piano aren't a consistent size. 
7 of the notes - the ones important enough in Western music to get their own letter name -
are given their own big white keys,
while the other 5 keys in each octave are given shrunken-down black keys.
One of the consequences of this layout is that 
if you want to change the key of a song (shift every note by the same frequency), 
you can't simply move the position of your hands on the keyboard;
you need to change the pattern that your fingers move in as well.

An *isomorphic* keyboard is one that doesn't have this particular problem.
Songs, chords, and intervals have the same shape, even when the key is changed.




## Linear Isomorphic Keyboard

Making a 1-dimensional isomorphic keyboard is simple.
Just take a piano and make all the keys the same shape.

At least one firm has tried to manufacture [a keyboard in this style](https://www.youtube.com/watch?v=hqbOqGRCAt0).

I've also found [this video of a **Ten**-tone equal temperament isomorphic keyboard](https://www.youtube.com/watch?v=LxeGZLd49Vs).
One commenter describes its sound as perfect for a "klingon opera".


## Hexagonal Isomorphic Keyboards.

There are a number of ways (28 to be exact) to arrange notes on a hexagonal grid in an isomorphic way.

Each possible isomorphic layout can be specified by a pair (α,β)
which describes the shift in semitones when moving in each direction.

![](isomorphic/isomorphicHexDescription.svg)


Ignoring rotations, reflections, and translations, and treating a shift in octave as the 'same note',
we only need to consider the 28 cases where 
α is between 0 and 6 inclusive, and β is between 0 and α inclusive.

Of these 28 possibilities, only 15 cover all 12 notes.
The other 13 possibilities are missing at least half of the notes.
For example, you could make a keyboard with (0,0) semitone shifts,
but thats only useful if you [only want to play E](https://www.youtube.com/watch?v=BFetTcrVWII).


### (1,1) The Janko Keyboard

[Invented in 1882 by Paul von Jankó](http://improvise.free.fr/janko.htm), 
this keyboard layout is similar to a 1-dimensional isomorphic keyboard,
but with multiple copies of the keyboard stacked above one another.

Because of its mechanical similarity to a standard piano,
there are several firms which have manufactured instruments with this layout.
[Here's a video of a player demonstrating such a piano](https://www.youtube.com/watch?v=cK4REjqGc9w&t=248s).
[And here's another](https://www.youtube.com/watch?v=FkN9-r7q7gg). [One more](https://www.youtube.com/watch?v=oT2zkss77Fo).
There are also [3d-printed overlays](https://www.youtube.com/watch?v=9tMtKyYEbaM) 
that can be dropped on top of a standard piano keyboard to convert it to a janky Janko layout.

<!--Another 3d printed version https://hackaday.com/2019/07/13/isomorphic-keyboards-with-cv-out/-->


### (2,1) Chromatic Button Accordion 

There are two types of key layout called type B and type C, but they are mirror images of each other.



### (3,1) and (4,1) Qwerty Chromatic

I don't know if there are any actual instruments with this layout,
but [my toy qwerty piano web app](https://www.rmwinslow.com/tones/) implements a version of (1,3), labelled "Isomorphic - Chromatic".

On a Qwerty keyboard, there are 4 rows, 
and so (if rotated properly) these layouts allow an octave to be covered by three consecutive columns.
<!--(The (1,4) layout would need to be rotated so that the 4-semitone shift happens horizontally.)-->


### (5,2) Wicki-Hayden

Used on some accordion-type instruments. <!--Proper term is squeezeboxes-->


### (4,3) Euler's Tonnetz

The Tonnetz, or Tone Network is a hexagonal grid of notes 
where 
each triplet of three adjacent notes forms a musically-significant chord.

The tonnetz was first described by Leonard Euler in 1739.
The modernized version with 12-tone equal temperament is also sometimes called a "Harmonic Table" layout.

There have been several instruments built using this keyboard layout,
including the [Harmonetta, which is like a big harmonica with a keyboard attached](https://www.youtube.com/watch?v=UyZ1beUJ4zw),
and the [AXiS 49 MIDI keyboard](https://www.youtube.com/watch?v=C9-OSCl7kOc).

<!--Also this Opal keyboard maybe?-->

[Here's a web app where you can play around with the Tonnetz](https://cifkao.github.io/tonnetz-viz/).
And [my toy qwerty piano web app](https://www.rmwinslow.com/tones/) also has a Tonnetz layout, labelled "Isomorphic - Euler".






---

### Other Possibilities not described above.

(0,1) would simply be multiple 1-dimensional keyboards stacked atop each each. Moving rows would shift the pitch by an octave.

(0,5) would be pretty bizarre. adjacent keys would making playing major fourths and minor fifths easy, 
but everything else would be significantly more difficult.

(2,3) is called the "Park" layout by Brett Park. <!--http://www.altkeyboards.com/instruments/isomorphic-keyboards-->







---

## Rectangular Isomorphic Keyboards.

Rectangular isomorphic keyboards can be mapped 1-1 to hexagonal isomorphic keyboards.
There are also 28 distinct rectangular isomorphic keyboards, 15 of which cover all 12 notes.
<!--The rectangular layouts can also be described with a pair (x,y) where-->

I won't list all the possibilities here.


###  The Harpeji <!--(1,2)-->

The harpeji is a string instrument played by tapping on frets.

Moving horizontally between strings shifts the pitch by two semitones,
and moving between frets shifts the pitch by one semitone.

Here are a few examples of people playing the harpeji:
[1](https://www.youtube.com/watch?v=LQtEElCV2lY&t=17s),
[2](https://www.youtube.com/watch?v=NWUYXQMwIk4),
[3](https://www.youtube.com/watch?v=DAvAC1EZUYQ),
[4](https://www.youtube.com/watch?v=eJ3H0Njb1As)

<!--
 (4:5:6 frequency ratio)
and there are also [diy projects](http://www.balanced-keyboard.com/) 
which try to retrofit a standard piano keyboard into a more isomorphic design.

https://en.wikipedia.org/wiki/Zhu_Zaiyu
Bizarre coincidence of history
exact calculation of twelve-tone equal temperament are Zhu Zaiyu (also romanized as Chu-Tsaiyu. Chinese: 朱載堉) in 1584 and Simon Stevin in 1585
wiskunde - dutch word for math, lit meaning art of what is known/ knowledge of what is certain

http://squeezehead.com/uniform-keyboard/
http://improvise.free.fr/
http://improvise.free.fr/altinst.htm
https://daskin.com/index.html
https://daskin.com/page5/page5.html
https://isomorphickeyboardoverlay.weebly.com/
http://www.dysartp.com/
http://musicnotation.org/wiki/instruments/janko-keyboard/
http://musicnotation.org/wiki/instruments/6-6-colored-traditional-7-5-keyboard/
https://en.xen.wiki/w/Microtonal_keyboards
https://bikexprt.com/music/bosanqet.htm

trichromatic vibraphone:
https://www.youtube.com/watch?v=sGXmPzspJWI

TODO: This web applet describes something called the MIDI api.
I don't have anything that hooks up to this,
but if I get a hold of such 
https://cifkao.github.io/tonnetz-viz/

Isomorphic keyboard on QWERTY
https://www.youtube.com/watch?v=2kxLhwZb7P8

Terpstra Keyboard Concept
https://www.youtube.com/watch?v=Nb_TQpwam54
Later rebranded as lumatone, I think.

Russian guy playing on qwerty janko
https://www.youtube.com/watch?v=myF39OL3rYA
https://www.youtube.com/watch?v=t-TBD2vhSd4
https://novayashkola.org/janko/keys.htm?
https://github.com/wcgbg/terpstrakeyboard/
-->