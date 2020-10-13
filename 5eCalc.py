#!/usr/bin/python3
#To whoever is reading this, I'm so sorry. It's been a bit since I've coded so here comes the CS101 sort of shit
#This is a calculator for 5th Edition DnD regarding summoned creatures because they eat up all of the combat time.
#Written by Alex Knoll 10/8/2020

import random #for the dice rolls
import sys #for the command line arguments

#This is a slower general 
def main():

    MM = {
        "coins": {
            "attackerCount": 10,
            "attackModifier": 4,
            "damageModifier": 4,
            "diceQuantity": 1,
            "diceType": 4
        },
        "ape": {
            "attackerCount": 8,
            "attackModifier": 5,
            "damageModifier": 3,
            "diceQuantity": 1,
            "diceType": 6
        },
        "warhorse": {
            "attackerCount": 4,
            "attackModifier": 6,
            "damageModifier": 4,
            "diceQuantity": 2,
            "diceType": 6
        },
        "rhinoceros": {
            "attackerCount": 1,
            "attackModifier": 7,
            "damageModifier": 5,
            "diceQuantity": 2,
            "diceType": 8
        }
    }
    if (len(sys.argv) >= 2):
        if (sys.argv[1] in MM):
            creature = MM[sys.argv[1]]
        else:
            print("Couldn't find that one. Manual that shit.")
            creature = manualEntry()
    else:
        creature = manualEntry()

    if (len(sys.argv) >= 3):
        print("Manual override:", sys.argv[2], "attackers.")
        creature["attackerCount"] = int(sys.argv[2])

    #enter the information from whatever input source
    attackerCount = creature["attackerCount"]
    attackModifier = creature["attackModifier"]
    damageModifier = creature["damageModifier"]
    diceQuantity = creature["diceQuantity"]
    diceType = creature["diceType"]

    AC = int(input("Target AC: "))
    print ("-----Rolling to hit-----")
    #declare the arrays for each attack
    rolls = [0] * attackerCount #raw dice rolls
    attacks = [0] * attackerCount #with modifiers
    hits = [False] * attackerCount #hit status
    damage = [damageModifier] * attackerCount #damage
    damageTotal = 0
    critTotal = 0

        #Calculation
    for i in range(attackerCount):
        print("----Attack", i, "-----")
        rolls[i] = random.randint(1,20)
        attacks[i] = rolls[i] + attackModifier
        if (rolls[i] == 20): #Crit
            print("Rolled a Nat 20!")
            print("That's a CRIT!") 
            hits[i] = True
            damage[i] += (damageCalc(diceQuantity, diceType) * 2)
            damageTotal += damage[i]
            critTotal += 1
            print("Crit:", damage[i], "damage!")
        elif (attacks[i] >= AC): #Hit
            print("Rolled a", attacks[i])
            hits[i] = True
            damage[i] += damageCalc(diceQuantity, diceType)
            damageTotal += damage[i]
            print("Hit:", damage[i], "damage")
        else: #Miss
            print("Rolled a ", rolls[i], " plus ", attackModifier, " for a ", attacks[i])
            print("Miss: 0 damage")
            damage[i] = 0
        print("\n")

    #Summary
    hitTotal = sum(hits)
    print("----Summary----")
    print(hitTotal, "out of", attackerCount, "hit.")
    print("There were", critTotal, "crits.")
    print("Damage total:", damageTotal)
    #print("dice rolls:", rolls)
    #print("attacks:", attacks)
    #print("hits", hits)
    #print("damage:", damage)
    return damageTotal



def manualEntry():
    attackerCount = int(input("Number of attackers: "))
    attackModifier = int(input("Attack Modifier: "))
    damageModifier = int(input("Damage Modifier: "))
    diceQuantity = int(input("Number of Dice per Hit: "))
    diceType = int(input("Type of Dice: d"))
    creature = {
    "attackerCount": attackerCount,
    "attackModifier": attackModifier,
    "damageModifier": damageModifier,
    "diceQuantity": diceQuantity,
    "diceType": diceType
    }
    return creature


def damageCalc(diceQuantity, diceType): #I figured it was neater to do the damage dice in a separate function
    damage = 0
    for i in range(diceQuantity):
        damage += random.randint(1,diceType)
    return damage

main()