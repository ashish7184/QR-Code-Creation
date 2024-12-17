#%%
# Import all necessary library
import pandas as pd
from flask import Flask,request
from flask_restful import Api, Resource
from flask_cors import CORS
import pyqrcode
import base64
import png

#%%

app = Flask(__name__)
CORS(app)
# creating an API object
api = Api(app)

class QR_Code_Input_Parameter(Resource):
    def post (self):
        pass
        encoded = request.get_json()  # Get base64 data from API
        #print(encoded)
        #encoded={'Supplier GSTIN': '27AAACT2165J1ZA', 'Supplier UPI ID': 'cushmanpmsi@hsbc', 'Account No': '22352115', 'IFSC': 'HSBC0110002', 'Invoice number': 'h20049502', 'Invoice date': '20/01/2021', 'Total Invoice Value': 33587, 'CGST': 200241, 'SGST': 222127, 'CESS': 124245, 'IGST': 124}

#%%
# Create dataframe and save all values, and create unique variable


        df = pd.DataFrame(list(encoded.items()),columns = ['KEY','Value'])
        for x in df['KEY']:
            if x =='Supplier GSTIN':
                Supplier_GSTIN=df['Value'][0]
            else:
                pass
            if x=='Supplier UPI ID':
                Supplier_UPI_ID=df['Value'][1]
            else:
                pass
            if x =='Account No':
                Account_No=df['Value'][2]
            else:
                pass
            if x=='IFSC':
                IFSC=df['Value'][3]
            else:
                pass
            if x =='Invoice number':
                Invoice_number=df['Value'][4]
            else:
                pass
            if x=='Invoice date':
                Invoice_date=df['Value'][5]
            else:
                pass
            if x =='Total Invoice Value':
                Total_Invoice_Value=df['Value'][6]
            else:
                pass
            if x=='CGST':
                CGST=df['Value'][7]
            else:
                pass
        
            if x=='SGST':
                SGST=df['Value'][8]
            else:
                pass
            if x =='CESS':
                CESS=df['Value'][9]
            else:
                pass
            if x=='IGST':
                IGST=df['Value'][10]
            else:
                pass
            
#%%            

# Applying condition for find correct value, like String and integer        
        
        if type(Supplier_GSTIN)==str:
            pass
        else:
            return("Please Enter Correct Supplier GSTIN in string form ")
        if type(Supplier_UPI_ID)==str:
            pass
        else:
            return("Please Enter Correct Supplier UPI ID in string form ")
        if type(Account_No)==str:
            pass
        else:
            return("Please Enter Correct Account No in string form ")
        if type(IFSC)==str:
            pass
        else:
            return("Please Enter Correct IFSC in string form ")   
        if type(Invoice_number)==str:
            pass
        else:
            return("Please Enter Correct Invoice number in string form ")
        if type(Invoice_date)==str:
            pass
        else:
            return("Please Enter Correct Invoice date in string form ")
        if type(Total_Invoice_Value)==int:
            pass
        else:
            return("Please Enter Correct Total Invoice Value in integer form ")
        if type(CGST)==int:
            pass
        else:
            return("Please Enter Correct CGST in integer form ")
        if type(SGST)==int:
            pass
        else:
            return("Please Enter Correct SGST in integer form ")
        if type(CESS)==int:
            pass
        else:
            return("Please Enter Correct CESS in integer form ")
        if type(IGST)==int:
            pass
        else:
            return("Please Enter Correct IGST in integer form ")
        
#%%        

        input_data="Supplier GSTIN : "+str(Supplier_GSTIN)+"\n\nSupplier UPI ID : "+Supplier_UPI_ID+"\n\nAccount No : "+Account_No +"\n\nIFSC : "+str(IFSC)+"\n\nInvoice Number : "+str(Invoice_number)+"\n\nInvoice Date : {} ".format(Invoice_date)+"\n\nTotal Invoice Value :  Rs."+str(Total_Invoice_Value)+"\n\nCGST : "+str(CGST)+"\n\nSGST : "+str(SGST)+"\n\nIGST : "+str(IGST)+"\n\nCESS : "+str(CESS)
  
        # Generate QR code
        url = pyqrcode.create(input_data)

        # Create and save the svg file naming "myqr.svg"

        #url.png(r'D:\Data Set\myqr.png', scale =3)  # Development Location
        url.png(r"D:\Webservices\python_E_Invoicing_UAT\myqr.png", scale =3)      # Server Location QR Code
        

        #with open(r'D:\Data Set\myqr.png', "rb") as image_file: # Development Location
        with open(r'D:\Webservices\python_E_Invoicing_UAT\myqr.png', "rb") as image_file: # Development Location
            encoded_string = str(base64.b64encode(image_file.read()))
            return (encoded_string)
#%%

api.add_resource(QR_Code_Input_Parameter,'/QR_Code_Input_Parameter')

if __name__ == "__main__":
    app.run(port=5000, debug=True)


