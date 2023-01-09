---
title: Jianpu ASCII Font
subtitle: A font to quickly jot down jianpu notation using ASCII characters.
parent: Jianpu
grand_parent: Art and Culture
nav_order: 1
has_children: false
layout: post
toc: false
date: 2023-01-07
---

<style>
@font-face {
    font-family: Jianpu;
    src: url("{{site.webfontdirectory}}/jianpu/JianpuASCII.ttf");
}
.jianpu {
    font-family: Jianpu;
    line-height: 1.5;
    font-size: 150%
}
.lyrics {
    font-size: 75%
}
@media (max-width: 50rem) {
    .jianpu  {
        font-size: 120%;
    }
    .lyrics {
        font-size: 60%
    }
}
</style>


I wanted a way to quickly jot down some melodies using numerical notation,
so I threw together a little font which renders ascii characters into jianpu-style notation.

It uses `'` and `,` for overdots and underdots, and `/` for underlines.

The <a href="{{site.webfontdirectory}}/jianpu/JianpuASCII.ttf">font can be downloaded here</a>.
Or you can [read more about the font at its GitHub Repo](https://github.com/RobertWinslow/jianpu-ascii-font).

## Editable Example

Here's a text area which has the jianpu font applied.

<textarea style="width: 100%; height=15rem; padding: 1rem;" class="jianpu">
5 |1' - 3'/1'/| 3' - 2' |1' - 6|5 - 5|1' - 3'/q1'/|3' - 2'/3'/|5' -
3 |3 - 5 |b7 -b7 |4 - 4|3 - 3|3 - 5 |1' - 5 |5 -
5, |1 - 1 | 1 - 1 |6, - 6,|1 - 1|5, - 5, |1 - 1 |7, -
1, |1, - 5, | 1, - 5, |4, - 4,|1, - 5,|1, - 3, |5, -   |5, -
 
2'/3'/|5' - 3'/1'/| 3' - 3'/2'/|1' - 6|5 - 5|1' - 3'/1'/|3' - 2'|1' - ||
5 |3 - 5 |b7 -b7 |4 - 4|3 - 3|3 - 5 |1' - 4|3 - ||
7, |5, - 1 | 1 - 1 |6, - 6,|1 - 1|5, - 5, |1 - 7,|1 - ||
5, |1, - 5, | 1, - 5, |4, - 4,|1, - 5,|1, - 1, |5, - 5,|1, - ||
</textarea>