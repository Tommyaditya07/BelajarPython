import pandas as pd
import PySimpleGUI as sg

sg.theme('DarkTeal12')

EXCEL_FILE = "absensi_mahasiswa1.xlsx"
df = pd.read_excel(EXCEL_FILE)

path_logo = 'logo.png'

layout = [
    [sg.Text('', size=(20, 1))],
    [sg.Col([[sg.Image(filename=path_logo, size=(399, 115), key='Logo')]], element_justification='center')],
    [sg.Text('', size=(20, 1))],
    [sg.Text('NIM', size=(15, 1)), sg.InputText(key='NIM')],
    [sg.Text('Nama', size=(15, 1)), sg.InputText(key='NAMA')],
    [sg.Text('Prodi', size=(15, 1)), sg.InputText(key='PRODI')],
    [sg.Text('Kode Kelas', size=(15, 1)), sg.InputText(key='KODE KELAS')],
    [sg.Text('Tanggal', size=(15, 1)), sg.InputText(key='TANGGAL'),
                                    sg.CalendarButton('Kalender', target='TANGGAL', format=('%d-%m-%Y'))],
    [sg.Text('Status', size=(15, 1)), sg.Radio('Hadir', 'Status', key='Hadir', default=True),
                                    sg.Radio('Tidak Hadir', 'Status', key='Tidak Hadir')],
    [sg.Submit(button_color=('white', 'green')), sg.Button('Clear', button_color=('white', 'red')), sg.Exit(button_color=('white', 'darkblue'))],
    [sg.Text('', size=(40, 1), key='StatusText')],
    [sg.Text('', size=(80, 1), key='MarqueeText', justification='center', text_color='white', background_color='darkblue')],
]

window = sg.Window('ABSENSI MAHASISWA KELOMPOK 3', layout, font=('Helvetica', 14, 'bold'))

def clear_input():
    for key in values:
        if key != 'Kalender':
            window[key]('')
    return None

marquee_text = "- Dasar Pemrograman - Kelompok 3 " * 10
marquee_index = 10

while True:
    event, values = window.read(timeout=200)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'Clear':
        clear_input()
        window['StatusText'].update('Formulir telah direset', text_color='white')

    elif event == 'Submit':
        # Pemilihan status hadir/tidak
        status = 'Hadir' if values['Hadir'] else 'Tidak Hadir'

        # Membuat data baru
        new_data = {
            'Nama': values['NAMA'],
            'NIM': values['NIM'],
            'PRODI': values['PRODI'],
            'Kode Kelas': values['KODE KELAS'],
            'Tanggal': values['TANGGAL'],
            'Status': status
        }

        # Menambahkan data baru ke DataFrame
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)

        window['StatusText'].update('Data berhasil disimpan', text_color='green')
        sg.popup('Data Berhasil di Simpan')
        clear_input()

    # Update teks berjalan
    window['MarqueeText'].update(marquee_text[marquee_index:marquee_index+80])
    marquee_index = (marquee_index + 1) % len(marquee_text)

window.close()
