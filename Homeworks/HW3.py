#Öğrenci isimlerinin ve notlarının kullanıcıdan alınması
student_1= input("Please Enter The Name Of Student_1:")
sudent_1_midterm = float(input("Please Enter The Student_1 Midterm Grade :"))
student_1_poject = float(input("Please Enter The Student_1 Project Grade :"))
student_1_final = float(input("Please Enter The Student_1 Final Grade :"))
student_1_passingGrade = round(sudent_1_midterm*0.3 + student_1_poject*0.3 + student_1_final*0.4,2)#round ile passinGrade iki basamağa yuvarladık.

student_2= input("Please Enter The Name Of Student_2:")
sudent_2_midterm = float(input("Please Enter The Student_2 Midterm Grade :"))
student_2_poject = float(input("Please Enter The Student_2 Project Grade :"))
student_2_final = float(input("Please Enter The Student_2 Final Grade :"))
student_2_passingGrade = round(sudent_2_midterm*0.3 + student_2_poject*0.3 + student_2_final*0.4,2)

student_3= input("Please Enter The Name Of Student_3:")
sudent_3_midterm = float(input("Please Enter The Student_3 Midterm Grade :"))
student_3_poject = float(input("Please Enter The Student_3 Project Grade :"))
student_3_final = float(input("Please Enter The Student_3 Final Grade :"))
student_3_passingGrade = round(sudent_3_midterm*0.3 + student_3_poject*0.3 + student_3_final*0.4,2)

student_4= input("Please Enter The Name Of Student_4:")
sudent_4_midterm = float(input("Please Enter The Student_4 Midterm Grade :"))
student_4_poject = float(input("Please Enter The Student_4 Project Grade :"))
student_4_final = float(input("Please Enter The Student_4 Final Grade :"))
student_4_passingGrade = round(sudent_4_midterm*0.3 + student_4_poject*0.3 + student_4_final*0.4,2)

student_5= input("Please Enter The Name Of Student_5:")
sudent_5_midterm = float(input("Please Enter The Student_5 Midterm Grade :"))
student_5_poject = float(input("Please Enter The Student_5 Project Grade :"))
student_5_final = float(input("Please Enter The Student_5 Final Grade :"))
student_5_passingGrade = round(sudent_5_midterm*0.3 + student_5_poject*0.3 + student_5_final*0.4,2)
#Boş bir Sözlük oluşturarak kullanıcadan alınan verilerin sözlüğe eklenmesi
studentGradeDictionary = {}
studentGradeDictionary["student_1"]= student_1
studentGradeDictionary["sudent_1_midterm" ]= sudent_1_midterm
studentGradeDictionary["student_1_poject"] = student_1_poject
studentGradeDictionary["student_1_final"] = student_1_final
studentGradeDictionary["student_2"]= student_2
studentGradeDictionary["sudent_2_midterm" ]= sudent_2_midterm
studentGradeDictionary["student_2_poject"] = student_2_poject
studentGradeDictionary["student_2_final"] = student_2_final
studentGradeDictionary["student_3"]= student_3
studentGradeDictionary["sudent_3_midterm" ]= sudent_3_midterm
studentGradeDictionary["student_3_poject"] = student_3_poject
studentGradeDictionary["student_3_final"] = student_3_final
studentGradeDictionary["student_4"]= student_4
studentGradeDictionary["sudent_4_midterm" ]= sudent_4_midterm
studentGradeDictionary["student_4_poject"] = student_4_poject
studentGradeDictionary["student_4_final"] = student_4_final
studentGradeDictionary["student_5"]= student_5
studentGradeDictionary["sudent_5_midterm" ]= sudent_5_midterm
studentGradeDictionary["student_5_poject"] = student_5_poject
studentGradeDictionary["student_5_final"] = student_5_final
print(studentGradeDictionary) #Oluşturduğumuz sözlüğün yazdırılması
#Boş liste oluşturarak 5 öğrencinin notları listeye eklendi. 
studentGradeList = []
studentGradeList.append(student_1_passingGrade)
studentGradeList.append(student_2_passingGrade)
studentGradeList.append(student_3_passingGrade)
studentGradeList.append(student_4_passingGrade)
studentGradeList.append(student_5_passingGrade)
print(studentGradeList) #Öğrenci notlarının listeye aktardıktan sonra yazdırılması
studentGradeList.sort() #sort ile listede yer alan öğrenci notlarını küçükten büyüğe sıraladık.
studentGradeList.reverse()#reverse ile küçükten büyüğe sıraladığımız listeyi ters çevirerek büyükten küçüğe çevirmiş olduk.
print(studentGradeList)


