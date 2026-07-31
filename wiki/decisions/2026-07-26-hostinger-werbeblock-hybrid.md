---
type: decision
date: 2026-07-26
status: accepted
team: growth
seats: [hormozi, chris-do, neil-patel]
roles: [moderator]
depth: standard
review_trigger: "Nach Phase 1 des Kohorten-Tests (~30 Videos / 1 Monat): Delta Block-Dip vs. Video-Baseline pro Arm auswerten; Gewinner in Phase 2 gegen On-Camera-Hook. Ergebnis in youtube-engine/docs/concepts/sponsor-hostinger.md zurückspielen."
project: "youtube-engine — wiederkehrender Hostinger-Werbeblock (Evergreen vs. personalisierter Einstieg)"
---

# Growth Council: Hostinger-Werbeblock — fix, personalisiert oder hybrid?

Anlass: Sebastians Evergreen-Werbeblock (Browser-Animation + VO) ist fast fertig. Frage:
Lohnt der wiederkehrende Aufwand eines video-spezifischen, per Teleprompter aufgenommenen
Einstiegs — oder ist ein zu 100 % fixer Block besser? Ökonomischer Rahmen (Sebastian):
Integrations-Gebühr (~2.500 €/Video) ⋙ Affiliate-Provisionen; Primärziel = Deal-Verlängerung
bei minimalem Produktionsaufwand; perspektivisch tägliche Videos.

## Verdict (Moderator)

**Hybrid mit VO-Default.** Der Block bleibt zu ~95 % fixer Evergreen-Kern (Animation + einmal
eingesprochene Stimme, KEIN Gesicht in der Konserve). Variabel ist genau EIN Brückensatz,
Default als **Voice-over über den ersten Sekunden der Animation**, eingesprochen in derselben
Session wie das Video (Grenzkosten < 5 Min, kein Teleprompter-Zwang, kein Kleidungsproblem).
Die von Sebastian gefürchtete Form der Personalisierung (On-Camera-Teleprompter-Take + eigener
Renderschritt pro Video) ist damit vom Tisch; die billige Form ist einstimmig empfohlen.
3/3-Konvergenz nach Cross-Examination; der einzige Fork (On-Camera vs. VO) wurde durch
Hormozis Konzession aufgelöst und lebt als Testarm weiter.

## Agreements (alle Sitze)

1. **Fixen Kern einfrieren** („Meat + CTA", Hormozi-Assembly-Line): Animation, VO, Anker
   KVM 1 → Empfehlung KVM 2 → Checkout/Code. Nie video-spezifisch anfassen.
2. **Ein variabler Brückensatz, Default VO.** Job: Kontext/Andocken an die Lektion des Videos
   („Ihr habt gerade gesehen, dass der Agent einen Server braucht …"). Hook-Swipe-File mit
   10–15 evergreen-wahren Varianten (70-20-10), video-spezifisch nur, wenn das Video den
   Server-Bedarf wirklich zeigt. **Rote Linie (Chris Do):** kein Konserven-Hook darf
   Video-Spezifik vortäuschen; diagnostischer Ton, keine Hook-Marketer-Energie.
3. **Gesicht raus aus dem fixen Block** (einstimmig): Konserven-Gesicht in fremder Kleidung
   liest sich als Konserve und lässt den Block altern. Wenn Gesicht, dann nur im variablen
   Hook in Tageskleidung — als Testarm, nicht als Pflicht.
4. **Disclosure + Exklusivität wandern IN den fixen Block** (erster gesprochener Satz:
   „Dieses Video hat einen Sponsor — genau einen: Hostinger, weil das bei uns selbst läuft.").
   Macht den Block selbsttragend (an schwachen Tagen solo shipbar = Volume-Floor) und den
   variablen Satz zum reinen Hook ohne Pflichtbaustein.
5. **Kapitelmarke „Sponsor" ab Tag 1, uniform über alle Testarme.** Ehrenhaft überspringbar;
   „freiwillige Watch-Through trotz Ein-Klick-Skip" ist das STÄRKERE Sponsor-Argument
   (Neil: ehrliche Zahl verkauft besser; Hormozi: claim your proof).
6. **Messen statt meinen — sequenziell paarweise (Neil):** Phase 1 (~30 Videos, interleaved):
   fix vs. VO-Brücke. Phase 2: Gewinner vs. On-Camera-Hook. Primärmetrik: **Delta zwischen
   Block-Dip und video-eigener Baseline direkt vor dem Block** (normalisiert Themen-Rauschen);
   Codes/Klicks pro 1.000 Views nur sekundär (Ökonomie hängt am Sponsor, nicht an Provision —
   Chris' Korrektur, von Neil akzeptiert).
7. **Refresh des fixen Kerns: Kurve triggert, Kalender sichert.** Wöchentlich Block-Retention
   ansehen; wächst der Dip über 2–3 Videos → refresh, sonst 6–8-Wochen-Backstop. Variante 2
   aus den Daten von Variante 1 ableiten (Kaleidoskop), kein Refresh aus Langeweile.
8. **Sponsor-Report als eigentlicher Verlängerungs-Hebel:** qualifizierte Watch-Through-Rate
   (trotz Skip-Möglichkeit) + Frequenz/kumulierte Block-Impressions als Asset + Kommentare;
   Code-Einlösungen als Bonuszeile. Renewal-Gespräch proaktiv VOR Deal-Ende terminieren.
   **Whitelisting** des Gewinner-Blocks als zweite Stufe NACH organischem Beweis anbieten,
   bepreist, Paid-/Organik-Zahlen strikt getrennt (Neil: „sponsor only organically-proven
   content").

## Dissent → durch Konzession aufgelöst (bemerkenswert sauber)

- **Hormozi zog On-Camera als Default zurück** (Chris' Kosten-Argument akzeptiert), behält
  aber seine Naht-These — Skip-Cue-Verzögerung: Frame 1 = Animation heißt für Stammzuschauer
  „Ad beginnt", Frame 1 = gleiches Set + gleiche Kleidung verzögert den Skip-Reflex um die
  entscheidenden Sekunden — als **Phase-2-Testarm** („let the data do the teaching").
- **Chris Do akzeptierte On-Camera unter Bedingungen:** Die kritische Naht ist
  Hook→Animation, gelöst durch **Audio-Brücke** (Hook-Satz läuft als Ton über die ersten
  Animations-Sekunden). Fallback-Regel: VO nachsprechen statt nachdrehen; **der Sponsor-Block
  darf nie der Grund sein, warum ein Video nicht rausgeht.**
- **Neil korrigierte seine eigene Primärmetrik** (Codes → Retention-Delta) nach Chris'
  Einwand, dass Codes auf das Ziel mit dem kleineren Scheck optimieren.

## Beiträge pro Sitz

- **Hormozi:** Ad-Assembly-Line-Frame (Hooks rotieren, Meat/CTA settled); Banner-Blindness
  bei täglicher Frequenz; Disclosure-in-den-Kern für den Volume-Floor; Whitelisting;
  Renewal als Sales-Prozess.
- **Chris Do:** Selbstkorrektur „klingt wie der Rest = Ton, nicht Frische"; deklarierter
  Rahmen ist die EHRLICHERE Form („ein fester Rahmen ist kein Vertrauensbruch, ein
  versteckter ist einer"); VO-Default; Kapitelmarke; Naht-Craft; Refresh-Kadenz.
- **Neil Patel:** ROI-Rechnung (Personalisierungs-Prämie < 2 % bei richtigem Batching);
  Fatigue skaliert mit Frequenz (Kumulation, nicht Einzelvideo); sequenzielles Zwei-Phasen-
  Testdesign mit normalisierter Metrik; Report-Framing „engaged exposure statt erzwungener
  Impressionen".

## Gaps

- Keiner der Sitze hat harte YouTube-Benchmarks zu Sponsor-Segment-Skip-Raten (beide
  Daten-Aussagen extrapolieren aus Paid-Ads-Fatigue) → deshalb Kohorten-Test statt Behauptung.
- Deutsche Werbekennzeichnungs-Pflichten: außerhalb aller Wikis, separat prüfen (YouTube-Flag
  „bezahlte Promotion" bleibt Pflicht-Minimum).

## Affected

`youtube-engine/docs/concepts/sponsor-hostinger.md` (Hybrid-Modell + Skript-Anpassung:
Disclosure in den fixen Teil, Hook-Swipe-File, Kapitelmarke, Test-/Refresh-/Report-Plan),
`youtube-engine/docs/log.md`.
