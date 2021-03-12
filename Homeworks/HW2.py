print("-"*30 , "CV Aplication Homework", "-"*30)

cV1 = {"Name": "Erdal",
       "Surname": "İnce",
       "Age": 35,
       "Gender" : "Male",
       "Occupation" : "Electrical and Electronics Engineer",
       "Job Experience" : "Turkish Air Force: 10 years ,Havelsan : 5 years",
       "Languages": "Turkish,English,Spanish"
       }
cV2 = {"Name": "Hülya",
       "Surname": "Karaca", 
       "Age": 24,
       "Gender" : "Female",
       "Occupation" : "Computer Engineer",
       "Job Experience" : "Global AI Hub: 3 years",
       "Languages": "Turkish ,English"
       }
cV3 = {"Name": "Betül",
       "Surname": "Delice",
       "Occupation" : "Doctor",
       "Age": 27,
       "Gender" : "Female",
       "Job Experience" : "Ankara City Hospital: 2 years",
       "Languages": "Turkish ,English ,French"
       }
cV4 = {"Name": "Ayşe",
       "Surname": "Koç",
       "Age": 23,
       "Gender" : "Female",
       "Education Information" : "Civil Cervant",
       "Job Experience" : "Ankara Üniversty: 3 years",
       "Languages": "Turkish"
       }
cV5 = {"Name": "Mehmet Ali",
       "Surname": "Tan",
       "Age": 26,
       "Gender" : "Male",
       "Education Information" : "Student",
       "Job Experience" : "Electrical Tecnician: 2 years",
       "Languages": "Italian"
       }
x = "*"*5
print(f"""
        {x} Erdal İnce'ye ait CV Bilgileri {x}
{cV1}    
        """, f"""
        {x} Hülya Karaca'ya ait CV Bilgileri {x}
{cV2}    
        """,f"""
        {x} Betül Delice'ye ait CV Bilgileri {x}
{cV3}    
        """,f"""
        {x} Ayşe Koç'a ait CV Bilgileri {x}
{cV4}    
        """,f"""
        {x} Mehmet Ali Tan'a ait CV Bilgileri {x}
{cV5}    
        """)
print("All rights reserved by Erdal İNCE not use without permision :)")
#%%
#Normal ödev yukarıda yaptım aynı ödevi pandas kütüphanesi ile yaptım.  
import pandas as pd
print("-"*30 , "CV Aplication Homework", "-"*30)
x = "*"*5

cV1 = {"Name": "Erdal",
       "Surname": "İnce",
       "Age": 35,
       "Gender" : "Male",
       "Occupation" : "Electrical and Electronics Engineer",
       "Job Experience" : "Turkish Air Force: 10 years ,Havelsan : 5 years",
       "Languages": "Turkish,English,Spanish"
       }
cV2 = {"Name": "Hülya",
       "Surname": "Karaca", 
       "Age": 24,
       "Gender" : "Female",
       "Occupation" : "Computer Engineer",
       "Job Experience" : "Global AI Hub: 3 years",
       "Languages": "Turkish ,English"
       }
cV3 = {"Name": "Betül",
       "Surname": "Delice",
       "Occupation" : "Doctor",
       "Age": 27,
       "Gender" : "Female",
       "Job Experience" : "Ankara City Hospital: 2 years",
       "Languages": "Turkish ,English ,French"
       }
cV4 = {"Name": "Ayşe",
       "Surname": "Koç",
       "Age": 23,
       "Gender" : "Female",
       "Education Information" : "Civil Cervant",
       "Job Experience" : "Ankara Üniversty: 3 years",
       "Languages": "Turkish"
       }
cV5 = {"Name": "Mehmet Ali",
       "Surname": "Tan",
       "Age": 26,
       "Gender" : "Male",
       "Education Information" : "Student",
       "Job Experience" : "Electrical Tecnician: 2 years",
       "Languages": "Italian"
       }
A,B,C,D,E = pd.Series(cV1),pd.Series(cV2),pd.Series(cV3),pd.Series(cV4),pd.Series(cV5)
print(f"""
        {x} Erdal İnce'ye ait CV Bilgileri {x}    
        """)
print(A)
print(f"""
        {x} Hülya Karaca'ya ait CV Bilgileri {x}    
        """)
print(B)
print(f"""
        {x} Betül Delice'ye ait CV Bilgileri {x}    
        """)
print(C)
print(f"""
        {x} Ayşe Koç'a ait CV Bilgileri {x}    
        """)
print(D)
print(f"""
        {x} Mehmet Ali Tan'a ait CV Bilgileri {x}    
        """)
print(E)
