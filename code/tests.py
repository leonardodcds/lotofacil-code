from mods import gerar_valores_aleatoriamente
from mods import gerar_resultado_aleatoriamente
from calc import *


def test_gerar_valores_aleatoriamente():
    assert gerar_valores_aleatoriamente() != 0


def test_gerar_resultado_aleatoriamente():
    assert gerar_resultado_aleatoriamente() != 0


def test_somar():
    assert somar(4, 2) == 6


def test_subtrair():
    assert subtrair(4, 2) == 2


def test_multiplicar():
    assert multiplicar(4, 2) == 8


def test_dividir():
    assert dividir(4, 2) == 2