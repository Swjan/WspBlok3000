from scipy.special import hyp2f1
from matplotlib import pyplot as plt
from tkinter import *

window = Tk()
window.title("WspBlok3000")
window.geometry("500x500")

#Wersja Pythona: Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32


# math functions:
def Silnia(x):
    if x <= 1:
        return 1
    else:
        return x * Silnia(x - 1)


def Dwumian(x, y):
    return Silnia(x) / (Silnia(y) * (Silnia(x - y)))


# plot functions:
def plot(ox, oy):
    plt.close()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Prawdopodobieństwo blokady')
    ax1.set_xlabel('Natężenie ruchu w erlangach')
    ax1.plot(ox, oy)
    plt.show()

def doublePlot(ox, oyer, oyen):
    plt.close()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('Prawdopodobieństwo blokady')
    ax1.set_xlabel('Natężenie ruchu w erlangach')
    ax1.plot(ox, oyer)
    ax1.plot(ox, oyen)
    ax1.legend(["Erlang B", "Engset"])
    plt.show()


# WspBlok functions:
def ErlangB(nat, lines):
    if nat == 0:
        return 0
    if lines == 0:
        return 1
    else:
        return 1 + (lines / nat) * ErlangB(nat, lines - 1)


def EngsetSil(nat, lines, sources):
    return 1.0 / hyp2f1(1, 0 - lines, sources - lines, -1.0 / (nat / sources))


def EngsetR(nat, lines, sources):
    p = nat / sources

    if lines == 0:
        print("ZERO")
        return 1
    if lines != 0:
        return (p * (sources - lines) * EngsetR(nat, lines - 1, sources)) / (
                    lines + (p * (sources - lines) * EngsetR(nat, lines - 1, sources)))


def EngsetHyperGeo(nat, lines, sources):
    return 1.0 / hyp2f1(1, 0 - lines, sources - lines, -1.0 / (nat / sources))


# Print functions:


def printMenu():
    for widgets in window.winfo_children():
        widgets.place_forget()

    MFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    MButtonErlangB.pack()
    MButtonEngset.pack()
    MButtonErVsEn.pack()
    MButtonInfo.pack()


def printErlangBmenu():
    for widgets in window.winfo_children():
        widgets.place_forget()
    ErMFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ErMLabel.pack()
    ErMButtonW.pack()
    ErMButtonL.pack()
    ErMButtonNat.pack()
    ErMButtonM.pack()


def printErlangBW():
    for widgets in window.winfo_children():
        widgets.place_forget()
    ErWFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ErWLabel.pack()
    ErWEntryLinesLabel.pack()
    ErWEntryLines.pack()
    ErWEntryNat1Label.pack()
    ErWEntryNat1.pack()
    ErWEntryNat2Label.pack()
    ErWEntryNat2.pack()
    ErWButtonExecute.pack()
    ErWButtonMenu.pack()


def printErlangBL():
    for widgets in window.winfo_children():
        widgets.place_forget()
    ErLFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ErLLabel.pack()
    ErLEntryNatLabel.pack()
    ErLEntryNat.pack()
    ErLEntryBlokLabel.pack()
    ErLEntryBlok.pack()
    ErLEntryWynLabel.pack()
    ErLEntryWyn.pack()
    ErLButtonExecute.pack()
    ErLButtonMenu.pack()


def printErlangBNat():
    for widgets in window.winfo_children():
        widgets.place_forget()
    ErNatFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ErNatLabel.pack()
    ErNatEntryLinesLabel.pack()
    ErNatEntryLines.pack()
    ErNatEntryBlokLabel.pack()
    ErNatEntryBlok.pack()
    ErNatEntryWynLabel.pack()
    ErNatEntryWyn.pack()
    ErNatButtonExecute.pack()
    ErNatButtonMenu.pack()


def printEngsetM():
    for widgets in window.winfo_children():
        widgets.place_forget()
    EnMFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    EnMLabel.pack()
    EnMButtonW.pack()
    EnMButtonL.pack()
    EnMButtonNat.pack()
    EnMButtonM.pack()


def printEngsetW():
    for widgets in window.winfo_children():
        widgets.place_forget()
    EnWFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    EnWLabel.pack()
    EnWEntryLinesLabel.pack()
    EnWEntryLines.pack()
    EnWEntryNat1Label.pack()
    EnWEntryNat1.pack()
    EnWEntryNat2Label.pack()
    EnWEntryNat2.pack()
    EnWEntrySourcesLabel.pack()
    EnWEntrySources.pack()
    EnWButtonGenerate.pack()
    EnWButtonMenu.pack()


def printEngsetL():
    for widgets in window.winfo_children():
        widgets.place_forget()
    EnLFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    EnLLabel.pack()
    EnLEntryNatLabel.pack()
    EnLEntryNat.pack()
    EnLEntryBlokLabel.pack()
    EnLEntryBlok.pack()
    EnLEntrySLabel.pack()
    EnLEntryS.pack()
    EnLEntryWynLabel.pack()
    EnLEntryWyn.pack()
    EnLButtonExecute.pack()
    EnLButtonMenu.pack()

def printEngsetNat():
    for widgets in window.winfo_children():
        widgets.place_forget()
    EnNatFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    EnNatLabel.pack()
    EnNatEntryLinesLabel.pack()
    EnNatEntryLines.pack()
    EnNatEntryBlokLabel.pack()
    EnNatEntryBlok.pack()
    EnNatEntrySLabel.pack()
    EnNatEntryS.pack()
    EnNatEntryWynLabel.pack()
    EnNatEntryWyn.pack()
    EnNatButtonExecute.pack()
    EnNatButtonMenu.pack()
    
def printErVsEn():
    for widgets in window.winfo_children():
        widgets.place_forget()
    ErEnFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    ErEnLabel.pack()
    ErEnEntryLinesLabel.pack()
    ErEnEntryLines.pack()
    ErEnEntryNat1Label.pack()
    ErEnEntryNat1.pack()
    ErEnEntryNat2Label.pack()
    ErEnEntryNat2.pack()
    ErEnEntrySourcesLabel.pack()
    ErEnEntrySources.pack()
    ErEnButtonGenerate.pack()
    ErEnButtonMenu.pack()

def printInfo():
    for widgets in window.winfo_children():
        widgets.place_forget()
    InfoFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    BasicInfo.pack()
    UseInfo.pack()
    ErlangInfo.pack()
    EngsetInfo.pack()
    VsInfo.pack()
    InfoButtonMenu.pack()

# Execute functions:
def executeErW():
    nat1 = float(ErWEntryNat1.get())
    nat2 = float(ErWEntryNat2.get())
    lines = float(ErWEntryLines.get())
    if nat1 < 0:
        nat1 = 0
        ErWEntryNat1.insert(0, "0")
    if nat2 < nat1:
        nat2 = nat1+1
        ErWEntryNat2.insert(0, str(nat2))

    interval = (nat2 - nat1) / 100
    ox = []
    for i in range(101):
        ox.append(nat1 + i * interval)
    oy = []
    for x in ox:
        if x == 0:
            oy.append(0)
        else:
            oy.append(1 / ErlangB(x, lines))

    plot(ox, oy)


def executeErNat():
    NatIterator = 0.0001

    if(float(ErNatEntryLines.get()) < 1):
        ErNatEntryLines.delete(0, "end")
        ErNatEntryLines.insert(0, "1")

    if(float(ErNatEntryBlok.get()) >= 1):
        ErNatEntryWyn.delete(0, "end")
        ErNatEntryWyn.insert(0, "inf")

    else:
        while True:
            if 1 / ErlangB(NatIterator, float(ErNatEntryLines.get())) > float(ErNatEntryBlok.get()):
                NatIterator -= 0.1
                break
            NatIterator += 0.1
        while True:
            if 1 / ErlangB(NatIterator, float(ErNatEntryLines.get())) > float(ErNatEntryBlok.get()):
                NatIterator -= 0.01
                break
            NatIterator += 0.01
        while True:
            if 1 / ErlangB(NatIterator, float(ErNatEntryLines.get())) > float(ErNatEntryBlok.get()):
                NatIterator -= 0.001
                break
            NatIterator += 0.001
        ErNatEntryWyn.delete(0, "end")
        ErNatEntryWyn.insert(0, str(round(NatIterator, 3)))


def executeErL():
    i = 1

    while True:
        if 1 / ErlangB(float(ErLEntryNat.get()), i) < float(ErLEntryBlok.get()):
            break
        i += 1

    ErLEntryWyn.delete(0, "end")
    ErLEntryWyn.insert(0, str(i))

def executeEnNat():
    NatIterator = 0.0001

    if(float(EnNatEntryBlok.get()) >= 1):
        EnNatEntryWyn.delete(0, "end")
        EnNatEntryWyn.insert(0, "inf")
    else:
        if(float(EnNatEntryLines.get()) >= float(EnNatEntryS.get())):
            EnNatEntryWyn.delete(0, "end")
            print(EnNatEntryS.get())
            EnNatEntryWyn.insert(0, EnNatEntryS.get())
        else:
            while True:
                if EngsetSil(NatIterator, float(EnNatEntryLines.get()), int(EnNatEntryS.get()) ) > float(EnNatEntryBlok.get()):
                    NatIterator -= 0.1
                    break
                NatIterator += 0.1
            while True:
                if EngsetSil(NatIterator, float(EnNatEntryLines.get()), int(EnNatEntryS.get()) ) > float(EnNatEntryBlok.get()):
                    NatIterator -= 0.01
                    break
                NatIterator += 0.01
            while True:
                if EngsetSil(NatIterator, float(EnNatEntryLines.get()), int(EnNatEntryS.get()) ) > float(EnNatEntryBlok.get()):
                    NatIterator -= 0.001
                    break
                NatIterator += 0.001

            if NatIterator > float(EnNatEntryS.get()):
                NatIterator = float(EnNatEntryS.get())

            EnNatEntryWyn.delete(0, "end")
            EnNatEntryWyn.insert(0, str(round(NatIterator, 3)))

def executeEnL():
    i = 1
    while True:
        if EngsetSil(float(EnLEntryNat.get()), i, int(EnLEntryS.get())) < float(EnLEntryBlok.get()):
            break
        i += 1
    EnLEntryWyn.delete(0, "end")
    EnLEntryWyn.insert(0, str(i))

def executeEnW():
    nat1 = float(EnWEntryNat1.get())
    nat2 = float(EnWEntryNat2.get())
    lines = float(EnWEntryLines.get())
    sources = float(EnWEntrySources.get())
    interval = (nat2 - nat1) / 100
    ox = []
    for i in range(101):
        ox.append(nat1 + i * interval)
    oy = []
    for x in ox:
        if x == 0:
            oy.append(0)
        else:
            oy.append(EngsetSil(x, lines, sources))

    plot(ox, oy)

def executeErVsEn():
    nat1 = float(ErEnEntryNat1.get())
    nat2 = float(ErEnEntryNat2.get())
    lines = float(ErEnEntryLines.get())
    sources = float(ErEnEntrySources.get())
    interval = (nat2 - nat1) / 100
    ox = []
    for i in range(101):
        ox.append(nat1 + i * interval)
    oy = []
    for x in ox:
        if x == 0:
            oy.append(0)
        else:
            oy.append(1/ErlangB(x, lines))
    oy2 = []
    for x in ox:
        if x == 0:
            oy2.append(0)
        else:
            oy2.append(EngsetSil(x, lines, sources))

    doublePlot(ox, oy, oy2)


# Menu widgets:
MFrame = Frame(window)

MButtonErlangB = Button(MFrame, text="Erlang B", width=20, command=printErlangBmenu)
MButtonEngset = Button(MFrame, text="Engset", width=20, command=printEngsetM)
MButtonErVsEn = Button(MFrame, text="Erlang VS Engset", width=20, command=printErVsEn)
MButtonInfo = Button(MFrame, text="Info", width=20, command=printInfo)

# ErlangBmenu widgets:
ErMFrame = Frame(window)

ErMLabel = Label(ErMFrame, text="Erlang B Menu", pady=40)
ErMButtonW = Button(ErMFrame, text="Wykres współczynnika blokady", width=30, command=printErlangBW)
ErMButtonL = Button(ErMFrame, text="Rozmiarowanie sieci", width=20, command=printErlangBL)
ErMButtonNat = Button(ErMFrame, text="Maksymalne natężenie", width=20, command=printErlangBNat)
ErMButtonM = Button(ErMFrame, text="Menu", width=20, command=printMenu)

# ErlangBwykres widgets:
ErWFrame = Frame(window)

ErWLabel = Label(ErWFrame, text="Wykres Erlang B", pady=20)
ErWEntryLinesLabel = Label(ErWFrame, text="Podaj liczbe linii w sieci:")
ErWEntryLines = Entry(ErWFrame, width=5)
ErWEntryLines.insert(0, "5")

ErWEntryNat1Label = Label(ErWFrame, text="Podaj minimalne natezenie ruchu w erlangach:")
ErWEntryNat1 = Entry(ErWFrame, width=5)
ErWEntryNat1.insert(0, "0")

ErWEntryNat2Label = Label(ErWFrame, text="Podaj maksymalne natezenie ruchu w erlangach:")
ErWEntryNat2 = Entry(ErWFrame, width=5)
ErWEntryNat2.insert(0, "10")

ErWButtonMenu = Button(ErWFrame, text="Menu", command=printMenu)
ErWButtonExecute = Button(ErWFrame, text="Generuj wykres", command=executeErW)

# ErlangBL widgets:
ErLFrame = Frame(window)

ErLLabel = Label(ErLFrame, text="Rozmiarowanie Erlang B", pady=40)
ErLEntryNatLabel = Label(ErLFrame, text="Podaj natezenie ruchu w erlangach:")
ErLEntryNat = Entry(ErLFrame, width=5)
ErLEntryNat.insert(0, "2.4")

ErLEntryBlokLabel = Label(ErLFrame, text="Podaj maksymalne prawdopodobieństwo blokady:")
ErLEntryBlok = Entry(ErLFrame, width=5)
ErLEntryBlok.insert(0, "0.04")

ErLEntryWynLabel = Label(ErLFrame, text="Liczba linii obsługujących połączenia:")
ErLEntryWyn = Entry(ErLFrame, width=5)

ErLButtonExecute = Button(ErLFrame, text="Oblicz", command=executeErL)
ErLButtonMenu = Button(ErLFrame, text="Erlang B Menu", command=printErlangBmenu)

# ErlangBNat widgets:
ErNatFrame = Frame(window)

ErNatLabel = Label(ErNatFrame, text="Maksymalne natężenie Erlang B", pady=40)
ErNatEntryLinesLabel = Label(ErNatFrame, text="Podaj liczbe linii w sieci:")
ErNatEntryLines = Entry(ErNatFrame, width=5)
ErNatEntryLines.insert(0, "3")

ErNatEntryBlokLabel = Label(ErNatFrame, text="Podaj maksymalne prawdobieństwo blokady:")
ErNatEntryBlok = Entry(ErNatFrame, width=5)
ErNatEntryBlok.insert(0, "0.354")

ErNatEntryWynLabel = Label(ErNatFrame, text="Maksymalne natężenie ruchu:")
ErNatEntryWyn = Entry(ErNatFrame, width=5)

ErNatButtonExecute = Button(ErNatFrame, text="Oblicz", command=executeErNat)
ErNatButtonMenu = Button(ErNatFrame, text="Erlang B Menu", command=printErlangBmenu)

# EngsetMenu widgets:
EnMFrame = Frame(window)

EnMLabel = Label(EnMFrame, text="Engset Menu", pady=40)
EnMButtonW = Button(EnMFrame, text="Wykres współczynnika blokady", width=30, command=printEngsetW)
EnMButtonL = Button(EnMFrame, text="Rozmiarowanie sieci", width=20, command=printEngsetL)
EnMButtonNat = Button(EnMFrame, text="Maksymalne natężenie", width=20, command=printEngsetNat)
EnMButtonM = Button(EnMFrame, text="Menu", width=20, command=printMenu)

# EngsetW widgets:
EnWFrame = Frame(window)

EnWLabel = Label(EnWFrame, text="Wykres Engset", pady=20)
EnWEntryLinesLabel = Label(EnWFrame, text="Podaj liczbę linii w sieci:")
EnWEntryLines = Entry(EnWFrame, width=5)
EnWEntryLines.insert(0, "5")

EnWEntryNat1Label = Label(EnWFrame, text="Podaj minimalne natężenie ruchu w erlangach:")
EnWEntryNat1 = Entry(EnWFrame, width=5)
EnWEntryNat1.insert(0, "0")

EnWEntryNat2Label = Label(EnWFrame, text="Podaj maksymalne natężenie ruchu w erlangach:")
EnWEntryNat2 = Entry(EnWFrame, width=5)
EnWEntryNat2.insert(0, "10")

EnWEntrySourcesLabel = Label(EnWFrame, text="Podaj liczbe źródeł ruchu:")
EnWEntrySources = Entry(EnWFrame, width=5)
EnWEntrySources.insert(0, "10")

EnWButtonMenu = Button(EnWFrame, text="Menu", command=printEngsetM)
EnWButtonGenerate = Button(EnWFrame, text="Generuj wykres", command=executeEnW)

# EngsetL widgets:
EnLFrame = Frame(window)

EnLLabel = Label(EnLFrame, text="Rozmiarowanie Engset", pady=40)
EnLEntryNatLabel = Label(EnLFrame, text="Podaj natezenie ruchu w erlangach:")
EnLEntryNat = Entry(EnLFrame, width=5)
EnLEntryNat.insert(0, "2.4")

EnLEntryBlokLabel = Label(EnLFrame, text="Podaj maksymalne prawdopodobieństwo blokady:")
EnLEntryBlok = Entry(EnLFrame, width=5)
EnLEntryBlok.insert(0, "0.04")

EnLEntrySLabel = Label(EnLFrame, text="Podaj liczbę źródeł ruchu:")
EnLEntryS = Entry(EnLFrame, width=5)
EnLEntryS.insert(0, "5")

EnLEntryWynLabel = Label(EnLFrame, text="Liczba linii obsługujących połączenia:")
EnLEntryWyn = Entry(EnLFrame, width=5)

EnLButtonExecute = Button(EnLFrame, text="Oblicz", command=executeEnL)
EnLButtonMenu = Button(EnLFrame, text="Engset Menu", command=printEngsetM)

# EngsetNat widgets:
EnNatFrame = Frame(window)

EnNatLabel = Label(EnNatFrame, text="Maksymalne natężenie Engset", pady=40)
EnNatEntryLinesLabel = Label(EnNatFrame, text="Podaj liczbe linii w sieci:")
EnNatEntryLines = Entry(EnNatFrame, width=5)
EnNatEntryLines.insert(0, "3")

EnNatEntryBlokLabel = Label(EnNatFrame, text="Podaj maksymalne prawdobieństwo blokady:")
EnNatEntryBlok = Entry(EnNatFrame, width=5)
EnNatEntryBlok.insert(0, "0.354")

EnNatEntrySLabel = Label(EnNatFrame, text="Podaj liczbę źródeł ruchu:")
EnNatEntryS = Entry(EnNatFrame, width=5)
EnNatEntryS.insert(0, "5")

EnNatEntryWynLabel = Label(EnNatFrame, text="Maksymalne natężenie ruchu:")
EnNatEntryWyn = Entry(EnNatFrame, width=5)

EnNatButtonExecute = Button(EnNatFrame, text="Oblicz", command=executeEnNat)
EnNatButtonMenu = Button(EnNatFrame, text="Engset Menu", command=printEngsetM)

# ErlangVsEngset widgets:
ErEnFrame = Frame(window)

ErEnLabel = Label(ErEnFrame, text="Wykres Erlang B vs Engset", pady=20)
ErEnEntryLinesLabel = Label(ErEnFrame, text="Podaj liczbę linii w sieci:")
ErEnEntryLines = Entry(ErEnFrame, width=5)
ErEnEntryLines.insert(0, "5")

ErEnEntryNat1Label = Label(ErEnFrame, text="Podaj minimalne natężenie ruchu w erlangach:")
ErEnEntryNat1 = Entry(ErEnFrame, width=5)
ErEnEntryNat1.insert(0, "0")

ErEnEntryNat2Label = Label(ErEnFrame, text="Podaj maksymalne natężenie ruchu w erlangach:")
ErEnEntryNat2 = Entry(ErEnFrame, width=5)
ErEnEntryNat2.insert(0, "10")

ErEnEntrySourcesLabel = Label(ErEnFrame, text="Podaj liczbe źródeł ruchu:")
ErEnEntrySources = Entry(ErEnFrame, width=5)
ErEnEntrySources.insert(0, "10")

ErEnButtonMenu = Button(ErEnFrame, text="Menu", command=printMenu)
ErEnButtonGenerate = Button(ErEnFrame, text="Generuj wykres", command=executeErVsEn)

#Info widgets:
InfoFrame = Frame(window)
BasicInfo = Label(InfoFrame, text="WspBlok3000: program pozwalający obliczyć parametry sieci telekomunikacyjnej przy użyciu modeli Erlang B i Engset.")
UseInfo = Label(InfoFrame, text="Pozwala na obliczenie współczynnika blokady, maksymalnego natężenia ruchu w sieci przy zachowaniu zadanego QoS oraz ilości linii obsługujących ruch wymaganych do utrzymania sprawnego działania sieci.")
ErlangInfo = Label(InfoFrame, text="Model Erlang B został oparty na funkcji rekurencyjnej, w celu ominięcia problemów związanych z silnimi wysokich liczb.")
EngsetInfo = Label(InfoFrame, text="Model Engset korzysta z funkcji hipergeometrycznej (hyp2f1 z pakietu scipy) - z podobnych powodów.")
VsInfo = Label(InfoFrame, text="Program posiada również możliwość rysowania wykresów współczynnika blokady dla obu modeli z osobna, a także pojedynczego wykresu porównawczego.")
InfoButtonMenu = Button(InfoFrame, text="Menu", command=printMenu)

#Start:
printMenu()

window.mainloop()
