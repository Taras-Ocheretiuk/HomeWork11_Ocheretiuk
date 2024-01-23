import pytest
import HomeWork6_Ocheretiuk

def test_human_positive():
    man = HomeWork6_Ocheretiuk.Human()
    assert man.life() == "live life"

def test_builder_positive():
    worker = HomeWork6_Ocheretiuk.Builder()
    assert worker.builder() == "Build house"

def test_sailor_positive():
    captain = HomeWork6_Ocheretiuk.Sailor()
    assert captain.sailor() == "Go to sea"

def test_pilot_positive():
    ghost = HomeWork6_Ocheretiuk.Pilot()
    assert ghost.pilot() == "Aviate"

def test_passport_positive():
    tennis_player = HomeWork6_Ocheretiuk.Passport()
    assert tennis_player.identifies() == "Stas Stakhovsky lived in Ukraine"

def test_ForeignPassport_positive():
    travel_pasport = HomeWork6_Ocheretiuk.ForeignPassport()
    assert travel_pasport.travel() == "Stas Stakhovsky lived in Ukraine, number foreign passport UK112233 and has opened visa"

def test_animal_positive():
    animal_1 = HomeWork6_Ocheretiuk.Animal()
    assert animal_1.live() == "live and eat"

def test_tiger_positive():
    tiger_1 = HomeWork6_Ocheretiuk.Tiger()
    assert tiger_1.hunt() == "hunt to eat"

def test_crocodile_positive():
    crocodile_1 = HomeWork6_Ocheretiuk.Crocodile()
    assert crocodile_1.swim() == "swim to eat"

def test_kangaroo_positive():
    kangaroo_1 = HomeWork6_Ocheretiuk.Kangaroo()
    assert kangaroo_1.jump() == "jump to survive"