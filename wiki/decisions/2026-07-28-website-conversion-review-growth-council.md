---
type: decision
date: 2026-07-28
status: accepted
team: growth
seats: [hormozi, neil-patel, chris-do]
roles: [moderator, evidence-reviewer]
depth: standard
review_trigger: "Nach Launch des eigenen Founder-VSL + erster instrumentierter Funnel-Daten (Quiz-Start → Call gebucht): Prioritätenliste gegen echte Drop-off-Zahlen neu gewichten."
supersedes: "keine — ergänzt die Landing-Page-Records 2026-07-27 (o-vegas-Umbau, Growth-Council-Redesign) um einen Review-Stand nach Aufzeichnungs-Bibliothek/DOI/Shopify-Shelf."
---

# Growth Council: Website-Konversions-Review (ki-business-agenten.de)

**Decision.** Priorisierte Verbesserungsliste für die (Fast-)One-Page-Website verabschiedet,
einstimmig auf den P1-Kernpunkten. Zwei Hebel dürfen NICHT council-lokal umgesetzt werden
(Offer-Mechanik, harte Regel 3): eine **abschluss-kontingente Completion-Garantie** und
**Studio-Tag-Verknappung** — beide als Founder/Council-Vorlage geflaggt. Alles Übrige ist
Copy/Design/Instrumentierung im Konvertierungs-Scope (Founder-Direktive 2026-07-22: Councils nur
noch für Konvertierung). Confidence: high (Konvergenz der drei Sitze).

**Context.** Review-Auftrag „geh über die Seite, sag was fehlt / besser geht". Seite ist seit den
07-27-Records deutlich gewachsen (Aufzeichnungs-Bibliothek `/langform` + DOI, Shopify-Shelf,
eigene `/workshop`-Seite). Bindende Regeln in jede Sitz-Brief geladen: **ein Angebot** (Studio-
Workshop, 5.000 € öffentlich, nie rabattiert/gerechtfertigt), **Kauf-Motion = Anfrage Quiz→Call
(kein Checkout)**, ehrliches Deliverable (Bauplan + erster Baustein live + selbst-weiterbauen mit
Claude Code, kein Turnkey), Wording „du"/kein Rabatt-Vokabular/nur Belegbares, keine Community-/
2Key-Bewerbung, Shopify nur Shelf.

**Reasoning (attribuiert, zitiert).**

- **Founder-VSL ist der größte Einzelhebel (Hormozi #1, Chris Do #1).** Hormozi: VSL als
  Fünf-Teiler mit Belief-Breaking-Formel (was sie denken → warum falsch → was richtig → Beweis),
  „80 % des Werts stecken in den ersten 30–90 s", rough-Hook JETZT statt auf Politur warten
  (`sales-frameworks`). Chris Do: „People buy *you* before your product; polish repels, real
  attracts; the venue frames the value" — echter Founder, im echten Studio, first person, inkl.
  wem es *nicht* passt (`system-prompt`, `branding`). Aktueller Hero-VSL ist ein Platzhalter-Cut →
  transferiert null Belief.
- **Community-Leak raus (alle drei, P1).** Stat „11.000+ Menschen in der Community" + Skool-Link
  im Footer. Hormozi: konkurrierender, *gratis* Off-Ramp am Entscheidungspunkt („focus =
  eliminating alternatives"). Neil: „reverse edge" aus dem Funnel; Nav auf den einen relevanten
  CTA reduzieren (HubSpot-Cut-Nav-Test +14–28 %). Chris Do: Follower-Zahlen sind *Fame*, kein
  Käufer-Beweis; „fame ≠ brand". → ersetzen durch käufer-relevanten Proof (Firmen, mit denen
  gebaut wurde; live gebaute Bausteine); Skool-Link streichen.
- **„- Florian"-Testimonial (Hormozi P1, Chris Do P2).** Teilt den Vornamen des Owners → taints
  die sechs echten Video-Testimonials daneben. Voller Name + Firma + Gesicht, sonst raus.
- **Messung fehlt komplett — Neils #1 (P1).** Kein GA4/Consent-Mode/Event-Tracking (Quiz-Start/-
  Complete, Application, Call gebucht, Gate-Confirm, VSL-Play). „traffic + conversions³"; Plattform-
  Zahlen misstrauen, gegen die Bank rekonziliieren; DSGVO-Consent global als Default (in Neils
  Tests kein Opt-in-Verlust). Ohne Instrumentierung ist jede weitere Optimierung geraten.
- **Ein CTA, identisch + wiederholt (Chris Do P1, Neil P2).** Exakt gleicher Primär-CTA-String
  überall (Message-Kongruenz); CTA unter jedem Benefit-Block + nach den Testimonials wiederholen
  (In-Content-CTAs ~3–4× Klicks); Sekundär-Pfade als Text-Link, nie zweiter Primär.
- **Proof über die Falz (Hormozi P1) + Schema (Neil P1/P2).** Ein Proof-Element in den Hero ziehen.
  FAQPage + LocalBusiness JSON-LD ergänzen (Organization ist da); SEO-Basics + Indexierbarkeit der
  Hauptdomain bestätigen, Shopify-Shelf `noindex`.
- **Angst am CTA senken (Konvergenz Neil/Chris Do/Hormozi).** Micro-Copy „2 Min, kostenlos, wir
  sagen ehrlich, wenn es nicht passt" (Neil: Risk-Reducer auf die *Application*, kein Preis-Move;
  Chris Do: Accusation Audit „das ist kein Verkaufsgespräch").
- **Studio zeigen (Chris Do P2) + Present-Tense-Demo-Proof (Hormozi P2).** Echte Raum-/Build-Fotos;
  kurzer Screen-Capture eines live gebauten Bausteins mit Claude Code (senkt zugleich den
  Effort-Term der Value-Equation, den euer ehrliches „du baust selbst" anhebt).
- **Kleinere P2/P3:** Standort Potsdam vs. Jüterbog klar benennen (alle drei); FAQ-Antworten in
  Beweis enden lassen (Hormozi); messbare Testimonial-Ergebniszeilen (Chris Do); Gratis-Pfad aus
  dem Offer-Band nach unten (Hormozi); zwei dunkle Bänder am Seitenende entzerren (Chris Do);
  Hero-VSL lazy-load/Page-Speed (Neil); Cost-of-Inaction-Beat (Chris Do); `/langform` crawlbarer
  Teaser + E-Mail-Nurture (Neil).

**Dissent.**
- **Was ist DER #1-Move?** Hormozi + Chris Do: **Founder-VSL**. Neil: **erst den Funnel
  instrumentieren** („you can't improve what you can't see", +280 % Quiz-Lever ungemessen).
  Moderator-Auflösung: **keine Konkurrenz, verschiedene Achsen.** Instrumentierung ist billig,
  schnell, parallel und *Voraussetzung*, um den VSL-Effekt überhaupt zu messen → sofort. Der VSL
  ist der größte *Content*-Hebel, hängt aber am Founder (Dreh) → kritischer Pfad des Founders,
  rough-Hook jetzt. Beide parallel, keiner blockiert den anderen.
- **Garantie/Verknappung:** von Hormozi als große Hebel benannt, aber selbst als Founder/Council-
  Sache markiert. Bleibt Dissent-frei nur, weil hier NICHT entschieden — an Founder zurückgegeben.

**Assumptions.**
- Der Founder liefert einen Founder-VSL-Dreh (bislang der genannte höchste Hebel, unerledigt).
- Testimonial-„Florian", die Community-Zahl und etwaige Aggregat-Ergebniszahlen sind vor
  Veröffentlichung vom Founder zu verifizieren (nur Belegbares — alle drei Sitze mahnen es an).
- Studio-Tag-Verknappung ist nur nutzbar, wenn *legitim* (echte Kapazitätsgrenze).

**Rejected alternatives.**
- Community-Zahl/Skool als „Social Proof" behalten (Fame ≠ Käufer-Beweis; Off-Ramp am Peak).
- Preis rechtfertigen/rabattieren (Chris Do: „justification concedes higher ground"; Neil:
  Rabatt-Signups churnen +29 %). Preis-*Framing* gegen die Alternative bleibt richtig.
- Direkt-Checkout/„Jetzt buchen" (widerspricht Quiz→Call-Motion + Commitment).
- Design-Politur vor Messung/VSL (optimiert eine Seite, deren Kern-Persuasion-Asset fehlt).

**Risks / next experiment.**
- Placeholder-VSL transferiert weiter null Belief, solange kein Founder-Dreh kommt → größter
  Gap zwischen Traffic und 5.000-€-Close.
- Billigster nächster Schritt: (1) GA4+Consent+Events verdrahten und Quiz-Drop-off pro Frage
  sichtbar machen; parallel (2) die Founder-losen P1-Fixes (Community-Leak, Testimonial, CTA-
  Unifizierung, Schema) sofort umsetzen; dann (3) Founder-VSL-Rough-Hook A/B gegen Static-Hero,
  Urteil auf *gebuchte Calls*, nicht Plays.

**Affected.** ki-business-agenten-website: `src/content/site.ts` (Stats/CTA/Copy), `src/app/page.tsx`
(CTA-Wiederholung, Proof-über-Falz, Band-Rhythmus, Studio-Fotos), `src/components/Footer.tsx`
(Skool-Link), `src/app/layout.tsx` (FAQPage/LocalBusiness-Schema), Analytics/Consent (neu),
`/quiz` (Per-Frage-Tracking), `/langform` (Teaser+Nurture), VSL-Asset (Founder). Founder-Vorlage:
Completion-Garantie + Verknappung. Hub-candidate: no (projekt-lokal; Orchestrierung: Growth-Team +
Chris-Do-Include bei Website-Reviews bewährt).
