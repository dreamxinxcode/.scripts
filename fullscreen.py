import os

def main():
    with open('/home/arch/.config/bspwm/bspwmrc') as bspwmrc:
        for line in bspwmrc:
            if 'fullscreen=true' in line:
                os.system("sed -i 's/fullscreen=true/fullscreen=false/g' /home/arch/.config/bspwm/bspwmrc")

            elif 'fullscreen=false' in line:
                os.system("sed -i 's/fullscreen=false/fullscreen=true/g' /home/arch/.config/bspwm/bspwmrc")

    with open('/home/arch/.config/picom.conf') as picom:
        for line in picom:
            if 'corner-radius = 0' in line:
                os.system("sed -i 's/corner-radius = 0/corner-radius = 15/g' /home/arch/.config/picom.conf")

            elif 'corner-radius = 15' in line:
                os.system("sed -i 's/corner-radius = 15/corner-radius = 0/g' /home/arch/.config/picom.conf")

if __name__ == "__main__":
    main()
    os.system('/home/$USER/.config/bspwm/bspwmrc')
    os.system('picom')
