#liblary yang di pakai
from tkinter import *

#akses data set
file1 = open("Trainset Syllabification 01 40K 1 2 3 4.txt","r")
data1 = file1.read()


#pemisah anatara kata dan silabifikasi
a1 = data1.split()
l1 = []
l2 = []
for i in range(len(a1)):
    if i % 2 == 0:
        l1.append(a1[i])
    elif i % 2 != 0:
        l2.append(a1[i])

#merubah silabifikasi menjadi kata dasar berpola
def def0(list):
  l1 = []
  for i in list:
    a = def1(i)
    for j in a:
      if j=='.':
        a.remove('.')
    l1.append(''.join(a))
  return l1

#memasukan file int data ke dalam list 1 dimensi
def def1(data):
    l = []
    for i in range(len(data)):
        l.append(data[i])
    return l
 
# identifikasi huruf
def def2(lis):
    #
    l = []
    #konsonan
    l1 = ["q","Q","w","W","r","R","t","T","y","Y","p","P","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L","z","Z","X","x","c","C","v","V","b","B","n","N","m","M"]
    #vokal
    l2 = ["a","i","u","e","o","A","I","U","E","O"]
    #pemisah silabifikasi
    a0 = "."
    #simbol selain diftong dan gabungan konesonan
    a1 = '-'
    a2 = '#' #e pepet
    # simbol diftong
    a3 = '@' #au
    a4 = '$' #ai
    a5 = '%' #ei
    a6 = '^' #oi
    # simbol gabungan huruf konsonan
    a7 = '(' #kh
    a8 = ')' #nk,ng
    a9 = '~' #sy
    a10 = '+' #ny
    a11 = '[au]'#(diftong)
    a12 = '[ai]'#(diftong)
    a13 = '[ei]'#(diftong)
    a14 = '[oi]'#(diftong)
    a15 = '[kh]'#(Gabungan Huruf Konsonan)
    a16 = '[nk]'#(Gabungan Huruf Konsonan)
    a17 = '[ng]'#(Gabungan Huruf Konsonan)
    a18 = '[sy]'#(Gabungan Huruf Konsonan)
    a19 = '[ny]'#(Gabungan Huruf Konsonan)
    for i in range(len(lis)):
        for j in range(len(l1)):
            if lis[i] == l1[j]:
                l.append("k")
        for z in range(len(l2)):
            if lis[i] == l2[z]:
                l.append("v")
        if lis[i] == a0:
            l.append(".")
        elif lis[i] == a1:
            l.append("-")
        elif lis[i] == a2:
            l.append("#")
        elif lis[i] == a3:
            l.append("@")
        elif lis[i] == a4:
            l.append("$")
        elif lis[i] == a5:
            l.append("%")
        elif lis[i] == a6:
            l.append("^")
        elif lis[i] == a7:
            l.append("(")
        elif lis[i] == a8:
            l.append(")")
        elif lis[i] == a9:
            l.append("~")
        elif lis[i] == a10:
            l.append("+")
        elif lis[i] == a11:
            l.append("@")
        elif lis[i] == a12:
            l.append("$")
        elif lis[i] == a13:
            l.append("%")
        elif lis[i] == a14:
            l.append("^")
        elif lis[i] == a15:
            l.append("(")
        elif lis[i] == a16:
            l.append(")")
        elif lis[i] == a17:
            l.append(")")
        elif lis[i] == a18:
            l.append("~")
        elif lis[i] == a19:
            l.append("+")
    return l
 
# fungsi identifikasi data
def def3(data):
    l = []
    for i in range(len(data)):
        a = def1(data[i])
        b = def2(a)
        l.append(b)
    return l

# eliminasi elemen yang sama pada suatu list
def def4(data):
    l = [] 
    for i in data: 
        if i not in l: 
            l.append(i)
    return l
 
#pembuatan pola kata (pola yang sama akan di eliminasi)
def def5(data1, data2):
    l1 = []
    l2 = []
    a1 = def3(data1)
    a2 = def3(data2)
    for i in range(len(a1)):
        l1.append(a1[i])
        l1.append(a2[i])
        l2.append(l1)
        l1 = []
    a3 = def4(l2)
    return a3

# silabifikasi proses 1
def def6(data):
    l1 = []
    l3 = []
    l4 = []
    for i in range(len(data)):
        a = def1(data[i])
        l1 = def2(a)
        l2 = list(data[i])
        l3.append(l1)
        l3.append(l2)
        l4.append(l3)
        l3 = []
    return l4
 
# silabifikasi proses 2
def def7(data1, data2):
    l1 =[]
    l2 =[]
    for i in data1:
        for j in data2:
            if i[0] == j[0]:
                l1.append(i[1])
                l1.append(j[1])
                break
        l2.append(l1)
        l1 = []
    return l2

#silabifikasi proses 3
def def8(data):
    l1 = []
    for i in data:
        for j in range(len(i[1])):
            if i[1][j] == '.':
                i[0][j:j] = ['.']
        l1.append(i[0])
    return l1

def def11(data):
	for i in range(len(data[0])):
		if data[0][i]=="@":
			data[0][i]="au"
		elif data[0][i]=="$":
			data[0][i]="ai"
		elif data[0][i]=="%":
			data[0][i]="ei"
		elif data[0][i]=="^":
			data[0][i]="oi"
		elif data[0][i]=="(":
			data[0][i]="kh"
		elif data[0][i]==")":
			data[0][i]="ng"
		elif data[0][i]=="~":
			data[0][i]="sy"
		elif data[0][i]=="+":
			data[0][i]="ny"
	str1 = "" 
	for j in data[0]: 
		str1 += j
	return str1

#

# kata dasar
a = def0(l2)
# pola
b = def5(a,l2) # pola kata, pola silabel
# silabifikasi proses 1
c = def6(a) # pola kata, kata dasar
# silabifikasi proses 2
e = def7(c,b)
# silabifikasi proses 3
f = def8(e)
# merubah string silabifikasi menjadi list


#ui

window = Tk()

window.title("Silabifiksi")
window.geometry("550x150")
window.eval("tk::PlaceWindow . center")
window.resizable(False,False)

# label ui
lbl1 = Label(window, text="Diftong\n au = @\n ai = $\n ei = %\n oi = ^")
lbl2 = Label(window, text="Gabungan konsonan\n kh =(\n ng =)\n sy = ~\n ny = +")

lbl1.grid(column=0, row=0)
lbl2.grid(column=1, row=0)

lbl3 = Label(window, text="Input text :")
lbl3.grid(column=0, row=1)

lbl4 = Label(window, text="Kata dasar = ")
lbl4.grid(column=2, row=1)

lbl5 = Label(window, text="Hasil silabifiksi = ")
lbl5.grid(column=2, row=2)

# entry ui
txt0 = Entry(window, width=30)
txt0.grid(column=1, row=1)


txt1 = Entry(window, width=30)
txt1.grid(column=3, row=1)

txt2 = Entry(window, width=30)
txt2.grid(column=3, row=2)

#fungsi bila tombol di tekan
def clicked():
	txt1.delete(0,"end")
	txt2.delete(0,"end")
	a1 = str(txt0.get())
	b1 = [def1(a1)]
	b2 = def11(b1)
	txt1.insert(0,b2)
	c1 = def6(b1)
	c2 = def7(c1,b)
	c3 = def8(c2)
	c4 = def11(c3)
	txt2.insert(0,c4)

# tombol ui
btn = Button(window,text="Proses", width=30, command=clicked)
btn.grid(column=0,row=2,columnspan=2)

window.mainloop()