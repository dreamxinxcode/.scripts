import os


def main():
    bspwmrc_path = '/home/arch/.config/bspwm/bspwmrc'
    output_path = '/home/arch/.config/bspwm/bspwmrc_output'

    with open(bspwmrc_path) as bspwmrc:
        for line in bspwmrc:
            if 'PRODUCTIVE_MODE OFF' in line:
                os.system("sed -i 's/PRODUCTIVE_MODE OFF/PRODUCTIVE_MODE ON/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config border_width           4/bspc config border_width           0/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config window_gap             20/bspc config window_gap             0/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config top_padding            $(( 12 + 27+8 + 13  +  1 ))/bspc config top_padding            $(( 0 + 0+0 + 0  +  0 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config left_padding           $(( 30  +  60 ))/bspc config left_padding           $(( 0  +  0 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config right_padding          $(( 30  +  60 ))/bspc config right_padding          $(( 0  +  0 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config bottom_padding         $(( 20  +  10 ))/bspc config bottom_padding         $(( 0  +  0 ))/g' /home/arch/.config/bspwm/bspwmrc")          
            
            elif 'PRODUCTIVE_MODE ON' in line:
                os.system("sed -i 's/PRODUCTIVE_MODE ON/PRODUCTIVE_MODE OFF/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config border_width           0/bspc config border_width           4/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config window_gap             0/bspc config window_gap             20/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config top_padding            $(( 0 + 0+0 + 0  +  0 ))/bspc config top_padding            $(( 12 + 27+8 + 13  +  1 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config left_padding           $(( 0  +  0 ))/bspc config left_padding           $(( 30  +  60 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config right_padding          $(( 0  +  0 ))/bspc config right_padding          $(( 30  +  60 ))/g' /home/arch/.config/bspwm/bspwmrc")
                os.system("sed -i 's/bspc config bottom_padding         $(( 0  +  0 ))/bspc config bottom_padding         $(( 20  +  10 ))/g' /home/arch/.config/bspwm/bspwmrc")          



if __name__ == "__main__":
    main()
    os.system('/home/$USER/.config/bspwm/bspwmrc')