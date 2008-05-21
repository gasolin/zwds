#!/usr/bin/python
# -*- coding: utf-8 -*-

from core import *
from lunar import *

def p_53d6_5f97_5c0d_6c96_v(p_5730_652f_v):
    """
    正對著本支的地支
    十二地支組成六沖
    
    zwds: 又稱 "沖宮" 及 "對宮"
    """
    return p_5730_652f_8868_v[(p_5730_652f_8868_v.index(p_5730_652f_v)+6)%12]

def p_53d6_5f97_4e09_5408_v(p_5730_652f_v):
    """
    
    zwds 又稱 "三方"
    """
    return [p_5730_652f_8868_v[(p_5730_652f_8868_v.index(p_5730_652f_v)+i)%12] for i in (4,8)]

def p_53d6_5f97_516d_5408_v(p_5730_652f_v):
    """
    與星曜間於不同宮位的強弱程度 (廟陷) 有關
    """
    p_516d_5408_v = {p_5b50_v:p_4e11_v, p_5bc5_v:p_4ea5_v, p_536f_v:p_620c_v,
           p_8fb0_v:p_9149_v, p_5df3_v:p_7533_v, p_5348_v:p_672a_v,
           p_672a_v:p_5348_v, p_7533_v:p_5df3_v, p_9149_v:p_8fb0_v,
           p_620c_v:p_536f_v, p_4ea5_v:p_5bc5_v, p_4e11_v:p_5b50_v,
        }
    return p_516d_5408_v[p_5730_652f_v]


# 古時月份從3月開始
p_5bc5_5bae_5730_652f_8868_v = p_5730_652f_8868_v[2:]+p_5730_652f_8868_v[:2]

# zwds
# 五行局數 河圖+洛書
# http://hk.myblog.yahoo.com/lawrencioy/article?mid=363
# http://hk.myblog.yahoo.com/lawrencioy/article?mid=368
p_706b_v.p_5c40_6578_v = 6
p_571f_v.p_5c40_6578_v = 5
p_91d1_v.p_5c40_6578_v = 4 
p_6728_v.p_5c40_6578_v = 3
p_6c34_v.p_5c40_6578_v = 2


class p_661f_66dc_v(object):
    """
    紫微星曜
    """
    def __init__(self, p_540d_7a31_v, repr, p_985e_578b_v, p_6642_8fb0_v="", p_7d1a_6578_v=""):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.repr = repr
        self.p_6b63_66dc_v = False
        self.p_5316_66dc_v = False
        #輔佐吉
        self.p_8f14_66dc_v = False
        self.p_4f50_66dc_v = False
        self.p_7a7a_52ab_v = False
        self.p_7a7a_66dc_v = False
        self.p_5211_66dc_v = False
        self.p_5fcc_66dc_v = False
        self.p_715e_66dc_v = False
        self.p_6843_82b1_v = False
        self.p_6587_66dc_v = False
        self.p_79d1_540d_v = False
        self.p_96dc_66dc_v = False

        if "正" in p_985e_578b_v:
            self.p_6b63_66dc_v = True
        if "化" in p_985e_578b_v:
            self.p_5316_66dc_v = True
        if "輔" in p_985e_578b_v:
            self.p_8f14_66dc_v = True
        if "佐" in p_985e_578b_v:
            self.p_4f50_66dc_v = True
        if "劫" in p_985e_578b_v:
            self.p_7a7a_52ab_v = True
        if "空" in p_985e_578b_v:
            self.p_7a7a_66dc_v = True
        if "刑" in p_985e_578b_v:
            self.p_5211_66dc_v = True
        if "忌" in p_985e_578b_v:
            self.p_5fcc_66dc_v = True
        if "煞" in p_985e_578b_v:
            self.p_715e_66dc_v = True
        if "桃" in p_985e_578b_v:
            self.p_6843_82b1_v = True
        if "文" in p_985e_578b_v:
            self.p_6587_66dc_v = True
        if "科" in p_985e_578b_v:
            self.p_79d1_540d_v = True
        if "雜" in p_985e_578b_v:
            self.p_96dc_66dc_v = True
        self.p_6642_8fb0_v = p_6642_8fb0_v
        self.p_7d1a_6578_v = p_7d1a_6578_v

    def __str__(self):
        return self.p_540d_7a31_v

# 114 星
#紫微
p_7d2b_5fae_v = p_661f_66dc_v("紫微", "", ["正"], "八字", "甲")
p_5929_6a5f_v = p_661f_66dc_v("天機", "", ["正"], "八字", "甲")
p_592a_967d_v = p_661f_66dc_v("太陽", "", ["正"], "八字", "甲")
p_6b66_66f2_v = p_661f_66dc_v("武曲", "", ["正"], "八字", "甲")
p_5929_540c_v = p_661f_66dc_v("天同", "", ["正"], "八字", "甲")
p_5ec9_8c9e_v = p_661f_66dc_v("廉貞", "", ["正"], "八字", "甲")

# 天府
p_5929_5e9c_v = p_661f_66dc_v("天府", "", ["正"], "八字", "甲")
p_592a_9670_v = p_661f_66dc_v("太陰", "", ["正"], "八字", "甲")
p_8caa_72fc_v = p_661f_66dc_v("貪狼", "", ["正"], "八字", "甲")
p_5de8_9580_v = p_661f_66dc_v("巨門", "", ["正"], "八字", "甲")
p_5929_76f8_v = p_661f_66dc_v("天相", "", ["正"], "八字", "甲")
p_5929_6881_v = p_661f_66dc_v("天梁", "", ["正"], "八字", "甲")
p_4e03_6bba_v = p_661f_66dc_v("七殺", "", ["正"], "八字", "甲")
p_7834_8ecd_v = p_661f_66dc_v("破軍", "", ["正"], "八字", "甲")

# 年干系星
p_5929_9b41_v = p_661f_66dc_v("天魁", "", ["輔"], "年干", "甲")
p_5929_925e_v = p_661f_66dc_v("天鉞", "", ["輔"], "年干", "甲")
p_797f_5b58_v = p_661f_66dc_v("祿存", "", ["佐"], "年干", "甲")
p_64ce_7f8a_v = p_661f_66dc_v("擎羊", "", ["煞", "刑"], "年干", "甲")
p_9640_7f85_v = p_661f_66dc_v("陀羅", "", ["煞", "忌"], "年干", "甲")
p_5929_5b98_v = p_661f_66dc_v("天官", "", ["科"], "年干", "乙")
p_5929_5eda_v = p_661f_66dc_v("天廚", "", ["科"], "年干", "")
p_5929_798f_v = p_661f_66dc_v("天福", "", ["科"], "年干", "乙")
p_5316_797f_v = p_661f_66dc_v("化祿", "", ["化"], "年干", "甲")
p_5316_6b0a_v = p_661f_66dc_v("化權", "", ["化"], "年干", "甲")
p_5316_79d1_v = p_661f_66dc_v("化科", "", ["化", "文", "科"], "年干", "甲")
p_5316_5fcc_v = p_661f_66dc_v("化忌", "", ["化", "忌"], "年干", "甲")
p_622a_7a7a_v = p_661f_66dc_v("截空", "", ["空"], "年干", "丙")
p_622a_8def_v = p_622a_7a7a_v
p_65ec_7a7a_v = p_661f_66dc_v("旬空", "", ["空"], "年干", "丙")
p_7a7a_4ea1_v = p_65ec_7a7a_v
# 博士、力士、青龍、小耗、將軍、奏書、飛廉、喜神、病符、大耗、伏兵、官府。長生
p_6c90_6d74_v = p_661f_66dc_v("沐浴", "", ["桃"], "年干", "丙")
# 冠帶、臨官、帝旺、衰、病、死、墓、絕、胎、養。

# 年支系星
p_7d05_9e1e_v = p_661f_66dc_v("紅鸞", "", ["桃"], "年干", "乙")
p_5929_559c_v = p_661f_66dc_v("天喜", "", ["桃"], "年干", "乙")
p_9f8d_6c60_v = p_661f_66dc_v("龍池", "", ["文", "科"], "年干", "乙")
p_9cf3_95a3_v = p_661f_66dc_v("鳳閣", "", ["文", "科"], "年干", "乙")
#天德、解神、天哭、天虛、弧辰、寡宿
p_5929_99ac_v = p_661f_66dc_v("天馬", "", ["佐"], "年干", "甲")
p_5929_7a7a_v = p_661f_66dc_v("天空", "", ["空"], "年干", "乙")
# 蜚廉、破碎、年解
p_5927_8017_v = p_661f_66dc_v("大耗", "", ["桃"], "年干", "丙")
#月德
p_5929_624d_v = p_661f_66dc_v("天才", "", ["文", "科"], "年干", "乙")
#天壽
p_706b_661f_v = p_661f_66dc_v("火星", "", ["煞"], "年干", "甲")
p_9234_661f_v = p_661f_66dc_v("鈴星", "", ["煞"], "年干", "甲")
# 將星、攀鞍、歲驛、息神、華蓋、劫煞、災煞、天煞、指背
p_54b8_6c60_v = p_661f_66dc_v("咸池", "", ["桃"], "年干", "乙")
#月煞、亡神。
# 太歲、晦氣、喪門、貫索、官符、小耗、歲破、龍德、白虎、天德、吊客、病符。

# 月系星
p_5de6_8f14_v = p_661f_66dc_v("左輔", "", ["輔"], "月", "甲")
p_53f3_5f3c_v = p_661f_66dc_v("右弼", "", ["輔"], "月", "甲")
p_5929_5211_v = p_661f_66dc_v("天刑", "", ["刑"], "月", "乙")
# 解神、天巫、天月
p_5929_59da_v = p_661f_66dc_v("天姚", "", ["桃"], "月", "乙")
#陰煞。

# 日系星
p_4e09_53f0_v = p_661f_66dc_v("三台", "", ["科"], "日", "乙")
p_516b_5ea7_v = p_661f_66dc_v("八座", "", ["科"], "日", "乙")
p_6069_5149_v = p_661f_66dc_v("恩光", "", ["科"], "日", "乙")
p_5929_8cb4_v = p_661f_66dc_v("天貴", "", ["科"], "日", "乙")

# 時系星
p_6587_660c_v = p_661f_66dc_v("文昌", "", ["佐", "文", "科"], "時", "甲")
p_6587_66f2_v = p_661f_66dc_v("文曲", "", ["佐", "文", "科"], "時", "甲")
p_5730_7a7a_v = p_661f_66dc_v("地空", "", ["劫", "空"], "時", "甲")
p_5730_52ab_v = p_661f_66dc_v("地劫", "", ["劫", "空"], "時", "甲")
p_53f0_8f14_v = p_661f_66dc_v("台輔", "", ["科"], "時", "乙")
p_5c01_8aa5_v = p_661f_66dc_v("封誥", "", ["科"], "時", "乙")




class p_5bae_57a3_v(object):
    """
    人事12宮垣
    http://hk.myblog.yahoo.com/lawrencioy/article?mid=118
    http://hk.myblog.yahoo.com/lawrencioy/article?mid=124

                  命身 
             兄弟      父母
        夫妻                福德        家庭人倫
    子女 ----------------------- 田宅 --------------
        財帛                事業        環境際遇
             疾厄      交友
                  遷移
    
    數往者順，知來者逆
    """
    def __init__(self, p_540d_7a31_v, repr):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.repr = repr
        self.p_5929_5e72_v = None #寅宮天干
        self.p_5730_652f_v = None #寅宮地支
        self.p_6b63_66dc_v = [] #甲級星
        self.p_8f14_66dc_v = [] #乙級星
        self.p_96dc_66dc_v = []

    def __str__(self):
        return self.p_540d_7a31_v

    # 宮位方法
    def p_540c_5bae_v(self):
        pass

    p_540c_5ea6_v = p_540c_5bae_v

# 本宮: 可用地支代表, 亦可用人事十二宮稱之
p_547d_5bae_v = p_5bae_57a3_v('命宮', '主個人先後天性格，人格特質，一生命運趨勢。個人先天個性與人格特質')
p_547d_8eab_v = p_547d_5bae_v
p_5144_5f1f_v = p_5bae_57a3_v('兄弟', '兄弟姊妹人數及關係；亦主與平輩間的關係。對兄弟或親友的態度')
p_592b_59bb_v = p_5bae_57a3_v('夫妻', '感情路上坦蕩，夫妻關係，婚姻狀況，配偶性格樣貌。對感情的處理態度及婚姻的相處模式')
p_9053_60c5_v = p_592b_59bb_v #佛道
p_5b50_5973_v = p_5bae_57a3_v('子女', '子女性格、多寡；引申表示與晚輩的關係。個人對子女的管教態度及期望')
p_5f1f_5b50_v = p_5b50_5973_v #佛道
p_8ca1_5e1b_v = p_5bae_57a3_v('財帛', '財政狀況，進財性質及方法，能否持盈。個人的理財模式')
p_75be_5384_v = p_5bae_57a3_v('疾厄', '易患何種疾病，宿疾有無，災厄意外的可能。個人對健康狀況的態度及處理模式')
p_9077_79fb_v = p_5bae_57a3_v('遷移', '社交能力，人際關係；移居、經營狀況、旅行遭遇等。亦能反映命運的趨勢。對外的人際關係，及發展的情況')
p_4ea4_53cb_v = p_5bae_57a3_v('交友', '與雇員或下屬的關係，並反映人際關係總體情況。個人與友人、部屬、同僚間的相處態度')
p_5974_50d5_v = p_4ea4_53cb_v
p_4e8b_696d_v = p_5bae_57a3_v('事業', '主事業運勢。個人事業的發展模式及態度')
p_5b98_797f_v = p_4e8b_696d_v
p_5e2b_865f_v = p_4e8b_696d_v #佛道
p_7530_5b85_v = p_5bae_57a3_v('田宅', '產業運勢，會否繼承，繼承後可有破敗，會否置業；何時遷居，及風水影響程度等。個人對理財的態度，與財帛宮互補')
p_798f_5fb7_v = p_5bae_57a3_v('福德', '思想活動與精神享受。個人思想及心態、慾望的強弱')
p_7236_6bcd_v = p_5bae_57a3_v('父母', '父母夭壽，與其緣份；上司關係，官吏機構關係。個人對父母或親長的態度及期望')
p_76f8_8c8c_v = p_7236_6bcd_v

# 順行
p_5341_4e8c_5bae_8868_v = [p_547d_5bae_v, p_7236_6bcd_v, p_798f_5fb7_v, p_7530_5b85_v, p_4e8b_696d_v, p_4ea4_53cb_v, p_9077_79fb_v, p_75be_5384_v, p_8ca1_5e1b_v, p_5b50_5973_v, p_592b_59bb_v, p_5144_5f1f_v]

# 對宮: 與本宮構成對沖關係的宮垣
p_547d_5bae_v.p_5c0d_5bae_v = p_9077_79fb_v # 取得對沖(命宮.地支)
p_7236_6bcd_v.p_5c0d_5bae_v = p_8ca1_5e1b_v
p_798f_5fb7_v.p_5c0d_5bae_v = p_75be_5384_v
p_7530_5b85_v.p_5c0d_5bae_v = p_5b50_5973_v
p_4e8b_696d_v.p_5c0d_5bae_v = p_592b_59bb_v
p_4ea4_53cb_v.p_5c0d_5bae_v = p_5144_5f1f_v
p_9077_79fb_v.p_5c0d_5bae_v = p_547d_5bae_v
p_75be_5384_v.p_5c0d_5bae_v = p_798f_5fb7_v
p_8ca1_5e1b_v.p_5c0d_5bae_v = p_7236_6bcd_v
p_5b50_5973_v.p_5c0d_5bae_v = p_7530_5b85_v
p_592b_59bb_v.p_5c0d_5bae_v = p_4e8b_696d_v
p_5144_5f1f_v.p_5c0d_5bae_v = p_4ea4_53cb_v

# 宮位關係
# 合宮: 與本宮構成三合關係的宮垣 取得對沖(地支)+取得三合(地支)
# 鄰宮: 本宮的左右兩宮
# 三方: 即三合宮位
# 四正: 三合宮加上對宮 [本宮]+取得對沖(地支)+取得三合(地支)
# 坐守: 星曜躔度本宮為之坐守
# 同度，同宮: 除已有星曜外，還有其他星曜坐守
# 對拱、拱照、朝拱: 星曜於對宮坐守
# 會照: 星曜於三合宮坐守
# 相夾: 星曜分別於鄰宮坐守
# 見: 星曜於三方四正宮位統稱為見
# 沖: 煞忌刑曜於三方四正宮位統稱為沖
# 由於安星規律的規範，斗數中某些星曜必然會於對宮及三合宮會照


"""
排盤

1. 找出命、身宮，
2. 再求五行局，
3. 找出紫微星與天府星

chunk 星, template 三方四正, 策略 局

一出生即為一歲,
過一立春算加一歲

由命宮始, 陽男陰女大限順行


西元日期 - 西曆轉農曆(Adapter) - 紫微星盤

"""
        
class p_751f_8fb0_516b_5b57_v(object):
    """
    時間基礎
    """
    def __init__(self, p_59d3_540d_v, p_6027_5225_v, p_5e72_652f_v, p_751f_6708_v, p_751f_65e5_v, p_751f_6642_v, p_958f_6708_v=0):
        self.p_59d3_540d_v = p_59d3_540d_v
        self.p_6027_5225_v = p_6027_5225_v
        self.p_5e72_652f_v = p_5e72_652f_v #生年
        self.p_751f_5e74_v = p_5e72_652f_v
        self.p_751f_6708_v = p_751f_6708_v
        self.p_958f_6708_v = p_958f_6708_v
        self.p_751f_65e5_v = p_751f_65e5_v
        self.p_751f_6642_v = p_751f_6642_v
        self.p_6642_8fb0_v = p_751f_6642_v


from copy import deepcopy
class p_7d2b_5fae_6597_6578_v(p_751f_8fb0_516b_5b57_v):
    """
    出生時辰 < 命宮位置 < 命宮天干 < 五行局 < 紫微星 > 十四主星
    http://hk.myblog.yahoo.com/lawrencioy/article?mid=257
    """
    def __init__(self, p_59d3_540d_v, p_6027_5225_v, p_751f_5e74_v, p_751f_6708_v, p_751f_65e5_v, p_751f_6642_v, p_958f_6708_v = 0):

        super(p_7d2b_5fae_6597_6578_v, self).__init__(p_59d3_540d_v, p_6027_5225_v, p_751f_5e74_v, p_751f_6708_v, p_751f_65e5_v, p_751f_6642_v, p_958f_6708_v)

        # 1. 安命身宮
        self.p_547d_5bae_v = self._p_53d6_547d_5bae_v() #命宮地支
        self.p_8eab_5bae_v = self._p_53d6_8eab_5bae_v()
        self.p_547d_4e3b_v = self._p_53d6_547d_4e3b_v()
        self.p_8eab_4e3b_v = self._p_53d6_8eab_4e3b_v()

        # 2. 安十二宮
        self.__p_547d_5bae_5730_652f_v = p_5bc5_5bae_5730_652f_8868_v.index(self.p_547d_5bae_v)
        # 讓各個紫微斗數物件擁有獨立的宮垣物件
        self.p_5341_4e8c_5bae_4f4d_v = deepcopy(p_5341_4e8c_5bae_8868_v[-self.__p_547d_5bae_5730_652f_v:]) + \
                    deepcopy(p_5341_4e8c_5bae_8868_v[:-self.__p_547d_5bae_5730_652f_v])

        # 3. 定宮位天干
        self.p_5bc5_5bae_5929_5e72_8868_v = p_5929_5e72_8868_v[p_5929_5e72_8868_v.index(self.p_4e94_864e_9041_v(self.p_751f_5e74_v.p_5929_5e72_v)):] + \
                    p_5929_5e72_8868_v[:(p_5929_5e72_8868_v.index(self.p_4e94_864e_9041_v(self.p_751f_5e74_v.p_5929_5e72_v))+2)]
        # 將寅宮干支填入十二宮位
        for p_9806_5e8f_v, p_5bae_4f4d_v in enumerate(self.p_5341_4e8c_5bae_4f4d_v):
            p_5bae_4f4d_v.p_5929_5e72_v = self.p_5bc5_5bae_5929_5e72_8868_v[p_9806_5e8f_v]
            p_5bae_4f4d_v.p_5730_652f_v = p_5bc5_5bae_5730_652f_8868_v[p_9806_5e8f_v]

        # 4. 安五行局
        self.p_4e94_884c_5c40_v = self._p_5b89_4e94_884c_5c40_v()
        # 5. 安十四主星的宮位
        self._p_5b89_5341_56db_4e3b_661f_v()
        # 6. 安輔、佐、煞、化、雜曜
        # 安四化
        self._p_5b89_56db_5316_661f_v()
        # 安輔佐諸曜
        self._p_5b89_4e03_5409_516d_715e_661f_v()
        # 
        self._p_5b89_5e74_7cfb_661f_v()
        self._p_5b89_6708_7cfb_661f_v()
        self._p_5b89_65e5_7cfb_661f_v()
        # 判斷亮度

    def _p_53d6_547d_5bae_v(self):
        """
        出生月份宮度起子時, 逆時針數到出生時辰
        
        月數減時辰數再加一
        
        寅正順數月逄。
        生月起子二頭通。
        逆至生時為命。
        順至生時為身。
        """
        return p_5bc5_5bae_5730_652f_8868_v[(p_5bc5_5bae_5730_652f_8868_v.index(p_5bc5_5bae_5730_652f_8868_v[self.p_751f_6708_v-1]) - p_5730_652f_8868_v.index(self.p_751f_6642_v))%12]
    
    def _p_53d6_8eab_5bae_v(self):
        """
        出生月份宮度起子時, 順時針數到出生時辰
        
        月數加時辰數再減一
        """
        return p_5bc5_5bae_5730_652f_8868_v[(p_5bc5_5bae_5730_652f_8868_v.index(p_5bc5_5bae_5730_652f_8868_v[self.p_751f_6708_v-1]) + p_5730_652f_8868_v.index(self.p_751f_6642_v))%12]

    def _p_53d6_547d_4e3b_v(self, p_985e_578b_v = 2):
        """
        承自 果老星宗 命術
        唯當命宮無主星，或命主星處於命宮三方四正方位時，星性會影響命主的個性。

        子屬貪狼丑亥門
        寅戌生人屬祿存
        卯酉屬文巳未武
        辰申廉宿午破軍
        
        類型1: 據出生年的地支而定
        類型2: 以命宮所在宮位的地支而定, 同 果老星宗
        """
        if p_985e_578b_v == 1:
            p_652f_v = self.p_751f_5e74_v.p_5730_652f_v
        if p_985e_578b_v == 2:
            p_652f_v = self.p_547d_5bae_v

        if p_652f_v == p_5b50_v:
            return p_8caa_72fc_v
        elif p_652f_v in (p_4e11_v, p_4ea5_v):
            return p_5de8_9580_v
        elif p_652f_v in (p_5bc5_v, p_620c_v):
            return p_797f_5b58_v
        elif p_652f_v in (p_536f_v, p_9149_v):
            return p_6587_66f2_v
        elif p_652f_v in (p_5df3_v, p_672a_v):
            return p_6b66_66f2_v
        elif p_652f_v in (p_8fb0_v, p_7533_v):
            return p_5ec9_8c9e_v
        elif p_652f_v == p_5348_v:
            return p_7834_8ecd_v

    def _p_53d6_8eab_4e3b_v(self):
        """
        看形性面貌的輔助
        當身主星處於命宮三方四正方位，同樣使身主所主的形性面貌更為明顯

        天機南斗第一星屬木
        天相南斗第二星屬水
        天梁南斗第三星屬土
        天同南斗第四星屬水
        文昌南斗第六星屬金
        火星屬火
        
        用生年地支為依據
        子支及午支對應的星曜有不同看法
        """
        p_652f_v = self.p_751f_5e74_v.p_5730_652f_v

        if p_652f_v in (p_5b50_v, p_5348_v):
            return p_706b_661f_v
        elif p_652f_v in (p_4e11_v, p_672a_v):
            return p_5929_76f8_v
        elif p_652f_v in (p_5bc5_v, p_7533_v):
            return p_5929_6881_v
        elif p_652f_v in (p_536f_v, p_9149_v):
            return p_5929_540c_v
        elif p_652f_v in (p_8fb0_v, p_620c_v):
            return p_6587_660c_v
        elif p_652f_v in (p_5df3_v, p_4ea5_v):
            return p_5929_6a5f_v

    def p_4e94_864e_9041_v(self, p_751f_5e74_5929_5e72_v):
        """
        定寅宮天干
        
        就命主出生的年干，按表尋得所化之五行
        找出該五行所洩的五行
        對應所洩五行的天干便是「寅」宮的天干
        """
        if p_751f_5e74_5929_5e72_v in (p_7532_v, p_5df1_v): # 土
            return p_571f_v.p_76f8_6d29_v.p_5929_5e72_v[0] #丙
        elif p_751f_5e74_5929_5e72_v in (p_4e59_v, p_5e9a_v): # 金
            return p_91d1_v.p_76f8_6d29_v.p_5929_5e72_v[0] #戊
        elif p_751f_5e74_5929_5e72_v in (p_4e19_v, p_8f9b_v): # 水
            return p_6c34_v.p_76f8_6d29_v.p_5929_5e72_v[0] #庚
        elif p_751f_5e74_5929_5e72_v in (p_4e01_v, p_58ec_v): # 木
            return p_6728_v.p_76f8_6d29_v.p_5929_5e72_v[0] #壬
        elif p_751f_5e74_5929_5e72_v in (p_620a_v, p_7678_v): # 火
            return p_706b_v.p_76f8_6d29_v.p_5929_5e72_v[0] #甲

    def _p_5b89_4e94_884c_5c40_v(self):
        """
        取得五行局數
        
        """
        p_5e72_652f_v = str(self.p_5bc5_5bae_5929_5e72_8868_v[self.__p_547d_5bae_5730_652f_v]) + str(self.p_547d_5bae_v)
        for p_82b1_7532_v in p_82b1_7532_8868_v:
            if p_5e72_652f_v == p_82b1_7532_v.p_540d_7a31_v:
                return p_82b1_7532_v.p_4e94_884c_5c40_v

    def _p_7d2b_5fae_661f_5bae_4f4d_v(self):
        """
        公式:
        出生日數+X%五行局數 = 0
        出生日數+X/五行局數 = Y
        
        """
        for y in range(1, 20):
            #如果 五行局數 * y >= 出生日數:
            #    x = 五行局數 * y - 出生日數
            if self.p_4e94_884c_5c40_v.p_5c40_6578_v * y >= self.p_751f_65e5_v:
                x = self.p_4e94_884c_5c40_v.p_5c40_6578_v * y - self.p_751f_65e5_v
                break
        if x % 2 == 0:
            return p_5bc5_5bae_5730_652f_8868_v[y + x -1]
        else:
            return p_5bc5_5bae_5730_652f_8868_v[y - x -1]
    
    def _p_5b89_7d2b_5fae_661f_7cfb_v(self, p_5bae_4f4d_v):
        """紫機一日, 武同二廉, 逆行"""
        #找宮位
        p_5bae_4f4d_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(p_5bae_4f4d_v)
        p_5bae_4f4d_v.p_6b63_66dc_v.append(p_7d2b_5fae_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-1].p_6b63_66dc_v.append(p_5929_6a5f_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-3].p_6b63_66dc_v.append(p_592a_967d_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-4].p_6b63_66dc_v.append(p_6b66_66f2_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-5].p_6b63_66dc_v.append(p_5929_540c_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-8].p_6b63_66dc_v.append(p_5ec9_8c9e_v)

    def _p_5929_5e9c_661f_5bae_4f4d_v(self, p_7d2b_5fae_5bae_4f4d_v):
        p_540c_5ea6_v = {p_5bc5_v:p_5bc5_v, p_7533_v:p_7533_v, p_4e11_v:p_536f_v, p_536f_v:p_4e11_v,
        	   p_5b50_v:p_8fb0_v, p_8fb0_v:p_5b50_v, p_5df3_v:p_4ea5_v, p_4ea5_v:p_5df3_v,
        	   p_5348_v:p_620c_v, p_620c_v:p_5348_v, p_672a_v:p_9149_v, p_9149_v:p_672a_v,
        }
        return p_540c_5ea6_v[p_7d2b_5fae_5bae_4f4d_v]

    def _p_5b89_5929_5e9c_661f_7cfb_v(self, p_5bae_4f4d_v):
        """府陰貪巨, 相梁殺三破 順行"""
        p_5bae_4f4d_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(p_5bae_4f4d_v)
        p_5bae_4f4d_v.p_6b63_66dc_v.append(p_5929_5e9c_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-2].p_6b63_66dc_v.append(p_7834_8ecd_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-6].p_6b63_66dc_v.append(p_4e03_6bba_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-7].p_6b63_66dc_v.append(p_5929_6881_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-8].p_6b63_66dc_v.append(p_5929_76f8_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-9].p_6b63_66dc_v.append(p_5de8_9580_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-10].p_6b63_66dc_v.append(p_8caa_72fc_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_5bae_4f4d_7d22_5f15_v-11].p_6b63_66dc_v.append(p_592a_9670_v)       

    def _p_5b89_5341_56db_4e3b_661f_v(self):
        """
        地支 -> 宮位 -> 正曜.更新(紫微)
        """
        self.__p_7d2b_5fae_5730_652f_v = self._p_7d2b_5fae_661f_5bae_4f4d_v()
        self.__p_5929_5e9c_5730_652f_v = self._p_5929_5e9c_661f_5bae_4f4d_v(self.__p_7d2b_5fae_5730_652f_v)
        for p_5bae_4f4d_v in self.p_5341_4e8c_5bae_4f4d_v:
           if p_5bae_4f4d_v.p_5730_652f_v == self.__p_7d2b_5fae_5730_652f_v:
               self._p_5b89_7d2b_5fae_661f_7cfb_v(p_5bae_4f4d_v)
           if p_5bae_4f4d_v.p_5730_652f_v == self.__p_5929_5e9c_5730_652f_v:
               self._p_5b89_5929_5e9c_661f_7cfb_v(p_5bae_4f4d_v)
    def _p_5b89_56db_5316_661f_v(self):
        """
        祿權科忌
        
        甲廉破武陽, 乙機梁紫陰, 丙同機昌廉,
        丁陰同機巨, 戊貪陰陽機, 己武貪梁曲,
        庚陽武府同, 辛巨陽曲昌, 壬梁紫府武,
        癸破巨陰貪
        """
        #TODO: not finish yet
        pass

    def _p_5b89_4e03_5409_516d_715e_661f_v(self):
        """
        左右、昌曲、魁鉞、祿馬
        羊陀、火鈴、空劫、天刑
        文曲星是由辰宮開始，順數到生時
        文昌星是由戌宮開始，逆數到生時
        左輔星是由辰宮開始，順數到生月
        右弼星是由戌宮開始，逆數到生月
        """
        #祿存, 羊陀
        p_797f_v = {p_7532_v:p_5bc5_v, p_4e59_v:p_536f_v, p_4e19_v:p_5df3_v, p_4e01_v:p_5348_v, p_620a_v:p_5df3_v, p_5df1_v:p_5348_v, p_5e9a_v:p_7533_v, p_8f9b_v:p_9149_v, p_58ec_v:p_4ea5_v, p_7678_v:p_5b50_v}
        __p_797f_5b58_5730_652f_v = p_797f_v[self.p_751f_5e74_v.p_5929_5e72_v]
        #火鈴
        #http://mm.httpcn.com/Html/News/2006-10-15/ILILPWCQ.shtml
        p_706b_v = {p_5b50_v:p_5bc5_v, p_4e11_v:p_536f_v, p_5bc5_v:p_4e11_v, p_536f_v:p_9149_v, p_8fb0_v:p_5bc5_v, p_5df3_v:p_536f_v, p_5348_v:p_4e11_v, p_672a_v:p_9149_v, p_7533_v:p_5bc5_v, p_9149_v:p_536f_v, p_620c_v:p_4e11_v, p_4ea5_v:p_9149_v}
        p_9234_v = {p_5b50_v:p_620c_v, p_4e11_v:p_620c_v, p_5bc5_v:p_536f_v, p_536f_v:p_620c_v, p_8fb0_v:p_620c_v, p_5df3_v:p_620c_v, p_5348_v:p_536f_v, p_672a_v:p_620c_v, p_7533_v:p_620c_v, p_9149_v:p_620c_v, p_620c_v:p_536f_v, p_4ea5_v:p_620c_v}
        self.__p_706b_661f_5730_652f_v = p_706b_v[self.p_751f_5e74_v.p_5730_652f_v]
        self.__p_9234_661f_5730_652f_v = p_9234_v[self.p_751f_5e74_v.p_5730_652f_v]

        for p_5bae_4f4d_v in self.p_5341_4e8c_5bae_4f4d_v:
           if p_5bae_4f4d_v.p_5730_652f_v == p_5b50_v: #火鈴
               self.__p_5b50_5bae_5bae_4f4d_v = p_5bae_4f4d_v
           if p_5bae_4f4d_v.p_5730_652f_v == p_8fb0_v:
               self.__p_8fb0_5bae_5bae_4f4d_v = p_5bae_4f4d_v
           if p_5bae_4f4d_v.p_5730_652f_v == p_620c_v:
               self.__p_620c_5bae_5bae_4f4d_v = p_5bae_4f4d_v
           if p_5bae_4f4d_v.p_5730_652f_v == p_4ea5_v:
               self.__p_4ea5_5bae_5bae_4f4d_v = p_5bae_4f4d_v 
           if p_5bae_4f4d_v.p_5730_652f_v == __p_797f_5b58_5730_652f_v:
               self.__p_797f_5b58_5bae_4f4d_v = p_5bae_4f4d_v

        # 索引從 0 開始 (已先減1)
        p_8fb0_5bae_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(self.__p_8fb0_5bae_5bae_4f4d_v)
        p_620c_5bae_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(self.__p_620c_5bae_5bae_4f4d_v)
        p_4ea5_5bae_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(self.__p_4ea5_5bae_5bae_4f4d_v)
        
        self.p_5341_4e8c_5bae_4f4d_v[p_8fb0_5bae_7d22_5f15_v-12+p_5730_652f_8868_v.index(self.p_751f_6642_v)].p_8f14_66dc_v.append(p_6587_66f2_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_620c_5bae_7d22_5f15_v-p_5730_652f_8868_v.index(self.p_751f_6642_v)].p_8f14_66dc_v.append(p_6587_660c_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_8fb0_5bae_7d22_5f15_v-12+self.p_751f_6708_v-1].p_8f14_66dc_v.append(p_5de6_8f14_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_620c_5bae_7d22_5f15_v-self.p_751f_6708_v+1].p_8f14_66dc_v.append(p_53f3_5f3c_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_4ea5_5bae_7d22_5f15_v-12+p_5730_652f_8868_v.index(self.p_751f_6642_v)].p_8f14_66dc_v.append(p_5730_52ab_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_4ea5_5bae_7d22_5f15_v-p_5730_652f_8868_v.index(self.p_751f_6642_v)].p_8f14_66dc_v.append(p_5730_7a7a_v)

        #魁鉞
        p_9b41_v = {p_7532_v:p_4e11_v, p_4e59_v:p_5b50_v, p_4e19_v:p_4ea5_v, p_4e01_v:p_4ea5_v, p_620a_v:p_4e11_v, p_5df1_v:p_5b50_v, p_5e9a_v:p_5348_v, p_8f9b_v:p_5348_v, p_58ec_v:p_536f_v, p_7678_v:p_536f_v}
        p_925e_v = {p_7532_v:p_672a_v, p_4e59_v:p_7533_v, p_4e19_v:p_9149_v, p_4e01_v:p_9149_v, p_620a_v:p_672a_v, p_5df1_v:p_7533_v, p_5e9a_v:p_5bc5_v, p_8f9b_v:p_5bc5_v, p_58ec_v:p_5df3_v, p_7678_v:p_5df3_v}
        for p_5bae_4f4d_v in self.p_5341_4e8c_5bae_4f4d_v:
            if p_5bae_4f4d_v.p_5730_652f_v == p_9b41_v[self.p_751f_5e74_v.p_5929_5e72_v]:
                p_5bae_4f4d_v.p_8f14_66dc_v.append(p_5929_9b41_v)
            if p_5bae_4f4d_v.p_5730_652f_v == p_925e_v[self.p_751f_5e74_v.p_5929_5e72_v]:
                p_5bae_4f4d_v.p_8f14_66dc_v.append(p_5929_925e_v)
        
        #羊陀
        self.__p_797f_5b58_5bae_4f4d_v.p_8f14_66dc_v.append(p_797f_5b58_v)
        p_797f_5b58_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(self.__p_797f_5b58_5bae_4f4d_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_797f_5b58_7d22_5f15_v -11].p_8f14_66dc_v.append(p_64ce_7f8a_v)
        self.p_5341_4e8c_5bae_4f4d_v[p_797f_5b58_7d22_5f15_v -1].p_8f14_66dc_v.append(p_9640_7f85_v)

        #火鈴
        p_5b50_5bae_7d22_5f15_v = self.p_5341_4e8c_5bae_4f4d_v.index(self.__p_5b50_5bae_5bae_4f4d_v) #火鈴
        # 陽年火順鈴逆
        p_706b_661f_8de8_8ddd_v = abs(p_5730_652f_8868_v.index(self.__p_706b_661f_5730_652f_v) - p_5730_652f_8868_v.index(self.p_751f_6642_v))
        p_9234_661f_8de8_8ddd_v = abs(p_5730_652f_8868_v.index(self.__p_9234_661f_5730_652f_v) - p_5730_652f_8868_v.index(self.p_751f_6642_v))
        if self.p_751f_5e74_v.p_9670_967d_v == p_967d_v:
            self.p_5341_4e8c_5bae_4f4d_v[p_5b50_5bae_7d22_5f15_v - 12 + p_706b_661f_8de8_8ddd_v + 2].p_8f14_66dc_v.append(p_706b_661f_v)
            self.p_5341_4e8c_5bae_4f4d_v[p_5b50_5bae_7d22_5f15_v - p_9234_661f_8de8_8ddd_v].p_8f14_66dc_v.append(p_9234_661f_v)
            #印出 子宮索引, 地支表.索引(我.__火星地支), 地支表.索引(我.生時), 我.十二宮位[子宮索引 - 火星跨距 - 1]
        else:
            self.p_5341_4e8c_5bae_4f4d_v[p_5b50_5bae_7d22_5f15_v - p_706b_661f_8de8_8ddd_v + 2].p_8f14_66dc_v.append(p_706b_661f_v)
            self.p_5341_4e8c_5bae_4f4d_v[p_5b50_5bae_7d22_5f15_v - 12 + p_9234_661f_8de8_8ddd_v + 2].p_8f14_66dc_v.append(p_9234_661f_v)
            #印出 子宮索引, 地支表.索引(我.__火星地支), 地支表.索引(我.生時), 我.十二宮位[子宮索引 - 火星跨距 - 1]

        #TODO: not finish yet

    def _p_5b89_5e74_7cfb_661f_v(self):
        #TODO: not finish yet
        pass

    def _p_5b89_6708_7cfb_661f_v(self):
        #TODO: not finish yet
        pass

    def _p_5b89_65e5_7cfb_661f_v(self):
        #TODO: not finish yet
        pass

    def p_5edf_65fa_5229_9677_v(self):
        """
        廟: 吉星逢之更吉, 兇星逢之不兇
        旺: 吉星逢之吉, 兇星逢之不兇
        得地(適度): 吉星逢之吉, 兇星逢之不兇
        利益(漸弱): 吉星逢之尚吉, 兇星逢之漸兇 
        平和(微):  吉星逢之力微, 兇星逢之加兇
        不得地(暗): 吉星逢之無力, 兇星逢之更兇  
        落陷(無光): 吉星逢之無用, 兇星逢之最兇 
        """
        #TODO: not finish yet
        pass

    def _p_53d6_5927_9650_v(self, p_5927_9650_v):
        """
        回傳大限範圍
        """
        return self.p_4e94_884c_5c40_v.p_5c40_6578_v+10*(p_5927_9650_v-1), self.p_4e94_884c_5c40_v.p_5c40_6578_v+10*p_5927_9650_v

    def p_5b9a_76e4_v(self):
        """紫微"""
        print self.p_59d3_540d_v
        print str(self.p_751f_5e74_v.p_9670_967d_v)+str(self.p_6027_5225_v), \
        str(self.p_4e94_884c_5c40_v)+str(self.p_4e94_884c_5c40_v.p_5c40_6578_v)+"局", \
            "生肖", str(self.p_751f_5e74_v.p_5730_652f_v.p_751f_8096_v)
    	print "定盤日期", str(self.p_751f_5e74_v)+"年 "+\
    	    str(self.p_751f_6708_v)+"月 "+str(self.p_751f_65e5_v)+"日 "+str(self.p_6642_8fb0_v)+"時"
    	import datetime
        # 年歲
        # if today.month <= 
        # if today.day <= 
        #print datetime.date.today().year - 1981 +1
    	# 現行大限  = _取大限(我.五行局.局數, )
    	print "命宮", str(self.p_547d_5bae_v), "身宮", str(self.p_8eab_5bae_v)
    	print "命主", str(self.p_547d_4e3b_v), "身主", str(self.p_8eab_4e3b_v), "\n"
    	
    	for p_5bae_4f4d_v in self.p_5341_4e8c_5bae_4f4d_v:
    	    print p_5bae_4f4d_v.p_5929_5e72_v, p_5bae_4f4d_v.p_5730_652f_v, p_5bae_4f4d_v
    	    if p_5bae_4f4d_v.p_6b63_66dc_v:
    	        for p_6b63_66dc_v in p_5bae_4f4d_v.p_6b63_66dc_v:
    	            print p_6b63_66dc_v
    	    if p_5bae_4f4d_v.p_8f14_66dc_v:
    	        for p_8f14_66dc_v in p_5bae_4f4d_v.p_8f14_66dc_v:
    	            print p_8f14_66dc_v

        #取 i 自 範圍(12):
        #    資料 = 字串(我.寅宮天干表[i]) + 字串(寅宮地支表[i]) + ' ' + 字串(我.十二宮位[i])
        #    印出 資料

    def p_5206_6790_v(self):
        pass
        #外貌
        #性格
        #格局

    def p_5b9a_6d41_5e74_76e4_v(self, p_5927_9650_v):
    	pass

    def __str__(self):
        #取 i in 我.十二宮位:
        #    print i
        return ''


if __name__=="__main__":
    # 代號 = 紫微斗數(姓名, 性別, 生年, 生月, 生日, 生時)
    #s = 紫微斗數("陳大文", 男, 丙午, 5, 6, 酉)
    #s.定盤()
    q = p_7d2b_5fae_6597_6578_v("如花", p_5973_v, p_8f9b_9149_v, 2, 24, p_5348_v)
    q.p_5b9a_76e4_v()

#    取 地支 自 地支表:
#        印出 地支, 地支.陰陽
#        印出 "對宮為", 取得對沖(地支)
#        印出 "三方為", 取得三合(地支)[0], 取得三合(地支)[1]
