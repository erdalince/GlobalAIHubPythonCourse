sorular =["Horozu çok olan köyde şeklinde başlayan atasözünün devamı nasıldır?",
          "Sosyal medyada, kısa sürede ve kolayca takipçi kazanmak isteyenlerin uyguladığı klişe taktik hangisidir?",
          "Klasik bir çengel bulmacada, bir kutucukta en fazla kaç farklı soru sorulur?",
          "Tarih boyunca İngiltere tahtına hangi adda bir kral çıkmamıştır?",
          "Yabancı bir eseri yer adları, şahıs adları deyimleri, gelenek ve görenekleriyle yerli hayata adapte ederek çevirmeye ne ad verilir?",          
          "Firavun Tutankamon vücudunda hangi hayvan figürünün olduğu bir kolyeyle mezara konulmuştur?",
          "Aşağıdaki programlama dilleri ve kurucuları eşleştirilmesinden hangisi yanlış eşleştirilmiştir?",
          "Ambidexter olduğunu söyleyen birinin özelliği hangisidir?",
          "Ortada olan her şey anlamına gelen ifade hangisidir?",
          "Şimal,cenup,şark,garp diyen bir kişi hangisini sayıyordur?"]#Sorulacak soruları liste içerisinde yazdık ve daha sonra her bir soru için cevap şıklarını ayrı listelere aktardık.
soru_1_Sıklar=["a) Sabah erken olur"," b) Akşam geç olur"," c) Akşam erken olur"," d) Sabah geç olur"]
soru_2_Sıklar=["a) Atara atar gidere gider"," b) Omuz omuza"," c) göze göz dişe diş"," d) Takibe takip"]
soru_3_Sıklar=["a) 1","b) 2"," c) 3"," d) 4"]
soru_4_Sıklar=["a) Arthur"," b) Richard"," c) Henry"," d) George"]
soru_5_Sıklar=["a)Uyarlama","b)Benzeştirme","c)Kodlama","d)Biçimleme"]
soru_6_Sıklar=["a)Kedi","b)Doğan","c)Yılan","d)Kurt"]
soru_7_Sıklar=["a)C dili-Dennis Ritchie","b)Ruby - Yukhiro Matsumoto","c)Java - Brendan Eich","d)Python - Guido Van Rossum"]
soru_8_Sıklar=["a)Gözleri birbirinden farklı renktedir","b)Tırnakları yoktur","c)İki elini eşit kullanıyordur","d)Parmak izi yoktur"]
soru_9_Sıklar=["a)Masa dolap","b)Cam çerçeve","c)Sandık sepet","d)Halı kilim"]
soru_10_Sıklar=["a)Tarihi çağlar","b)Ana yönler","c)Maddenin halleri","d)Doğada bulunan elementler"]
cevaplar= ["d","d","b","a","a","b","c","c","c","b"]# soruların cevaplarını liste içerisine girdik.

print("Lütfen Soruları Cevaplarken Sadece Cevap Şıklarını Giriniz. Yarışmada Başarılar Dileriz...")
print('-'*50)  

def bilgiYarışmasınıBaslat():#Bilgi yarışması için bir fonksiyon oluşturduk.
    puan = 0 
    yanlısCevap = 0
    dogruCevap = 0
    name = input("Lütfen Adınızı Giriniz: ")
    surname = input("Lütfen Soyadınızı Giriniz: ")
    print('-'*50)
    print(f'Soru 1 : {sorular[0]}')
    
    for i in soru_1_Sıklar:
        print(i)
        
    cevap_1 = input("Lütfen 1.Sorunun Cevabını Giriniz :")
    
    if cevap_1.lower() == cevaplar[0]:  #kullanıcı küçük yada büyük harf girerse harf duyarlılığı için lower kullandık.Çünkü cevaplarımız küçük harfli.
        print("Tebrikler 1.Soruyu Doğru Cevapladınız")        
        puan +=10 #kullanıcı her bir doğru cevabı için 10 puan alacak.
        dogruCevap +=1 #fonksiyon içerisindeki doğruCevap bir artarak kullanıcının kaç soruya deoğru cevap verdiğini öğreneceğiz.
        
    else:
        print("Üzgünüz 1.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1 #fonksiyon içerisindeki yanlısCevap bir artarak kullanıcının kaç soruya yanlış cevap verdiğini öğreneceğiz.
    print('-'*50)
            
    print(f'Soru 2 : {sorular[1]}')
    for i in soru_2_Sıklar:
        print(i)
        
    cevap_2 = input("Lütfen 2.Sorunun Cevabınızı Giriniz :")
    
    if cevap_2.lower() == cevaplar[1]:
        print("Tebrikler 2.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1 
    else:
        print("Üzgünüz 2.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
    print('-'*50)                
    print(f'Soru 3 : {sorular[2]}')
    for i in soru_3_Sıklar:
        print(i)
        
    cevap_3 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_3.lower() == cevaplar[2]:
        print("Tebrikler 3.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1 
    else:
        print("Üzgünüz 3.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
            
    print('-'*50) 
    print(f'Soru 4 : {sorular[3]}')
    for i in soru_4_Sıklar:
        print(i)
        
    cevap_4 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_4.lower() == cevaplar[3]:
        print("Tebrikler 4.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 4.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
        
    print('-'*50) 
    print(f'Soru 5 : {sorular[4]}')
    for i in soru_5_Sıklar:
        print(i)
        
    cevap_5 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_5.lower() == cevaplar[4]:
        print("Tebrikler 5.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 5.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
    
    print('-'*50) 
    print(f'Soru 6 : {sorular[5]}')
    for i in soru_6_Sıklar:
        print(i)
        
    cevap_6 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_6.lower() == cevaplar[5]:
        print("Tebrikler 6.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 6.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
        
    print('-'*50)   
    print(f'Soru 7 : {sorular[6]}')
    for i in soru_7_Sıklar:
        print(i)
        
    cevap_7 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_7.lower() == cevaplar[6]:
        print("Tebrikler 7.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 7.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
        
    print('-'*50)   
    print(f'Soru 8 : {sorular[7]}')
    for i in soru_8_Sıklar:
        print(i)
        
    cevap_8 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_8.lower() == cevaplar[7]:
        print("Tebrikler 8.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 8.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
        
    print('-'*50)   
    print(f'Soru 9 : {sorular[8]}')
    for i in soru_9_Sıklar:
        print(i)
        
    cevap_9 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_9.lower() == cevaplar[8]:
        print("Tebrikler 9.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 9.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
        
    print('-'*50)   
    print(f'Soru 10 : {sorular[9]}')
    for i in soru_10_Sıklar:
        print(i)
        
    cevap_10 = input("Lütfen Cevabınızı Giriniz :")
    
    if cevap_10.lower() == cevaplar[9]:
        print("Tebrikler 10.Soruyu Doğru Cevapladınız")        
        puan +=10
        dogruCevap +=1     
    else:
        print("Üzgünüz 10.Soruya Yanlış Cevap Verdiniz")
        yanlısCevap +=1
    print('-'*50) 
    if yanlısCevap >=5 : #Eğer kullanıcının yanlış sağısı 5 veya daha az olursa ekrana başarısız olduğunu ayrıntılı olarak yazdıracak.
        print(f'Sayın {name} {surname}\nÜzgünüz Yarışmada Başarısız Oldunuz.\nToplam {dogruCevap} soruya doğru\nToplam {yanlısCevap} soruya yanlış cevap verdiniz.\nToplam puanınız: {puan} puan ')
    else:#Kullanıcı 6 cevap ve üzeri için bilgi yarışmasında başarılı olacak.ve bilgileri ayrıntılı olarak yazdırılacak.
        print(f'Sayın {name} {surname}\nTebrikler Yarışmada Başarılı Oldunuz.\nToplam {dogruCevap} soruya doğru\nToplam {yanlısCevap} soruya yanlış cevap verdiniz.\nToplam puanınız: {puan} puan')     
   
bilgiYarışmasınıBaslat()
