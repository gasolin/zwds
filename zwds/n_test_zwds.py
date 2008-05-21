#!/usr/bin/python
# -*- coding: utf-8 -*-

from n_zwds import *

def test_p_661f_66dc_v():
    assert p_5730_7a7a_v.p_7a7a_52ab_v == True
    assert p_5730_7a7a_v.p_7a7a_66dc_v == True
    assert p_9640_7f85_v.p_5fcc_66dc_v == True
    assert p_9640_7f85_v.p_715e_66dc_v == True
    assert p_9640_7f85_v.p_5316_66dc_v == False

def test_p_751f_8fb0_v():
    # test basic value
    g = p_751f_8fb0_516b_5b57_v("陳大文", p_7537_v, p_4e19_5348_v, 5, 6, p_9149_v)
    assert g.p_59d3_540d_v == "陳大文" 
    assert g.p_6027_5225_v == p_7537_v
    assert g.p_5e72_652f_v == p_4e19_5348_v
    assert g.p_751f_5e74_v == p_4e19_5348_v
    assert g.p_751f_6708_v == 5
    assert g.p_751f_65e5_v == 6
    assert g.p_6642_8fb0_v == p_9149_v
    assert g.p_751f_6642_v == p_9149_v

def test_p_6597_6578_751f_8fb0_v():
    # test basic value
    g = p_7d2b_5fae_6597_6578_v("陳大文", p_7537_v, p_4e19_5348_v, 5, 6, p_9149_v)
    assert g.p_59d3_540d_v == "陳大文" 
    assert g.p_6027_5225_v == p_7537_v
    assert g.p_5e72_652f_v == p_4e19_5348_v
    assert g.p_751f_5e74_v == p_4e19_5348_v
    assert g.p_751f_6708_v == 5
    assert g.p_751f_65e5_v == 6
    assert g.p_6642_8fb0_v == p_9149_v
    
def test_p_5bae_4f4d_v():
    # test basic value
    g = p_7d2b_5fae_6597_6578_v("如花", p_5973_v, p_8f9b_9149_v, 2, 24, p_5348_v)
    assert g.p_547d_5bae_v == p_9149_v
    assert g.p_8eab_5bae_v == p_9149_v
    assert g.p_4e94_884c_5c40_v == p_706b_v

