import turtle
import random
import time

#oyunekranı

window = turtle.Screen()
window.title("Kablumbağayı Yakala")
window.bgcolor("#D0D3D4")

#turtle oluştur
tortu = turtle.Turtle()
tortu.shape("turtle")
tortu.color("Blue")
tortu.penup()

#skor
skor = 0

#skor yazısı
skorYazisi = turtle.Turtle()
skorYazisi.speed(0)
skorYazisi.color("Black")
skorYazisi.penup()
skorYazisi.hideturtle()
skorYazisi.goto(0,280)
skorYazisi.write(f"Skor= {skor}",align="center",font=("Courier",20,"normal"))

sure = 30

sureYazisi = turtle.Turtle()
sureYazisi.speed(0)
sureYazisi.color("black")
sureYazisi.penup()
sureYazisi.hideturtle()
sureYazisi.goto(0, -260)
sureYazisi.write(f"Süre:{sure} ", align="center",font=("Courier", 24, "normal"))

def tortuyuyakala(x, y):
    global skor
    skor +=1
    skorYazisi.clear()
    skorYazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))
    tortukac()

def tortukac():
    x = random.randint(-290,290)
    y = random.randint(-290, 290)
    tortu.hideturtle()
    tortu.goto(x, y)
    tortu.showturtle()

    window.ontimer(tortukac, 3000)
def zaman():
    global sure
    sure -= 1
    sureYazisi.clear()
    sureYazisi.write(f"Süre:{sure} ", align = "center", font = ("Courier", 24, "normal"))

    if sure == 0:
        oyunusifirla()
    else:
        window.ontimer(zaman, 1000)

def oyunusifirla():
    global skor, sure
    skor = 0
    sure = 30
    skorYazisi.clear()
    skorYazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))
    sureYazisi.clear()
    sureYazisi.write("Süre: {} saniye".format(sure), align="center", font=("Courier", 18, "normal"))
    tortukac()
    zaman()

tortukac()
tortu.onclick(tortuyuyakala)


zaman()
window.mainloop()











turtle.mainloop()