import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df1= pd.read_csv('patients_details.csv')
df2 = pd.read_csv('patients_medical_details.csv')
df3= pd.read_csv('patients_details.csv')

def mask_mobile_number(number):
    num= str(number)
    return f'XXX-XXX-{num[7:11]}'

df3['Mobile_number'] = df1['Mobile_number'].apply(mask_mobile_number)


db_conn={
    'host': 'localhost',
    'database':'postgres',
    'user':'postgres', 
    'password': '4567',
    'port': '5432'
}


def scenario_1():
    file = int(input('Enter number: '))
    flag = 0
    if file == 1:
        flag= 1
    
    try:    
        if flag == 1: 
            print('Access granted to check the patient details')
            conn= psycopg2.connect(**db_conn)
            engine=  create_engine(f"postgresql://{db_conn['user']}:{db_conn['password']}@{db_conn['host']}:{db_conn['port']}/{db_conn['database']}")
            df1.to_sql('patients_real_data_',con=engine,if_exists='replace',index=False)
            
            create_view= ''' CREATE VIEW patients_real_data_view AS
                            SELECT * FROM patients_real_data_;'''
                            
            with conn.cursor() as cursor:
                cursor.execute(create_view)
                conn.commit()
            
            conn.close()
            print('Data transferred to postgreSQL sucessfully.')
            
        elif flag == 0:
            print('Access not granted to check the personal details')
            
            conn= psycopg2.connect(**db_conn)
            engine=  create_engine(f"postgresql://{db_conn['user']}:{db_conn['password']}@{db_conn['host']}:{db_conn['port']}/{db_conn['database']}")
            df1.to_sql('patients_real_blinded',con=engine,if_exists='replace',index=False)
            
            create_view= ''' CREATE VIEW patients_real_blinded_view AS
                            SELECT "ID","Age","Diagnosis","Consultant_Doctor","First_Inspection","Second_Inspection",
                            "Ongoing_Inspection","Medicines","Precautions"
                            FROM patients_real_blinded;'''
                            
            with conn.cursor() as cursor:
                cursor.execute(create_view)
                conn.commit()
                
                conn.close()
            print('patients_real_blinded_view created successfully')
            
        else:
            print('Invalid Access number')
            
        
    except Exception as error:
        print(error)
        
    finally:
        try:
            with conn.cursor() as cursor:
                drop_table01 = "DROP TABLE IF EXISTS patients_real_data_ CASCADE;"
                drop_view01="DROP TABLE IF EXISTS patients_real_data_view CASCADE;"
                drop_table02= "DROP TABLE IF EXISTS patients_real_blinded CASCADE;"
                drop_view02 = "DROP VIEW IF EXISTS patients_real_blinded_view CASCADE;"
                cursor.execute(drop_table01)
                cursor.execute(drop_view01)
                cursor.execute(drop_table02)
                cursor.execute(drop_view02)
                conn.commit()
                print('Both table and view dropped successfully.')
        except Exception as error:
            print('Error dropping table and view:', error)
        conn.close()

def scenario_2(): 
    try:
        conn= psycopg2.connect(**db_conn)
        engine=  create_engine(f"postgresql://{db_conn['user']}:{db_conn['password']}@{db_conn['host']}:{db_conn['port']}/{db_conn['database']}")
        df2.to_sql('patients_blinded_data',con=engine,if_exists='replace',index=False)
        
        print('Data transferred to postgreSQL sucessfully.')
        
        create_view= ''' CREATE VIEW patients_blinded_data_view AS
                        SELECT * FROM patients_blinded_data;'''
                        
        with conn.cursor() as cursor:
            cursor.execute(create_view)
            conn.commit()
        print('patients_blinded_data_view created successfully')
        
        conn.close()
    except Exception as error:
        print(error)
        
    finally:   
        try:
            
            with conn.cursor() as cursor:
                drop_table= "DROP TABLE IF EXISTS patients_blinded_data CASCADE;"
                drop_view= "DROP TABLE IF EXISTS patients_blinded_data_view CASCADE;"
                cursor.execute(drop_table)
                cursor.execute(drop_view)
                conn.commit()
                print('Both table and view dropped successfully.')
        except Exception as error:
            print('Error dropping table and view: ',error)
        
        conn.close()
        
def scenario_3():
    
    try:
        conn= psycopg2.connect(**db_conn)
        engine= create_engine(f"postgresql://{db_conn['user']}:{db_conn['password']}@{db_conn['host']}:{db_conn['port']}/{db_conn['database']}")
        df3.to_sql('patients_real_details_',con=engine,if_exists='replace',index=False)
        df2.to_sql('patients_blinded_details_',con=engine, if_exists='replace',index=False)
        
        create_view= ''' CREATE VIEW patients_real_details_view AS
                        SELECT "ID","Age","Mobile_number","Diagnosis","Consultant_Doctor","First_Inspection","Second_Inspection",
                            "Ongoing_Inspection","Medicines","Precautions"
                            FROM patients_real_details_;'''
                        
        with conn.cursor() as cursor:
            cursor.execute(create_view)
            conn.commit()
            
        print('masking and view on patients_real_details_view succesfully done.')
        try: 
            with conn.cursor() as cursor:

                drop_blinded_table= "DROP VIEW IF EXISTS patients_blinded_data_view CASCADE"
                cursor.execute(drop_blinded_table)
                conn.commit()
                
            print('successfully drop existing blinded view')
        
        except Exception as error:
            print('Error in dropping blinded file:', error)
            
        
        try:
            create_blinded_view = '''
                            CREATE VIEW patients_blinded_view AS
                            SELECT "ID","Age","Mobile_number","Diagnosis","Consultant_Doctor","First_Inspection","Second_Inspection",
                            "Ongoing_Inspection","Medicines","Precautions" 
                            FROM patients_real_details_;'''
            
            with conn.cursor() as cursor:
                cursor.execute(create_blinded_view)
                conn.commit()
                print('New blinded view created from real data.')
                conn.close()
        except Exception as error:
            print('Error in creating view file: ', error)
            
            
    except Exception as error:
        print('Error:',error)
            
      
    finally:
        try:
            with conn.cursor() as cursor:                
                drop_table = "DROP TABLE IF EXISTS patients_real_details_ CASCADE;"
                drop_view = "DROP VIEW IF EXISTS patients_real_details_view CASCADE;"
                drop_view1= "DROP VIEW IF EXISTS patients_blinded_view CASCADE;"
                cursor.execute(drop_table)
                cursor.execute(drop_view)
                cursor.execute(drop_view1)
                conn.commit()
                print('Both table and view dropped successfully.')
        except Exception as error:
            print('Error dropping table and view:', error)
            
        conn.close()


selected_scenario= input('Enter the file_name: ')

if selected_scenario== 'Real Data':
    scenario_1()
elif selected_scenario=='Blinded Data':
    scenario_2()
elif selected_scenario == 'Real Blinded Data':
    scenario_3()
else:
    print('Invalid selected scenario.')



     
