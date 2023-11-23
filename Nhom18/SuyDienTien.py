from Connection import *
from RuleDefine import *

class SuyDienTien:
    def __init__(self):
        self.kn = KetNoi()
        self.bin = []
        self.SAT = []
        self.demLuat = 0

    def DocLuatTuFfile(self):
        qr = 'select noidung from Luat'
        tbLuat = self.kn.getTable(qr)

        for row in tbLuat:
            buff = row[0]
            luatTG = RuleDefine()
            tg = buff.split('>')
            # Ben trai
            left = tg[0].split('^')
            for buff1 in left:
                luatTG.left.append(buff1)
            # Ben phai
            right = tg[1].split(',')
            for buff1 in right:
                luatTG.right.append(buff1)
            self.bin.append(luatTG)
            
            self.demLuat += 1

    def XuatLuat(self, mangLuat):
        tg = ""
        for r in mangLuat:
            tg += "^".join(r.left) + "->" + "^".join(r.right) + "\n"
        return tg

    def CheckIn(self, a, b):
        dem = 0
        for tg1 in a:
            for tg2 in b:
                if tg1 == tg2:
                    dem += 1
        return dem == len(a)

    def TimTapSat(self, L, mangLuat):
        i = 0
        for lTG in mangLuat:
            if self.CheckIn(L, lTG.left) and lTG not in self.SAT:
                self.SAT.append(lTG)
                

    # def SuyDien(self, left, right):
    #     mangLuat = self.bin
    #     TG = left
    #     KL = right
    #     self.TimTapSat(TG, mangLuat)
        
    #     while len(self.SAT) > 0 and not self.CheckIn(KL, TG):
    #         r = self.SAT[0]
    #         mangLuat.remove(r)
    #         self.SAT.pop(0)

    #         for tg in r.right:
    #             if tg not in TG:
    #                 TG.append(tg)
    #                 print(tg)

    #         self.TimTapSat(TG, mangLuat)
    #     # for r in TG:
    #     #     print(r)
    #     return self.CheckIn(TG, KL)
    
    def SuyDien(self, left):
        mangLuat = self.bin
        TG = left
        result = []
        # KL = right
        self.TimTapSat(TG, mangLuat)
        
        while len(self.SAT) > 0:
            r = self.SAT[0]
            mangLuat.remove(r)
            self.SAT.pop(0)

            for tg in r.right:
                if tg not in TG:
                    TG.append(tg)
                    # print(tg)
                    result.append(tg)

            self.TimTapSat(TG, mangLuat)
            # print(TG)
        return result

# suy_dien_instance = SuyDienTien()
# suy_dien_instance.DocLuatTuFfile()
# KQ = suy_dien_instance.SuyDien(['K1', 'HL4'])

# print(KQ)
    