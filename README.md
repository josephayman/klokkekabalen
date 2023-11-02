# klokkekabalen

Besvarelse til en oppgave fra MAT1120 Linear Algebra.

[Video forklaring](https://www.uio.no/studier/emner/matnat/math/MAT1120/h23/klokkeoppgave_vert.mp4)

### Oppgavetekst:

Skriv et program i Python eller Matlab som estimerer sannsynligheten for at klokkekabalen går opp, jamfør beskjed med lenke til video på semestersiden. Programmet skal spørre brukeren hvor mange ganger kabalen skal legges, og returnere (a) antall ganger kabalen gikk opp, (b) antall ganger den ikke gikk opp og brøken \(\mathrm{a} /(\mathrm{a}+\mathrm{b})\). Hvilket anslag for sannsynligheten får du ved å bruke programmet ditt? Lever programmet som en kjørbar kodefil (.m eller .py). Det er ikke nødvendig å legge ved kjøreeksempler.

### Algortime:

1. Hvis kortstokken er tom, kabalen har gått ned.
2. Hvis posisjonen allerede har riktig kort, hopp til neste ledige posisjon.
3. Ta et kort fra toppen av kortstokken og legg det på posisjonen.
4. Hvis kortet matcher posisjonen, lar vi det ligge. Hvis ikke, legger vi det i en kø for den posisjonen.
5. Hvis vi legger et kort på en bunke (kø) der kortet er på riktig plass, legger vi alle kortene unntatt det riktige kortet tilbake i kortstokken.
6. Hvis alle posisjoner er fylt, er kabalen gått opp. Hvis ikke, gå tilbake til steg 1.