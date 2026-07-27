---
type: decision
date: 2026-07-26
status: accepted
team: youtube
seats: [mkbhd, hormozi, chris-do, skeptical-reviewer, evidence-reviewer]
review_trigger: nach 3 veröffentlichten Folgen (Frame-Mix + Enemy-A/B + Architektur-Aufwand gegen die Kanal-Benchmark auswerten)
supersedes: none
extends: 2026-07-26-workshop-serie-intro-format
---

# Workshop-Serie Intro: Gast-Typen (Frames) + modulare Vorproduktions-Architektur

**Decision.** Erweitert Runde 1. (1) **Eine Position, drei Castings** (Unternehmer / „der Aufbauende" /
Professional), verankert auf dem **Aufbauenden/Starter** als Show-Identität; Job-Status = Demografie,
die Position = Psychografie (verliert Zeit an Aufgaben, die KI könnte, weiß nicht wo anfangen). Kein
Lügen über Status. (2) **Geweiteter, frame-agnostischer Spine:** „Ein echter Mensch mit einem echten
Problem baut an einem Tag ein KI-System, das am Ende wirklich läuft." (3) **Feind raus aus dem Spine**
(eigene Evidenz: Warn-Frames underperformen), nur optionaler, leicht formulierter Per-Folge-Beat im
10%-Test-Slot. (4) **Modulare Architektur:** EIN eingefrorenes Gerüst (`head`+`tail` als Caches) +
Batch-injizierte Alpha-Overlays (Name + Rollen-Zeile) + Layer-2-Footage (Reveal im Mittelfenster) +
Musik als Assembly-Stem; HyperFrames-Projekt+Batch-Config = kanonisch, Renders = ableitbare Caches.
(5) **VO:** 1 evergreen Spine-Read + 3 kurze Casting-Zeilen-Reads, Name NIE gesprochen (Layer-1-Text).
(6) **Adam = Folge 1 = Starter**, Ziel in Business-Wert (€/Stunden) denominiert, möglichst Geld-das-floss
am Ende. Confidence: **high** (Struktur/Architektur), **medium** (Klick-/Käufer-Wirkung, eigene Evidenz fehlt).

**Context.** Nicht jeder Gast ist Unternehmer (Adam will ein Business *aufbauen*). Sebastian lügt nicht.
Sein realer Post-Production-Engpass ist die Animations-/Titelarbeit (nicht Multicam); er will maximal
vorproduzieren (Vorbild: sein vorab eingesprochener Hostinger-Block) und pro Folge nur Variablen (Name,
eine Zeile, Bild) einspeisen, ohne Animationen neu zu bauen. Tool = HyperFrames (`--batch` JSON-Variablen,
Alpha-Overlay-Export). Eigene Evidenz geladen: Anfänger-Verheißung am stärksten belohnt (DE-KI-Markt);
Warn-/Feind-Frames underperformen auf eigenem + Julian-Ivanov-Kanal; Curiosity-Gap relativ stark, Video
trotzdem schwächstes der 10; Nordstern = Workshop-Anfragen, nicht Views.

**Reasoning.**
- **Eine Position, drei Castings [CD]:** Positionierung = eine Stelle im Kopf besetzen (Framework 18/32);
  drei gleichrangige Frames = kein Flag. Status ist Demografie, positioniert wird auf Psychografie
  (Framework 6). Held = Want+Obstacle, nicht ein verdienter Titel → der Starter ist der *sichtbarere*
  Held (Transformation schließt sich auf Kamera).
- **Aufbauender als Anker [AH]:** breitester Wert-zu-Kosten-Spread in Identifikations-Währung; Anfänger =
  größtes, am stärksten belohntes Segment. „All growth is constrained by irrelevance" → nicht drei halbe
  Versprechen.
- **Feind raus aus dem Spine [alle, CD konzediert]:** eigene Evidenz > Persona-Doktrin. Feind wird
  implizit-durch-Kontrast („echt…echt…wirklich läuft"), explizit nur im 10%-Slot (70-20-10), an RPM/Fit
  gemessen [AH: „your promise is not a differentiator, your proof is"].
- **Architektur [MKBHD]:** frozen *Render*, nicht frozen *Source*. `head`/`tail` als getrennte Caches +
  Reveal im Mittelfenster + Musik-Stem = variable Reveal-Länge und Quartals-Upgrade ohne Hand-Rebuild.
  Drei Gast-Typen = eine VO-Variable, nicht drei Builds.
- **Starter-Stakes [AH]:** trackbares Ja/Nein-Ziel Minute eins, in €/Stunden denominiert; Payoff =
  laufendes Artefakt + echte Reaktion, idealerweise Geld-das-floss; „sell the goal, not the program".

**Dissent.** Wieder durch Konzession aufgelöst; ein Gradient bleibt offen:
- **Chris Do zog den Feind aus dem Spine** (räumt ein: eigene Evidenz schlägt seine Villain-Doktrin;
  Flag überlebt implizit).
- **VO-Variant-Zahl (mild offen):** MKBHD = 3 tonale Casting-Reads (erfüllt Sebastians „3 fertige Intros"-
  Gefühl); Hormozi hält die tonale Differenz für gering und würde langfristig **eine** Stimme + wachsende
  Call-out-**Zeilen-Bibliothek** fahren. Beide kompatibel (Reads = austauschbare Audio-Variablen); als
  Gradient dokumentiert, nicht erzwungen.
- **Episode-1-Payoff-Höhe (mild offen):** Hormozi = „Geld, das floss" (echter zahlender Kunde am Tag);
  Chris = Geld ODER zurückgewonnene Stunden (P&L-denominiert). Synthese: Geld-das-floss als Gold-Standard,
  Fallback = verkaufsfertiges Angebot + zeit/geld-denominiertes Artefakt.

**Assumptions.** (1) HyperFrames `--batch` + Alpha-Overlay tragen das Layer-Modell zuverlässig. (2) Ein
Starter kann an einem Tag ein €/Stunden-denominiertes Ergebnis (idealerweise echten Umsatz) ehrlich
zeigen. (3) Der geweitete Spine bleibt spezifisch genug (vier konkrete Anker) statt matschig.

**Rejected alternatives.** Drei monolithische Intros (drei driftende Timelines); Feind im Dauer-Spine
(Warn-Frame-Evidenz); Namen im VO (killt „für immer gebankt"); Status-Inflation (Angestellter als
„Unternehmer" — Werte-Test); Ein-Monolith-Master (bricht bei variabler Reveal-Länge + Upgrade);
Ziel als „cooles Ding das läuft" statt Business-Wert (trainiert Hobby-Publikum).

**Risks / next experiment.**
- **Hobby-Drift:** Aufbauenden-Anker zieht Hobbybastler über den Käufer-Avatar → jede Folge muss auf
  Business-Ergebnis landen; Adam (Folge 1) ist der Test, Ziel in €/Stunden denominieren.
- **Enemy-A/B:** eine Folge mit leicht formuliertem Feind-Beat vs. no-enemy-Cut; Retention erste 30 s +
  Benchmark ablesen.
- **Architektur-Aufwand:** einmaliger Shell/VO/Template-Bau amortisiert sich erst über mehrere Folgen;
  billigster Test = für Adam bauen, Post-Production-Zeit vs. Pierre messen.

**Affected.** `youtube-engine/docs/concepts/workshop-serie-intro-format.md` (§0b, §5b, §6 staged-reveal,
§11 Architektur; Spine in §0 revidiert), `docs/log.md`. Folge-Arbeit: Generator-Skill + HyperFrames-Shell
(Hand-off /work oder /plan).
