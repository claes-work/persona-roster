---
type: decision
date: 2026-07-21
status: accepted
team: executive
seats: [hormozi, chris-do]
review_trigger: Ergebnis des Pre-Order-/Founding-Tests (Three-Yeses-Kalibrierung); spätestens beim Agent-Launch (Max-Neubepreisung)
---

# 2Key Pricing & Conversion-Funnel: Preise halten, Wert sichtbar machen, Kasse an den Peak-Pain-Moment bauen

**Decision.** Preise werden NICHT gesenkt, obwohl der Agentenmodus fehlt — stattdessen: (1) das
Agent-Phantom sofort aus dem Max-Verkaufsversprechen nehmen, (2) die Kaufstrecke an den
Peak-Pain-Moment bauen (Ein-Klick-Upgrade + Top-up im „Kontingent aufgebraucht"-Popup), (3) einen
Gespart-Zeit-Zähler als Wert-Beweis in die App, (4) verbrauchsbasierte E-Mail-/In-App-Trigger als
Educate-Sequenz, (5) Jahresabo ausschließlich als verdientes Founding-Member-Angebot an aktive
Nutzer, mit 30-Tage-Geld-zurück-Garantie. Die 75 Gratis-Credits bleiben unbefristet (Dissens
Hormozi, s. u.). Confidence: high (Kernpunkte konvergent), medium bei Free-Tier-Urgency.

**Context.** Sebastians Frage (/council): Welche Preisformen + welcher End-to-End-Sales-Prozess
konvertieren Free-Nutzer in (Jahres-)Abos? Preise waren für den (noch nicht existenten)
Agentenmodus kalkuliert; heute nur Diktat/Textbearbeitung/Gespräch. Stand: Starter 75 Credits
einmalig/unbefristet · Pro 15 €/1.200 · Max 39 €/3.500+Agent-Capability · nur Monatsabos ·
Top-up-DB fertig, Kaufstrecke fehlt · E-Mail-Templates fertig, Trigger fehlen · Popup mit
ausgegrautem Kauf-Button. Bindende Vorbeschlüsse: Owner-Operator-Avatar, Founding-Member-Prepay
statt Rabatt, Pre-Order-Test, Marken-Gate, Nordstern „zahlende Nutzer + Churn".

**Reasoning.**
- **Keine Preissenkung (einstimmig).** Hormozi: „Value depends on price"; Preis steigt beim
  Agent-Launch, eingefrorener Launch-Preis ist die ehrliche Urgency; eigener 50-Mio-Fehler:
  Preissenkung bewegte Churn um null. Chris Do: Cost-plus rückwärts; Markus kauft 3–4 gesparte
  Std./Woche (8–13x Return bei 15 €); Premium-Versprechen (Datensouveränität) zum
  Discounter-Preis erzeugt Dissonanz.
- **Max verkauft ein Phantom (einstimmig).** 39 € für nicht existente Agent-Capability =
  Vaporware („promise nothing, deliver a ton" / „Abhebung vom bucket of trust"). Kurzfristig über
  Existierendes differenzieren (Kapazität/Priorität) oder als „Warteliste — kommt mit dem
  Agenten" rahmen; beim Agent-Launch als echter ~5x-Sprung (~75–99 €, Hypothese) neu bepreisen,
  Bestand/Founding eingefroren.
- **Kasse an den Peak-Pain-Moment (einstimmig, Prio 1 beider Seats).** Der ausgegraute
  „Credits kaufen"-Button am Moment maximaler Kaufbereitschaft ist eine abgesperrte Kasse
  (Hormozi: „never stop a flow until we create another flow"; Chris Do: „when somebody is ready
  to buy, shut up and get out of the way"). Höchster ROI pro Entwicklerstunde.
- **Gespart-Zeit-Zähler (einstimmig).** Wert in Output-Sprache statt Credits; „when they say it,
  you're closing" — der Nutzer sieht SEINE Zahl (gesparte Minuten) und verkauft sich selbst.
  Fundament aller Trigger/Mails.
- **Trigger-Architektur (konvergent).** 50 % Verbrauch = Wert-Bilanz (kein Verkauf) · 80–90 % =
  erstes Angebot („50 Cent am Tag") · 100 % = Ein-Klick binnen Minuten. E-Mail auslöserbasiert,
  nicht kalenderbasiert; 2:1 Wert-zu-Ask; Nicht-Aktivierte bekommen Hilfe- statt Upgrade-Mail
  (Activation Points instrumentieren: Hypothese erste Diktat-Session <10 Min., 3+ Tage in
  Woche 1); Ask mit accusation audit + Matchmaker-Downsell („bleib gratis, wenn's reicht");
  nach Kauf sofort raus aus jeder Verkaufssequenz.
- **Top-up als Decoy (konvergent).** Einzel-Credits bewusst teurer (~1,33–2x pro Credit vs.
  Abo) — existiert, damit Pro wie ein Geschenk aussieht; Hormozis Decoy-Kurve (1,33x → 50 %
  Continuity, 2x → 70 %).
- **Jahresabo (konvergent, baut auf Werbebudget-Beschluss auf).** Kein zweiter Preis auf der
  Pricing-Page, sondern verdientes Founding-Member-Angebot an aktive Pro-Nutzer in Monat 1–2
  (Take-Rate-Prior 30–40 %); Annual-Churn-Prior 2 % vs. 10,7 % monatlich (~5,35x LTV, US-Daten);
  echter Name (MAGIC, „Gründer-Jahrgang"-Richtung); 30 Tage bedingungslose Geld-zurück-Garantie
  (Downside bounded auf ~30 Tage API-Kosten); Bonuses statt Rabatt — Bonus-Credits als
  margensicherstes Material; Three-Yeses-Kalibrierung: >60–70 % Close → nächste Kohorte teurer.
- **Dreier-Struktur bleibt (Kompromiss aus Kreuzbefragung).** Hormozi konzediert drei Slots
  (eigenes Decoy-Prinzip), Chris Do konzediert Zahl am Top-Anker: Solange Max pausiert, drei
  Spalten Starter / Pro / Enterprise-MIT-Zahl („Anker ohne Zahl ankert nicht").

**Dissent.**
- **Credit-Verfall (ungelöst, dokumentiert):** Hormozi will Split ~25 Credits evergreen + ~50
  verfallen 14 Tage nach Signup — offen ausgewiesene Deadline sei legitime Urgency („the money
  is in the maybes"; Zähler ohne Datum hat keinen Entscheidungsmoment). Chris Do lehnt ab: ein
  Geschenk mit Rücknahmedatum ist ein „String", teuerste Abhebung vom Trust-Konto einer
  Datensouveränitäts-Marke; Urgency kommt aus Cost of Inaction + Founding-Knappheit +
  angekündigter Preiserhöhung. **Moderator-Entscheid: Chris-Do-Linie als Default**
  (markenkonsistent, Nordstern ist Churn/Vertrauen, ehrliche Urgency existiert bereits doppelt);
  Hormozis Split bleibt testbare Hypothese für ein A/B bei ausreichend Signup-Volumen.
- **Auto-Renewal-Default beim Top-up:** Hormozi dafür (disclosed Default), Chris Do dagegen
  (vorangekreuzt = email-trap-Mechanismus). Moderator: Chris Do gewinnt zusätzlich juristisch —
  vorangekreuzte Checkboxen für Nebenleistungen sind im EU-/DE-Verbraucherrecht unzulässig
  (Moderator-Anmerkung, kein Seat-Zitat). Aktive, klar beschriftete Wahl.

**Assumptions.** Avatar Owner-Operator hält (Pre-Order-Test steht aus) · typischer Verbrauch
20–50 % (Bonus-Credits-Ökonomie) · US-Priors (Churn, Take-Rates, Decoy-Kurve) übertragen sich
grob auf DE — testen · Diktat ist der Aha-Moment (<10 Min. erreichbar).

**Rejected alternatives.** Preissenkung wegen fehlendem Agenten (beide Seats: zerstört Anker,
Marke und Founding-Deal-Element) · Prozent-Rabatte auf Monatsabos (Churn-wirkungslos,
margenvernichtend) · Jahresabo als zweite Pricing-Page-Spalte · Max unverändert weiterverkaufen ·
genereller Credit-Verfall (nur als Hypothese am Leben).

**Risks / next experiment.** Risiko: Ohne Verfall fehlt dem Free-Tier ein Zeitanker — wenn
Free→Paid-Conversion nach Einbau von Zähler+Triggern <2–3 % bleibt, Hormozi-Split testen.
Billigster nächster Schritt: Kaufstrecke ins Popup + Verbrauchs-Trigger (Templates existieren)
shippen, dann Pre-Order-/Founding-Test (Beschluss 2026-07-20) mit den Schwellen ≥50/<20 fahren.
Rechts-Check (deutsches Verbraucherrecht: Auto-Renewal, Kündigungsbutton, Preisangaben) von
beiden Seats explizit als außerhalb ihrer Kompetenz markiert — separat klären.

**Affected.** `D:\Dev\2key-workforce\wiki\konversions-strategie.md` (neuer Plan-Artefakt) ·
`wiki/preise.md` (Verweis) · Website-Pricing-Page, Gateway/Stripe (Top-up-Kaufstrecke),
E-Mail-Trigger (email-system.md Kat. D), Desktop-Popup. Vorbeschlüsse:
[2026-07-20-2key-werbebudget-25k](2026-07-20-2key-werbebudget-25k.md),
[2026-07-20-2key-zielgruppe-owner-operator](2026-07-20-2key-zielgruppe-owner-operator.md).

## Seat-Quellen

- Hormozi: `alex-hormozi-clone/wiki/sources/2021-100m-offers.md`,
  `sources/2025-100m-pricing-playbook.md`, `sources/2025-100m-retention-playbook.md`,
  `sources/2025-100m-lead-nurture-playbook.md`, `topics/business/pricing-psychology.md`,
  `topics/business/money-model.md`, `topics/business/attraction-offers.md`,
  `topics/business/continuity-offers.md`, `persona/system-prompt.md`
- Chris Do: `chris-do-clone/wiki/topics/pricing/pricing.md` (§1, §5, §8, §10, §14),
  `topics/sales-clients/sales-clients.md` (§1, §4, §5, §10, §13),
  `topics/content-strategy/content-strategy.md` (§1, §3, §21, §29, §31),
  `persona/system-prompt.md`
