---
type: plan
status: proposal
created: 2026-08-01
owner: Florian
---

# Meta Ads Copilot — klon-gesteuerter Kampagnen-Aufbau über die Meta Marketing API

**Idee:** Das destillierte Ads-Wissen der Persona-Klone (v. a. `eddy-ad`) als
Entscheidungs-Gehirn nutzen, um über die **Meta Marketing API** (Graph API v26.0) echte
Facebook/Instagram-Kampagnen **programmatisch anzulegen** — pausiert, prüfbar, vom Menschen
freigeschaltet. Die API kann Objekte bauen; die Klone wissen, *welche* und *warum*.

Grundlage: Recherche Meta Marketing API v26.0 (Stand 2026-08-01) + Klon-Doktrin aus
`clones/eddy-ad-clone/` (521 Adbaker-Lektionen), ergänzt durch `webinar-hero`,
`agency-scaler`, `heartbeat`.

---

## 1. Warum das stark ist

Eine Marketing-API allein ist dumm — sie legt an, was man ihr sagt. Der Engpass ist die
**Entscheidungslogik**: Struktur, Zielgruppen, Creatives, Budgets, wann skalieren. Genau die
ist in `eddy-ad` bereits kodiert und zitierfähig:

- **Struktur:** ABO (Testen) vs. CBO (Skalieren); Kampagne > Adset > Ad; Naming Conventions.
- **Budget/Lernphase:** ~50 Optimierungs-Events/Woche/Adset; Budget nicht zersplittern.
- **Zielgruppen:** broad / Lookalike 1 %→10 % / Interesse; „das Creative ist dein Targeting".
- **Creatives:** Ad Building Blocks (Hook→Body→CTA), Top-Hooks, Performance- vs. Grafikdesign.
- **KPIs:** Leadpreis/CPA als Richter, ROAS-Mindestwerte nach Marge, Offsite-vs-Onsite-Gewichtung,
  Diagnose-Logik (teurer Klick → Zielgruppe/Creative; billiger Klick + teurer Lead → Funnel/LP).
- **Skalierung:** vertikal 20–30 % / 24–72 h, dann horizontal über 5 Aktionslevel.

Das ist der „Taste-Layer", der die API von einem Werkzeug zu einem Operator macht.

---

## 2. Architektur (4 Schichten)

```
① STRATEGIE-GEHIRN   Klone (eddy-ad Kern; webinar-hero/agency-scaler/heartbeat Kontext)
                     Input: Angebot, Ziel-Leadpreis/ROAS, Budget, Funnel-Stufe, Markt
                     Output: strukturierter Kampagnen-BRIEF (JSON) — Objective, ABO/CBO,
                     Adset-Split, Zielgruppen, Creative-Angles+Hooks, Copy, Budget, Testing,
                     KPI-Ziele, Skalier-Regeln
        │
② ÜBERSETZER         Brief-JSON → Meta-API-Objekte (Campaign/AdSet/Ad/AdCreative +
                     targeting-spec + promoted_object/pixel). Validierung gegen v26.0-Schema.
        │
③ AUSFÜHRER          facebook_business SDK: legt alles STATUS=PAUSED an (oder Sandbox).
                     Liest zurück → Review-Report (Mensch prüft im Ads Manager, schaltet live).
        │
④ FEEDBACK (später)  Insights-API (Spend/CPL/ROAS/CTR) → zurück an eddy-ad → Diagnose &
                     Skalier-/Abschalt-Empfehlung (die Doktrin ist schon da).
```

---

## 3. Meta Marketing API — die harten Fakten (v26.0)

**Objektmodell (alles POST auf `act_<id>`):**
- Campaign: `POST /act_{id}/campaigns` — `name`, `objective` (ODAX: `OUTCOME_LEADS`,
  `OUTCOME_SALES`, `OUTCOME_TRAFFIC`, …), `status`, `special_ad_categories` (`[]` wenn keine).
- Ad Set: `POST /act_{id}/adsets` — `campaign_id`, `optimization_goal`, `billing_event`,
  `bid_strategy`/`bid_amount`, `daily_budget`/`lifetime_budget`, `targeting`, `promoted_object`
  (bei Conversions: `pixel_id` + `custom_event_type`), `status`.
- Ad Creative: `POST /act_{id}/adcreatives` — `object_story_spec` (Seiten-Post: `page_id`,
  `link_data`/`video_data`, `image_hash`, `message`, `call_to_action`). Assets vorher hoch:
  `/adimages` (→ `image_hash`), `/advideos` (→ video id).
- Ad: `POST /act_{id}/ads` — `adset_id`, `creative:{creative_id}`, `status`.

**Sicherheit „bauen ohne Spend":**
- `status=PAUSED` auf Campaign UND Adset → nichts wird ausgespielt/bezahlt, bis ein Mensch auf
  `ACTIVE` stellt. Standard-Muster: via API bauen → im Ads Manager prüfen → manuell aktivieren.
- **Sandbox-Werbekonto** (App-Dashboard): alle Calls funktionieren, aber Meta liefert nie aus →
  null Impressionen, null Spend, kein Zahlungsmittel nötig. Validiert Struktur, keine Perf-Daten.

**Auth/Zugang (die eigentliche Hürde, nach Schwierigkeit):**
1. Eigenes Konto, `ads_management`-Token → **sofort**, keine Review. (Minuten.)
2. **System-User-Token** (Business Manager) → produktionsstabil, läuft nicht ab. (~30 Min.)
3. **Business-Verifizierung** → nötig für Kunden-Konten. (Tage.)
4. **App-Review** für Advanced/Full `ads_management` → nur für Kunden-Konten. (am aufwändigsten.)

**Rate Limits:** Dev-Tier ~300 Schreib-Calls/h pro Werbekonto (Write=3 Punkte, Max-Score 60) →
beim Bulk-Anlegen batchen + `X-Business-Use-Case-Usage`-Header lesen. Full-Access-Upgrade
automatisch bei ≥500 Calls/15 Tage & <15 % Fehlerrate.

**Insights / Daten runterziehen (read-only):**
- `GET /act_{id}/insights` (oder je Campaign/Adset/Ad) — Felder: `spend`, `impressions`, `reach`,
  `frequency`, `clicks`, `ctr`, `cpc`, `cpm`, `actions` (Conversions), `cost_per_action_type`
  (= CPL/CPA je Event), `purchase_roas`, Video-Metriken (`video_thruplay_watched_actions` …).
- **Breakdowns:** `age`, `gender`, `publisher_platform`, `platform_position`, `region`, `device`,
  `hourly_stats_aggregated_by_advertiser_time_zone`, sowie je Creative/Ad.
- **Zeit:** `date_preset` (last_7d …) oder `time_range` + `time_increment` (täglich).
- Braucht nur **`ads_read`** → geringstes Risiko, kein Spend, kein App-Review fürs eigene Konto,
  funktioniert **sofort auf deinen bereits laufenden Kampagnen**.

**Stack:** `facebook_business` (Python SDK, am reifsten) oder Node-SDK; raw HTTP geht auch.

**Gotcha:** API-Versionen sunsetten ~2 Jahre → Version im URL pinnen (`/v26.0/`), Upgrades einplanen.

---

## 4. Modul-Breakdown & Aufwand (grobe Dev-Tage)

| Modul | Inhalt | Aufwand |
|---|---|---|
| M1 Brief-Generator | Klon-Prompt-Kette (eddy-ad + Kontext) → validiertes Brief-JSON-Schema | 1–2 d |
| M2 Übersetzer | Brief → Meta-Objekt-Payloads, v26.0-Schema-Validierung | 1–2 d |
| M3 Ausführer (Sandbox) | SDK-Anbindung, PAUSED-Anlage Campaign→Adset→Creative→Ad, Review-Report | 1 d |
| M4 Asset-Handling | Bild/Video-Upload (`/adimages`,`/advideos`), Creative-Bau | 0.5–1 d |
| M5 Targeting/Pixel | targeting-spec, Custom/LAL-Audiences, `promoted_object`/Pixel | 1 d |
| **M0 Analyse-Audit** | **Insights read-only ziehen → eddy-ad-Diagnose → priorisierter „Was besser machen"-Report** | **1–2 d** |
| M6 Insights-Feedback | laufender Loop: Insights → Diagnose → Skalier-/Abschalt-Empfehlung | 2–3 d |
| M7 Kunden-Modus | Business-Verifizierung + App-Review + Multi-Account | Wochen (extern) |

MVP = M1–M4 gegen Sandbox: realistisch **~1 Woche**. Kunden-tauglich (M7) ist ein separates,
Meta-getaktetes Projekt.

---

## 5. Guardrails (nicht verhandelbar)

- **Live/Spend = Mensch.** Ich lege nur PAUSED/Sandbox an. Keine Kampagne wird von mir auf
  `ACTIVE` gesetzt und kein Budget freigegeben ohne deine explizite Einzelfreigabe.
- **Token/Secrets fasse ich nicht an.** Du legst den System-User-Token an; der Code liest ihn
  aus `.env`/Keychain. Kein Klartext-Token durch mich.
- **Policy-Compliance:** `special_ad_categories` korrekt setzen; Meta-Werberichtlinien beachten
  (Ablehnungen sind normal — der Review-Report muss sie sichtbar machen).
- **Zitierbarkeit:** Jede strategische Entscheidung im Brief wird aus der Klon-Doktrin
  begründet/zitiert (wie im Live-Test), nicht erfunden.

---

## 6. Risiken & Mitigation

| Risiko | Mitigation |
|---|---|
| Rate Limits beim Bulk-Anlegen | Batch-Requests, Header-basiertes Self-Throttling, Backoff |
| API-Version-Sunset (~2 J.) | Version pinnen, Upgrade-Task im Backlog |
| Ad-Policy-Ablehnungen | `special_ad_categories`, Review-Report zeigt Rejects, Mensch entscheidet |
| Tracking/iOS-Signalverlust | Pixel **+ CAPI** (dataset-id in `promoted_object`) — Doktrin ist da |
| Sandbox liefert keine Perf-Daten | Struktur in Sandbox, Perf-Test später auf echtem Konto (PAUSED→live) |
| Kunden-Konten brauchen Review | Erst eigenes Konto/MVP, App-Review nur wenn Kundengeschäft kommt |

---

## 7. Phasen-Roadmap

1. **Phase 0 (jetzt):** dieser Plan. Entscheidung: eigenes Konto vs. Sandbox vs. Kundenmodus.
1b. **Phase 1a — EMPFOHLENER EINSTIEG: M0 Analyse-Audit.** Read-only Insights deiner **schon
    laufenden** Kampagnen ziehen → durch eddy-ads Diagnose-Doktrin jagen (teurer Klick →
    Zielgruppe/Creative; billiger Klick + teurer Lead → Funnel/LP; Lernphase; Skalier-Fenster)
    → priorisierter „Was-besser-machen"-Report mit Zitaten. **Nur `ads_read`, kein Spend, kein
    Anlegen, kein Review** — niedrigstes Risiko, sofortiger Wert am Tag 1.
2. **Phase 1b:** M1 Brief-Generator (reiner Text, kein Token) — zeigt Anlege-Qualität.
3. **Phase 2:** M2–M4 gegen **Sandbox** — End-to-End „Brief → pausierte Kampagne", null Risiko.
4. **Phase 3:** gegen **echtes eigenes Konto**, alles PAUSED, du schaltest live.
5. **Phase 4:** M6 Insights-Feedback-Loop (eddy-ad liest & optimiert).
6. **Phase 5 (optional):** M7 Kundenmodus (Business-Verifizierung + App-Review).

---

## 8. Was von dir gebraucht wird (ab Phase 2)

- Meta **Developer-App** (Marketing-API-Produkt, Limited Access — sofort).
- **Sandbox-Werbekonto** (Phase 2) bzw. **Business Manager + Werbekonto `act_<id>` + Facebook-Seite**
  (+ Instagram optional) für Phase 3.
- **System-User-Token** mit `ads_management` (du legst ihn an; Code liest ihn aus der Umgebung).

## 9. Offene Entscheidungen

- Eigenes Konto zuerst (schnell, keine Review) vs. direkt Kundenmodus (Review-Aufwand)?
- Python (`facebook_business`, reifer) — vermutlich ja.
- Wo lebt der Code? Eigenes Repo `meta-ads-copilot` vs. Modul im Roster.
- Umfang Phase 1 Brief: nur Leadgen (Dienstleistung) zuerst, oder gleich E-Com/Sales mit?
