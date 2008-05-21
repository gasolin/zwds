#!/usr/bin/python
# -*- coding: utf-8 -*-

from n_yingyang import *

def test_p_5929_5e72_v():
    assert p_4e01_v.p_9670_967d_v == p_9670_v
    assert p_58ec_v.p_9670_967d_v == p_967d_v

def test_p_5929_5e72_8868_v():
    assert p_5929_5e72_8868_v[5] == p_5df1_v
    assert p_5929_5e72_8868_v[9] == p_7678_v
    assert p_5929_5e72_8868_v[-2] == p_58ec_v

def test_p_5730_652f_v():
    assert p_672a_v.p_65b9_5411_v == p_5357_v
    assert p_4e11_v.p_9670_967d_v == p_9670_v
    assert p_7533_v.p_6642_9593_v == (15, 17)

def test_p_5730_652f_8868_v():
    assert p_5730_652f_8868_v[-3] == p_9149_v
    assert p_5730_652f_8868_v[6] == p_5348_v

def test_p_751f_8096_v():
    # 地支對應陰陽
    assert p_9f20_v.p_5730_652f_v.p_9670_967d_v == p_967d_v
    # 地支對應生肖
    assert p_8fb0_v.p_751f_8096_v == p_9f8d_v

def test_p_4e94_884c_751f_524b_v():
    assert p_706b_v.p_76f8_524b_v == p_91d1_v
    assert p_91d1_v.p_76f8_751f_v == p_6c34_v
    assert p_6c34_v.p_76f8_6d29_v == p_91d1_v
    assert p_6c34_v.p_76f8_4e58_v == p_706b_v
    assert p_571f_v.p_76f8_6094_v == p_6728_v

def test_p_4e94_884c_8207_65b9_5411_v():
    assert p_5317_v.p_4e94_884c_v == p_6c34_v
    assert p_6c34_v.p_65b9_5411_v == p_5317_v

def test_p_4e94_884c_8207_5929_5e72_v():
    assert p_571f_v.p_5929_5e72_v == (p_620a_v, p_5df1_v)
    assert p_5e9a_v.p_4e94_884c_v == p_91d1_v

def test_p_4e94_884c_8207_5730_652f_v():
    assert p_706b_v.p_5730_652f_v == (p_5df3_v, p_5348_v)
    assert p_5348_v.p_4e94_884c_v == p_706b_v
