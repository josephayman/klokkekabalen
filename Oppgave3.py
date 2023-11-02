import random


def klokkekabal_simulation():
   # Lager en kortstokk
    kortstokk = [i for i in range(1, 14)] * 4
    random.shuffle(kortstokk)

    klokke = [0] * 13
    queues = [[] for _ in range(13)]  # En kø for hvert av de 13 posisjonene

    while kortstokk:
        for position in range(13):
            # Hvis posisjonen allerede har riktig kort, hopp til neste ledige posisjon
            if klokke[position] == position + 1:
                continue

            # Sjekker om kortstokken er tom
            if not kortstokk:
                return "ned"
            
            kort = kortstokk.pop(0)

            # Sjekker om kortet matcher sin posisjon
            if kort == position + 1:
                klokke[position] = kort
                # Legg alle kort i køen (unntatt det riktige kortet) tilbake i kortstokken
                for q_kort in queues[position]:
                    if q_kort != kort:
                        kortstokk.append(q_kort)
                # Bare det riktige kortet forblir i køen
                queues[position] = [kort]
            else:
                queues[position].append(kort)

            # Sjekker om klokken er fylt opp med riktige kort
            if all(klokke):
                return "opp"

    return "ned"  # Kortstokken er tom før alle kort er plassert, kabalen går "ned"


def estimate_probability_from_input():
    # Lager en liste med n simuleringer
    n = int(input("Hvor mange ganger vil du at simuleringen skal kjøres? "))
    resultater = [klokkekabal_simulation() for i in range(n)]

    # Teller antall "opp" og "ned"
    opp = resultater.count("opp")
    ned = resultater.count("ned")

    # Regner ut sannsynligheten for at kabalen går "opp"
    sannsynlighet = opp / (opp + ned)

    return opp, ned, sannsynlighet


# Test the function with 1000 simulations
a, b, fraction = estimate_probability_from_input()
print(a, b, fraction)
