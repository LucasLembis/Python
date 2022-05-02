from tkinter import *
Master = Tk()

#funcoes

def ClassificacaoIMCAdulto(imc):
    if imc < 18.5:
        LabelIMCClassificacao["text"]="Baixo peso"

    elif imc >= 18.5 and imc <= 24.9:
        LabelIMCClassificacao["text"] = "Peso normal"

    elif imc >= 25.0 and imc <= 29.9:
        LabelIMCClassificacao["text"] = "Pré-obesidade"

    elif imc >= 30.0 and imc <= 34.9:
        LabelIMCClassificacao["text"] = "Obesidade grau 1"

    elif imc >= 35.0 and imc <= 39.9:
        LabelIMCClassificacao["text"] = "Obesidade grau 2"

    elif imc >= 40.0:
        LabelIMCClassificacao["text"] = "Obesidade grau 3"


def ClassificacaoIMCCrianca(imc):
    if imc <= 18.5:
        LabelIMCClassificacao["text"]="Baixo peso"

    elif imc > 18.5 and imc < 24.9:
        LabelIMCClassificacao["text"] = "Peso Normal"

    elif imc > 25 and imc < 29.9:
        LabelIMCClassificacao["text"] = "Excesso de Peso"

    else:
        LabelIMCClassificacao["text"] = "Obesidade"


def CalculaIMC():
    altura = float(EntryAltura.get())
    peso = float(EntryPeso.get())
    divisor = altura**2
    imc = peso / divisor
    imc = round(imc, 1)
    LabelIMCResultado["text"]=imc

    if FaixaEtaria.get():
        ClassificacaoIMCAdulto(imc)

    else:
        ClassificacaoIMCCrianca(imc)


#---------------------------------------------

#imagens

TitleImg= PhotoImage(file="TitleImg.png")
TableImg= PhotoImage(file="TableImg.png")
BottomImg= PhotoImage(file="BottomImg.png")
Box1Img= PhotoImage(file="Box1Img.png")
Box2Img= PhotoImage(file="Box2Img.png")

#---------------------------------------------
#Frames-Containers: agrupadores de objetos na tela

TopFrame= Frame(Master, relief='solid', bd=0, bg="#1c1c1a")
TopFrame.place(width=991, height=407, x=0, y=0)

LabelTitle = Label(TopFrame, image=TitleImg, borderwidth=0,
                   compound="center", highlightthickness=0)
LabelTitle.place(x=0, y=0)

LabelTitle = Label(TopFrame, image=TableImg, borderwidth=0,
                   compound="center", highlightthickness=0)
LabelTitle.place(x=0, y=48)

BottomFrame = Frame(Master, relief='solid', bd=0, bg="#1c1c3a")
BottomFrame.place(width=991, height=232, x=0, y=407)

LabelBottom = Label(BottomFrame, image=BottomImg,
borderwidth=0,
            compound="center", highlightthickness=0)
LabelBottom.place(x=0, y=0)


Box1Frame = Frame(Master, relief='solid', bd=0, bg="#B97A57")
Box1Frame.place(width=276, height=200, x=23, y=422)
LabelBox1 = Label(Box1Frame, image=Box1Img, borderwidth=0,
                  compound="center", highlightthickness=0)
LabelBox1.place(x=0, y=0)


Box2Frame = Frame(Master, relief='solid', bd=0, bg="#7F7F7F")
Box2Frame.place(width=612, height=175, x=318, y=422)
LabelBox2 = Label(Box2Frame, image=Box2Img, borderwidth=0,
                  compound="center", highlightthickness=0)
LabelBox2.place(x=0, y=0)

#---------------------------------------------------------

EntryAltura = Entry(Box1Frame, font="Arial 15")
EntryAltura.place(width=88, height=21, x=123, y=109)
EntryAltura.insert(END, 1.75)

EntryPeso = Entry(Box1Frame, font="Arial 15")
EntryPeso.place(width=88, height=21, x=123, y=148)
EntryPeso.insert(END, 70)

LabelIMCResultado = Label(Box2Frame, text="0.00", font="Arial 20", bg="white", fg="#FF0000")
LabelIMCResultado.place(width=102, height=42, x=32, y=56)

LabelIMCClassificacao = Label(Box2Frame, text="Peso Normal", font="Arial 20", bg="white", fg="#FF0000")
LabelIMCClassificacao.place(width=395, height=41, x=175, y=56)

ButtonIMC = Button(Box2Frame, text="Calcular IMC", font="Arial 11 bold", command=CalculaIMC, bg="#993399")
ButtonIMC.place(width=117, height=41, x=238, y=126)

FaixaEtaria = IntVar()
FaixaEtaria.set(1)
CheckCrianca = Checkbutton(Box1Frame, variable=FaixaEtaria, onvalue=1, bg="#993399")
CheckCrianca.place(x=68, y=53)

CheckCrianca = Checkbutton(Box1Frame, variable=FaixaEtaria, onvalue=0, bg="#993399")
CheckCrianca.place(x=173, y=53)


#Configurações da tela Master

Master.geometry("951x634+50+50")
Master.title("Calculadora de Indice de Massa Corporal - IMC")
Master.iconbitmap(default="Imc.ico")
mainloop()










