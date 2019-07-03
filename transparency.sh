#!/bin/bash


if grep -Fxq "URxvt*transparent: false" /home/gentoo/.Xresources
then
	sed -i 's/URxvt\*transparent: false/URxvt\*transparent: true/g' /home/gentoo/.Xresources
	xrdb ~/.Xresources
else grep -Fxq "URxvt*transparent: true" /home/gentoo/.Xresources
	sed -i 's/URxvt\*transparent: true/URxvt\*transparent: false/g' /home/gentoo/.Xresources
	xrdb ~/.Xresources
fi
