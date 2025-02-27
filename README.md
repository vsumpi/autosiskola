# Magyarországi aktív autósiskolák térképe
1. Válaszd ki a jogosítvány kategóriát.
2. Zoomolj a térképen arra a területre, ahol keresel.
3. Az A, B és C kategóriák esetében a bal oldalon megjelennek az adott terület iskolái rangsorolva, a besorolás alapját az [Átlagos Képzési Óraszám és a forgalmi Vizsga Sikerességi Mutató](https://github.com/watchingdogs/autosiskola#a-statisztikák-és-a-rangsor-jelentése) képezik. A rangsorban mindig csak a képernyőn látható iskolák szerepelnek.
4. Egy-egy térképjelölőre kattintva meg lehet nézni az adott iskola legutóbbi két negyedéves statisztikáját, valamint egyéb elérhető infókat.

[<img src="https://github.com/user-attachments/assets/7ed9a22b-09a6-426c-9dae-efc5bbf167a4">](https://autosiskolaterkep.hu)

## Amire figyelni kell
- A rangsorbeli előny önmagában nem jelenti, hogy egy iskola objektíven jobb, **ez csak egy iránymutató eszköz**.
- Ez az oldal csak az igazán rossz iskolákat segít elkerülni, mindenki hallott már horror-sztorikat sokadik buktatásról és bunkó oktatókról.
- A térképen az iskolák irodája van megjelölve, nem a vezetés helyszíne vagy beszállási pontok. Ezek általában csak az iskolák weboldalán vannak fent.

## A statisztikák és a rangsor jelentése 
A rangsor pontszáma két statisztikát vesz alapul: az Átlagos Képzési Óraszámot (ÁKÓ) és a forgalmi Vizsga Sikerességi Mutatót (VSM). Ezeket a felugró ablakok is mutatják.

Az ÁKÓ azt mutatja meg, hogy a minimum teljesítendő gyakorlati (vezetési) órákhoz képest a tanulók ténylegesen hány többletórát vesznek a sikeres vizsgáig. B kategóriás jogosítványnál a minimum 29 óra jeleneti a 100%-ot, és így például 158% 46 gyakorlati órát jelent. Ez természetesen nem csak az iskolákat minősíti, hanem a vizsgázókat is. Elképzelhető, hogy egy iskolához csak kiemelkedően tehetséges vagy gyenge tanulók jelentkeztek egy adott időszakban.
A VSM-nak két típusa van, az elméleti és a gyakorlati. Az elméleti VSM nincs beleszámolva a rangsor pontszámába, mivel sok helyen E-Titánon keresztül lehet KRESZ tanfolyamot végezni, így nem lehet megkülönböztetni ezeket az eseteket a tantermi oktatást végző iskoláktól.

> [!IMPORTANT]
> **A rangsor pontszáma tehát az elméleti VSM és az ÁKÓ reciprokának az egyenlő súlyozású átlaga.**
> Ez csak a legutóbbi két negyedévet veszi figyelembe, tehát négy adatot átlagol. Minél több adat van, annál pontosabb képet ad az iskoláról a pontszáma.

A térképjelölőkön az OÁ az Országos Átlagot jelenti.

## Egyéb segítség a választásban
[KAV Tanácsai autósiskola választáshoz](https://vizsgakozpont.hu/tudastar/tanacsok-autosiskola-valasztashoz)

[Országos vizsgaútvonalak](https://www.kozlekedesihatosag.kormany.hu/hu/dokumentum/485371)

[Jogsikalkulator.hu iskolaválasztás](https://jogsikalkulator.hu/hu/iskolavalasztas.html)

## Az adatok forrása
A térképen jelölt iskolák és a statisztikájuk a [KAV nyilántartásából](https://vizsgakozpont.hu/ako_vsm) származnak. Ezekhez a címek és az engedélyezett kategóriák a [Közlekedési Hatóság Dokumentumtárjából](https://www.kozlekedesihatosag.kormany.hu/hu/dokumentum/466204) jönnek. Valamint, az E-Titán támogatása az [eduKRESZ partnerlistájából](https://edukresz.hu/edukresz-partnerek) tudható meg.

## Miért jött létre?
A nagyobb városokban nehéz magabiztosan iskolát választani. Mi ezt a problémát próbáljuk megoldani, és egyszerűbbé tenni ezt a folyamatot mindenki számára. Nem a mi feladatunk lenne, hogy ezt megoldjuk, hanem a KAV-é, mivel náluk van az összes adat. Emellett sajnos az eduKRESZ egyik weboldala sem ad átfogó képet a biztos választáshoz, ezért jött létre ez a projekt. 

Amennyiben a KAV nem tervez saját weboldalt létrehozni, már az alábbi változások is sokat számítanának:
- Nyílt REST API az előző évek összes adatáról, nem csak a legutóbbi kettő, és ne kelljen PDF-eket parsolni. Ez lehetővé tenné az iskolák hosszútávú értékelését, lehetne látni trendeket is.
- Egy mindent tartalmazó általános Képzési Költség (KK) publikálása, ami nem tér el adminisztrációs, kezelési, kiállítási díjakkal. Jelenleg ezt az iskolák csak a legeldugodtabb menük legalján mutatják be.
- Elméleti VSM felbontása E-Titános és tantermi oktatásra, vagy az E-Titán teljes kihagyása a statisztikákból, mivel az csak a tanuló teljesítményétől / motivációjától függ.
- Esetleg az ÁKÓ és a gyakorlati VSM lebontása külön oktatókra.

# Közreműködés
## Kell a segítség!
Még a jelenlegi állapotában is sok mindent lehetne tenni ezért a projectért. Mobilon jelenleg szinte használhatatlan a térképjelzők ugrálása miatt, de sok más egyebet is lehetne a UI-hoz tenni. Futtatásoknál a Google API használattal is lehetne spórolni. Valamint még tervben van a statisztikákból visszamenőleg egy trend grafikon is, mivel igazán a tartósan magas színvonal mutatja meg ha jó egy iskola. Ehhez a commitok közt ott vannak 2024 Q1-Q4 adatai, de talán 2023 Q4 is, de a maradék meg a hivatalos PDFekből kinyerhető. Szintén amire érdemes figyelni, hogy a képzőszervek listájából kiderül, hogy elméletet és vagy gyakorlatot oktat egy iskola, de ez nincs szétválasztva. Legfontosabb viszont talán egy keresőmező lenne az iskoláknak.

## Támogatás
A project nyílt forráskódú, és a weboldal is bárki számára elérhető. Nincsenek nagy költségeink, csak a domainek, a Google Geocoding API használata, meg majd a jövőben a szerver fenntartása. Amennyiben hozzájárulnál ezekhez, vagy csak támogatnál, [azt itt teheted](https://github.com/sponsors/watchingdogs).

## Hall of Fame

[@123a456b789c](https://github.com/watchingdogs/autosiskola/commits?author=123a456b789c) csinálta a weboldal nagyrészét. Az eredeti PoC után ő tette használhatóvá és élvezhetővé az egészet. Nélküle nem fejeződhetett volna be a project.

[@watchingdogs](https://github.com/watchingdogs/autosiskola/commits?author=watchingdogs) felelős az adatok feldolgozásáért és CI/CD-ért.
