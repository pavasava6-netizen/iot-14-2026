"""Лабораторна робота №5, варіант 20.
Класи: AtomType (enum), Atom, Molecule.
"""
from enum import Enum


class AtomType(Enum):
    ISOTYPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4
    STABLE = 5


class Atom:
    def __init__(self, name, atomic_mass, neutrons, protons, electrons,
                 atom_type=AtomType.STABLE):
        self._name = name
        self._atomic_mass = atomic_mass  # а.о.м. (atomic mass unit)
        self._neutrons = neutrons
        self._protons = protons
        self._electrons = electrons
        self._type = atom_type

    def __del__(self):
        print(f"Атом {self._name} видалено")

    # --- функції доступу ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def atomic_mass(self):
        return self._atomic_mass

    @atomic_mass.setter
    def atomic_mass(self, value):
        self._atomic_mass = value

    @property
    def neutrons(self):
        return self._neutrons

    @neutrons.setter
    def neutrons(self, value):
        self._neutrons = value

    @property
    def protons(self):
        return self._protons

    @protons.setter
    def protons(self, value):
        self._protons = value

    @property
    def electrons(self):
        return self._electrons

    @electrons.setter
    def electrons(self, value):
        self._electrons = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    # --- методи ---
    def is_neutral(self):
        """Атом нейтральний, якщо кількість протонів дорівнює кількості електронів."""
        return self._neutrons == self._electrons

    def show(self):
        print(f"Атом {self._name}: маса = {self._atomic_mass} а.о.м., "
              f"нейтронів = {self._neutrons}, протонів = {self._protons}, "
              f"електронів = {self._electrons}, тип = {self._type.name}, "
              f"нейтральний = {self.is_neutral()}")

    def __str__(self):
        return f"{self._name} ({self._atomic_mass})"


class Molecule:
    def __init__(self, name, atoms=None):
        self._name = name
        self._atoms = list(atoms) if atoms else []

    def __del__(self):
        print(f"Молекулу {self._name} видалено")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def atoms(self):
        return self._atoms

    def add_atom(self, atom):
        if not isinstance(atom, Atom):
            raise TypeError("Only Atom objects can be added")
        self._atoms.append(atom)

    def remove_atom(self, atom):
        if atom in self._atoms:
            self._atoms.remove(atom)
        else:
            print("Такого атома в молекулі немає")

    def sort_by_mass(self, reverse=False):
        """Сортування атомів за масою."""
        self._atoms.sort(key=lambda a: a.atomic_mass, reverse=reverse)

    @staticmethod
    def find_average_mass(atoms):
        """Середня маса атомів серед заданих."""
        if not atoms:
            return 0
        return sum(a.atomic_mass for a in atoms) / len(atoms)

    def show(self):
        print(f"Молекула {self._name}, атомів: {len(self._atoms)}")
        for atom in self._atoms:
            atom.show()


def main():
    h1 = Atom("Hydrogen", 1.008, 0, 1, 1, AtomType.STABLE)
    h2 = Atom("Hydrogen", 1.008, 0, 1, 1, AtomType.STABLE)
    o = Atom("Oxygen", 15.999, 8, 8, 8, AtomType.STABLE)
    c14 = Atom("Carbon-14", 14.003, 8, 6, 6, AtomType.RADIOACTIVE)
    na = Atom("Sodium ion", 22.990, 12, 11, 10, AtomType.ION)

    print("=== Атоми ===")
    for a in (h1, o, c14, na):
        a.show()

    water = Molecule("Water", [o, h1, h2])
    print("\n=== Молекула до сортування ===")
    water.show()

    water.sort_by_mass()
    print("\n=== Після сортування за масою (за зростанням) ===")
    water.show()

    print("\nСередня маса атомів у воді:",
          round(Molecule.find_average_mass(water.atoms), 3))

    print("\n=== Додавання / видалення ===")
    water.add_atom(c14)
    print("Після додавання C-14 атомів:", len(water.atoms))
    water.remove_atom(c14)
    print("Після видалення C-14 атомів:", len(water.atoms))

    print("\n=== Доступ через властивості ===")
    na.electrons = 11
    print("Після зміни кількості електронів Na нейтральний:", na.is_neutral())


if __name__ == "__main__":
    main()
