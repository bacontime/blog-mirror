---
title: Jianpu
subtitle: Simplified Numeric Musical Notation
parent: Art and Culture
has_children: false
layout: post
toc: false
date: 2022-12-29
---

<style>
@font-face {
    font-family: Jianpu;
    src: url("{{site.webfontdirectory}}/jianpu/JianpuASCII.ttf ");
}
.jianpu {
    font-family: Jianpu;
    line-height: 1.5;
    font-size: 20px;
}
</style>

You're almost certainly familiar with western staff notation 🎼, even if you don't know how to read it.

But this isn't the only system for recording music. 
I'm particularly fond of numbered musical notation,
which seems to be more commonly used in China, 
where it's sometimes called *jianpu*, meaning *simplified score*.

<aside hidden>
My granpa-in-law, for example only knows how to read this kind of notation. 
</aside>

In western staff notation, 
the shape of a symbol indicates that note's duration,
while the vertical position of the symbol indicates the note's pitch.

In jianpu, by contrast,
the shape of the symbol indicates its pitch.

The digits 1-7 are used to indicate the notes of the scale *do re mi fa so la ti*, while 0 indicates a rest.

For example, *Twinkle Twinkle Little Star* can be written

<pre class="jianpu">
| 1 1 5 5 | 6 6 5 - | 4 4 3 3 | 2 2 1 - |
</pre>
<pre class="jianpu">
| 5 5 4 4 | 3 3 2 - | 5 5 4 4 | 3 3 2 - | 
</pre>
<pre class="jianpu">
| 1 1 5 5 | 6 6 5 - | 4 4 3 3 | 2 2 1 - |
</pre>

The dashes indicate that the previous note should be extended by one quarter note.
Like in staff notation, a dot after a note indicate that a note's duration should be extended by 50%.

Some other bits of notation:
- Underlining a note halves its duration.
- Placing a dot above or below a note moves up or down an octave, respectively.
- Finally, if notes are vertically stacked, this means they should be played simultaneously as a chord.

These features are demonstrated in the following rendition of *Amazing Grace*, transcribed from [Wikipedia's page on jianpu](https://en.wikipedia.org/wiki/Numbered_musical_notation#Examples).



<pre class="jianpu">
5 |1' - q3'q1'| 3' - 2' |1' - 6|5 - 5|1' - q3'q1'|3' - q2'q3'|5' -
3 |3 - 5 |b7 -b7 |4 - 4|3 - 3|3 - 5 |1' - 5 |5 -
5, |1 - 1 | 1 - 1 |6, - 6,|1 - 1|5, - 5, |1 - 1 |7, -
1, |1, - 5, | 1, - 5, |4, - 4,|1, - 5,|1, - 3, |5, -   |5, -
 
2'/3'/|5' - 3'/1'/| 3' - 3'/2'/|1' - 6|5 - 5|1' - 3'/1'/|3' - 2'|1' - ||
5 |3 - 5 |b7 -b7 |4 - 4|3 - 3|3 - 5 |1' - 4|3 - ||
7, |5, - 1 | 1 - 1 |6, - 6,|1 - 1|5, - 5, |1 - 7,|1 - ||
5, |1, - 5, | 1, - 5, |4, - 4,|1, - 5,|1, - 1, |5, - 5,|1, - ||
</pre>

