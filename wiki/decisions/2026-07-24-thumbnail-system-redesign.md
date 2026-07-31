---
type: decision
date: 2026-07-24
status: accepted
team: youtube
seats: [mkbhd, hormozi, chris-do]
roles: [moderator]
review: [skeptical-reviewer, evidence-reviewer]
depth: standard
review_trigger: "90 Tage Doktrin-Freeze (bis ~2026-10-24): nur Daten ändern das System. Erste hellen Thumbnails per YouTube-A/B gegen dunkle Variante validieren; nach je 10 Videos Top-10% vs. Bottom-10%. Nordstern Workshop-Anfragen/Avatar-Fit, nicht Views. Feld-Farbe hat Ablaufdatum: kippt der deutsche KI-Feed auf hell, neu entscheiden."
project: "youtube-engine — Thumbnail-Erstellungsprozess (kanalweit, nicht videospezifisch)"
supersedes: "packaging-prinzipien.md §2 v1 (Ein-Schritt-KI-Generierung, Navy-Verlauf-Hintergrund, 2026-07-18/19)"
---

# YouTube Council: Thumbnail-System-Redesign (Komposition statt Generierung)

Anlass: Sebastian verwarf die KI-generierten Thumbnails grundsätzlich („grauenvoll": Logos
falsch/zu klein/missplatziert, Text langweilig, Bild langweilig, Posen sinnlos, leerer
Blick) und beauftragte eine Analyse viraler Thumbnails (Julian Ivanov, Hormozi, NateHerk,
TheFutur, MKBHD) plus Prozess-Neuentwurf. Empirische Basis: Top-12-Thumbnails aller 5
Kanäle visuell einzeln analysiert (60 Bilder) + 16 eigene (10 live, 6 neu) mit
Performance-Abgleich. Befunde: `youtube-engine/docs/research/data/thumbnail-analyse-2026-07/findings/`.
Synthese: `youtube-engine/docs/research/thumbnail-system-analyse.md`.

## Verdict (Moderator) — einstimmig nach Cross-Examination

**Komposition statt Ein-Schritt-Generierung.** Doktrin [AH]: „Ein echtes Foto, ein echter
Beweis, maximal vier Wörter, ein Versprechen." Grenz-Satz [CD]: System entscheidet einmalig
das WIE (Raster, Schrift, Farben, Crop, Highlight-Mechanik); jedes Video entscheidet neu das
WAS (das eine Beweis-Objekt, das eine Amber-Wort, der eine Ausdruck) — fehlen die drei
begründeten WAS-Entscheidungen, gilt das Thumbnail als abgelehnt.

1. **Feld hell** („keep the ink, flip the field" [CD]; MKBHD bestätigt mit
   Produktionsbedingung High-Key-Fotos; Hormozi bestätigt datenbasiert: keine bestehende
   Wiedererkennung zu verlieren, Julian = Kontrollgruppe, per A/B validieren, Feld-Farbe =
   Doktrin mit Ablaufdatum, nicht Identität).
2. **Gesicht nur noch echt** (Expression-Bibliothek: eine Session, High-Key-Licht
   eingefroren, Uniform, 8–12 Emotionen × 3 Winkel, gegen echte Botschaft gerichtet,
   320px-Test, ~3-monatlich nachschießen). KI-Gesicht = „Vertrauenssteuer" [MKBHD].
3. **Beweis nur echt** (Original-Logos, echte Screenshots aufs eine Detail beschnitten,
   Zahlen, Kunden-Reaktionen; „claim your proof, don't prove your claim — fix reality"
   [AH]; „fabricated proof ist die eine Todsünde einer Trust-Marke" [CD]).
4. **Signature = Typo-Stimme, kein Ornament** (Navy-Kicker + Headline mit hartem
   Weight-Sprung + EIN Amber-Wort + Punkt als Register [CD]; Hormozis Einspruch gegen
   geliehene Grafik-Signaturen übernommen; MKBHD: „Hormozis Doktrin als Gesetz, Chris' Grid
   als Verfassung, Element nur mit Job").
5. **Pipeline:** Konzept bei VIDEO-PLANUNG (nicht Post) [MKBHD+AH] → echte Assets →
   deterministische HTML-Komposition (KI nur Hintergrund-Textur, nie
   Gesicht/Logo/Text/Beweis) → binäres QA-Gate (120–320px, ein Hero-Read, Text≠Titel, ein
   Amber-Wort, Logo korrekt, Text fehlerfrei, Versprechen einlösbar, 3 WAS begründet) →
   3 Varianten 70-20-10 → YouTube-A/B.
6. **Messung:** CTR × Watchtime + Workshop-Anfragen als Nordstern (nicht Views — sonst
   Optimierung ans falsche Publikum [AH]); 90-Tage-Freeze; Top/Bottom-10%-Review je 10 Videos.
7. **Gast-Videos:** Headline = Gast-Zitat in Anführungszeichen nach Umkehr-Test („klickt
   es auch mit anonymem Experten?" [AH]); Gast-Name nur Kicker; Host groß/Gast klein [CD].

## Attribuierter Dissens / Auflösungen (preserved)

- **Feld hell vs. dunkel:** aufgelöst 3/3 hell, konditioniert (High-Key-Produktion; A/B;
  Ablaufdatum-Klausel).
- **Signature:** Hormozi gegen grafisches Erkennungszeichen („geliehener Anzug"), Chris
  konzediert Rule-Line, hält Typo-Stimme als Signatur; MKBHD schlichtet (Element nur mit
  Job). → Substanz = Echtheit, Handschrift = Typo-Lockup.
- **Gleichförmigkeits-Risiko [MKBHD]:** Template-Lock darf nicht Tapete werden → durch
  Chris' QA-Klausel operationalisiert (Beweis-Objekt = Variable, „jedes Mal neu verdient").
- **Hormozi-Vorbehalt (wichtig, offen):** Packaging ist Ticket of Entry — der 14x-Gap zu
  Julian kommt aus Themenwahl UND Packaging; nur Thumbnails zu optimieren poliert ggf.
  Themen, die keiner sucht. Themenwahl bleibt eigener Hebel (nicht Teil dieses Records).

## Konsequenzen (im Zielprojekt umgesetzt, gleiche Session)

- `docs/research/thumbnail-system-analyse.md` (Analyse + System, neu)
- `docs/research/data/thumbnail-analyse-2026-07/` (Rohdaten: 5×Top-12-TSVs, 76 Thumbnails,
  6 Findings-Dokumente)
- `docs/concepts/packaging-prinzipien.md` §2 komplett auf v2 umgestellt (v1-Learnings als
  §2.4 historisch dokumentiert)
- `.claude/skills/thumbnail/SKILL.md` auf Kompositions-Pipeline umgeschrieben
  (inkl. Übergangsmodus bis Foto-Bibliothek + Compose-Tool existieren)
- Offene Bausteine: Expression-Foto-Session (Blocker), `scripts/thumbnail-compose.mjs` +
  HTML-Templates, Drehplan-/Checklisten-Feld „Thumbnail-Bildidee", Furkan-Video-Thumbnail
  nach neuem System.

## Konfidenz

Hoch auf Prozess-Architektur (3/3 + deckungsgleich mit Selbst-Diagnose und eigener
Kanal-Performance-Evidenz). Mittel auf Feld-Farbe hell (fremde Evidenz stark, eigene steht
aus → A/B). Hub-candidate: ja (Prinzip „probabilistisches Tool nie deterministische
Entscheidungen besitzen lassen" + Kompositions-Pipeline sind projektübergreifend).
