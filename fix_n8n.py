import json

with open(r'c:\Users\Usuario\Downloads\gestion-pagos\n8n_workflow.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for node in data['nodes']:
    if node['type'] == 'n8n-nodes-base.googleSheets' and node['parameters'].get('operation') == 'appendOrUpdate':
        params = node['parameters']
        if 'columns' in params:
            params['columns']['mappingMode'] = 'defineBelow'
            if node['name'] == 'Append or update row in sheet':
                params['columns']['value'] = {
                    "ID": "={{ $json.ID }}",
                    "Estatus del Pago": "={{ $json['Estatus del Pago'] }}",
                    "StatusHistory": "={{ $json.StatusHistory }}",
                    "Motivo de Rechazo": "={{ $json['Motivo de Rechazo'] }}",
                    "Solicitud de Aclaración": "={{ $json['Solicitud de Aclaración'] }}",
                    "Respuesta a Aclaración": "={{ $json['Respuesta a Aclaración'] }}",
                    "Observaciones de Finanzas": "={{ $json['Observaciones de Finanzas'] }}"
                }
            elif node['name'] == 'Append or update row in sheet1':
                params['columns']['value'] = {
                    "ID": "={{ $json.ID }}",
                    "Monto Pagado": "={{ $json['Monto Pagado'] }}",
                    "T/C": "={{ $json['T/C'] }}",
                    "Monto en MXN": "={{ $json['Monto en MXN'] }}",
                    "Banco": "={{ $json['Banco'] }}",
                    "Operación": "={{ $json['Operación'] }}",
                    "Modo pago": "={{ $json['Modo pago'] }}",
                    "N° de factura": "={{ $json['N° de factura'] }}",
                    "Link Factura": "={{ $json['Link Factura'] }}",
                    "Tipo de gasto": "={{ $json['Tipo de gasto'] }}",
                    "Tipo de operación": "={{ $json['Tipo de operación'] }}",
                    "Estatus OC": "={{ $json['Estatus OC'] }}",
                    "Cliente": "={{ $json['Cliente'] }}",
                    "Prestación del bien o servicio": "={{ $json['Prestación del bien o servicio'] }}",
                    "Propuesta": "={{ $json['Propuesta'] }}",
                    "Comprobante de pago": "={{ $json['Comprobante de pago'] }}",
                    "Observaciones de Finanzas": "={{ $json['Observaciones de Finanzas'] }}",
                    "Estatus del Pago": "={{ $json['Estatus del Pago'] }}"
                }

with open(r'c:\Users\Usuario\Downloads\gestion-pagos\n8n_workflow.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
