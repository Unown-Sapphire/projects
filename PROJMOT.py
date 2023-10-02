import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np

Gravity_Options = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Sun"]

#entry UI
root = tk.Tk()
root.geometry("400x700")
title = tk.Label(root, text="Projectile Motion Calculator", font=('Times New Roman Bold', 22))
title.pack()
#Initial Velocity
initial_velocity_text = tk.Label(root, text="Enter initial velocity:", font=('Arial', 13))
initial_velocity_text.pack()
initial_velocity = tk.Entry(root, justify="center")
initial_velocity.pack()

#Angle of launch
launch_angle_text = tk.Label(root, text="Enter the Angle of launch of the object:", font=('Arial', 13))
launch_angle_text.pack()
launch_angle = tk.Entry(root, justify="center")
launch_angle.pack()

#Simulation of Gravity
Gravity_Select_Text = tk.Label(root, text="Select the gravity to simulate:", font=('Arial', 13))
Gravity_Select_Text.pack()
grav_menu = tk.StringVar(root)
grav_menu.set("Select gravity to simulate")
grav_sel = tk.OptionMenu(root, grav_menu, *Gravity_Options)
grav_sel.pack()



#logic + graphing
def calculations():
    print(grav_menu.get())
    if int(launch_angle.get()) <= 90:
        #velocities
        vertical_velocity = (int(initial_velocity.get())) * math.sin(int(launch_angle.get()) * ((math.pi)/180))
        print("Vertical Velocity is:", vertical_velocity)
        horizontal_velocity = (int(initial_velocity.get())) * math.cos(int(launch_angle.get()) * ((math.pi)/180))
        print("Horizontal Velocity is:", horizontal_velocity)
        def logic(g: float):
            max_height = ((vertical_velocity)**2)/(2*(g))
            print("The maximum height the projectile reached was:", max_height,"m")
            time_taken = ((vertical_velocity)/g)
            print("The time taken for the projectile to reach maximum height was:", float(time_taken),"s")
            horizontal_displacement = (horizontal_velocity * (2 * time_taken))
            print("The horizontal distance the projectile travellled was:", horizontal_displacement,"m")
            plt.style.use('_mpl-gallery')
            x = np.linspace(0, int(horizontal_displacement)+0.9999, num=1000)
            y = ((-(max_height))/((1/2)*horizontal_displacement)**2)*((x-((1/2)*horizontal_displacement))**2) + max_height
            fig, ax = plt.subplots()
            ax.plot(x, y, linewidth=2.0,)
            ax.set_xlabel('Horizontal Height(m)')
            ax.set_ylabel('Vertical Height(m)')
            plt.tight_layout()
            plt.show()
        if grav_menu.get() == "Mercury":
            logic(3.703)
        elif grav_menu.get() == "Venus":
            logic(8.872)
        elif grav_menu.get() == "Earth":
            logic(9.8067)
        elif grav_menu.get() == "Mars":
            logic(3.728)
        elif grav_menu.get() == "Jupiter":
            logic(25.93)
        elif grav_menu.get() == "Saturn":
            logic(11.19)
        elif grav_menu.get() == "Uranus":
            logic(9.01)
        elif grav_menu.get() == "Neptune":
            logic(11.28)
        elif grav_menu.get() == "Pluto":
            logic(0.610)
        elif grav_menu.get() == "Sun":
            logic(274.1)
        else:
            print("You havent selected a planet :C")

    else:
        print("Projectile angle exceeds calculable limit!")        

#Submission of Data
submit_button = tk.Button(root, text="Submit Data", command=lambda:[calculations()])
submit_button.pack()

root.mainloop()