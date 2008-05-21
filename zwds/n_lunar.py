#!/usr/bin/python
# -*- coding: utf-8 -*-

from core import *

"""
術數曆法 花甲
"""
class p_82b1_7532_v(object):
    """
    子丑, 寅卯, 辰巳 ... 類推
    """
    def __init__(self, p_540d_7a31_v, p_5929_5e72_v, p_5730_652f_v, p_4e94_884c_5c40_v):
        self.p_540d_7a31_v = p_540d_7a31_v
        self.p_4e94_884c_5c40_v = p_4e94_884c_5c40_v
        self.p_5929_5e72_v = p_5929_5e72_v
        self.p_5730_652f_v = p_5730_652f_v
        self.p_9670_967d_v = p_5929_5e72_v.p_9670_967d_v

    def __str__(self):
        return self.p_540d_7a31_v

p_7532_5b50_v = p_82b1_7532_v(p_540d_7a31_v = '甲子', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_5b50_v, p_4e94_884c_5c40_v = p_91d1_v)
p_4e59_4e11_v = p_82b1_7532_v(p_540d_7a31_v = '乙丑', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_4e11_v, p_4e94_884c_5c40_v = p_91d1_v)
p_4e19_5bc5_v = p_82b1_7532_v(p_540d_7a31_v = '丙寅', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_5bc5_v, p_4e94_884c_5c40_v = p_706b_v)
p_4e01_536f_v = p_82b1_7532_v(p_540d_7a31_v = '丁卯', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_536f_v, p_4e94_884c_5c40_v = p_706b_v)
p_620a_8fb0_v = p_82b1_7532_v(p_540d_7a31_v = '戊辰', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_8fb0_v, p_4e94_884c_5c40_v = p_6728_v)
p_5df1_5df3_v = p_82b1_7532_v(p_540d_7a31_v = '己巳', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_5df3_v, p_4e94_884c_5c40_v = p_6728_v)
p_5e9a_5348_v = p_82b1_7532_v(p_540d_7a31_v = '庚午', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_5348_v, p_4e94_884c_5c40_v = p_571f_v)
p_8f9b_672a_v = p_82b1_7532_v(p_540d_7a31_v = '辛未', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_672a_v, p_4e94_884c_5c40_v = p_571f_v)
p_58ec_7533_v = p_82b1_7532_v(p_540d_7a31_v = '壬申', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_7533_v, p_4e94_884c_5c40_v = p_91d1_v)
p_7678_9149_v = p_82b1_7532_v(p_540d_7a31_v = '癸酉', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_9149_v, p_4e94_884c_5c40_v = p_91d1_v)
p_7532_620c_v = p_82b1_7532_v(p_540d_7a31_v = '甲戌', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_620c_v, p_4e94_884c_5c40_v = p_706b_v)
p_4e59_4ea5_v = p_82b1_7532_v(p_540d_7a31_v = '乙亥', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_4ea5_v, p_4e94_884c_5c40_v = p_706b_v)

p_4e19_5b50_v = p_82b1_7532_v(p_540d_7a31_v = '丙子', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_5b50_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e01_4e11_v = p_82b1_7532_v(p_540d_7a31_v = '丁丑', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_4e11_v, p_4e94_884c_5c40_v = p_6c34_v)
p_620a_5bc5_v = p_82b1_7532_v(p_540d_7a31_v = '戊寅', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_5bc5_v, p_4e94_884c_5c40_v = p_571f_v)
p_5df1_536f_v = p_82b1_7532_v(p_540d_7a31_v = '己卯', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_536f_v, p_4e94_884c_5c40_v = p_571f_v)
p_5e9a_8fb0_v = p_82b1_7532_v(p_540d_7a31_v = '庚辰', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_8fb0_v, p_4e94_884c_5c40_v = p_91d1_v)
p_8f9b_5df3_v = p_82b1_7532_v(p_540d_7a31_v = '辛巳', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_5df3_v, p_4e94_884c_5c40_v = p_91d1_v)
p_58ec_5348_v = p_82b1_7532_v(p_540d_7a31_v = '壬午', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_5348_v, p_4e94_884c_5c40_v = p_6728_v)
p_7678_672a_v = p_82b1_7532_v(p_540d_7a31_v = '癸未', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_672a_v, p_4e94_884c_5c40_v = p_6728_v)
p_7532_7533_v = p_82b1_7532_v(p_540d_7a31_v = '甲申', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_7533_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e59_9149_v = p_82b1_7532_v(p_540d_7a31_v = '乙酉', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_9149_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e19_620c_v = p_82b1_7532_v(p_540d_7a31_v = '丙戌', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_620c_v, p_4e94_884c_5c40_v = p_571f_v)
p_4e01_4ea5_v = p_82b1_7532_v(p_540d_7a31_v = '丁亥', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_4ea5_v, p_4e94_884c_5c40_v = p_571f_v)

p_620a_5b50_v = p_82b1_7532_v(p_540d_7a31_v = '戊子', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_5b50_v, p_4e94_884c_5c40_v = p_706b_v)
p_5df1_4e11_v = p_82b1_7532_v(p_540d_7a31_v = '己丑', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_4e11_v, p_4e94_884c_5c40_v = p_706b_v)
p_5e9a_5bc5_v = p_82b1_7532_v(p_540d_7a31_v = '庚寅', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_5bc5_v, p_4e94_884c_5c40_v = p_6728_v)
p_8f9b_536f_v = p_82b1_7532_v(p_540d_7a31_v = '辛卯', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_536f_v, p_4e94_884c_5c40_v = p_6728_v)
p_58ec_8fb0_v = p_82b1_7532_v(p_540d_7a31_v = '壬辰', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_8fb0_v, p_4e94_884c_5c40_v = p_6c34_v)
p_7678_5df3_v = p_82b1_7532_v(p_540d_7a31_v = '癸巳', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_5df3_v, p_4e94_884c_5c40_v = p_6c34_v)
p_7532_5348_v = p_82b1_7532_v(p_540d_7a31_v = '甲午', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_5348_v, p_4e94_884c_5c40_v = p_91d1_v)
p_4e59_672a_v = p_82b1_7532_v(p_540d_7a31_v = '乙未', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_672a_v, p_4e94_884c_5c40_v = p_91d1_v)
p_4e19_7533_v = p_82b1_7532_v(p_540d_7a31_v = '丙申', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_7533_v, p_4e94_884c_5c40_v = p_706b_v)
p_4e01_9149_v = p_82b1_7532_v(p_540d_7a31_v = '丁酉', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_9149_v, p_4e94_884c_5c40_v = p_706b_v)
p_620a_620c_v = p_82b1_7532_v(p_540d_7a31_v = '戊戌', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_620c_v, p_4e94_884c_5c40_v = p_6728_v)
p_5df1_4ea5_v = p_82b1_7532_v(p_540d_7a31_v = '己亥', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_4ea5_v, p_4e94_884c_5c40_v = p_6728_v)

p_5e9a_5b50_v = p_82b1_7532_v(p_540d_7a31_v = '庚子', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_5b50_v, p_4e94_884c_5c40_v = p_571f_v)
p_8f9b_4e11_v = p_82b1_7532_v(p_540d_7a31_v = '辛丑', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_4e11_v, p_4e94_884c_5c40_v = p_571f_v)
p_58ec_5bc5_v = p_82b1_7532_v(p_540d_7a31_v = '壬寅', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_5bc5_v, p_4e94_884c_5c40_v = p_91d1_v)
p_7678_536f_v = p_82b1_7532_v(p_540d_7a31_v = '癸卯', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_536f_v, p_4e94_884c_5c40_v = p_91d1_v)
p_7532_8fb0_v = p_82b1_7532_v(p_540d_7a31_v = '甲辰', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_8fb0_v, p_4e94_884c_5c40_v = p_706b_v)
p_4e59_5df3_v = p_82b1_7532_v(p_540d_7a31_v = '乙巳', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_5df3_v, p_4e94_884c_5c40_v = p_706b_v)
p_4e19_5348_v = p_82b1_7532_v(p_540d_7a31_v = '丙午', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_5348_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e01_672a_v = p_82b1_7532_v(p_540d_7a31_v = '丁未', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_672a_v, p_4e94_884c_5c40_v = p_6c34_v)
p_620a_7533_v = p_82b1_7532_v(p_540d_7a31_v = '戊申', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_7533_v, p_4e94_884c_5c40_v = p_571f_v)
p_5df1_9149_v = p_82b1_7532_v(p_540d_7a31_v = '己酉', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_9149_v, p_4e94_884c_5c40_v = p_571f_v)
p_5e9a_620c_v = p_82b1_7532_v(p_540d_7a31_v = '庚戌', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_620c_v, p_4e94_884c_5c40_v = p_91d1_v)
p_8f9b_4ea5_v = p_82b1_7532_v(p_540d_7a31_v = '辛亥', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_4ea5_v, p_4e94_884c_5c40_v = p_91d1_v)

p_58ec_5b50_v = p_82b1_7532_v(p_540d_7a31_v = '壬子', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_5b50_v, p_4e94_884c_5c40_v = p_6728_v)
p_7678_4e11_v = p_82b1_7532_v(p_540d_7a31_v = '癸丑', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_4e11_v, p_4e94_884c_5c40_v = p_6728_v)
p_7532_5bc5_v = p_82b1_7532_v(p_540d_7a31_v = '甲寅', p_5929_5e72_v = p_7532_v, p_5730_652f_v = p_5bc5_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e59_536f_v = p_82b1_7532_v(p_540d_7a31_v = '乙卯', p_5929_5e72_v = p_4e59_v, p_5730_652f_v = p_536f_v, p_4e94_884c_5c40_v = p_6c34_v)
p_4e19_8fb0_v = p_82b1_7532_v(p_540d_7a31_v = '丙辰', p_5929_5e72_v = p_4e19_v, p_5730_652f_v = p_8fb0_v, p_4e94_884c_5c40_v = p_571f_v)
p_4e01_5df3_v = p_82b1_7532_v(p_540d_7a31_v = '丁巳', p_5929_5e72_v = p_4e01_v, p_5730_652f_v = p_5df3_v, p_4e94_884c_5c40_v = p_571f_v)
p_620a_5348_v = p_82b1_7532_v(p_540d_7a31_v = '戊午', p_5929_5e72_v = p_620a_v, p_5730_652f_v = p_5348_v, p_4e94_884c_5c40_v = p_706b_v)
p_5df1_672a_v = p_82b1_7532_v(p_540d_7a31_v = '己未', p_5929_5e72_v = p_5df1_v, p_5730_652f_v = p_672a_v, p_4e94_884c_5c40_v = p_706b_v)
p_5e9a_7533_v = p_82b1_7532_v(p_540d_7a31_v = '庚申', p_5929_5e72_v = p_5e9a_v, p_5730_652f_v = p_7533_v, p_4e94_884c_5c40_v = p_6728_v)
p_8f9b_9149_v = p_82b1_7532_v(p_540d_7a31_v = '辛酉', p_5929_5e72_v = p_8f9b_v, p_5730_652f_v = p_9149_v, p_4e94_884c_5c40_v = p_6728_v)
p_58ec_620c_v = p_82b1_7532_v(p_540d_7a31_v = '壬戌', p_5929_5e72_v = p_58ec_v, p_5730_652f_v = p_620c_v, p_4e94_884c_5c40_v = p_6c34_v)
p_7678_4ea5_v = p_82b1_7532_v(p_540d_7a31_v = '癸亥', p_5929_5e72_v = p_7678_v, p_5730_652f_v = p_4ea5_v, p_4e94_884c_5c40_v = p_6c34_v)

p_82b1_7532_8868_v = (p_7532_5b50_v, p_4e59_4e11_v, p_4e19_5bc5_v, p_4e01_536f_v, p_620a_8fb0_v, p_5df1_5df3_v, p_5e9a_5348_v, p_8f9b_672a_v, p_58ec_7533_v, p_7678_9149_v, p_7532_620c_v, p_4e59_4ea5_v,
p_4e19_5b50_v, p_4e01_4e11_v, p_620a_5bc5_v, p_5df1_536f_v, p_5e9a_8fb0_v, p_8f9b_5df3_v, p_58ec_5348_v, p_7678_672a_v, p_7532_7533_v, p_4e59_9149_v, p_4e19_620c_v, p_4e01_4ea5_v,
p_620a_5b50_v, p_5df1_4e11_v, p_5e9a_5bc5_v, p_8f9b_536f_v, p_58ec_8fb0_v, p_7678_5df3_v, p_7532_5348_v, p_4e59_672a_v, p_4e19_7533_v, p_4e01_9149_v, p_620a_620c_v, p_5df1_4ea5_v,
p_5e9a_5b50_v, p_8f9b_4e11_v, p_58ec_5bc5_v, p_7678_536f_v, p_7532_8fb0_v, p_4e59_5df3_v, p_4e19_5348_v, p_4e01_672a_v, p_620a_7533_v, p_5df1_9149_v, p_5e9a_620c_v, p_8f9b_4ea5_v,
p_58ec_5b50_v, p_7678_4e11_v, p_7532_5bc5_v, p_4e59_536f_v, p_4e19_8fb0_v, p_4e01_5df3_v, p_620a_5348_v, p_5df1_672a_v, p_5e9a_7533_v, p_8f9b_9149_v, p_58ec_620c_v, p_7678_4ea5_v
)

# not being used yet
class p_7bc0_6c23_v(object):
    """
    http://www.componentcn.com/show_new.asp?id=397
    """
    def __init__(self, p_540d_7a31_v):
        self.p_540d_7a31_v = p_540d_7a31_v

    def __str__(self):
        return self.p_540d_7a31_v

p_5c0f_5bd2_v = p_7bc0_6c23_v("小寒")
p_5927_5bd2_v = p_7bc0_6c23_v("大寒")
p_7acb_6625_v = p_7bc0_6c23_v("立春")
p_96e8_6c34_v = p_7bc0_6c23_v("雨水")
p_9a5a_87c4_v = p_7bc0_6c23_v("驚蟄")
p_6625_5206_v = p_7bc0_6c23_v("春分")
p_6e05_660e_v = p_7bc0_6c23_v("清明")
p_7a40_96e8_v = p_7bc0_6c23_v("穀雨")
p_7acb_590f_v = p_7bc0_6c23_v("立夏")
p_5c0f_6eff_v = p_7bc0_6c23_v("小滿")
p_8292_7a2e_v = p_7bc0_6c23_v("芒種")
p_590f_81f3_v = p_7bc0_6c23_v("夏至")
p_5c0f_6691_v = p_7bc0_6c23_v("小暑")
p_5927_6691_v = p_7bc0_6c23_v("大暑")
p_7acb_79cb_v = p_7bc0_6c23_v("立秋")
p_8655_6691_v = p_7bc0_6c23_v("處暑")
p_767d_9732_v = p_7bc0_6c23_v("白露")
p_79cb_5206_v = p_7bc0_6c23_v("秋分")
p_5bd2_9732_v = p_7bc0_6c23_v("寒露")
p_971c_964d_v = p_7bc0_6c23_v("霜降")
p_7acb_51ac_v = p_7bc0_6c23_v("立冬")
p_5c0f_96ea_v = p_7bc0_6c23_v("小雪")
p_5927_96ea_v = p_7bc0_6c23_v("大雪")
p_51ac_81f3_v = p_7bc0_6c23_v("冬至")

p_7bc0_6c23_8868_v = (p_5c0f_5bd2_v, p_5927_5bd2_v, p_7acb_6625_v, p_96e8_6c34_v,
        p_9a5a_87c4_v, p_6625_5206_v, p_6e05_660e_v, p_7a40_96e8_v,
        p_7acb_590f_v, p_5c0f_6eff_v, p_8292_7a2e_v, p_590f_81f3_v,
        p_5c0f_6691_v, p_5927_6691_v, p_7acb_79cb_v, p_8655_6691_v,
        p_767d_9732_v, p_79cb_5206_v, p_5bd2_9732_v, p_971c_964d_v,
        p_7acb_51ac_v, p_5c0f_96ea_v, p_5927_96ea_v, p_51ac_81f3_v)

class p_8fb2_66c6_v(object):
    """
    use pyzh calendar
    http://www.hsip.cn/article/12/2005/200512162906.html
    http://www.evget.com/zh-CN/article/1694/default.aspx
    http://www.evget.com/zh-CN/article/1695/default.aspx
    """
    def __init__(self):
        from lunarcalendar import LunarCalendar
        self._p_8fb2_66c6_v = LunarCalendar()

    def p_897f_5143_751f_8fb0_v(self, p_751f_5e74_v, p_751f_6708_v, p_751f_65e5_v, p_751f_6642_v):
        self.p_751f_5e74_v = p_751f_5e74_v
        self.p_751f_6708_v = p_751f_6708_v
        self.p_751f_65e5_v = p_751f_65e5_v
        self.p_751f_6642_v = p_751f_6642_v
        self.p_8fb2_66c6_751f_5e74_v, self.p_8fb2_66c6_751f_6708_v, self.p_8fb2_66c6_751f_65e5_v, self.p_958f_6708_v = self._p_8fb2_66c6_v.getLunarDate(self.p_751f_5e74_v, self.p_751f_6708_v, self.p_751f_65e5_v)
        self.p_8fb2_66c6_751f_8fb0_v = self.__p_8fb2_66c6_751f_8fb0_v()

    def __p_8fb2_66c6_751f_8fb0_v(self):
        """干支, 月, 日, 時, 閏"""
        p_65e9_5b50_6642_v = False
        if self.p_751f_6642_v < 1:
           p_6642_8fb0_v = p_5b50_v
           p_65e9_5b50_6642_v = True
        elif self.p_751f_6642_v < 3:
           p_6642_8fb0_v = p_4e11_v
        elif self.p_751f_6642_v < 5:
           p_6642_8fb0_v = p_5bc5_v
        elif self.p_751f_6642_v < 7:
           p_6642_8fb0_v = p_536f_v
        elif self.p_751f_6642_v < 9:
           p_6642_8fb0_v = p_8fb0_v
        elif self.p_751f_6642_v < 11:
           p_6642_8fb0_v = p_5df3_v
        elif self.p_751f_6642_v < 13:
           p_6642_8fb0_v = p_5348_v
        elif self.p_751f_6642_v < 15:
           p_6642_8fb0_v = p_672a_v
        elif self.p_751f_6642_v < 17:
           p_6642_8fb0_v = p_7533_v
        elif self.p_751f_6642_v < 19:
           p_6642_8fb0_v = p_9149_v
        elif self.p_751f_6642_v < 21:
           p_6642_8fb0_v = p_620c_v
        else:
           p_6642_8fb0_v = p_4ea5_v
        return p_6642_8fb0_v, p_65e9_5b50_6642_v
