import streamlit as st

#text_number_1 = st.number_input("Číslo jedna")
#text_number_2 = st.number_input("Číslo dvě")
#list_operace =["scitani","odcitani","nasobeni","deleni"]
#slct_operace = st.selectbox("operace",list_operace )
#btn_proved_operaci= st.button("proved operaci")
#if slct_operace:
#soucet=text_number_1 + text_number_2
#st.write(soucet)

#list_jmen = ["Adéla","Albert"]
#text_jmeno = st.text_input("zadej jmnéno")
#if text_jmeno in list_jmen:
#    st.write(f"Ahoj {text_jmeno}")
#if text_jmeno not in list_jmen:
#    list_jmen.append(text_jmeno)
#st.write(list_jmen)

#slovnik={
#    "Adéla":30,
#    "Míša":29}
#st.write( slovnik)
#st.write( slovnik["Adéla"])
#for clovek, vek in slovnik.items():
#    st.write(f"{clovek} je {vek} let")
#del slovnik["Adéla"]
#st.write(slovnik)

#Máte dict_jmen = {"Adela":25, "Albert": 30}
#uživatel zadá své jméno a pokud je v dict_jmen, tak se na
#stránce zobrazí "Ahoj" + jméno + "je ti" + věk,
# jinak "Nemám tě v dict_jmen"
 
#dict_jmen={"Adéla":25,"Albert":30}
#text_jmeno = st.text_input("Zadej jméno")
#if text_jmeno in dict_jmen:
#        st.write(f"Ahoj {text_jmeno} je ti {dict_jmen[text_jmeno]} let")
#elif text_jmeno not in dict_jmen:
#        st.write("Nemám tě v dict_jmen")

#cislo = 2

#if cislo == 1:
#        st.write("Kontroluju cislo 1")
#elif cislo == 2:
#        st.write("Kontroluju číslo 2")
#elif cislo >=2 :
#        st.write("Kontroluju číslo 3")

#st.write("---")

#if cislo == 1:
#        st.write("Kontroluju cislo 1")
#if cislo == 2:
#        st.write("Kontroluju cislo 2")
#if cislo >=2:
#        st.write("Kontroluju cislo 3")

#Méte dict_jmen = {"Adéla": 25,"Albert": 30}
#Uživatel zadá jméno
#Vytisknete hodnotu věku pro toto jméno.

#dict_jmen = {"Adéla":25, "Albert":30}
#text_jmeno = st.text_input("Zadej jméno")
#st.write(f"{dict_jmen[text_jmeno]}")

#Méte dict_jmen = {"Adéla": 25,"Albert": 30}
#Uživatel zadá jméno
#Vytvořte nový klíč s tímto jménem a přiřadte mu hodnotu 0.
#Vytisknete tento dict_jmen

#dict_jmen = {"Adéla":25, "Albert":30}

#def funkce_scitani(cislo_1, cislo_2):
#    vysledek = cislo_1 + cislo_2
#    return vysledek

#def funkce_pozdrav_s_defaul_value(jmeno="Albert"):
#    return f"Ahoj" {jmeno}

#Vytvořete funkci která bude mít dva číselné vstupy
#tyto dvě čísla odečte.

#a=50
#b=10
#def funkce_odcitat(cislo_1, cislo_2):
#    vysledek = cislo_1 - cislo_2
#    return vysledek
#st.write(funkce_odcitat(a,b))

#Vytvořte funkci, která bude mít dva číselné vstupy
#a jeden textový, který bude scitat nebo odcitat.
#Dle textu se rozhodne, zda bude čísla sčítat nebo odčítat.

#a=10
#b=20
#c="scitat"
#def funkce_scitat(cislo_1, cislo_2):
#    vysledek = cislo_1 + cislo_2
#st.write(funkce_scitat(a,b))

#def funkce_operace(cislo_1, cislo_2, operace):
#    if operace == "scitani":
#        vysledek = cislo_1 + cislo_2
#        return vysledek
#    elif operace - "odcitat":
#        vysledek = cislo_1 - cislo_2
#        return vysledek
#def funkce_scitani(cislo_1, cislo_2):
#    st.write(funkce_scitani(a,b))


#18.11.2023
#19.11.2023-základní streamlit, struktura

#25.11.2023-st. session_state
#26.11.2023-API,json, request

#02.11.2023-Projekty-Konzultace
#03.11.2023-Projekty-Konzultace

#07.12.20023 od 17:00-Prezentace projektů

#uživatel zada své jméno
#použijte checkbox na odsouhlasení, že je vám více jak 18 let.
#přidejte tlačítko, které po stisknutí
#zkontroluje zda checkbox je aktivní
#pokud je tak vytisknete "Vítej v klubu ___".
#Pokud není, tak vytiskne "You shall not pass"

#jmeno = st.text_input("zadej jmnéno")
#plnoletost = st.checkbox("Je vám více jak 18 let")
#st.write(plnoletost)
#tlacitko = st.button("tlačítko")
#if tlacitko:
#    if plnoletost:
#        st.write(f"Vítej v klubu {jmeno}")
#    else:
#        st.write("You Shall not pass")

#Mate list list_klub = ["Adéla", "Albert", "Míša"]
#Uživatel zadá svůj věk
#použijte toggle, který při věku nad 18 je aktivní,
#při věku pod 18 je neaktivní
#Pokud je toggle neaktivní, vypište "You shall not pass"
#pokud je toggle aktivní, umožněte uživateli zadat jméno a přidejte
#tlačítko, které po stisknutí přidá jméno do listu list_klub.
#vytisknete list list_klubu.

#list_klub = ["Adéla","Albert","Míša"]
#vek = st.number_input("Zadejte věk")
#toggle_status = False
#if vek < 18:
#    toggle_status = False
#else:
#    toggle_status = True
#on = st.toggle("plnoletý",toggle_status, disabled=True)
#if on:
#    jmeno = st.text_input("zadejte jmeno")
#    tlacitko = st.button("přidat")
#    if tlacitko:
#        list_klub.append(jmeno)
#        st.write(list_klub)
#else:
#    st.write("You shall not pass")

#with st.form("Přihlášení"):
#    st.write("Přihlášení")
#    jmeno = st.text_input("Jméno")
#    heslo = st.text_input ("Heslo",type="password")
#    tlacitko = st.form_submit_button("Přihlásit")


#dict_jmen = {"Míša":"tapo",
#             "Karel":"majda",
#             "Týna":"bara",
#             "Dáša":"necum",
#             "Alex":"marcus"}
#if tlacitko:
#    if jmeno == "" or heslo == "":
#        st.warning("Vyplňte jméno a heslo", icon="🚨")
#    elif jmeno in dict_jmen:
#        st.error("Jméno není v adresáři", icon="🚨")
#    elif jmeno and heslo in dict_jmen:
#        st.success("Správné údaje",icon="✅")
#    elif heslo in dict_jmen :
 #       st.error("Špatné heslo", icon="🚨")



