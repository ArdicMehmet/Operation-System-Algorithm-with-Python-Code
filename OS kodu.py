import time
import numpy as np


class OperationSystem :
    def __init__(self):
        self.SürecSonHali=list()
        self.süre=0

    def FCFS(self,Sürecler):
        süre=0

        for sürec in Sürecler:

            self.IslemiBaslat(sürec,sürec[1])


    def SJF(self,Sürecler):

        for i in range(len(Sürecler)):
            öncelikli = Sürecler[0]

            for y in range(0, len(Sürecler)):
                if self.süre>=Sürecler[y][0]:
                    if öncelikli[1]>Sürecler[y][1]:
                        öncelikli=Sürecler[y]
                        sil=y

            self.IslemiBaslat(öncelikli,öncelikli[1])
            if len(Sürecler)!=0:
                Sürecler.remove(öncelikli)


    def SRJF(self,Sürecler):
        toplam=0
        for i in range(len(Sürecler)):
            toplam+=Sürecler[i][1]
        öncelikli = Sürecler[0]
        burda=0
        for i in range(toplam):

            for y in range(0, len(Sürecler)):

                if self.süre >= Sürecler[y][0]:
                    if öncelikli[1] > Sürecler[y][1]:
                        öncelikli = Sürecler[y]



            self.IslemiBaslat(öncelikli,1)
            öncelikli[1] = öncelikli[1] - 1


            if öncelikli[1] == 0:
                Sürecler.remove(öncelikli)
                if len(Sürecler) != 0:
                    öncelikli=Sürecler[0]
                else:
                    break
                '''for z in range(len(Sürecler)):
                    if self.süre >= Sürecler[z][0]:
                        if öncelikli[1] > Sürecler[z][1]:
                            öncelikli = Sürecler[z] '''


    def RoundRobin(self,Sürecler,deger):


        while len(Sürecler)!=0:
            if len(Sürecler)>1 and Sürecler[0][1]+self.süre<Sürecler[1][0]:
                self.IslemiBaslat(Sürecler[0], Sürecler[0][1])

            else:
                if Sürecler[0][1]<deger:
                    self.IslemiBaslat(Sürecler[0], Sürecler[0][1])

                else:
                    self.IslemiBaslat(Sürecler[0],deger)
                    Sürecler[0][1]=Sürecler[0][1] - deger
                    Sürecler.append(Sürecler[0])
            del Sürecler[0]



    def IslemiBaslat(self,sürec,zaman):

        if sürec[0]>self.süre:
            while sürec[0]>self.süre:
                print(f'{"Sistem Boşta Sn:"}{self.süre}')
                time.sleep(1)
                self.süre+=1

        for i in range(zaman):
            print(f'{"P"}{sürec[2]}{"Süreci Calisiyor Sn :"}{self.süre}')
            time.sleep(1)
            self.süre+=1


    def Sürec_Düzenle(self,Sürecler,Yöntem):
        if Yöntem==1:
            self.FCFS(Sürecler)
        if Yöntem==2:
            self.SJF(Sürecler)
        if Yöntem==3:
            self.SRJF(Sürecler)
        if Yöntem == 4:
            deger=0
            deger=int(input("Lutfen Quantum time ı girin "))
            self.RoundRobin(Sürecler,deger)

def SürecOlustur():

    Sürecler=list()
    count = 0
    Süre=0
    while True :
        try:

            GelisZamani,Süre=input("Lütfen Sırasıyla Geliş Zamanını ve "
                                       "Süresini Giriniz "
                                       "Çıkmak İçin Süreye 0 yazınız").split()
            GelisZamani=int(GelisZamani)
            Süre=int(Süre)
            if Süre == 0:
                break
            Sürecler.append([GelisZamani,Süre,count])
            count+=1
        except:
            print("Sayi Girmediniz")
    Sürecler.sort()


    Secim=int(input("Lütfen Sürec Yöntemi Seciniz:\n"
                "1-FCFS\n"
                "2-SJF\n"
                "3-SRJF\n"
                "4-Round Robin "))
    return Sürecler,Secim



Sürecler,Tercih=SürecOlustur()
OS=OperationSystem()
OS.Sürec_Düzenle(Sürecler,Tercih)







