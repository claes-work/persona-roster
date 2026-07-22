---
type: decision
date: 2026-07-22
status: accepted
team: growth
seats: [hormozi, chris-do, neil-patel]
roles: [moderator, evidence-reviewer]
depth: standard
review_trigger: "Erste Kurs-Verkaufszahlen über Shopify (Custom-Build-Reevaluierung); Event-2-Runs-Kill-Test; Phasenübergänge Tag 45/90 des 2Key-Funnels; monatliche Bank-Rekonziliation."
supersedes: "Reverst die On-Site-Commerce-Sperre aus 2026-07-21-website-funnel-structure.md (falsche Prämisse korrigiert); bestätigt und schärft die BUILD-Sperre aus 2026-07-21-funnel-operational-rulings.md (Custom-Website-Rebuild bleibt denied)."
---

# Growth Council: Website-Shop-Override ratifizieren + Event-/Workshop-/2Key-Funnel-Rulings

Kontext: Firmen-Website-Neubau (Claes & Herrmann KI-Agenten GmbH). Founder-Override (D0
der Grill-Findings in `../company-website/website-implementation-findings.md`) plus drei
Funnel-Detailfragen dem Growth Council vorgelegt. Geplanter Stack: self-hosted Next.js +
self-hosted Supabase + Shopify (Commerce, YouTube-Shopping) + Bunny (Video) + Brevo (Mail);
2Key getrennt/off-website.

**Neuer Fakt, der eine frühere Prämisse korrigiert:** Runde 5 (`website-funnel-structure`)
kippte „no on-site commerce" mit der Begründung „YouTube shop integration only supports
approved providers". Das ist falsch — **Shopify IST ein von YouTube-Shopping zugelassener
Provider.** Damit fällt die Prämisse, auf der das On-Site-Commerce-Verbot ruhte.

## Decision (Verdict)

**1. Founder-Override: BEDINGT RATIFIZIERT — Kanal ja, Custom-Build nein (einstimmig).**
- **Kanal ratifiziert, ohne Vorbehalt:** eigener Shopify-Shop + Kurs-DIREKTKAUF on-site +
  YouTube-Shopping. Der korrigierte Fakt macht die Round-5-Prämisse tot; Chris Do widerruft
  ausdrücklich sein eigenes Round-5-Veto („a native Shopify store that surfaces the product
  under the video is *fewer* hops, not more → the doctrine that killed commerce now argues
  FOR it"). Direktkauf = weniger Hops = mehr Completions (Neil); „sell at the point of
  greatest deprivation" (Hormozi).
- **Build-Scope NICHT ratifiziert:** der self-built Next.js + self-hosted Supabase + eigener
  Bunny-Player als Kurs-LMS bleibt der Round-3-Befund „a second software product wearing a
  website costume" (Chris Do) / „the textbook wrong-lever trap" (Hormozi). Der YouTube-Fakt
  dreht den *Verkaufskanal*, nicht die *Wrong-Lever-Regel*. Confidence: high (einstimmig).

**2. Event-Buchungs-/Belastungs-Mechanik (einstimmig nach Kreuzbefragung):**
Primär **(a)** Karte hinterlegen, erst bei Zustandekommen belasten — via Shopify-App mit
vaulted-card/deferred-capture, *falls* das App-Ökosystem es sauber hergibt (Shopify-natives
authorize-capture hält nur ~7 Tage < mehrwöchiges Fill-Fenster → reines Auth-Hold scheidet
aus). Realistischer Default: **(c) Deposit**, von Neil geschärft zu **nicht-erstattbar-aber-
übertragbar** (rollt in die nächste Kohorte, falls Event nicht zustande kommt). **(d) Sofort
+ Refund verworfen** (Brand-Veto Chris Do, mitgetragen). **(b) Gratis-Reservierung verworfen**
(No-Show-Falle). E-Mail in Schritt 1 (Abandoned-Checkout-Recovery), ehrliche Deadline-Urgency,
Deposit-Höhe auf Gesamtprofit splittesten (nicht Conversion-%).

**3. Workshop-Preis pro Kopf (Rahmen; konkrete Zahl = Founders):**
Wertbasiert, premium, **kein Rabatt**; **~2× ist Boden, nicht Ziel** (Hormozi: für live+
interaktiv zu billig gedacht). Self-Serve-Korridor **$1.000 Boden – ~$3.000 Decke** (Neil,
Webinar-Ökonomie); **über ~$3.000 → Bewerbungs-/Qualifizierungsschritt davor** (deckt sich mit
der Anfrage-Motion des Workshops). Kalibrierung: Three-Yeses; Close-Rate >60–70 % = unterpreist
→ verdoppeln, nicht erhöhen in Trippelschritten.

**4. /2key-Funnel-Übergabe in die separate 2Key-App:**
`/2key` = **Lead-Magnet/Anzeige, kein Checkout**; **EINE Vorwärts-CTA** je Phase (Warteliste →
Pre-Order → Gratis-Signup); Owned-E-Mail mit Source-Tag einsammeln und weiterreichen; **Value-
vor-Karte**; Vaporware-Verbot über die Naht hinweg (nur Existierendes); **forward-only, keine
Loops** (sonst bricht Attribution); frischer Consent auf 2Key-Seite; harter Message-Match
zwischen `/2key` und App. Der eigentliche Kauf passiert am Peak-Pain **in der App**.

## Rulings / Reasoning (attribuiert, zitiert)

- **Kanal-Ja (alle drei):** Neil — „own your audience and monetize ~1%", „sell inside the
  platform for ROAS"; Direktkauf beseitigt eine Rückwärtskante (Kursseite → Skool → separater
  Kauf), die Attribution zerstört. Chris Do — Round-5-Doktrin „send nothing that could confuse"
  argumentiert bei korrektem Fakt FÜR den Direktkauf (weniger Hops). Hormozi — „sell at the
  point of greatest deprivation".
- **Build-Nein (alle drei):** Hormozi — „Simple Scales, Fancy Fails"; „businesses die of
  indigestion, not starvation"; Build-Zeit gehört 2Key. Chris Do — „a second software product
  wearing a website costume"; off-the-shelf-Delivery (Shopify-Digital-Delivery / Course-App /
  Skool-Classroom) + Bunny-Plug-in reicht; Custom-Player „deferred until sales volume proves
  it". Neil — „validate/pre-sell before you build; collect money first"; „budget problem, not
  money problem" — Custom-Delivery-Stack gegen bewiesenen Umsatz erst später buchen.
- **Event (a)/(c):** Hormozi — „Pay Less Now or Pay More Later" (Karte für 0 €, Belastung bei
  Zustandekommen), Karte = Commitment-Filter; (d) hält fremdes Geld für ein noch nicht
  garantiertes Event → „selling stuff you can't deliver on ruins your reputation"; Deposit
  fängt Neils Money-first-Logik zu ~80 % ohne Reputationskosten. Chris Do — „bucket of trust:
  everything you do loses or gains trust"; volles Geld für ein Vielleicht = genau der „String",
  Refund ist Rückgabe von Float, kein Geschenk; Deposit-first („anxious people don't buy").
  Neil — konvergiert auf (c): „protect the brand over the last dollar"; Deposit ist trotzdem
  Commitment-Filter + Cash-forward + E-Mail-Capture, und Shopify-nativ (kein Auth-Fenster-Race).
- **Workshop-Preis:** Neil — harte Rails aus Webinar-Ökonomie ($1k Boden / ~$3k Self-Serve-
  Decke; über $3k ohne Sales-Team schwer); Tier-Anchoring (Masterclass neben Workshop);
  „cheap reads as fake". Hormozi — „charge as high as you can say out loud without cracking a
  smile"; „don't inch — double"; live+interaktiv = AI-resistentes Alpha, teuerster Teil.
  Chris Do — Three-Yeses; >60–70 % Close = unterpreist; „re-design, don't discount".
- **/2key:** Chris Do — „matchmaker, not seller: stay free if that's enough"; „one CTA, don't
  confuse"; „no card before value"; Give-Value-Ratio ~12–15:1. Neil — „no reverse edges",
  Unique-Link + monatliche Bank-Rekonziliation, Message-Match wie bei Paid-Ads, globaler Consent
  ohne Opt-in-Verlust. Hormozi — Cold-Traffic nie direkt auf Kaufen; Lead-Magnet → Peak-Pain-
  Kauf in der App; Pre-Order vor Free-Trial; Founding = eingefrorener Preis + Boni, kein Rabatt.

## Dissent (preserved)

- **Event (a) vs (c):** kontingent auf Shopify-App-Machbarkeit — Hormozi/Chris Do bevorzugen
  (a), falls eine vaulted-card/deferred-capture-App existiert (dann „(a) beats both, moot").
  Alle „no wiki number → test it". Hormozi ergänzt eine **Pay-Now-Option (MESO)** neben der
  Reservierung; Deposit erzeugt eine zweite Verkaufssituation (Hormozi-Caveat). Neils Deposit
  ist **nicht-erstattbar-aber-übertragbar** (statt refundable) — schärfere Variante.
- **Build-Scope vs. Founder-Wille:** Der Founder hat in der Grill-Session den self-hosted
  Custom-Stack gewählt. Das Council registriert das als sein Vorrecht, benennt es aber
  geschlossen als falschen Hebel zulasten von 2Keys Runway. **Kein Konsens Founder↔Council
  im Build-Scope — bewusst offen an den Founder zurückgegeben.**
- **Workshop-Zahl:** keine konkrete Euro-Zahl (kein Seat hat Grundlage; bewusst an Founders).

## Assumptions

- Shopify-App-Ökosystem bietet (a) vaulted-card/deferred-capture sauber an — ungeprüft.
- Off-the-shelf-Course-Delivery (Shopify-Digital / Course-App / Skool) ist akzeptable UX für
  den MVP; Custom-Player ist ein Upgrade nach Umsatzbeweis, kein Launch-Blocker.
- US-Priors (Neils $1k/$3k-Rails, Refund-/Close-Rate-Zahlen) übertragen sich grob auf DE — testen.
- 2Key bleibt technisch/finanziell getrennt; Website bewirbt + Owned-E-Mail-Handoff.

## Rejected alternatives

- On-Site-Commerce-Verbot beibehalten (Prämisse widerlegt — Shopify ist zugelassen).
- Self-built Kurs-LMS/Player als Launch-Abhängigkeit (Round-3-Wrong-Lever bestätigt).
- Event: (d) Sofort+Refund als Default (Brand-Veto); (b) Gratis-Reservierung (No-Show-Falle).
- Workshop unter $1k / mit Rabatt (unterpreist, Marken-/Churn-Schaden).
- 2Key-Checkout/Stripe auf der Website; Rückwärtskanten im Funnel (Attribution).

## Risks / next experiment

- Custom-Build frisst 2Key-Runway, falls Founder gegen das Ruling baut — Council-Warnung steht.
- Event: Shopify-(a)-Machbarkeit ungeprüft → erst App-Landschaft evaluieren, sonst (c).
- Cross-App-Drop-off Website→2Key = reale Conversion-Steuer → Message-Match + wenige Schritte;
  Pre-fill-Handoff (SSO-artig, mit Consent) vs. cold testen.
- Billigster nächster Schritt: Shopify-Store + off-the-shelf-Delivery aufsetzen, Kurse pre-sell,
  DANN über Custom-Delivery entscheiden.

## Affected

Company-website (Plan-Artefakt `company-website/website-implementation-findings.md` D0/D5/D10 —
Build-Scope-Ruling einarbeiten), Shopify-Store + Course-App + Bunny, Event-Buchungs-App,
`/2key`-Übergabe, Workshop-Preis-/Anfrage-Motion. Hub-candidate: yes.

## Founder-Auflösung (2026-07-22, nach Council)

Der Founder **überstimmt den Build-Scope-Teil** (Punkt 1, „Custom-Build nein"): der self-hosted
Stack (Next.js + self-hosted Supabase + eigener Bunny-Player) **wird gebaut**. Begründung: das
Council kannte zwei Fakten nicht — (1) den Build-Speed mit Claude Code, (2) die bereits gesetzte
Projekt-Struktur —, wodurch der Eigenbau kein teurer „wrong lever" ist; das Risiko wird bewusst
genommen. Kanal-Ratifizierung + Event-/Workshop-/2Key-Rulings bleiben unberührt in Kraft.

**Scope-Direktive für künftige Councils (Founder):** Die Infrastruktur-/Build-Grundsatzfrage
ist GESCHLOSSEN und wird **nicht erneut vorgelegt**. Councils werden für dieses Projekt künftig
nur für **Konvertierung** einberufen (Onboarding-Funnel, Flow, Copy/Texte, Conversion → Umsatz),
nicht um die Sinnhaftigkeit der Infrastruktur zu re-litigieren.
