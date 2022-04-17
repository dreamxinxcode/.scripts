#!/bin/bash

if grep -Fxq "URxvt.transparent: false" /home/$USER/.Xresources
then
	sed -i 's/URxvt\.transparent: false/URxvt\*transparent: true/g' /home/$USER/.Xresources
	xrdb ~/.Xresources
else grep -Fxq "URxvt.transparent: true" /home/$USER/.Xresources
	sed -i 's/URxvt\.transparent: true/URxvt\*transparent: false/g' /home/$USER/.Xresources
	xrdb ~/.Xresources
fi
