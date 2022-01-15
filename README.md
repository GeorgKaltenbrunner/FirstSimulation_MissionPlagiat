# FirstSimulation_MissionPlagiat

Generelle Frage: Was mag ich herausfinden?
- Optimale Maschinenbelegung?
- Optimale Produktionsreihenfolge?

Generell benötigt:
- Dictionary mit Infos, wie lange verschiedene Produkte in der Produktion (Für Maschine A und B) benötigen
- Liste der jeweiligen Orders -> mit Dictionary abgleichbar um die Produktionszeit herauszubekommen
- Werden sonst Ressourcen simuliert? -> zunächst nur Maschinen einzige Ressource
- Die class Factory(object) -> hier passiert alles
- Maschine A und Maschine B

### 1. Aufträge werden generiert
- randomly werden gewisse Aufträge generiert -> über numpy
- Liste der Aufträge
### 2. Maschine bearbeitet die Aufträge

### 3. Nach Bearbeitung werden Aufträge im Lager gelagert

### 4. Löschung