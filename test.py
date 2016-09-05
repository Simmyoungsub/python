from tkinter import *
import math

root = Tk()
root.title(u"간단하게 그리기")

N=400
mypaper = Canvas(root,width=N,height=N,background="light green")

def draw_N(ox,oy,r,n):
    mypaper.create_text(ox,oy,font=(u"맑은고딕",20),fill="blue",text=str(n)+u"각형")
    total_angle_sum=(n-2)*math.pi
    a=ox+r
    b=oy
    for i in range(n):
        mypaper.create_line(a,b,ox+r*math.cos((i+1)*(math.pi-total_angle_sum/n)),oy+r*math.sin((i+1)*(math.pi-total_angle_sum/n)),width=3)
        
        a=ox+r*math.cos((i+1)*(math.pi-total_angle_sum/n))
        b=ox+r*math.sin((i+1)*(math.pi-total_angle_sum/n))
        
draw_N(200,200,100,5)
mypaper.grid(row=0,column=0)

root.mainloop()
