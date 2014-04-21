from ..models import Category


def create_categories():
    """Create some categories to test with.
    The tree looks like:
    Root
     | --- Weapons
     |        | --- Swords
     |
     | --- Armor
             | --- Plate
             | --- Mail
             | --- Cloth

    """
    c = Category.objects.create
    root = c(name='Root')

    wep = c(name='Weapons', parent=root)
    c(name='Swords', parent=wep)

    armor = c(name='Armor', parent=root)
    c(name='Plate', parent=armor)
    c(name='Mail', parent=armor)
    c(name='Cloth', parent=armor)


