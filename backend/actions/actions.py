# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import datetime as dt
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from actions.api import prlist, pritems, pritemdetails, polist, poitems, poitemdetails

prno = ""
pritemno = ""
pono = ""
poitemno = ""

# def clear_global_variable_pr():
#     global prno
#     prno = None
#     global pritemno
#     pritemno = None

# def clear_global_variable_po():
#     global pono
#     pono = None
#     global poitemno
#     poitemno = None


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_show_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []


class ActionCompanyPolicy(Action):
    def name(self) -> Text:
        return "action_company_policy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        policies = [
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/ESi_WHpAvMxGjlr_bh1f8Q0B3sA-bvcA2MOVpvrlOn2Pww?e=Wxln2N",
                "tag": "Corporate attire policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EYx8kvvCRpRAkurURg-yj2kB5xQSSg4a80GBF17us8-LZg?e=aTc8f0",
                "tag": "Over-time policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EZg_FFmCnPdHhAKGUJHR1goBesQgE1-1biuchTx0bVps2w?e=TlYUHv",
                "tag": "Leave policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EYWZDRBdlKpLtZUOcFhZP28BqbdauU7cQmYlShDnmU5cOA?e=042DZo",
                "tag": "Probation policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EUhpOqfZy2tJgz2yahSHUgABOHXhOT-_xhzypM9n7I3vxw?e=hVMbGG",
                "tag": "Travel policy",
            },
            {
                "link": "httpshttps://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EYgbC92aDftBpQuSK5y-yXMBBXvboXfZYciY7aWbIcS1yg?e=Fy7OKD",
                "tag": "Additional billing hours policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EUSF6ead6W9Pp5OeW7rrNaYB1oj9HBbsh6-W0_Im2RLssw?e=Q5ovc8",
                "tag": "Expense management system policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20FTF%20Buckets%20Policy.pdf?csf=1&web=1&e=BYTeTJ",
                "tag": "Kaar FTF Bucket policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EVtNosoO381Bu5t4A5BsT8sBrog2CRJFJ44lOidcb7-c5g?e=Ti2zHk",
                "tag": "KICC policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EQCFToagM5lFmddEuUC-U14BrdJUICBfWFwwHnEx6Lih-Q?e=yupAcJ",
                "tag": "Reimbursement policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EXI8zU3Kj2pOjYrEH44qPqkBiy-GFNxEcZuJ87tYMEBXEg?e=T7l4zp",
                "tag": "Interview panel policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EaB7MyQOKwlLhrJH7fJhrPQBwD_74V4wnC7IGXtjETThDQ?e=vip6P9",
                "tag": "WFH policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/ER40ujNgMQpBlLIqY6AviiQBITsG_LdmHawXyDoZlPku7Q?e=KFolru",
                "tag": "Appraisal policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/Eac-zip92x5Lq1TVkL2-ZlkB0xyna0mZVzRG0iChVTUO7A?e=QnV6Ae",
                "tag": "Certification policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EdlLrrAywrNArTomqtnoymkBv-OPnqHruO2zXDCuZNvpTg?e=FecsJF",
                "tag": "Deputation policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EfYFr4748h5IpwUHl2qcjNABb4P8sqc0HUfG2_qaaIHVfw?e=b3Bfh0",
                "tag": "Training policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EZySyUPBZ5tLhhLDQkdmlrYBogz656RfcwU1SbNFXPjByQ?e=fc7bC3",
                "tag": "Working hours policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EUbZHQJAFhxGvU3clYsRSrwBLmKrqfGTLwRn-cPuqUoX-A?e=FjeReg",
                "tag": "Employee soft loan policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EeSvQDCEKCRGpPro9DRcwT8BS95YaCBjQY66mrWJq29ApQ?e=mecyro",
                "tag": "Laptop damage policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EQOzE6LeEdRMrWMV6iumfj0BfBXXLGApSp6Nm7xhHIOaaA?e=4X1Jy3",
                "tag": "Odd hour commute policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/ETNzjOR1pYpIkTDb_oTrQUMBIlev7ka8FXnUdjh-CFDI0A?e=1QbpRK",
                "tag": "Performance appraisal policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EUe8vFJY4DZCtJgkLLWbNU0Boj6jJ5xL7_2WeRQjcy2M_Q?e=LwdOrq",
                "tag": "R and R policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/EYklvdFgu9RIn559g0hOOjsBEpFG5udHA6V97cPojtPWKA?e=7h7Al9",
                "tag": "Timesheet policy",
            },
            {
                "link": "https://kaartechit-my.sharepoint.com/:b:/g/personal/damudhesh_kaartech_com/Ef3_SJq93ClNoroJINdmpKIB-5Kjz28Q_NKtjTWgdP_iCQ?e=rbdKgt",
                "tag": "Remote working policy",
            },
        ]

        send = {"links": policies, "msg": "The Company Policies are.."}
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionPRList(Action):
    def name(self) -> Text:
        return "action_pr_list"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        prlists = prlist()
        prlists = prlists[:50]
        # dispatcher.utter_template("utter_givepr",tracker,temp=prlists)
        # message = f"The list of PR's are: {prlists}. Choose a PR Number to display its items"
        send = {
            "requests": prlists,
            "msg": "The PR lists are given below. Choose Any one to see PR Items",
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        # dispatcher.utter_message(text=prlists)
        # dispatcher.utter_message(text=f"Your pr number is {pr_num}!")

        return []


class ActionPOList(Action):
    def name(self) -> Text:
        return "action_po_list"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        polists = polist()
        polists = polists[450:500]
        # dispatcher.utter_template("utter_givepr",tracker,temp=prlists)
        # message = f"The list of PR's are: {prlists}. Choose a PR Number to display its items"
        send = {
            "requests": polists,
            "msg": "The PO lists are given below. Choose Any one to see PO Items",
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        # dispatcher.utter_message(text=prlists)
        # dispatcher.utter_message(text=f"Your pr number is {pr_num}!")

        return []


# class ActionPRNumber(Action):

#     def name(self) -> Text:
#         return "action_pr_number"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         prlists = prlist()
#         prlists = prlists[:10]
#         # dispatcher.utter_template("utter_givepr",tracker,temp=prlists)
#         message = f"The list of PR's are: {prlists}. Choose a PR Number to display its items"
#         dispatcher.utter_message(text=message)
#         # dispatcher.utter_message(text=f"Your pr number is {pr_num}!")

#         return []


class ActionPRitems(Action):
    def name(self) -> Text:
        return "action_pr_items"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        global prno
        prnotext = tracker.latest_message["text"]
        prno = prnotext.split()[-1]
        # prno = prnotext
        # prno = tracker.get_slot("prnumber")
        pritemslist = pritems(prno)
        pritemslist = pritemslist[:50]
        # dispatcher.utter_template("utter_givepr",tracker,temp=prlists)
        # message = f"The list of PR's items are: {pritemslist}. Choose Any one to see the description.."
        # dispatcher.utter_message(text=message)

        send = {
            "requests": pritemslist,
            "msg": "The PR items lists are given below. Choose Any one to see the Item description",
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)


class ActionPOitems(Action):
    def name(self) -> Text:
        return "action_po_items"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        global pono
        ponotext = tracker.latest_message["text"]
        pono = ponotext.split()[-1]
        print(pono)
        # prno = prnotext
        # prno = tracker.get_slot("prnumber")
        poitemslist = poitems(pono)
        poitemslist = poitemslist[:50]
        # dispatcher.utter_template("utter_givepr",tracker,temp=prlists)
        # message = f"The list of PR's items are: {pritemslist}. Choose Any one to see the description.."
        # dispatcher.utter_message(text=message)

        send = {
            "requests": poitemslist,
            "msg": "The PO items lists are given below. Choose Any one to see the Item description",
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)


class ActionPRitemDesc(Action):
    def name(self) -> Text:
        return "action_pr_item_desc"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # prno=tracker.latest_message['text']
        # prno = '10000640'
        # pritemno = '220'
        # prno = tracker.get_slot('other_slot')
        global pritemno, prno
        pritemnotext = tracker.latest_message["text"]
        pritemno = pritemnotext.split()[-1]
        print(prno)
        print(pritemno)
        pritemdesc = pritemdetails(prno, pritemno)
        print(pritemdesc)
        for i in pritemdesc.keys():
            if i == "Purchase_Requisition_Number":
                PRnumber = pritemdesc[i]
            elif i == "Purchase_Requisition_Item_Number":
                PRItemNumber = pritemdesc[i]
            elif i == "Purchase_Requisition_Release_Status":
                PRItemStatus = pritemdesc[i]
            elif i == "Purchase_Requisition_Item_Text":
                PRItemText = pritemdesc[i]
            elif i == "Purchase_Requisition_Material_Group":
                PRMaterialGroup = pritemdesc[i]
            elif i == "Requested_Quantity":
                PRQuantity = pritemdesc[i]
            elif i == "Base_Unit":
                PRBaseUnit = pritemdesc[i]
            elif i == "Purchase_Requisition_Price":
                PRPrice = pritemdesc[i]
            elif i == "Plant":
                PRPlant = pritemdesc[i]
            elif i == "Company_Code":
                PRCompanyCode = pritemdesc[i]
            elif i == "Processing_Status":
                PRProcessingStatus = pritemdesc[i]
            elif i == "Delivery_Date":
                PRDeliveryDate = pritemdesc[i]
            elif i == "Creation_Date":
                PRCreationDate = pritemdesc[i]

        if PRItemStatus == "01":
            status = "Saved, not yet released"
        elif PRItemStatus == "02":
            status = "Released"
        elif PRItemStatus == "03":
            status = "Partially ordered"
        elif PRItemStatus == "04":
            status = "Completely ordered"
        elif PRItemStatus == "05":
            status = "Deleted"
        elif PRItemStatus == "06":
            status = "Manually set to Closed"
        elif PRItemStatus == "07":
            status = "Technically completed"
        elif PRItemStatus == "08":
            status = "Manually set to Locked"
        elif PRItemStatus == "09":
            status = "Sent"
        elif PRItemStatus == "10":
            status = "Partially invoiced"
        elif PRItemStatus == "11":
            status = "Completely invoiced"
        elif PRItemStatus == "12":
            status = "Manually set to Archived"

        if PRProcessingStatus == "N":
            Pstatus = "Not edited"
        elif PRProcessingStatus == "B":
            Pstatus = "PO created"
        elif PRProcessingStatus == "A":
            Pstatus = "RFQ created"
        elif PRProcessingStatus == "K":
            Pstatus = "Contract created"
        elif PRProcessingStatus == "L":
            Pstatus = "Scheduling aggrement created"
        elif PRProcessingStatus == "S":
            Pstatus = "Service entry sheet created"
        elif PRProcessingStatus == "D":
            Pstatus = "Deployment STR"
        elif PRProcessingStatus == "E":
            Pstatus = "RFQ sent to external system for sourcing"

        new_line = "\n"
        details = {
            "Purchase Requisition Number": PRnumber,
            "Purchase Requisition Item Number": PRItemNumber,
            "Purchase_Requisition_Release_Status": f"{ PRItemStatus} - {status}",
            "Purchase Requisition Item Text": PRItemText,
            "Purchase_Requisition_Material_Group": PRMaterialGroup,
            "Requested_Quantity": PRQuantity,
            "Base_Unit": PRBaseUnit,
            "Purchase_Requisition_Price": PRPrice,
            "Plant": PRPlant,
            "Company_Code": PRCompanyCode,
            "Processing_Status": f"{PRProcessingStatus} - {Pstatus}",
            "Creation_Date": PRCreationDate,
            "Delivery_Date": PRDeliveryDate,
        }
        # dispatcher.utter_message(text=message)
        send = {
            "msg": "Here is the Details of Purchase Requisition... ",
            "details": details,
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        # clear_global_variable_pr()
        return []


class ActionPOitemDesc(Action):
    def name(self) -> Text:
        return "action_po_item_desc"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # prno=tracker.latest_message['text']
        # prno = '10000640'
        # pritemno = '220'
        # prno = tracker.get_slot('other_slot')
        global pono, poitemno
        print(pono)
        poitemnotext = tracker.latest_message["text"]
        poitemno = poitemnotext.split()[-1]

        print(poitemno)
        poitemdesc = poitemdetails(pono, poitemno)
        print(poitemdesc)
        for i in poitemdesc.keys():
            if i == "Purchase_Order_Number":
                POnumber = poitemdesc[i]
            elif i == "Purchase_Order_Item_Number":
                POItemNumber = poitemdesc[i]
            elif i == "Purchase_Order_Quantity":
                POQuantity = poitemdesc[i]
            elif i == "Purchase_Order_Item_Text":
                POItemText = poitemdesc[i]
            elif i == "Purchase_Order_Material_Group":
                POMaterialGroup = poitemdesc[i]
            elif i == "Item_Net_Weight":
                POItemweight = poitemdesc[i]
            elif i == "Item_Weight_Unit":
                POWeightunit = poitemdesc[i]
            elif i == "Purchase_Order_Price":
                POPrice = poitemdesc[i]
            elif i == "Currency":
                POCurrency = poitemdesc[i]
            elif i == "Plant":
                POPlant = poitemdesc[i]
            elif i == "Purchase_Requisition_Number":
                PRnumber = poitemdesc[i]
            elif i == "Purchase_Requisition_Item_Number":
                PRItemNumber = poitemdesc[i]

        details = {
            "Purchase Order Number": POnumber,
            "Purchase Order Item Number": POItemNumber,
            "Purchase Order Quantity": POQuantity,
            "Purchase Requisition Item Text": POItemText,
            "Material Group": POMaterialGroup,
            "Item Net Weight": POItemweight,
            "Item Weight Unit": POWeightunit,
            "Purchase_Order_price": POPrice,
            "Currency": POCurrency,
            "Plant": POPlant,
            "Purchase Requisition Number": PRnumber,
            "Purchase Requisition Item Number": PRItemNumber,
        }
        # dispatcher.utter_message(text=message)
        send = {
            "msg": "Here is the Details of Purchase Requisition... ",
            "details": details,
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        # clear_global_variable_po()
        return []


# POLICIES#
class ActionCorporateAttirePolicy(Action):
    def name(self) -> Text:
        return "action_corporateattirepol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Corporate Attire Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Corporate%20Attire%20Policy.pdf?csf=1&web=1&e=nhNR98",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionOvertimePolicy(Action):
    def name(self) -> Text:
        return "action_over-timepol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Overtime Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Overtime%20Policy.pdf?csf=1&web=1&e=gy7927",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionLeavePolicy(Action):
    def name(self) -> Text:
        return "action_leavepol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Leave Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Overtime%20Policy.pdf?csf=1&web=1&e=gy7927",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionProbationPolicy(Action):
    def name(self) -> Text:
        return "action_probationpol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Probation Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Leave%20Policy%20-%20India.pdf?csf=1&web=1&e=h6mBdS, Others- https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Leave%20Policy.pdf?csf=1&web=1&e=hres42",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionTravelPolicy(Action):
    def name(self) -> Text:
        return "action_travelpol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Travel Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Travel%20Policy.pdf?csf=1&web=1&e=ia4gK9",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class Actionaddlbillinghourspolicies(Action):
    def name(self) -> Text:
        return "action_addlbillinghrspol"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Additional Billing Hours Policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Additional%20Billing%20Hours%20Policy%20-%20UK%202.0.pdf?csf=1&web=1&e=i373nJ",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionexpensemgmtsystemPolicy(Action):
    def name(self) -> Text:
        return "action_expensemgmtsystem"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Expense management system policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Expenses%20Management%20System%20Policy.pdf?csf=1&web=1&e=Hwue5A",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionFTFBucketsPolicy(Action):
    def name(self) -> Text:
        return "action_ftfbucketspolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "tag": "Kaar FTF Bucket policy",
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20FTF%20Buckets%20Policy.pdf?csf=1&web=1&e=BYTeTJ",
                }
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionInternalComplaintsCommitteePolicy(Action):
    def name(self) -> Text:
        return "action_InternalComplaintsCommitteePolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Internal%20Complaints%20Committee%20Policy.pdf?csf=1&web=1&e=mGiNwo",
                    "tag": "KICC policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionReimbursementsPolicy(Action):
    def name(self) -> Text:
        return "action_ReimbursementsPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Reimbursement%20Policy%20.pdf?csf=1&web=1&e=5N5YJu",
                    "tag": "Reimbursement policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)

        return []


class ActionInterviewPanelPolicy(Action):
    def name(self) -> Text:
        return "action_InterviewPanelPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Kaar%20Virtual%20Interview%20Panel%20Policy.pdf?csf=1&web=1&e=ecDx6s",
                    "tag": "Interview panel policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionWFHPolicy(Action):
    def name(self) -> Text:
        return "action_WFHPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20%20-%20WFH%20Policy.pdf?csf=1&web=1&e=s9jfRN",
                    "tag": "WFH policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionAppraisalPolicy(Action):
    def name(self) -> Text:
        return "action_AppraisalPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Appraisal%20Policy.pdf?csf=1&web=1&e=qzEmnc",
                    "tag": "Appraisal policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionCertificationPolicy(Action):
    def name(self) -> Text:
        return "action_CertificationPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Certification%20Policy.pdf?csf=1&web=1&e=nqvkXE",
                    "tag": "Certification policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionDeputationPolicy(Action):
    def name(self) -> Text:
        return "action_DeputationPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Deputation%20Policy.pdf?csf=1&web=1&e=jleXgV",
                    "tag": "Deputation policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionTrainingPolicy(Action):
    def name(self) -> Text:
        return "action_TrainingPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Training%20Policy.pdf?csf=1&web=1&e=BwcyK9",
                    "tag": "Training policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionWorkingHoursPolicy(Action):
    def name(self) -> Text:
        return "action_WorkingHoursPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20-%20Working%20Hours%20Policy.pdf?csf=1&web=1&e=U3hSrn",
                    "tag": "Working hours policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionEmployeeSoftLoanPolicy(Action):
    def name(self) -> Text:
        return "action_EmployeeSoftLoanPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20Employee%20Soft%20Loan%20Policy.pdf?csf=1&web=1&e=3OpGGF",
                    "tag": "Employee soft loan policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionLaptopDamagePolicy(Action):
    def name(self) -> Text:
        return "action_LaptopDamagePolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/KaarTech%20Laptop%20Damage%20Policy.pdf?csf=1&web=1&e=uujQca",
                    "tag": "Laptop damage policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionOddHourCommutePolicy(Action):
    def name(self) -> Text:
        return "action_OddHourCommutePolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Odd%20Hour%20Commute%20Policy.pdf?csf=1&web=1&e=dyTnnA",
                    "tag": "Odd hour commute policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionPerformanceAppraisalPolicy(Action):
    def name(self) -> Text:
        return "action_PerformanceAppraisalPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Performance%20Appraisal%20Policy%202.0.pdf?csf=1&web=1&e=26GAVq",
                    "tag": "Performance appraisal policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionRewardsandRecognitionPolicy(Action):
    def name(self) -> Text:
        return "action_RewardsandRecognitionPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/R%20%26%20R%20Policy.pdf?csf=1&web=1&e=vZbdDu",
                    "tag": "Rewards and Recognition policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionTimesheetPolicy(Action):
    def name(self) -> Text:
        return "action_TimesheetPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Timesheet%202.0%20Policy.pdf?csf=1&web=1&e=sGAPY3",
                    "tag": "Timesheet policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


class ActionRemoteworkingPolicy(Action):
    def name(self) -> Text:
        return "action_RemoteworkingPolicy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        send = {
            "links": [
                {
                    "link": "https://kaartechit-my.sharepoint.com/:b:/r/personal/damudhesh_kaartech_com/Documents/Documents/Kaar_policies/POLICIES/Remote%20WorX%20Policy.pdf?csf=1&web=1&e=aemqla",
                    "tag": "Remote working policy",
                },
            ]
        }
        my_json = json.dumps(send)
        dispatcher.utter_message(text=my_json)
        return []


# POLICIES#
