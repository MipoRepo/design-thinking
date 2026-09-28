# Palautteen kerääminen ja analysointi

**Prosessin vaihe:** 05 Testaa
**Liittyy:** [[Käyttäjätestauksen periaatteet]], [[Iterointi]], [[Tiedon synteesi ja analyysi]]

---

## Määritelmä

Palautteen kerääminen tarkoittaa käyttäjien reaktioiden, havaintojen ja mielipiteiden kirjaamista testin aikana ja sen jälkeen. Analyysi jäsentää palautteen opituiksi asioiksi ja parannuskohteiksi.

## Keskeiset asiat

- Kerätään sekä **havaintoja** (mitä käyttäjä teki) että **mielipiteitä** (mitä hän sanoi).
- Palaute on **dataa**, ei henkilökohtainen arvio suunnittelijasta.
- Analyysin tuloksena tiedetään, **mitä säilytetään, muutetaan tai hylätään**.

## Palautteen keruu

### Menetelmiä

| Menetelmä | Kuvaus |
|---|---|
| **Havainnointi** | Katsotaan, missä käyttäjä onnistuu ja epäröi |
| **Ääneen ajattelu** | Käyttäjä kertoo ajatuksensa tehtävän aikana |
| **Loppuhaastattelu** | Syvennetään havaintoja ("Miksi teit näin?") |
| **Lyhyt kysely** | Nopea arvio kokemuksesta |
| **Tallenne** | Video, kuvat, näyttökaappaukset (luvalla) |

### Haastattelukysymyksiä

- Mikä toimi hyvin? Mikä oli hankalaa?
- Mitä odotit tapahtuvan?
- Mikä yllätti?
- Mitä muuttaisit?

## Palautteen jäsentäminen

### Feedback Capture Grid

| Kenttä | Sisältö |
|---|---|
| **I like** (+) | Mikä toimi ja miellytti |
| **I wish** (Δ) | Toiveet ja parannusehdotukset |
| **What if** (?) | Uudet ideat ja kysymykset |
| **Kysymykset ja havainnot** | Avoimet asiat, joita kannattaa tutkia |

### Kirjaaminen

- Kirjaa **suora lainaus** ja **havainto** erikseen.
- Kirjaa **testaaja, tehtävä ja tilanne**.
- Merkitse ongelman **vakavuus** (kriittinen, merkittävä, pieni).

## Analyysi

1. **Kokoa** palaute yhteen kaikilta testaajilta.
2. **Ryhmittele** teemoihin (affiniteettikaavio).
3. **Etsi toistuvat ongelmat**, jotka useampi käyttäjä kohtasi.
4. **Priorisoi** vakavuuden ja korjauksen vaivan mukaan.
5. **Tulkitse:** miksi ongelma syntyi?
6. **Päätä:** säilytä, muuta, hylkää vai testaa uudelleen.

### Palautteeseen suhtautuminen

- Kuuntele, älä puolusta.
- Erota **tarve** ja **ehdotettu ratkaisu**: käyttäjän ehdotus ei aina ole paras ratkaisu, mutta sen takana oleva tarve on arvokas.
- Yksittäinen mielipide ei ole kuvio, toistuva havainto on.

## Yleisiä virheitä

- Kerätään vain kehuja
- Tulkitaan palautetta oman idean vahvistukseksi
- Ei kirjata syitä
- Jätetään analyysi tekemättä

## Yhteenveto omin sanoin

Palaute kerätään havainnoimalla ja haastattelemalla, kirjataan jäsennellysti ja analysoidaan kuvioiden löytämiseksi. Sen perusteella päätetään jatkosta.

## Avoimet kysymykset

-

## Lähteet

- Stanford d.school: *Feedback Capture Grid*, *I Like, I Wish, What If*.
- IDEO.org: *The Field Guide to Human-Centered Design*.
