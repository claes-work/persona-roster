---
type: decision
date: 2026-08-01
team: executive
seats: [heartbeat, hormozi, agency-scaler, neil-patel, mkbhd, chris-do]
roles: [moderator, skeptical-reviewer]
review: [evidence-reviewer, skeptical-reviewer]
depth: deep
tags: [finance-dashboard, kpis, controlling, product, external-user]
status: decided
---

# Council: Finanz-Dashboard-KPIs für GF/Controller (KI-Buchhaltungs-App, Lexware-API)

**Frage:** Ein Gründer baut eine KI-Web-App (Rechnungen aus E-Mails → Buchhaltung, Positions-/
Steuerkategorie-Zuweisung) + ein Dashboard aus Lexware-Ist-Daten. Was sind die wichtigsten
Dashboard-Ansichten/KPIs für einen Geschäftsführer bzw. Controller? (Bereits gedacht:
Cashflow, Einnahmen, Ausgaben pro Monat/Jahr.)

## Verdikt (Moderator)

**Einstimmig:** Cashflow/Umsatz/Ausgaben ist die **Buchhalter-/Rückspiegel-Sicht** (was war).
Ein GF-Dashboard muss die **Treiber** zeigen und jede Kachel muss eine **Entscheidung**
auslösen („so what do I DO?"). Umsatz ist Vanity — **Gewinn/Marge, Unit Economics, der
Vertriebs-Funnel und Cash-Runway** sind die Steuergrößen. Struktur: **Vogelperspektive
(5–6 Verdikt-Kacheln) → Trends → Drill-down**, zwei Default-Sichten (CEO vs. Controller),
jede Zahl **mit Kontext** (vs. Vormonat / vs. Vorjahr / vs. Ziel + Richtung), Ampel-Logik,
und das Ding treibt **Action** (Alerts + Review-Ritual), kein passives Starren.

## Konsens-KPIs (nach Gruppen)

**1) Echtes Geld & Überleben**
- **Gross Profit + Marge %** statt Umsatz (Netto-Marge ≤ Brutto-Marge) — Hormozi, Chris Do, Heartbeat.
- **Net Profit + Profit-Level 1/2/3** (Profit 1 = operative Leitzahl, groß oben); Gründergehalt ist **Kosten, nicht Profit** — Heartbeat, Chris Do.
- **Operativer Cashflow bereinigt** (minus USt, minus durchlaufende Posten) — NICHT die nackte Kontozahl — agency-scaler, Heartbeat.
- **Runway in Monaten + „Worry Date"** (als Datum, nicht Balken; ≥3 Monate; Steuerkonto separat) — Chris Do, agency-scaler, alle.
- **True Free Cash = verfügbar − geschuldete Steuern** (Killer-Feature, weil die App Steuerkategorien kennt) — Chris Do.
- **Offene/überfällige Forderungen als ACTION-Liste** (nicht tote Zahl) — agency-scaler, mkbhd.

**2) Unit Economics (rentiert die Maschine?)**
- **CAC** (voll: Ads + Marketing-Payroll + Sales-Provision, über 12 Monate) — alle.
- **LTV:CAC / LTGP:CAC / DB-LTV:CAC** (>3:1 SaaS … 9–12:1 bei viel Personal; relevant ist **DB-LTV zu CAC**, nicht Front-End) — Hormozi, Heartbeat, Neil.
- **30-Tage-Cash / Payback-Period** (Gross Profit in 30 Tagen ≥ COGS + CAC) — Hormozi.
- **Marketing-Spend % vom Umsatz + Blended-ROAS/ROI** (Front-End vs. Gesamt getrennt; CPB <500€, CPO) — Neil, agency-scaler.
- **Umsatz nach Kanal + Attribution** — Neil.

**3) Die Maschine (warum der Umsatz so ist)**
- **Sales-Funnel als Wertschöpfungskette:** Termine → Show-up (>80%) → Offer (~80%) → Offer-Close **und** Call-Close (getrennt) → Cash Collected / Upfront — **pro Closer/Setter**, nicht Team-Schnitt — agency-scaler, Heartbeat.
- **Umsatz pro Mitarbeiter (FTE, >20–25k)** — agency-scaler.
- **OpEx-Split % + 3 Buckets** (Customer Acquisition / Fulfillment / Overhead) mit **DB-Korridoren nach Umsatzstufe** (0–50k → 50–70%; 100–500k → 30–50%; >1 Mio → 30–40%); Fulfillment-Kostenquote = zentrale Stellgröße — Heartbeat, agency-scaler.

**4) Retention & Risiko (der Multiplikator)**
- **Churn / Net Revenue Retention** (5%→10% Churn halbiert LTV) — Hormozi, Neil, Heartbeat, agency-scaler.
- **Golden Ratio: % Empfehler ÷ % Churn** (>1 = passives Wachstum) — Hormozi.
- **Profitabilität pro Kunde & pro Service** (größter Umsatzkunde = oft dünnste Marge) — Chris Do.
- **Umsatzkonzentration / Klumpenrisiko** (kein Kunde >20–40%) — Hormozi, Chris Do (Wiki-silent, aus Prinzip abgeleitet).
- **Fulfillment: Kosten <30%, NPS/Kundenzufriedenheit** — agency-scaler, Heartbeat.

## Darstellung (Konsens)
- **2 Default-Sichten:** CEO (Health/Growth/Cash) vs. Controller (Aging/Steuer/Reconciliation) — Neil, mkbhd.
- **Top-Band = Verdikt mit Richtung** (Runway „4,2 Monate", nicht „184.203 €"), ≤5–6 Kacheln; darunter Trends; darunter Drill-down — mkbhd, Neil, agency-scaler.
- **Jede Zahl mit Vergleich** (Vormonat/Vorjahr/Ziel) + Trend-Sparkline; „in a vacuum" ist wertlos — mkbhd, Chris Do, Neil, agency-scaler, Heartbeat (Korridore).
- **Ampel = Bedeutung** (grün/rot), Form < Funktion, Vanity killen, runde Zahlen — mkbhd, agency-scaler, Chris.
- **Kachel = Frage** die sie beantwortet („Kann ich 6 Monate Gehälter zahlen?") — Chris Do.
- **Engpass sichtbar machen:** die rote Kachel = was diesen Monat zu fixen ist — Hormozi, agency-scaler.
- **Action statt Starren:** Anomalie-**Alerts** (push bei Schwellenbruch) + festes **Review-Ritual** (Finance monatlich, Sales/Marketing wöchentlich) + „Action Steps"-Element — Neil, agency-scaler, Hormozi.

## Bonus für die App selbst (über die Frage hinaus)
- **Reconciliation als Glaubwürdigkeits-Superkraft:** externe/Plattform-Zahlen gegen die gebuchte Realität abgleichen (Neil) — ABER die Kontozahl um USt/Einmal-Posten **bereinigen** (Heartbeat). → **bereinigte Ist-Zahlen** als Wahrheit.
- **KI-Kategorisierung-Vertrauens-UX** (der eigentliche Produkt-Knackpunkt): Konfidenz zeigen (leise bei hoch, laut bei niedrig = Review-Queue), immer das **„Warum"** zeigen, **Ein-Gesten-Korrektur die sichtbar lernt**, Bulk-Korrektur, „KI schlägt vor, Mensch bestätigt" — mkbhd.
- **Positionierung:** Outcome verkaufen, nicht Feature — „Nie wieder von der Steuerrechnung überrascht / immer wissen ob du Gehälter zahlen kannst / endlich sehen welche Kunden Geld bringen", nicht „Lexware-API + Auto-Buchung" — Chris Do.

## Attribuierter Dissens / aufgelöste Spannungen
1. **Kontozahl:** Neil „gegen Bank abgleichen" vs. Heartbeat „trau der Kontozahl nie". → Aufgelöst: externe Claims gegen gebuchte Realität abgleichen, aber USt/Einmal-Posten-bereinigte Ist-Zahlen als Profit-Größe. Beide → „bereinigte Ist-Zahlen".
2. **Umsatzziel:** Heartbeat „**kein** großes rotes Umsatz-Monatsziel (demotiviert, Stufen-Denken), über Input-/Conversion-KPIs steuern" vs. Hormozis Forward-Kachel „Hypothetical Max Revenue = Sales-Velocity × LTGP". → Komplementär: Trajektorie/Run-Rate zeigen, kein schuldauslösendes fixes Monatsziel.
3. **Alerts vs. Ritual:** Neil „Alerts, nicht starren" vs. agency-scaler „mach ein Meeting draus". → Beides: Anomalie-Alerts + fester Review-Rhythmus.

## Gaps (ehrlich markiert)
**Alle Seats deferren einstimmig** bei: korrekte deutsche Steuerkategorien, GoBD/DATEV,
Lexware-Datenmodell, USt-Behandlung einzelner Eingangsrechnungen → **Steuerberater-Lane**,
keine Steuer-/Rechtsberatung aus dem Council. Der Council entwirft die **Steuerungs-/UX-
Schicht**, nicht die buchhalterische Korrektheit. Chris Do: Umsatzkonzentrations-Schwelle
aus Prinzip abgeleitet, nicht zitiert. Hormozi/Heartbeat: Money-Math ist universelle
Arithmetik, unabhängig vom Buchungsstandard.

## Per-Seat-Beitrag
- **heartbeat/Stefan Graf:** Finanzsteuerungs-Doktrin (3 Buckets, Profit-Level, CAC/DB-LTV, DB-Korridore, Sales-Funnel-KPIs, Stufen-Denken). Kernstimme.
- **hormozi:** Unit Economics (Gross Profit, LTGP:CAC, 30-Tage-Cash, Churn/NRR, Golden Ratio, EV=Kunden×LTGP÷Risiko, Engpass).
- **agency-scaler:** 3 Cockpits, Sales-Funnel pro Person, Umsatz/MA, offene Forderungen als Action-Liste, CPB/CPO/ROAS, „mach ein Meeting draus".
- **neil-patel:** Growth-Layer neben Finance (CAC, Spend%, Attribution, Wachstums-RATEN), Design (gegen Ist abgleichen, Vanity killen, Hierarchie, 2 Sichten, Alerts).
- **mkbhd:** Produkt/UX (Was du weglässt = Produkt, Verdikt-Top-Zeile, Trends+Vergleich, KI-Kategorisierung-Vertrauens-UX, Form<Funktion).
- **chris-do:** Entscheidungs- vs. Vanity-Metriken, Profitabilität pro Kunde/Service, Worry-Date, True-Free-Cash, Outcome-Positionierung.

## Nächster Schritt
Umsetzung: `/plan` (Dashboard-Informationsarchitektur + KPI-Definitionen + Datenherkunft aus Lexware) — oder direkt als Feature-Spec an den Gründer. Steuer-Korrektheit vorab mit einem Steuerberater klären.
