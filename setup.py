# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

executables = [
    Executable('askerlik.py') # dosyanızın ismi. Ben note.py yaptım.
]

setup(name='askerlik', # programın görünmesini istediğiniz ismi
      version='0.1', # sürüm
      description='note ayyildiz tim', # açıklama kısmı. Türkçe karakter kullanmamaya çalışın
      executables=executables
      )