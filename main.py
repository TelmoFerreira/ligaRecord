#https://forum.arduino.cc/index.php?topic=167492.60
#On pycharm console:
#After install->  pip install auto-py-to-exe
#use auto-py-to-exe

# pyinstaller --noconfirm --onefile --windowed --name "ligaRecord" "%userprofile%/PycharmProjects/ligaRecord/main.py"  --icon "%userprofile%\PycharmProjects\ligaRecord\ico.ico"  --distpath %userprofile%/Desktop

import pandas
import PySimpleGUI as sg
import pprint
import time

main_dic = {}
folhas = []

def read_excell(file):
    print(file)
    folhas = pandas.ExcelFile(file)
    for sheet in folhas.sheet_names:
        if sheet != '+':
            excel_data_df = pandas.read_excel(file, sheet_name=sheet)
            excel_data_df = excel_data_df.sort_values('pontos ronda', ascending=False)
            pontos = excel_data_df['pontos ronda'].tolist()
            divida = []
            for p in pontos:
                divida.append(pontos[0] - p)

            main_dic[sheet] = {
                'equipa': excel_data_df['equipa'].tolist(),
                'pontos': pontos,
                'divida': divida,
            }


    print(main_dic)



layout = [
    [sg.Input(key='fileLocation',enable_events=True), sg.FileBrowse('...',target='fileLocation',file_types=(("Text Files", "*.xls"),))]]
window = sg.Window('Liga Record', layout,finalize=True,resizable=True)
DEFAULT_WINDOW_SIZE = window.Size

while True:
    event, values = window.read(timeout=0)
    if event is None:
        break
    if event == "__TIMEOUT__":
        continue
    if event == "fileLocation":
        if len(values['fileLocation']) > 10:
            read_excell(values['fileLocation'])
            break

window.close()





header_list = ['Equipa','Pontos','Divida']
layout2 = [
    [
        [sg.Radio('Geral', 1, enable_events=True)]+[sg.Radio('Ronda 1', 1, enable_events=True)]+[sg.Radio('Ronda 2', 1, enable_events=True)]+[sg.Radio('Ronda 3', 1, enable_events=True)]+[sg.Radio('Ronda 4', 1, enable_events=True)]+[sg.Radio('Ronda 5', 1, enable_events=True)]+
        [sg.Radio('Ronda 6', 1, enable_events=True)]+[sg.Radio('Ronda 7', 1, enable_events=True)]+[sg.Radio('Ronda 8', 1, enable_events=True)]+[sg.Radio('Ronda 9', 1, enable_events=True)]+[sg.Radio('Ronda 10', 1, enable_events=True)]+[sg.Radio('Ronda 11', 1, enable_events=True)]+[sg.Radio('Ronda 12', 1, enable_events=True)],
        [sg.Radio('Ronda 13', 1, enable_events=True)]+[sg.Radio('Ronda 14', 1, enable_events=True)]+[sg.Radio('Ronda 15', 1, enable_events=True)]+[sg.Radio('Ronda 16', 1, enable_events=True)]+[sg.Radio('Ronda 17', 1, enable_events=True)]+[sg.Radio('Ronda 18', 1, enable_events=True)]+
        [sg.Radio('Ronda 19', 1, enable_events=True)]+[sg.Radio('Ronda 20', 1, enable_events=True)]+[sg.Radio('Ronda 21', 1, enable_events=True)]+[sg.Radio('Ronda 22', 1, enable_events=True)]+[sg.Radio('Ronda 23', 1, enable_events=True)]+[sg.Radio('Ronda 24', 1, enable_events=True)],
        [sg.Radio('Ronda 25', 1, enable_events=True)]+[sg.Radio('Ronda 26', 1, enable_events=True)]+[sg.Radio('Ronda 27', 1, enable_events=True)]+[sg.Radio('Ronda 28', 1, enable_events=True)]+[sg.Radio('Ronda 29', 1, enable_events=True)]+
        [sg.Radio('Ronda 30', 1, enable_events=True)]+[sg.Radio('Ronda 31', 1, enable_events=True)]
     ],
    [[sg.Table(values=[],
              display_row_numbers=False,
              key='TABELA',
              headings=header_list,
              auto_size_columns=False,
              alternating_row_color='#82878c',
              enable_events=True,
              col_widths=[50,25,25],
              justification="center",
              num_rows=25)]]
]



def update_table(id):
    dic_key = 'Ronda '+str(id)
    table_data = []
    if id == 0:
        aux = {}
        for each in main_dic:
            ct = 0
            for each_team in main_dic[each]['equipa']:
                equipa = main_dic[each]['equipa'][ct]
                pontos = main_dic[each]['pontos'][ct]
                divida = main_dic[each]['divida'][ct]
                if each_team not in aux:
                    aux[each_team] = {'equipa': each_team, 'pontos':0, 'divida':0}
                aux[each_team]['pontos'] += pontos
                aux[each_team]['divida'] += divida
                ct +=1

        for x in aux:
            table_data.append([aux[x]['equipa'], aux[x]['pontos'], aux[x]['divida']])
            print(aux[x])



    elif dic_key in main_dic:
        x =0
        for each in main_dic[dic_key]['equipa']:
            table_data.append([main_dic[dic_key]['equipa'][x],main_dic[dic_key]['pontos'][x],main_dic[dic_key]['divida'][x]])
            x += 1

    window2.Element('TABELA').Update(values=table_data)





window2 = sg.Window('Liga Record', layout2,finalize=True,resizable=True)
DEFAULT_WINDOW_SIZE = window2.Size

while True:
    event, values = window2.read(timeout=0)
    if event is None:
        break
    if event == "__TIMEOUT__":
        continue

    if type(event) == int:
        update_table(event)




window2.close()