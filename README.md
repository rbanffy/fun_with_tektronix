# Fun With Tektronix

Tektronix direct view storage tube terminals were some of the coolest terminals that ever existed. They had no such thing as pixels - they drew on the phosphor screen with an electron beam the same way a pen plotter draws on paper. 

Storage tubes can be drawn to with a low power beam, in which case the image will have to be frequently redrawn, or with a high power beam, in which case the image will be stored and kept refreshed by the tube itself without the need to redraw it. This gives them their distinctive "feel" where the line that's being drawn is very bright in relation to the rest of the display and where you can pinpoint where the updates are happening by watching the bright spot. The last ones were capable of two colors by having an extra layer of red phosphor on top of the green one - by controlling the power of the writing beam, the terminal could excite one or two layers, allowing it to make green and yellow traces.

It also has the unsettling characteristic of building the image by firing a high-power particle gun in your general direction.

I wrote a small program that uses its graphics commands to draw lines on a screen. Unfortunately, I'm not cool enough to have an actual Tektronix 4004 (or one of its even cooler descendants) to play with. I have to content myself with what `xterm` can do.

Sigh.

Some screenshots follow:

![Running program](https://raw.githubusercontent.com/wiki/rbanffy/fun_with_tektronix/lines.png)

![The two files](https://raw.githubusercontent.com/wiki/rbanffy/fun_with_tektronix/terminal.png)

# Notes

Documentation on these relics is hard to find - one needs to dig through either source code or scanned versions of the documentation that survived. Luckily, a lot of physical terminals (made by DEC, Wyse and others) implemented the Tektronix functions. The Wyse documentation is excellent, as well as xterm's.

[WY-370 Programmer's Guide](http://www.bitsavers.org/pdf/wyse/WY-370/881133-02A_WY-370_Programmers_Guide_Jun90.pdf)
