#INPUT
input1 = input ("Masukkan angka : ")
input2 = input ("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3?")
input3 = input ("Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10?")

#OUPUT
if input1 == "10" and input2:
    print ("IYA")
if input1== "10" and input3 :
    print ("IYA DONG")
if input1 == "22" and input2:
    print ("IYA")
if input1== "22" and input3 :
    print ("TIDAK")
if input1== "9" :
    print ("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. progam dihentikan")