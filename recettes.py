import random
import sys, hashlib, os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from datetime import date
from datetime import datetime, date, time

import fPDF
#from stock import Ui_MainWindow
from recettesDiverses import Ui_MainWindow
from tools import Req
from admin import Admin
import formatA6



class Recettes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Recettes, self).__init__()
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.Ui.retranslateUi(self)
        self.ReqInstance = Req()
        self.AdminInstance = Admin()
        #self.FPDFInstance = FPDF()
        #self.MyPDFInstance = MyPDF()
        #self.XXXXInstance = FPDF()
        #self.genererPdfInstance = generer_pdf()
        #self.ConnectInstance = Connect()
        self.Ui.PageMenu.setCurrentIndex(7)  # ouvrir sur la première page
        self.Ui.PageContent.setCurrentIndex(17)  # ouvrir sur la première page

        #self.Operateur = self.Ui.OperateurLineEdit_2

        self.Ui.ConnexionUserBtn.clicked.connect(self.GetCurrentUser)
        self.Ui.ConnexionUserBtn.clicked.connect(self.Orientation)



    # Menu de navigation
    # Partie 1
        self.Ui.ActesBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(1))
        self.Ui.RetourProduitBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(5))

        self.Ui.PatientBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(2))
        self.Ui.RetourClientBtn.clicked.connect(lambda: self.Ui.PageMenu.setCurrentIndex(5))

        self.Ui.AdmissionBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(3))
        self.Ui.RetourCommandeBtn.clicked.connect(lambda: self.Ui.PageMenu.setCurrentIndex(5))



        #self.Ui.CaisseBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(4))
        self.Ui.RetourStockBtn.clicked.connect(lambda: self.Ui.PageMenu.setCurrentIndex(5))

        self.Ui.QuitterRecettesBtn.clicked.connect(lambda : self.close())                  # pour quitter l'application


    # Partie 2
        self.Ui.MenuPrincipalRecettesBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(17))

        self.Ui.VoirProduitBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(1))
        self.Ui.AjouterProduitBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(2))
        self.Ui.ModifierProduitBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(3))

        self.Ui.VoirClientBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(5))
        self.Ui.VoirClientBtn.clicked.connect(self.ShowClient)
        self.Ui.AjouterClientBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(6))
        self.Ui.ModifierClientBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(7))

        self.Ui.AssureBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(14))
        self.Ui.AssureInamBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(18))
        self.Ui.AssureBtn.clicked.connect(self.ShowAssure)



        self.Ui.HistoriqueCommandeBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(9))
        self.Ui.AjouterCommandeBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(10))
        self.Ui.AjouterCommandeBtn.clicked.connect(self.GetCurrentUser)
        #self.Ui.ModifierCommandeBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(11))

        self.Ui.HistoriqueStockBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(12))
        self.Ui.HistoriqueStockBtn.clicked.connect(self.ShowStock)
        self.Ui.RavitaillerStockBtn.clicked.connect(self.Ravitailler)
        self.Ui.StockRavitaillerBtn.clicked.connect(self.UpdateStock)
        self.Ui.StockRavitaillerBtn.hide()
        self.Ui.StockQuantiteLineEdit.hide()

        self.Ui.CaisseBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(6))
        self.Ui.RetournerAuMenuBtn.clicked.connect(lambda : self.Ui.PageMenu.setCurrentIndex(5))
        self.Ui.EncaissementBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(15))
        self.Ui.BrouillardBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(16))
        self.Ui.EtatRecettesBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(22))
        self.Ui.AnnulationsBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(23))

    # Fin menu de navigation

    # Connexions des différents boutons de l'application

        self.Ui.AjoutProduitBtn.clicked.connect(self.AddProduit) # si on clique sur AjoutProduitBtn on se connecte à AddProduit
        self.Ui.VoirProduitBtn.clicked.connect(self.ShowProduit) # si on clique sur VoirProduitBtn on se connecte à ShowProduit
        self.Ui.ModifierProduitBtn.clicked.connect(self.ModifProduit) # si on clique sur ModifierProduitBtn on se connecte à ModifProduit
        self.Ui.UpdateProduitBtn.clicked.connect(self.UpdateProduit)  # si on clique sur UpdateProduitBtn on se connecte à UpdateProduit
        self.Ui.ProduitCreerBtn.clicked.connect(self.CreerNouveauProduit)
        self.Ui.ModifProduitCreerBtn.clicked.connect(self.CreerUpdateProduit)

        self.Ui.AjoutClientBtn.clicked.connect(self.AddClient)
        self.Ui.VoirClientBtn.clicked.connect(self.ShowClient)
        self.Ui.ModifierClientBtn.clicked.connect(self.ModifClient)
        self.Ui.UpdateClientBtn.clicked.connect(self.UpdateClient)
        self.Ui.TableauClient.doubleClicked.connect(self.RemplirPatient)
        #self.Ui.RetraitClientBtn.clicked.connect(self.DeleteClient)
        self.Ui.NouveauClientBtn.clicked.connect(self.NouveauClient)
        self.Ui.NouveauClientBtn.clicked.connect(self.NumPatient)
        self.Ui.ActiverComboBoxModifClientBtn.clicked.connect(self.ActiverComboBoxModifClient)
        self.Ui.AnneeCalculBtn.clicked.connect(self.CalculerAnnee)
        self.Ui.AgeCalculBtn.clicked.connect(self.CalculerAge)
        self.Ui.RechercheClientBox.currentIndexChanged.connect(self.SearchParNom)
        self.Ui.TableauRecherchePatient.doubleClicked.connect(self.SerachRemplirPatient)


        # sur assurance ou prise charge
        self.Ui.NouveauAssureBtn.clicked.connect(self.CreerNouvelAssure)
        self.Ui.AjoutAssureBtn.clicked.connect(self.AddAssure)
        self.Ui.AjoutAssureInamBtn.clicked.connect(self.AddAssureINAM)
        self.Ui.SiAssureBtn.clicked.connect(self.ChoisirAssure)
        self.Ui.AssureBtn.clicked.connect(self.ShowAssure)
        self.Ui.TableauAjoutAssure.doubleClicked.connect(self.RemplirAssure)
        #self.Ui.AppliquerAssuranceBtn.clicked.connect(self.AppliquerPec)

        # sur commande
        self.Ui.NouveauCmdBtn.clicked.connect(self.NouvelleCommande)
        self.Ui.AjoutAMaCommandeBtn.clicked.connect(self.AddCommande)
        self.Ui.AjoutCommandeOkProduitBtn.clicked.connect(self.AddCommandeOkProduit)
        self.Ui.AjoutCommandeInamOkProduitBtn.clicked.connect(self.AddCommandeInamOkProduit)
        self.Ui.RetirerDeMaCommandeBtn.clicked.connect(self.RetireDeCommande)
        self.Ui.RetirerDeMaCommandeInamBtn.clicked.connect(self.RetireDeCommande)
        self.Ui.ValiderCommandeBtn.clicked.connect(self.ValideCommande)
        self.Ui.HistoriqueCommandeBtn.clicked.connect(self.ShowCommande)
        self.Ui.TableauCommande.doubleClicked.connect(self.ShowDetailCommande)
        self.Ui.AnnulerCmdBtn.clicked.connect(self.AnnulerSaisie)
        #self.Ui.AppliquerAssuranceBtn.clicked.connect(self.AppliquerPec)
        self.Ui.AjoutCommandeOkNomBtn.clicked.connect(self.RemplirNomPatient)
        self.Ui.AjoutCommandeInamOkNomBtn.clicked.connect(self.RemplirNomPatientInam)

        # sur commande INAM
        self.Ui.InamBtn.clicked.connect(lambda : self.Ui.PageContent.setCurrentIndex(19))
        self.Ui.InamBtn.clicked.connect(self.ShowAssureInam)
        self.Ui.NouveauCmdInamBtn.clicked.connect(self.NouvelleCommandeInam)
        self.Ui.TableauClientInam.doubleClicked.connect(self.RemplirPatientInam)
        self.Ui.AjoutAMaCommandeInamBtn.clicked.connect(self.AddCommandeInam)
        # self.Ui.RetirerDeMaCommandeBtn.clicked.connect(self.DeleteDeCommande)
        self.Ui.ValiderCommandeInamBtn.clicked.connect(self.ValideCommandeInam)
        self.Ui.NouveauAssureInamBtn.clicked.connect(self.CreerNouvelAssureInam)
        self.Ui.SiAssureInamBtn.clicked.connect(self.ChoisirAssureInam)
        self.Ui.AssureInamBtn.clicked.connect(self.ChoisirAssureInam)
        self.Ui.TableauAjoutAssureInam.doubleClicked.connect(self.RemplirAssureInam)
        # self.Ui.HistoriqueCommandeBtn.clicked.connect(self.ShowCommande)
        # self.Ui.TableauCommande.doubleClicked.connect(self.ShowDetailCommande)
        self.Ui.AnnulerCmdInamBtn.clicked.connect(self.AnnulerSaisieInam)



        #### ENCAISSEMENT DES RECETTES

        self.Ui.EncaissementBtn.clicked.connect(self.GetCurrentUser)
        self.Ui.EncaissementBtn.clicked.connect(self.ShowCommandeCaisse)
        self.Ui.TableauCaisse.clicked.connect(self.ShowDetailCaisse)
        self.Ui.TableauCaisse.clicked.connect(self.RemplirlesChamps)
        self.Ui.RappelNumCommandeBtn.clicked.connect(self.RappelCommandeCaisseById)
        self.Ui.CreerLigneAvecIdMax.clicked.connect(self.CreerLigneAvecIdMax)
        self.Ui.CreerLigneAvecIdMax.clicked.connect(self.AddToCaisse)
        #self.Ui.ValiderCaisseBtn.clicked.connect(fPDF.createPdf)
        self.Ui.ValiderCaisseBtn.clicked.connect(self.PrintRecuCaisse)
        #self.Ui.ValiderCaisseBtn.clicked.connect(self.AddToCaisse)
        #self.Ui.ValiderCaisseBtn.clicked.connect(self.PrintDocument)
        self.Ui.CaisseActualiserBtn.clicked.connect(self.ActualiserCaisse)
        self.Ui.RappelNumCommandePharmaBtn.clicked.connect(self.RappelCommandePharmaById)
        self.Ui.AnnulerPharmaValiderBtn.clicked.connect(self.AnnulationPharma)
        self.Ui.TableauAnnulationPharma.clicked.connect(self.ShowAnnulationDetailPharma)
        self.Ui.RappelNumCommandeCaisseBtn.clicked.connect(self.RappelCommandeCaisseById)
        self.Ui.AnnulerCaisseValiderBtn.clicked.connect(self.AnnulationCaisse)
        self.Ui.TableauAnnulationCaisse.clicked.connect(self.ShowAnnulationDetailCaisse)



        ########## ETATS DES RECETTES ##########

        #self.Ui.BrouillardBtn.clicked.connect(self.BrouillardDeCaisse)
        self.Ui.AfficherRecettesDuJourBtn.clicked.connect(self.RecettesDuJour)
        self.Ui.TableauBrouillard.doubleClicked.connect(self.ShowDetailCaisseByIdCommande)
        self.Ui.EtatRecettesParCompte.clicked.connect(self.RecettesParCompte)




        self.Ligne = 0

    #####       CONNECXION    #####

    def GetCurrentUser(self):
        with open("user.txt", "r") as IdUsers:
            IdUsers = IdUsers.read()

            Ut = Req()
            Ut = (Ut.GetCurrentUserById(IdUsers))
            # print(Ut)

            A = Ut[0]
            B = Ut[1]
            C = Ut[2]
            D = Ut[3]

            self.IdUsers = A
            self.Operateur = B + " " + C
            self.Departement = D

            self.Ui.AjoutCommandeUserIdLabel.setText(str(self.IdUsers))
            self.Ui.AjoutCommandeUserLabel.setText(str(self.Operateur))

            self.Ui.AjoutCommandeInamUserIdLabel.setText(str(self.IdUsers))
            self.Ui.AjoutCommandeInamUserLabel.setText(str(self.Operateur))

            self.Ui.CaissierIdLabel.setText(str(self.IdUsers))
            self.Ui.CaissierUserLabel.setText(str(self.Operateur))

            self.Ui.UserIdLabel.setText(str(self.IdUsers))
            self.Ui.UserLabel.setText(str(self.Operateur))
            self.Ui.UserDepartementLabel.setText(str(self.Departement))

    def Orientation(self):
        UserDepartement = self.Ui.UserDepartementLabel.text()
        User = self.Ui.UserLabel.text()
        UserId = self.Ui.UserIdLabel.text()

        if UserDepartement == "ORDONNATEUR":
            self.Ui.PageMenu.setCurrentIndex(2)

        elif UserDepartement == "CAISSE":
            self.Ui.PageMenu.setCurrentIndex(5)

        elif UserDepartement == "PHARMACIE":
            self.Ui.PageMenu.setCurrentIndex(3)

        else:
            pass

    def CreerNouveauProduit(self):

        with open("user.txt", "r") as IdUsers:

            IdUsers = IdUsers.read()

            # Ut = User()
            Ut = Req()
            Ut = (Ut.GetCurrentUserById(IdUsers))
            # print(Ut)

            A = Ut[0]
            B = Ut[1]
            C = Ut[2]
            self.IdUsers = A
            self.Operateur = B + " " + C


        self.Ui.AjoutProduitUserLabel.setText(str(self.Operateur))
        self.Ui.AjoutProduitUserIdLabel.setText(str(self.IdUsers))

        # self.Ui.ProduitConditionnBox.clear()
        # self.Ui.ProduitDatePeremptionBox.clear()
        self.Ui.ProduitCatSoinsBox.clear()
        self.Ui.ProduitDepartementBox.clear()
        self.Ui.ProduitCatPatientBox.clear()
        self.Ui.ProduitCompteBudgetBox.clear()


        for i in self.AdminInstance.ShowCatSoins():
            self.IdCatSoins = i[0]
            CatSoins = i[1]
            self.Ui.ProduitCatSoinsBox.addItem(CatSoins)

        for i in self.AdminInstance.ShowDepartement():
            self.IdDepartement = i[0]
            Departement = i[1]
            self.Ui.ProduitDepartementBox.addItem(Departement)

        for i in self.AdminInstance.ShowCatPatient():
            self.IdCatPatient = i[0]
            CatPatient = i[1]
            self.Ui.ProduitCatPatientBox.addItem(CatPatient)

        for i in self.AdminInstance.ShowCompteBudget():
            self.IdCompteBudget = i[0]
            X = i[2]
            Y = i[3]
            CompteBudget = str(i[2]) + " " + " " + i[3]
            self.Ui.ProduitCompteBudgetBox.addItem(CompteBudget)

    # Creer Btn avant de commencer UpdateProduit

    def CreerUpdateProduit(self):

        self.Ui.ModifProduitCatSoinsBox.clear()
        self.Ui.ModifProduitDepartementBox.clear()
        self.Ui.ModifProduitCatPatientBox.clear()
        self.Ui.ModifProduitCompteBudgetBox.clear()

        for i in self.AdminInstance.ShowCatSoins():
            self.IdCatSoins = i[0]
            CatSoins = i[1]
            self.Ui.ModifProduitCatSoinsBox.addItem(CatSoins)

        for i in self.AdminInstance.ShowDepartement():
            self.IdDepartement = i[0]
            Departement = i[1]
            self.Ui.ModifProduitDepartementBox.addItem(Departement)

        for i in self.AdminInstance.ShowCatPatient():
            self.IdCatPatient = i[0]
            CatPatient = i[1]
            self.Ui.ModifProduitCatPatientBox.addItem(CatPatient)

        for i in self.AdminInstance.ShowCompteBudget():
            self.IdCompteBudget = i[0]
            X = i[2]
            Y = i[3]
            CompteBudget = str(i[2]) +" "+" "+ i[3]
            self.Ui.ModifProduitCompteBudgetBox.addItem(CompteBudget)

    # Annuler la saisie admission

    def AnnulerSaisie(self):

        self.Ui.TableauAjouterCommande.clear()
        self.Ui.AjoutCommandeProduitBox.setCurrentText(" ")
        #self.Ui.AjoutCommandeQteLineEdit.clear()
        #self.Ui.TableauAjouterCommande.clear()
        self.Ui.AjoutCommandeNomLineEdit.setText(" ")
        self.Ui.AjoutCommandeAgeLineEdit.setText(" ")
        self.Ui.AjoutCommandeSexeLineEdit.setText(" ")
        self.Ui.AjoutCommandeGroupageLineEdit.setText(" ")
        self.Ui.AjoutCommandePathologieLineEdit.setText(" ")
        self.Ui.AjoutCommandeTelephoneLineEdit.setText(" ")
        self.Ui.AjoutCommandeAdresseLineEdit.setText(" ")
        self.Ui.AjoutCommandeQteExistLineEdit.setText(" ")
        self.Ui.AjoutCommandePULineEdit.setText(" ")
        self.Ui.AjoutCommandePrixInamLineEdit.setText(" ")
        self.Ui.AjoutCommandeTauxInamLineEdit.setText(" ")
        self.Ui.AjoutCommandeQteLineEdit.setText("1")
        self.Ui.AjoutCommandeNomAssureLineEdit.setText(" ")
        self.Ui.AjoutCommandeAssurePecLineEdit.setText(" ")
        self.Ui.AjoutCommandeAssureTauxLineEdit.setText("0")
        self.Ui.AjoutCommandeCodeAssureLineEdit.setText(" ")
        self.Ui.AjoutCommandeCodeFeuilletLineEdit.setText(" ")
        self.Ui.AjoutCommandeAssureStatutLineEdit.setText(" ")
        self.Ui.NumPatientLineEdit.setText(" ")
        self.Ui.PrixTotalLabel.setText("0")
        self.Ui.PrixPecLabel.setText("0")
        self.Ui.PrixPayeLabel.setText("0")
        self.Ui.AjoutCommandeIdCommandeLineEdit.setText("0")

        self.Ligne = 0;
        #

    def AnnulerSaisieInam(self):

        self.Ui.TableauAjouterCommandeInam.clear()
        self.Ui.AjoutCommandeInamProduitBox.setCurrentText(" ")
        #self.Ui.AjoutCommandeQteLineEdit.clear()
        #self.Ui.TableauAjouterCommande.clear()
        self.Ui.AjoutCommandeInamNomLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamAgeLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamSexeLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamGroupageLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamPathologieLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamTelephoneLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamAdresseLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamQteExistLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamPULineEdit.setText(" ")
        self.Ui.AjoutCommandeInamPrixInamLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamTauxInamLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamQteLineEdit.setText("1")
        self.Ui.AjoutCommandeInamNomAssureLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamAssurePecLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamAssureTauxLineEdit.setText("0")
        self.Ui.AjoutCommandeInamCodeAssureLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamCodeFeuilletLineEdit.setText(" ")
        self.Ui.AjoutCommandeInamAssureStatutLineEdit.setText(" ")
        self.Ui.NumPatientInamLineEdit.setText(" ")
        self.Ui.PrixTotalInamLabel.setText("0")
        self.Ui.PrixPecInamLabel.setText("0")
        self.Ui.PrixPayeInamLabel.setText("0")
        self.Ui.AjoutCommandeInamIdCommandeLineEdit.setText("0")

        self.Ligne = 0;

    # Ajouter les produits en base de données

    def AddProduit(self):

        Libelle = self.Ui.ProduitLibelleLineEdit.text()  # récupérer le text du libellé
        PU = self.Ui.ProduitPrixUnitLineEdit.text()  # récupérer le text du PU
        PrixInam = self.Ui.ProduitPrixInamLineEdit.text()
        TauxInam = self.Ui.ProduitTauxInamLineEdit.text()
        CatSoins = self.Ui.ProduitCatSoinsBox.currentText()
        Departement = self.Ui.ProduitDepartementBox.currentText()
        CatPatient = self.Ui.ProduitCatPatientBox.currentText()
        CompteBudget = self.Ui.ProduitCompteBudgetBox.currentText()
        #Date = datetime.datetime.today().strftime("%d %m %Y")
        Date = datetime.today()
        Operateur = self.Operateur
        Data = (Libelle, PU, PrixInam, TauxInam, CatSoins, Departement, CatPatient, CompteBudget, Date, Operateur)

        if self.ReqInstance.AddActes(Libelle, PU, PrixInam, TauxInam, CatSoins, Departement, CatPatient,CompteBudget) == 0:
            self.Ui.AjouterProduitLabel.setText("L'acte a été bien ajouté.")
            self.Ui.AjouterProduitLabel.setStyleSheet("color: green;")
            self.Ui.ProduitLibelleLineEdit.setText("")
            self.Ui.ProduitPrixUnitLineEdit.setText("")
            self.Ui.ProduitPrixInamLineEdit.setText("")
            self.Ui.ProduitTauxInamLineEdit.setText("")
            self.Ui.ProduitCatSoinsBox.setCurrentText("")
            self.Ui.ProduitDepartementBox.setCurrentText("")
            self.Ui.ProduitCatPatientBox.setCurrentText("")
            self.Ui.ProduitCompteBudgetBox.setCurrentText("")


    # Afficher les actes

    def ShowProduit(self):
        Operateur = self.Operateur
        self.Ui.TableauProduit.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowActes():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauProduit)  # je crée une ligne vide
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la table Produit
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauProduit.topLevelItem(Ligne).setText(9, str(i[9]))

            Ligne += 1                                                             # j'incrémente Ligne à 1

    # Modifier un produit existant
    # Partie 1
    def ModifProduit(self):

        try:
            self.Id = self.Ui.TableauProduit.selectedItems()[0].text(0)          # je récupère l'Id
            self.Libelle = self.Ui.TableauProduit.selectedItems()[0].text(1)     # je récupère le Libellé
            self.PU = self.Ui.TableauProduit.selectedItems()[0].text(2)          # je récupère le PU
            self.PrixInam = self.Ui.TableauProduit.selectedItems()[0].text(3)
            self.TauxInam = self.Ui.TableauProduit.selectedItems()[0].text(4)
            self.CatSoins = self.Ui.TableauProduit.selectedItems()[0].text(8)
            self.Departement= self.Ui.TableauProduit.selectedItems()[0].text(9)
            self.CatPatient = self.Ui.TableauProduit.selectedItems()[0].text(10)
            self.CompteBudget = self.Ui.TableauProduit.selectedItems()[0].text(11)

            self.Ui.ModifProduitLibelleLineEdit.setText(self.Libelle)                # j'affiche les éléments sélectionné dans leurs champs de modif
            self.Ui.ModifProduitPULineEdit.setText(self.PU)
            self.Ui.ModifProduitPrixInamLineEdit.setText(self.PrixInam)
            self.Ui.ModifProduitTauxInamLineEdit.setText(self.TauxInam)
            self.Ui.ModifProduitCatSoinsBox.setCurrentText(self.CatSoins)
            self.Ui.ModifProduitDepartementBox.setCurrentText(self.Departement)
            self.Ui.ModifProduitCatPatientBox.setCurrentText(self.CatPatient)
            self.Ui.ModifProduitCompteBudgetBox.setCurrentText(self.CompteBudget)
        except:
            self.Ui.PageContent.setCurrentIndex(1)
            self.ReqInstance.ShowProduit()

    # Partie 2
    def UpdateProduit(self):
        self.Libelle = self.Ui.ModifProduitLibelleLineEdit.text()  # je récupère le nouveau Libelle
        self.PU = self.Ui.ModifProduitPULineEdit.text()           # je récupère le nouveau PU
        self.PrixInam = self.Ui.ModifProduitPrixInamLineEdit.text()
        self.TauxInam = self.Ui.ModifProduitTauxInamLineEdit.text()
        self.CatSoins = self.Ui.ModifProduitCatSoinsBox.currentText()
        self.Departement = self.Ui.ModifProduitDepartementBox.currentText()
        self.CatPatient = self.Ui.ModifProduitCatPatientBox.currentText()
        self.CompteBudget = self.Ui.ModifProduitCompteBudgetBox.currentText()
        Data = (self.Libelle, self.PU, self.PrixInam, self.TauxInam, self.CatSoins, self.Departement, self.CatPatient, self.CompteBudget, self.Id)

        if self.ReqInstance.UpdateActes(Data) == 0 :

            self.ShowProduit()                             # pour affichage de la modification
            self.Ui.PageContent.setCurrentIndex(1)         # je retourne sur la page voir les produits

            Libelle = self.Libelle
            IdProduit = self.ReqInstance.GetActesIdByName(Libelle)
            # Libelle, on l'a déjà dans cette méthode
            # Quantite = 0  # parce que la mise à jour ne touche pas la quantité
            Data = (IdProduit, Libelle)
            #self.ReqInstance.UpdateProduitStock(Data)  # pour exécuter ma requête de mise à jour du libelle dans la table stock

    # Nouveau client

    def NouveauClient(self):

        self.Ui.AnneeNaissanceBox.clear()
        self.Ui.TypeAgeBox.clear()
        self.Ui.SexeBox.clear()
        self.Ui.ProfessionBox.clear()
        self.Ui.PathologieBox.clear()
        self.Ui.GroupeSanguinBox.clear()

        for i in self.AdminInstance.ShowAnnee():
            self.IdAnnee = i[0]
            Annee = str(i[1])
            self.Ui.AnneeNaissanceBox.addItem(Annee)

        for i in self.AdminInstance.ShowTypeAnnee():
            self.IdTypeAnnee = i[0]
            TypeAnnee = i[1]
            self.Ui.TypeAgeBox.addItem(TypeAnnee)

        for i in self.AdminInstance.ShowSexe():
            self.IdSexe = i[0]
            Sexe = i[1]
            self.Ui.SexeBox.addItem(Sexe)

        for i in self.AdminInstance.ShowProfession():
            self.IdProfession = i[0]
            Profession = i[1]
            self.Ui.ProfessionBox.addItem(Profession)

        for i in self.AdminInstance.ShowPathologie():
            self.IdPathologie = i[0]
            Pathologie = i[1]
            self.Ui.PathologieBox.addItem(Pathologie)

        for i in self.AdminInstance.ShowGroupage():
            self.IdGroupage = i[0]
            Groupage = i[3]
            self.Ui.GroupeSanguinBox.addItem(Groupage)

    def NumPatient(self):
        IdClient = 0
        NumPatient = self.Ui.NumeroClientLineEdit.text()
        IdMaxClient = self.ReqInstance.GetIdMaxClient()
        IdClient += 1
        if self.ReqInstance.GetIdMaxClient() <= 8 :
            NumPat = "P"+str(0)+""+str(0)+""+str(0)+""+str(IdMaxClient+1)+"CNRSD"
            self.Ui.NumeroClientLineEdit.setText(NumPat)

        elif self.ReqInstance.GetIdMaxClient() >= 10 and IdClient < 99 :
            NumPat = "P"+str(0)+""+str(0)+""+str(IdMaxClient+1)+"CNRSD"
            self.Ui.NumeroClientLineEdit.setText(NumPat)

        elif self.ReqInstance.GetIdMaxClient() >= 100 and IdClient < 999 :
            NumPat = "P"+str(0)+""+str(IdMaxClient+1)+"CNRSD"
            self.Ui.NumeroClientLineEdit.setText(NumPat)

        elif self.ReqInstance.GetIdMaxClient() >= 1000 :
            NumPat = "P"+""+str(IdMaxClient+1)+"CNRSD"
            self.Ui.NumeroClientLineEdit.setText(NumPat)

        else:
            pass

    def CalculerAge(self):
        AnneeNaissance = self.Ui.AnneeNaissanceBox.currentText()
        self.Ui.AgeLineEdit.setText(str((date.today().year) - int(AnneeNaissance)))

    def CalculerAnnee(self):
        Age = self.Ui.AgeLineEdit.text()
        self.Ui.AnneeNaissanceBox.setCurrentText(str((date.today().year) - int(Age)))

    # Afficher les clients

    def ShowClient(self):
        self.Ui.TableauClient.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowClient():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauClient)  # je crée une ligne vide
            self.Ui.TableauClient.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la table Client
            self.Ui.TableauClient.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauClient.topLevelItem(Ligne).setText(13, str(i[13]))
            Ligne += 1

    # Ajouter les clients en base de données

    def AddClient(self):

        NumPatient = self.Ui.NumeroClientLineEdit.text()
        NomX = self.Ui.NomClientLineEdit.text()           # récupérer le text du Nom
        PrenomsX = self.Ui.PrenomClientLineEdit.text()    # récupérer le text du Prenom
        Nom = NomX +" "+ PrenomsX
        Adresse = self.Ui.AdresseLineEdit.text()
        Telephone = self.Ui.TelephoneLineEdit.text()
        AnneeNaissance = self.Ui.AnneeNaissanceBox.currentText()
        Age = self.Ui.AgeLineEdit.text()
        TypeAge = self.Ui.TypeAgeBox.currentText()
        Sexe = self.Ui.SexeBox.currentText()
        Profession = self.Ui.ProfessionBox.currentText()
        Pathologie = self.Ui.PathologieBox.currentText()
        GroupageSanguin = self.Ui.GroupeSanguinBox.currentText()
        Date = date.today()
        Data = (NumPatient,Nom, Adresse, Telephone, AnneeNaissance, Age, TypeAge, Sexe, Profession, Pathologie, GroupageSanguin, Date)

        if self.ReqInstance.AddClient(NumPatient,Nom, Adresse, Telephone, AnneeNaissance, Age, TypeAge, Sexe, Profession, Pathologie, GroupageSanguin) == 0:
            self.ShowClient()
            self.Ui.PageContent.setCurrentIndex(5)
            self.Ui.NumeroClientLineEdit.setText("")
            self.Ui.NomClientLineEdit.setText("")
            self.Ui.PrenomClientLineEdit.setText("")
            self.Ui.AdresseLineEdit.setText("")
            self.Ui.TelephoneLineEdit.setText("")
            self.Ui.AnneeNaissanceBox.setCurrentText("")
            self.Ui.AgeLineEdit.setText("")
            self.Ui.TypeAgeBox.setCurrentText("")
            self.Ui.SexeBox.setCurrentText("")
            self.Ui.ProfessionBox.setCurrentText("")
            self.Ui.PathologieBox.setCurrentText("")
            self.Ui.GroupeSanguinBox.setCurrentText("")

    # Modifier un client existant
    # Partie 1

    def ModifClient(self):

        try:
            self.Id = self.Ui.TableauClient.selectedItems()[0].text(0)  # je récupère l'Id
            self.NumPatient = self.Ui.TableauClient.selectedItems()[0].text(1)
            self.Nom = self.Ui.TableauClient.selectedItems()[0].text(2)  # je récupère le Libellé
            self.Prenoms = self.Ui.TableauClient.selectedItems()[0].text(3)  # je récupère le PU
            self.Adresse = self.Ui.TableauClient.selectedItems()[0].text(4)
            self.Telephone = self.Ui.TableauClient.selectedItems()[0].text(5)
            self.AnneeNaissance = self.Ui.TableauClient.selectedItems()[0].text(6)
            self.Age = self.Ui.TableauClient.selectedItems()[0].text(7)
            self.TypeAge = self.Ui.TableauClient.selectedItems()[0].text(8)
            self.Sexe = self.Ui.TableauClient.selectedItems()[0].text(9)
            self.Profession = self.Ui.TableauClient.selectedItems()[0].text(10)
            self.Pathologie = self.Ui.TableauClient.selectedItems()[0].text(11)
            self.GroupageSanguin = self.Ui.TableauClient.selectedItems()[0].text(12)

            self.Ui.ModifierNumClientLineEdit.setText(self.NumPatient)
            self.Ui.ModifierNomClientLineEdit.setText(self.Nom)  # j'affiche les éléments sélectionné dans leurs champs de modif
            self.Ui.ModifierPrenomClientLineEdit.setText(self.Prenoms)
            self.Ui.ModifierAdresseLineEdit.setText(self.Adresse)
            self.Ui.ModifierTelephoneLineEdit.setText(self.Telephone)
            self.Ui.ModifierAnneeNaissanceBox.setCurrentText(self.AnneeNaissance)
            self.Ui.ModifierAgeLineEdit.setText(self.Age)
            self.Ui.ModifierTypeAgeBox.setCurrentText(self.TypeAge)
            self.Ui.ModifierSexeBox.setCurrentText(self.Sexe)
            self.Ui.ModifierProfessionBox.setCurrentText(self.Profession)
            self.Ui.ModifierPathologieBox.setCurrentText(self.Pathologie)
            self.Ui.ModifierGroupeSanguinBox.setCurrentText(self.GroupageSanguin)
        except:
            self.ReqInstance.ShowClient()
            self.Ui.PageContent.setCurrentIndex(5)

    def ActiverComboBoxModifClient(self):

        self.Ui.ModifierAnneeNaissanceBox.clear()
        self.Ui.ModifierTypeAgeBox.clear()
        self.Ui.ModifierSexeBox.clear()
        self.Ui.ModifierProfessionBox.clear()
        self.Ui.ModifierPathologieBox.clear()
        self.Ui.ModifierGroupeSanguinBox.clear()

        for i in self.AdminInstance.ShowAnnee():
            self.IdAnnee = i[0]
            Annee = str(i[1])
            self.Ui.ModifierAnneeNaissanceBox.addItem(Annee)

        for i in self.AdminInstance.ShowTypeAnnee():
            self.IdTypeAnnee = i[0]
            TypeAnnee = i[1]
            self.Ui.ModifierTypeAgeBox.addItem(TypeAnnee)

        for i in self.AdminInstance.ShowSexe():
            self.IdSexe = i[0]
            Sexe = i[1]
            self.Ui.ModifierSexeBox.addItem(Sexe)

        for i in self.AdminInstance.ShowProfession():
            self.IdProfession = i[0]
            Profession = i[1]
            self.Ui.ModifierProfessionBox.addItem(Profession)

        for i in self.AdminInstance.ShowPathologie():
            self.IdPathologie = i[0]
            Pathologie = i[1]
            self.Ui.ModifierPathologieBox.addItem(Pathologie)

        for i in self.AdminInstance.ShowGroupage():
            self.IdGroupage = i[0]
            Groupage = i[3]
            self.Ui.ModifierGroupeSanguinBox.addItem(Groupage)

    # Partie 2

    def UpdateClient(self):
        self.NumPatient = self.Ui.ModifierNumClientLineEdit.text()
        self.Nom = self.Ui.ModifierNomClientLineEdit.text()  # je récupère le nouveau Nom
        self.Prenoms = self.Ui.ModifierPrenomClientLineEdit.text()  # je récupère le nouveau Prenom
        self.Adresse = self.Ui.ModifierAdresseLineEdit.text()
        self.Telephone = self.Ui.ModifierTelephoneLineEdit.text()
        self.AnneeNaissance = self.Ui.ModifierAnneeNaissanceBox.currentText()
        self.Age = self.Ui.ModifierAgeLineEdit.text()
        self.TypeAge = self.Ui.ModifierTypeAgeBox.currentText()
        self.Sexe = self.Ui.ModifierSexeBox.currentText()
        self.Profession = self.Ui.ModifierProfessionBox.currentText()
        self.Pathologie = self.Ui.ModifierPathologieBox.currentText()
        self.GroupageSanguin = self.Ui.ModifierGroupeSanguinBox.currentText()
        Data = (self.NumPatient, self.Nom, self.Prenoms, self.Adresse, self.Telephone, self.AnneeNaissance, self.Age, self.TypeAge, self.Sexe, self.Profession, self.Pathologie, self.GroupageSanguin)

        if self.ReqInstance.UpdateClient(Data) == 0:
            self.ShowClient()  # pour affichage de la modification
            self.Ui.PageContent.setCurrentIndex(5)  # je retourne sur la page voir les produits

    # Supprimer un client

    def DeleteClient(self):
        self.Id = self.Ui.TableauClient.selectedItems()[0].text(0)
        if self.ReqInstance.DeleteClient(self.Id) == 0:
            self.ShowClient()

    # pour ajouter une nouvelle commande
    def NouvelleCommande(self):

        QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommande)
        self.Ui.AjoutCommandeProduitBox.clear()
        self.Ui.AjoutCommandePatientBox.clear()

        ###################################
        #####################################
        ########################################
        IdCommande = 0
        IdUsers = self.Ui.AjoutCommandeUserIdLabel.text()
        Operateur = self.Ui.AjoutCommandeUserLabel.text()

        #DateCommande = datetime.datetime.today().strftime("%d %m %Y")
        DateCommande = date.today()

        # je crée une insertion de la variable dans la table commande

        #DateHeure = datetime.datetime.today().strftime("%d %m %Y / %H:%M:%S")
        DateHeure = datetime.now()
        Data = (IdUsers, Operateur, DateHeure)
        if self.ReqInstance.InsererIdCommande(IdUsers,Operateur, DateHeure) == 0:

            pass

        # après je récupère l'Id
        # IdCommande =  retour de GetIdMaxCommande ==MAXICOMMANDE

        Data = (IdUsers,)
        self.MAXICOMMANDE = self.ReqInstance.GetIdMaxCommande(Data)

        ### afficher numéro commande sur l'interface ##########

        self.Ui.AjoutCommandeIdCommandeLineEdit.setText(str(self.MAXICOMMANDE))

        for i in self.ReqInstance.ShowClient():
            IdClient = i[0]
            Num = i[1]
            Nom = i[2]
            Prenoms = i[3]
            NomPrenoms = Nom +" "+Prenoms
            self.Ui.AjoutCommandePatientBox.addItem(NomPrenoms)

        self.Ui.AjoutCommandeProduitBox.clear()

        for i in self.ReqInstance.ShowActes():
            self.IdProduit = i[0]
            Libelle = i[1]
            PU = i[2]
            PrixInam = i[3]
            TauxInam = i[4]
            CatSoins = i[5]
            Departement = i[6]
            CatPatient = i[7]
            CompteBudget = i[8]
            QuantiteExist = i[9]

            self.Ui.AjoutCommandeProduitBox.addItem(Libelle)
            self.Ui.MsgErreurIdCommande.hide()


    def RemplirNomPatient(self):
        NomPrenoms = self.Ui.AjoutCommandePatientBox.currentText()
        Patient = self.ReqInstance.GetPatientByName(NomPrenoms)[0]
        NumP = Patient[1]
        NomP = Patient[2]
        AgeX = Patient[3]
        AgeY = Patient[4]
        AgeP = AgeX +" "+ AgeY
        SexeP = Patient[5]
        GsP = Patient[8]
        PathP = Patient[7]
        TelP = Patient[9]
        AdressP = Patient[10]

        self.Ui.NumPatientLineEdit.setText(NumP)
        self.Ui.AjoutCommandeNomLineEdit.setText(NomP)
        self.Ui.AjoutCommandeAgeLineEdit.setText(AgeP)
        self.Ui.AjoutCommandeSexeLineEdit.setText(SexeP)
        self.Ui.AjoutCommandeGroupageLineEdit.setText(GsP)
        self.Ui.AjoutCommandePathologieLineEdit.setText(PathP)
        self.Ui.AjoutCommandeTelephoneLineEdit.setText(TelP)
        self.Ui.AjoutCommandeAdresseLineEdit.setText(AdressP)

    def NouvelleCommandeInam(self):

        QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommandeInam)
        self.Ui.AjoutCommandeInamProduitBox.clear()

        ###################################
        #####################################
        ########################################
        IdCommande = 0
        IdUsers = self.Ui.AjoutCommandeInamUserIdLabel.text()
        Operateur = self.Ui.AjoutCommandeInamUserLabel.text()

        #DateCommande = datetime.datetime.today().strftime("%d %m %Y")
        DateCommande = date.today()

        # je crée une insertion de la variable dans la table commande

        #DateHeure = datetime.datetime.today().strftime("%d %m %Y / %H:%M:%S")
        DateHeure = datetime.today()
        Data = (IdUsers, Operateur, DateHeure)
        if self.ReqInstance.InsererIdCommande(IdUsers,Operateur, DateHeure) == 0:

            pass

        # après je récupère l'Id
        # IdCommande =  retour de GetIdMaxCommande ==MAXICOMMANDE

        Data = (IdUsers,)
        self.MAXICOMMANDE = self.ReqInstance.GetIdMaxCommande(Data)

        ### afficher numéro commande sur l'interface ##########

        self.Ui.AjoutCommandeInamIdCommandeLineEdit.setText(str(self.MAXICOMMANDE))

        for i in self.ReqInstance.ShowClient():
            IdClient = i[0]
            Num = i[1]
            Nom = i[2]
            Prenoms = i[3]
            NomPrenoms = Nom + " " + Prenoms
            self.Ui.AjoutCommandePatientInamBox.addItem(NomPrenoms)

        for i in self.ReqInstance.ShowActes():
            self.IdProduit = i[0]
            Libelle = i[1]
            PU = i[2]
            PrixInam = i[3]
            TauxInam = i[4]
            CatSoins = i[5]
            Departement = i[6]
            CatPatient = i[7]
            CompteBudget = i[8]
            QuantiteExist = i[9]

            self.Ui.AjoutCommandeInamProduitBox.addItem(Libelle)
            self.Ui.MsgErreurIdCommandeInam.hide()


    def RemplirNomPatientInam(self):
        NomPrenoms = self.Ui.AjoutCommandePatientInamBox.currentText()
        Patient = self.ReqInstance.GetPatientByName(NomPrenoms)[0]
        NumP = Patient[1]
        NomP = Patient[2]
        AgeX = Patient[3]
        AgeY = Patient[4]
        AgeP = AgeX +" "+ AgeY
        SexeP = Patient[5]
        GsP = Patient[8]
        PathP = Patient[7]
        TelP = Patient[9]
        AdressP = Patient[10]

        self.Ui.NumPatientInamLineEdit.setText(NumP)
        self.Ui.AjoutCommandeInamNomLineEdit.setText(NomP)
        self.Ui.AjoutCommandeInamAgeLineEdit.setText(AgeP)
        self.Ui.AjoutCommandeInamSexeLineEdit.setText(SexeP)
        self.Ui.AjoutCommandeInamGroupageLineEdit.setText(GsP)
        self.Ui.AjoutCommandeInamPathologieLineEdit.setText(PathP)
        self.Ui.AjoutCommandeInamTelephoneLineEdit.setText(TelP)
        self.Ui.AjoutCommandeInamAdresseLineEdit.setText(AdressP)

    def SearchParNom(self):
        if self.Ui.RechercheClientBox.currentIndex() == 1:  # ma condition pour type de recherche (==1 ie 2è valeur, recherche par nom)
            Tag = self.Ui.RechercheClientLineEdit.text()  # je récupère la valeur saisie dans une variable
            for i in range(len(self.ReqInstance.SearchParNom(Tag))):  # condition pour le nombre de lignes à créer
                self.Ui.TableauRecherchePatient.addItem(QtWidgets.QListWidgetItem())  # code de création de lignes
                self.Ui.TableauRecherchePatient.item(i).setText(str(" ".join(str(self.ReqInstance.SearchParNom(Tag)[i]))))

            self.Ui.RechercheClientLineEdit.setText("")  ## pour vider le champs de recherche
            self.Ui.RechercheClientLineEdit.setText("")  ## pour vider le champs de recherche

    # Remplir infos patient de la commande

    def RemplirPatient(self):

        # Operateur = self.Operateur
        IdPatient = self.Ui.TableauClient.selectedItems()[0].text(0)

        self.Id = self.Ui.TableauClient.selectedItems()[0].text(0)  # je récupère l'Id
        self.NumPatient = self.Ui.TableauClient.selectedItems()[0].text(1)
        self.NomX = self.Ui.TableauClient.selectedItems()[0].text(2)  # je récupère le Libellé
        self.PrenomsY = self.Ui.TableauClient.selectedItems()[0].text(3)  # je récupère le PU
        self.NomPrenoms = self.NomX+" "+self.PrenomsY
        self.Adresse = self.Ui.TableauClient.selectedItems()[0].text(4)
        self.Telephone = self.Ui.TableauClient.selectedItems()[0].text(5)
        self.AgeX = self.Ui.TableauClient.selectedItems()[0].text(7)
        self.TypeAgeY = self.Ui.TableauClient.selectedItems()[0].text(8)
        self.Age = self.AgeX+" "+self.TypeAgeY
        self.Sexe = self.Ui.TableauClient.selectedItems()[0].text(9)
        self.Pathologie = self.Ui.TableauClient.selectedItems()[0].text(11)
        self.GroupageSanguin = self.Ui.TableauClient.selectedItems()[0].text(12)

        self.Ui.NumPatientLineEdit.setText(self.NumPatient)
        self.Ui.AjoutCommandeNomLineEdit.setText(self.NomPrenoms)  # j'affiche les éléments sélectionné dans leurs champs de modif
        #self.Ui.AjoutCommandePrenomLineEdit.setText(self.Prenoms)
        self.Ui.AjoutCommandeAgeLineEdit.setText(self.Age)
        self.Ui.AjoutCommandeSexeLineEdit.setText(self.Sexe)
        self.Ui.AjoutCommandeGroupageLineEdit.setText(self.GroupageSanguin)
        self.Ui.AjoutCommandePathologieLineEdit.setText(self.Pathologie)
        self.Ui.AjoutCommandeTelephoneLineEdit.setText(self.Telephone)
        self.Ui.AjoutCommandeAdresseLineEdit.setText(self.Adresse)

        self.Ui.PageContent.setCurrentIndex(10)

        # self.Ui.AjoutCommandeCatSoinsBox.clear()
        # self.Ui.AjoutCommandeDepartementBox.clear()
        # self.Ui.AjoutCommandeCatPatientBox.clear()

        self.Ui.AjoutCommandeProduitBox.clear()

        for i in self.ReqInstance.ShowActes():
            self.IdProduit = i[0]
            Libelle = i[1]
            PU = i[2]
            PrixInam = i[3]
            TauxInam = i[4]
            CatSoins = i[5]
            Departement = i[6]
            CatPatient = i[7]
            CompteBudget = i[8]
            QuantiteExist = i[9]

        ## Ici en commentaire

            self.Ui.AjoutCommandeProduitBox.addItem(Libelle)

        self.Ui.PageMenu.setCurrentIndex(3)

    def RemplirPatientInam(self):

        # Operateur = self.Operateur
        IdPatient = self.Ui.TableauClientInam.selectedItems()[0].text(0)

        self.Id = self.Ui.TableauClientInam.selectedItems()[0].text(0)  # je récupère l'Id
        self.NumPatient = self.Ui.TableauClientInam.selectedItems()[0].text(1)
        self.NomX = self.Ui.TableauClientInam.selectedItems()[0].text(2)  # je récupère le Libellé
        self.PrenomsY = self.Ui.TableauClientInam.selectedItems()[0].text(3)  # je récupère le PU
        self.NomPrenoms = self.NomX + " " + self.PrenomsY
        self.Adresse = self.Ui.TableauClientInam.selectedItems()[0].text(4)
        self.Telephone = self.Ui.TableauClientInam.selectedItems()[0].text(5)
        self.AgeX = self.Ui.TableauClientInam.selectedItems()[0].text(7)
        self.TypeAgeY = self.Ui.TableauClientInam.selectedItems()[0].text(8)
        self.Age = self.AgeX + " " + self.TypeAgeY
        self.Sexe = self.Ui.TableauClientInam.selectedItems()[0].text(9)
        self.Pathologie = self.Ui.TableauClientInam.selectedItems()[0].text(11)
        self.GroupageSanguin = self.Ui.TableauClientInam.selectedItems()[0].text(12)

        self.Ui.NumPatientInamLineEdit.setText(self.NumPatient)
        self.Ui.AjoutCommandeInamNomLineEdit.setText(self.NomPrenoms)
        self.Ui.AjoutCommandeInamAgeLineEdit.setText(self.Age)
        self.Ui.AjoutCommandeInamSexeLineEdit.setText(self.Sexe)
        self.Ui.AjoutCommandeInamGroupageLineEdit.setText(self.GroupageSanguin)
        self.Ui.AjoutCommandeInamPathologieLineEdit.setText(self.Pathologie)
        self.Ui.AjoutCommandeInamTelephoneLineEdit.setText(self.Telephone)
        self.Ui.AjoutCommandeInamAdresseLineEdit.setText(self.Adresse)

        self.Ui.PageContent.setCurrentIndex(18)

        self.Ui.AjoutCommandeProduitBox.clear()

        for i in self.ReqInstance.ShowActes():
            self.IdProduit = i[0]
            Libelle = i[1]
            PU = i[2]
            PrixInam = i[3]
            TauxInam = i[4]
            CatSoins = i[5]
            Departement = i[6]
            CatPatient = i[7]
            CompteBudget = i[8]
            QuantiteExist = i[9]

            ## Ici en commentaire

            self.Ui.AjoutCommandeInamProduitBox.addItem(Libelle)

        self.Ui.PageMenu.setCurrentIndex(3)

    def SerachRemplirPatient(self):
        IdPatient = self.Ui.TableauRecherchePatient.setSelectionMode(0)
        self.Id = self.Ui.TableauRecherchePatient.setSelectionMode(0) # je récupère l'Id
        self.NomX = self.Ui.TableauRecherchePatient.selectedItems()[0].text(2)  # je récupère le Libellé
        self.PrenomsY = self.Ui.TableauRecherchePatient.selectedItems()[0].text(3)  # je récupère le PU
        self.NomPrenoms = self.NomX + " " + self.PrenomsY
        self.Adresse = self.Ui.TableauRecherchePatient.selectedItems()[0].text(4)
        self.Telephone = self.Ui.TableauRecherchePatient.selectedItems()[0].text(5)
        self.AgeX = self.Ui.TableauRecherchePatient.selectedItems()[0].text(7)
        self.TypeAgeY = self.Ui.TableauRecherchePatient.selectedItems()[0].text(8)
        self.Age = self.AgeX + " " + self.TypeAgeY
        self.Sexe = self.Ui.TableauRecherchePatient.selectedItems()[0].text(9)
        self.Pathologie = self.Ui.TableauRecherchePatient.selectedItems()[0].text(11)
        self.GroupageSanguin = self.Ui.TableauRecherchePatient.selectedItems()[0].text(12)

    def AddCommandeOkProduit(self):

        Libelle = self.Ui.AjoutCommandeProduitBox.currentText()  # récupérer la valeur de produit

        # afficher les valeurs dans le tableau
        Info = self.ReqInstance.GetActesByName(Libelle)[0]  # en récupérant mon tuple
        Id = Info[0]  # et en récupérant la 1ère valeur Id de mon tuple
        PU = Info[1]  # et en récupérant la 2è valeur PU de mon tuple
        PrixInam = Info[2]
        TauxInam = Info[3]
        CatSoins = Info[4]
        Departement = Info[5]
        CatPatient = Info[6]
        CompteBudget = Info[7]
        # QuantiteExist = Info[8]

        self.Ui.AjoutCommandePULineEdit.setText(str(PU))
        self.Ui.AjoutCommandePrixInamLineEdit.setText(str(PrixInam))
        self.Ui.AjoutCommandeTauxInamLineEdit.setText(str(TauxInam))
        self.Ui.AjoutCommandeCatSoinsLineEdit.setText(CatSoins)
        self.Ui.AjoutCommandeDepartementLineEdit.setText(Departement)
        self.Ui.AjoutCommandeCatPatientLineEdit.setText(CatPatient)
        self.Ui.AjoutCommandeCompteBudgetLineEdit.setText(str(CompteBudget))
        # self.Ui.AjoutCommandeQteExistLineEdit.setText(str(QuantiteExist))

    def AddCommande(self):
        IdCom = self.Ui.AjoutCommandeIdCommandeLineEdit.text()
        #print(IdCom)
        if int(IdCom) > 0 :
            try:

                QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommande) # on doit créer une ligne vide pour les données à récupérer

                Qte = self.Ui.AjoutCommandeQteLineEdit.text()               # récupérer la valeur de quantité
                Taux = self.Ui.AjoutCommandeAssureTauxLineEdit.text()

                Libelle = self.Ui.AjoutCommandeProduitBox.currentText()  # récupérer la valeur de produit

                                                            # afficher les valeurs dans le tableau
                Info = self.ReqInstance.GetActesByName(Libelle)[0]   # en récupérant mon tuple
                Id = Info[0]   # et en récupérant la 1ère valeur Id de mon tuple
                PU = Info[1]   # et en récupérant la 2è valeur PU de mon tuple
                PrixInam = Info[2]
                TauxInam = Info[3]
                CatSoins = Info[4]
                Departement = Info[5]
                CatPatient = Info[6]
                CompteBudget = Info[7]
                #QuantiteExist = Info[8]


                self.Ui.AjoutCommandePULineEdit.setText(str(PU))
                self.Ui.AjoutCommandePrixInamLineEdit.setText(str(PrixInam))
                self.Ui.AjoutCommandeTauxInamLineEdit.setText(str(TauxInam))
                self.Ui.AjoutCommandeCatSoinsLineEdit.setText(CatSoins)
                self.Ui.AjoutCommandeDepartementLineEdit.setText(Departement)
                self.Ui.AjoutCommandeCatPatientLineEdit.setText(CatPatient)
                self.Ui.AjoutCommandeCompteBudgetLineEdit.setText(str(CompteBudget))
                #self.Ui.AjoutCommandeQteExistLineEdit.setText(str(QuantiteExist))

                # comme on a récupéré toutes données de notre détail commande, on va les insérer dans le tableau
                # de tel sorte qu'on peut ajouter plusieurs sur même commande d'où l'intervention de self.Ligne = 0 et self.Ligne +=1

                IdCommande = self.MAXICOMMANDE
                Data = (IdCommande)

                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(0, str(IdCommande))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(1,str(Id))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(2,str(Libelle))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(3,str(PU))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(4,str(Qte))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(5,str(int(PU)*int(Qte)))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(6, str(Taux))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(7, str(PrixInam))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(8, str(TauxInam))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(9, str(round(int(PU)*int(Qte)*int(Taux)/100)))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(10, str(round(int(PU)*int(Qte)-(int(PU)*int(Qte)*int(Taux)/100))))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(11, str(Departement))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(12, str(CatSoins))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(13, str(CatPatient))
                self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(14, str(CompteBudget))

                self.Ligne +=1

                # je vais calculer le montant brut

                ### Ajouter à la table TamponCommande

                for i in range(self.Ligne):
                    #IdCommande = self.ReqInstance.GetCommandeIdByUniqueId(UniqueId)
                    IdCommande = self.MAXICOMMANDE
                    IdProduit = self.Ui.TableauAjouterCommande.topLevelItem(i).text(1)
                    Libelle = self.Ui.TableauAjouterCommande.topLevelItem(i).text(2)
                    PU = self.Ui.TableauAjouterCommande.topLevelItem(i).text(3)
                    Quantite = self.Ui.TableauAjouterCommande.topLevelItem(i).text(4)
                    Total = self.Ui.TableauAjouterCommande.topLevelItem(i).text(5)
                    Taux = self.Ui.TableauAjouterCommande.topLevelItem(i).text(6)
                    PrixInam = self.Ui.TableauAjouterCommande.topLevelItem(i).text(7)
                    TauxInam = self.Ui.TableauAjouterCommande.topLevelItem(i).text(8)
                    TotalPec = self.Ui.TableauAjouterCommande.topLevelItem(i).text(9)
                    TotalPaye = self.Ui.TableauAjouterCommande.topLevelItem(i).text(10)
                    Departement = self.Ui.TableauAjouterCommande.topLevelItem(i).text(11)
                    CatSoins = self.Ui.TableauAjouterCommande.topLevelItem(i).text(12)
                    CatPatient = self.Ui.TableauAjouterCommande.topLevelItem(i).text(13)
                    CompteBudget = self.Ui.TableauAjouterCommande.topLevelItem(i).text(14)
                    DateCommande = date.today()

                    InfoDataTampon = (IdCommande, IdProduit, Libelle, PU, Quantite, Total, Taux, PrixInam, TauxInam, TotalPec, TotalPaye,
                    Departement, CatSoins, CatPatient, CompteBudget, DateCommande)
                    Data = (IdCommande)

                    if self.ReqInstance.AddTableTamponCommande(InfoDataTampon) == 0:

                        self.Ui.PrixTotalLabel.setText(str(self.ReqInstance.SommeDetailCommande(IdCommande)))
                        self.Ui.PrixPecLabel.setText(str(self.ReqInstance.SommeTotalPec(IdCommande)))
                        self.Ui.PrixPayeLabel.setText(str(self.ReqInstance.SommeTotalPaye(IdCommande)))

            except:
                print("Impossible d'ajouter des champs vides")
        else:
            self.Ui.MsgErreurIdCommande.show()
            self.Ui.MsgErreurIdCommande.setText("Veuiller cliquer sur nouveau")
            self.Ui.MsgErreurIdCommande.setStyleSheet("color:red;")

    def RetireDeCommande(self):
        IdProduit = self.Ui.TableauAjouterCommande.selectedItems()[0].text(1)
        self.Ui.TableauAjouterCommande.removeItemWidget(str(IdProduit))



    def AddCommandeInamOkProduit(self):

        Libelle = self.Ui.AjoutCommandeInamProduitBox.currentText()  # récupérer la valeur de produit

        # afficher les valeurs dans le tableau
        Info = self.ReqInstance.GetActesByName(Libelle)[0]  # en récupérant mon tuple
        Id = Info[0]  # et en récupérant la 1ère valeur Id de mon tuple
        PU = Info[1]  # et en récupérant la 2è valeur PU de mon tuple
        PrixInam = Info[2]
        TauxInam = Info[3]
        CatSoins = Info[4]
        Departement = Info[5]
        CatPatient = Info[6]
        CompteBudget = Info[7]
        # QuantiteExist = Info[8]

        self.Ui.AjoutCommandeInamPULineEdit.setText(str(PU))
        self.Ui.AjoutCommandeInamPrixInamLineEdit.setText(str(PrixInam))
        self.Ui.AjoutCommandeInamTauxInamLineEdit.setText(str(TauxInam))
        self.Ui.AjoutCommandeInamCatSoinsLineEdit.setText(CatSoins)
        self.Ui.AjoutCommandeInamDepartementLineEdit.setText(Departement)
        self.Ui.AjoutCommandeInamCatPatientLineEdit.setText(CatPatient)
        self.Ui.AjoutCommandeInamCompteBudgetLineEdit.setText(str(CompteBudget))
        # self.Ui.AjoutCommandeQteExistLineEdit.setText(str(QuantiteExist))

    def AddCommandeInam(self):
        IdCom = self.Ui.AjoutCommandeInamIdCommandeLineEdit.text()
        # print(IdCom)
        if int(IdCom) > 0:
            try:
                QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommandeInam)

                Qte = self.Ui.AjoutCommandeInamQteLineEdit.text()
                Taux = self.Ui.AjoutCommandeInamAssureTauxLineEdit.text()
                Libelle = self.Ui.AjoutCommandeInamProduitBox.currentText()
                Info = self.ReqInstance.GetActesByName(Libelle)[0]   # en récupérant mon tuple
                Id = Info[0]   # et en récupérant la 1ère valeur Id de mon tuple
                PU = Info[1]   # et en récupérant la 2è valeur PU de mon tuple
                PrixInam = Info[2]
                TauxInam = Info[3]
                CatSoins = Info[4]
                Departement = Info[5]
                CatPatient = Info[6]
                CompteBudget = Info[7]
                #QuantiteExist = Info[8]


                self.Ui.AjoutCommandeInamPULineEdit.setText(str(PU))
                self.Ui.AjoutCommandeInamPrixInamLineEdit.setText(str(PrixInam))
                self.Ui.AjoutCommandeInamTauxInamLineEdit.setText(str(TauxInam))
                self.Ui.AjoutCommandeInamCatSoinsLineEdit.setText(CatSoins)
                self.Ui.AjoutCommandeInamDepartementLineEdit.setText(Departement)
                self.Ui.AjoutCommandeInamCatPatientLineEdit.setText(CatPatient)
                self.Ui.AjoutCommandeInamCompteBudgetLineEdit.setText(str(CompteBudget))
                #self.Ui.AjoutCommandeInamQteExistLineEdit.setText(str(QuantiteExist))

                IdCommande = self.MAXICOMMANDE
                Data = (IdCommande)

                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(0, str(IdCommande))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(1,str(Id))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(2,str(Libelle))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(3,str(PU))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(4,str(Qte))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(5,str(int(PU)*int(Qte)))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(6, str(Taux))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(7, str(PrixInam))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(8, str(TauxInam))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(9, str(round(int(PrixInam)*int(Qte)*int(TauxInam)/100)))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(10, str(round((int(PU) - int(PrixInam)) * int(Qte) + ((int(int(PrixInam)*int(Qte)) - (int(PrixInam) * int(Qte) * int(TauxInam) / 100))))))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(11, str(Departement))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(12, str(CatSoins))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(13, str(CatPatient))
                self.Ui.TableauAjouterCommandeInam.topLevelItem(self.Ligne).setText(14, str(CompteBudget))

                self.Ligne +=1


                ### Ajouter à la table TamponCommande

                for i in range(self.Ligne):
                    #IdCommande = self.ReqInstance.GetCommandeIdByUniqueId(UniqueId)
                    IdCommande = self.MAXICOMMANDE
                    IdProduit = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(1)
                    Libelle = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(2)
                    PU = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(3)
                    Quantite = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(4)
                    Total = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(5)
                    Taux = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(6)
                    PrixInam = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(7)
                    TauxInam = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(8)
                    TotalPec = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(9)
                    TotalPaye = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(10)
                    Departement = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(11)
                    CatSoins = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(12)
                    CatPatient = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(13)
                    CompteBudget = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(14)
                    DateCommande = date.today()

                    InfoDataTampon = (IdCommande, IdProduit, Libelle, PU, Quantite, Total, Taux, PrixInam, TauxInam, TotalPec, TotalPaye,
                    Departement, CatSoins, CatPatient, CompteBudget, DateCommande)
                    Data = (IdCommande)

                    if self.ReqInstance.AddTableTamponCommande(InfoDataTampon) == 0:

                        self.Ui.PrixTotalInamLabel.setText(str(self.ReqInstance.SommeDetailCommande(IdCommande)))
                        self.Ui.PrixPecInamLabel.setText(str(self.ReqInstance.SommeTotalPec(IdCommande)))
                        self.Ui.PrixPayeInamLabel.setText(str(self.ReqInstance.SommeTotalPaye(IdCommande)))
            except:
                print("Impossible d'ajouter des champs vides")

        else:
            self.Ui.MsgErreurIdCommandeInam.show()
            self.Ui.MsgErreurIdCommandeInam.setText("Veuiller cliquer sur nouveau")
            self.Ui.MsgErreurIdCommandeInam.setStyleSheet("color:red;")

    # Valider la commande

    def ValideCommande(self):

        try:
            #Client = self.Ui.AjoutCommandeClientBox.currentText()  # je récupère la valeur du patient
            #IdClient = self.ReqInstance.GetClientIdByName(Client.split(" ")[0])  # je récupère le Id du client
            IdUsers = self.Ui.AjoutCommandeUserIdLabel.text()
            Operateur = self.Ui.AjoutCommandeUserLabel.text()
            NomPrenoms= self.Ui.AjoutCommandeNomLineEdit.text() ## je récupère la valeur du patient
            #IdPatient = self.ReqInstance.GetPatientIdByName(NomPrenoms.split(" ")[0])  # je récupère le Id du patient
            IdPatient = self.ReqInstance.GetPatientIdByName(NomPrenoms)
            Age = self.Ui.AjoutCommandeAgeLineEdit.text()
            Sexe = self.Ui.AjoutCommandeSexeLineEdit.text()
            GroupageSanguin = self.Ui.AjoutCommandeGroupageLineEdit.text()
            Pathologie = self.Ui.AjoutCommandePathologieLineEdit.text()
            CatSoins = self.Ui.AjoutCommandeCatSoinsLineEdit.text()
            Departement = self.Ui.AjoutCommandeDepartementLineEdit.text()
            CompteBudget = self.Ui.AjoutCommandeCompteBudgetLineEdit.text()

            PrixTotal = 0
            PrixPec = 0
            PrixPaye = 0

            Assurance = self.Ui.AjoutCommandeAssurePecLineEdit.text()
            Taux = self.Ui. AjoutCommandeAssureTauxLineEdit.text()
            Assure = self.Ui.AjoutCommandeNomAssureLineEdit.text()
            CodeAssure = self.Ui.AjoutCommandeCodeAssureLineEdit.text()

            #Date = datetime.now().strftime("%d %m %Y %T")
            Date = date.today()
            UniqueId = random.random()
            #DateHeure = datetime.now().strftime("%d %m %Y / %H:%M:%S")
            DateHeure = datetime.now()
            Data = (IdPatient,NomPrenoms,PrixTotal,PrixPec,PrixPaye,Assurance,Taux,Date,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,UniqueId,Assure,CodeAssure,Operateur,DateHeure)
            if self.ReqInstance.AddTableCommande(Data) == 0 :
                for i in range(self.Ligne):
                    IdCommande = self.ReqInstance.GetCommandeIdByUniqueId(UniqueId)
                    IdCommande = self.MAXICOMMANDE
                    IdProduit = self.Ui.TableauAjouterCommande.topLevelItem(i).text(1)
                    Libelle = self.Ui.TableauAjouterCommande.topLevelItem(i).text(2)
                    PU = self.Ui.TableauAjouterCommande.topLevelItem(i).text(3)
                    Quantite = self.Ui.TableauAjouterCommande.topLevelItem(i).text(4)
                    Total = int(self.Ui.TableauAjouterCommande.topLevelItem(i).text(5))
                    Taux = self.Ui.TableauAjouterCommande.topLevelItem(i).text(6)
                    PrixInam = self.Ui.TableauAjouterCommande.topLevelItem(i).text(7)
                    TauxInam = self.Ui.TableauAjouterCommande.topLevelItem(i).text(8)
                    TotalPec = int(self.Ui.TableauAjouterCommande.topLevelItem(i).text(9))
                    TotalPaye = int(self.Ui.TableauAjouterCommande.topLevelItem(i).text(10))
                    Departement = self.Ui.TableauAjouterCommande.topLevelItem(i).text(11)
                    CatSoins = self.Ui.TableauAjouterCommande.topLevelItem(i).text(12)
                    CatPatient = self.Ui.TableauAjouterCommande.topLevelItem(i).text(13)
                    CompteBudget = self.Ui.TableauAjouterCommande.topLevelItem(i).text(14)
                    DateCommande = datetime.today()
                    InfoData = (IdCommande,IdProduit,Libelle,PU,Quantite,Total,Taux,PrixInam,TauxInam,TotalPec,TotalPaye,Departement,CatSoins,CatPatient,CompteBudget,DateCommande)
                    DataStock = (Quantite, IdProduit)

                    if self.ReqInstance.AddInfoCommande(InfoData) == 0 :
                                                      # mettre à jour la quantité dans le stock
                        #self.ReqInstance.UpdateQteStock(DataStock) # ici le stock n'existe pas

                        PrixTotal += Total
                        PrixPec += TotalPec
                        PrixPaye += TotalPaye

                        # self.Ui.PrixTotalLabel.setText(str(self.Ui.TableauAjouterCommande.topLevelItem(i).text(5)))
                        self.Ui.PrixPecLabel.setText(str(TotalPec))
                        self.Ui.PrixPayeLabel.setText(str(TotalPaye))

                if self.ReqInstance.UpdateCommande(IdPatient,NomPrenoms,PrixTotal, PrixPec,PrixPaye,Assurance,Taux,Date,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,UniqueId,Assure,CodeAssure,DateHeure,IdCommande) == 0:

                    self.Ui.AjoutCommandeProduitBox.setCurrentText(" ")
                    #self.Ui.AjoutCommandeQteLineEdit.setText(" ")
                    self.Ui.TableauAjouterCommande.clear()
                    QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommande)
                    self.Ui.AjoutCommandeNomLineEdit.setText(" ")
                    self.Ui.AjoutCommandeAgeLineEdit.setText(" ")
                    self.Ui.AjoutCommandeSexeLineEdit.setText(" ")
                    self.Ui.AjoutCommandeGroupageLineEdit.setText(" ")
                    self.Ui.AjoutCommandePathologieLineEdit.setText(" ")
                    self.Ui.AjoutCommandeTelephoneLineEdit.setText(" ")
                    self.Ui.AjoutCommandeAdresseLineEdit.setText(" ")
                    self.Ui.AjoutCommandeCatSoinsLineEdit.setText(" ")
                    self.Ui.AjoutCommandeDepartementLineEdit.setText(" ")
                    self.Ui.AjoutCommandeCatPatientLineEdit.setText(" ")
                    self.Ui.AjoutCommandeCompteBudgetLineEdit.setText(" ")
                    self.Ui.AjoutCommandeProduitBox.setCurrentText(" ")
                    self.Ui.AjoutCommandeQteExistLineEdit.setText(" ")
                    self.Ui.AjoutCommandePULineEdit.setText(" ")
                    self.Ui.AjoutCommandePrixInamLineEdit.setText(" ")
                    self.Ui.AjoutCommandeTauxInamLineEdit.setText(" ")
                    self.Ui.AjoutCommandeQteLineEdit.setText("1")
                    self.Ui.AjoutCommandeNomAssureLineEdit.setText(" ")
                    self.Ui.AjoutCommandeAssurePecLineEdit.setText(" ")
                    self.Ui.AjoutCommandeAssureTauxLineEdit.setText("0")
                    self.Ui.AjoutCommandeCodeAssureLineEdit.setText(" ")
                    self.Ui.AjoutCommandeCodeFeuilletLineEdit.setText(" ")
                    self.Ui.AjoutCommandeAssureStatutLineEdit.setText(" ")
                    self.Ui.NumPatientLineEdit.setText(" ")
                    self.Ui.AjoutCommandeIdCommandeLineEdit.setText("0")
                    self.Ui.AjoutCommandePatientBox.setCurrentText(" ")

            self.Ligne = 0;


            self.Ui.PrixTotalLabel.setText("0")
            self.Ui.PrixPecLabel.setText("0")
            self.Ui.PrixPayeLabel.setText("0")
            self.ReqInstance.DeleteTamponCommande(IdCommande)
        except:
            print("Impossible de valider la commande")

        self.Ui.PageContent.setCurrentIndex(15)
        self.ShowCommandeCaisse()


    def ValideCommandeInam(self):
        try:

            IdUsers = self.Ui.AjoutCommandeInamUserIdLabel.text()
            Operateur = self.Ui.AjoutCommandeInamUserLabel.text()
            NomPrenoms = self.Ui.AjoutCommandeInamNomLineEdit.text()  ## je récupère la valeur du patient
            IdPatient = self.ReqInstance.GetPatientIdByName(NomPrenoms)  # je récupère le Id du patient
            Age = self.Ui.AjoutCommandeInamAgeLineEdit.text()
            Sexe = self.Ui.AjoutCommandeInamSexeLineEdit.text()
            GroupageSanguin = self.Ui.AjoutCommandeInamGroupageLineEdit.text()
            Pathologie = self.Ui.AjoutCommandeInamPathologieLineEdit.text()
            CatSoins = self.Ui.AjoutCommandeInamCatSoinsLineEdit.text()
            Departement = self.Ui.AjoutCommandeInamDepartementLineEdit.text()
            CompteBudget = self.Ui.AjoutCommandeInamCompteBudgetLineEdit.text()

            PrixTotal = 0
            PrixPec = 0
            PrixPaye = 0

            Assurance = self.Ui.AjoutCommandeInamAssurePecLineEdit.text()
            Taux = self.Ui.AjoutCommandeInamAssureTauxLineEdit.text()
            Assure = self.Ui.AjoutCommandeInamNomAssureLineEdit.text()
            CodeAssure = self.Ui.AjoutCommandeInamCodeAssureLineEdit.text()

            # Date = datetime.now().strftime("%d %m %Y %T")
            Date = date.today()
            UniqueId = random.random()
            # DateHeure = datetime.now().strftime("%d %m %Y / %H:%M:%S")
            DateHeure = datetime.now()
            Data = (IdPatient, NomPrenoms, PrixTotal, PrixPec, PrixPaye, Assurance, Taux, Date, Age, Sexe, GroupageSanguin,
                    Pathologie,CatSoins,Departement,CompteBudget,UniqueId, Assure, CodeAssure, Operateur, DateHeure)
            if self.ReqInstance.AddTableCommande(Data) == 0:
                for i in range(self.Ligne):
                    IdCommande = self.ReqInstance.GetCommandeIdByUniqueId(UniqueId)
                    IdCommande = self.MAXICOMMANDE
                    IdProduit = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(1)
                    Libelle = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(2)
                    PU = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(3)
                    Quantite = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(4)
                    Total = int(self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(5))
                    Taux = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(6)
                    PrixInam = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(7)
                    TauxInam = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(8)
                    TotalPec = int(self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(9))
                    TotalPaye = int(self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(10))
                    Departement = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(11)
                    CatSoins = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(12)
                    CatPatient = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(13)
                    CompteBudget = self.Ui.TableauAjouterCommandeInam.topLevelItem(i).text(14)
                    DateCommande = datetime.today()
                    InfoData = (IdCommande, IdProduit, Libelle, PU, Quantite, Total, Taux, PrixInam, TauxInam, TotalPec, TotalPaye,
                    Departement, CatSoins, CatPatient, CompteBudget, DateCommande)
                    DataStock = (Quantite, IdProduit)

                    if self.ReqInstance.AddInfoCommande(InfoData) == 0:
                        # mettre à jour la quantité dans le stock
                        #self.ReqInstance.UpdateQteStock(DataStock)  # ici le stock n'existe pas

                        PrixTotal += Total
                        PrixPec += TotalPec
                        PrixPaye += TotalPaye

                        # self.Ui.PrixTotalLabel.setText(str(self.Ui.TableauAjouterCommande.topLevelItem(i).text(5)))
                        self.Ui.PrixPecInamLabel.setText(str(TotalPec))
                        self.Ui.PrixPayeInamLabel.setText(str(TotalPaye))

                if self.ReqInstance.UpdateCommande(IdPatient,NomPrenoms,PrixTotal, PrixPec,PrixPaye,Assurance,Taux,Date,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,UniqueId,Assure,CodeAssure,DateHeure,IdCommande) == 0:
                    self.Ui.AjoutCommandeInamProduitBox.setCurrentText(" ")
                    # self.Ui.AjoutCommandeQteLineEdit.setText(" ")
                    self.Ui.TableauAjouterCommandeInam.clear()
                    QtWidgets.QTreeWidgetItem(self.Ui.TableauAjouterCommandeInam)
                    self.Ui.AjoutCommandeInamNomLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamAgeLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamSexeLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamGroupageLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamPathologieLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamTelephoneLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamAdresseLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamCatSoinsLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamDepartementLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamCatPatientLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamCompteBudgetLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamProduitBox.setCurrentText(" ")
                    self.Ui.AjoutCommandeInamQteExistLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamPULineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamPrixInamLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamTauxInamLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamQteLineEdit.setText("1")
                    self.Ui.AjoutCommandeInamNomAssureLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamAssurePecLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamAssureTauxLineEdit.setText("0")
                    self.Ui.AjoutCommandeInamCodeAssureLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamCodeFeuilletLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamAssureStatutLineEdit.setText(" ")
                    self.Ui.NumPatientInamLineEdit.setText(" ")
                    self.Ui.AjoutCommandeInamIdCommandeLineEdit.setText("0")
                    self.Ui.AjoutCommandePatientInamBox.setCurrentText(" ")

            self.Ligne = 0;

            self.Ui.PrixTotalInamLabel.setText("0")
            self.Ui.PrixPecInamLabel.setText("0")
            self.Ui.PrixPayeInamLabel.setText("0")
            self.ReqInstance.DeleteTamponCommande(IdCommande)
            self.Ui.PageContent.setCurrentIndex(10)

        except:
            print("Impossible de valider la commande")

        self.Ui.PageContent.setCurrentIndex(15)
        self.ShowCommandeCaisse()

    # Afficher les commandes

    def ShowCommande(self):
        self.Ui.TableauCommande.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowCommande():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauCommande)  # je crée une ligne vide
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la table Client
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(14, str(i[14]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(15, str(i[15]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(16, str(i[16]))
            self.Ui.TableauCommande.topLevelItem(Ligne).setText(17, str(i[17]))
            Ligne += 1

    # Afficher le détail d'une commande

    def ShowDetailCommande(self):
        IdCommande = self.Ui.TableauCommande.selectedItems()[0].text(0)
        self.Ui.TableauDetailCommande.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowDetailCommande(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauDetailCommande)  # je crée une ligne vide
            self.Ui.TableauDetailCommande.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauDetailCommande.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauDetailCommande.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauDetailCommande.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauDetailCommande.topLevelItem(Ligne).setText(4, str(i[4]))
            Ligne += 1
        self.Ui.PageContent.setCurrentIndex(13)

    # Afficher le stock

    def ShowStock(self):
        self.Ui.TableauStock.clear()  # vider le tableau
        Ligne = 0
        for i in self.ReqInstance.GetStock():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauStock)  # je crée une ligne vide
            self.Ui.TableauStock.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauStock.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauStock.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauStock.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauStock.topLevelItem(Ligne).setText(4, str(i[2]*i[3]))

            self.Ui.StockRavitaillerBtn.hide()    # cacher bouton ravitailler
            self.Ui.StockQuantiteLineEdit.hide()  # cacher champs quantite

            Ligne += 1

    # Ravitailler le stock

    def Ravitailler(self):
        self.IdProduit = self.Ui.TableauStock.selectedItems()[0].text(0)
        self.Ui.StockRavitaillerBtn.show()
        self.Ui.StockQuantiteLineEdit.show()

    # mise à jour de la table stock et historique de stock

    def UpdateStock(self):
        Quantite = self.Ui.StockQuantiteLineEdit.text()
        Data = (Quantite, self.IdProduit)
        if self.ReqInstance.UpdateStock(Data) == 0 :      # si la mise à jour dans la stock est vrai, alors montrer stock
            self.Ui.TableauStock.clear()                  # vider le tableau
            Ligne = 0
            for i in self.ReqInstance.GetStock():
                QtWidgets.QTreeWidgetItem(self.Ui.TableauStock)  # je crée une ligne vide
                self.Ui.TableauStock.topLevelItem(Ligne).setText(0, str(i[0]))
                self.Ui.TableauStock.topLevelItem(Ligne).setText(1, str(i[1]))
                self.Ui.TableauStock.topLevelItem(Ligne).setText(2, str(i[2]))
                self.Ui.TableauStock.topLevelItem(Ligne).setText(3, str(i[3]))
                self.Ui.TableauStock.topLevelItem(Ligne).setText(4, str(i[2] * i[3]))
                Ligne += 1
            self.Ui.StockQuantiteLineEdit.setText(" ")
            self.Ui.StockRavitaillerBtn.hide()
            self.Ui.StockQuantiteLineEdit.hide()

        # Clic Btn avant de créer NouvelAssure

    def CreerNouvelAssure(self):

        self.Ui.AssuranceNomBox.clear()
        self.Ui.SocieteAssureBox.clear()
        self.Ui.TauxAssuranceBox.clear()
        self.Ui.PECBox.clear()

        for i in self.AdminInstance.ShowNomAssuranceAutres():
            self.IdAssuranceNom = i[0]
            AssuranceNom = i[1]
            self.Ui.AssuranceNomBox.addItem(AssuranceNom)

        for i in self.AdminInstance.ShowSocieteAssure():
            self.IdSocieteAssure = i[0]
            SocieteAssure = i[1]
            self.Ui.SocieteAssureBox.addItem(SocieteAssure)

        for i in self.AdminInstance.ShowTauxPec():
            self.IdTauxPec = i[0]
            TauxPec = str(i[1])
            self.Ui.TauxAssuranceBox.addItem(TauxPec)


        for i in self.AdminInstance.ShowAssuranceAutres():
            self.IdAssurance = i[0]
            Assurance = i[2]
            self.Ui.PECBox.addItem(Assurance)

    def CreerNouvelAssureInam(self):

        self.Ui.AssuranceNomInamBox.clear()
        self.Ui.SocieteAssureInamBox.clear()
        self.Ui.TauxAssuranceInamBox.clear()
        self.Ui.PECBox.clear()

        for i in self.AdminInstance.ShowNomAssuranceINAM():
            self.IdAssuranceNom = i[0]
            AssuranceNom = i[1]
            self.Ui.AssuranceNomInamBox.addItem(AssuranceNom)

        for i in self.AdminInstance.ShowSocieteAssure():
            self.IdSocieteAssure = i[0]
            SocieteAssure = i[1]
            self.Ui.SocieteAssureInamBox.addItem(SocieteAssure)

        for i in self.AdminInstance.ShowTauxPec():
            self.IdTauxPec = i[0]
            TauxPec = str(i[1])
            self.Ui.TauxAssuranceInamBox.addItem(TauxPec)


        for i in self.AdminInstance.ShowAssuranceInam():
            self.IdAssurance = i[0]
            Assurance = i[2]
            self.Ui.PECInamBox.addItem(Assurance)

    # Créer un assuré
    def AddAssure(self):
        NomAssure = self.Ui.NomAssureLineEdit.text()  # récupérer le text du Nom
        PrenomsAssure = self.Ui.PrenomsAssureLineEdit.text()  # récupérer le text du Prenom
        NumAssure = self.Ui.NumeroAssureLineEdit.text()
        NumFeuillet = self.Ui.FeuilletAssureLineEdit.text()
        Assurance = self.Ui.AssuranceNomBox.currentText()
        SocieteAssure = self.Ui.SocieteAssureBox.currentText()
        Taux = self.Ui.TauxAssuranceBox.currentText()
        Pec = self.Ui.PECBox.currentText()
        DateCreation = datetime.today().strftime("%d %m %Y / %H:%M:%S")
        Data = (NomAssure, PrenomsAssure, NumAssure, NumFeuillet, Assurance, SocieteAssure, Taux, Pec, DateCreation)

        if self.ReqInstance.AddAssure(NomAssure, PrenomsAssure, NumAssure, NumFeuillet, Assurance, SocieteAssure, Taux, Pec) == 0:
            self.ShowAssure()
            self.Ui.PageContent.setCurrentIndex(14)
            self.Ui.NomAssureLineEdit.setText("")
            self.Ui.PrenomsAssureLineEdit.setText("")
            self.Ui.NumeroAssureLineEdit.setText("")
            self.Ui.FeuilletAssureLineEdit.setText("")
            self.Ui.AssuranceNomBox.setCurrentText("")
            self.Ui.SocieteAssureBox.setCurrentText("")
            self.Ui.TauxAssuranceBox.setCurrentText("")
            self.Ui.PECBox.setCurrentText("")

    # Créer un assuré INAM
    def AddAssureINAM(self):
        NomAssure = self.Ui.NomAssureInamLineEdit.text()  # récupérer le text du Nom
        PrenomsAssure = self.Ui.PrenomsAssureInamLineEdit.text()  # récupérer le text du Prenom
        NumAssure = self.Ui.NumeroAssureInamLineEdit.text()
        NumFeuillet = self.Ui.FeuilletAssureLineInamEdit.text()
        Assurance = self.Ui.AssuranceNomInamBox.currentText()
        SocieteAssure = self.Ui.SocieteAssureInamBox.currentText()
        Taux = self.Ui.TauxAssuranceInamBox.currentText()
        Pec = self.Ui.PECInamBox.currentText()
        DateCreation = datetime.today()
        Data = (NomAssure, PrenomsAssure, NumAssure, NumFeuillet, Assurance, SocieteAssure, Taux, Pec, DateCreation)

        if self.ReqInstance.AddAssure(NomAssure, PrenomsAssure, NumAssure, NumFeuillet, Assurance, SocieteAssure,
                                      Taux, Pec) == 0:
            self.ShowAssureInam()
            self.Ui.PageContent.setCurrentIndex(19)
            self.Ui.NomAssureInamLineEdit.setText("")
            self.Ui.PrenomsAssureInamLineEdit.setText("")
            self.Ui.NumeroAssureInamLineEdit.setText("")
            self.Ui.FeuilletAssureLineInamEdit.setText("")
            self.Ui.AssuranceNomInamBox.setCurrentText("")
            self.Ui.SocieteAssureInamBox.setCurrentText("")
            self.Ui.TauxAssuranceInamBox.setCurrentText("")
            self.Ui.PECInamBox.setCurrentText("")

    # Afficher les assurés

    def ShowAssure(self):
        self.Ui.TableauAjoutAssure.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowAssure():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAjoutAssure)  # je crée une ligne vide
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(10, str(i[10]))

            Ligne += 1

    def ShowAssureInam(self):
        self.Ui.TableauAjoutAssureInam.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowAssureInam():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAjoutAssureInam)  # je crée une ligne vide
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(10, str(i[10]))

            Ligne += 1

    # choisir assuré

    def ChoisirAssure(self):
        self.Ui.AjoutCommandeNomAssureLineEdit.clear()
        self.Ui.AjoutCommandeAssurePecLineEdit.clear()
        self.Ui.AjoutCommandeAssureTauxLineEdit.clear()
        self.Ui.AjoutCommandeCodeAssureLineEdit.clear()
        self.Ui.AjoutCommandeCodeFeuilletLineEdit.clear()
        self.Ui.AjoutCommandeAssureStatutLineEdit.clear()

        for i in self.ReqInstance.ShowAssure():
            self.Ui.PageContent.setCurrentIndex(14)
            self.Ui.PageMenu.setCurrentIndex(2)

            self.Ui.TableauAjoutAssure.clear()  # vider le tableau
            Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
            for i in self.ReqInstance.ShowAssure():
                QtWidgets.QTreeWidgetItem(self.Ui.TableauAjoutAssure)  # je crée une ligne vide
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(1, str(i[1]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(2, str(i[2]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(3, str(i[3]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(5, str(i[5]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(6, str(i[6]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(7, str(i[7]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(8, str(i[8]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(9, str(i[9]))
                self.Ui.TableauAjoutAssure.topLevelItem(Ligne).setText(10, str(i[10]))

                Ligne += 1

    # choisir assuré Inam

    def ChoisirAssureInam(self):
        self.Ui.AjoutCommandeInamNomAssureLineEdit.clear()
        self.Ui.AjoutCommandeInamAssurePecLineEdit.clear()
        self.Ui.AjoutCommandeInamAssureTauxLineEdit.clear()
        self.Ui.AjoutCommandeInamCodeAssureLineEdit.clear()
        self.Ui.AjoutCommandeInamCodeFeuilletLineEdit.clear()
        self.Ui.AjoutCommandeInamNomAssureLineEdit.clear()

        for i in self.ReqInstance.ShowAssureInam():
            self.Ui.PageContent.setCurrentIndex(19)
            self.Ui.PageMenu.setCurrentIndex(2)

            self.Ui.TableauAjoutAssureInam.clear()  # vider le tableau
            Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
            for i in self.ReqInstance.ShowAssureInam():
                QtWidgets.QTreeWidgetItem(self.Ui.TableauAjoutAssureInam)  # je crée une ligne vide
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(0, str(i[0]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(1, str(i[1]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(2, str(i[2]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(3, str(i[3]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(5, str(i[5]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(6, str(i[6]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(7, str(i[7]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(8, str(i[8]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(9, str(i[9]))
                self.Ui.TableauAjoutAssureInam.topLevelItem(Ligne).setText(10, str(i[10]))

                Ligne += 1

        # Remplir infos assure de la commande

    def RemplirAssure(self):
        IdAssure = self.Ui.TableauAjoutAssure.selectedItems()[0].text(0)

        # Ligne = 0     # je crée l'instance Ligne qui prend la valeur 0

        self.Id = self.Ui.TableauAjoutAssure.selectedItems()[0].text(0)  # je récupère l'Id
        self.NomX = self.Ui.TableauAjoutAssure.selectedItems()[0].text(1)  # je récupère le
        self.PrenomsY = self.Ui.TableauAjoutAssure.selectedItems()[0].text(2)  # je récupère le
        self.NomAssure = self.NomX + " " + self.PrenomsY
        self.Pec = self.Ui.TableauAjoutAssure.selectedItems()[0].text(8)
        self.Taux = self.Ui.TableauAjoutAssure.selectedItems()[0].text(7)
        self.NumAssure = self.Ui.TableauAjoutAssure.selectedItems()[0].text(3)
        self.CodeFeuillet = self.Ui.TableauAjoutAssure.selectedItems()[0].text(4)
        self.Statut = self.Ui.TableauAjoutAssure.selectedItems()[0].text(9)

        self.Ui.AjoutCommandeNomAssureLineEdit.setText(self.NomAssure)  # j'affiche les éléments sélectionné dans leurs champs de modif
        self.Ui.AjoutCommandeAssurePecLineEdit.setText(self.Pec)
        self.Ui.AjoutCommandeAssureTauxLineEdit.setText(self.Taux)
        self.Ui.AjoutCommandeCodeAssureLineEdit.setText(self.NumAssure)
        self.Ui.AjoutCommandeCodeFeuilletLineEdit.setText(self.CodeFeuillet)
        self.Ui.AjoutCommandeAssureStatutLineEdit.setText(self.Statut)

        self.Ui.PageContent.setCurrentIndex(10)
        self.Ui.PageMenu.setCurrentIndex(3)
        self.Ui.AjoutCommandeIdCommandeLineEdit.setText("0")

    def RemplirAssureInam(self):
        IdAssure = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(0)
        self.Id = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(0)  # je récupère l'Id
        self.NomX = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(1)  # je récupère le
        self.PrenomsY = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(2)  # je récupère le
        self.NomAssure = self.NomX + " " + self.PrenomsY
        self.Pec = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(8)
        self.Taux = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(7)
        self.NumAssure = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(3)
        self.CodeFeuillet = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(4)
        self.Statut = self.Ui.TableauAjoutAssureInam.selectedItems()[0].text(9)

        self.Ui.AjoutCommandeInamNomAssureLineEdit.setText(self.NomAssure)
        self.Ui.AjoutCommandeInamAssurePecLineEdit.setText(self.Pec)
        self.Ui.AjoutCommandeInamAssureTauxLineEdit.setText(self.Taux)
        self.Ui.AjoutCommandeInamCodeAssureLineEdit.setText(self.NumAssure)
        self.Ui.AjoutCommandeInamCodeFeuilletLineEdit.setText(self.CodeFeuillet)
        self.Ui.AjoutCommandeInamAssureStatutLineEdit.setText(self.Statut)

        self.Ui.PageContent.setCurrentIndex(18)
        self.Ui.PageMenu.setCurrentIndex(3)
        self.Ui.AjoutCommandeInamIdCommandeLineEdit.setText("0")

    # Appliquer Pec

    def AppliquerPec(self):

        ### add dans le tableau TableauCommandePec
        QtWidgets.QTreeWidgetItem(self.Ui.TableauCommandePec)  # on doit créer une ligne vide pour les données à récupérer
        MontantBrut = self.Ui.AjoutCommandeMontantBrut.text()
        NomAssure = self.Ui.AjoutCommandeNomAssureLineEdit.text()  # récupère CatSoins
        AssurePec = self.Ui.AjoutCommandeAssurePecLineEdit.text()
        Taux = self.Ui.AjoutCommandeAssureTauxLineEdit.text()
        CodeAssure = self.Ui.AjoutCommandeCodeAssureLineEdit.text()  # récupérer la valeur de produit
        CodeFeuillet = self.Ui.AjoutCommandeCodeFeuilletLineEdit.text()  # récupérer la valeur de quantité
        Statut = self.Ui.AjoutCommandeAssureStatutLineEdit.text()

        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(0, str(int(MontantBrut)*int(Taux)))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(1, str(AssurePec))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(2, str(Taux))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(3, str(NomAssure))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(4, str(CodeAssure))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(6, str(Statut))
        self.Ui.TableauCommandePec.topLevelItem(self.Ligne).setText(5, str(CodeFeuillet))


        self.Ligne += 1

        ### appliquer le taux sur les montants dans le tableau TableauAjouterCommande

        Taux = self.Ui.AjoutCommandeAssureTauxLineEdit.text()

        self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(5, str(Taux))
        self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(8, str(round(int(PU) * int(Qte) * int(Taux) / 100)))
        self.Ui.TableauAjouterCommande.topLevelItem(self.Ligne).setText(9, str(round(int(PU) * int(Qte) - (int(PU) * int(Qte) * int(Taux) / 100))))

    # ENCAISSEMENT DES RECETTES

    # Afficher les factures à encaisser

    def ShowCommandeCaisse(self):

        for i in self.ReqInstance.ShowCommandeCaisse():
            self.Ui.PageContent.setCurrentIndex(15)
            self.Ui.TableauCaisse.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowCommandeCaisse():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauCaisse)  # je crée une ligne vide
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la tabl
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(14, str(i[14]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(15, str(i[15]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(16, str(i[16]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(17, str(i[17]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(18, str(i[18]))

            Ligne += 1

    # Actualiser la liste des commandes
    def ActualiserCaisse(self):
        self.ShowCommandeCaisse()

    # Afficher la facture à encaisser
    def RappelCommandeCaisseById(self):

        IdCommande = self.Ui.RappelNumCommandeLineEdit.text()

        for i in self.ReqInstance.RappelCommandeById(IdCommande):
            self.Ui.TableauCaisse.clear()  # vider le tableau
            self.Ui.TableauCaisseDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.RappelCommandeById(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauCaisse)  # je crée une ligne vide
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la tabl
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauCaisse.topLevelItem(Ligne).setText(14, str(i[14]))

            Ligne += 1

            self.Ui.TotalBrutCaisseLabel.setText(str(self.ReqInstance.ShowMtBrutCaisse(IdCommande)))
            self.Ui.TotalPecCaisseLabel.setText(str(self.ReqInstance.ShowMtPecCaisse(IdCommande)))
            self.Ui.TotalPayeCaisseLabel.setText(str(self.ReqInstance.ShowMtPayeCaisse(IdCommande)))



        # Afficher le détail d'une facture à encaisser

    def ShowDetailCaisse(self):
        IdCommande = self.Ui.TableauCaisse.selectedItems()[0].text(0)
        self.Ui.TableauCaisseDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowDetailCaisse(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauCaisseDetail)  # je crée une ligne vide
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauCaisseDetail.topLevelItem(Ligne).setText(11, str(i[11]))

            Ligne += 1

    def RemplirlesChamps(self):

        self.IdCommande = self.Ui.TableauCaisse.selectedItems()[0].text(0)
        self.NomPrenoms = self.Ui.TableauCaisse.selectedItems()[0].text(1)
        self.MtTotal = self.Ui.TableauCaisse.selectedItems()[0].text(2)
        self.MtPec = self.Ui.TableauCaisse.selectedItems()[0].text(3)
        self.MtPaye = self.Ui.TableauCaisse.selectedItems()[0].text(4)
        self.Assuranc = self.Ui.TableauCaisse.selectedItems()[0].text(5)
        self.Taux = self.Ui.TableauCaisse.selectedItems()[0].text(6)
        self.Age = self.Ui.TableauCaisse.selectedItems()[0].text(7)
        self.Sexe = self.Ui.TableauCaisse.selectedItems()[0].text(8)
        self.Groupe = self.Ui.TableauCaisse.selectedItems()[0].text(9)
        self.Patho = self.Ui.TableauCaisse.selectedItems()[0].text(10)
        self.CatSoins = self.Ui.TableauCaisse.selectedItems()[0].text(11)
        self.Departement = self.Ui.TableauCaisse.selectedItems()[0].text(12)
        self.CompteBudget = self.Ui.TableauCaisse.selectedItems()[0].text(13)
        self.Operateur = self.Ui.TableauCaisse.selectedItems()[0].text(14)
        self.Assure = self.Ui.TableauCaisse.selectedItems()[0].text(16)
        self.CodeAssure = self.Ui.TableauCaisse.selectedItems()[0].text(17)
        self.DateCommande = self.Ui.TableauCaisse.selectedItems()[0].text(18)

        self.Ui.IdCommandeLineEdit.setText(self.IdCommande)
        self.Ui.NomPrenLineEdit.setText(self.NomPrenoms)
        self.Ui.AgLineEdit.setText(self.Age)
        self.Ui.SexLineEdit.setText(self.Sexe)
        self.Ui.GroupLineEdit.setText(self.Groupe)
        self.Ui.PatholoLineEdit.setText(self.Patho)
        self.Ui.AssurLineEdit.setText(self.Assuranc)
        self.Ui.TauLineEdit.setText(self.Taux)
        self.Ui.OperatLineEdit.setText(self.Operateur)
        self.Ui.TotalBrutCaisseLabel.setText(self.MtTotal)
        self.Ui.TotalPecCaisseLabel.setText(self.MtPec)
        self.Ui.TotalPayeCaisseLabel.setText(self.MtPaye)
        self.Ui.TauLineEdit.setText(self.Taux)
        self.Ui.AssureLineEdit.setText(self.Assure)
        self.Ui.CodeAssureLineEdit.setText(self.CodeAssure)
        self.Ui.CatSoinsLineEdit.setText(self.CatSoins)
        self.Ui.DepartementLineEdit.setText(self.Departement)
        self.Ui.CompteBudgetLineEdit.setText(self.CompteBudget)
        self.Ui.DateCommandeLineEdit.setText(self.DateCommande)

    def CreerLigneAvecIdMax(self):

        # créer une ligne vide avec Idcaisse, Caissier et IdCaissier
        IdCaisse = 0

        # je récupère IdCaissier et le nom du caissier

        IdCaissier = self.Ui.CaissierIdLabel.text()
        Caissier = self.Ui.CaissierUserLabel.text()
        #DateHeure = datetime.datetime.today().strftime("%d %m %Y / %H:%M:%S")
        DateHeure = datetime.today()

        # je crée une insertion de la variable dans la table commande

        DataCaisse = (IdCaisse, IdCaissier, Caissier, DateHeure)
        if self.ReqInstance.InsererIdCaisse(IdCaissier, Caissier, DateHeure) == 0:
            pass

        # après je récupère l'Id
        # IdCommande =  retour de GetIdMaxCommande ==MAXICOMMANDE

        Data = (IdCaissier,)
        self.MAXICaisse = self.ReqInstance.GetIdMaxCaisse(Data)

    def AddToCaisse(self):

        IdCommande = self.Ui.IdCommandeLineEdit.text()
        DateCommande = self.Ui.DateCommandeLineEdit.text()
        NomPrenoms = self.Ui.NomPrenLineEdit.text()
        MontantTotal = self.Ui.TotalBrutCaisseLabel.text()
        MontantPec = self.Ui.TotalPecCaisseLabel.text()
        MontantPaye = self.Ui.TotalPayeCaisseLabel.text()
        Assurance = self.Ui.AssurLineEdit.text()
        Taux = self.Ui.TauLineEdit.text()
        Age = self.Ui.AgLineEdit.text()
        Sexe = self.Ui.SexLineEdit.text()
        GroupageSanguin = self.Ui.GroupLineEdit.text()
        Pathologie = self.Ui.PatholoLineEdit.text()
        CatSoins = self.Ui.CatSoinsLineEdit.text()
        Departement = self.Ui.DepartementLineEdit.text()
        CompteBudget = self.Ui.CompteBudgetLineEdit.text()
        Assure = self.Ui.AssureLineEdit.text()
        CodeAssure = self.Ui.CodeAssureLineEdit.text()
        Operateur = self.Ui.OperatLineEdit.text()
        #Date = datetime.datetime.today().strftime("%d %m %Y")
        DateCaisse = date.today()
        IdCaisse = self.MAXICaisse
        IdCaissier = self.Ui.CaissierIdLabel.text()
        Caissier = self.Ui.CaissierUserLabel.text()
        #DateHeure = datetime.datetime.today().strftime("%d %m %Y / %H:%M:%S")
        DateHeure = datetime.today()
        Data = (IdCommande,NomPrenoms,MontantTotal,MontantPec,MontantPaye,Assurance,Taux,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,Assure,CodeAssure,Operateur,DateCaisse,Caissier,IdCaisse)

        if self.ReqInstance.Encaissement(IdCommande,NomPrenoms,MontantTotal,MontantPec,MontantPaye,Assurance,Taux,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,Assure,CodeAssure,Operateur,DateCaisse,Caissier,IdCaisse) == 0 :
            IdCommande = self.Ui.IdCommandeLineEdit.text()
            # with open("testo.txt", "w") as RecId:
            #     RecId.write(str(IdCommande))
            #self.ReqInstance.DeleteTamponEncaissement()
            self.ReqInstance.TamponEncaissement(IdCommande,NomPrenoms,MontantTotal,MontantPec,MontantPaye,Assurance,Taux,Age,Sexe,GroupageSanguin,Pathologie,CatSoins,Departement,CompteBudget,Assure,CodeAssure,Operateur,DateCaisse,Caissier)
            self.ReqInstance.UpdateValideCommande(IdCommande)
            self.Ui.TableauCaisseDetail.clear()
            self.Ui.IdCommandeLineEdit.setText("")
            self.Ui.DateCommandeLineEdit.setText("")
            self.Ui.NomPrenLineEdit.setText("")
            self.Ui.TotalBrutCaisseLabel.setText("")
            self.Ui.TotalPecCaisseLabel.setText("")
            self.Ui.TotalPayeCaisseLabel.setText("")
            self.Ui.AssurLineEdit.setText("")
            self.Ui.TauLineEdit.setText("")
            self.Ui.AgLineEdit.setText("")
            self.Ui.SexLineEdit.setText("")
            self.Ui.GroupLineEdit.setText("")
            self.Ui.PatholoLineEdit.setText("")
            self.Ui.CatSoinsLineEdit.setText("")
            self.Ui.DepartementLineEdit.setText("")
            self.Ui.CompteBudgetLineEdit.setText("")
            self.Ui.AssureLineEdit.setText("")
            self.Ui.CodeAssureLineEdit.setText("")
            self.Ui.OperatLineEdit.setText("")
            self.ShowCommandeCaisse()


    def PrintRecuCaisse(self):
        Chemin = "formatA6.pdf"
        os.system(Chemin)
    #
    #     self.ShowCommandeCaisse()
    #     self.Ui.TableauCaisseDetail.clear()
        #self.ReqInstance.DeleteTamponEncaissement()

    def BrouillardDeCaisse(self):

        self.Ui.TableauBrouillard.clear()
        Ligne = 0

        for i in self.ReqInstance.BrouillardDeCaisse():
            QtWidgets.QTreeWidgetItem(self.Ui.TableauBrouillard)

            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(14, str(i[14]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(15, str(i[15]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(16, str(i[16]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(17, str(i[17]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(18, str(i[18]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(19, str(i[19]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(20, str(i[20]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(21, str(i[21]))

            Ligne += 1

            self.Ui.RecettesJourTotalBrutLabel.setText(str(self.ReqInstance.ShowMtBrutBrCaisseG()))
            self.Ui.RecettesJourTotalPecLabel.setText(str(self.ReqInstance.ShowMtPecBrCaisseG()))
            self.Ui.RecettesJourTotalEncaisseLabel.setText(str(self.ReqInstance.ShowMtPayeBrCaisseG()))

    def RecettesDuJour(self):
        self.ReqInstance.DeleteTamponDate()
        DateDebut = self.Ui.RecettesJourDateDebut.date().toPyDate()
        DateFin = self.Ui.RecettesJourDateFin.date().toPyDate()
        Data = (DateDebut,DateFin)
        if self.ReqInstance.TamponDate(Data) == 0 :
            self.Ui.TableauBrouillard.clear()
            Ligne = 0

            #for i in self.ReqInstance.RecettesDuJour(DateDebut,DateFin):
            for i in self.ReqInstance.RecettesJournal():

                QtWidgets.QTreeWidgetItem(self.Ui.TableauBrouillard)
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(0, str(i[0]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(1, str(i[1]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(2, str(i[2]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(3, str(i[3]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(4, str(i[4]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(5, str(i[5]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(6, str(i[6]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(7, str(i[7]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(8, str(i[8]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(9, str(i[9]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(10, str(i[10]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(11, str(i[11]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(12, str(i[12]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(13, str(i[13]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(14, str(i[14]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(15, str(i[15]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(16, str(i[16]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(17, str(i[17]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(18, str(i[18]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(19, str(i[19]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(20, str(i[20]))
                self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(21, str(i[21]))

                Ligne += 1


                self.Ui.RecettesJourTotalBrutLabel.setText(str(self.ReqInstance.ShowMtBrutBrCaisse()))
                self.Ui.RecettesJourTotalPecLabel.setText(str(self.ReqInstance.ShowMtPecBrCaisse()))
                self.Ui.RecettesJourTotalEncaisseLabel.setText(str(self.ReqInstance.ShowMtPayeBrCaisse()))

    def RecettesHier(self):
        self.Ui.TableauBrouillard.clear()
        Ligne = 0

        #for i in self.ReqInstance.RecettesDuJour(DateDebut,DateFin):
        for i in self.ReqInstance.RecettesHier():

            QtWidgets.QTreeWidgetItem(self.Ui.TableauBrouillard)
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(14, str(i[14]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(15, str(i[15]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(16, str(i[16]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(17, str(i[17]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(18, str(i[18]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(19, str(i[19]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(20, str(i[20]))
            self.Ui.TableauBrouillard.topLevelItem(Ligne).setText(21, str(i[21]))

            Ligne += 1

            self.Ui.RecettesJourTotalBrutLabel.setText(str(self.ReqInstance.ShowMtBrutBrCaisseHier()))
            self.Ui.RecettesJourTotalPecLabel.setText(str(self.ReqInstance.ShowMtPecBrCaisseHier()))
            self.Ui.RecettesJourTotalEncaisseLabel.setText(str(self.ReqInstance.ShowMtPayeBrCaisseHier()))

    def RecettesParCompte(self):
        self.ReqInstance.DeleteTamponDate()
        DateDebut = self.Ui.EtatRecettesDateDebut.date().toPyDate()
        DateFin = self.Ui.EtatRecettesDateFin.date().toPyDate()
        Data = (DateDebut, DateFin)
        if self.ReqInstance.TamponDate(Data) == 0:
            self.Ui.TableauEtatRecettes.clear()
            Ligne = 0

            # for i in self.ReqInstance.RecettesDuJour(DateDebut,DateFin):
            for i in self.ReqInstance.RecettesParCompte():
                QtWidgets.QTreeWidgetItem(self.Ui.TableauEtatRecettes)
                self.Ui.TableauEtatRecettes.topLevelItem(Ligne).setText(0, str(i[0]))
                self.Ui.TableauEtatRecettes.topLevelItem(Ligne).setText(1, str(i[1]))
                self.Ui.TableauEtatRecettes.topLevelItem(Ligne).setText(2, str(i[2]))

                Ligne += 1

                self.Ui.EtatRecettesTotalEncaisseLabel.setText(str(self.ReqInstance.ShowMtRecParCompte()))

    def ShowDetailCaisseByIdCommande(self):
        IdCommande = self.Ui.TableauBrouillard.selectedItems()[0].text(1)
        self.Ui.TableauDetailCaisse.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowDetailCaisseByIdCommande(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauDetailCaisse)  # je crée une ligne vide
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauDetailCaisse.topLevelItem(Ligne).setText(13, str(i[13]))

            Ligne += 1
        self.Ui.PageContent.setCurrentIndex(21)

    ################################# Annulations ###############################
    ################################# Annulations ###############################
    ## Pharma ####
    # Afficher la commande pharma à annuler
    def RappelCommandePharmaById(self):

        IdCommande = self.Ui.RappelNumCommandePharmaLineEdit.text()

        for i in self.ReqInstance.RappelCommandeById(IdCommande):
            self.Ui.TableauAnnulationPharma.clear()  # vider le tableau
            # self.Ui.TableauCaisseDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.RappelCommandeById(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAnnulationPharma)  # je crée une ligne vide
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la tabl
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(11, str(i[11]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(12, str(i[12]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(13, str(i[13]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(14, str(i[14]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(15, str(i[15]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(16, str(i[16]))
            self.Ui.TableauAnnulationPharma.topLevelItem(Ligne).setText(17, str(i[17]))

            Ligne += 1

            self.Ui.TotalBrutAnnulerPharmaLabel.setText(str(self.ReqInstance.ShowMtBrutCaisse(IdCommande)))
            self.Ui.TotalPecAnnulerPharmaLabel.setText(str(self.ReqInstance.ShowMtPecCaisse(IdCommande)))
            self.Ui.TotalPayeAnnulerPharmaLabel.setText(str(self.ReqInstance.ShowMtPayeCaisse(IdCommande)))
            for i in range(Ligne):
                AnnulePharma = self.Ui.TableauAnnulationPharma.topLevelItem(i).text(17)
                self.Ui.AnnulePharmaResulteLineEdit.setText(AnnulePharma)

    def AnnulationPharma(self):
        IdCommande = self.Ui.RappelNumCommandePharmaLineEdit.text()
        # AnnuleCommande = "CAMMANDE ANNULEE"
        AnnuleCommande = 1
        DateAnnuleCommande = datetime.now()
        Data = (AnnuleCommande,DateAnnuleCommande,IdCommande)
        if self.ReqInstance.AnnulationPharma(AnnuleCommande,DateAnnuleCommande,IdCommande) == 0 :

            for i in range(self.Ligne):
                IdProduit = self.Ui.TableauAnnulationPharmaDetail.topLevelItem(i).text(1)
                Quantite = self.Ui.TableauAnnulationPharmaDetail.topLevelItem(i).text(4)
                Departement = self.Ui.TableauAnnulationPharmaDetail.topLevelItem(i).text(8)
                DataStock = (IdProduit, Quantite)
                if Departement == "PHARMACIE" :
                    self.ReqInstance.AnnulationPharmaUpdateQteStock(DataStock)
                else:
                    pass

            self.Ui.PharmaConfirmationAnnuleLabel.setText("La commande a été bien annulée")
            self.Ui.PharmaConfirmationAnnuleLabel.setStyleSheet("Color:green;")
            self.Ui.RappelNumCommandePharmaLineEdit.setText(" ")
            self.Ui.TotalBrutAnnulerPharmaLabel.setText("0")
            self.Ui.TotalPecAnnulerPharmaLabel.setText("0")
            self.Ui.TotalPayeAnnulerPharmaLabel.setText("0")
            self.Ui.TableauAnnulationPharma.clear()
            self.Ui.TableauAnnulationPharmaDetail.clear()

    def ShowAnnulationDetailPharma(self):
        IdCommande = self.Ui.TableauAnnulationPharma.selectedItems()[0].text(0)
        self.Ui.TableauAnnulationPharmaDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowDetailCaisse(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAnnulationPharmaDetail)  # je crée une ligne vide
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauAnnulationPharmaDetail.topLevelItem(Ligne).setText(11, str(i[11]))

            Ligne += 1

    ## Caisse ####
    # Afficher la commande caisse à annuler

    def RappelCommandeCaisseById(self):

        IdCommande = self.Ui.RappelNumCommandecaisseLineEdit.text()

        for i in self.ReqInstance.RappelCaisseByIdCommande(IdCommande):
            self.Ui.TableauAnnulationCaisse.clear()  # vider le tableau
            # self.Ui.TableauCaisseDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.RappelCaisseByIdCommande(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAnnulationCaisse)  # je crée une ligne vide
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(0, str(i[0]))  # je crée les différents champs de la tabl
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauAnnulationCaisse.topLevelItem(Ligne).setText(11, str(i[11]))

            Ligne += 1

            self.Ui.TotalBrutAnnulerCaisseLabel.setText(str(self.ReqInstance.ShowMtBrutCaisse(IdCommande)))
            self.Ui.TotalPecAnnulerCaisseLabel.setText(str(self.ReqInstance.ShowMtPecCaisse(IdCommande)))
            self.Ui.TotalPayeAnnulerCaisseLabel.setText(str(self.ReqInstance.ShowMtPayeCaisse(IdCommande)))
            for i in range(Ligne):
                AnnuleCaisse = self.Ui.TableauAnnulationCaisse.topLevelItem(i).text(10)
                self.Ui.AnnuleCaisseResulteLineEdit.setText(AnnuleCaisse)

    def ShowAnnulationDetailCaisse(self):
        IdCommande = self.Ui.TableauAnnulationCaisse.selectedItems()[0].text(0)
        self.Ui.TableauAnnulationCaisseDetail.clear()  # vider le tableau
        Ligne = 0  # je crée l'instance Ligne qui prend la valeur 0
        for i in self.ReqInstance.ShowDetailCaisse(IdCommande):
            QtWidgets.QTreeWidgetItem(self.Ui.TableauAnnulationCaisseDetail)  # je crée une ligne vide
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(0, str(i[0]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(1, str(i[1]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(2, str(i[2]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(3, str(i[3]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(4, str(i[4]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(5, str(i[5]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(6, str(i[6]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(7, str(i[7]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(8, str(i[8]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(9, str(i[9]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(10, str(i[10]))
            self.Ui.TableauAnnulationCaisseDetail.topLevelItem(Ligne).setText(11, str(i[11]))

            Ligne += 1

    def AnnulationUpdateStock(self):
        Ligne = 0

        for i in range(Ligne):
            IdProduit = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(1)
            Quantite = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(4)
            Departement = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(8)
            Data = (IdProduit, Quantite)
            if Departement == "PHARMACIE" :
                self.ReqInstance.AnnulationCaisseUpdateQteStock(Data)
            else:
                pass

    def AnnulationCaisse(self):
        # Ligne = 0
        IdCommande = self.Ui.RappelNumCommandecaisseLineEdit.text()
        # AnnuleCaisse = "ENCAISSEMENT ANNULE"
        AnnuleCaisse = 1
        DateAnnulationCaisse = datetime.now()
        Data = (AnnuleCaisse,DateAnnulationCaisse,IdCommande)
        if self.ReqInstance.AnnulationCaisse(AnnuleCaisse,DateAnnulationCaisse,IdCommande) == 0 :

            for i in range(self.Ligne):
                IdProduit = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(1)
                Quantite = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(4)
                Departement = self.Ui.TableauAnnulationCaisseDetail.topLevelItem(i).text(8)
                DataStock = (IdProduit, Quantite)
                if Departement == "PHARMACIE" :
                    self.ReqInstance.AnnulationCaisseUpdateQteStock(DataStock)
                else:
                    pass

            self.Ui.CaisseConfirmationAnnuleLabel.setText("L'encaissement a été annulé avec succès")
            self.Ui.CaisseConfirmationAnnuleLabel.setStyleSheet("Color:green;")
            self.Ui.RappelNumCommandecaisseLineEdit.setText(" ")
            self.Ui.TotalBrutAnnulerCaisseLabel.setText("0")
            self.Ui.TotalPecAnnulerCaisseLabel.setText("0")
            self.Ui.TotalPayeAnnulerCaisseLabel.setText("0")
            self.Ui.TableauAnnulationCaisse.clear()
            self.Ui.TableauAnnulationCaisseDetail.clear()







if __name__=="__main__":
    App = QtWidgets.QApplication([])
    Win = Recettes()
    Win.show()
    sys.exit(App.exec())