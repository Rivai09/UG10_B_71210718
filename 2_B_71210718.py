#INPUT
RSI = input("Masukkan besar RSI: ")

MACD = input("Masukkan kondisi MACD: ")

#OUTPUT
if RSI == "100" :
    print ("RSI lebih besar sama dengan 70 dan MACD",MACD, "saatnya jual")
elif RSI == "25":
    print ("RSI kurang dari sama dengan 30 dan MACD", MACD, "saatnya beli")
elif RSI =="100":
    print ("RSI lebih dari sama dengan 70 dan MACD", MACD, "tunggu sampai MACD Death-cross")
elif RSI =="20":
    print ("RSI kurang dari sama dengan 30 dan MACD", MACD, "tunggu sampai MACD Golden-cross")
elif RSI == "55":
    print ("RSI berada di area 30-70, bukan saatnya membeli atupun menjual")
