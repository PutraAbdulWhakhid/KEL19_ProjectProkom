from tkinter import*
import tkinter.messagebox as tm
import PySimpleGUI as sg
import pandas as pd

def ok():
    sg.theme('DarkGreen')
    EXCEL_FILE = 'DataPemesan.xlsx'

    df = pd.read_excel(EXCEL_FILE)

    layout= [
    [sg.Text('Masukkan Data Anda: ')],
    [sg.Text('Nama', size=(20,1)), sg.InputText(key='Nama')],
    [sg.Text('No telepon', size=(20,1)), sg.InputText(key='Tlp')],
    [sg.Text('Alamat', size=(20,1)), sg.Multiline(key='Alamat')],
    [sg.Text('Tgl Acara', size=(20,1)),sg.InputText(key='Tgl Acara'),
                                sg.CalendarButton('kalender',target= 'Tgl Acara',format=('%d-%m-%Y'))],
    [sg.Text('Paket yang dipesan', size=(20,1)),sg.Checkbox('Birthday',key='Birthday'),
                                sg.Checkbox('Wedding',key='Wedding'),
                                sg.Checkbox('Prewedding',key='Prewedding'),
                                sg.Checkbox('Photo Product',key='Photo Product'),
                                sg.Checkbox('Year Book',key='Year Book')],
    [sg.Submit(),sg.Exit()]                         
    ]

    window=sg.Window('Form Pemesanan',layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break         
        if (event == 'Submit'):
                text = values['Tlp']
                if text == '':
                        answer = tm.showerror(
                        title='Error',
                        message='Data Anda Belum Valid')
                elif ((len(text)!=12)):
                        answer = tm.askyesno(
                        title='Error',
                        message='Nomor Telepon Harus terisi dengan 12  digit angka')
                else:
                        try:
                                value = int(text)
                                print(f'Integer: {value}')
                                global close
                                df = df.append(values, ignore_index=True)
                                df.to_excel(EXCEL_FILE, index=False)
                                cont = tm.askyesno(
                                title='Jasa Fotografi Kelompok 19',
                                message='Data telah disimpan, untuk informasi lebih lanjut akan kami hubungi melalui nomer telpon yang telah anda inputkan \n\nApakah Anda ingin memesan paket lain')
                                if cont==True:
                                        window.close()
                                elif cont==False:
                                        window.close()
                                        global close
                                        close = "yesplis"
                                        root.quit()
                        except:
                                print("Not Integer")
                                answer = tm.showwarning(
                                title='Error',
                                message='Nomor Telepon Harus terisi')

           
def birthday():
        answer = tm.askokcancel(
        title='Jasa Fotografi Kelompok 19',
        message='====Berikut fasilitas paket Birthday====\nIDR 1.000.000 \nDurasi 6 jam \n1 Fotografer \n1 DVD File Foto (Soft Copy) \n1 Album Foto Landscape Ukuran 20×30 cm \n5 Sheet/10 Halaman   \n\nKlik Ok Untuk lanjut memesan paket Birthday!!!')
        if answer:
            ok()

def wedding():
        answer = tm.askokcancel(
        title='Jasa Fotografi Kelompok 19',
        message='====Berikut fasilitas paket Wedding====\nIDR 5000.000 \nDurasi 1 Hari  \n2 Fotografer \n2 Vidiografer \n2 Album Foto Landscape Ukuran 20×30 cm \n1 DVD File Foto (Soft Copy) \n1 DVD File Video yang diedit 30-60 menit   \n\nKlik Ok Untuk lanjut memesan paket Wedding!!!' )
        if answer:
            ok()

def prewedding():
        answer = tm.askokcancel(
        title='Jasa Fotografi Kelompok 19',
        message='====Berikut fasilitas paket Prewedding====\nIDR 3.000.000 \nDurasi 12 jam \n2 Fotografer  \n1 DVD File Foto (Soft Copy) \n10 Foto edit \nOutdoor Indoor \n2 Foto Cetak 12 R+Bingkai    \n\nKlik Ok Untuk lanjut memesan paket Prewedding!!!' )
        if answer:
            ok()

def photoproduct():
        answer = tm.askokcancel(
        title='Jasa Fotografi Kelompok 19',
        message='====Berikut fasilitas paket  Photo Product====\nIDR 2.000.000 \nDurasi 3 jam \n1 Fotografer \nFile asli (berpa link drive)  \n30 Foto + Semua diedit  \nHard File Ukuran 20×30 cm \n(5 Sheet/10 Halaman )   \n\nKlik Ok Untuk lanjut memesan paket Photo Product!!!' )
        if answer:
            ok()

def yearbook():
        answer = tm.askokcancel(
        title='Jasa Fotografi Kelompok 19',
        message='====Berikut fasilitas paket  Year Book====\nIDR 70.000/orang \nDurasi 6 jam/40 orang \n1 Fotografer \nFoto individu, kelas, angkatan \n1 Hard file buku 50 halaman (Ukuran 30×20 cm) \nBonus totebag+softfile foto  \n\nKlik Ok Untuk lanjut memesan paket Year Book!!!' )
        if answer:
            ok()


def main():
  
    global root
    root= Tk()
    root.title("Fotografi Kelompok 19")
    root.config(background="DarkGreen")


    l1=Label(text="Pilih paket yang anda pilih",bg="lightyellow",
         font="Normal 10")
    l1.grid(row=0,column=0,columnspan=4,pady=20,padx=30)



    b1= Button(text="Birthday",activebackground="lightblue",
            bd=5, relief=RIDGE,font="Normal 10",width=10,command=birthday)
    b1.grid(row=1,column=0)
    b2= Button(text="Wedding",activebackground="lightblue",
            bd=5, relief=RIDGE,font="Normal 10",width=10,command=wedding)
    b2.grid(row=1,column=1)
    b3= Button(text="Prewedding",activebackground="lightblue",
            bd=5, relief=RIDGE,font="Normal 10",width=10,command=prewedding)
    b3.grid(row=1,column=2)
    b4= Button(text="Photo Product",activebackground="lightblue",
            bd=5, relief=RIDGE,font="Normal 10",width=10,command=photoproduct)
    b4.grid(row=1,column=3)
    b5= Button(text="Year Book",activebackground="lightblue",
            bd=5, relief=RIDGE,font="Normal 10",width=10,command=yearbook)
    b5.grid(row=1,column=4)
  
    root.mainloop()
    
main()



