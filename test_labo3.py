from random import random
from labo3 import *

# Q1
def test_multiples3():
    assert multiples3(100) == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# Q2
def test_arrondi():
    n = 46.6
    assert arrondi(n) == 47
    assert arrondi(46.5) == 47
    assert arrondi(46.4) == 46

# Q3
def test_racines():
    assert racines(1, 0, -1) == (1.0, -1.0)
    assert racines(1, 2, 1) == (-1.0,)
    assert racines(1, 0, 1) == ()

# Q4
def test_rayon_polygone():
    assert round(rayon_polygone(3, 10), 3) == 5.774
    assert round(rayon_polygone(4, 10), 3) == 7.071 
    assert round(rayon_polygone(5, 10), 3) == 8.507
    assert round(rayon_polygone(6, 10), 3) == 10.0
    assert round(rayon_polygone(7, 10), 3) == 11.524
    assert round(rayon_polygone(8, 10), 3) == 13.066

# Q5
def test_rayon_cercle():
    assert round(rayon_cercle(3, 10), 3) == 11.439
    assert round(rayon_cercle(4, 10), 3) == 15.252
    assert round(rayon_cercle(5, 10), 3) == 19.065
    assert round(rayon_cercle(6, 10), 3) == 22.878
    assert round(rayon_cercle(7, 10), 3) == 26.691
    assert round(rayon_cercle(8, 10), 3) == 30.504

# Q6
def test_aire_cercle():
    assert round(aire_cercle(5), 3) == 78.540

# Q7
def test_xor():
    assert not xor(True, True)
    assert xor(True, False)
    assert xor(False, True)
    assert not xor(False, False)

# Q8
def test_entre_100_500():
    assert not entre_100_500(99)
    assert not entre_100_500(100)
    assert entre_100_500(200)
    assert not entre_100_500(500)
    assert not entre_100_500(501)

# Q9
def test_est_multiple():
    assert est_multiple(2, 2)
    assert est_multiple(4, 2)
    assert not est_multiple(2,4)

# Q10
def test_somme100():
    assert somme100() == 9900

# Q11
def test_sommeneg100():
    assert sommeneg100() == -4950

# Q12
def test_premiers():
    assert premiers(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Q13
def test_pluspetit():
    assert pluspetit([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 2
    assert pluspetit([2, 3, 5, 7, 11, 13, 17, 19, 23, .29, 31, 37, 41]) == .29
    assert pluspetit([2, 3, 5, 7, 11, 13, 17, 19, 23, .29, 31, 37, -41]) == -41

# Q14
def test_est_palindrome():
    assert est_palindrome("a")
    assert est_palindrome("aa")
    assert est_palindrome("aba")
    assert est_palindrome("abba")
    assert not est_palindrome("abc")

# Q15
def test_triangle():
    assert triangle((0,0), (0,1), (1,0)) == {"équilatéral": False, "isocèle": True, "rectangle": True, "scalène": False }
    assert triangle((0,0), (0,1), (2,0)) == {"équilatéral": False, "isocèle": False, "rectangle": True, "scalène": False }
    assert triangle((0,0), (1,2), (2,0)) == {"équilatéral": False, "isocèle": True, "rectangle": False, "scalène": False }
    assert triangle((0,0), (1,2), (3,0)) == {"équilatéral": False, "isocèle": False, "rectangle": False, "scalène": True }
    assert triangle((0,0), (1.5, sqrt(9-1.5**2)), (3,0)) == {"équilatéral": True, "isocèle": True, "rectangle": False, "scalène": False }