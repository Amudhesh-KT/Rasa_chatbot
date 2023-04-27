import requests
import xmltodict
import json
from flatten_json import flatten

url = 'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV/A_PurchaseRequisitionHeader'
username = 'K1277'
password = 'Kaar@1234'
# Create a session and set the authorization header
session = requests.Session()
session.auth = (username, password)


def prlist():
    api_address = 'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV/A_PurchaseRequisitionHeader'
    # city = input('Enter the City Name :')
    url = api_address
    xml_data = session.get(url)
    obj = xml_data.content
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    values = js_obj['feed']['entry']
    prnumber = []
    for i in values:
        prnumber.append(
            f"PR {i['content']['m:properties']['d:PurchaseRequisition']}")
    return prnumber


def polist():
    api_address = 'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder'
    url = api_address
    xml_data = session.get(url)
    obj = xml_data.content
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    values = js_obj['feed']['entry']
    ponumber = []
    for i in values:
        ponumber.append(
            f"PO {i['content']['m:properties']['d:PurchaseOrder']}")
    return ponumber


def pritems(prno):
    api_address = f'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV/A_PurchaseRequisitionHeader(\'{prno}\')?$expand=to_PurchaseReqnItem'
    url = api_address
    response = session.get(url)
# Print the response status code and content
    obj = response.content
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    flatjs = flatten(js_obj)
    itemlist = []
    i = 0
    while True:
        try:
            itemlist.append(
                f"PR Item {flatjs[f'entry_link_1_m:inline_feed_entry_{i}_content_m:properties_d:PurchaseRequisitionItem']}")
            i += 1
        except:
            break
    return itemlist


def poitems(pono):
    api_address = f'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrder(\'{pono}\')?$expand=to_PurchaseOrderItem'
# city = input('Enter the City Name :')
    url = api_address
    xml_data = session.get(url)
    obj = xml_data.content  
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    flatjs = flatten(js_obj)
    itemlist = []
    i = 0
    while True:
        try:
            itemlist.append(
                f"PO Item {flatjs[f'entry_link_1_m:inline_feed_entry_{i}_content_m:properties_d:PurchaseOrderItem']}")
            i += 1
        except:
            break
    return itemlist


def pritemdetails(prno, pritemno):
    print(prno, pritemno)
    api_address = f'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEREQ_PROCESS_SRV/A_PurchaseRequisitionItem(PurchaseRequisition=\'{prno}\',PurchaseRequisitionItem=\'{pritemno}\')'
    url = api_address
    response = session.get(url)
# Print the response status code and content
    obj = response.content
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    flatjs = flatten(js_obj)
    desc = {}
    desc['Purchase_Requisition_Number'] = flatjs['entry_content_m:properties_d:PurchaseRequisition']
    desc['Purchase_Requisition_Item_Number'] = flatjs['entry_content_m:properties_d:PurchaseRequisitionItem']
    desc['Purchase_Requisition_Release_Status'] = flatjs['entry_content_m:properties_d:PurReqnReleaseStatus']
    desc['Purchase_Requisition_Item_Text'] = flatjs['entry_content_m:properties_d:PurchaseRequisitionItemText']
    desc['Purchase_Requisition_Material_Group'] = flatjs['entry_content_m:properties_d:MaterialGroup']
    desc['Requested_Quantity'] = flatjs['entry_content_m:properties_d:RequestedQuantity']
    desc['Base_Unit'] = flatjs['entry_content_m:properties_d:BaseUnit']
    desc['Purchase_Requisition_Price'] = flatjs['entry_content_m:properties_d:PurchaseRequisitionPrice']
    desc['Plant'] = flatjs['entry_content_m:properties_d:Plant']
    desc['Company_Code'] = flatjs['entry_content_m:properties_d:CompanyCode']
    desc['Processing_Status'] = flatjs['entry_content_m:properties_d:ProcessingStatus']
    desc['Delivery_Date'] = flatjs['entry_content_m:properties_d:DeliveryDate']
    desc['Creation_Date'] = flatjs['entry_content_m:properties_d:CreationDate']
    return desc

def poitemdetails(pono, poitemno):
    api_address = f'http://61.16.128.69:8002/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV/A_PurchaseOrderItem(PurchaseOrder=\'{pono}\',PurchaseOrderItem=\'{poitemno}\')'
    url = api_address
    response = session.get(url)
# Print the response status code and content
    obj = response.content
    objstr = str(obj, 'UTF-8')
    obj2 = xmltodict.parse(objstr)
    js = json.dumps(obj2)
    js_obj = json.loads(js)
    flatjs = flatten(js_obj)
    desc = {}
    desc['Purchase_Order_Number'] = flatjs['entry_content_m:properties_d:PurchaseOrder']
    desc['Purchase_Order_Item_Number'] = flatjs['entry_content_m:properties_d:PurchaseOrderItem']
    desc['Purchase_Order_Quantity'] = flatjs['entry_content_m:properties_d:OrderQuantity']
    desc['Purchase_Order_Item_Text'] = flatjs['entry_content_m:properties_d:PurchaseOrderItemText']
    desc['Purchase_Order_Material_Group'] = flatjs['entry_content_m:properties_d:MaterialGroup']
    desc['Item_Net_Weight'] = flatjs['entry_content_m:properties_d:ItemNetWeight']
    desc['Item_Weight_Unit'] = flatjs['entry_content_m:properties_d:ItemWeightUnit']
    desc['Purchase_Order_Price'] = flatjs['entry_content_m:properties_d:NetPriceAmount']
    desc['Currency'] = flatjs['entry_content_m:properties_d:DocumentCurrency']
    desc['Plant'] = flatjs['entry_content_m:properties_d:Plant']
    desc['Purchase_Requisition_Number'] = flatjs['entry_content_m:properties_d:PurchaseRequisition']
    desc['Purchase_Requisition_Item_Number'] = flatjs['entry_content_m:properties_d:PurchaseRequisitionItem']
    
    return desc


# def prdelete(prno):
#     api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
#     # city = input('Enter the City Name :')
#     url = api_address + prno
#     json_data = requests.get(url).json()
#     format_add = json_data['main']
#     print(format_add)
#     # print("Weather is {0} Temperature is mininum {1} Celcius and maximum is {2} Celcius".format(
#     #     json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
#     return format_add
