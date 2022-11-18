import unittest
from string import Template
from random import choice

DEFAULT_ATACK = 5
DEFAULT_DEFENSE = 10
DEFAULT_SKILL = 15
DEFAULT_STAMINA = 80
WARIOR_NAME = 'Warrior - дерзкий воин ближнего боя. Сильный, выносливый и отважный.'
MAGE_NAME = 'Mage - находчивый воин дальнего боя. Обладает высоким интеллектом.'
HEALER_NAME = 'Healer - могущественный заклинатель. Черпает силы из природы, веры и духов.'

DEF_PHRASE = Template('$name блокировал $value ед. урона.')
ATACK_PHRASE = Template('$name нанёс противнику урон, равный $value.')
SPEC_PHRASE = Template('$name применил специальное умение $skill_name $value.')


NAMES = (
    'Egor', 'Bob', 'John', 'Jack', 'Silverhand', 'Cratos', 'Geralt', 'Ciri',
    'Patric', 'Dipper', 'Stan', 'Zus', 'Valera', 'Ezik', 'Gamlet', 'Igon',
    'Snow', 'Aria', 'Stiven', 'Peny', 'Sheldon', 'Ghost'
)

try:
    from main import Character
except ImportError:
    raise AssertionError('Отсутствует класс Character')

try:
    from main import Warrior
except ImportError:
    raise AssertionError('Отсутствует класс Warrior')

try:
    from main import Mage
except ImportError:
    raise AssertionError('Отсутствует класс Mage')

try:
    from main import Healer
except ImportError:
    raise AssertionError('Отсутствует класс Healer')


class TestPersons(unittest.TestCase):
    def test_subclass(self):
        assert issubclass(Warrior, Character), 'Warrior не является наследником Сharacter'
        assert issubclass(Mage, Character), 'Mage не является наследником Сharacter'
        assert issubclass(Healer, Character), 'Healer не является наследником Сharacter'

    def test_warrior_phrase(self):
        hero = Warrior(choice(NAMES))
        def_phrases = set(
            DEF_PHRASE.substitute(name=hero.name, value=DEFAULT_DEFENSE + i)
            for i in range(5, 11)
        )
        atack_phrases = set(
            ATACK_PHRASE.substitute(name=hero.name, value=DEFAULT_ATACK + i)
            for i in range(3, 6)
        )
        skill_phrase = SPEC_PHRASE.substitute(name=hero.name, value=DEFAULT_STAMINA + 25, skill_name='Выносливость')
        assert hero.__str__() == WARIOR_NAME
        for _ in range(100):
            atack_phrase = hero.attack()
            deph_phrase = hero.defence()
            spec_phrase = hero.special()
            assert atack_phrase in atack_phrases, f'{atack_phrase} не подходит к шаблону'
            assert deph_phrase in def_phrases, f'{deph_phrase} не подходит к шаблону'
            assert spec_phrase == skill_phrase, f'{spec_phrase} не подходит к шаблону'

    def test_healer_phrase(self):
        hero = Healer(choice(NAMES))
        def_phrases = set(
            DEF_PHRASE.substitute(name=hero.name, value=DEFAULT_DEFENSE + i)
            for i in range(2, 6)
        )
        atack_phrases = set(
            ATACK_PHRASE.substitute(name=hero.name, value=DEFAULT_ATACK + i)
            for i in range(-3, 0)
        )
        skill_phrase = SPEC_PHRASE.substitute(name=hero.name, value=DEFAULT_DEFENSE + 30, skill_name='Защита')
        assert hero.__str__() == HEALER_NAME
        for _ in range(100):
            atack_phrase = hero.attack()
            deph_phrase = hero.defence()
            spec_phrase = hero.special()
            assert atack_phrase in atack_phrases, f'{atack_phrase} не подходит к шаблону'
            assert deph_phrase in def_phrases, f'{deph_phrase} не подходит к шаблону'
            assert spec_phrase == skill_phrase, f'{spec_phrase} не подходит к шаблону {skill_phrase}'

    def test_mage_phrase(self):
        hero = Mage(choice(NAMES))
        def_phrases = set(
            DEF_PHRASE.substitute(name=hero.name, value=DEFAULT_DEFENSE + i)
            for i in range(-2, 3)
        )
        atack_phrases = set(
            ATACK_PHRASE.substitute(name=hero.name, value=DEFAULT_ATACK + i)
            for i in range(5, 11)
        )
        skill_phrase = SPEC_PHRASE.substitute(name=hero.name, value=DEFAULT_ATACK + 40, skill_name='Атака')
        assert hero.__str__() == MAGE_NAME, f'{hero.__str__()} != {MAGE_NAME}'
        for _ in range(100):
            atack_phrase = hero.attack()
            deph_phrase = hero.defence()
            spec_phrase = hero.special()
            assert atack_phrase in atack_phrases, f'{atack_phrase} не подходит к шаблону'
            assert deph_phrase in def_phrases, f'{deph_phrase} не подходит к шаблону'
            assert spec_phrase == skill_phrase, f'{spec_phrase} не подходит к шаблону'
