import formatA6
from fpdf import FPDF
import os
from num2words import num2words
from datetime import date
from datetime import datetime, date, time
import mysql.connector
from mysql.connector import errorcode

#Conn = mysql.connector.connect(host="192.168.1.8", database="chumanagement", user="server",password="")
Conn = mysql.connector.connect(host="localhost", database="chumanagement", user="root",password="")
Cursor = Conn.cursor(buffered=True)

def GetIdCommandeTamponEncaissement():
    Req = "SELECT IdCommande FROM TamponEncaissement"
    Cursor.execute(Req)
    return Cursor.fetchone()[0]

IdCommande = GetIdCommandeTamponEncaissement()
# print(IdCommande)

# with open("testo.txt", "r") as IdCommande:
#     IdCommande = IdCommande.read()

def CaisseValide(IdCommande):
    Data = (IdCommande,)
    Req = "SELECT * FROM CAISSE WHERE IdCommande = %s"
    Cursor.execute(Req, Data)
    return Cursor.fetchall()

DataP = CaisseValide(IdCommande)[0]

# def CaisseValide():
#     Req = "SELECT * FROM CAISSE"
#     Cursor.execute(Req)
#     return Cursor.fetchall()
#
# DataP = CaisseValide()[0]

class FPDF(FPDF):

    ## conception de la page pdf

    def header(self):

        self.set_font("helvetica", "i", 7)
        #self.set_xy(5, 5)
        self.image("cnrsd.jpg",h=15)
        self.set_xy(11, 5)
        self.cell(54,4,"CENTRE NATIONAL", align="c", border = 0)
        self.cell(2, 3, align="c", border=0)
        self.cell(2, 3, align="c", border=0)
        self.cell(10, 4, "REPUBLIQUE TOGOLAISE", align="l", border=0, ln=1)
        self.cell(21, 3,align="c", border=0)
        self.cell(25, 4, "DE RECHERCHE ET DE SOINS", align="c", border=0)
        self.cell(5, 3,align="c", border=0)
        self.cell(11, 3, align="c", border=0)
        self.cell(35, 4, "Travail-Liberté-Patrie", align="c", border=0,ln=1)
        self.cell(18, 3, align="c", border=0)
        self.cell(30, 4, "AUX DREPANOCYTAIRES", align="c", border=0, ln=1)
        self.cell(62, 4, "CNRSD", align="c", border=0)
        self.set_font("helvetica", "B", 11)
        self.cell(0, 4, str(DataP[1]) ,align="l",border=0, ln=1)                     ############## "Num Caisse"
        self.set_font("helvetica", "i", 7)
        self.set_xy(5, 21)
        DatePrint = datetime.today().strftime("%d %m %Y / %H:%M:%S")
        self.cell(6, 4, "Date et heure:", align="l", border=0)
        self.cell(48, 4, DatePrint , align="c", border=0)                      ############## "Date"
        self.set_font("helvetica", "B", 9)
        pdf.set_text_color(255, 0, 0)
        self.cell(35, 4, "ORIGINAL" , align="r", border=0, ln=1)
        #self.cell(20, 4, str(DataP[21]), align="r", border=0, ln=1)                    ############## "Heure"
        self.line(0,25,150,25)


    def footer(self):
        self.set_font("helvetica", "i", 7)
        #self.set_y(-13)
        self.set_xy(5, -13)
        self.line(0, 190, 150, 190)
        pageNum = self.page_no()
        if pageNum >= 1 :
            self.cell(0, 5, "NB: seuls les bons de consulatation sont valables pour 30 jours.",align="c",ln=1)
            #self.cell(0, 3, "Le centre vous souhaite une bonne guérison.", align="c", ln=1)
            self.set_font("helvetica", "i", 7)
            self.cell(10, 5, "Caissier:", align="l", border=0)
            self.cell(30, 5, str(DataP[19]) , border=0)                             ###### "Nom Caissier"
            self.cell(5,5,str(pageNum), border=1,align="c")
            self.cell(12, 5, "Opérateur:", align="l", border=0)
            self.cell(35, 5, str(DataP[17]) , border=0, align="l")                  ####### "Nom Operateur"


# CONFIGURATION BASIQUE

#pdf = FPDF("P", "mm", "A5")

pdf = FPDF("P", "mm", format = (105, 145))

# pdf = FPDF("P", "mm", format = (50, 200))
# P = portrait
# L = c'est paysage
# on peut spécifier le format de la page à imprimer

# w = 210
# h = 297

pdf.set_font("helvetica", "i", 9 )
pdf.set_margin(5)

# pour ajuster la marge on fait: pdf.set_margins(5, 5, 5)

# B = Bold. Au milieu on peut mettre italique si c'est ce style on veut

pdf.add_page()

# pour numérotation de page on fait: pdf.add_page(60, 5, "Page 1" 1)
# si on crée une 2è page on fait: pdf.add_page(60, 5, "Page 2" 1)

### CREATION DE CELLULE

pdf.cell(00,7, "REÇU PATIENT", border = 0, align= "c", ln=1)



pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
pdf.set_xy(5, 32)

# pdf.cell(40,7,  border = 0, fill = True)
# pdf.cell(40,7, "xxxxxxxxxxxxxxxxx", border = 1)
# pdf.cell(40,7, "xxxxxxxxxxx", border = 1, ln=1)
# pdf.cell(40,7, "xxxxxxxxxxxxxxxx", border = 1)
# pdf.cell(40,7, border = 0)
# pdf.cell(40,7, "xxxxxxxxxxxxx", border = 1,  align= "r", ln=1)

# pdf.cell(120,7, border = 0, ln=1)
#pdf.set_font("helvetica", "B", 9)
pdf.cell(64,13, str(DataP[2]) , border = 1)                #### "Nom et prénom"
pdf.set_font("helvetica", "i", 8)
pdf.cell(2,4,border=0)
pdf.cell(15,4, str(DataP[8]) , border = 0)                 #### "Age"
pdf.cell(23,4, str(DataP[9]) , border = 0, ln=1)           ### "Sexe"

pdf.cell(65,10, border = 0)
pdf.cell(20,10, str(DataP[10]) , border = 0)                 #### "Groupe"
pdf.cell(18,10, str(DataP[11]) , border = 0, ln=1)           #### "Patho"

## Label
pdf.set_xy(5, 45)

pdf.cell(32,7, "Montant Total", border = 1)
pdf.cell(32,7, "Montant Assurance", border = 1)
pdf.cell(32,7, "Montant Payé", border = 1, ln=1)

## Data
pdf.set_font("helvetica", "B", 9)
pdf.cell(32,7, str(DataP[3]) , border = 0)                            ### "DataMontant Total"
pdf.cell(32,7, str(DataP[4]) , border = 0)                            ### "DataMontant Assurance"
pdf.set_font("helvetica", "B", 10)
pdf.cell(32,6, str(DataP[5]) , border = 0, ln=1)                     ### "DataMontant Payé"

pdf.set_font("helvetica", "i", 8)
pdf.set_xy(5, 58)
pdf.set_text_color(255,0,0)                                   ##### num2words(42, lang='fr')
MtEnLettres = num2words(str(DataP[5]), lang="fr")
pdf.cell(00,7, MtEnLettres+" "+"francs CFA" , border = 0, ln=1)                        ### "Montant en lettres"

pdf.set_font("helvetica", "i", 8)
pdf.set_text_color(0,0,0)
pdf.cell(00,7, "DETAILS", border = 0, align= "c", ln=1)

pdf.dashed_line(0,65,150,65)
pdf.set_xy(5, 72)
pdf.set_font("helvetica", "i", 7)
## Label
pdf.cell(42,4, "Actes", border = 1, align= "l")
pdf.cell(10,4, "PU", border = 1, align= "c")
pdf.cell(7,4, "Qte", border = 1, align= "c")
pdf.cell(10,4, "Total", border = 1, align= "c")
pdf.cell(7,4, "Taux", border = 1, align= "c")
pdf.cell(10,4, "Mt Pec", border = 1, align= "c")
pdf.cell(10,4, "Mt Payé", border = 1, ln=1, align= "c")
### Data
pdf.set_font("helvetica", "i",6)
pdf.set_xy(5, 77)

### Data

def DetailCommande(IdCommande):
    Info = (IdCommande,)
    Req = "SELECT * FROM InfoCommande WHERE IdCommande = %s"
    Cursor.execute(Req,Info)
    return Cursor.fetchall()
Data = DetailCommande(IdCommande)

for i in Data :

    pdf.set_font("helvetica", "i",5)
    pdf.cell(42,3, str(i[3]), border = 0)                        ##### Actes
    #pdf.set_font("helvetica", "i", 7)
    pdf.cell(10,3, str(i[4]), border = 0, align= "c")            ##### PU
    pdf.cell(7,3, str(i[5]), border = 0, align= "c")            ##### Qte
    pdf.cell(10,3, str(i[6]), border = 0, align= "c")            ##### Total
    pdf.cell(7,3, str(i[9]), border = 0, align= "c")             ##### Taux
    pdf.cell(10,3, str(i[7]), border = 0, align= "c")             ##### MtPec
    pdf.cell(10,3, str(i[8]), border = 0, align= "c", ln=1)       ##### MtPaye

pdf.set_font("helvetica", "i",8)
pdf.cell(00,2,border=0,ln=1)
pdf.cell(00,4, "PRISE EN CHARGE", border = 0, align= "c", ln=1)

#pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
#pdf.set_xy(5, 32)

pdf.cell(50,4, str(DataP[6]) , border = 0)                           #### "AssurancePec"
pdf.set_font("helvetica", "i", 8)
pdf.cell(40,4, str(DataP[15]) , align= "r", border = 0, ln=1)         #### "Nom assure"
pdf.cell(21,4, str(DataP[7]) , border = 0)                           #### "Taux"
pdf.cell(30,4, str(DataP[4]) , border = 0)                            ### "MontantPec"
pdf.cell(40,4, str(DataP[16]) , align= "r", border = 0, ln=1)        #### "Code assure"
#pdf.cell(18,4, str(DataP[11]) , border = 0, ln=1)         #### "Patho"

###################################### RECU CONTRÔLE ###########################################
###################################### RECU CONTRÔLE ###########################################

pdf.add_page()

pdf.cell(00,7, "REÇU CONTRÔLE", border = 0, align= "c", ln=1)


pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
pdf.set_xy(5, 32)

# pdf.cell(40,7,  border = 0, fill = True)
# pdf.cell(40,7, "xxxxxxxxxxxxxxxxx", border = 1)
# pdf.cell(40,7, "xxxxxxxxxxx", border = 1, ln=1)
# pdf.cell(40,7, "xxxxxxxxxxxxxxxx", border = 1)
# pdf.cell(40,7, border = 0)
# pdf.cell(40,7, "xxxxxxxxxxxxx", border = 1,  align= "r", ln=1)

# pdf.cell(120,7, border = 0, ln=1)
#pdf.set_font("helvetica", "B", 9)
pdf.cell(64,13, str(DataP[2]) , border = 1)                #### "Nom et prénom"
pdf.set_font("helvetica", "i", 8)
pdf.cell(2,4,border=0)
pdf.cell(15,4, str(DataP[8]) , border = 0)                 #### "Age"
pdf.cell(23,4, str(DataP[9]) , border = 0, ln=1)           ### "Sexe"

pdf.cell(65,10, border = 0)
pdf.cell(20,10, str(DataP[10]) , border = 0)                 #### "Groupe"
pdf.cell(18,10, str(DataP[11]) , border = 0, ln=1)           #### "Patho"

## Label
pdf.set_xy(5, 45)

pdf.cell(32,7, "Montant Total", border = 1)
pdf.cell(32,7, "Montant Assurance", border = 1)
pdf.cell(32,7, "Montant Payé", border = 1, ln=1)

## Data
pdf.set_font("helvetica", "B", 9)
pdf.cell(32,7, str(DataP[3]) , border = 0)                            ### "DataMontant Total"
pdf.cell(32,7, str(DataP[4]) , border = 0)                            ### "DataMontant Assurance"
pdf.set_font("helvetica", "B", 10)
pdf.cell(32,6, str(DataP[5]) , border = 0, ln=1)                     ### "DataMontant Payé"

pdf.set_font("helvetica", "i", 8)
pdf.set_xy(5, 58)
pdf.set_text_color(255,0,0)                                   ##### num2words(42, lang='fr')
MtEnLettres = num2words(str(DataP[5]), lang="fr")
pdf.cell(00,7, MtEnLettres+" "+"francs CFA" , border = 0, ln=1)                        ### "Montant en lettres"

pdf.set_font("helvetica", "i", 8 )
pdf.set_text_color(0,0,0)
pdf.cell(00,7, "DETAILS", border = 0, align= "c", ln=1)

pdf.dashed_line(0,65,150,65)
pdf.set_xy(5, 72)
pdf.set_font("helvetica", "i", 7)
## Label
pdf.cell(42,4, "Actes", border = 1, align= "l")
pdf.cell(10,4, "PU", border = 1, align= "c")
pdf.cell(7,4, "Qte", border = 1, align= "c")
pdf.cell(10,4, "Total", border = 1, align= "c")
pdf.cell(7,4, "Taux", border = 1, align= "c")
pdf.cell(10,4, "Mt Pec", border = 1, align= "c")
pdf.cell(10,4, "Mt Payé", border = 1, ln=1, align= "c")
### Data
pdf.set_font("helvetica", "i",6)
pdf.set_xy(5, 77)

### Data

def DetailCommande(IdCommande):
    Info = (IdCommande,)
    Req = "SELECT * FROM InfoCommande WHERE IdCommande = %s"
    Cursor.execute(Req,Info)
    return Cursor.fetchall()
Data = DetailCommande(IdCommande)

for i in Data :

    pdf.set_font("helvetica", "i",5)
    pdf.cell(42,3, str(i[3]), border = 0)                        ##### Actes
    #pdf.set_font("helvetica", "i", 7)
    pdf.cell(10,3, str(i[4]), border = 0, align= "c")            ##### PU
    pdf.cell(7,3, str(i[5]), border = 0, align= "c")            ##### Qte
    pdf.cell(10,3, str(i[6]), border = 0, align= "c")            ##### Total
    pdf.cell(7,3, str(i[9]), border = 0, align= "c")             ##### Taux
    pdf.cell(10,3, str(i[7]), border = 0, align= "c")             ##### MtPec
    pdf.cell(10,3, str(i[8]), border = 0, align= "c", ln=1)       ##### MtPaye


pdf.set_font("helvetica", "i",8)
pdf.cell(00,2,border=0,ln=1)
pdf.cell(00,7, "PRISE EN CHARGE", border = 0, align= "c", ln=1)

#pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
#pdf.set_xy(5, 32)

pdf.cell(50,4, str(DataP[6]) , border = 0)                           #### "AssurancePec"
pdf.set_font("helvetica", "i", 8)
pdf.cell(40,4, str(DataP[15]) , align= "r", border = 0, ln=1)         #### "Nom assure"
pdf.cell(21,4, str(DataP[7]) , border = 0)                           #### "Taux"
pdf.cell(30,4, str(DataP[4]) , border = 0)                            ### "MontantPec"
pdf.cell(40,4, str(DataP[16]) , align= "r", border = 0, ln=1)        #### "Code assure"

###################################### RECU SERVICE ###########################################
###################################### RECU SERVICE ###########################################

pdf.add_page()

pdf.cell(00,7, "REÇU SERVICE", border = 0, align= "c", ln=1)


pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
pdf.set_xy(5, 32)

pdf.cell(64,13, str(DataP[2]) , border = 1)                #### "Nom et prénom"
pdf.set_font("helvetica", "i", 8)
pdf.cell(2,4,border=0)
pdf.cell(15,4, str(DataP[8]) , border = 0)                 #### "Age"
pdf.cell(23,4, str(DataP[9]) , border = 0, ln=1)           ### "Sexe"

pdf.cell(65,10, border = 0)
pdf.cell(20,10, str(DataP[10]) , border = 0)                 #### "Groupe"
pdf.cell(18,10, str(DataP[11]) , border = 0, ln=1)           #### "Patho"

## Label
pdf.set_xy(5, 45)

pdf.cell(32,7, "Montant Total", border = 1)
pdf.cell(32,7, "Montant Assurance", border = 1)
pdf.cell(32,7, "Montant Payé", border = 1, ln=1)

## Data
pdf.set_font("helvetica", "B", 9)
pdf.cell(32,7, str(DataP[3]) , border = 0)                            ### "DataMontant Total"
pdf.cell(32,7, str(DataP[4]) , border = 0)                            ### "DataMontant Assurance"
pdf.set_font("helvetica", "B", 10)
pdf.cell(32,6, str(DataP[5]) , border = 0, ln=1)                     ### "DataMontant Payé"

pdf.set_font("helvetica", "i", 8)
pdf.set_xy(5, 58)
pdf.set_text_color(255,0,0)                                   ##### num2words(42, lang='fr')
MtEnLettres = num2words(str(DataP[5]), lang="fr")
pdf.cell(00,7, MtEnLettres+" "+"francs CFA" , border = 0, ln=1)                        ### "Montant en lettres"

pdf.set_font("helvetica", "i", 8 )
pdf.set_text_color(0,0,0)
pdf.cell(00,7, "DETAILS", border = 0, align= "c", ln=1)

pdf.dashed_line(0,65,150,65)
pdf.set_xy(5, 72)
pdf.set_font("helvetica", "i", 7)
## Label
pdf.cell(42,4, "Actes", border = 1, align= "l")
pdf.cell(10,4, "PU", border = 1, align= "c")
pdf.cell(7,4, "Qte", border = 1, align= "c")
pdf.cell(10,4, "Total", border = 1, align= "c")
pdf.cell(7,4, "Taux", border = 1, align= "c")
pdf.cell(10,4, "Mt Pec", border = 1, align= "c")
pdf.cell(10,4, "Mt Payé", border = 1, ln=1, align= "c")
### Data
pdf.set_font("helvetica", "i",6)
pdf.set_xy(5, 77)

### Data

def DetailCommande(IdCommande):
    Info = (IdCommande,)
    Req = "SELECT * FROM InfoCommande WHERE IdCommande = %s"
    Cursor.execute(Req,Info)
    return Cursor.fetchall()
Data = DetailCommande(IdCommande)

for i in Data :

    pdf.set_font("helvetica", "i",5)
    pdf.cell(42,3, str(i[3]), border = 0)                        ##### Actes
    #pdf.set_font("helvetica", "i", 7)
    pdf.cell(10,3, str(i[4]), border = 0, align= "c")            ##### PU
    pdf.cell(7,3, str(i[5]), border = 0, align= "c")            ##### Qte
    pdf.cell(10,3, str(i[6]), border = 0, align= "c")            ##### Total
    pdf.cell(7,3, str(i[9]), border = 0, align= "c")             ##### Taux
    pdf.cell(10,3, str(i[7]), border = 0, align= "c")             ##### MtPec
    pdf.cell(10,3, str(i[8]), border = 0, align= "c", ln=1)       ##### MtPaye


pdf.set_font("helvetica", "i",8)
pdf.cell(00,2,border=0,ln=1)
pdf.cell(00,7, "PRISE EN CHARGE", border = 0, align= "c", ln=1)

#pdf.cell(00,3, border = 0, ln=1)
pdf.set_font("helvetica", "i", 9 )
#pdf.set_xy(5, 32)

pdf.cell(50,4, str(DataP[6]) , border = 0)                           #### "AssurancePec"
pdf.set_font("helvetica", "i", 8)
pdf.cell(40,4, str(DataP[15]) , align= "r", border = 0, ln=1)         #### "Nom assure"
pdf.cell(21,4, str(DataP[7]) , border = 0)                           #### "Taux"
pdf.cell(30,4, str(DataP[4]) , border = 0)                            ### "MontantPec"
pdf.cell(40,4, str(DataP[16]) , align= "r", border = 0, ln=1)        #### "Code assure"

Chemin = "formatA6.pdf"
os.system(Chemin)

# valeur 1 = largeur  valeur 2 = hauteur   cell 1 = Nom de la cellule   border = 1 veut dire bordure de la cellule est 1
# Pour mettre une cellule sous une autre il faut faire: pdf.cell(60,7, "Nom et prénom", border = 1)
pdf.output("formatA6.pdf")