# Käyttäjätestauksen periaatteet

---

## Määritelmä

Käyttäjätestaus tarkoittaa prototyypin tai ratkaisun kokeilemista oikeilla käyttäjillä sen selvittämiseksi, toimiiko se, vastaako se tarpeeseen ja mitä pitää parantaa. Testaus on oppimista, ei idean puolustamista.

## Keskeiset asiat

- Testataan **käyttäjän kanssa**, ei käyttäjän puolesta.
- Tavoitteena on **oppia ja kehittää**, ei todistaa idean olevan oikea.
- Testaaminen tehdään **varhain ja usein**.
- **Havainnoidaan** käyttäytymistä enemmän kuin kysytään mielipidettä.
- Testaus voi johtaa paluuseen mihin tahansa aiempaan vaiheeseen.

## Periaatteet

1. **Määritä oppimistavoite:** mitä halutaan tietää?
2. **Valitse oikeat käyttäjät:** todelliset tai edustavat kohderyhmän jäsenet.
3. **Anna tehtäviä**, älä ohjeita: "Yritä varata aika" eikä "Paina tästä".
4. **Älä auta tai selitä** testin aikana. Havainnoi, missä testaaja takertuu.
5. **Pyydä ajattelemaan ääneen** (think aloud).
6. **Kirjaa tarkasti** huomiot, lainaukset ja ongelmakohdat.
7. **Pidä asenne avoimena:** kritiikki on arvokasta tietoa.
8. **Testaa useita versioita**, jos mahdollista.

## Testauksen vaiheet

1. Suunnittele: tavoite, tehtävät, käyttäjät, roolit
2. Valmistele prototyyppi ja ympäristö
3. Kerro testaajalle: testataan ratkaisua, ei häntä
4. Suorita testi ja havainnoi
5. Keskustele lopuksi (haastattelu)
6. Kirjaa ja analysoi tulokset

## Tiimin roolit

| Rooli | Tehtävä |
|---|---|
| **Fasilitaattori** | Ohjaa testiä ja esittää tehtävät |
| **Havainnoija/kirjaaja** | Tekee muistiinpanot |
| **Testaaja** | Käyttäjä, joka kokeilee |

## Käyttäjien määrä

Laadullisessa käytettävyystestauksessa jo noin **5 käyttäjää** löytää suurimman osan keskeisistä ongelmista (Nielsen). Parempi tehdä useita pieniä kierroksia kuin yksi suuri.

## Yleisiä virheitä

- Johdatellaan käyttäjää tai selitetään liikaa
- Testataan vain tiimin omia ystäviä
- Uskotaan sanottuun, vaikka teot kertovat muuta
- Reagoidaan puolustavasti

## Esimerkki

Kirjaston nuorten tilan pahvimalli: nuorille annetaan tehtävä "Etsi paikka, jossa voit pelata kavereiden kanssa". Havaitaan, että he kiertävät pelialueen, koska opaste puuttuu.

## Yhteenveto

Testaus tarkoittaa ratkaisun kokeilemista käyttäjillä oppimistavoitteen kanssa. Havainnointi kertoo enemmän kuin kysely.

## Lähteet

- Nielsen Norman Group: *Why You Only Need to Test with 5 Users*.
- Stanford d.school: *Test*, *Design Thinking Bootleg*.
