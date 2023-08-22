import random
import pandas as pd
import getindianname as name

id= [f'PAT_00{i}' for i in range(1,101)]
ran_name_g= [name.randname() for i in range(int(100))]
ran_age= [random.randint(5,95) for i in range(int(100))]

class Patient:
    def __init__(self, mobile_no,address, treatment,doc_name,inspection1, inspection2,ongoing_inspection,medicines,patients_preacutions):
        self.mobile_no= mobile_no
        self.address= address
        self.treatment = treatment
        self.doc_name=doc_name
        self.inspection1= inspection1
        self.inspection2= inspection2
        self.ongoing_inspection= ongoing_inspection
        self.medicines= medicines
        self.patients_preactions= patients_preacutions
        
def generate_details():
 
    try:
        def mobile_number(mob):
            try:
                series= '+91' + random.choice(mob)
                number= ''.join(random.choice(['0','1','2','3','4','5','6','7','8']) for i in range(9))
                return series + number
            except Exception as e:
                print(f'Error occurs in mpbile number:{str(e)}')

        mob= ['9','8','7']
        Mobileno_= mobile_number(mob) 
    
        def address_generation(city,street,code):
            try:
                city_= random.choice(city)
                street_= random.choice(street)
                code_=random.choice(code)
                return city_ + ' ' +street_ + ' ' + code_
            except Exception as e:
                print(f'Error occours in address generation: {str(e)}')

        city= ['Nagpur','Pune', 'Mumbai','Nashik','Delhi','Amravati','Raipur']
        street= ['Gandi nagar', 'Sarojni chowk','Ambedkar road','Shankar nagar','MJ road', 'Shivaji nagar','RSVP road','VCA chowk']
        code= ['440825','429086','551867','624428','427188','428179','629177','472878','427820','529876','692782','544211']
        address_=address_generation(city, street,code) 
        
        def medical_treatment(med):
            try:
                med_= random.choice(med)
                return med_
            except Exception as e:
                print(f'Error occurs in medical treatment: {str(e)}')
    
        med= ['Laser Eye Operation','Hyperglycaemia (high blood sugar)','Bipolar disorder','Down syndrome','Kidney infection', 
                    'kidney stone','Chest infection','Atopic eczema' ,'Alzheimer disease','Botox Treatment(lip Fealing)','Hemmoroids', 
                    'Rabies imnunization schedule','Liver disease','Malaria','Meniere disease','Pneumonia', 'Rhabdomyosarcoma',
                    'epistaxis cautery Treatment(nose bleed)','Chronic kidney disease','Constipation','Food poisoning','Gastroenteritis'
                    'Cardio Obstructive Pulmonary Disease', 'Chest pain','Chickenpox','Therapeutic angioplasty','Asthma','Sore throat']
        medical_=medical_treatment(med) 
        
        
        def doct_g(doct_name):
            try:
                doct_name_= random.choice(doct_name)             
                return doct_name_
            except Exception as e:
                print(f' Error occurs in doctor name: {str(e)}')
    
        doct_name=['Dr.Anshuman Roy','Dr.Shivani Gour','Dr.Arvind Kumar','Dr.Ajay Roy','Dr.Sharath Reddy','Dr. Srinivas Reddy', 'Dr. Minakshi MAnchanda',
                'Dr.Kaushik Bhattacharya','Dr.Priyanks Sarangi','Dr.Shefali Sharma','Dr.Mayank Bansal','Dr. Mamta Singh','Dr.Singh',
                'Dr.Deepak Varshey','Dr.Kamal Verma','Dr. Sudhir Kumar Orthopaedics','Dr. Sudhir Kumar ', 'Dr.Smiriti Pandey',  'Dr. Shilpa Gupta',
                'Dr. Riya Chaturvedi','Dr.Anshul D','Dr.V K Bahl','Dr. Manish Nanda', 'Dr.shilpa Thakur','Dr.Ashok Kumar',
                'Dr. R.Madhwan','Dr.Shreya H. Rai', 'Dr.Parth G', 'Dr.Raghini Khanna']
        doctor_=doct_g(doct_name) 
        
        
        def insepction_date1(date1,month1,year1):
            try:
                year_1 = random.choice(year1)
                month_1 ='/'+ random.choice(month1)
                date_1 = '/'+random.choice(date1)

                return year_1  + month_1 + date_1
            except Exception as e:
                print(f'Error occurs in inspection date 1: {str(e)}')
        date1=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27',
              '28','29','30']
        month1=['1','2','3']
        year1=['2023']
        first_=insepction_date1(date1, month1, year1) 
        
        def insepction_date2(date2,month2,year2):
            try:
                year_2 = random.choice(year2)
                month_2 ='/'+ random.choice(month2)
                date_2 = '/'+ random.choice(date2)

                return year_2 + month_2 + date_2
            except Exception as e :
                print(f'Error occurs in inspection date 2: {str(e)}')
           
        date2=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27',
                    '28','29','30']
        month2=['4','5','6']
        year2=['2023']
        second_=insepction_date2(date2, month2, year2) 
        
        
        def og(x):
            try:
                og1= random.choice(x)
                return og1
    
            except Exception as e:
                print(f'Error Occurs in ongoing Inspection: {str(e)}')

        x= ['Processing','completed']
        ongoing = og(x) 
        
        def medi(medicine1,medicine2,medicine3,medicine4):
            try: 
                tablets_1= random.choice(medicine1)
                tablets_2= random.choice(medicine2)
                tablets_3= random.choice(medicine3)
                tablets_4= random.choice(medicine4)
                return tablets_1 +' ,' + tablets_2 +', ' + tablets_3+ ' ,' + tablets_4
            except Exception as e:
                print(f'Error occurs in medicines: {str(e)}')
            

        medicine1= 'Diclofenac', 'Aspirin', 'Azithromycin', 'Amoxicillin', 'Diazepam','Fentanyl'
        medicine2= 'Amlodipine', 'Spironolactone', 'Cephalexin','Citalopram', 'Lorazepam', 'Montelukast'
        medicine3= 'Lisinopril', 'Ibuprofen', 'Amitriptyline','Naproxen','Cymbalta'
        medicine4= 'Atorvastatin','Metformin','Simvastatin','Omeprazole','Amlodipine','Metoprolol','Acetaminophen & hydrocodone','Albuterol'
        medicine_=medi(medicine1, medicine2, medicine3, medicine4)
        
        def pre(precautions1,precautions2,precautions3,precautions4):
            try:
                precautions_1= random.choice(precautions1)
                precautions_2= random.choice(precautions2)
                precautions_3= random.choice(precautions3)
                precautions_4= random.choice(precautions4)

                return precautions_1 + ' ,' + precautions_2 + ',' + precautions_3 +',' +precautions_4
            except Exception as e:
                print(f' Error occurs in precaution: {str(e)}')
            
        precautions1= ['Avoide Spicy food','Stay Hydrated','Maintain Hygine']
        precautions2= ['Take enough rest', 'Avoide too much meat','Eat more fiber']
        precautions3=['Dont Carry heavy Load', 'Drink lot of water','Dont Stress']
        precautions4=['Avoide Drinking and Smoking', 'Avoide oily Food']
        precations_=pre(precautions1,precautions2,precautions3,precautions4) 
                      
    except Exception as e:
        print(f'Error occours in generation details: {str(e)}')
    return Patient(Mobileno_,address_,medical_,doctor_,first_, second_,ongoing, medicine_, precations_)

def main():
    patients = [generate_details() for i in range(100)]

    data = {"ID": id,
        "Name":ran_name_g,
        "Age": ran_age,
        "Mobile_number": [patient.mobile_no for patient in patients],
        "Address":[patient.address for patient in patients],
        "Diagnosis": [patient.treatment for patient in patients],
        "Consultant_Doctor": [patient.doc_name for patient in patients],
        "First_Inspection": [patient.inspection1 for patient in patients],
        "Second_Inspection": [patient.inspection2 for patient in patients],
        "Ongoing_Inspection":[patient.ongoing_inspection for patient in patients],
        "Medicines": [patient.medicines for patient in patients],
        "Precautions": [patient.patients_preactions for patient in patients]
    }
    df = pd.DataFrame(data)

    df.to_csv("patients_details.csv", index= False)
    print("patients personal CSV file has been created successfully.")

if __name__ == "__main__":
    main()


# creating patients medical data:

data1= pd.read_csv('patients_details.csv')

input_csv= 'patients_details.csv'
output_csv= 'patients_medical_details.csv'
hide_column= ['Name','Mobile_number','Address']

data1= pd.read_csv('patients_Details.csv', index_col=False)

data1= data1.drop(columns=hide_column)

data1.to_csv(output_csv)
print(data1)
print('patients medical report file has been created successfully.')

        

        