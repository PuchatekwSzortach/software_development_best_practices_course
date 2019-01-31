import basic
import advanced


if __name__ == "__main__":

    person = basic.Person("Tom", 27)
    warrior = advanced.Warrior("Goku", age=20, strength=9000)

    print(person)
    print(warrior)
    print(warrior.kick())
