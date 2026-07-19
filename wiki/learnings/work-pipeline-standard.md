---
type: learning
created: 2026-07-18
updated: 2026-07-18
scope: roster
---

# Standard-Pipeline (/work): erste echte Läufe

## Persona view

n/a — dies ist eine Orchestrierungs-Erfahrung, kein Persona-Thema.

## Own evidence

- [2026-07-18] Erster echter Cross-Project-/work-Lauf (youtube-engine: 5 Titelvarianten
  für das Infrastruktur-Video). Setup: standard-Pipeline, Team youtube, Seats Hormozi +
  Chris Do (per `--include`), Review skeptical + evidence. (n=1, source: roster log.md
  Eintrag 2026-07-18, Artefakt `youtube-engine/videos/wip/2026-07-11-…/titel-hypothesen.md`)
  - **Zwei aktive Seats konvergierten unabhängig** auf denselben Favoriten (Gap-Statement
    wortgleich zur Video-Hook) und dieselben Verwerfungen (Geld-Zahl, Tool-Bait) — die
    Konvergenz war das stärkste Entscheidungssignal des Laufs.
  - **Ein echter Dissens** (Kubernetes-Titel: Hormozi pro Damaging Admission, Chris Do
    contra Jargon-Filter) ließ sich über die Zielgruppen-Definition des Zielprojekts
    auflösen und wurde als Dissens im Artefakt dokumentiert.
  - **Die Funktions-Reviewer lieferten Substanz, die beide Personas übersahen:**
    Orthografie (Deppenleerzeichen), Mobile-Truncation an der Payoff-Stelle, fehlendes
    Test-Protokoll (Pseudo-Reversibilität beim Titel-Tausch), fehlende Mechaniken
    (Gast-Autorität, „Bevor du"). Der Evidence Reviewer fing zudem zwei Überdehnungen
    („häufigst belohnt" ≠ „stärkstes", Virality-Formel ist Mr. Beast via Hormozi).
  - Aufwand: 2 Advisor- + 2 Reviewer-Agents, gut parallelisierbar, Latenz je ~1,5–2 Min.
- [2026-07-18] Zweiter Lauf (gleiches Projekt, Thumbnail-Konzepte; n=2): Konvergenz-Muster
  bestätigt (beide Seats unabhängig: kein Gast im Bild, kein Foto-Board, ruhige Mimik) und
  ein PRODUKTIVER Dissens (Beweis-Zahl vs. Neugier-Vertiefung) wurde direkt als
  A/B-Test-Dimension übernommen statt aufgelöst — Dissens kann das Testdesign liefern.
  **Wichtigster Befund: Der Evidence Reviewer entdeckte durch Prüfung gegen den
  Drehbericht + extrahierte Video-Frames, dass ein bereits beschlossener TITEL (V3) vom
  realen Videomaterial widerlegt war** — der erste Titel-Lauf hatte nur gegen Plan-Dokumente
  geprüft (Briefing-Fehler des Orchestrators, nicht des Reviewers). (source: youtube-engine
  docs/log.md 2026-07-18, thumbnail-prompts.md)

## Effective rule

Für Kreativ-/Packaging-Entscheidungen (Titel, Thumbnails, Hooks) ist **standard** die
richtige Tiefe: 2 nicht-redundante Persona-Seats + beide Funktions-Reviewer. Die Reviewer
sind KEIN Formalismus — sie haben in n=2 wiederholt entscheidende Must-fixes geliefert
(bis hin zum Kippen einer bereits getroffenen Titel-Entscheidung). Council-Output nie
ungeprüft shippen. **Reviewer-Briefings müssen auf die IST-Artefakte zeigen (Drehbericht,
Take-Landkarte, finales Material), nie nur auf Plan-Dokumente** — Einlösbarkeits-Prüfungen
gegen den Plan sind wertlos, sobald Plan und Realität auseinanderlaufen.

## Open questions

- Skaliert die Konvergenz-Heuristik (Übereinstimmung zweier Seats = starkes Signal) auch
  bei 4+ Seats, oder entsteht dann Herdenbildung? Prüfen, sobald weitere Klone aktiv sind.
- Titel-Performance des Laufs messen (48h/7d/28d im Zielprojekt) — erst dann ist bewertbar,
  ob der Council-Output auch ERGEBNIS-Qualität hat, nicht nur Prozess-Qualität.
