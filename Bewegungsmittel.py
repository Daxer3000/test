#Basis Klasse
class Bewegungsmittel():
    def __init__(self,Geschwindigkeit=200,Ps=600,Art_der_Fortbewegung="Land und Fahrend",Sitzplätze=6,öffentlich=True,Tank=80,aktueller_Tank=0):
        self.kmh=Geschwindigkeit
        self.ps=Ps
        self.fort=Art_der_Fortbewegung
        self.sitze=Sitzplätze
        self.public=öffentlich
        self.tank=Tank
        self.nowtank=aktueller_Tank
    #Tank füllen
    def fill_in(self,much):
        print("Tank ist zu ",self.nowtank / self.tank *100," Prozent gefüllt ")
        if self.tank==self.nowtank:
            print("Error Tank ist voll")
        elif self.nowtank + much >self.tank:
            print("so viel ist nicht einfüll bar")
        else:
            self.nowtank=self.nowtank+much
            print("Tank ist jetzt zu ",self.nowtank / self.tank *100," Prozent voll" )
#neue Klasse mit vererrbung von Klasse Bewegungsmittel
class Flugzeug(Bewegungsmittel):
    def _init__(self,höhe_Flug=10000,aktuelle_höhe=0):
        Bewegungsmittel.__init__(self)
        self.höhe_flug=höhe_Flug
        self.nowhöhe=aktuelle_höhe
Auto=Bewegungsmittel(Ps=300)
Auto.fill_in(40)
Fliger=Flugzeug(100)
print(Fliger.kmh,"kmh Zahl des Flugzeugs")
