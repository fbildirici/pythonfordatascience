###############################################
######sözlük veri tipi, dictionary#############

# - Değiştirilebilir
# - Sırasız (3.7 sıralı sonra sırasız)
# - Kapsayıcı

# key-value

dictionary= {"REG": "Regression",
            "LOG": "Logistic Regression",
            "CART": "Classification and Reg"
            }

dictionary= {"REG": ["RMSE",10],
             "LOG": ["MSE",20],
             "CART": ["SSE",30]}

dictionary["CART"][1] #CART bölümünden 0,1 yani ikinci değeri 30 değerini getirir


###### Key Sorgulama ################
#####################################

"REG" in dictionary #True
"Elon" in dictionary #False

##### Keye göre value erişimi #######

dictionary["REG"]
dictionary.get("REG") # (Reg içine tanımlı RMSE,10 değerini getirir)

######### Value Değiştirmek-Değiştirilebilirlik Özelliği#########

dictionary["REG"] = ["YSA", 10]
dictionary

######REG değerinin içi değiştirildi ############################

############### Tüm Keylere Erişmek #############################

dictionary.keys() #keyleri getirir
dictionary.values() #valueları getirir

#####tüm çiftleri tuple - demet haline çevirme

dictionary.items()

############## key-value değerini güncellemek ###################

dictionary.update({"REG": 11})

########## YENİ Key-Value eklemek ###############################

dictionary.update({"RF" : 25 })

dictionary