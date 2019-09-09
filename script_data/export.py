import json
from pprint import pprint

doc_report = '/home/yago/Documentos/hc/desafio_hc/report.json'
doc_response = '/home/yago/Documentos/hc/desafio_hc/response.json'
        
# app_json = json.dumps(doc)
# user_dict = json.loads(app_json)

with open(doc_report) as f:
    data_report = json.load(f)

with open(doc_response) as f:
    data_response = json.load(f)

# for d in data_response:
#     print (d)
#     print (type(d))


lista_report = []
lista_response = []
report_indice = 1
supervisor_indice = 1

def add_report_dict(lista,indice,supervisor_indice):
    
    new_dict = {'model': 'core.report', 
                'pk': indice, 
                'fields': {'author': supervisor_indice, 
                           'message': 'mensagem ' + str(indice), 
                           'supervisors': [supervisor_indice]}}
    lista.append(new_dict)
    
def add_response_dict(lista,indice,supervisor_indice,report_indice):
    
    new_dict1 = {'model': 'core.reportresponse',
                'fields': {'author': supervisor_indice, 
                           'message': 'resposta 1', 
                           'report': report_indice}
               }
    new_dict2 = {'model': 'core.reportresponse', 
                'fields': {'author': supervisor_indice, 
                           'message': 'resposta 2', 
                           'report': report_indice}
               }    
    lista.append(new_dict1)
    lista.append(new_dict2)

for x in range(1,101):
    supervisor_indice +=1
    if (supervisor_indice) > 20:
        supervisor_indice = 1
    add_report_dict(lista_report,x,supervisor_indice)
    
for x in range(1,101):
    supervisor_indice +=1
    if (supervisor_indice) > 20:
        supervisor_indice = 1
    report_indice +=1
    if (report_indice) > 100:
        report_indice = 1
    add_response_dict(lista_response,x,supervisor_indice,report_indice)
    
with open('report_new.json', 'w') as file:
    json.dump(lista_report, file)

with open('response_new.json', 'w') as file:
    json.dump(lista_response, file)
