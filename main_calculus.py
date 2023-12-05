

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
from cal_bridge import *
import mplcursors
 
class ctkApp:

    
    def __init__(self):
        global t
        ctk.set_appearance_mode("Light")        
 
        
        ctk.set_default_color_theme("green") 

        self.root = ctk.CTk()
        self.root.title("App")   
        self.length = 50
        self.height = 20
        self.base = 5
        self.alpha = 5.5
        self.x_c = []
        self.y_c = []
        self.text = ""

        self.cursor = None
        self.graph()

        self.root.after(0, lambda:self.root.state('zoomed'))

        self.root.mainloop()

    def get_data(self):
        root1 = ctk.CTk()  # create the Tk window like you normally do
        root1.geometry("400x240")
        root1.title("CustomTkinter Test")

        ctk.set_appearance_mode("Dark") 
        ctk.set_default_color_theme("green")
        ponts_tension = tension_cable(self.alpha, self.base)

        l = length_cable(self.length, self.height, self.base)
        label_len = ctk.CTkLabel(master=root1, text=f"The length of whole cable is : {l}", font=('Agency FB Bold', 20)).grid(row = 1, column = 1)
        
        useless = ctk.CTkLabel(master=root1, text="").grid(row = 2, column = 1)

        label_len = ctk.CTkLabel(master=root1, text=f"Tension at the endpoints of the bridge : {ponts_tension[0]}N", font=('Agency FB Bold', 20)).grid(row = 3, column = 1)
        
        useless = ctk.CTkLabel(master=root1, text="").grid(row = 2, column = 1)



        
        root1.mainloop()
    def update_alpha(self):

        global cursor
        
        text1 = e_al.get()
        cursor.remove()

        self.alpha = text1
        
        hov = ax.scatter(self.x_c, self.y_c,color='blue', label='Points', s=100)
        cursor = mplcursors.cursor(hov, hover=True)

        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))

            
            



    def update_length_in(self):
        
        global cursor
        
        ax.clear()
        cursor.remove()
        len_up = self.length+10
        self.length = len_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)
        self.x_c = x_cable
        self.y_c = y_cable
        ponts_tension = tension_cable(self.alpha, self.base)
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))
        
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, len_up+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([len_up, len_up], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()
    def update_length_de(self):
        global cursor
        ax.clear()
        cursor.remove()
        
        
        len_up = self.length-10
        self.length = len_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        mplcursors.cursor(ax).remove()
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))        
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, len_up+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([len_up, len_up], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()


    def update_height_in(self):
        global cursor
        ax.clear()
        cursor.remove()
        hei_up = self.height+5
        self.height = hei_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        mplcursors.cursor(ax).remove()
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))        
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, self.length+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([self.length, self.length], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()
    def update_height_de(self):
        global cursor
        ax.clear()
        cursor.remove()
        hei_up = self.height-5
        self.height = hei_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        mplcursors.cursor(ax).remove()
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))        
        ax.plot(x_parabola, y_paraboa,c='black')

        ax.legend()
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, self.length+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([self.length, self.length], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()



    def update_base_in(self):
        global cursor
        ax.clear()
        cursor.remove()
        bas_up = self.base+3
        self.base = bas_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        mplcursors.cursor(ax).remove()
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))        
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, self.length+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([self.length, self.length], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()
    def update_base_de(self):
        global cursor
        ax.clear()
        cursor.remove()
        bas_up = self.base-3
        self.base = bas_up
        x_parabola, y_paraboa, x_cable, y_cable = parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        mplcursors.cursor(ax).remove()
        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))
        ax.plot(x_parabola, y_paraboa,c='black')
        ax.plot([-15, self.length+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([self.length, self.length], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        canvas.draw()


    def graph(self):
        
        global ax, canvas, len, t, cursor, e_al

        def on_scroll(event):
            if event.button == 'down':
                ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
                ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
            if event.button == 'up':
                ax.set_xlim(ax.get_xlim()[0] / 1.1, ax.get_xlim()[1] / 1.1)
                ax.set_ylim(ax.get_ylim()[0] / 1.1, ax.get_ylim()[1] / 1.1)
            canvas.draw()
        
        fig = Figure(figsize=(15, 8), dpi=100)
        ax = fig.add_subplot(111)
        len = 50

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=0, y=0, relwidth=1, relheight=0.9)

        canvas.mpl_connect('scroll_event', on_scroll)
        

        
        x_parabola, y_paraboa, x_cable, y_cable= parabol(self.length, self.height, self.base)

        self.x_c = x_cable
        self.y_c = y_cable


        ponts_tension = tension_cable(self.alpha, self.base)
        ax.plot(x_parabola, y_paraboa,c='black')


        for i in range(0, round((self.length)/10)):
            ax.plot([x_cable[i], x_cable[i]], [1, y_cable[i]],c='red')
        hov = ax.scatter(x_cable, y_cable,color='blue', label='Points', s=100)
        ax.legend()
        cursor = mplcursors.cursor(hov, hover=True)
        ponts_tension = tension_cable(self.alpha, self.base)
        cursor.connect("add", lambda sel: sel.annotation.set(text=f"tension: {ponts_tension[sel.index]}N", bbox=dict(boxstyle='round', fc='white', ec='black'), fontsize=12))

        mplcursors.cursor(ax).remove()
        ax.plot([-15, len+15], [1, 1],color='#ccbf99',linewidth=20 )
        ax.plot([0, 0], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.plot([len, len], [-5, self.height+3],color='#aeafb2',linewidth=15)
        ax.set_title("Interactive Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

        canvas.draw()

        


        

        b1 = ctk.CTkButton(master=self.root, text="increase the length", command=self.update_length_in)
        b1.place(x=10, y = -40, rely=1.0, anchor='sw')
        b2 = ctk.CTkButton(master=self.root, text="decrease the length", command=self.update_length_de)
        b2.place(x=10, y = 0, rely=1.0, anchor='sw')

        b_h1 = ctk.CTkButton(master=self.root, text="increase the height", command=self.update_height_in)
        b_h1.place(x=230, y = -40, rely=1.0, anchor='sw')
        b_h2 = ctk.CTkButton(master=self.root, text="decrease the height", command=self.update_height_de)
        b_h2.place(x=230,y = -0, rely=1.0, anchor='sw')

        b_b1 = ctk.CTkButton(master=self.root, text="increase the base of cable", command=self.update_base_in)
        b_b1.place(x=430, y = -40,rely=1.0, anchor='sw')
        b_b2 = ctk.CTkButton(master=self.root, text="decrease the base of cable", command=self.update_base_de)
        b_b2.place(x=430, y = 0,rely=1.0, anchor='sw')

        l_al = ctk.CTkLabel(master=self.root, text="change the linear density(alpha)").place(x = 730, y = -40,rely=1.0, anchor='sw')
       
        e_al = ctk.CTkEntry(master=self.root)
        e_al.insert(0, '5.5')
        e_al.place(x = 930, y = -40,rely=1.0, anchor='sw')

        text1 = e_al.get()

        self.alpha = text1
        b_al = ctk.CTkButton(master=self.root, text="submit", command=self.update_alpha)
        b_al.place(x=830, y= 0,rely=1.0, anchor='sw')

        b_g1 = ctk.CTkButton(master=self.root, text="get the all data of bridge", command=self.get_data)
        b_g1.place(x=1230, y = -40,rely=1.0, anchor='sw')
        

    

 
if __name__ == "__main__":
    ctkApp()
    