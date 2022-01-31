---
title: Open-source Emojis
grand_parent: Language
parent: Unicode Characters
---

# Comparison Table for Open-Source Emoji Fonts


<!--
For this page to display properly, you'll need to install the following font files:
- [Twitter Color Emoji SVGinOT Font](https://github.com/eosrei/twemoji-color-font/releases)
- [Google's Noto Color Emoji Font](https://github.com/googlefonts/noto-emoji/tree/main/fonts) (this one might only work on Windows 10)
- [A version of the OpenMoji font from here.](https://github.com/mavit/openmoji/tree/nanoemoji/font)
- [Blobmoji?](https://github.com/C1710/blobmoji)
- EmojiOne font?

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

TwemojiMozilla.ttf   🌟🌟🌟
 - works great on all the browsers on windows. renders in color, even in chrome
 - Also working on android
 - great work mozilla team!
 - doesn't work on mac os chrome or mac os Firefox. works fine on mac os safari. 

OpenMoji-Color.COLRv0.ttf  🌟🌟🌟🌟
- Works everywhere I've tried it. Windows, Mac, android, ios
- Wowzers, I wish I could have figured out how to get nanoemoji working.

NotoSVGmiconv.woff2
- Doesn't work at all, sadly.

Blobmoji.ttf
- Only working in chromium browsers...
- Also, I think it's sometimes misaligned?

Catrinity.woff2
- Color was borked by conversion. What tool did Adobe use to get a functional color woff2?!

NotoEmoji.otf (SVG)
- monochrome. Works everywhere though.


NotoColorEmoji-SVG.otf


Catrinity.otf


-->

## Tables of Emojis

<style>
td {
    vertical-align: middle;
}
@font-face {
  font-family: 'Adobe EmojiOne';
  src: url(https://www.rmwinslow.com/posts/language/fonts/emojione/EmojiOneColorAdobe.woff2);
}
td:nth-child(2) {
  font-family: 'Adobe EmojiOne';
  font-size: 48px;
  padding: 0px;
}
@font-face {
  font-family: 'Twemoji';
  src: url(https://www.rmwinslow.com/posts/language/fonts/twitter/TwemojiMozilla.ttf);
}
td:nth-child(3) {
  font-family: 'Twemoji';
  font-size: 48px;
  padding: 0px;
}
@font-face {
  font-family: 'OpenMoji';
  src: url(https://www.rmwinslow.com/posts/language/fonts/openmoji/OpenMoji-Color.COLRv0.ttf);
}
td:nth-child(4) {
  font-family: 'OpenMoji';
  font-size: 48px;
  padding: 0px;
}
@font-face {
  font-family: 'Noto SVG';
  src: url(https://www.rmwinslow.com/posts/language/fonts/notosvg/NotoColorEmoji-SVG.otf);
}
td:nth-child(5) {
  font-family: 'Noto SVG';
  font-size: 48px;
  padding: 0px;
}
@font-face {
  font-family: 'Noto Blob';
  src: url(https://www.rmwinslow.com/posts/language/fonts/notoblob/Blobmoji.ttf);
}
td:nth-child(6) {
  font-family: 'Noto Blob';
  font-size: 48px;
  padding: 0px;
}
@font-face {
  font-family: 'catrinitytest';
  src: url(https://www.rmwinslow.com/posts/language/fonts/catrinity/Catrinity.otf);
}
.catcard {
  font-family: 'catrinitytest';
  font-size: 64px;
}
</style>



<div class='catcard' style>
🃠 🃡 🃢 🃣 
🃤 🃥 🃦 🃧 
🃨 🃩 🃪 🃫 
🃬 🃭 🃮 🃯 
🃰 🃱 🃲 🃳 
🃴 🃵
</div>
















## Animals & Nature


### animal-mammal

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| monkey face | &#x1F435; | &#x1F435; | &#x1F435; | &#x1F435; | &#x1F435; | 
| monkey | &#x1F412; | &#x1F412; | &#x1F412; | &#x1F412; | &#x1F412; | 
| gorilla | &#x1F98D; | &#x1F98D; | &#x1F98D; | &#x1F98D; | &#x1F98D; | 
| orangutan |  | &#x1F9A7; | &#x1F9A7; | &#x1F9A7; | &#x1F9A7; | 
| dog face | &#x1F436; | &#x1F436; | &#x1F436; | &#x1F436; | &#x1F436; | 
| dog | &#x1F415; | &#x1F415; | &#x1F415; | &#x1F415; | &#x1F415; | 
| guide dog |  | &#x1F9AE; | &#x1F9AE; | &#x1F9AE; | &#x1F9AE; | 
| service dog |  | &#x1F415;&#x200D;&#x1F9BA; | &#x1F415;&#x200D;&#x1F9BA; | &#x1F415;&#x200D;&#x1F9BA; | &#x1F415;&#x200D;&#x1F9BA; | 
| poodle | &#x1F429; | &#x1F429; | &#x1F429; | &#x1F429; | &#x1F429; | 
| wolf | &#x1F43A; | &#x1F43A; | &#x1F43A; | &#x1F43A; | &#x1F43A; | 
| fox | &#x1F98A; | &#x1F98A; | &#x1F98A; | &#x1F98A; | &#x1F98A; | 
| raccoon |  | &#x1F99D; | &#x1F99D; | &#x1F99D; | &#x1F99D; | 
| cat face | &#x1F431; | &#x1F431; | &#x1F431; | &#x1F431; | &#x1F431; | 
| cat | &#x1F408; | &#x1F408; | &#x1F408; | &#x1F408; | &#x1F408; | 
| black cat |  | &#x1F408;&#x200D;&#x2B1B; | &#x1F408;&#x200D;&#x2B1B; | &#x1F408;&#x200D;&#x2B1B; | &#x1F408;&#x200D;&#x2B1B; | 
| lion | &#x1F981; | &#x1F981; | &#x1F981; | &#x1F981; | &#x1F981; | 
| tiger face | &#x1F42F; | &#x1F42F; | &#x1F42F; | &#x1F42F; | &#x1F42F; | 
| tiger | &#x1F405; | &#x1F405; | &#x1F405; | &#x1F405; | &#x1F405; | 
| leopard | &#x1F406; | &#x1F406; | &#x1F406; | &#x1F406; | &#x1F406; | 
| horse face | &#x1F434; | &#x1F434; | &#x1F434; | &#x1F434; | &#x1F434; | 
| horse | &#x1F40E; | &#x1F40E; | &#x1F40E; | &#x1F40E; | &#x1F40E; | 
| unicorn | &#x1F984; | &#x1F984; | &#x1F984; | &#x1F984; | &#x1F984; | 
| zebra |  | &#x1F993; | &#x1F993; | &#x1F993; | &#x1F993; | 
| deer | &#x1F98C; | &#x1F98C; | &#x1F98C; | &#x1F98C; | &#x1F98C; | 
| bison |  | &#x1F9AC; | &#x1F9AC; | &#x1F9AC; | &#x1F9AC; | 
| cow face | &#x1F42E; | &#x1F42E; | &#x1F42E; | &#x1F42E; | &#x1F42E; | 
| ox | &#x1F402; | &#x1F402; | &#x1F402; | &#x1F402; | &#x1F402; | 
| water buffalo | &#x1F403; | &#x1F403; | &#x1F403; | &#x1F403; | &#x1F403; | 
| cow | &#x1F404; | &#x1F404; | &#x1F404; | &#x1F404; | &#x1F404; | 
| pig face | &#x1F437; | &#x1F437; | &#x1F437; | &#x1F437; | &#x1F437; | 
| pig | &#x1F416; | &#x1F416; | &#x1F416; | &#x1F416; | &#x1F416; | 
| boar | &#x1F417; | &#x1F417; | &#x1F417; | &#x1F417; | &#x1F417; | 
| pig nose | &#x1F43D; | &#x1F43D; | &#x1F43D; | &#x1F43D; | &#x1F43D; | 
| ram | &#x1F40F; | &#x1F40F; | &#x1F40F; | &#x1F40F; | &#x1F40F; | 
| ewe | &#x1F411; | &#x1F411; | &#x1F411; | &#x1F411; | &#x1F411; | 
| goat | &#x1F410; | &#x1F410; | &#x1F410; | &#x1F410; | &#x1F410; | 
| camel | &#x1F42A; | &#x1F42A; | &#x1F42A; | &#x1F42A; | &#x1F42A; | 
| two-hump camel | &#x1F42B; | &#x1F42B; | &#x1F42B; | &#x1F42B; | &#x1F42B; | 
| llama |  | &#x1F999; | &#x1F999; | &#x1F999; | &#x1F999; | 
| giraffe |  | &#x1F992; | &#x1F992; | &#x1F992; | &#x1F992; | 
| elephant | &#x1F418; | &#x1F418; | &#x1F418; | &#x1F418; | &#x1F418; | 
| mammoth |  | &#x1F9A3; | &#x1F9A3; | &#x1F9A3; | &#x1F9A3; | 
| rhinoceros | &#x1F98F; | &#x1F98F; | &#x1F98F; | &#x1F98F; | &#x1F98F; | 
| hippopotamus |  | &#x1F99B; | &#x1F99B; | &#x1F99B; | &#x1F99B; | 
| mouse face | &#x1F42D; | &#x1F42D; | &#x1F42D; | &#x1F42D; | &#x1F42D; | 
| mouse | &#x1F401; | &#x1F401; | &#x1F401; | &#x1F401; | &#x1F401; | 
| rat | &#x1F400; | &#x1F400; | &#x1F400; | &#x1F400; | &#x1F400; | 
| hamster | &#x1F439; | &#x1F439; | &#x1F439; | &#x1F439; | &#x1F439; | 
| rabbit face | &#x1F430; | &#x1F430; | &#x1F430; | &#x1F430; | &#x1F430; | 
| rabbit | &#x1F407; | &#x1F407; | &#x1F407; | &#x1F407; | &#x1F407; | 
| chipmunk | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | &#x1F43F;&#xFE0F; | 
| beaver |  | &#x1F9AB; | &#x1F9AB; | &#x1F9AB; | &#x1F9AB; | 
| hedgehog |  | &#x1F994; | &#x1F994; | &#x1F994; | &#x1F994; | 
| bat | &#x1F987; | &#x1F987; | &#x1F987; | &#x1F987; | &#x1F987; | 
| bear | &#x1F43B; | &#x1F43B; | &#x1F43B; | &#x1F43B; | &#x1F43B; | 
| polar bear |  | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | &#x1F43B;&#x200D;&#x2744;&#xFE0F; | 
| koala | &#x1F428; | &#x1F428; | &#x1F428; | &#x1F428; | &#x1F428; | 
| panda | &#x1F43C; | &#x1F43C; | &#x1F43C; | &#x1F43C; | &#x1F43C; | 
| sloth |  | &#x1F9A5; | &#x1F9A5; | &#x1F9A5; | &#x1F9A5; | 
| otter |  | &#x1F9A6; | &#x1F9A6; | &#x1F9A6; | &#x1F9A6; | 
| skunk |  | &#x1F9A8; | &#x1F9A8; | &#x1F9A8; | &#x1F9A8; | 
| kangaroo |  | &#x1F998; | &#x1F998; | &#x1F998; | &#x1F998; | 
| badger |  | &#x1F9A1; | &#x1F9A1; | &#x1F9A1; | &#x1F9A1; | 
| paw prints | &#x1F43E; | &#x1F43E; | &#x1F43E; | &#x1F43E; | &#x1F43E; | 

### animal-bird

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| turkey | &#x1F983; | &#x1F983; | &#x1F983; | &#x1F983; | &#x1F983; | 
| chicken | &#x1F414; | &#x1F414; | &#x1F414; | &#x1F414; | &#x1F414; | 
| rooster | &#x1F413; | &#x1F413; | &#x1F413; | &#x1F413; | &#x1F413; | 
| hatching chick | &#x1F423; | &#x1F423; | &#x1F423; | &#x1F423; | &#x1F423; | 
| baby chick | &#x1F424; | &#x1F424; | &#x1F424; | &#x1F424; | &#x1F424; | 
| front-facing baby chick | &#x1F425; | &#x1F425; | &#x1F425; | &#x1F425; | &#x1F425; | 
| bird | &#x1F426; | &#x1F426; | &#x1F426; | &#x1F426; | &#x1F426; | 
| penguin | &#x1F427; | &#x1F427; | &#x1F427; | &#x1F427; | &#x1F427; | 
| dove | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | &#x1F54A;&#xFE0F; | 
| eagle | &#x1F985; | &#x1F985; | &#x1F985; | &#x1F985; | &#x1F985; | 
| duck | &#x1F986; | &#x1F986; | &#x1F986; | &#x1F986; | &#x1F986; | 
| swan |  | &#x1F9A2; | &#x1F9A2; | &#x1F9A2; | &#x1F9A2; | 
| owl | &#x1F989; | &#x1F989; | &#x1F989; | &#x1F989; | &#x1F989; | 
| dodo |  | &#x1F9A4; | &#x1F9A4; | &#x1F9A4; | &#x1F9A4; | 
| feather |  | &#x1FAB6; | &#x1FAB6; | &#x1FAB6; | &#x1FAB6; | 
| flamingo |  | &#x1F9A9; | &#x1F9A9; | &#x1F9A9; | &#x1F9A9; | 
| peacock |  | &#x1F99A; | &#x1F99A; | &#x1F99A; | &#x1F99A; | 
| parrot |  | &#x1F99C; | &#x1F99C; | &#x1F99C; | &#x1F99C; | 

### animal-amphibian

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| frog | &#x1F438; | &#x1F438; | &#x1F438; | &#x1F438; | &#x1F438; | 

### animal-reptile

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| crocodile | &#x1F40A; | &#x1F40A; | &#x1F40A; | &#x1F40A; | &#x1F40A; | 
| turtle | &#x1F422; | &#x1F422; | &#x1F422; | &#x1F422; | &#x1F422; | 
| lizard | &#x1F98E; | &#x1F98E; | &#x1F98E; | &#x1F98E; | &#x1F98E; | 
| snake | &#x1F40D; | &#x1F40D; | &#x1F40D; | &#x1F40D; | &#x1F40D; | 
| dragon face | &#x1F432; | &#x1F432; | &#x1F432; | &#x1F432; | &#x1F432; | 
| dragon | &#x1F409; | &#x1F409; | &#x1F409; | &#x1F409; | &#x1F409; | 
| sauropod |  | &#x1F995; | &#x1F995; | &#x1F995; | &#x1F995; | 
| T-Rex |  | &#x1F996; | &#x1F996; | &#x1F996; | &#x1F996; | 

### animal-marine

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| spouting whale | &#x1F433; | &#x1F433; | &#x1F433; | &#x1F433; | &#x1F433; | 
| whale | &#x1F40B; | &#x1F40B; | &#x1F40B; | &#x1F40B; | &#x1F40B; | 
| dolphin | &#x1F42C; | &#x1F42C; | &#x1F42C; | &#x1F42C; | &#x1F42C; | 
| seal |  | &#x1F9AD; | &#x1F9AD; | &#x1F9AD; | &#x1F9AD; | 
| fish | &#x1F41F; | &#x1F41F; | &#x1F41F; | &#x1F41F; | &#x1F41F; | 
| tropical fish | &#x1F420; | &#x1F420; | &#x1F420; | &#x1F420; | &#x1F420; | 
| blowfish | &#x1F421; | &#x1F421; | &#x1F421; | &#x1F421; | &#x1F421; | 
| shark | &#x1F988; | &#x1F988; | &#x1F988; | &#x1F988; | &#x1F988; | 
| octopus | &#x1F419; | &#x1F419; | &#x1F419; | &#x1F419; | &#x1F419; | 
| spiral shell | &#x1F41A; | &#x1F41A; | &#x1F41A; | &#x1F41A; | &#x1F41A; | 

### animal-bug

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| snail | &#x1F40C; | &#x1F40C; | &#x1F40C; | &#x1F40C; | &#x1F40C; | 
| butterfly | &#x1F98B; | &#x1F98B; | &#x1F98B; | &#x1F98B; | &#x1F98B; | 
| bug | &#x1F41B; | &#x1F41B; | &#x1F41B; | &#x1F41B; | &#x1F41B; | 
| ant | &#x1F41C; | &#x1F41C; | &#x1F41C; | &#x1F41C; | &#x1F41C; | 
| honeybee | &#x1F41D; | &#x1F41D; | &#x1F41D; | &#x1F41D; | &#x1F41D; | 
| beetle |  | &#x1FAB2; | &#x1FAB2; | &#x1FAB2; | &#x1FAB2; | 
| lady beetle | &#x1F41E; | &#x1F41E; | &#x1F41E; | &#x1F41E; | &#x1F41E; | 
| cricket |  | &#x1F997; | &#x1F997; | &#x1F997; | &#x1F997; | 
| cockroach |  | &#x1FAB3; | &#x1FAB3; | &#x1FAB3; | &#x1FAB3; | 
| spider | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | &#x1F577;&#xFE0F; | 
| spider web | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | &#x1F578;&#xFE0F; | 
| scorpion | &#x1F982; | &#x1F982; | &#x1F982; | &#x1F982; | &#x1F982; | 
| mosquito |  | &#x1F99F; | &#x1F99F; | &#x1F99F; | &#x1F99F; | 
| fly |  | &#x1FAB0; | &#x1FAB0; | &#x1FAB0; | &#x1FAB0; | 
| worm |  | &#x1FAB1; | &#x1FAB1; | &#x1FAB1; | &#x1FAB1; | 
| microbe |  | &#x1F9A0; | &#x1F9A0; | &#x1F9A0; | &#x1F9A0; | 

### plant-flower

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| bouquet | &#x1F490; | &#x1F490; | &#x1F490; | &#x1F490; | &#x1F490; | 
| cherry blossom | &#x1F338; | &#x1F338; | &#x1F338; | &#x1F338; | &#x1F338; | 
| white flower | &#x1F4AE; | &#x1F4AE; | &#x1F4AE; | &#x1F4AE; | &#x1F4AE; | 
| rosette | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | &#x1F3F5;&#xFE0F; | 
| rose | &#x1F339; | &#x1F339; | &#x1F339; | &#x1F339; | &#x1F339; | 
| wilted flower | &#x1F940; | &#x1F940; | &#x1F940; | &#x1F940; | &#x1F940; | 
| hibiscus | &#x1F33A; | &#x1F33A; | &#x1F33A; | &#x1F33A; | &#x1F33A; | 
| sunflower | &#x1F33B; | &#x1F33B; | &#x1F33B; | &#x1F33B; | &#x1F33B; | 
| blossom | &#x1F33C; | &#x1F33C; | &#x1F33C; | &#x1F33C; | &#x1F33C; | 
| tulip | &#x1F337; | &#x1F337; | &#x1F337; | &#x1F337; | &#x1F337; | 

### plant-other

| name | EmojiOne | Twitter | OpenMoji | Noto Emoji | Blobmoji |
|:-:|:-:|:-:|:-:|:-:|
| seedling | &#x1F331; | &#x1F331; | &#x1F331; | &#x1F331; | &#x1F331; | 
| potted plant |  | &#x1FAB4; | &#x1FAB4; | &#x1FAB4; | &#x1FAB4; | 
| evergreen tree | &#x1F332; | &#x1F332; | &#x1F332; | &#x1F332; | &#x1F332; | 
| deciduous tree | &#x1F333; | &#x1F333; | &#x1F333; | &#x1F333; | &#x1F333; | 
| palm tree | &#x1F334; | &#x1F334; | &#x1F334; | &#x1F334; | &#x1F334; | 
| cactus | &#x1F335; | &#x1F335; | &#x1F335; | &#x1F335; | &#x1F335; | 
| sheaf of rice | &#x1F33E; | &#x1F33E; | &#x1F33E; | &#x1F33E; | &#x1F33E; | 
| herb | &#x1F33F; | &#x1F33F; | &#x1F33F; | &#x1F33F; | &#x1F33F; | 
| shamrock | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | &#x2618;&#xFE0F; | 
| four leaf clover | &#x1F340; | &#x1F340; | &#x1F340; | &#x1F340; | &#x1F340; | 
| maple leaf | &#x1F341; | &#x1F341; | &#x1F341; | &#x1F341; | &#x1F341; | 
| fallen leaf | &#x1F342; | &#x1F342; | &#x1F342; | &#x1F342; | &#x1F342; | 
| leaf fluttering in wind | &#x1F343; | &#x1F343; | &#x1F343; | &#x1F343; | &#x1F343; | 
