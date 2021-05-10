import nmap
nmScan = nmap.PortScanner()
hedef = input('Tarama yapmak istediğiniz ip adresi --> ')
dosyadi = input('Rapor adı --> ')
nmScan.scan('-oX ' + dosyadi + ' ' + hedef)

