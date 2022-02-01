---
title: Open-source Emojis
grand_parent: Language
parent: Unicode Characters
---

# Comparison Table for a Few Open-Source Emoji Fonts

The tables below depict a few different open-source emoji fonts.
[A more complete comparison can be found here on the Unicode Consortium's website.](https://unicode.org/emoji/charts/full-emoji-list.html)
But all of the glyphs below are in the form of web fonts loaded by this page. And specifically, they are in the form of COLRv0 web fonts, which have near-universal support across platforms.


<details markdown='block'>
<summary> Click for more information about these fonts.</summary>

EmojiOne
: EmojiOne is an early set of emojis which hasn't been under development since Emoji version 4.0. It's published under the MiT license, and a closed-source successor is provided under the name [Joypixels](https://www.joypixels.com/emoji/flat). The assets for EmojiOne can be found in [this forked repo called EmojiTwo](https://github.com/EmojiTwo/emojitwo), and a COLRv0 version of the font [is provided by Mozilla](https://github.com/mozilla/twemoji-colr/releases/tag/v0.2.2). A backup version of the font (which should only be relevant on Chrome for MacOS) is [provided by Adobe](https://github.com/adobe-fonts/emojione-color).

[Twemoji](https://github.com/twitter/twemoji)
: Twemoji is Twitter's emoji set, and [a font implementation is provided by Mozilla here](https://github.com/mozilla/twemoji-colr), released under the Apache License. The version of the font in this page is actually a slight modification from the one published on Mozilla's repo; I recompiled it to fix [an issue where the font wouldn't render in some browsers on MacOS](https://github.com/mozilla/twemoji-colr/issues/50).


[OpenMoji](https://openmoji.org/)
: OpenMoji is an emoji set designed primarily by students and staff at the Schwäbisch Gmünd University of Design. It's released under the [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license. The main version of the font linked on the OpenMoji website is incredibly glitchy, and so the font loaded by this page [comes from a fork of the project's github repo](https://github.com/mavit/openmoji/tree/nanoemoji/font/glyf_colr_0).


There are several more open-source emoji sets out there, but none of the following are displayed on this page because of a lack of widely compatible font implementations (and also because the fonts that do exist are massive in size).
These additional emoji sets are:
- [Noto Color Emoji by Google](https://github.com/googlefonts/noto-emoji). Google is working on a COLR version of the font, but it's COLRv1. And whereas COLRv0 works basically everywhere, COLRv1 works basically nowhere (except for the Chrome beta).
- [Blobmoji](https://github.com/C1710/blobmoji), which keeps alive a much-beloved prior version of Google's Emoji set[.](https://github.com/C1710/blobmoji/blob/main/svg/emoji_u1f9a7.svg) 
- [Catmoji](https://github.com/catmoji/catmoji-colr). It's Twemoji, but they made all the smilies into cats.



<!--TODO: Link to a second version of the page with the full shebang. All the fonts, baybee.-->


</details>



The tables below cover most of the [emoji codepoints in version 13.0 of the standard](https://www.unicode.org/Public/emoji/13.0/emoji-test.txt), but I've left out most of the skin tone and gender variations (which comprise nearly half of the glyphs).








<!--
TODO: Recompile the EmojiOne from Mozilla but with a fixed layerize.js file
    I checked that I can drop in the e1 emojis into the modern less buggy twemoji compilation folder. 
    So I just need to update the metadata and so forth. Eh. Nevermind. It borked out at the very last minute. I think fixing the problems there would take more effort then its worth.
TODO: Clean up the extra fonts and licenses and whatnot floating around.
TODO: Share the tweaked versions of the fonts with the twemoji mozilla repo people.-->


<!--
For this page to display properly, you'll need to install the following font files:
- [Twitter Color Emoji SVGinOT Font](https://github.com/eosrei/twemoji-color-font/releases)
- [Google's Noto Color Emoji Font](https://github.com/googlefonts/noto-emoji/tree/main/fonts) (this one might only work on Windows 10)
- [A version of the OpenMoji font from here.](https://github.com/mavit/openmoji/tree/nanoemoji/font)
- [Blobmoji?](https://github.com/C1710/blobmoji)
- EmojiOne font?

https://www.guemil.info/

https://github.com/hfg-gmuend/openmoji/pull/260
https://github.com/mavit/openmoji/tree/nanoemoji/font
https://github.com/C1710/blobmoji
https://helpx.adobe.com/fonts/using/ot-svg-color-fonts.html
https://color.typekit.com/
https://stackoverflow.com/questions/43828750/how-to-use-google-noto-color-emoji-front-from-cdn-via-css
https://bugzilla.mozilla.org/show_bug.cgi?id=1454152

https://transfonter.org/
Sadly, this tool fails to preserve colors

Catmoji replaces all the twemoji smilies with cats.
https://github.com/catmoji/catmoji-colr

https://github.com/googlefonts/noto-emoji/issues/375


td:nth-child(2) {
  font-family: EmojiOne Color;
  font-size: 72px;
  padding: 0px;
}
td:nth-child(3) {
  font-family: Twitter Color Emoji;
  font-size: 72px;
  padding: 0px;
}
td:nth-child(4) {
  font-family: OpenMoji Color;
  font-size: 72px;
  padding: 0px;
}


Notes on font performances:

TwemojiMozilla.woff:
- Breaks on windowsFF, windowsChrome, and on mac, just everywhere it is borked.
- displays system default instead
- woff compressions just completely borked it I think

NotoColorEmoji-SVG.woff:
EmojiOneColor.woff2:
- renders on chrome, FF, 
- but always B&W. I think woff compressor strips the formatting.
- The woff2 from color.typekit.com is bigger than what I get doing the conversion myself. I think the online converters can't handle color fonts

NotoColorEmoji.ttf
- renders fine everywhere but FF. It's a known bug with FF. Just doesn't show up there at all. System default instead
- Trying to convert this (bitmap?) font to woff yields broken results.



EmojiOneColorAdobe.woff2  🌟🌟
- Works everywhere, but in windows/mac, it's only colorful in Firefox. 
- That's fine. That's what I expected.

TwemojiMozilla.ttf   🌟
 - works great on all the browsers on windows. renders in color, even in chrome
 - Also working on android
 - And so svelte!
 - great work mozilla team!
 - doesn't work on mac os chrome or mac os Firefox. works fine on mac os safari. 

OpenMoji-Color.COLRv0.ttf  🌟🌟🌟🌟
- Works everywhere I've tried it. Windows, Mac, android, ios
- reasonable size at only a bit over 2 MB. 
- Wowzers, I wish I could have figured out how to get nanoemoji working.

NotoSVGmiconv.woff2
- Doesn't work at all, sadly.

Blobmoji.ttf
- Only working in chromium browsers...
- Also, I think it's sometimes misaligned? Actually, no. I think that might have been a markdown formatting error on my part.

Catrinity.woff2
- Color was borked by conversion. What tool did Adobe use to get a functional color woff2?!

NotoEmoji.otf (SVG)
- monochrome. Works everywhere though.


NotoColorEmoji-SVG.otf
- So big!

Catrinity.otf



I generated some fonts on my mac. Hopefully these work.

TweMozMine.ttf
- Generated by following the steps from the Mozilla Twemoji repo

TwemojiNanoemoji.ttf 🌟🌟🌟🌟
- Generated using nanoemoji and color mode glyf_colr_0
- Works perfectly everywhere I've tried it. Can't figure out how to generalize the nanoemoji to other places





TwemojiMozillaBoundFix.ttf 🌟🌟🌟🌟
- generated from mozilla repo with tweaks to layerize.js
- nope. Didn't fix it. In fact, it's even more broken.
- I removed the spaces from the file name. That seems to have fixed it. 
- works on macos too now

Catmoji.ttf
- cats
- https://github.com/catmoji/catmoji-colr
- also made using grunt?
- but only works in chromium browsers?
- I am a confusion.
- Ah, despite the repo name, the latest release version doesn't actually have colr glyphs. But the authors uploaded a colr version in one of the issues pages.



I've spent too much time on this, so I should give up on trying to get the grunt twemoji mozilla whatsit to compile on windows. 
And just deal with the fact that I don't have a machine set up to handle this kind of task.
Oh well. I should have been doing other things today anyways.



Some variants on the twemoji mozilla, to test at which point it breaks.
I want to fully swap over a different emoji set into it.

TwemojiMozillaNoFlag.ttf
- just deleted the flags from the zip using 7zip

TwemojiSmallReplacement.ttf
- no flags, and also dropped in some noto emojis.
- They appear. It works. It's just... uh. They're teeny tiny.
- Oddly, it looks like twemoji has width 36 and noto has width 128. so I'm not sure why the noto would be *smaller*
- When I open the svg files in inkscape, sure enough, the noto assets are much bigger.
- It is worth noticing that the thumbnail for the svg files when view in MacOS is tiny and cornered as well. Not on windows though. It might be an operating system level misinterpretation.

I really wanted to compile the blobmojis to a COLRv0 font, but the blobmoji svgs are just too wonky.
It looks like Mozilla already made a COLRv0 version of the EmojiOne font though. 

EmojiOneMozilla.ttf

-->

## Tables of Emojis

<style>
td {
    vertical-align: middle;
}
@font-face {
  font-family: 'Mozilla EmojiOne';
  src: url(https://www.rmwinslow.com/posts/language/fonts/emojione/EmojiOneMozilla.ttf), url(https://www.rmwinslow.com/posts/language/fonts/emojione/EmojiOneColor.otf);
}
td:nth-child(2) {
  font-family: 'Mozilla EmojiOne';
  font-size: 48px;
  padding: 0px;
}

@font-face {
  font-family: 'Twemoji Fixed';
  src: url(https://www.rmwinslow.com/posts/language/fonts/twitter/TwemojiMozillaBoundFix.ttf);
}
td:nth-child(3) {
  font-family: 'Twemoji Fixed';
  font-size: 48px;
  padding: 0px;
}

@font-face {
  font-family: 'OpenMoji Nano';
  src: url(https://www.rmwinslow.com/posts/language/fonts/openmoji/OpenMoji-Color.COLRv0.ttf);
}
td:nth-child(4) {
  font-family: 'OpenMoji Nano';
  font-size: 48px;
  padding: 0px;
}

</style>






## Smileys & Emotion


### face-smiling

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| grinning face | &#x1F600; | &#x1F600; | &#x1F600; | 
| grinning face with big eyes | &#x1F603; | &#x1F603; | &#x1F603; | 
| grinning face with smiling eyes | &#x1F604; | &#x1F604; | &#x1F604; | 
| beaming face with smiling eyes | &#x1F601; | &#x1F601; | &#x1F601; | 
| grinning squinting face | &#x1F606; | &#x1F606; | &#x1F606; | 
| grinning face with sweat | &#x1F605; | &#x1F605; | &#x1F605; | 
| rolling on the floor laughing | &#x1F923; | &#x1F923; | &#x1F923; | 
| face with tears of joy | &#x1F602; | &#x1F602; | &#x1F602; | 
| slightly smiling face | &#x1F642; | &#x1F642; | &#x1F642; | 
| upside-down face | &#x1F643; | &#x1F643; | &#x1F643; | 
| winking face | &#x1F609; | &#x1F609; | &#x1F609; | 
| smiling face with smiling eyes | &#x1F60A; | &#x1F60A; | &#x1F60A; | 
| smiling face with halo | &#x1F607; | &#x1F607; | &#x1F607; | 

### face-affection

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| smiling face with hearts |  | &#x1F970; | &#x1F970; | 
| smiling face with heart-eyes | &#x1F60D; | &#x1F60D; | &#x1F60D; | 
| star-struck |  | &#x1F929; | &#x1F929; | 
| face blowing a kiss | &#x1F618; | &#x1F618; | &#x1F618; | 
| kissing face | &#x1F617; | &#x1F617; | &#x1F617; | 
| smiling face | &#x263A;&#xFE0F; | &#x263A;&#xFE0F; | &#x263A;&#xFE0F; | 
| kissing face with closed eyes | &#x1F61A; | &#x1F61A; | &#x1F61A; | 
| kissing face with smiling eyes | &#x1F619; | &#x1F619; | &#x1F619; | 
| smiling face with tear |  | &#x1F972; | &#x1F972; | 

### face-tongue

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| face savoring food | &#x1F60B; | &#x1F60B; | &#x1F60B; | 
| face with tongue | &#x1F61B; | &#x1F61B; | &#x1F61B; | 
| winking face with tongue | &#x1F61C; | &#x1F61C; | &#x1F61C; | 
| zany face |  | &#x1F92A; | &#x1F92A; | 
| squinting face with tongue | &#x1F61D; | &#x1F61D; | &#x1F61D; | 
| money-mouth face | &#x1F911; | &#x1F911; | &#x1F911; | 

### face-hand

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| hugging face | &#x1F917; | &#x1F917; | &#x1F917; | 
| face with hand over mouth |  | &#x1F92D; | &#x1F92D; | 
| shushing face |  | &#x1F92B; | &#x1F92B; | 
| thinking face | &#x1F914; | &#x1F914; | &#x1F914; | 

### face-neutral-skeptical

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| zipper-mouth face | &#x1F910; | &#x1F910; | &#x1F910; | 
| face with raised eyebrow |  | &#x1F928; | &#x1F928; | 
| neutral face | &#x1F610; | &#x1F610; | &#x1F610; | 
| expressionless face | &#x1F611; | &#x1F611; | &#x1F611; | 
| face without mouth | &#x1F636; | &#x1F636; | &#x1F636; | 
| smirking face | &#x1F60F; | &#x1F60F; | &#x1F60F; | 
| unamused face | &#x1F612; | &#x1F612; | &#x1F612; | 
| face with rolling eyes | &#x1F644; | &#x1F644; | &#x1F644; | 
| grimacing face | &#x1F62C; | &#x1F62C; | &#x1F62C; | 
| lying face | &#x1F925; | &#x1F925; | &#x1F925; | 

### face-sleepy

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| relieved face | &#x1F60C; | &#x1F60C; | &#x1F60C; | 
| pensive face | &#x1F614; | &#x1F614; | &#x1F614; | 
| sleepy face | &#x1F62A; | &#x1F62A; | &#x1F62A; | 
| drooling face | &#x1F924; | &#x1F924; | &#x1F924; | 
| sleeping face | &#x1F634; | &#x1F634; | &#x1F634; | 

### face-unwell

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| face with medical mask | &#x1F637; | &#x1F637; | &#x1F637; | 
| face with thermometer | &#x1F912; | &#x1F912; | &#x1F912; | 
| face with head-bandage | &#x1F915; | &#x1F915; | &#x1F915; | 
| nauseated face | &#x1F922; | &#x1F922; | &#x1F922; | 
| face vomiting |  | &#x1F92E; | &#x1F92E; | 
| sneezing face | &#x1F927; | &#x1F927; | &#x1F927; | 
| hot face |  | &#x1F975; | &#x1F975; | 
| cold face |  | &#x1F976; | &#x1F976; | 
| woozy face |  | &#x1F974; | &#x1F974; | 
| dizzy face | &#x1F635; | &#x1F635; | &#x1F635; | 
| exploding head |  | &#x1F92F; | &#x1F92F; | 

### face-hat

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| cowboy hat face | &#x1F920; | &#x1F920; | &#x1F920; | 
| partying face |  | &#x1F973; | &#x1F973; | 
| disguised face |  | &#x1F978; | &#x1F978; | 

### face-glasses

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| smiling face with sunglasses | &#x1F60E; | &#x1F60E; | &#x1F60E; | 
| nerd face | &#x1F913; | &#x1F913; | &#x1F913; | 
| face with monocle |  | &#x1F9D0; | &#x1F9D0; | 

### face-concerned

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| confused face | &#x1F615; | &#x1F615; | &#x1F615; | 
| worried face | &#x1F61F; | &#x1F61F; | &#x1F61F; | 
| slightly frowning face | &#x1F641; | &#x1F641; | &#x1F641; | 
| frowning face | &#x2639;&#xFE0F; | &#x2639;&#xFE0F; | &#x2639;&#xFE0F; | 
| face with open mouth | &#x1F62E; | &#x1F62E; | &#x1F62E; | 
| hushed face | &#x1F62F; | &#x1F62F; | &#x1F62F; | 
| astonished face | &#x1F632; | &#x1F632; | &#x1F632; | 
| flushed face | &#x1F633; | &#x1F633; | &#x1F633; | 
| pleading face |  | &#x1F97A; | &#x1F97A; | 
| frowning face with open mouth | &#x1F626; | &#x1F626; | &#x1F626; | 
| anguished face | &#x1F627; | &#x1F627; | &#x1F627; | 
| fearful face | &#x1F628; | &#x1F628; | &#x1F628; | 
| anxious face with sweat | &#x1F630; | &#x1F630; | &#x1F630; | 
| sad but relieved face | &#x1F625; | &#x1F625; | &#x1F625; | 
| crying face | &#x1F622; | &#x1F622; | &#x1F622; | 
| loudly crying face | &#x1F62D; | &#x1F62D; | &#x1F62D; | 
| face screaming in fear | &#x1F631; | &#x1F631; | &#x1F631; | 
| confounded face | &#x1F616; | &#x1F616; | &#x1F616; | 
| persevering face | &#x1F623; | &#x1F623; | &#x1F623; | 
| disappointed face | &#x1F61E; | &#x1F61E; | &#x1F61E; | 
| downcast face with sweat | &#x1F613; | &#x1F613; | &#x1F613; | 
| weary face | &#x1F629; | &#x1F629; | &#x1F629; | 
| tired face | &#x1F62B; | &#x1F62B; | &#x1F62B; | 
| yawning face |  | &#x1F971; | &#x1F971; | 

### face-negative

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| face with steam from nose | &#x1F624; | &#x1F624; | &#x1F624; | 
| pouting face | &#x1F621; | &#x1F621; | &#x1F621; | 
| angry face | &#x1F620; | &#x1F620; | &#x1F620; | 
| face with symbols on mouth |  | &#x1F92C; | &#x1F92C; | 
| smiling face with horns | &#x1F608; | &#x1F608; | &#x1F608; | 
| angry face with horns | &#x1F47F; | &#x1F47F; | &#x1F47F; | 
| skull | &#x1F480; | &#x1F480; | &#x1F480; | 
| skull and crossbones | &#x2620;&#xFE0F; | &#x2620;&#xFE0F; | &#x2620;&#xFE0F; | 

### face-costume

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| pile of poo | &#x1F4A9; | &#x1F4A9; | &#x1F4A9; | 
| clown face | &#x1F921; | &#x1F921; | &#x1F921; | 
| ogre | &#x1F479; | &#x1F479; | &#x1F479; | 
| goblin | &#x1F47A; | &#x1F47A; | &#x1F47A; | 
| ghost | &#x1F47B; | &#x1F47B; | &#x1F47B; | 
| alien | &#x1F47D; | &#x1F47D; | &#x1F47D; | 
| alien monster | &#x1F47E; | &#x1F47E; | &#x1F47E; | 
| robot | &#x1F916; | &#x1F916; | &#x1F916; | 

### cat-face

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| grinning cat | &#x1F63A; | &#x1F63A; | &#x1F63A; | 
| grinning cat with smiling eyes | &#x1F638; | &#x1F638; | &#x1F638; | 
| cat with tears of joy | &#x1F639; | &#x1F639; | &#x1F639; | 
| smiling cat with heart-eyes | &#x1F63B; | &#x1F63B; | &#x1F63B; | 
| cat with wry smile | &#x1F63C; | &#x1F63C; | &#x1F63C; | 
| kissing cat | &#x1F63D; | &#x1F63D; | &#x1F63D; | 
| weary cat | &#x1F640; | &#x1F640; | &#x1F640; | 
| crying cat | &#x1F63F; | &#x1F63F; | &#x1F63F; | 
| pouting cat | &#x1F63E; | &#x1F63E; | &#x1F63E; | 

### monkey-face

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| see-no-evil monkey | &#x1F648; | &#x1F648; | &#x1F648; | 
| hear-no-evil monkey | &#x1F649; | &#x1F649; | &#x1F649; | 
| speak-no-evil monkey | &#x1F64A; | &#x1F64A; | &#x1F64A; | 

### emotion

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| kiss mark | &#x1F48B; | &#x1F48B; | &#x1F48B; | 
| love letter | &#x1F48C; | &#x1F48C; | &#x1F48C; | 
| heart with arrow | &#x1F498; | &#x1F498; | &#x1F498; | 
| heart with ribbon | &#x1F49D; | &#x1F49D; | &#x1F49D; | 
| sparkling heart | &#x1F496; | &#x1F496; | &#x1F496; | 
| growing heart | &#x1F497; | &#x1F497; | &#x1F497; | 
| beating heart | &#x1F493; | &#x1F493; | &#x1F493; | 
| revolving hearts | &#x1F49E; | &#x1F49E; | &#x1F49E; | 
| two hearts | &#x1F495; | &#x1F495; | &#x1F495; | 
| heart decoration | &#x1F49F; | &#x1F49F; | &#x1F49F; | 
| heart exclamation | &#x2763;&#xFE0F; | &#x2763;&#xFE0F; | &#x2763;&#xFE0F; | 
| broken heart | &#x1F494; | &#x1F494; | &#x1F494; | 
| red heart | &#x2764;&#xFE0F; | &#x2764;&#xFE0F; | &#x2764;&#xFE0F; | 
| orange heart |  | &#x1F9E1; | &#x1F9E1; | 
| yellow heart | &#x1F49B; | &#x1F49B; | &#x1F49B; | 
| green heart | &#x1F49A; | &#x1F49A; | &#x1F49A; | 
| blue heart | &#x1F499; | &#x1F499; | &#x1F499; | 
| purple heart | &#x1F49C; | &#x1F49C; | &#x1F49C; | 
| brown heart |  | &#x1F90E; | &#x1F90E; | 
| black heart | &#x1F5A4; | &#x1F5A4; | &#x1F5A4; | 
| white heart |  | &#x1F90D; | &#x1F90D; | 
| hundred points | &#x1F4AF; | &#x1F4AF; | &#x1F4AF; | 
| anger symbol | &#x1F4A2; | &#x1F4A2; | &#x1F4A2; | 
| collision | &#x1F4A5; | &#x1F4A5; | &#x1F4A5; | 
| dizzy | &#x1F4AB; | &#x1F4AB; | &#x1F4AB; | 
| sweat droplets | &#x1F4A6; | &#x1F4A6; | &#x1F4A6; | 
| dashing away | &#x1F4A8; | &#x1F4A8; | &#x1F4A8; | 
| hole | &#x1F573;&#xFE0F; | &#x1F573;&#xFE0F; | &#x1F573;&#xFE0F; | 
| bomb | &#x1F4A3; | &#x1F4A3; | &#x1F4A3; | 
| speech balloon | &#x1F4AC; | &#x1F4AC; | &#x1F4AC; | 
| eye in speech bubble | &#x1F441;&#xFE0F;&#x200D;&#x1F5E8;&#xFE0F; | &#x1F441;&#xFE0F;&#x200D;&#x1F5E8;&#xFE0F; | &#x1F441;&#xFE0F;&#x200D;&#x1F5E8;&#xFE0F; | 
| left speech bubble | &#x1F5E8;&#xFE0F; | &#x1F5E8;&#xFE0F; | &#x1F5E8;&#xFE0F; | 
| right anger bubble | &#x1F5EF;&#xFE0F; | &#x1F5EF;&#xFE0F; | &#x1F5EF;&#xFE0F; | 
| thought balloon | &#x1F4AD; | &#x1F4AD; | &#x1F4AD; | 
| zzz | &#x1F4A4; | &#x1F4A4; | &#x1F4A4; | 

## People & Body


### hand-fingers-open

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| waving hand | &#x1F44B; | &#x1F44B; | &#x1F44B; | 
| raised back of hand | &#x1F91A; | &#x1F91A; | &#x1F91A; | 
| hand with fingers splayed | &#x1F590;&#xFE0F; | &#x1F590;&#xFE0F; | &#x1F590;&#xFE0F; | 
| raised hand | &#x270B; | &#x270B; | &#x270B; | 
| vulcan salute | &#x1F596; | &#x1F596; | &#x1F596; | 

### hand-fingers-partial

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| OK hand | &#x1F44C; | &#x1F44C; | &#x1F44C; | 
| pinched fingers |  | &#x1F90C; | &#x1F90C; | 
| pinching hand |  | &#x1F90F; | &#x1F90F; | 
| victory hand | &#x270C;&#xFE0F; | &#x270C;&#xFE0F; | &#x270C;&#xFE0F; | 
| crossed fingers | &#x1F91E; | &#x1F91E; | &#x1F91E; | 
| love-you gesture |  | &#x1F91F; | &#x1F91F; | 
| sign of the horns | &#x1F918; | &#x1F918; | &#x1F918; | 
| call me hand | &#x1F919; | &#x1F919; | &#x1F919; | 

### hand-single-finger

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| backhand index pointing left | &#x1F448; | &#x1F448; | &#x1F448; | 
| backhand index pointing right | &#x1F449; | &#x1F449; | &#x1F449; | 
| backhand index pointing up | &#x1F446; | &#x1F446; | &#x1F446; | 
| middle finger | &#x1F595; | &#x1F595; | &#x1F595; | 
| backhand index pointing down | &#x1F447; | &#x1F447; | &#x1F447; | 
| index pointing up | &#x261D;&#xFE0F; | &#x261D;&#xFE0F; | &#x261D;&#xFE0F; | 

### hand-fingers-closed

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| thumbs up | &#x1F44D; | &#x1F44D; | &#x1F44D; | 
| thumbs down | &#x1F44E; | &#x1F44E; | &#x1F44E; | 
| raised fist | &#x270A; | &#x270A; | &#x270A; | 
| oncoming fist | &#x1F44A; | &#x1F44A; | &#x1F44A; | 
| left-facing fist | &#x1F91B; | &#x1F91B; | &#x1F91B; | 
| right-facing fist | &#x1F91C; | &#x1F91C; | &#x1F91C; | 

### hands

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| clapping hands | &#x1F44F; | &#x1F44F; | &#x1F44F; | 
| raising hands | &#x1F64C; | &#x1F64C; | &#x1F64C; | 
| open hands | &#x1F450; | &#x1F450; | &#x1F450; | 
| palms up together |  | &#x1F932; | &#x1F932; | 
| handshake | &#x1F91D; | &#x1F91D; | &#x1F91D; | 
| folded hands | &#x1F64F; | &#x1F64F; | &#x1F64F; | 

### hand-prop

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| writing hand | &#x270D;&#xFE0F; | &#x270D;&#xFE0F; | &#x270D;&#xFE0F; | 
| nail polish | &#x1F485; | &#x1F485; | &#x1F485; | 
| selfie | &#x1F933; | &#x1F933; | &#x1F933; | 

### body-parts

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| flexed biceps | &#x1F4AA; | &#x1F4AA; | &#x1F4AA; | 
| mechanical arm |  | &#x1F9BE; | &#x1F9BE; | 
| mechanical leg |  | &#x1F9BF; | &#x1F9BF; | 
| leg |  | &#x1F9B5; | &#x1F9B5; | 
| foot |  | &#x1F9B6; | &#x1F9B6; | 
| ear | &#x1F442; | &#x1F442; | &#x1F442; | 
| ear with hearing aid |  | &#x1F9BB; | &#x1F9BB; | 
| nose | &#x1F443; | &#x1F443; | &#x1F443; | 
| brain |  | &#x1F9E0; | &#x1F9E0; | 
| anatomical heart |  | &#x1FAC0; | &#x1FAC0; | 
| lungs |  | &#x1FAC1; | &#x1FAC1; | 
| tooth |  | &#x1F9B7; | &#x1F9B7; | 
| bone |  | &#x1F9B4; | &#x1F9B4; | 
| eyes | &#x1F440; | &#x1F440; | &#x1F440; | 
| eye | &#x1F441;&#xFE0F; | &#x1F441;&#xFE0F; | &#x1F441;&#xFE0F; | 
| tongue | &#x1F445; | &#x1F445; | &#x1F445; | 
| mouth | &#x1F444; | &#x1F444; | &#x1F444; | 

### person

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| baby | &#x1F476; | &#x1F476; | &#x1F476; | 
| child |  | &#x1F9D2; | &#x1F9D2; | 
| boy | &#x1F466; | &#x1F466; | &#x1F466; | 
| girl | &#x1F467; | &#x1F467; | &#x1F467; | 
| person |  | &#x1F9D1; | &#x1F9D1; | 
| person: blond hair | &#x1F471; | &#x1F471; | &#x1F471; | 
| man | &#x1F468; | &#x1F468; | &#x1F468; | 
| man: beard |  | &#x1F9D4; | &#x1F9D4; | 
| man: red hair |  | &#x1F468;&#x200D;&#x1F9B0; | &#x1F468;&#x200D;&#x1F9B0; | 
| man: curly hair |  | &#x1F468;&#x200D;&#x1F9B1; | &#x1F468;&#x200D;&#x1F9B1; | 
| man: white hair |  | &#x1F468;&#x200D;&#x1F9B3; | &#x1F468;&#x200D;&#x1F9B3; | 
| man: bald |  | &#x1F468;&#x200D;&#x1F9B2; | &#x1F468;&#x200D;&#x1F9B2; | 
| woman | &#x1F469; | &#x1F469; | &#x1F469; | 
| woman: red hair |  | &#x1F469;&#x200D;&#x1F9B0; | &#x1F469;&#x200D;&#x1F9B0; | 
| person: red hair |  | &#x1F9D1;&#x200D;&#x1F9B0; | &#x1F9D1;&#x200D;&#x1F9B0; | 
| woman: curly hair |  | &#x1F469;&#x200D;&#x1F9B1; | &#x1F469;&#x200D;&#x1F9B1; | 
| person: curly hair |  | &#x1F9D1;&#x200D;&#x1F9B1; | &#x1F9D1;&#x200D;&#x1F9B1; | 
| woman: white hair |  | &#x1F469;&#x200D;&#x1F9B3; | &#x1F469;&#x200D;&#x1F9B3; | 
| person: white hair |  | &#x1F9D1;&#x200D;&#x1F9B3; | &#x1F9D1;&#x200D;&#x1F9B3; | 
| woman: bald |  | &#x1F469;&#x200D;&#x1F9B2; | &#x1F469;&#x200D;&#x1F9B2; | 
| person: bald |  | &#x1F9D1;&#x200D;&#x1F9B2; | &#x1F9D1;&#x200D;&#x1F9B2; | 
| woman: blond hair |  | &#x1F471;&#x200D;&#x2640;&#xFE0F; | &#x1F471;&#x200D;&#x2640;&#xFE0F; | 
| man: blond hair |  | &#x1F471;&#x200D;&#x2642;&#xFE0F; | &#x1F471;&#x200D;&#x2642;&#xFE0F; | 
| older person |  | &#x1F9D3; | &#x1F9D3; | 
| old man | &#x1F474; | &#x1F474; | &#x1F474; | 
| old woman | &#x1F475; | &#x1F475; | &#x1F475; | 

### person-gesture

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| person frowning | &#x1F64D; | &#x1F64D; | &#x1F64D; | 
| person pouting | &#x1F64E; | &#x1F64E; | &#x1F64E; | 
| person gesturing NO | &#x1F645; | &#x1F645; | &#x1F645; | 
| person gesturing OK | &#x1F646; | &#x1F646; | &#x1F646; | 
| person tipping hand | &#x1F481; | &#x1F481; | &#x1F481; | 
| person raising hand | &#x1F64B; | &#x1F64B; | &#x1F64B; | 
| deaf person |  | &#x1F9CF; | &#x1F9CF; | 
| person bowing | &#x1F647; | &#x1F647; | &#x1F647; | 
| person facepalming | &#x1F926; | &#x1F926; | &#x1F926; | 
| person shrugging | &#x1F937; | &#x1F937; | &#x1F937; | 


### person-role

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| health worker |  | &#x1F9D1;&#x200D;&#x2695;&#xFE0F; | &#x1F9D1;&#x200D;&#x2695;&#xFE0F; | 
| student |  | &#x1F9D1;&#x200D;&#x1F393; | &#x1F9D1;&#x200D;&#x1F393; | 
| teacher |  | &#x1F9D1;&#x200D;&#x1F3EB; | &#x1F9D1;&#x200D;&#x1F3EB; | 
| judge |  | &#x1F9D1;&#x200D;&#x2696;&#xFE0F; | &#x1F9D1;&#x200D;&#x2696;&#xFE0F; | 
| farmer |  | &#x1F9D1;&#x200D;&#x1F33E; | &#x1F9D1;&#x200D;&#x1F33E; | 
| cook |  | &#x1F9D1;&#x200D;&#x1F373; | &#x1F9D1;&#x200D;&#x1F373; | 
| mechanic |  | &#x1F9D1;&#x200D;&#x1F527; | &#x1F9D1;&#x200D;&#x1F527; | 
| factory worker |  | &#x1F9D1;&#x200D;&#x1F3ED; | &#x1F9D1;&#x200D;&#x1F3ED; | 
| office worker |  | &#x1F9D1;&#x200D;&#x1F4BC; | &#x1F9D1;&#x200D;&#x1F4BC; | 
| scientist |  | &#x1F9D1;&#x200D;&#x1F52C; | &#x1F9D1;&#x200D;&#x1F52C; | 
| technologist |  | &#x1F9D1;&#x200D;&#x1F4BB; | &#x1F9D1;&#x200D;&#x1F4BB; | 
| singer |  | &#x1F9D1;&#x200D;&#x1F3A4; | &#x1F9D1;&#x200D;&#x1F3A4; | 
| artist |  | &#x1F9D1;&#x200D;&#x1F3A8; | &#x1F9D1;&#x200D;&#x1F3A8; | 
| pilot |  | &#x1F9D1;&#x200D;&#x2708;&#xFE0F; | &#x1F9D1;&#x200D;&#x2708;&#xFE0F; | 
| astronaut |  | &#x1F9D1;&#x200D;&#x1F680; | &#x1F9D1;&#x200D;&#x1F680; | 
| firefighter |  | &#x1F9D1;&#x200D;&#x1F692; | &#x1F9D1;&#x200D;&#x1F692; | 
| police officer | &#x1F46E; | &#x1F46E; | &#x1F46E; | 
| detective | &#x1F575;&#xFE0F; | &#x1F575;&#xFE0F; | &#x1F575;&#xFE0F; | 
| guard | &#x1F482; | &#x1F482; | &#x1F482; | 
| ninja |  | &#x1F977; | &#x1F977; | 
| construction worker | &#x1F477; | &#x1F477; | &#x1F477; | 
| prince | &#x1F934; | &#x1F934; | &#x1F934; | 
| princess | &#x1F478; | &#x1F478; | &#x1F478; | 
| person wearing turban | &#x1F473; | &#x1F473; | &#x1F473; | 
| person with skullcap | &#x1F472; | &#x1F472; | &#x1F472; | 
| woman with headscarf |  | &#x1F9D5; | &#x1F9D5; | 
| person in tuxedo | &#x1F935; | &#x1F935; | &#x1F935; | 
| person with veil | &#x1F470; | &#x1F470; | &#x1F470; | 
| pregnant woman | &#x1F930; | &#x1F930; | &#x1F930; | 
| breast-feeding |  | &#x1F931; | &#x1F931; | 
| person feeding baby |  | &#x1F9D1;&#x200D;&#x1F37C; | &#x1F9D1;&#x200D;&#x1F37C; | 

### person-fantasy

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| baby angel | &#x1F47C; | &#x1F47C; | &#x1F47C; | 
| Santa Claus | &#x1F385; | &#x1F385; | &#x1F385; | 
| Mrs. Claus | &#x1F936; | &#x1F936; | &#x1F936; | 
| mx claus |  | &#x1F9D1;&#x200D;&#x1F384; | &#x1F9D1;&#x200D;&#x1F384; | 
| superhero |  | &#x1F9B8; | &#x1F9B8; | 
| man superhero |  | &#x1F9B8;&#x200D;&#x2642;&#xFE0F; | &#x1F9B8;&#x200D;&#x2642;&#xFE0F; | 
| woman superhero |  | &#x1F9B8;&#x200D;&#x2640;&#xFE0F; | &#x1F9B8;&#x200D;&#x2640;&#xFE0F; | 
| supervillain |  | &#x1F9B9; | &#x1F9B9; | 
| man supervillain |  | &#x1F9B9;&#x200D;&#x2642;&#xFE0F; | &#x1F9B9;&#x200D;&#x2642;&#xFE0F; | 
| woman supervillain |  | &#x1F9B9;&#x200D;&#x2640;&#xFE0F; | &#x1F9B9;&#x200D;&#x2640;&#xFE0F; | 
| mage |  | &#x1F9D9; | &#x1F9D9; | 
| man mage |  | &#x1F9D9;&#x200D;&#x2642;&#xFE0F; | &#x1F9D9;&#x200D;&#x2642;&#xFE0F; | 
| woman mage |  | &#x1F9D9;&#x200D;&#x2640;&#xFE0F; | &#x1F9D9;&#x200D;&#x2640;&#xFE0F; | 
| fairy |  | &#x1F9DA; | &#x1F9DA; | 
| man fairy |  | &#x1F9DA;&#x200D;&#x2642;&#xFE0F; | &#x1F9DA;&#x200D;&#x2642;&#xFE0F; | 
| woman fairy |  | &#x1F9DA;&#x200D;&#x2640;&#xFE0F; | &#x1F9DA;&#x200D;&#x2640;&#xFE0F; | 
| vampire |  | &#x1F9DB; | &#x1F9DB; | 
| man vampire |  | &#x1F9DB;&#x200D;&#x2642;&#xFE0F; | &#x1F9DB;&#x200D;&#x2642;&#xFE0F; | 
| woman vampire |  | &#x1F9DB;&#x200D;&#x2640;&#xFE0F; | &#x1F9DB;&#x200D;&#x2640;&#xFE0F; | 
| merperson |  | &#x1F9DC; | &#x1F9DC; | 
| merman |  | &#x1F9DC;&#x200D;&#x2642;&#xFE0F; | &#x1F9DC;&#x200D;&#x2642;&#xFE0F; | 
| mermaid |  | &#x1F9DC;&#x200D;&#x2640;&#xFE0F; | &#x1F9DC;&#x200D;&#x2640;&#xFE0F; | 
| elf |  | &#x1F9DD; | &#x1F9DD; | 
| man elf |  | &#x1F9DD;&#x200D;&#x2642;&#xFE0F; | &#x1F9DD;&#x200D;&#x2642;&#xFE0F; | 
| woman elf |  | &#x1F9DD;&#x200D;&#x2640;&#xFE0F; | &#x1F9DD;&#x200D;&#x2640;&#xFE0F; | 
| genie |  | &#x1F9DE; | &#x1F9DE; | 
| man genie |  | &#x1F9DE;&#x200D;&#x2642;&#xFE0F; | &#x1F9DE;&#x200D;&#x2642;&#xFE0F; | 
| woman genie |  | &#x1F9DE;&#x200D;&#x2640;&#xFE0F; | &#x1F9DE;&#x200D;&#x2640;&#xFE0F; | 
| zombie |  | &#x1F9DF; | &#x1F9DF; | 
| man zombie |  | &#x1F9DF;&#x200D;&#x2642;&#xFE0F; | &#x1F9DF;&#x200D;&#x2642;&#xFE0F; | 
| woman zombie |  | &#x1F9DF;&#x200D;&#x2640;&#xFE0F; | &#x1F9DF;&#x200D;&#x2640;&#xFE0F; | 

### person-activity

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| person getting massage | &#x1F486; | &#x1F486; | &#x1F486; | 
| person getting haircut | &#x1F487; | &#x1F487; | &#x1F487; | 
| person walking | &#x1F6B6; | &#x1F6B6; | &#x1F6B6; | 
| person standing |  | &#x1F9CD; | &#x1F9CD; | 
| person kneeling |  | &#x1F9CE; | &#x1F9CE; | 
| person with white cane |  | &#x1F9D1;&#x200D;&#x1F9AF; | &#x1F9D1;&#x200D;&#x1F9AF; | 
| person in motorized wheelchair |  | &#x1F9D1;&#x200D;&#x1F9BC; | &#x1F9D1;&#x200D;&#x1F9BC; | 
| person in manual wheelchair |  | &#x1F9D1;&#x200D;&#x1F9BD; | &#x1F9D1;&#x200D;&#x1F9BD; | 
| person running | &#x1F3C3; | &#x1F3C3; | &#x1F3C3; | 
| woman dancing | &#x1F483; | &#x1F483; | &#x1F483; | 
| man dancing | &#x1F57A; | &#x1F57A; | &#x1F57A; | 
| person in suit levitating | &#x1F574;&#xFE0F; | &#x1F574;&#xFE0F; | &#x1F574;&#xFE0F; | 
| people with bunny ears | &#x1F46F; | &#x1F46F; | &#x1F46F; | 
| men with bunny ears | &#x1F46F;&#x200D;&#x2642;&#xFE0F; | &#x1F46F;&#x200D;&#x2642;&#xFE0F; | &#x1F46F;&#x200D;&#x2642;&#xFE0F; | 
| women with bunny ears | &#x1F46F;&#x200D;&#x2640;&#xFE0F; | &#x1F46F;&#x200D;&#x2640;&#xFE0F; | &#x1F46F;&#x200D;&#x2640;&#xFE0F; | 
| person in steamy room |  | &#x1F9D6; | &#x1F9D6; | 
| person climbing |  | &#x1F9D7; | &#x1F9D7; | 


### person-sport

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| person fencing | &#x1F93A; | &#x1F93A; | &#x1F93A; | 
| horse racing | &#x1F3C7; | &#x1F3C7; | &#x1F3C7; | 
| skier | &#x26F7;&#xFE0F; | &#x26F7;&#xFE0F; | &#x26F7;&#xFE0F; | 
| snowboarder | &#x1F3C2; | &#x1F3C2; | &#x1F3C2; | 
| person golfing | &#x1F3CC;&#xFE0F; | &#x1F3CC;&#xFE0F; | &#x1F3CC;&#xFE0F; | 
| person surfing | &#x1F3C4; | &#x1F3C4; | &#x1F3C4; | 
| person rowing boat | &#x1F6A3; | &#x1F6A3; | &#x1F6A3; | 
| person swimming | &#x1F3CA; | &#x1F3CA; | &#x1F3CA; | 
| person bouncing ball | &#x26F9;&#xFE0F; | &#x26F9;&#xFE0F; | &#x26F9;&#xFE0F; | 
| person lifting weights | &#x1F3CB;&#xFE0F; | &#x1F3CB;&#xFE0F; | &#x1F3CB;&#xFE0F; | 
| person biking | &#x1F6B4; | &#x1F6B4; | &#x1F6B4; | 
| person mountain biking | &#x1F6B5; | &#x1F6B5; | &#x1F6B5; | 
| person cartwheeling | &#x1F938; | &#x1F938; | &#x1F938; | 
| people wrestling | &#x1F93C; | &#x1F93C; | &#x1F93C; | 
| person playing water polo | &#x1F93D; | &#x1F93D; | &#x1F93D; | 
| person playing handball | &#x1F93E; | &#x1F93E; | &#x1F93E; | 
| person juggling | &#x1F939; | &#x1F939; | &#x1F939; | 


### person-resting

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| person in lotus position |  | &#x1F9D8; | &#x1F9D8; | 
| person taking bath | &#x1F6C0; | &#x1F6C0; | &#x1F6C0; | 
| person in bed | &#x1F6CC; | &#x1F6CC; | &#x1F6CC; | 

### family

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| people holding hands |  | &#x1F9D1;&#x200D;&#x1F91D;&#x200D;&#x1F9D1; | &#x1F9D1;&#x200D;&#x1F91D;&#x200D;&#x1F9D1; | 
| women holding hands | &#x1F46D; | &#x1F46D; | &#x1F46D; | 
| woman and man holding hands | &#x1F46B; | &#x1F46B; | &#x1F46B; | 
| men holding hands | &#x1F46C; | &#x1F46C; | &#x1F46C; | 
| kiss | &#x1F48F; | &#x1F48F; | &#x1F48F; | 
| kiss: woman, man | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | 
| kiss: man, man | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F468; | 
| kiss: woman, woman | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F469; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F469; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F48B;&#x200D;&#x1F469; | 
| couple with heart | &#x1F491; | &#x1F491; | &#x1F491; | 
| couple with heart: woman, man | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | 
| couple with heart: man, man | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | &#x1F468;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F468; | 
| couple with heart: woman, woman | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F469; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F469; | &#x1F469;&#x200D;&#x2764;&#xFE0F;&#x200D;&#x1F469; | 
| family | &#x1F46A; | &#x1F46A; | &#x1F46A; | 
| family: man, woman, boy | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466; | 
| family: man, woman, girl | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467; | 
| family: man, woman, girl, boy | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | 
| family: man, woman, boy, boy | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | 
| family: man, woman, girl, girl | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | 
| family: man, man, boy | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466; | 
| family: man, man, girl | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467; | 
| family: man, man, girl, boy | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F466; | 
| family: man, man, boy, boy | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F466;&#x200D;&#x1F466; | 
| family: man, man, girl, girl | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F467; | 
| family: woman, woman, boy | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466; | 
| family: woman, woman, girl | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467; | 
| family: woman, woman, girl, boy | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | 
| family: woman, woman, boy, boy | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | 
| family: woman, woman, girl, girl | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | 
| family: man, boy |   | &#x1F468;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F466; | 
| family: man, boy, boy |   | &#x1F468;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F466;&#x200D;&#x1F466; | 
| family: man, girl |   | &#x1F468;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F467; | 
| family: man, girl, boy |   | &#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F466; | 
| family: man, girl, girl |   | &#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F468;&#x200D;&#x1F467;&#x200D;&#x1F467; | 
| family: woman, boy |   | &#x1F469;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F466; | 
| family: woman, boy, boy |   | &#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F466;&#x200D;&#x1F466; | 
| family: woman, girl |   | &#x1F469;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F467; | 
| family: woman, girl, boy |   | &#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | &#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F466; | 
| family: woman, girl, girl |   | &#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | &#x1F469;&#x200D;&#x1F467;&#x200D;&#x1F467; | 

### person-symbol

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| speaking head | &#x1F5E3;&#xFE0F; | &#x1F5E3;&#xFE0F; | &#x1F5E3;&#xFE0F; | 
| bust in silhouette | &#x1F464; | &#x1F464; | &#x1F464; | 
| busts in silhouette | &#x1F465; | &#x1F465; | &#x1F465; | 
| people hugging |  | &#x1FAC2; | &#x1FAC2; | 
| footprints | &#x1F463; | &#x1F463; | &#x1F463; | 

## Animals & Nature


### animal-mammal

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| monkey face | &#x1F435; | &#x1F435; | &#x1F435; | 
| monkey | &#x1F412; | &#x1F412; | &#x1F412; | 
| gorilla | &#x1F98D; | &#x1F98D; | &#x1F98D; | 
| orangutan |  | &#x1F9A7; | &#x1F9A7; | 
| dog face | &#x1F436; | &#x1F436; | &#x1F436; | 
| dog | &#x1F415; | &#x1F415; | &#x1F415; | 
| guide dog |  | &#x1F9AE; | &#x1F9AE; | 
| service dog |  | &#x1F415;&#x200D;&#x1F9BA; | &#x1F415;&#x200D;&#x1F9BA; | 
| poodle | &#x1F429; | &#x1F429; | &#x1F429; | 
| wolf | &#x1F43A; | &#x1F43A; | &#x1F43A; | 
| fox | &#x1F98A; | &#x1F98A; | &#x1F98A; | 
| raccoon |  | &#x1F99D; | &#x1F99D; | 
| cat face | &#x1F431; | &#x1F431; | &#x1F431; | 
| cat | &#x1F408; | &#x1F408; | &#x1F408; | 
| black cat |  | &#x1F408;&#x200D;&#x2B1B; | &#x1F408;&#x200D;&#x2B1B; | 
| lion | &#x1F981; | &#x1F981; | &#x1F981; | 
| tiger face | &#x1F42F; | &#x1F42F; | &#x1F42F; | 
| tiger | &#x1F405; | &#x1F405; | &#x1F405; | 
| leopard | &#x1F406; | &#x1F406; | &#x1F406; | 
| horse face | &#x1F434; | &#x1F434; | &#x1F434; | 
| horse | &#x1F40E; | &#x1F40E; | &#x1F40E; | 
| unicorn | &#x1F984; | &#x1F984; | &#x1F984; | 
| zebra |  | &#x1F993; | &#x1F993; | 
| deer | &#x1F98C; | &#x1F98C; | &#x1F98C; | 
| bison |  | &#x1F9AC; | &#x1F9AC; | 
| cow face | &#x1F42E; | &#x1F42E; | &#x1F42E; | 
| ox | &#x1F402; | &#x1F402; | &#x1F402; | 
| water buffalo | &#x1F403; | &#x1F403; | &#x1F403; | 
| cow | &#x1F404; | &#x1F404; | &#x1F404; | 
| pig face | &#x1F437; | &#x1F437; | &#x1F437; | 
| pig | &#x1F416; | &#x1F416; | &#x1F416; | 
| boar | &#x1F417; | &#x1F417; | &#x1F417; | 
| pig nose | &#x1F43D; | &#x1F43D; | &#x1F43D; | 
| ram | &#x1F40F; | &#x1F40F; | &#x1F40F; | 
| ewe | &#x1F411; | &#x1F411; | &#x1F411; | 
| goat | &#x1F410; | &#x1F410; | &#x1F410; | 
| camel | &#x1F42A; | &#x1F42A; | &#x1F42A; | 
| two-hump camel | &#x1F42B; | &#x1F42B; | &#x1F42B; | 
| llama |  | &#x1F999; | &#x1F999; | 
| giraffe |  | &#x1F992; | &#x1F992; | 
| elephant | &#x1F418; | &#x1F418; | &#x1F418; | 
| mammoth |  | &#x1F9A3; | &#x1F9A3; | 
| rhinoceros | &#x1F98F; | &#x1F98F; | &#x1F98F; | 
| hippopotamus |  | &#x1F99B; | &#x1F99B; | 
| mouse face | &#x1F42D; | &#x1F42D; | &#x1F42D; | 
| mouse | &#x1F401; | &#x1F401; | &#x1F401; | 
| rat | &#x1F400; | &#x1F400; | &#x1F400; | 
| hamster | &#x1F439; | &#x1F439; | &#x1F439; | 
| rabbit face | &#x1F430; | &#x1F430; | &#x1F430; | 
| rabbit | &#x1F407; | &#x1F407; | &#x1F407; | 
| chipmunk | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | 
| beaver |  | &#x1F9AB; | &#x1F9AB; | 
| hedgehog |  | &#x1F994; | &#x1F994; | 
| bat | &#x1F987; | &#x1F987; | &#x1F987; | 
| bear | &#x1F43B; | &#x1F43B; | &#x1F43B; | 
| polar bear |  | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | 
| koala | &#x1F428; | &#x1F428; | &#x1F428; | 
| panda | &#x1F43C; | &#x1F43C; | &#x1F43C; | 
| sloth |  | &#x1F9A5; | &#x1F9A5; | 
| otter |  | &#x1F9A6; | &#x1F9A6; | 
| skunk |  | &#x1F9A8; | &#x1F9A8; | 
| kangaroo |  | &#x1F998; | &#x1F998; | 
| badger |  | &#x1F9A1; | &#x1F9A1; | 
| paw prints | &#x1F43E; | &#x1F43E; | &#x1F43E; | 

### animal-bird

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| turkey | &#x1F983; | &#x1F983; | &#x1F983; | 
| chicken | &#x1F414; | &#x1F414; | &#x1F414; | 
| rooster | &#x1F413; | &#x1F413; | &#x1F413; | 
| hatching chick | &#x1F423; | &#x1F423; | &#x1F423; | 
| baby chick | &#x1F424; | &#x1F424; | &#x1F424; | 
| front-facing baby chick | &#x1F425; | &#x1F425; | &#x1F425; | 
| bird | &#x1F426; | &#x1F426; | &#x1F426; | 
| penguin | &#x1F427; | &#x1F427; | &#x1F427; | 
| dove | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | 
| eagle | &#x1F985; | &#x1F985; | &#x1F985; | 
| duck | &#x1F986; | &#x1F986; | &#x1F986; | 
| swan |  | &#x1F9A2; | &#x1F9A2; | 
| owl | &#x1F989; | &#x1F989; | &#x1F989; | 
| dodo |  | &#x1F9A4; | &#x1F9A4; | 
| feather |  | &#x1FAB6; | &#x1FAB6; | 
| flamingo |  | &#x1F9A9; | &#x1F9A9; | 
| peacock |  | &#x1F99A; | &#x1F99A; | 
| parrot |  | &#x1F99C; | &#x1F99C; | 

### animal-amphibian

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| frog | &#x1F438; | &#x1F438; | &#x1F438; | 

### animal-reptile

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| crocodile | &#x1F40A; | &#x1F40A; | &#x1F40A; | 
| turtle | &#x1F422; | &#x1F422; | &#x1F422; | 
| lizard | &#x1F98E; | &#x1F98E; | &#x1F98E; | 
| snake | &#x1F40D; | &#x1F40D; | &#x1F40D; | 
| dragon face | &#x1F432; | &#x1F432; | &#x1F432; | 
| dragon | &#x1F409; | &#x1F409; | &#x1F409; | 
| sauropod |  | &#x1F995; | &#x1F995; | 
| T-Rex |  | &#x1F996; | &#x1F996; | 

### animal-marine

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| spouting whale | &#x1F433; | &#x1F433; | &#x1F433; | 
| whale | &#x1F40B; | &#x1F40B; | &#x1F40B; | 
| dolphin | &#x1F42C; | &#x1F42C; | &#x1F42C; | 
| seal |  | &#x1F9AD; | &#x1F9AD; | 
| fish | &#x1F41F; | &#x1F41F; | &#x1F41F; | 
| tropical fish | &#x1F420; | &#x1F420; | &#x1F420; | 
| blowfish | &#x1F421; | &#x1F421; | &#x1F421; | 
| shark | &#x1F988; | &#x1F988; | &#x1F988; | 
| octopus | &#x1F419; | &#x1F419; | &#x1F419; | 
| spiral shell | &#x1F41A; | &#x1F41A; | &#x1F41A; | 

### animal-bug

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| snail | &#x1F40C; | &#x1F40C; | &#x1F40C; | 
| butterfly | &#x1F98B; | &#x1F98B; | &#x1F98B; | 
| bug | &#x1F41B; | &#x1F41B; | &#x1F41B; | 
| ant | &#x1F41C; | &#x1F41C; | &#x1F41C; | 
| honeybee | &#x1F41D; | &#x1F41D; | &#x1F41D; | 
| beetle |  | &#x1FAB2; | &#x1FAB2; | 
| lady beetle | &#x1F41E; | &#x1F41E; | &#x1F41E; | 
| cricket |  | &#x1F997; | &#x1F997; | 
| cockroach |  | &#x1FAB3; | &#x1FAB3; | 
| spider | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | 
| spider web | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | 
| scorpion | &#x1F982; | &#x1F982; | &#x1F982; | 
| mosquito |  | &#x1F99F; | &#x1F99F; | 
| fly |  | &#x1FAB0; | &#x1FAB0; | 
| worm |  | &#x1FAB1; | &#x1FAB1; | 
| microbe |  | &#x1F9A0; | &#x1F9A0; | 

### plant-flower

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| bouquet | &#x1F490; | &#x1F490; | &#x1F490; | 
| cherry blossom | &#x1F338; | &#x1F338; | &#x1F338; | 
| white flower | &#x1F4AE; | &#x1F4AE; | &#x1F4AE; | 
| rosette | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | 
| rose | &#x1F339; | &#x1F339; | &#x1F339; | 
| wilted flower | &#x1F940; | &#x1F940; | &#x1F940; | 
| hibiscus | &#x1F33A; | &#x1F33A; | &#x1F33A; | 
| sunflower | &#x1F33B; | &#x1F33B; | &#x1F33B; | 
| blossom | &#x1F33C; | &#x1F33C; | &#x1F33C; | 
| tulip | &#x1F337; | &#x1F337; | &#x1F337; | 

### plant-other

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| seedling | &#x1F331; | &#x1F331; | &#x1F331; | 
| potted plant |  | &#x1FAB4; | &#x1FAB4; | 
| evergreen tree | &#x1F332; | &#x1F332; | &#x1F332; | 
| deciduous tree | &#x1F333; | &#x1F333; | &#x1F333; | 
| palm tree | &#x1F334; | &#x1F334; | &#x1F334; | 
| cactus | &#x1F335; | &#x1F335; | &#x1F335; | 
| sheaf of rice | &#x1F33E; | &#x1F33E; | &#x1F33E; | 
| herb | &#x1F33F; | &#x1F33F; | &#x1F33F; | 
| shamrock | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | 
| four leaf clover | &#x1F340; | &#x1F340; | &#x1F340; | 
| maple leaf | &#x1F341; | &#x1F341; | &#x1F341; | 
| fallen leaf | &#x1F342; | &#x1F342; | &#x1F342; | 
| leaf fluttering in wind | &#x1F343; | &#x1F343; | &#x1F343; | 

## Food & Drink


### food-fruit

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| grapes | &#x1F347; | &#x1F347; | &#x1F347; | 
| melon | &#x1F348; | &#x1F348; | &#x1F348; | 
| watermelon | &#x1F349; | &#x1F349; | &#x1F349; | 
| tangerine | &#x1F34A; | &#x1F34A; | &#x1F34A; | 
| lemon | &#x1F34B; | &#x1F34B; | &#x1F34B; | 
| banana | &#x1F34C; | &#x1F34C; | &#x1F34C; | 
| pineapple | &#x1F34D; | &#x1F34D; | &#x1F34D; | 
| mango |  | &#x1F96D; | &#x1F96D; | 
| red apple | &#x1F34E; | &#x1F34E; | &#x1F34E; | 
| green apple | &#x1F34F; | &#x1F34F; | &#x1F34F; | 
| pear | &#x1F350; | &#x1F350; | &#x1F350; | 
| peach | &#x1F351; | &#x1F351; | &#x1F351; | 
| cherries | &#x1F352; | &#x1F352; | &#x1F352; | 
| strawberry | &#x1F353; | &#x1F353; | &#x1F353; | 
| blueberries |  | &#x1FAD0; | &#x1FAD0; | 
| kiwi fruit | &#x1F95D; | &#x1F95D; | &#x1F95D; | 
| tomato | &#x1F345; | &#x1F345; | &#x1F345; | 
| olive |  | &#x1FAD2; | &#x1FAD2; | 
| coconut |  | &#x1F965; | &#x1F965; | 

### food-vegetable

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| avocado | &#x1F951; | &#x1F951; | &#x1F951; | 
| eggplant | &#x1F346; | &#x1F346; | &#x1F346; | 
| potato | &#x1F954; | &#x1F954; | &#x1F954; | 
| carrot | &#x1F955; | &#x1F955; | &#x1F955; | 
| ear of corn | &#x1F33D; | &#x1F33D; | &#x1F33D; | 
| hot pepper | &#x1F336;&#xFE0F; | &#x1F336;&#xFE0F; | &#x1F336;&#xFE0F; | 
| bell pepper |  | &#x1FAD1; | &#x1FAD1; | 
| cucumber | &#x1F952; | &#x1F952; | &#x1F952; | 
| leafy green |  | &#x1F96C; | &#x1F96C; | 
| broccoli |  | &#x1F966; | &#x1F966; | 
| garlic |  | &#x1F9C4; | &#x1F9C4; | 
| onion |  | &#x1F9C5; | &#x1F9C5; | 
| mushroom | &#x1F344; | &#x1F344; | &#x1F344; | 
| peanuts | &#x1F95C; | &#x1F95C; | &#x1F95C; | 
| chestnut | &#x1F330; | &#x1F330; | &#x1F330; | 

### food-prepared

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| bread | &#x1F35E; | &#x1F35E; | &#x1F35E; | 
| croissant | &#x1F950; | &#x1F950; | &#x1F950; | 
| baguette bread | &#x1F956; | &#x1F956; | &#x1F956; | 
| flatbread |  | &#x1FAD3; | &#x1FAD3; | 
| pretzel |  | &#x1F968; | &#x1F968; | 
| bagel |  | &#x1F96F; | &#x1F96F; | 
| pancakes | &#x1F95E; | &#x1F95E; | &#x1F95E; | 
| waffle |  | &#x1F9C7; | &#x1F9C7; | 
| cheese wedge | &#x1F9C0; | &#x1F9C0; | &#x1F9C0; | 
| meat on bone | &#x1F356; | &#x1F356; | &#x1F356; | 
| poultry leg | &#x1F357; | &#x1F357; | &#x1F357; | 
| cut of meat |  | &#x1F969; | &#x1F969; | 
| bacon | &#x1F953; | &#x1F953; | &#x1F953; | 
| hamburger | &#x1F354; | &#x1F354; | &#x1F354; | 
| french fries | &#x1F35F; | &#x1F35F; | &#x1F35F; | 
| pizza | &#x1F355; | &#x1F355; | &#x1F355; | 
| hot dog | &#x1F32D; | &#x1F32D; | &#x1F32D; | 
| sandwich |  | &#x1F96A; | &#x1F96A; | 
| taco | &#x1F32E; | &#x1F32E; | &#x1F32E; | 
| burrito | &#x1F32F; | &#x1F32F; | &#x1F32F; | 
| tamale |  | &#x1FAD4; | &#x1FAD4; | 
| stuffed flatbread | &#x1F959; | &#x1F959; | &#x1F959; | 
| falafel |  | &#x1F9C6; | &#x1F9C6; | 
| egg | &#x1F95A; | &#x1F95A; | &#x1F95A; | 
| cooking | &#x1F373; | &#x1F373; | &#x1F373; | 
| shallow pan of food | &#x1F958; | &#x1F958; | &#x1F958; | 
| pot of food | &#x1F372; | &#x1F372; | &#x1F372; | 
| fondue |  | &#x1FAD5; | &#x1FAD5; | 
| bowl with spoon |  | &#x1F963; | &#x1F963; | 
| green salad | &#x1F957; | &#x1F957; | &#x1F957; | 
| popcorn | &#x1F37F; | &#x1F37F; | &#x1F37F; | 
| butter |  | &#x1F9C8; | &#x1F9C8; | 
| salt |  | &#x1F9C2; | &#x1F9C2; | 
| canned food |  | &#x1F96B; | &#x1F96B; | 

### food-asian

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| bento box | &#x1F371; | &#x1F371; | &#x1F371; | 
| rice cracker | &#x1F358; | &#x1F358; | &#x1F358; | 
| rice ball | &#x1F359; | &#x1F359; | &#x1F359; | 
| cooked rice | &#x1F35A; | &#x1F35A; | &#x1F35A; | 
| curry rice | &#x1F35B; | &#x1F35B; | &#x1F35B; | 
| steaming bowl | &#x1F35C; | &#x1F35C; | &#x1F35C; | 
| spaghetti | &#x1F35D; | &#x1F35D; | &#x1F35D; | 
| roasted sweet potato | &#x1F360; | &#x1F360; | &#x1F360; | 
| oden | &#x1F362; | &#x1F362; | &#x1F362; | 
| sushi | &#x1F363; | &#x1F363; | &#x1F363; | 
| fried shrimp | &#x1F364; | &#x1F364; | &#x1F364; | 
| fish cake with swirl | &#x1F365; | &#x1F365; | &#x1F365; | 
| moon cake |  | &#x1F96E; | &#x1F96E; | 
| dango | &#x1F361; | &#x1F361; | &#x1F361; | 
| dumpling |  | &#x1F95F; | &#x1F95F; | 
| fortune cookie |  | &#x1F960; | &#x1F960; | 
| takeout box |  | &#x1F961; | &#x1F961; | 

### food-marine

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| crab | &#x1F980; | &#x1F980; | &#x1F980; | 
| lobster |  | &#x1F99E; | &#x1F99E; | 
| shrimp | &#x1F990; | &#x1F990; | &#x1F990; | 
| squid | &#x1F991; | &#x1F991; | &#x1F991; | 
| oyster |  | &#x1F9AA; | &#x1F9AA; | 

### food-sweet

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| soft ice cream | &#x1F366; | &#x1F366; | &#x1F366; | 
| shaved ice | &#x1F367; | &#x1F367; | &#x1F367; | 
| ice cream | &#x1F368; | &#x1F368; | &#x1F368; | 
| doughnut | &#x1F369; | &#x1F369; | &#x1F369; | 
| cookie | &#x1F36A; | &#x1F36A; | &#x1F36A; | 
| birthday cake | &#x1F382; | &#x1F382; | &#x1F382; | 
| shortcake | &#x1F370; | &#x1F370; | &#x1F370; | 
| cupcake |  | &#x1F9C1; | &#x1F9C1; | 
| pie |  | &#x1F967; | &#x1F967; | 
| chocolate bar | &#x1F36B; | &#x1F36B; | &#x1F36B; | 
| candy | &#x1F36C; | &#x1F36C; | &#x1F36C; | 
| lollipop | &#x1F36D; | &#x1F36D; | &#x1F36D; | 
| custard | &#x1F36E; | &#x1F36E; | &#x1F36E; | 
| honey pot | &#x1F36F; | &#x1F36F; | &#x1F36F; | 

### drink

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| baby bottle | &#x1F37C; | &#x1F37C; | &#x1F37C; | 
| glass of milk | &#x1F95B; | &#x1F95B; | &#x1F95B; | 
| hot beverage | &#x2615; | &#x2615; | &#x2615; | 
| teapot |  | &#x1FAD6; | &#x1FAD6; | 
| teacup without handle | &#x1F375; | &#x1F375; | &#x1F375; | 
| sake | &#x1F376; | &#x1F376; | &#x1F376; | 
| bottle with popping cork | &#x1F37E; | &#x1F37E; | &#x1F37E; | 
| wine glass | &#x1F377; | &#x1F377; | &#x1F377; | 
| cocktail glass | &#x1F378; | &#x1F378; | &#x1F378; | 
| tropical drink | &#x1F379; | &#x1F379; | &#x1F379; | 
| beer mug | &#x1F37A; | &#x1F37A; | &#x1F37A; | 
| clinking beer mugs | &#x1F37B; | &#x1F37B; | &#x1F37B; | 
| clinking glasses | &#x1F942; | &#x1F942; | &#x1F942; | 
| tumbler glass | &#x1F943; | &#x1F943; | &#x1F943; | 
| cup with straw |  | &#x1F964; | &#x1F964; | 
| bubble tea |  | &#x1F9CB; | &#x1F9CB; | 
| beverage box |  | &#x1F9C3; | &#x1F9C3; | 
| mate |  | &#x1F9C9; | &#x1F9C9; | 
| ice |  | &#x1F9CA; | &#x1F9CA; | 

### dishware

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| chopsticks |  | &#x1F962; | &#x1F962; | 
| fork and knife with plate | &#x1F37D;&#xFE0F; | &#x1F37D;&#xFE0F; | &#x1F37D;&#xFE0F; | 
| fork and knife | &#x1F374; | &#x1F374; | &#x1F374; | 
| spoon | &#x1F944; | &#x1F944; | &#x1F944; | 
| kitchen knife | &#x1F52A; | &#x1F52A; | &#x1F52A; | 
| amphora | &#x1F3FA; | &#x1F3FA; | &#x1F3FA; | 

## Travel & Places


### place-map

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| globe showing Europe-Africa | &#x1F30D; | &#x1F30D; | &#x1F30D; | 
| globe showing Americas | &#x1F30E; | &#x1F30E; | &#x1F30E; | 
| globe showing Asia-Australia | &#x1F30F; | &#x1F30F; | &#x1F30F; | 
| globe with meridians | &#x1F310; | &#x1F310; | &#x1F310; | 
| world map | &#x1F5FA;&#xFE0F; | &#x1F5FA;&#xFE0F; | &#x1F5FA;&#xFE0F; | 
| map of Japan | &#x1F5FE; | &#x1F5FE; | &#x1F5FE; | 
| compass |  | &#x1F9ED; | &#x1F9ED; | 

### place-geographic

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| snow-capped mountain | &#x1F3D4;&#xFE0F; | &#x1F3D4;&#xFE0F; | &#x1F3D4;&#xFE0F; | 
| mountain | &#x26F0;&#xFE0F; | &#x26F0;&#xFE0F; | &#x26F0;&#xFE0F; | 
| volcano | &#x1F30B; | &#x1F30B; | &#x1F30B; | 
| mount fuji | &#x1F5FB; | &#x1F5FB; | &#x1F5FB; | 
| camping | &#x1F3D5;&#xFE0F; | &#x1F3D5;&#xFE0F; | &#x1F3D5;&#xFE0F; | 
| beach with umbrella | &#x1F3D6;&#xFE0F; | &#x1F3D6;&#xFE0F; | &#x1F3D6;&#xFE0F; | 
| desert | &#x1F3DC;&#xFE0F; | &#x1F3DC;&#xFE0F; | &#x1F3DC;&#xFE0F; | 
| desert island | &#x1F3DD;&#xFE0F; | &#x1F3DD;&#xFE0F; | &#x1F3DD;&#xFE0F; | 
| national park | &#x1F3DE;&#xFE0F; | &#x1F3DE;&#xFE0F; | &#x1F3DE;&#xFE0F; | 

### place-building

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| stadium | &#x1F3DF;&#xFE0F; | &#x1F3DF;&#xFE0F; | &#x1F3DF;&#xFE0F; | 
| classical building | &#x1F3DB;&#xFE0F; | &#x1F3DB;&#xFE0F; | &#x1F3DB;&#xFE0F; | 
| building construction | &#x1F3D7;&#xFE0F; | &#x1F3D7;&#xFE0F; | &#x1F3D7;&#xFE0F; | 
| brick |  | &#x1F9F1; | &#x1F9F1; | 
| rock |  | &#x1FAA8; | &#x1FAA8; | 
| wood |  | &#x1FAB5; | &#x1FAB5; | 
| hut |  | &#x1F6D6; | &#x1F6D6; | 
| houses | &#x1F3D8;&#xFE0F; | &#x1F3D8;&#xFE0F; | &#x1F3D8;&#xFE0F; | 
| derelict house | &#x1F3DA;&#xFE0F; | &#x1F3DA;&#xFE0F; | &#x1F3DA;&#xFE0F; | 
| house | &#x1F3E0; | &#x1F3E0; | &#x1F3E0; | 
| house with garden | &#x1F3E1; | &#x1F3E1; | &#x1F3E1; | 
| office building | &#x1F3E2; | &#x1F3E2; | &#x1F3E2; | 
| Japanese post office | &#x1F3E3; | &#x1F3E3; | &#x1F3E3; | 
| post office | &#x1F3E4; | &#x1F3E4; | &#x1F3E4; | 
| hospital | &#x1F3E5; | &#x1F3E5; | &#x1F3E5; | 
| bank | &#x1F3E6; | &#x1F3E6; | &#x1F3E6; | 
| hotel | &#x1F3E8; | &#x1F3E8; | &#x1F3E8; | 
| love hotel | &#x1F3E9; | &#x1F3E9; | &#x1F3E9; | 
| convenience store | &#x1F3EA; | &#x1F3EA; | &#x1F3EA; | 
| school | &#x1F3EB; | &#x1F3EB; | &#x1F3EB; | 
| department store | &#x1F3EC; | &#x1F3EC; | &#x1F3EC; | 
| factory | &#x1F3ED; | &#x1F3ED; | &#x1F3ED; | 
| Japanese castle | &#x1F3EF; | &#x1F3EF; | &#x1F3EF; | 
| castle | &#x1F3F0; | &#x1F3F0; | &#x1F3F0; | 
| wedding | &#x1F492; | &#x1F492; | &#x1F492; | 
| Tokyo tower | &#x1F5FC; | &#x1F5FC; | &#x1F5FC; | 
| Statue of Liberty | &#x1F5FD; | &#x1F5FD; | &#x1F5FD; | 

### place-religious

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| church | &#x26EA; | &#x26EA; | &#x26EA; | 
| mosque | &#x1F54C; | &#x1F54C; | &#x1F54C; | 
| hindu temple |  | &#x1F6D5; | &#x1F6D5; | 
| synagogue | &#x1F54D; | &#x1F54D; | &#x1F54D; | 
| shinto shrine | &#x26E9;&#xFE0F; | &#x26E9;&#xFE0F; | &#x26E9;&#xFE0F; | 
| kaaba | &#x1F54B; | &#x1F54B; | &#x1F54B; | 

### place-other

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| fountain | &#x26F2; | &#x26F2; | &#x26F2; | 
| tent | &#x26FA; | &#x26FA; | &#x26FA; | 
| foggy | &#x1F301; | &#x1F301; | &#x1F301; | 
| night with stars | &#x1F303; | &#x1F303; | &#x1F303; | 
| cityscape | &#x1F3D9;&#xFE0F; | &#x1F3D9;&#xFE0F; | &#x1F3D9;&#xFE0F; | 
| sunrise over mountains | &#x1F304; | &#x1F304; | &#x1F304; | 
| sunrise | &#x1F305; | &#x1F305; | &#x1F305; | 
| cityscape at dusk | &#x1F306; | &#x1F306; | &#x1F306; | 
| sunset | &#x1F307; | &#x1F307; | &#x1F307; | 
| bridge at night | &#x1F309; | &#x1F309; | &#x1F309; | 
| hot springs | &#x2668;&#xFE0F; | &#x2668;&#xFE0F; | &#x2668;&#xFE0F; | 
| carousel horse | &#x1F3A0; | &#x1F3A0; | &#x1F3A0; | 
| ferris wheel | &#x1F3A1; | &#x1F3A1; | &#x1F3A1; | 
| roller coaster | &#x1F3A2; | &#x1F3A2; | &#x1F3A2; | 
| barber pole | &#x1F488; | &#x1F488; | &#x1F488; | 
| circus tent | &#x1F3AA; | &#x1F3AA; | &#x1F3AA; | 

### transport-ground

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| locomotive | &#x1F682; | &#x1F682; | &#x1F682; | 
| railway car | &#x1F683; | &#x1F683; | &#x1F683; | 
| high-speed train | &#x1F684; | &#x1F684; | &#x1F684; | 
| bullet train | &#x1F685; | &#x1F685; | &#x1F685; | 
| train | &#x1F686; | &#x1F686; | &#x1F686; | 
| metro | &#x1F687; | &#x1F687; | &#x1F687; | 
| light rail | &#x1F688; | &#x1F688; | &#x1F688; | 
| station | &#x1F689; | &#x1F689; | &#x1F689; | 
| tram | &#x1F68A; | &#x1F68A; | &#x1F68A; | 
| monorail | &#x1F69D; | &#x1F69D; | &#x1F69D; | 
| mountain railway | &#x1F69E; | &#x1F69E; | &#x1F69E; | 
| tram car | &#x1F68B; | &#x1F68B; | &#x1F68B; | 
| bus | &#x1F68C; | &#x1F68C; | &#x1F68C; | 
| oncoming bus | &#x1F68D; | &#x1F68D; | &#x1F68D; | 
| trolleybus | &#x1F68E; | &#x1F68E; | &#x1F68E; | 
| minibus | &#x1F690; | &#x1F690; | &#x1F690; | 
| ambulance | &#x1F691; | &#x1F691; | &#x1F691; | 
| fire engine | &#x1F692; | &#x1F692; | &#x1F692; | 
| police car | &#x1F693; | &#x1F693; | &#x1F693; | 
| oncoming police car | &#x1F694; | &#x1F694; | &#x1F694; | 
| taxi | &#x1F695; | &#x1F695; | &#x1F695; | 
| oncoming taxi | &#x1F696; | &#x1F696; | &#x1F696; | 
| automobile | &#x1F697; | &#x1F697; | &#x1F697; | 
| oncoming automobile | &#x1F698; | &#x1F698; | &#x1F698; | 
| sport utility vehicle | &#x1F699; | &#x1F699; | &#x1F699; | 
| pickup truck |  | &#x1F6FB; | &#x1F6FB; | 
| delivery truck | &#x1F69A; | &#x1F69A; | &#x1F69A; | 
| articulated lorry | &#x1F69B; | &#x1F69B; | &#x1F69B; | 
| tractor | &#x1F69C; | &#x1F69C; | &#x1F69C; | 
| racing car | &#x1F3CE;&#xFE0F; | &#x1F3CE;&#xFE0F; | &#x1F3CE;&#xFE0F; | 
| motorcycle | &#x1F3CD;&#xFE0F; | &#x1F3CD;&#xFE0F; | &#x1F3CD;&#xFE0F; | 
| motor scooter | &#x1F6F5; | &#x1F6F5; | &#x1F6F5; | 
| manual wheelchair |  | &#x1F9BD; | &#x1F9BD; | 
| motorized wheelchair |  | &#x1F9BC; | &#x1F9BC; | 
| auto rickshaw |  | &#x1F6FA; | &#x1F6FA; | 
| bicycle | &#x1F6B2; | &#x1F6B2; | &#x1F6B2; | 
| kick scooter | &#x1F6F4; | &#x1F6F4; | &#x1F6F4; | 
| skateboard |  | &#x1F6F9; | &#x1F6F9; | 
| roller skate |  | &#x1F6FC; | &#x1F6FC; | 
| bus stop | &#x1F68F; | &#x1F68F; | &#x1F68F; | 
| motorway | &#x1F6E3;&#xFE0F; | &#x1F6E3;&#xFE0F; | &#x1F6E3;&#xFE0F; | 
| railway track | &#x1F6E4;&#xFE0F; | &#x1F6E4;&#xFE0F; | &#x1F6E4;&#xFE0F; | 
| oil drum | &#x1F6E2;&#xFE0F; | &#x1F6E2;&#xFE0F; | &#x1F6E2;&#xFE0F; | 
| fuel pump | &#x26FD; | &#x26FD; | &#x26FD; | 
| police car light | &#x1F6A8; | &#x1F6A8; | &#x1F6A8; | 
| horizontal traffic light | &#x1F6A5; | &#x1F6A5; | &#x1F6A5; | 
| vertical traffic light | &#x1F6A6; | &#x1F6A6; | &#x1F6A6; | 
| stop sign | &#x1F6D1; | &#x1F6D1; | &#x1F6D1; | 
| construction | &#x1F6A7; | &#x1F6A7; | &#x1F6A7; | 

### transport-water

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| anchor | &#x2693; | &#x2693; | &#x2693; | 
| sailboat | &#x26F5; | &#x26F5; | &#x26F5; | 
| canoe | &#x1F6F6; | &#x1F6F6; | &#x1F6F6; | 
| speedboat | &#x1F6A4; | &#x1F6A4; | &#x1F6A4; | 
| passenger ship | &#x1F6F3;&#xFE0F; | &#x1F6F3;&#xFE0F; | &#x1F6F3;&#xFE0F; | 
| ferry | &#x26F4;&#xFE0F; | &#x26F4;&#xFE0F; | &#x26F4;&#xFE0F; | 
| motor boat | &#x1F6E5;&#xFE0F; | &#x1F6E5;&#xFE0F; | &#x1F6E5;&#xFE0F; | 
| ship | &#x1F6A2; | &#x1F6A2; | &#x1F6A2; | 

### transport-air

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| airplane | &#x2708;&#xFE0F; | &#x2708;&#xFE0F; | &#x2708;&#xFE0F; | 
| small airplane | &#x1F6E9;&#xFE0F; | &#x1F6E9;&#xFE0F; | &#x1F6E9;&#xFE0F; | 
| airplane departure | &#x1F6EB; | &#x1F6EB; | &#x1F6EB; | 
| airplane arrival | &#x1F6EC; | &#x1F6EC; | &#x1F6EC; | 
| parachute |  | &#x1FA82; | &#x1FA82; | 
| seat | &#x1F4BA; | &#x1F4BA; | &#x1F4BA; | 
| helicopter | &#x1F681; | &#x1F681; | &#x1F681; | 
| suspension railway | &#x1F69F; | &#x1F69F; | &#x1F69F; | 
| mountain cableway | &#x1F6A0; | &#x1F6A0; | &#x1F6A0; | 
| aerial tramway | &#x1F6A1; | &#x1F6A1; | &#x1F6A1; | 
| satellite | &#x1F6F0;&#xFE0F; | &#x1F6F0;&#xFE0F; | &#x1F6F0;&#xFE0F; | 
| rocket | &#x1F680; | &#x1F680; | &#x1F680; | 
| flying saucer |  | &#x1F6F8; | &#x1F6F8; | 

### hotel

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| bellhop bell | &#x1F6CE;&#xFE0F; | &#x1F6CE;&#xFE0F; | &#x1F6CE;&#xFE0F; | 
| luggage |  | &#x1F9F3; | &#x1F9F3; | 

### time

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| hourglass done | &#x231B; | &#x231B; | &#x231B; | 
| hourglass not done | &#x23F3; | &#x23F3; | &#x23F3; | 
| watch | &#x231A; | &#x231A; | &#x231A; | 
| alarm clock | &#x23F0; | &#x23F0; | &#x23F0; | 
| stopwatch | &#x23F1;&#xFE0F; | &#x23F1;&#xFE0F; | &#x23F1;&#xFE0F; | 
| timer clock | &#x23F2;&#xFE0F; | &#x23F2;&#xFE0F; | &#x23F2;&#xFE0F; | 
| mantelpiece clock | &#x1F570;&#xFE0F; | &#x1F570;&#xFE0F; | &#x1F570;&#xFE0F; | 
| twelve o’clock | &#x1F55B; | &#x1F55B; | &#x1F55B; | 
| twelve-thirty | &#x1F567; | &#x1F567; | &#x1F567; | 
| one o’clock | &#x1F550; | &#x1F550; | &#x1F550; | 
| one-thirty | &#x1F55C; | &#x1F55C; | &#x1F55C; | 
| two o’clock | &#x1F551; | &#x1F551; | &#x1F551; | 
| two-thirty | &#x1F55D; | &#x1F55D; | &#x1F55D; | 
| three o’clock | &#x1F552; | &#x1F552; | &#x1F552; | 
| three-thirty | &#x1F55E; | &#x1F55E; | &#x1F55E; | 
| four o’clock | &#x1F553; | &#x1F553; | &#x1F553; | 
| four-thirty | &#x1F55F; | &#x1F55F; | &#x1F55F; | 
| five o’clock | &#x1F554; | &#x1F554; | &#x1F554; | 
| five-thirty | &#x1F560; | &#x1F560; | &#x1F560; | 
| six o’clock | &#x1F555; | &#x1F555; | &#x1F555; | 
| six-thirty | &#x1F561; | &#x1F561; | &#x1F561; | 
| seven o’clock | &#x1F556; | &#x1F556; | &#x1F556; | 
| seven-thirty | &#x1F562; | &#x1F562; | &#x1F562; | 
| eight o’clock | &#x1F557; | &#x1F557; | &#x1F557; | 
| eight-thirty | &#x1F563; | &#x1F563; | &#x1F563; | 
| nine o’clock | &#x1F558; | &#x1F558; | &#x1F558; | 
| nine-thirty | &#x1F564; | &#x1F564; | &#x1F564; | 
| ten o’clock | &#x1F559; | &#x1F559; | &#x1F559; | 
| ten-thirty | &#x1F565; | &#x1F565; | &#x1F565; | 
| eleven o’clock | &#x1F55A; | &#x1F55A; | &#x1F55A; | 
| eleven-thirty | &#x1F566; | &#x1F566; | &#x1F566; | 

### sky & weather

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| new moon | &#x1F311; | &#x1F311; | &#x1F311; | 
| waxing crescent moon | &#x1F312; | &#x1F312; | &#x1F312; | 
| first quarter moon | &#x1F313; | &#x1F313; | &#x1F313; | 
| waxing gibbous moon | &#x1F314; | &#x1F314; | &#x1F314; | 
| full moon | &#x1F315; | &#x1F315; | &#x1F315; | 
| waning gibbous moon | &#x1F316; | &#x1F316; | &#x1F316; | 
| last quarter moon | &#x1F317; | &#x1F317; | &#x1F317; | 
| waning crescent moon | &#x1F318; | &#x1F318; | &#x1F318; | 
| crescent moon | &#x1F319; | &#x1F319; | &#x1F319; | 
| new moon face | &#x1F31A; | &#x1F31A; | &#x1F31A; | 
| first quarter moon face | &#x1F31B; | &#x1F31B; | &#x1F31B; | 
| last quarter moon face | &#x1F31C; | &#x1F31C; | &#x1F31C; | 
| thermometer | &#x1F321;&#xFE0F; | &#x1F321;&#xFE0F; | &#x1F321;&#xFE0F; | 
| sun | &#x2600;&#xFE0F; | &#x2600;&#xFE0F; | &#x2600;&#xFE0F; | 
| full moon face | &#x1F31D; | &#x1F31D; | &#x1F31D; | 
| sun with face | &#x1F31E; | &#x1F31E; | &#x1F31E; | 
| ringed planet |  | &#x1FA90; | &#x1FA90; | 
| star | &#x2B50; | &#x2B50; | &#x2B50; | 
| glowing star | &#x1F31F; | &#x1F31F; | &#x1F31F; | 
| shooting star | &#x1F320; | &#x1F320; | &#x1F320; | 
| milky way | &#x1F30C; | &#x1F30C; | &#x1F30C; | 
| cloud | &#x2601;&#xFE0F; | &#x2601;&#xFE0F; | &#x2601;&#xFE0F; | 
| sun behind cloud | &#x26C5; | &#x26C5; | &#x26C5; | 
| cloud with lightning and rain | &#x26C8;&#xFE0F; | &#x26C8;&#xFE0F; | &#x26C8;&#xFE0F; | 
| sun behind small cloud | &#x1F324;&#xFE0F; | &#x1F324;&#xFE0F; | &#x1F324;&#xFE0F; | 
| sun behind large cloud | &#x1F325;&#xFE0F; | &#x1F325;&#xFE0F; | &#x1F325;&#xFE0F; | 
| sun behind rain cloud | &#x1F326;&#xFE0F; | &#x1F326;&#xFE0F; | &#x1F326;&#xFE0F; | 
| cloud with rain | &#x1F327;&#xFE0F; | &#x1F327;&#xFE0F; | &#x1F327;&#xFE0F; | 
| cloud with snow | &#x1F328;&#xFE0F; | &#x1F328;&#xFE0F; | &#x1F328;&#xFE0F; | 
| cloud with lightning | &#x1F329;&#xFE0F; | &#x1F329;&#xFE0F; | &#x1F329;&#xFE0F; | 
| tornado | &#x1F32A;&#xFE0F; | &#x1F32A;&#xFE0F; | &#x1F32A;&#xFE0F; | 
| fog | &#x1F32B;&#xFE0F; | &#x1F32B;&#xFE0F; | &#x1F32B;&#xFE0F; | 
| wind face | &#x1F32C;&#xFE0F; | &#x1F32C;&#xFE0F; | &#x1F32C;&#xFE0F; | 
| cyclone | &#x1F300; | &#x1F300; | &#x1F300; | 
| rainbow | &#x1F308; | &#x1F308; | &#x1F308; | 
| closed umbrella | &#x1F302; | &#x1F302; | &#x1F302; | 
| umbrella | &#x2602;&#xFE0F; | &#x2602;&#xFE0F; | &#x2602;&#xFE0F; | 
| umbrella with rain drops | &#x2614; | &#x2614; | &#x2614; | 
| umbrella on ground | &#x26F1;&#xFE0F; | &#x26F1;&#xFE0F; | &#x26F1;&#xFE0F; | 
| high voltage | &#x26A1; | &#x26A1; | &#x26A1; | 
| snowflake | &#x2744;&#xFE0F; | &#x2744;&#xFE0F; | &#x2744;&#xFE0F; | 
| snowman | &#x2603;&#xFE0F; | &#x2603;&#xFE0F; | &#x2603;&#xFE0F; | 
| snowman without snow | &#x26C4; | &#x26C4; | &#x26C4; | 
| comet | &#x2604;&#xFE0F; | &#x2604;&#xFE0F; | &#x2604;&#xFE0F; | 
| fire | &#x1F525; | &#x1F525; | &#x1F525; | 
| droplet | &#x1F4A7; | &#x1F4A7; | &#x1F4A7; | 
| water wave | &#x1F30A; | &#x1F30A; | &#x1F30A; | 

## Activities


### event

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| jack-o-lantern | &#x1F383; | &#x1F383; | &#x1F383; | 
| Christmas tree | &#x1F384; | &#x1F384; | &#x1F384; | 
| fireworks | &#x1F386; | &#x1F386; | &#x1F386; | 
| sparkler | &#x1F387; | &#x1F387; | &#x1F387; | 
| firecracker |  | &#x1F9E8; | &#x1F9E8; | 
| sparkles | &#x2728; | &#x2728; | &#x2728; | 
| balloon | &#x1F388; | &#x1F388; | &#x1F388; | 
| party popper | &#x1F389; | &#x1F389; | &#x1F389; | 
| confetti ball | &#x1F38A; | &#x1F38A; | &#x1F38A; | 
| tanabata tree | &#x1F38B; | &#x1F38B; | &#x1F38B; | 
| pine decoration | &#x1F38D; | &#x1F38D; | &#x1F38D; | 
| Japanese dolls | &#x1F38E; | &#x1F38E; | &#x1F38E; | 
| carp streamer | &#x1F38F; | &#x1F38F; | &#x1F38F; | 
| wind chime | &#x1F390; | &#x1F390; | &#x1F390; | 
| moon viewing ceremony | &#x1F391; | &#x1F391; | &#x1F391; | 
| red envelope |  | &#x1F9E7; | &#x1F9E7; | 
| ribbon | &#x1F380; | &#x1F380; | &#x1F380; | 
| wrapped gift | &#x1F381; | &#x1F381; | &#x1F381; | 
| reminder ribbon | &#x1F397;&#xFE0F; | &#x1F397;&#xFE0F; | &#x1F397;&#xFE0F; | 
| admission tickets | &#x1F39F;&#xFE0F; | &#x1F39F;&#xFE0F; | &#x1F39F;&#xFE0F; | 
| ticket | &#x1F3AB; | &#x1F3AB; | &#x1F3AB; | 

### award-medal

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| military medal | &#x1F396;&#xFE0F; | &#x1F396;&#xFE0F; | &#x1F396;&#xFE0F; | 
| trophy | &#x1F3C6; | &#x1F3C6; | &#x1F3C6; | 
| sports medal | &#x1F3C5; | &#x1F3C5; | &#x1F3C5; | 
| st place medal | &#x1F947; | &#x1F947; | &#x1F947; | 
| nd place medal | &#x1F948; | &#x1F948; | &#x1F948; | 
| rd place medal | &#x1F949; | &#x1F949; | &#x1F949; | 

### sport

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| soccer ball | &#x26BD; | &#x26BD; | &#x26BD; | 
| baseball | &#x26BE; | &#x26BE; | &#x26BE; | 
| softball |  | &#x1F94E; | &#x1F94E; | 
| basketball | &#x1F3C0; | &#x1F3C0; | &#x1F3C0; | 
| volleyball | &#x1F3D0; | &#x1F3D0; | &#x1F3D0; | 
| american football | &#x1F3C8; | &#x1F3C8; | &#x1F3C8; | 
| rugby football | &#x1F3C9; | &#x1F3C9; | &#x1F3C9; | 
| tennis | &#x1F3BE; | &#x1F3BE; | &#x1F3BE; | 
| flying disc |  | &#x1F94F; | &#x1F94F; | 
| bowling | &#x1F3B3; | &#x1F3B3; | &#x1F3B3; | 
| cricket game | &#x1F3CF; | &#x1F3CF; | &#x1F3CF; | 
| field hockey | &#x1F3D1; | &#x1F3D1; | &#x1F3D1; | 
| ice hockey | &#x1F3D2; | &#x1F3D2; | &#x1F3D2; | 
| lacrosse |  | &#x1F94D; | &#x1F94D; | 
| ping pong | &#x1F3D3; | &#x1F3D3; | &#x1F3D3; | 
| badminton | &#x1F3F8; | &#x1F3F8; | &#x1F3F8; | 
| boxing glove | &#x1F94A; | &#x1F94A; | &#x1F94A; | 
| martial arts uniform | &#x1F94B; | &#x1F94B; | &#x1F94B; | 
| goal net | &#x1F945; | &#x1F945; | &#x1F945; | 
| flag in hole | &#x26F3; | &#x26F3; | &#x26F3; | 
| ice skate | &#x26F8;&#xFE0F; | &#x26F8;&#xFE0F; | &#x26F8;&#xFE0F; | 
| fishing pole | &#x1F3A3; | &#x1F3A3; | &#x1F3A3; | 
| diving mask |  | &#x1F93F; | &#x1F93F; | 
| running shirt | &#x1F3BD; | &#x1F3BD; | &#x1F3BD; | 
| skis | &#x1F3BF; | &#x1F3BF; | &#x1F3BF; | 
| sled |  | &#x1F6F7; | &#x1F6F7; | 
| curling stone |  | &#x1F94C; | &#x1F94C; | 

### game

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| direct hit | &#x1F3AF; | &#x1F3AF; | &#x1F3AF; | 
| yo-yo |  | &#x1FA80; | &#x1FA80; | 
| kite |  | &#x1FA81; | &#x1FA81; | 
| pool 8 ball | &#x1F3B1; | &#x1F3B1; | &#x1F3B1; | 
| crystal ball | &#x1F52E; | &#x1F52E; | &#x1F52E; | 
| magic wand |  | &#x1FA84; | &#x1FA84; | 
| nazar amulet |  | &#x1F9FF; | &#x1F9FF; | 
| video game | &#x1F3AE; | &#x1F3AE; | &#x1F3AE; | 
| joystick | &#x1F579;&#xFE0F; | &#x1F579;&#xFE0F; | &#x1F579;&#xFE0F; | 
| slot machine | &#x1F3B0; | &#x1F3B0; | &#x1F3B0; | 
| game die | &#x1F3B2; | &#x1F3B2; | &#x1F3B2; | 
| puzzle piece |  | &#x1F9E9; | &#x1F9E9; | 
| teddy bear |  | &#x1F9F8; | &#x1F9F8; | 
| piñata |  | &#x1FA85; | &#x1FA85; | 
| nesting dolls |  | &#x1FA86; | &#x1FA86; | 
| spade suit | &#x2660;&#xFE0F; | &#x2660;&#xFE0F; | &#x2660;&#xFE0F; | 
| heart suit | &#x2665;&#xFE0F; | &#x2665;&#xFE0F; | &#x2665;&#xFE0F; | 
| diamond suit | &#x2666;&#xFE0F; | &#x2666;&#xFE0F; | &#x2666;&#xFE0F; | 
| club suit | &#x2663;&#xFE0F; | &#x2663;&#xFE0F; | &#x2663;&#xFE0F; | 
| chess pawn |  | &#x265F;&#xFE0F; | &#x265F;&#xFE0F; | 
| joker | &#x1F0CF; | &#x1F0CF; | &#x1F0CF; | 
| mahjong red dragon | &#x1F004; | &#x1F004; | &#x1F004; | 
| flower playing cards | &#x1F3B4; | &#x1F3B4; | &#x1F3B4; | 

### arts & crafts

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| performing arts | &#x1F3AD; | &#x1F3AD; | &#x1F3AD; | 
| framed picture | &#x1F5BC;&#xFE0F; | &#x1F5BC;&#xFE0F; | &#x1F5BC;&#xFE0F; | 
| artist palette | &#x1F3A8; | &#x1F3A8; | &#x1F3A8; | 
| thread |  | &#x1F9F5; | &#x1F9F5; | 
| sewing needle |  | &#x1FAA1; | &#x1FAA1; | 
| yarn |  | &#x1F9F6; | &#x1F9F6; | 
| knot |  | &#x1FAA2; | &#x1FAA2; | 

## Objects


### clothing

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| glasses | &#x1F453; | &#x1F453; | &#x1F453; | 
| sunglasses | &#x1F576;&#xFE0F; | &#x1F576;&#xFE0F; | &#x1F576;&#xFE0F; | 
| goggles |  | &#x1F97D; | &#x1F97D; | 
| lab coat |  | &#x1F97C; | &#x1F97C; | 
| safety vest |  | &#x1F9BA; | &#x1F9BA; | 
| necktie | &#x1F454; | &#x1F454; | &#x1F454; | 
| t-shirt | &#x1F455; | &#x1F455; | &#x1F455; | 
| jeans | &#x1F456; | &#x1F456; | &#x1F456; | 
| scarf |  | &#x1F9E3; | &#x1F9E3; | 
| gloves |  | &#x1F9E4; | &#x1F9E4; | 
| coat |  | &#x1F9E5; | &#x1F9E5; | 
| socks |  | &#x1F9E6; | &#x1F9E6; | 
| dress | &#x1F457; | &#x1F457; | &#x1F457; | 
| kimono | &#x1F458; | &#x1F458; | &#x1F458; | 
| sari |  | &#x1F97B; | &#x1F97B; | 
| one-piece swimsuit |  | &#x1FA71; | &#x1FA71; | 
| briefs |  | &#x1FA72; | &#x1FA72; | 
| shorts |  | &#x1FA73; | &#x1FA73; | 
| bikini | &#x1F459; | &#x1F459; | &#x1F459; | 
| woman’s clothes | &#x1F45A; | &#x1F45A; | &#x1F45A; | 
| purse | &#x1F45B; | &#x1F45B; | &#x1F45B; | 
| handbag | &#x1F45C; | &#x1F45C; | &#x1F45C; | 
| clutch bag | &#x1F45D; | &#x1F45D; | &#x1F45D; | 
| shopping bags | &#x1F6CD;&#xFE0F; | &#x1F6CD;&#xFE0F; | &#x1F6CD;&#xFE0F; | 
| backpack | &#x1F392; | &#x1F392; | &#x1F392; | 
| thong sandal |  | &#x1FA74; | &#x1FA74; | 
| man’s shoe | &#x1F45E; | &#x1F45E; | &#x1F45E; | 
| running shoe | &#x1F45F; | &#x1F45F; | &#x1F45F; | 
| hiking boot |  | &#x1F97E; | &#x1F97E; | 
| flat shoe |  | &#x1F97F; | &#x1F97F; | 
| high-heeled shoe | &#x1F460; | &#x1F460; | &#x1F460; | 
| woman’s sandal | &#x1F461; | &#x1F461; | &#x1F461; | 
| ballet shoes |  | &#x1FA70; | &#x1FA70; | 
| woman’s boot | &#x1F462; | &#x1F462; | &#x1F462; | 
| crown | &#x1F451; | &#x1F451; | &#x1F451; | 
| woman’s hat | &#x1F452; | &#x1F452; | &#x1F452; | 
| top hat | &#x1F3A9; | &#x1F3A9; | &#x1F3A9; | 
| graduation cap | &#x1F393; | &#x1F393; | &#x1F393; | 
| billed cap |  | &#x1F9E2; | &#x1F9E2; | 
| military helmet |  | &#x1FA96; | &#x1FA96; | 
| rescue worker’s helmet | &#x26D1;&#xFE0F; | &#x26D1;&#xFE0F; | &#x26D1;&#xFE0F; | 
| prayer beads | &#x1F4FF; | &#x1F4FF; | &#x1F4FF; | 
| lipstick | &#x1F484; | &#x1F484; | &#x1F484; | 
| ring | &#x1F48D; | &#x1F48D; | &#x1F48D; | 
| gem stone | &#x1F48E; | &#x1F48E; | &#x1F48E; | 

### sound

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| muted speaker | &#x1F507; | &#x1F507; | &#x1F507; | 
| speaker low volume | &#x1F508; | &#x1F508; | &#x1F508; | 
| speaker medium volume | &#x1F509; | &#x1F509; | &#x1F509; | 
| speaker high volume | &#x1F50A; | &#x1F50A; | &#x1F50A; | 
| loudspeaker | &#x1F4E2; | &#x1F4E2; | &#x1F4E2; | 
| megaphone | &#x1F4E3; | &#x1F4E3; | &#x1F4E3; | 
| postal horn | &#x1F4EF; | &#x1F4EF; | &#x1F4EF; | 
| bell | &#x1F514; | &#x1F514; | &#x1F514; | 
| bell with slash | &#x1F515; | &#x1F515; | &#x1F515; | 

### music

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| musical score | &#x1F3BC; | &#x1F3BC; | &#x1F3BC; | 
| musical note | &#x1F3B5; | &#x1F3B5; | &#x1F3B5; | 
| musical notes | &#x1F3B6; | &#x1F3B6; | &#x1F3B6; | 
| studio microphone | &#x1F399;&#xFE0F; | &#x1F399;&#xFE0F; | &#x1F399;&#xFE0F; | 
| level slider | &#x1F39A;&#xFE0F; | &#x1F39A;&#xFE0F; | &#x1F39A;&#xFE0F; | 
| control knobs | &#x1F39B;&#xFE0F; | &#x1F39B;&#xFE0F; | &#x1F39B;&#xFE0F; | 
| microphone | &#x1F3A4; | &#x1F3A4; | &#x1F3A4; | 
| headphone | &#x1F3A7; | &#x1F3A7; | &#x1F3A7; | 
| radio | &#x1F4FB; | &#x1F4FB; | &#x1F4FB; | 

### musical-instrument

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| saxophone | &#x1F3B7; | &#x1F3B7; | &#x1F3B7; | 
| accordion |  | &#x1FA97; | &#x1FA97; | 
| guitar | &#x1F3B8; | &#x1F3B8; | &#x1F3B8; | 
| musical keyboard | &#x1F3B9; | &#x1F3B9; | &#x1F3B9; | 
| trumpet | &#x1F3BA; | &#x1F3BA; | &#x1F3BA; | 
| violin | &#x1F3BB; | &#x1F3BB; | &#x1F3BB; | 
| banjo |  | &#x1FA95; | &#x1FA95; | 
| drum | &#x1F941; | &#x1F941; | &#x1F941; | 
| long drum |  | &#x1FA98; | &#x1FA98; | 

### phone

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| mobile phone | &#x1F4F1; | &#x1F4F1; | &#x1F4F1; | 
| mobile phone with arrow | &#x1F4F2; | &#x1F4F2; | &#x1F4F2; | 
| telephone | &#x260E;&#xFE0F; | &#x260E;&#xFE0F; | &#x260E;&#xFE0F; | 
| telephone receiver | &#x1F4DE; | &#x1F4DE; | &#x1F4DE; | 
| pager | &#x1F4DF; | &#x1F4DF; | &#x1F4DF; | 
| fax machine | &#x1F4E0; | &#x1F4E0; | &#x1F4E0; | 

### computer

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| battery | &#x1F50B; | &#x1F50B; | &#x1F50B; | 
| electric plug | &#x1F50C; | &#x1F50C; | &#x1F50C; | 
| laptop | &#x1F4BB; | &#x1F4BB; | &#x1F4BB; | 
| desktop computer | &#x1F5A5;&#xFE0F; | &#x1F5A5;&#xFE0F; | &#x1F5A5;&#xFE0F; | 
| printer | &#x1F5A8;&#xFE0F; | &#x1F5A8;&#xFE0F; | &#x1F5A8;&#xFE0F; | 
| keyboard | &#x2328;&#xFE0F; | &#x2328;&#xFE0F; | &#x2328;&#xFE0F; | 
| computer mouse | &#x1F5B1;&#xFE0F; | &#x1F5B1;&#xFE0F; | &#x1F5B1;&#xFE0F; | 
| trackball | &#x1F5B2;&#xFE0F; | &#x1F5B2;&#xFE0F; | &#x1F5B2;&#xFE0F; | 
| computer disk | &#x1F4BD; | &#x1F4BD; | &#x1F4BD; | 
| floppy disk | &#x1F4BE; | &#x1F4BE; | &#x1F4BE; | 
| optical disk | &#x1F4BF; | &#x1F4BF; | &#x1F4BF; | 
| dvd | &#x1F4C0; | &#x1F4C0; | &#x1F4C0; | 
| abacus |  | &#x1F9EE; | &#x1F9EE; | 

### light & video

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| movie camera | &#x1F3A5; | &#x1F3A5; | &#x1F3A5; | 
| film frames | &#x1F39E;&#xFE0F; | &#x1F39E;&#xFE0F; | &#x1F39E;&#xFE0F; | 
| film projector | &#x1F4FD;&#xFE0F; | &#x1F4FD;&#xFE0F; | &#x1F4FD;&#xFE0F; | 
| clapper board | &#x1F3AC; | &#x1F3AC; | &#x1F3AC; | 
| television | &#x1F4FA; | &#x1F4FA; | &#x1F4FA; | 
| camera | &#x1F4F7; | &#x1F4F7; | &#x1F4F7; | 
| camera with flash | &#x1F4F8; | &#x1F4F8; | &#x1F4F8; | 
| video camera | &#x1F4F9; | &#x1F4F9; | &#x1F4F9; | 
| videocassette | &#x1F4FC; | &#x1F4FC; | &#x1F4FC; | 
| magnifying glass tilted left | &#x1F50D; | &#x1F50D; | &#x1F50D; | 
| magnifying glass tilted right | &#x1F50E; | &#x1F50E; | &#x1F50E; | 
| candle | &#x1F56F;&#xFE0F; | &#x1F56F;&#xFE0F; | &#x1F56F;&#xFE0F; | 
| light bulb | &#x1F4A1; | &#x1F4A1; | &#x1F4A1; | 
| flashlight | &#x1F526; | &#x1F526; | &#x1F526; | 
| red paper lantern | &#x1F3EE; | &#x1F3EE; | &#x1F3EE; | 
| diya lamp |  | &#x1FA94; | &#x1FA94; | 

### book-paper

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| notebook with decorative cover | &#x1F4D4; | &#x1F4D4; | &#x1F4D4; | 
| closed book | &#x1F4D5; | &#x1F4D5; | &#x1F4D5; | 
| open book | &#x1F4D6; | &#x1F4D6; | &#x1F4D6; | 
| green book | &#x1F4D7; | &#x1F4D7; | &#x1F4D7; | 
| blue book | &#x1F4D8; | &#x1F4D8; | &#x1F4D8; | 
| orange book | &#x1F4D9; | &#x1F4D9; | &#x1F4D9; | 
| books | &#x1F4DA; | &#x1F4DA; | &#x1F4DA; | 
| notebook | &#x1F4D3; | &#x1F4D3; | &#x1F4D3; | 
| ledger | &#x1F4D2; | &#x1F4D2; | &#x1F4D2; | 
| page with curl | &#x1F4C3; | &#x1F4C3; | &#x1F4C3; | 
| scroll | &#x1F4DC; | &#x1F4DC; | &#x1F4DC; | 
| page facing up | &#x1F4C4; | &#x1F4C4; | &#x1F4C4; | 
| newspaper | &#x1F4F0; | &#x1F4F0; | &#x1F4F0; | 
| rolled-up newspaper | &#x1F5DE;&#xFE0F; | &#x1F5DE;&#xFE0F; | &#x1F5DE;&#xFE0F; | 
| bookmark tabs | &#x1F4D1; | &#x1F4D1; | &#x1F4D1; | 
| bookmark | &#x1F516; | &#x1F516; | &#x1F516; | 
| label | &#x1F3F7;&#xFE0F; | &#x1F3F7;&#xFE0F; | &#x1F3F7;&#xFE0F; | 

### money

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| money bag | &#x1F4B0; | &#x1F4B0; | &#x1F4B0; | 
| coin |  | &#x1FA99; | &#x1FA99; | 
| yen banknote | &#x1F4B4; | &#x1F4B4; | &#x1F4B4; | 
| dollar banknote | &#x1F4B5; | &#x1F4B5; | &#x1F4B5; | 
| euro banknote | &#x1F4B6; | &#x1F4B6; | &#x1F4B6; | 
| pound banknote | &#x1F4B7; | &#x1F4B7; | &#x1F4B7; | 
| money with wings | &#x1F4B8; | &#x1F4B8; | &#x1F4B8; | 
| credit card | &#x1F4B3; | &#x1F4B3; | &#x1F4B3; | 
| receipt |  | &#x1F9FE; | &#x1F9FE; | 
| chart increasing with yen | &#x1F4B9; | &#x1F4B9; | &#x1F4B9; | 

### mail

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| envelope | &#x2709;&#xFE0F; | &#x2709;&#xFE0F; | &#x2709;&#xFE0F; | 
| e-mail | &#x1F4E7; | &#x1F4E7; | &#x1F4E7; | 
| incoming envelope | &#x1F4E8; | &#x1F4E8; | &#x1F4E8; | 
| envelope with arrow | &#x1F4E9; | &#x1F4E9; | &#x1F4E9; | 
| outbox tray | &#x1F4E4; | &#x1F4E4; | &#x1F4E4; | 
| inbox tray | &#x1F4E5; | &#x1F4E5; | &#x1F4E5; | 
| package | &#x1F4E6; | &#x1F4E6; | &#x1F4E6; | 
| closed mailbox with raised flag | &#x1F4EB; | &#x1F4EB; | &#x1F4EB; | 
| closed mailbox with lowered flag | &#x1F4EA; | &#x1F4EA; | &#x1F4EA; | 
| open mailbox with raised flag | &#x1F4EC; | &#x1F4EC; | &#x1F4EC; | 
| open mailbox with lowered flag | &#x1F4ED; | &#x1F4ED; | &#x1F4ED; | 
| postbox | &#x1F4EE; | &#x1F4EE; | &#x1F4EE; | 
| ballot box with ballot | &#x1F5F3;&#xFE0F; | &#x1F5F3;&#xFE0F; | &#x1F5F3;&#xFE0F; | 

### writing

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| pencil | &#x270F;&#xFE0F; | &#x270F;&#xFE0F; | &#x270F;&#xFE0F; | 
| black nib | &#x2712;&#xFE0F; | &#x2712;&#xFE0F; | &#x2712;&#xFE0F; | 
| fountain pen | &#x1F58B;&#xFE0F; | &#x1F58B;&#xFE0F; | &#x1F58B;&#xFE0F; | 
| pen | &#x1F58A;&#xFE0F; | &#x1F58A;&#xFE0F; | &#x1F58A;&#xFE0F; | 
| paintbrush | &#x1F58C;&#xFE0F; | &#x1F58C;&#xFE0F; | &#x1F58C;&#xFE0F; | 
| crayon | &#x1F58D;&#xFE0F; | &#x1F58D;&#xFE0F; | &#x1F58D;&#xFE0F; | 
| memo | &#x1F4DD; | &#x1F4DD; | &#x1F4DD; | 

### office

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| briefcase | &#x1F4BC; | &#x1F4BC; | &#x1F4BC; | 
| file folder | &#x1F4C1; | &#x1F4C1; | &#x1F4C1; | 
| open file folder | &#x1F4C2; | &#x1F4C2; | &#x1F4C2; | 
| card index dividers | &#x1F5C2;&#xFE0F; | &#x1F5C2;&#xFE0F; | &#x1F5C2;&#xFE0F; | 
| calendar | &#x1F4C5; | &#x1F4C5; | &#x1F4C5; | 
| tear-off calendar | &#x1F4C6; | &#x1F4C6; | &#x1F4C6; | 
| spiral notepad | &#x1F5D2;&#xFE0F; | &#x1F5D2;&#xFE0F; | &#x1F5D2;&#xFE0F; | 
| spiral calendar | &#x1F5D3;&#xFE0F; | &#x1F5D3;&#xFE0F; | &#x1F5D3;&#xFE0F; | 
| card index | &#x1F4C7; | &#x1F4C7; | &#x1F4C7; | 
| chart increasing | &#x1F4C8; | &#x1F4C8; | &#x1F4C8; | 
| chart decreasing | &#x1F4C9; | &#x1F4C9; | &#x1F4C9; | 
| bar chart | &#x1F4CA; | &#x1F4CA; | &#x1F4CA; | 
| clipboard | &#x1F4CB; | &#x1F4CB; | &#x1F4CB; | 
| pushpin | &#x1F4CC; | &#x1F4CC; | &#x1F4CC; | 
| round pushpin | &#x1F4CD; | &#x1F4CD; | &#x1F4CD; | 
| paperclip | &#x1F4CE; | &#x1F4CE; | &#x1F4CE; | 
| linked paperclips | &#x1F587;&#xFE0F; | &#x1F587;&#xFE0F; | &#x1F587;&#xFE0F; | 
| straight ruler | &#x1F4CF; | &#x1F4CF; | &#x1F4CF; | 
| triangular ruler | &#x1F4D0; | &#x1F4D0; | &#x1F4D0; | 
| scissors | &#x2702;&#xFE0F; | &#x2702;&#xFE0F; | &#x2702;&#xFE0F; | 
| card file box | &#x1F5C3;&#xFE0F; | &#x1F5C3;&#xFE0F; | &#x1F5C3;&#xFE0F; | 
| file cabinet | &#x1F5C4;&#xFE0F; | &#x1F5C4;&#xFE0F; | &#x1F5C4;&#xFE0F; | 
| wastebasket | &#x1F5D1;&#xFE0F; | &#x1F5D1;&#xFE0F; | &#x1F5D1;&#xFE0F; | 

### lock

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| locked | &#x1F512; | &#x1F512; | &#x1F512; | 
| unlocked | &#x1F513; | &#x1F513; | &#x1F513; | 
| locked with pen | &#x1F50F; | &#x1F50F; | &#x1F50F; | 
| locked with key | &#x1F510; | &#x1F510; | &#x1F510; | 
| key | &#x1F511; | &#x1F511; | &#x1F511; | 
| old key | &#x1F5DD;&#xFE0F; | &#x1F5DD;&#xFE0F; | &#x1F5DD;&#xFE0F; | 

### tool

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| hammer | &#x1F528; | &#x1F528; | &#x1F528; | 
| axe |  | &#x1FA93; | &#x1FA93; | 
| pick | &#x26CF;&#xFE0F; | &#x26CF;&#xFE0F; | &#x26CF;&#xFE0F; | 
| hammer and pick | &#x2692;&#xFE0F; | &#x2692;&#xFE0F; | &#x2692;&#xFE0F; | 
| hammer and wrench | &#x1F6E0;&#xFE0F; | &#x1F6E0;&#xFE0F; | &#x1F6E0;&#xFE0F; | 
| dagger | &#x1F5E1;&#xFE0F; | &#x1F5E1;&#xFE0F; | &#x1F5E1;&#xFE0F; | 
| crossed swords | &#x2694;&#xFE0F; | &#x2694;&#xFE0F; | &#x2694;&#xFE0F; | 
| pistol | &#x1F52B; | &#x1F52B; | &#x1F52B; | 
| boomerang |  | &#x1FA83; | &#x1FA83; | 
| bow and arrow | &#x1F3F9; | &#x1F3F9; | &#x1F3F9; | 
| shield | &#x1F6E1;&#xFE0F; | &#x1F6E1;&#xFE0F; | &#x1F6E1;&#xFE0F; | 
| carpentry saw |  | &#x1FA9A; | &#x1FA9A; | 
| wrench | &#x1F527; | &#x1F527; | &#x1F527; | 
| screwdriver |  | &#x1FA9B; | &#x1FA9B; | 
| nut and bolt | &#x1F529; | &#x1F529; | &#x1F529; | 
| gear | &#x2699;&#xFE0F; | &#x2699;&#xFE0F; | &#x2699;&#xFE0F; | 
| clamp | &#x1F5DC;&#xFE0F; | &#x1F5DC;&#xFE0F; | &#x1F5DC;&#xFE0F; | 
| balance scale | &#x2696;&#xFE0F; | &#x2696;&#xFE0F; | &#x2696;&#xFE0F; | 
| white cane |  | &#x1F9AF; | &#x1F9AF; | 
| link | &#x1F517; | &#x1F517; | &#x1F517; | 
| chains | &#x26D3;&#xFE0F; | &#x26D3;&#xFE0F; | &#x26D3;&#xFE0F; | 
| hook |  | &#x1FA9D; | &#x1FA9D; | 
| toolbox |  | &#x1F9F0; | &#x1F9F0; | 
| magnet |  | &#x1F9F2; | &#x1F9F2; | 
| ladder |  | &#x1FA9C; | &#x1FA9C; | 

### science

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| alembic | &#x2697;&#xFE0F; | &#x2697;&#xFE0F; | &#x2697;&#xFE0F; | 
| test tube |  | &#x1F9EA; | &#x1F9EA; | 
| petri dish |  | &#x1F9EB; | &#x1F9EB; | 
| dna |  | &#x1F9EC; | &#x1F9EC; | 
| microscope | &#x1F52C; | &#x1F52C; | &#x1F52C; | 
| telescope | &#x1F52D; | &#x1F52D; | &#x1F52D; | 
| satellite antenna | &#x1F4E1; | &#x1F4E1; | &#x1F4E1; | 

### medical

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| syringe | &#x1F489; | &#x1F489; | &#x1F489; | 
| drop of blood |  | &#x1FA78; | &#x1FA78; | 
| pill | &#x1F48A; | &#x1F48A; | &#x1F48A; | 
| adhesive bandage |  | &#x1FA79; | &#x1FA79; | 
| stethoscope |  | &#x1FA7A; | &#x1FA7A; | 

### household

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| door | &#x1F6AA; | &#x1F6AA; | &#x1F6AA; | 
| elevator |  | &#x1F6D7; | &#x1F6D7; | 
| mirror |  | &#x1FA9E; | &#x1FA9E; | 
| window |  | &#x1FA9F; | &#x1FA9F; | 
| bed | &#x1F6CF;&#xFE0F; | &#x1F6CF;&#xFE0F; | &#x1F6CF;&#xFE0F; | 
| couch and lamp | &#x1F6CB;&#xFE0F; | &#x1F6CB;&#xFE0F; | &#x1F6CB;&#xFE0F; | 
| chair |  | &#x1FA91; | &#x1FA91; | 
| toilet | &#x1F6BD; | &#x1F6BD; | &#x1F6BD; | 
| plunger |  | &#x1FAA0; | &#x1FAA0; | 
| shower | &#x1F6BF; | &#x1F6BF; | &#x1F6BF; | 
| bathtub | &#x1F6C1; | &#x1F6C1; | &#x1F6C1; | 
| mouse trap |  | &#x1FAA4; | &#x1FAA4; | 
| razor |  | &#x1FA92; | &#x1FA92; | 
| lotion bottle |  | &#x1F9F4; | &#x1F9F4; | 
| safety pin |  | &#x1F9F7; | &#x1F9F7; | 
| broom |  | &#x1F9F9; | &#x1F9F9; | 
| basket |  | &#x1F9FA; | &#x1F9FA; | 
| roll of paper |  | &#x1F9FB; | &#x1F9FB; | 
| bucket |  | &#x1FAA3; | &#x1FAA3; | 
| soap |  | &#x1F9FC; | &#x1F9FC; | 
| toothbrush |  | &#x1FAA5; | &#x1FAA5; | 
| sponge |  | &#x1F9FD; | &#x1F9FD; | 
| fire extinguisher |  | &#x1F9EF; | &#x1F9EF; | 
| shopping cart | &#x1F6D2; | &#x1F6D2; | &#x1F6D2; | 

### other-object

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| cigarette | &#x1F6AC; | &#x1F6AC; | &#x1F6AC; | 
| coffin | &#x26B0;&#xFE0F; | &#x26B0;&#xFE0F; | &#x26B0;&#xFE0F; | 
| headstone |  | &#x1FAA6; | &#x1FAA6; | 
| funeral urn | &#x26B1;&#xFE0F; | &#x26B1;&#xFE0F; | &#x26B1;&#xFE0F; | 
| moai | &#x1F5FF; | &#x1F5FF; | &#x1F5FF; | 
| placard |  | &#x1FAA7; | &#x1FAA7; | 

## Symbols


### transport-sign

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| ATM sign | &#x1F3E7; | &#x1F3E7; | &#x1F3E7; | 
| litter in bin sign | &#x1F6AE; | &#x1F6AE; | &#x1F6AE; | 
| potable water | &#x1F6B0; | &#x1F6B0; | &#x1F6B0; | 
| wheelchair symbol | &#x267F; | &#x267F; | &#x267F; | 
| men’s room | &#x1F6B9; | &#x1F6B9; | &#x1F6B9; | 
| women’s room | &#x1F6BA; | &#x1F6BA; | &#x1F6BA; | 
| restroom | &#x1F6BB; | &#x1F6BB; | &#x1F6BB; | 
| baby symbol | &#x1F6BC; | &#x1F6BC; | &#x1F6BC; | 
| water closet | &#x1F6BE; | &#x1F6BE; | &#x1F6BE; | 
| passport control | &#x1F6C2; | &#x1F6C2; | &#x1F6C2; | 
| customs | &#x1F6C3; | &#x1F6C3; | &#x1F6C3; | 
| baggage claim | &#x1F6C4; | &#x1F6C4; | &#x1F6C4; | 
| left luggage | &#x1F6C5; | &#x1F6C5; | &#x1F6C5; | 

### warning

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| warning | &#x26A0;&#xFE0F; | &#x26A0;&#xFE0F; | &#x26A0;&#xFE0F; | 
| children crossing | &#x1F6B8; | &#x1F6B8; | &#x1F6B8; | 
| no entry | &#x26D4; | &#x26D4; | &#x26D4; | 
| prohibited | &#x1F6AB; | &#x1F6AB; | &#x1F6AB; | 
| no bicycles | &#x1F6B3; | &#x1F6B3; | &#x1F6B3; | 
| no smoking | &#x1F6AD; | &#x1F6AD; | &#x1F6AD; | 
| no littering | &#x1F6AF; | &#x1F6AF; | &#x1F6AF; | 
| non-potable water | &#x1F6B1; | &#x1F6B1; | &#x1F6B1; | 
| no pedestrians | &#x1F6B7; | &#x1F6B7; | &#x1F6B7; | 
| no mobile phones | &#x1F4F5; | &#x1F4F5; | &#x1F4F5; | 
| no one under eighteen | &#x1F51E; | &#x1F51E; | &#x1F51E; | 
| radioactive | &#x2622;&#xFE0F; | &#x2622;&#xFE0F; | &#x2622;&#xFE0F; | 
| biohazard | &#x2623;&#xFE0F; | &#x2623;&#xFE0F; | &#x2623;&#xFE0F; | 

### arrow

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| up arrow | &#x2B06;&#xFE0F; | &#x2B06;&#xFE0F; | &#x2B06;&#xFE0F; | 
| up-right arrow | &#x2197;&#xFE0F; | &#x2197;&#xFE0F; | &#x2197;&#xFE0F; | 
| right arrow | &#x27A1;&#xFE0F; | &#x27A1;&#xFE0F; | &#x27A1;&#xFE0F; | 
| down-right arrow | &#x2198;&#xFE0F; | &#x2198;&#xFE0F; | &#x2198;&#xFE0F; | 
| down arrow | &#x2B07;&#xFE0F; | &#x2B07;&#xFE0F; | &#x2B07;&#xFE0F; | 
| down-left arrow | &#x2199;&#xFE0F; | &#x2199;&#xFE0F; | &#x2199;&#xFE0F; | 
| left arrow | &#x2B05;&#xFE0F; | &#x2B05;&#xFE0F; | &#x2B05;&#xFE0F; | 
| up-left arrow | &#x2196;&#xFE0F; | &#x2196;&#xFE0F; | &#x2196;&#xFE0F; | 
| up-down arrow | &#x2195;&#xFE0F; | &#x2195;&#xFE0F; | &#x2195;&#xFE0F; | 
| left-right arrow | &#x2194;&#xFE0F; | &#x2194;&#xFE0F; | &#x2194;&#xFE0F; | 
| right arrow curving left | &#x21A9;&#xFE0F; | &#x21A9;&#xFE0F; | &#x21A9;&#xFE0F; | 
| left arrow curving right | &#x21AA;&#xFE0F; | &#x21AA;&#xFE0F; | &#x21AA;&#xFE0F; | 
| right arrow curving up | &#x2934;&#xFE0F; | &#x2934;&#xFE0F; | &#x2934;&#xFE0F; | 
| right arrow curving down | &#x2935;&#xFE0F; | &#x2935;&#xFE0F; | &#x2935;&#xFE0F; | 
| clockwise vertical arrows | &#x1F503; | &#x1F503; | &#x1F503; | 
| counterclockwise arrows button | &#x1F504; | &#x1F504; | &#x1F504; | 
| BACK arrow | &#x1F519; | &#x1F519; | &#x1F519; | 
| END arrow | &#x1F51A; | &#x1F51A; | &#x1F51A; | 
| ON! arrow | &#x1F51B; | &#x1F51B; | &#x1F51B; | 
| SOON arrow | &#x1F51C; | &#x1F51C; | &#x1F51C; | 
| TOP arrow | &#x1F51D; | &#x1F51D; | &#x1F51D; | 

### religion

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| place of worship | &#x1F6D0; | &#x1F6D0; | &#x1F6D0; | 
| atom symbol | &#x269B;&#xFE0F; | &#x269B;&#xFE0F; | &#x269B;&#xFE0F; | 
| om | &#x1F549;&#xFE0F; | &#x1F549;&#xFE0F; | &#x1F549;&#xFE0F; | 
| star of David | &#x2721;&#xFE0F; | &#x2721;&#xFE0F; | &#x2721;&#xFE0F; | 
| wheel of dharma | &#x2638;&#xFE0F; | &#x2638;&#xFE0F; | &#x2638;&#xFE0F; | 
| yin yang | &#x262F;&#xFE0F; | &#x262F;&#xFE0F; | &#x262F;&#xFE0F; | 
| latin cross | &#x271D;&#xFE0F; | &#x271D;&#xFE0F; | &#x271D;&#xFE0F; | 
| orthodox cross | &#x2626;&#xFE0F; | &#x2626;&#xFE0F; | &#x2626;&#xFE0F; | 
| star and crescent | &#x262A;&#xFE0F; | &#x262A;&#xFE0F; | &#x262A;&#xFE0F; | 
| peace symbol | &#x262E;&#xFE0F; | &#x262E;&#xFE0F; | &#x262E;&#xFE0F; | 
| menorah | &#x1F54E; | &#x1F54E; | &#x1F54E; | 
| dotted six-pointed star | &#x1F52F; | &#x1F52F; | &#x1F52F; | 

### zodiac

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| Aries | &#x2648; | &#x2648; | &#x2648; | 
| Taurus | &#x2649; | &#x2649; | &#x2649; | 
| Gemini | &#x264A; | &#x264A; | &#x264A; | 
| Cancer | &#x264B; | &#x264B; | &#x264B; | 
| Leo | &#x264C; | &#x264C; | &#x264C; | 
| Virgo | &#x264D; | &#x264D; | &#x264D; | 
| Libra | &#x264E; | &#x264E; | &#x264E; | 
| Scorpio | &#x264F; | &#x264F; | &#x264F; | 
| Sagittarius | &#x2650; | &#x2650; | &#x2650; | 
| Capricorn | &#x2651; | &#x2651; | &#x2651; | 
| Aquarius | &#x2652; | &#x2652; | &#x2652; | 
| Pisces | &#x2653; | &#x2653; | &#x2653; | 
| Ophiuchus | &#x26CE; | &#x26CE; | &#x26CE; | 

### av-symbol

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| shuffle tracks button | &#x1F500; | &#x1F500; | &#x1F500; | 
| repeat button | &#x1F501; | &#x1F501; | &#x1F501; | 
| repeat single button | &#x1F502; | &#x1F502; | &#x1F502; | 
| play button | &#x25B6;&#xFE0F; | &#x25B6;&#xFE0F; | &#x25B6;&#xFE0F; | 
| fast-forward button | &#x23E9; | &#x23E9; | &#x23E9; | 
| next track button | &#x23ED;&#xFE0F; | &#x23ED;&#xFE0F; | &#x23ED;&#xFE0F; | 
| play or pause button | &#x23EF;&#xFE0F; | &#x23EF;&#xFE0F; | &#x23EF;&#xFE0F; | 
| reverse button | &#x25C0;&#xFE0F; | &#x25C0;&#xFE0F; | &#x25C0;&#xFE0F; | 
| fast reverse button | &#x23EA; | &#x23EA; | &#x23EA; | 
| last track button | &#x23EE;&#xFE0F; | &#x23EE;&#xFE0F; | &#x23EE;&#xFE0F; | 
| upwards button | &#x1F53C; | &#x1F53C; | &#x1F53C; | 
| fast up button | &#x23EB; | &#x23EB; | &#x23EB; | 
| downwards button | &#x1F53D; | &#x1F53D; | &#x1F53D; | 
| fast down button | &#x23EC; | &#x23EC; | &#x23EC; | 
| pause button | &#x23F8;&#xFE0F; | &#x23F8;&#xFE0F; | &#x23F8;&#xFE0F; | 
| stop button | &#x23F9;&#xFE0F; | &#x23F9;&#xFE0F; | &#x23F9;&#xFE0F; | 
| record button | &#x23FA;&#xFE0F; | &#x23FA;&#xFE0F; | &#x23FA;&#xFE0F; | 
| eject button | &#x23CF;&#xFE0F; | &#x23CF;&#xFE0F; | &#x23CF;&#xFE0F; | 
| cinema | &#x1F3A6; | &#x1F3A6; | &#x1F3A6; | 
| dim button | &#x1F505; | &#x1F505; | &#x1F505; | 
| bright button | &#x1F506; | &#x1F506; | &#x1F506; | 
| antenna bars | &#x1F4F6; | &#x1F4F6; | &#x1F4F6; | 
| vibration mode | &#x1F4F3; | &#x1F4F3; | &#x1F4F3; | 
| mobile phone off | &#x1F4F4; | &#x1F4F4; | &#x1F4F4; | 

### gender

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| female sign | &#x2640;&#xFE0F; | &#x2640;&#xFE0F; | &#x2640;&#xFE0F; | 
| male sign | &#x2642;&#xFE0F; | &#x2642;&#xFE0F; | &#x2642;&#xFE0F; | 
| transgender symbol |  | &#x26A7;&#xFE0F; | &#x26A7;&#xFE0F; | 

### math

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| multiply | &#x2716;&#xFE0F; | &#x2716;&#xFE0F; | &#x2716;&#xFE0F; | 
| plus | &#x2795; | &#x2795; | &#x2795; | 
| minus | &#x2796; | &#x2796; | &#x2796; | 
| divide | &#x2797; | &#x2797; | &#x2797; | 
| infinity |  | &#x267E;&#xFE0F; | &#x267E;&#xFE0F; | 

### punctuation

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| double exclamation mark | &#x203C;&#xFE0F; | &#x203C;&#xFE0F; | &#x203C;&#xFE0F; | 
| exclamation question mark | &#x2049;&#xFE0F; | &#x2049;&#xFE0F; | &#x2049;&#xFE0F; | 
| question mark | &#x2753; | &#x2753; | &#x2753; | 
| white question mark | &#x2754; | &#x2754; | &#x2754; | 
| white exclamation mark | &#x2755; | &#x2755; | &#x2755; | 
| exclamation mark | &#x2757; | &#x2757; | &#x2757; | 
| wavy dash | &#x3030;&#xFE0F; | &#x3030;&#xFE0F; | &#x3030;&#xFE0F; | 

### currency

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| currency exchange | &#x1F4B1; | &#x1F4B1; | &#x1F4B1; | 
| heavy dollar sign | &#x1F4B2; | &#x1F4B2; | &#x1F4B2; | 

### other-symbol

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| medical symbol | &#x2695;&#xFE0F; | &#x2695;&#xFE0F; | &#x2695;&#xFE0F; | 
| recycling symbol | &#x267B;&#xFE0F; | &#x267B;&#xFE0F; | &#x267B;&#xFE0F; | 
| fleur-de-lis | &#x269C;&#xFE0F; | &#x269C;&#xFE0F; | &#x269C;&#xFE0F; | 
| trident emblem | &#x1F531; | &#x1F531; | &#x1F531; | 
| name badge | &#x1F4DB; | &#x1F4DB; | &#x1F4DB; | 
| Japanese symbol for beginner | &#x1F530; | &#x1F530; | &#x1F530; | 
| hollow red circle | &#x2B55; | &#x2B55; | &#x2B55; | 
| check mark button | &#x2705; | &#x2705; | &#x2705; | 
| check box with check | &#x2611;&#xFE0F; | &#x2611;&#xFE0F; | &#x2611;&#xFE0F; | 
| check mark | &#x2714;&#xFE0F; | &#x2714;&#xFE0F; | &#x2714;&#xFE0F; | 
| cross mark | &#x274C; | &#x274C; | &#x274C; | 
| cross mark button | &#x274E; | &#x274E; | &#x274E; | 
| curly loop | &#x27B0; | &#x27B0; | &#x27B0; | 
| double curly loop | &#x27BF; | &#x27BF; | &#x27BF; | 
| part alternation mark | &#x303D;&#xFE0F; | &#x303D;&#xFE0F; | &#x303D;&#xFE0F; | 
| eight-spoked asterisk | &#x2733;&#xFE0F; | &#x2733;&#xFE0F; | &#x2733;&#xFE0F; | 
| eight-pointed star | &#x2734;&#xFE0F; | &#x2734;&#xFE0F; | &#x2734;&#xFE0F; | 
| sparkle | &#x2747;&#xFE0F; | &#x2747;&#xFE0F; | &#x2747;&#xFE0F; | 
| copyright | &#x00A9;&#xFE0F; | &#x00A9;&#xFE0F; | &#x00A9;&#xFE0F; | 
| registered | &#x00AE;&#xFE0F; | &#x00AE;&#xFE0F; | &#x00AE;&#xFE0F; | 
| trade mark | &#x2122;&#xFE0F; | &#x2122;&#xFE0F; | &#x2122;&#xFE0F; | 

### keycap

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| keycap: # | &#x0023;&#xFE0F;&#x20E3; | &#x0023;&#xFE0F;&#x20E3; | &#x0023;&#xFE0F;&#x20E3; | 
| keycap: * | &#x002A;&#xFE0F;&#x20E3; | &#x002A;&#xFE0F;&#x20E3; | &#x002A;&#xFE0F;&#x20E3; | 
| keycap: 0 | &#x0030;&#xFE0F;&#x20E3; | &#x0030;&#xFE0F;&#x20E3; | &#x0030;&#xFE0F;&#x20E3; | 
| keycap: 1 | &#x0031;&#xFE0F;&#x20E3; | &#x0031;&#xFE0F;&#x20E3; | &#x0031;&#xFE0F;&#x20E3; | 
| keycap: 2 | &#x0032;&#xFE0F;&#x20E3; | &#x0032;&#xFE0F;&#x20E3; | &#x0032;&#xFE0F;&#x20E3; | 
| keycap: 3 | &#x0033;&#xFE0F;&#x20E3; | &#x0033;&#xFE0F;&#x20E3; | &#x0033;&#xFE0F;&#x20E3; | 
| keycap: 4 | &#x0034;&#xFE0F;&#x20E3; | &#x0034;&#xFE0F;&#x20E3; | &#x0034;&#xFE0F;&#x20E3; | 
| keycap: 5 | &#x0035;&#xFE0F;&#x20E3; | &#x0035;&#xFE0F;&#x20E3; | &#x0035;&#xFE0F;&#x20E3; | 
| keycap: 6 | &#x0036;&#xFE0F;&#x20E3; | &#x0036;&#xFE0F;&#x20E3; | &#x0036;&#xFE0F;&#x20E3; | 
| keycap: 7 | &#x0037;&#xFE0F;&#x20E3; | &#x0037;&#xFE0F;&#x20E3; | &#x0037;&#xFE0F;&#x20E3; | 
| keycap: 8 | &#x0038;&#xFE0F;&#x20E3; | &#x0038;&#xFE0F;&#x20E3; | &#x0038;&#xFE0F;&#x20E3; | 
| keycap: 9 | &#x0039;&#xFE0F;&#x20E3; | &#x0039;&#xFE0F;&#x20E3; | &#x0039;&#xFE0F;&#x20E3; | 
| keycap: 10 | &#x1F51F; | &#x1F51F; | &#x1F51F; | 

### alphanum

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| input latin uppercase | &#x1F520; | &#x1F520; | &#x1F520; | 
| input latin lowercase | &#x1F521; | &#x1F521; | &#x1F521; | 
| input numbers | &#x1F522; | &#x1F522; | &#x1F522; | 
| input symbols | &#x1F523; | &#x1F523; | &#x1F523; | 
| input latin letters | &#x1F524; | &#x1F524; | &#x1F524; | 
| A button (blood type) | &#x1F170;&#xFE0F; | &#x1F170;&#xFE0F; | &#x1F170;&#xFE0F; | 
| AB button (blood type) | &#x1F18E; | &#x1F18E; | &#x1F18E; | 
| B button (blood type) | &#x1F171;&#xFE0F; | &#x1F171;&#xFE0F; | &#x1F171;&#xFE0F; | 
| CL button | &#x1F191; | &#x1F191; | &#x1F191; | 
| COOL button | &#x1F192; | &#x1F192; | &#x1F192; | 
| FREE button | &#x1F193; | &#x1F193; | &#x1F193; | 
| information | &#x2139;&#xFE0F; | &#x2139;&#xFE0F; | &#x2139;&#xFE0F; | 
| ID button | &#x1F194; | &#x1F194; | &#x1F194; | 
| circled M | &#x24C2;&#xFE0F; | &#x24C2;&#xFE0F; | &#x24C2;&#xFE0F; | 
| NEW button | &#x1F195; | &#x1F195; | &#x1F195; | 
| NG button | &#x1F196; | &#x1F196; | &#x1F196; | 
| O button (blood type) | &#x1F17E;&#xFE0F; | &#x1F17E;&#xFE0F; | &#x1F17E;&#xFE0F; | 
| OK button | &#x1F197; | &#x1F197; | &#x1F197; | 
| P button | &#x1F17F;&#xFE0F; | &#x1F17F;&#xFE0F; | &#x1F17F;&#xFE0F; | 
| SOS button | &#x1F198; | &#x1F198; | &#x1F198; | 
| UP! button | &#x1F199; | &#x1F199; | &#x1F199; | 
| VS button | &#x1F19A; | &#x1F19A; | &#x1F19A; | 
| Japanese “here” button | &#x1F201; | &#x1F201; | &#x1F201; | 
| Japanese “service charge” button | &#x1F202;&#xFE0F; | &#x1F202;&#xFE0F; | &#x1F202;&#xFE0F; | 
| Japanese “monthly amount” button | &#x1F237;&#xFE0F; | &#x1F237;&#xFE0F; | &#x1F237;&#xFE0F; | 
| Japanese “not free of charge” button | &#x1F236; | &#x1F236; | &#x1F236; | 
| Japanese “reserved” button | &#x1F22F; | &#x1F22F; | &#x1F22F; | 
| Japanese “bargain” button | &#x1F250; | &#x1F250; | &#x1F250; | 
| Japanese “discount” button | &#x1F239; | &#x1F239; | &#x1F239; | 
| Japanese “free of charge” button | &#x1F21A; | &#x1F21A; | &#x1F21A; | 
| Japanese “prohibited” button | &#x1F232; | &#x1F232; | &#x1F232; | 
| Japanese “acceptable” button | &#x1F251; | &#x1F251; | &#x1F251; | 
| Japanese “application” button | &#x1F238; | &#x1F238; | &#x1F238; | 
| Japanese “passing grade” button | &#x1F234; | &#x1F234; | &#x1F234; | 
| Japanese “vacancy” button | &#x1F233; | &#x1F233; | &#x1F233; | 
| Japanese “congratulations” button | &#x3297;&#xFE0F; | &#x3297;&#xFE0F; | &#x3297;&#xFE0F; | 
| Japanese “secret” button | &#x3299;&#xFE0F; | &#x3299;&#xFE0F; | &#x3299;&#xFE0F; | 
| Japanese “open for business” button | &#x1F23A; | &#x1F23A; | &#x1F23A; | 
| Japanese “no vacancy” button | &#x1F235; | &#x1F235; | &#x1F235; | 

### geometric

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| red circle | &#x1F534; | &#x1F534; | &#x1F534; | 
| orange circle |  | &#x1F7E0; | &#x1F7E0; | 
| yellow circle |  | &#x1F7E1; | &#x1F7E1; | 
| green circle |  | &#x1F7E2; | &#x1F7E2; | 
| blue circle | &#x1F535; | &#x1F535; | &#x1F535; | 
| purple circle |  | &#x1F7E3; | &#x1F7E3; | 
| brown circle |  | &#x1F7E4; | &#x1F7E4; | 
| black circle | &#x26AB; | &#x26AB; | &#x26AB; | 
| white circle | &#x26AA; | &#x26AA; | &#x26AA; | 
| red square |  | &#x1F7E5; | &#x1F7E5; | 
| orange square |  | &#x1F7E7; | &#x1F7E7; | 
| yellow square |  | &#x1F7E8; | &#x1F7E8; | 
| green square |  | &#x1F7E9; | &#x1F7E9; | 
| blue square |  | &#x1F7E6; | &#x1F7E6; | 
| purple square |  | &#x1F7EA; | &#x1F7EA; | 
| brown square |  | &#x1F7EB; | &#x1F7EB; | 
| black large square | &#x2B1B; | &#x2B1B; | &#x2B1B; | 
| white large square | &#x2B1C; | &#x2B1C; | &#x2B1C; | 
| black medium square | &#x25FC;&#xFE0F; | &#x25FC;&#xFE0F; | &#x25FC;&#xFE0F; | 
| white medium square | &#x25FB;&#xFE0F; | &#x25FB;&#xFE0F; | &#x25FB;&#xFE0F; | 
| black medium-small square | &#x25FE; | &#x25FE; | &#x25FE; | 
| white medium-small square | &#x25FD; | &#x25FD; | &#x25FD; | 
| black small square | &#x25AA;&#xFE0F; | &#x25AA;&#xFE0F; | &#x25AA;&#xFE0F; | 
| white small square | &#x25AB;&#xFE0F; | &#x25AB;&#xFE0F; | &#x25AB;&#xFE0F; | 
| large orange diamond | &#x1F536; | &#x1F536; | &#x1F536; | 
| large blue diamond | &#x1F537; | &#x1F537; | &#x1F537; | 
| small orange diamond | &#x1F538; | &#x1F538; | &#x1F538; | 
| small blue diamond | &#x1F539; | &#x1F539; | &#x1F539; | 
| red triangle pointed up | &#x1F53A; | &#x1F53A; | &#x1F53A; | 
| red triangle pointed down | &#x1F53B; | &#x1F53B; | &#x1F53B; | 
| diamond with a dot | &#x1F4A0; | &#x1F4A0; | &#x1F4A0; | 
| radio button | &#x1F518; | &#x1F518; | &#x1F518; | 
| white square button | &#x1F533; | &#x1F533; | &#x1F533; | 
| black square button | &#x1F532; | &#x1F532; | &#x1F532; | 

## Flags


### flag

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| chequered flag | &#x1F3C1; | &#x1F3C1; | &#x1F3C1; | 
| triangular flag | &#x1F6A9; | &#x1F6A9; | &#x1F6A9; | 
| crossed flags | &#x1F38C; | &#x1F38C; | &#x1F38C; | 
| black flag | &#x1F3F4; | &#x1F3F4; | &#x1F3F4; | 
| white flag | &#x1F3F3;&#xFE0F; | &#x1F3F3;&#xFE0F; | &#x1F3F3;&#xFE0F; | 
| rainbow flag | &#x1F3F3;&#xFE0F;&#x200D;&#x1F308; | &#x1F3F3;&#xFE0F;&#x200D;&#x1F308; | &#x1F3F3;&#xFE0F;&#x200D;&#x1F308; | 
| transgender flag |  | &#x1F3F3;&#xFE0F;&#x200D;&#x26A7;&#xFE0F; | &#x1F3F3;&#xFE0F;&#x200D;&#x26A7;&#xFE0F; | 
| pirate flag |  | &#x1F3F4;&#x200D;&#x2620;&#xFE0F; | &#x1F3F4;&#x200D;&#x2620;&#xFE0F; | 

### country-flag

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| flag: Ascension Island | &#x1F1E6;&#x1F1E8; | &#x1F1E6;&#x1F1E8; | &#x1F1E6;&#x1F1E8; | 
| flag: Andorra | &#x1F1E6;&#x1F1E9; | &#x1F1E6;&#x1F1E9; | &#x1F1E6;&#x1F1E9; | 
| flag: United Arab Emirates | &#x1F1E6;&#x1F1EA; | &#x1F1E6;&#x1F1EA; | &#x1F1E6;&#x1F1EA; | 
| flag: Afghanistan | &#x1F1E6;&#x1F1EB; | &#x1F1E6;&#x1F1EB; | &#x1F1E6;&#x1F1EB; | 
| flag: Antigua & Barbuda | &#x1F1E6;&#x1F1EC; | &#x1F1E6;&#x1F1EC; | &#x1F1E6;&#x1F1EC; | 
| flag: Anguilla | &#x1F1E6;&#x1F1EE; | &#x1F1E6;&#x1F1EE; | &#x1F1E6;&#x1F1EE; | 
| flag: Albania | &#x1F1E6;&#x1F1F1; | &#x1F1E6;&#x1F1F1; | &#x1F1E6;&#x1F1F1; | 
| flag: Armenia | &#x1F1E6;&#x1F1F2; | &#x1F1E6;&#x1F1F2; | &#x1F1E6;&#x1F1F2; | 
| flag: Angola | &#x1F1E6;&#x1F1F4; | &#x1F1E6;&#x1F1F4; | &#x1F1E6;&#x1F1F4; | 
| flag: Antarctica | &#x1F1E6;&#x1F1F6; | &#x1F1E6;&#x1F1F6; | &#x1F1E6;&#x1F1F6; | 
| flag: Argentina | &#x1F1E6;&#x1F1F7; | &#x1F1E6;&#x1F1F7; | &#x1F1E6;&#x1F1F7; | 
| flag: American Samoa | &#x1F1E6;&#x1F1F8; | &#x1F1E6;&#x1F1F8; | &#x1F1E6;&#x1F1F8; | 
| flag: Austria | &#x1F1E6;&#x1F1F9; | &#x1F1E6;&#x1F1F9; | &#x1F1E6;&#x1F1F9; | 
| flag: Australia | &#x1F1E6;&#x1F1FA; | &#x1F1E6;&#x1F1FA; | &#x1F1E6;&#x1F1FA; | 
| flag: Aruba | &#x1F1E6;&#x1F1FC; | &#x1F1E6;&#x1F1FC; | &#x1F1E6;&#x1F1FC; | 
| flag: Åland Islands | &#x1F1E6;&#x1F1FD; | &#x1F1E6;&#x1F1FD; | &#x1F1E6;&#x1F1FD; | 
| flag: Azerbaijan | &#x1F1E6;&#x1F1FF; | &#x1F1E6;&#x1F1FF; | &#x1F1E6;&#x1F1FF; | 
| flag: Bosnia & Herzegovina | &#x1F1E7;&#x1F1E6; | &#x1F1E7;&#x1F1E6; | &#x1F1E7;&#x1F1E6; | 
| flag: Barbados | &#x1F1E7;&#x1F1E7; | &#x1F1E7;&#x1F1E7; | &#x1F1E7;&#x1F1E7; | 
| flag: Bangladesh | &#x1F1E7;&#x1F1E9; | &#x1F1E7;&#x1F1E9; | &#x1F1E7;&#x1F1E9; | 
| flag: Belgium | &#x1F1E7;&#x1F1EA; | &#x1F1E7;&#x1F1EA; | &#x1F1E7;&#x1F1EA; | 
| flag: Burkina Faso | &#x1F1E7;&#x1F1EB; | &#x1F1E7;&#x1F1EB; | &#x1F1E7;&#x1F1EB; | 
| flag: Bulgaria | &#x1F1E7;&#x1F1EC; | &#x1F1E7;&#x1F1EC; | &#x1F1E7;&#x1F1EC; | 
| flag: Bahrain | &#x1F1E7;&#x1F1ED; | &#x1F1E7;&#x1F1ED; | &#x1F1E7;&#x1F1ED; | 
| flag: Burundi | &#x1F1E7;&#x1F1EE; | &#x1F1E7;&#x1F1EE; | &#x1F1E7;&#x1F1EE; | 
| flag: Benin | &#x1F1E7;&#x1F1EF; | &#x1F1E7;&#x1F1EF; | &#x1F1E7;&#x1F1EF; | 
| flag: St. Barthélemy | &#x1F1E7;&#x1F1F1; | &#x1F1E7;&#x1F1F1; | &#x1F1E7;&#x1F1F1; | 
| flag: Bermuda | &#x1F1E7;&#x1F1F2; | &#x1F1E7;&#x1F1F2; | &#x1F1E7;&#x1F1F2; | 
| flag: Brunei | &#x1F1E7;&#x1F1F3; | &#x1F1E7;&#x1F1F3; | &#x1F1E7;&#x1F1F3; | 
| flag: Bolivia | &#x1F1E7;&#x1F1F4; | &#x1F1E7;&#x1F1F4; | &#x1F1E7;&#x1F1F4; | 
| flag: Caribbean Netherlands | &#x1F1E7;&#x1F1F6; | &#x1F1E7;&#x1F1F6; | &#x1F1E7;&#x1F1F6; | 
| flag: Brazil | &#x1F1E7;&#x1F1F7; | &#x1F1E7;&#x1F1F7; | &#x1F1E7;&#x1F1F7; | 
| flag: Bahamas | &#x1F1E7;&#x1F1F8; | &#x1F1E7;&#x1F1F8; | &#x1F1E7;&#x1F1F8; | 
| flag: Bhutan | &#x1F1E7;&#x1F1F9; | &#x1F1E7;&#x1F1F9; | &#x1F1E7;&#x1F1F9; | 
| flag: Bouvet Island | &#x1F1E7;&#x1F1FB; | &#x1F1E7;&#x1F1FB; | &#x1F1E7;&#x1F1FB; | 
| flag: Botswana | &#x1F1E7;&#x1F1FC; | &#x1F1E7;&#x1F1FC; | &#x1F1E7;&#x1F1FC; | 
| flag: Belarus | &#x1F1E7;&#x1F1FE; | &#x1F1E7;&#x1F1FE; | &#x1F1E7;&#x1F1FE; | 
| flag: Belize | &#x1F1E7;&#x1F1FF; | &#x1F1E7;&#x1F1FF; | &#x1F1E7;&#x1F1FF; | 
| flag: Canada | &#x1F1E8;&#x1F1E6; | &#x1F1E8;&#x1F1E6; | &#x1F1E8;&#x1F1E6; | 
| flag: Cocos (Keeling) Islands | &#x1F1E8;&#x1F1E8; | &#x1F1E8;&#x1F1E8; | &#x1F1E8;&#x1F1E8; | 
| flag: Congo - Kinshasa | &#x1F1E8;&#x1F1E9; | &#x1F1E8;&#x1F1E9; | &#x1F1E8;&#x1F1E9; | 
| flag: Central African Republic | &#x1F1E8;&#x1F1EB; | &#x1F1E8;&#x1F1EB; | &#x1F1E8;&#x1F1EB; | 
| flag: Congo - Brazzaville | &#x1F1E8;&#x1F1EC; | &#x1F1E8;&#x1F1EC; | &#x1F1E8;&#x1F1EC; | 
| flag: Switzerland | &#x1F1E8;&#x1F1ED; | &#x1F1E8;&#x1F1ED; | &#x1F1E8;&#x1F1ED; | 
| flag: Côte d’Ivoire | &#x1F1E8;&#x1F1EE; | &#x1F1E8;&#x1F1EE; | &#x1F1E8;&#x1F1EE; | 
| flag: Cook Islands | &#x1F1E8;&#x1F1F0; | &#x1F1E8;&#x1F1F0; | &#x1F1E8;&#x1F1F0; | 
| flag: Chile | &#x1F1E8;&#x1F1F1; | &#x1F1E8;&#x1F1F1; | &#x1F1E8;&#x1F1F1; | 
| flag: Cameroon | &#x1F1E8;&#x1F1F2; | &#x1F1E8;&#x1F1F2; | &#x1F1E8;&#x1F1F2; | 
| flag: China | &#x1F1E8;&#x1F1F3; | &#x1F1E8;&#x1F1F3; | &#x1F1E8;&#x1F1F3; | 
| flag: Colombia | &#x1F1E8;&#x1F1F4; | &#x1F1E8;&#x1F1F4; | &#x1F1E8;&#x1F1F4; | 
| flag: Clipperton Island | &#x1F1E8;&#x1F1F5; | &#x1F1E8;&#x1F1F5; | &#x1F1E8;&#x1F1F5; | 
| flag: Costa Rica | &#x1F1E8;&#x1F1F7; | &#x1F1E8;&#x1F1F7; | &#x1F1E8;&#x1F1F7; | 
| flag: Cuba | &#x1F1E8;&#x1F1FA; | &#x1F1E8;&#x1F1FA; | &#x1F1E8;&#x1F1FA; | 
| flag: Cape Verde | &#x1F1E8;&#x1F1FB; | &#x1F1E8;&#x1F1FB; | &#x1F1E8;&#x1F1FB; | 
| flag: Curaçao | &#x1F1E8;&#x1F1FC; | &#x1F1E8;&#x1F1FC; | &#x1F1E8;&#x1F1FC; | 
| flag: Christmas Island | &#x1F1E8;&#x1F1FD; | &#x1F1E8;&#x1F1FD; | &#x1F1E8;&#x1F1FD; | 
| flag: Cyprus | &#x1F1E8;&#x1F1FE; | &#x1F1E8;&#x1F1FE; | &#x1F1E8;&#x1F1FE; | 
| flag: Czechia | &#x1F1E8;&#x1F1FF; | &#x1F1E8;&#x1F1FF; | &#x1F1E8;&#x1F1FF; | 
| flag: Germany | &#x1F1E9;&#x1F1EA; | &#x1F1E9;&#x1F1EA; | &#x1F1E9;&#x1F1EA; | 
| flag: Diego Garcia | &#x1F1E9;&#x1F1EC; | &#x1F1E9;&#x1F1EC; | &#x1F1E9;&#x1F1EC; | 
| flag: Djibouti | &#x1F1E9;&#x1F1EF; | &#x1F1E9;&#x1F1EF; | &#x1F1E9;&#x1F1EF; | 
| flag: Denmark | &#x1F1E9;&#x1F1F0; | &#x1F1E9;&#x1F1F0; | &#x1F1E9;&#x1F1F0; | 
| flag: Dominica | &#x1F1E9;&#x1F1F2; | &#x1F1E9;&#x1F1F2; | &#x1F1E9;&#x1F1F2; | 
| flag: Dominican Republic | &#x1F1E9;&#x1F1F4; | &#x1F1E9;&#x1F1F4; | &#x1F1E9;&#x1F1F4; | 
| flag: Algeria | &#x1F1E9;&#x1F1FF; | &#x1F1E9;&#x1F1FF; | &#x1F1E9;&#x1F1FF; | 
| flag: Ceuta & Melilla | &#x1F1EA;&#x1F1E6; | &#x1F1EA;&#x1F1E6; | &#x1F1EA;&#x1F1E6; | 
| flag: Ecuador | &#x1F1EA;&#x1F1E8; | &#x1F1EA;&#x1F1E8; | &#x1F1EA;&#x1F1E8; | 
| flag: Estonia | &#x1F1EA;&#x1F1EA; | &#x1F1EA;&#x1F1EA; | &#x1F1EA;&#x1F1EA; | 
| flag: Egypt | &#x1F1EA;&#x1F1EC; | &#x1F1EA;&#x1F1EC; | &#x1F1EA;&#x1F1EC; | 
| flag: Western Sahara | &#x1F1EA;&#x1F1ED; | &#x1F1EA;&#x1F1ED; | &#x1F1EA;&#x1F1ED; | 
| flag: Eritrea | &#x1F1EA;&#x1F1F7; | &#x1F1EA;&#x1F1F7; | &#x1F1EA;&#x1F1F7; | 
| flag: Spain | &#x1F1EA;&#x1F1F8; | &#x1F1EA;&#x1F1F8; | &#x1F1EA;&#x1F1F8; | 
| flag: Ethiopia | &#x1F1EA;&#x1F1F9; | &#x1F1EA;&#x1F1F9; | &#x1F1EA;&#x1F1F9; | 
| flag: European Union | &#x1F1EA;&#x1F1FA; | &#x1F1EA;&#x1F1FA; | &#x1F1EA;&#x1F1FA; | 
| flag: Finland | &#x1F1EB;&#x1F1EE; | &#x1F1EB;&#x1F1EE; | &#x1F1EB;&#x1F1EE; | 
| flag: Fiji | &#x1F1EB;&#x1F1EF; | &#x1F1EB;&#x1F1EF; | &#x1F1EB;&#x1F1EF; | 
| flag: Falkland Islands | &#x1F1EB;&#x1F1F0; | &#x1F1EB;&#x1F1F0; | &#x1F1EB;&#x1F1F0; | 
| flag: Micronesia | &#x1F1EB;&#x1F1F2; | &#x1F1EB;&#x1F1F2; | &#x1F1EB;&#x1F1F2; | 
| flag: Faroe Islands | &#x1F1EB;&#x1F1F4; | &#x1F1EB;&#x1F1F4; | &#x1F1EB;&#x1F1F4; | 
| flag: France | &#x1F1EB;&#x1F1F7; | &#x1F1EB;&#x1F1F7; | &#x1F1EB;&#x1F1F7; | 
| flag: Gabon | &#x1F1EC;&#x1F1E6; | &#x1F1EC;&#x1F1E6; | &#x1F1EC;&#x1F1E6; | 
| flag: United Kingdom | &#x1F1EC;&#x1F1E7; | &#x1F1EC;&#x1F1E7; | &#x1F1EC;&#x1F1E7; | 
| flag: Grenada | &#x1F1EC;&#x1F1E9; | &#x1F1EC;&#x1F1E9; | &#x1F1EC;&#x1F1E9; | 
| flag: Georgia | &#x1F1EC;&#x1F1EA; | &#x1F1EC;&#x1F1EA; | &#x1F1EC;&#x1F1EA; | 
| flag: French Guiana | &#x1F1EC;&#x1F1EB; | &#x1F1EC;&#x1F1EB; | &#x1F1EC;&#x1F1EB; | 
| flag: Guernsey | &#x1F1EC;&#x1F1EC; | &#x1F1EC;&#x1F1EC; | &#x1F1EC;&#x1F1EC; | 
| flag: Ghana | &#x1F1EC;&#x1F1ED; | &#x1F1EC;&#x1F1ED; | &#x1F1EC;&#x1F1ED; | 
| flag: Gibraltar | &#x1F1EC;&#x1F1EE; | &#x1F1EC;&#x1F1EE; | &#x1F1EC;&#x1F1EE; | 
| flag: Greenland | &#x1F1EC;&#x1F1F1; | &#x1F1EC;&#x1F1F1; | &#x1F1EC;&#x1F1F1; | 
| flag: Gambia | &#x1F1EC;&#x1F1F2; | &#x1F1EC;&#x1F1F2; | &#x1F1EC;&#x1F1F2; | 
| flag: Guinea | &#x1F1EC;&#x1F1F3; | &#x1F1EC;&#x1F1F3; | &#x1F1EC;&#x1F1F3; | 
| flag: Guadeloupe | &#x1F1EC;&#x1F1F5; | &#x1F1EC;&#x1F1F5; | &#x1F1EC;&#x1F1F5; | 
| flag: Equatorial Guinea | &#x1F1EC;&#x1F1F6; | &#x1F1EC;&#x1F1F6; | &#x1F1EC;&#x1F1F6; | 
| flag: Greece | &#x1F1EC;&#x1F1F7; | &#x1F1EC;&#x1F1F7; | &#x1F1EC;&#x1F1F7; | 
| flag: South Georgia & South Sandwich Islands | &#x1F1EC;&#x1F1F8; | &#x1F1EC;&#x1F1F8; | &#x1F1EC;&#x1F1F8; | 
| flag: Guatemala | &#x1F1EC;&#x1F1F9; | &#x1F1EC;&#x1F1F9; | &#x1F1EC;&#x1F1F9; | 
| flag: Guam | &#x1F1EC;&#x1F1FA; | &#x1F1EC;&#x1F1FA; | &#x1F1EC;&#x1F1FA; | 
| flag: Guinea-Bissau | &#x1F1EC;&#x1F1FC; | &#x1F1EC;&#x1F1FC; | &#x1F1EC;&#x1F1FC; | 
| flag: Guyana | &#x1F1EC;&#x1F1FE; | &#x1F1EC;&#x1F1FE; | &#x1F1EC;&#x1F1FE; | 
| flag: Hong Kong SAR China | &#x1F1ED;&#x1F1F0; | &#x1F1ED;&#x1F1F0; | &#x1F1ED;&#x1F1F0; | 
| flag: Heard & McDonald Islands | &#x1F1ED;&#x1F1F2; | &#x1F1ED;&#x1F1F2; | &#x1F1ED;&#x1F1F2; | 
| flag: Honduras | &#x1F1ED;&#x1F1F3; | &#x1F1ED;&#x1F1F3; | &#x1F1ED;&#x1F1F3; | 
| flag: Croatia | &#x1F1ED;&#x1F1F7; | &#x1F1ED;&#x1F1F7; | &#x1F1ED;&#x1F1F7; | 
| flag: Haiti | &#x1F1ED;&#x1F1F9; | &#x1F1ED;&#x1F1F9; | &#x1F1ED;&#x1F1F9; | 
| flag: Hungary | &#x1F1ED;&#x1F1FA; | &#x1F1ED;&#x1F1FA; | &#x1F1ED;&#x1F1FA; | 
| flag: Canary Islands | &#x1F1EE;&#x1F1E8; | &#x1F1EE;&#x1F1E8; | &#x1F1EE;&#x1F1E8; | 
| flag: Indonesia | &#x1F1EE;&#x1F1E9; | &#x1F1EE;&#x1F1E9; | &#x1F1EE;&#x1F1E9; | 
| flag: Ireland | &#x1F1EE;&#x1F1EA; | &#x1F1EE;&#x1F1EA; | &#x1F1EE;&#x1F1EA; | 
| flag: Israel | &#x1F1EE;&#x1F1F1; | &#x1F1EE;&#x1F1F1; | &#x1F1EE;&#x1F1F1; | 
| flag: Isle of Man | &#x1F1EE;&#x1F1F2; | &#x1F1EE;&#x1F1F2; | &#x1F1EE;&#x1F1F2; | 
| flag: India | &#x1F1EE;&#x1F1F3; | &#x1F1EE;&#x1F1F3; | &#x1F1EE;&#x1F1F3; | 
| flag: British Indian Ocean Territory | &#x1F1EE;&#x1F1F4; | &#x1F1EE;&#x1F1F4; | &#x1F1EE;&#x1F1F4; | 
| flag: Iraq | &#x1F1EE;&#x1F1F6; | &#x1F1EE;&#x1F1F6; | &#x1F1EE;&#x1F1F6; | 
| flag: Iran | &#x1F1EE;&#x1F1F7; | &#x1F1EE;&#x1F1F7; | &#x1F1EE;&#x1F1F7; | 
| flag: Iceland | &#x1F1EE;&#x1F1F8; | &#x1F1EE;&#x1F1F8; | &#x1F1EE;&#x1F1F8; | 
| flag: Italy | &#x1F1EE;&#x1F1F9; | &#x1F1EE;&#x1F1F9; | &#x1F1EE;&#x1F1F9; | 
| flag: Jersey | &#x1F1EF;&#x1F1EA; | &#x1F1EF;&#x1F1EA; | &#x1F1EF;&#x1F1EA; | 
| flag: Jamaica | &#x1F1EF;&#x1F1F2; | &#x1F1EF;&#x1F1F2; | &#x1F1EF;&#x1F1F2; | 
| flag: Jordan | &#x1F1EF;&#x1F1F4; | &#x1F1EF;&#x1F1F4; | &#x1F1EF;&#x1F1F4; | 
| flag: Japan | &#x1F1EF;&#x1F1F5; | &#x1F1EF;&#x1F1F5; | &#x1F1EF;&#x1F1F5; | 
| flag: Kenya | &#x1F1F0;&#x1F1EA; | &#x1F1F0;&#x1F1EA; | &#x1F1F0;&#x1F1EA; | 
| flag: Kyrgyzstan | &#x1F1F0;&#x1F1EC; | &#x1F1F0;&#x1F1EC; | &#x1F1F0;&#x1F1EC; | 
| flag: Cambodia | &#x1F1F0;&#x1F1ED; | &#x1F1F0;&#x1F1ED; | &#x1F1F0;&#x1F1ED; | 
| flag: Kiribati | &#x1F1F0;&#x1F1EE; | &#x1F1F0;&#x1F1EE; | &#x1F1F0;&#x1F1EE; | 
| flag: Comoros | &#x1F1F0;&#x1F1F2; | &#x1F1F0;&#x1F1F2; | &#x1F1F0;&#x1F1F2; | 
| flag: St. Kitts & Nevis | &#x1F1F0;&#x1F1F3; | &#x1F1F0;&#x1F1F3; | &#x1F1F0;&#x1F1F3; | 
| flag: North Korea | &#x1F1F0;&#x1F1F5; | &#x1F1F0;&#x1F1F5; | &#x1F1F0;&#x1F1F5; | 
| flag: South Korea | &#x1F1F0;&#x1F1F7; | &#x1F1F0;&#x1F1F7; | &#x1F1F0;&#x1F1F7; | 
| flag: Kuwait | &#x1F1F0;&#x1F1FC; | &#x1F1F0;&#x1F1FC; | &#x1F1F0;&#x1F1FC; | 
| flag: Cayman Islands | &#x1F1F0;&#x1F1FE; | &#x1F1F0;&#x1F1FE; | &#x1F1F0;&#x1F1FE; | 
| flag: Kazakhstan | &#x1F1F0;&#x1F1FF; | &#x1F1F0;&#x1F1FF; | &#x1F1F0;&#x1F1FF; | 
| flag: Laos | &#x1F1F1;&#x1F1E6; | &#x1F1F1;&#x1F1E6; | &#x1F1F1;&#x1F1E6; | 
| flag: Lebanon | &#x1F1F1;&#x1F1E7; | &#x1F1F1;&#x1F1E7; | &#x1F1F1;&#x1F1E7; | 
| flag: St. Lucia | &#x1F1F1;&#x1F1E8; | &#x1F1F1;&#x1F1E8; | &#x1F1F1;&#x1F1E8; | 
| flag: Liechtenstein | &#x1F1F1;&#x1F1EE; | &#x1F1F1;&#x1F1EE; | &#x1F1F1;&#x1F1EE; | 
| flag: Sri Lanka | &#x1F1F1;&#x1F1F0; | &#x1F1F1;&#x1F1F0; | &#x1F1F1;&#x1F1F0; | 
| flag: Liberia | &#x1F1F1;&#x1F1F7; | &#x1F1F1;&#x1F1F7; | &#x1F1F1;&#x1F1F7; | 
| flag: Lesotho | &#x1F1F1;&#x1F1F8; | &#x1F1F1;&#x1F1F8; | &#x1F1F1;&#x1F1F8; | 
| flag: Lithuania | &#x1F1F1;&#x1F1F9; | &#x1F1F1;&#x1F1F9; | &#x1F1F1;&#x1F1F9; | 
| flag: Luxembourg | &#x1F1F1;&#x1F1FA; | &#x1F1F1;&#x1F1FA; | &#x1F1F1;&#x1F1FA; | 
| flag: Latvia | &#x1F1F1;&#x1F1FB; | &#x1F1F1;&#x1F1FB; | &#x1F1F1;&#x1F1FB; | 
| flag: Libya | &#x1F1F1;&#x1F1FE; | &#x1F1F1;&#x1F1FE; | &#x1F1F1;&#x1F1FE; | 
| flag: Morocco | &#x1F1F2;&#x1F1E6; | &#x1F1F2;&#x1F1E6; | &#x1F1F2;&#x1F1E6; | 
| flag: Monaco | &#x1F1F2;&#x1F1E8; | &#x1F1F2;&#x1F1E8; | &#x1F1F2;&#x1F1E8; | 
| flag: Moldova | &#x1F1F2;&#x1F1E9; | &#x1F1F2;&#x1F1E9; | &#x1F1F2;&#x1F1E9; | 
| flag: Montenegro | &#x1F1F2;&#x1F1EA; | &#x1F1F2;&#x1F1EA; | &#x1F1F2;&#x1F1EA; | 
| flag: St. Martin | &#x1F1F2;&#x1F1EB; | &#x1F1F2;&#x1F1EB; | &#x1F1F2;&#x1F1EB; | 
| flag: Madagascar | &#x1F1F2;&#x1F1EC; | &#x1F1F2;&#x1F1EC; | &#x1F1F2;&#x1F1EC; | 
| flag: Marshall Islands | &#x1F1F2;&#x1F1ED; | &#x1F1F2;&#x1F1ED; | &#x1F1F2;&#x1F1ED; | 
| flag: North Macedonia | &#x1F1F2;&#x1F1F0; | &#x1F1F2;&#x1F1F0; | &#x1F1F2;&#x1F1F0; | 
| flag: Mali | &#x1F1F2;&#x1F1F1; | &#x1F1F2;&#x1F1F1; | &#x1F1F2;&#x1F1F1; | 
| flag: Myanmar (Burma) | &#x1F1F2;&#x1F1F2; | &#x1F1F2;&#x1F1F2; | &#x1F1F2;&#x1F1F2; | 
| flag: Mongolia | &#x1F1F2;&#x1F1F3; | &#x1F1F2;&#x1F1F3; | &#x1F1F2;&#x1F1F3; | 
| flag: Macao SAR China | &#x1F1F2;&#x1F1F4; | &#x1F1F2;&#x1F1F4; | &#x1F1F2;&#x1F1F4; | 
| flag: Northern Mariana Islands | &#x1F1F2;&#x1F1F5; | &#x1F1F2;&#x1F1F5; | &#x1F1F2;&#x1F1F5; | 
| flag: Martinique | &#x1F1F2;&#x1F1F6; | &#x1F1F2;&#x1F1F6; | &#x1F1F2;&#x1F1F6; | 
| flag: Mauritania | &#x1F1F2;&#x1F1F7; | &#x1F1F2;&#x1F1F7; | &#x1F1F2;&#x1F1F7; | 
| flag: Montserrat | &#x1F1F2;&#x1F1F8; | &#x1F1F2;&#x1F1F8; | &#x1F1F2;&#x1F1F8; | 
| flag: Malta | &#x1F1F2;&#x1F1F9; | &#x1F1F2;&#x1F1F9; | &#x1F1F2;&#x1F1F9; | 
| flag: Mauritius | &#x1F1F2;&#x1F1FA; | &#x1F1F2;&#x1F1FA; | &#x1F1F2;&#x1F1FA; | 
| flag: Maldives | &#x1F1F2;&#x1F1FB; | &#x1F1F2;&#x1F1FB; | &#x1F1F2;&#x1F1FB; | 
| flag: Malawi | &#x1F1F2;&#x1F1FC; | &#x1F1F2;&#x1F1FC; | &#x1F1F2;&#x1F1FC; | 
| flag: Mexico | &#x1F1F2;&#x1F1FD; | &#x1F1F2;&#x1F1FD; | &#x1F1F2;&#x1F1FD; | 
| flag: Malaysia | &#x1F1F2;&#x1F1FE; | &#x1F1F2;&#x1F1FE; | &#x1F1F2;&#x1F1FE; | 
| flag: Mozambique | &#x1F1F2;&#x1F1FF; | &#x1F1F2;&#x1F1FF; | &#x1F1F2;&#x1F1FF; | 
| flag: Namibia | &#x1F1F3;&#x1F1E6; | &#x1F1F3;&#x1F1E6; | &#x1F1F3;&#x1F1E6; | 
| flag: New Caledonia | &#x1F1F3;&#x1F1E8; | &#x1F1F3;&#x1F1E8; | &#x1F1F3;&#x1F1E8; | 
| flag: Niger | &#x1F1F3;&#x1F1EA; | &#x1F1F3;&#x1F1EA; | &#x1F1F3;&#x1F1EA; | 
| flag: Norfolk Island | &#x1F1F3;&#x1F1EB; | &#x1F1F3;&#x1F1EB; | &#x1F1F3;&#x1F1EB; | 
| flag: Nigeria | &#x1F1F3;&#x1F1EC; | &#x1F1F3;&#x1F1EC; | &#x1F1F3;&#x1F1EC; | 
| flag: Nicaragua | &#x1F1F3;&#x1F1EE; | &#x1F1F3;&#x1F1EE; | &#x1F1F3;&#x1F1EE; | 
| flag: Netherlands | &#x1F1F3;&#x1F1F1; | &#x1F1F3;&#x1F1F1; | &#x1F1F3;&#x1F1F1; | 
| flag: Norway | &#x1F1F3;&#x1F1F4; | &#x1F1F3;&#x1F1F4; | &#x1F1F3;&#x1F1F4; | 
| flag: Nepal | &#x1F1F3;&#x1F1F5; | &#x1F1F3;&#x1F1F5; | &#x1F1F3;&#x1F1F5; | 
| flag: Nauru | &#x1F1F3;&#x1F1F7; | &#x1F1F3;&#x1F1F7; | &#x1F1F3;&#x1F1F7; | 
| flag: Niue | &#x1F1F3;&#x1F1FA; | &#x1F1F3;&#x1F1FA; | &#x1F1F3;&#x1F1FA; | 
| flag: New Zealand | &#x1F1F3;&#x1F1FF; | &#x1F1F3;&#x1F1FF; | &#x1F1F3;&#x1F1FF; | 
| flag: Oman | &#x1F1F4;&#x1F1F2; | &#x1F1F4;&#x1F1F2; | &#x1F1F4;&#x1F1F2; | 
| flag: Panama | &#x1F1F5;&#x1F1E6; | &#x1F1F5;&#x1F1E6; | &#x1F1F5;&#x1F1E6; | 
| flag: Peru | &#x1F1F5;&#x1F1EA; | &#x1F1F5;&#x1F1EA; | &#x1F1F5;&#x1F1EA; | 
| flag: French Polynesia | &#x1F1F5;&#x1F1EB; | &#x1F1F5;&#x1F1EB; | &#x1F1F5;&#x1F1EB; | 
| flag: Papua New Guinea | &#x1F1F5;&#x1F1EC; | &#x1F1F5;&#x1F1EC; | &#x1F1F5;&#x1F1EC; | 
| flag: Philippines | &#x1F1F5;&#x1F1ED; | &#x1F1F5;&#x1F1ED; | &#x1F1F5;&#x1F1ED; | 
| flag: Pakistan | &#x1F1F5;&#x1F1F0; | &#x1F1F5;&#x1F1F0; | &#x1F1F5;&#x1F1F0; | 
| flag: Poland | &#x1F1F5;&#x1F1F1; | &#x1F1F5;&#x1F1F1; | &#x1F1F5;&#x1F1F1; | 
| flag: St. Pierre & Miquelon | &#x1F1F5;&#x1F1F2; | &#x1F1F5;&#x1F1F2; | &#x1F1F5;&#x1F1F2; | 
| flag: Pitcairn Islands | &#x1F1F5;&#x1F1F3; | &#x1F1F5;&#x1F1F3; | &#x1F1F5;&#x1F1F3; | 
| flag: Puerto Rico | &#x1F1F5;&#x1F1F7; | &#x1F1F5;&#x1F1F7; | &#x1F1F5;&#x1F1F7; | 
| flag: Palestinian Territories | &#x1F1F5;&#x1F1F8; | &#x1F1F5;&#x1F1F8; | &#x1F1F5;&#x1F1F8; | 
| flag: Portugal | &#x1F1F5;&#x1F1F9; | &#x1F1F5;&#x1F1F9; | &#x1F1F5;&#x1F1F9; | 
| flag: Palau | &#x1F1F5;&#x1F1FC; | &#x1F1F5;&#x1F1FC; | &#x1F1F5;&#x1F1FC; | 
| flag: Paraguay | &#x1F1F5;&#x1F1FE; | &#x1F1F5;&#x1F1FE; | &#x1F1F5;&#x1F1FE; | 
| flag: Qatar | &#x1F1F6;&#x1F1E6; | &#x1F1F6;&#x1F1E6; | &#x1F1F6;&#x1F1E6; | 
| flag: Réunion | &#x1F1F7;&#x1F1EA; | &#x1F1F7;&#x1F1EA; | &#x1F1F7;&#x1F1EA; | 
| flag: Romania | &#x1F1F7;&#x1F1F4; | &#x1F1F7;&#x1F1F4; | &#x1F1F7;&#x1F1F4; | 
| flag: Serbia | &#x1F1F7;&#x1F1F8; | &#x1F1F7;&#x1F1F8; | &#x1F1F7;&#x1F1F8; | 
| flag: Russia | &#x1F1F7;&#x1F1FA; | &#x1F1F7;&#x1F1FA; | &#x1F1F7;&#x1F1FA; | 
| flag: Rwanda | &#x1F1F7;&#x1F1FC; | &#x1F1F7;&#x1F1FC; | &#x1F1F7;&#x1F1FC; | 
| flag: Saudi Arabia | &#x1F1F8;&#x1F1E6; | &#x1F1F8;&#x1F1E6; | &#x1F1F8;&#x1F1E6; | 
| flag: Solomon Islands | &#x1F1F8;&#x1F1E7; | &#x1F1F8;&#x1F1E7; | &#x1F1F8;&#x1F1E7; | 
| flag: Seychelles | &#x1F1F8;&#x1F1E8; | &#x1F1F8;&#x1F1E8; | &#x1F1F8;&#x1F1E8; | 
| flag: Sudan | &#x1F1F8;&#x1F1E9; | &#x1F1F8;&#x1F1E9; | &#x1F1F8;&#x1F1E9; | 
| flag: Sweden | &#x1F1F8;&#x1F1EA; | &#x1F1F8;&#x1F1EA; | &#x1F1F8;&#x1F1EA; | 
| flag: Singapore | &#x1F1F8;&#x1F1EC; | &#x1F1F8;&#x1F1EC; | &#x1F1F8;&#x1F1EC; | 
| flag: St. Helena | &#x1F1F8;&#x1F1ED; | &#x1F1F8;&#x1F1ED; | &#x1F1F8;&#x1F1ED; | 
| flag: Slovenia | &#x1F1F8;&#x1F1EE; | &#x1F1F8;&#x1F1EE; | &#x1F1F8;&#x1F1EE; | 
| flag: Svalbard & Jan Mayen | &#x1F1F8;&#x1F1EF; | &#x1F1F8;&#x1F1EF; | &#x1F1F8;&#x1F1EF; | 
| flag: Slovakia | &#x1F1F8;&#x1F1F0; | &#x1F1F8;&#x1F1F0; | &#x1F1F8;&#x1F1F0; | 
| flag: Sierra Leone | &#x1F1F8;&#x1F1F1; | &#x1F1F8;&#x1F1F1; | &#x1F1F8;&#x1F1F1; | 
| flag: San Marino | &#x1F1F8;&#x1F1F2; | &#x1F1F8;&#x1F1F2; | &#x1F1F8;&#x1F1F2; | 
| flag: Senegal | &#x1F1F8;&#x1F1F3; | &#x1F1F8;&#x1F1F3; | &#x1F1F8;&#x1F1F3; | 
| flag: Somalia | &#x1F1F8;&#x1F1F4; | &#x1F1F8;&#x1F1F4; | &#x1F1F8;&#x1F1F4; | 
| flag: Suriname | &#x1F1F8;&#x1F1F7; | &#x1F1F8;&#x1F1F7; | &#x1F1F8;&#x1F1F7; | 
| flag: South Sudan | &#x1F1F8;&#x1F1F8; | &#x1F1F8;&#x1F1F8; | &#x1F1F8;&#x1F1F8; | 
| flag: São Tomé & Príncipe | &#x1F1F8;&#x1F1F9; | &#x1F1F8;&#x1F1F9; | &#x1F1F8;&#x1F1F9; | 
| flag: El Salvador | &#x1F1F8;&#x1F1FB; | &#x1F1F8;&#x1F1FB; | &#x1F1F8;&#x1F1FB; | 
| flag: Sint Maarten | &#x1F1F8;&#x1F1FD; | &#x1F1F8;&#x1F1FD; | &#x1F1F8;&#x1F1FD; | 
| flag: Syria | &#x1F1F8;&#x1F1FE; | &#x1F1F8;&#x1F1FE; | &#x1F1F8;&#x1F1FE; | 
| flag: Eswatini | &#x1F1F8;&#x1F1FF; | &#x1F1F8;&#x1F1FF; | &#x1F1F8;&#x1F1FF; | 
| flag: Tristan da Cunha | &#x1F1F9;&#x1F1E6; | &#x1F1F9;&#x1F1E6; | &#x1F1F9;&#x1F1E6; | 
| flag: Turks & Caicos Islands | &#x1F1F9;&#x1F1E8; | &#x1F1F9;&#x1F1E8; | &#x1F1F9;&#x1F1E8; | 
| flag: Chad | &#x1F1F9;&#x1F1E9; | &#x1F1F9;&#x1F1E9; | &#x1F1F9;&#x1F1E9; | 
| flag: French Southern Territories | &#x1F1F9;&#x1F1EB; | &#x1F1F9;&#x1F1EB; | &#x1F1F9;&#x1F1EB; | 
| flag: Togo | &#x1F1F9;&#x1F1EC; | &#x1F1F9;&#x1F1EC; | &#x1F1F9;&#x1F1EC; | 
| flag: Thailand | &#x1F1F9;&#x1F1ED; | &#x1F1F9;&#x1F1ED; | &#x1F1F9;&#x1F1ED; | 
| flag: Tajikistan | &#x1F1F9;&#x1F1EF; | &#x1F1F9;&#x1F1EF; | &#x1F1F9;&#x1F1EF; | 
| flag: Tokelau | &#x1F1F9;&#x1F1F0; | &#x1F1F9;&#x1F1F0; | &#x1F1F9;&#x1F1F0; | 
| flag: Timor-Leste | &#x1F1F9;&#x1F1F1; | &#x1F1F9;&#x1F1F1; | &#x1F1F9;&#x1F1F1; | 
| flag: Turkmenistan | &#x1F1F9;&#x1F1F2; | &#x1F1F9;&#x1F1F2; | &#x1F1F9;&#x1F1F2; | 
| flag: Tunisia | &#x1F1F9;&#x1F1F3; | &#x1F1F9;&#x1F1F3; | &#x1F1F9;&#x1F1F3; | 
| flag: Tonga | &#x1F1F9;&#x1F1F4; | &#x1F1F9;&#x1F1F4; | &#x1F1F9;&#x1F1F4; | 
| flag: Turkey | &#x1F1F9;&#x1F1F7; | &#x1F1F9;&#x1F1F7; | &#x1F1F9;&#x1F1F7; | 
| flag: Trinidad & Tobago | &#x1F1F9;&#x1F1F9; | &#x1F1F9;&#x1F1F9; | &#x1F1F9;&#x1F1F9; | 
| flag: Tuvalu | &#x1F1F9;&#x1F1FB; | &#x1F1F9;&#x1F1FB; | &#x1F1F9;&#x1F1FB; | 
| flag: Taiwan | &#x1F1F9;&#x1F1FC; | &#x1F1F9;&#x1F1FC; | &#x1F1F9;&#x1F1FC; | 
| flag: Tanzania | &#x1F1F9;&#x1F1FF; | &#x1F1F9;&#x1F1FF; | &#x1F1F9;&#x1F1FF; | 
| flag: Ukraine | &#x1F1FA;&#x1F1E6; | &#x1F1FA;&#x1F1E6; | &#x1F1FA;&#x1F1E6; | 
| flag: Uganda | &#x1F1FA;&#x1F1EC; | &#x1F1FA;&#x1F1EC; | &#x1F1FA;&#x1F1EC; | 
| flag: U.S. Outlying Islands | &#x1F1FA;&#x1F1F2; | &#x1F1FA;&#x1F1F2; | &#x1F1FA;&#x1F1F2; | 
| flag: United Nations |  | &#x1F1FA;&#x1F1F3; | &#x1F1FA;&#x1F1F3; | 
| flag: United States | &#x1F1FA;&#x1F1F8; | &#x1F1FA;&#x1F1F8; | &#x1F1FA;&#x1F1F8; | 
| flag: Uruguay | &#x1F1FA;&#x1F1FE; | &#x1F1FA;&#x1F1FE; | &#x1F1FA;&#x1F1FE; | 
| flag: Uzbekistan | &#x1F1FA;&#x1F1FF; | &#x1F1FA;&#x1F1FF; | &#x1F1FA;&#x1F1FF; | 
| flag: Vatican City | &#x1F1FB;&#x1F1E6; | &#x1F1FB;&#x1F1E6; | &#x1F1FB;&#x1F1E6; | 
| flag: St. Vincent & Grenadines | &#x1F1FB;&#x1F1E8; | &#x1F1FB;&#x1F1E8; | &#x1F1FB;&#x1F1E8; | 
| flag: Venezuela | &#x1F1FB;&#x1F1EA; | &#x1F1FB;&#x1F1EA; | &#x1F1FB;&#x1F1EA; | 
| flag: British Virgin Islands | &#x1F1FB;&#x1F1EC; | &#x1F1FB;&#x1F1EC; | &#x1F1FB;&#x1F1EC; | 
| flag: U.S. Virgin Islands | &#x1F1FB;&#x1F1EE; | &#x1F1FB;&#x1F1EE; | &#x1F1FB;&#x1F1EE; | 
| flag: Vietnam | &#x1F1FB;&#x1F1F3; | &#x1F1FB;&#x1F1F3; | &#x1F1FB;&#x1F1F3; | 
| flag: Vanuatu | &#x1F1FB;&#x1F1FA; | &#x1F1FB;&#x1F1FA; | &#x1F1FB;&#x1F1FA; | 
| flag: Wallis & Futuna | &#x1F1FC;&#x1F1EB; | &#x1F1FC;&#x1F1EB; | &#x1F1FC;&#x1F1EB; | 
| flag: Samoa | &#x1F1FC;&#x1F1F8; | &#x1F1FC;&#x1F1F8; | &#x1F1FC;&#x1F1F8; | 
| flag: Kosovo | &#x1F1FD;&#x1F1F0; | &#x1F1FD;&#x1F1F0; | &#x1F1FD;&#x1F1F0; | 
| flag: Yemen | &#x1F1FE;&#x1F1EA; | &#x1F1FE;&#x1F1EA; | &#x1F1FE;&#x1F1EA; | 
| flag: Mayotte | &#x1F1FE;&#x1F1F9; | &#x1F1FE;&#x1F1F9; | &#x1F1FE;&#x1F1F9; | 
| flag: South Africa | &#x1F1FF;&#x1F1E6; | &#x1F1FF;&#x1F1E6; | &#x1F1FF;&#x1F1E6; | 
| flag: Zambia | &#x1F1FF;&#x1F1F2; | &#x1F1FF;&#x1F1F2; | &#x1F1FF;&#x1F1F2; | 
| flag: Zimbabwe | &#x1F1FF;&#x1F1FC; | &#x1F1FF;&#x1F1FC; | &#x1F1FF;&#x1F1FC; | 

### subdivision-flag

| name | EmojiOne | Twemoji | OpenMoji |
|:-:|:-:|:-:|:-:|
| flag: England |  | &#x1F3F4;&#xE0067;&#xE0062;&#xE0065;&#xE006E;&#xE0067;&#xE007F; | &#x1F3F4;&#xE0067;&#xE0062;&#xE0065;&#xE006E;&#xE0067;&#xE007F; | 
| flag: Scotland |  | &#x1F3F4;&#xE0067;&#xE0062;&#xE0073;&#xE0063;&#xE0074;&#xE007F; | &#x1F3F4;&#xE0067;&#xE0062;&#xE0073;&#xE0063;&#xE0074;&#xE007F; | 
| flag: Wales |  | &#x1F3F4;&#xE0067;&#xE0062;&#xE0077;&#xE006C;&#xE0073;&#xE007F; | &#x1F3F4;&#xE0067;&#xE0062;&#xE0077;&#xE006C;&#xE0073;&#xE007F; | 
