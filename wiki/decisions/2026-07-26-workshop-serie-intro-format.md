---
type: decision
date: 2026-07-26
status: accepted
team: youtube
seats: [mkbhd, hormozi, chris-do, skeptical-reviewer, evidence-reviewer]
review_trigger: nach 3 veröffentlichten Serien-Folgen (Opener + Show-Name gegen die feste Kanal-Benchmark auswerten)
supersedes: none
---

# Intro-Format der Studio-Workshop-Serie („Ein Tag, ein System")

**Decision.** Ein reproduzierbares, in HyperFrames templatisierbares 20–25-s-Intro für Sebastians
Studio-Workshop-Serie (ein echter Unternehmer baut einen Tag lang mit Claude Code; Vorbild
*Scale or Fail*). Nur **zwei SWAP-Slots** (Name + eine Ziel/Versprechen-Zeile) + ein Gast-Foto/-Clip;
alles andere fix. Cold Open = **Gast in der Reaktion** (Existenz zeigen, nicht Outcome); Gast = Held,
Sebastian = Begleiter, Gegner immer außen, **kein** Fail-/Kandidaten-Frame; **keine** „Fremder"-Behauptung;
Show benennen (A/B „Ein Tag, ein System" vs. „8 Stunden Vorsprung"). Volles Artefakt im Zielprojekt:
`youtube-engine/docs/concepts/workshop-serie-intro-format.md`. Confidence: **high** (auf Craft/Struktur),
**medium** auf konkreter Klick-Wirkung (eigene Evidenz fehlt noch).

**Context.** Aufnehmen läuft gut; die wiederkehrenden Intros/Werbeblöcke sind der Reib-Punkt. Sebastian
will ein generalisierbares Intro, das Post-Production auf einen Zwei-Felder-Job reduziert und trotzdem
„spannend wie eine Show" wirkt, ohne MrBeast-Hektik. Erster Lauf: Pierre (bereits gedreht). Nächster: Adam.
Effektive Kanal-Regeln geladen: Curiosity-Gap gewinnt 74/25 (aber Video trotzdem schwächstes der 10);
Warn-Frames underperformen auf beiden Kanälen; Outcome > Tool; Werte-Test; keine Gedankenstriche.

**Reasoning.**
- **Show statt Workshop [CD]:** Ein Workshop ist Logistik; zur Show wird es durch einen wiederkehrenden
  ehrlichen Konflikt. Ohne Preis/Rivalität ist **der Zustandswechsel selbst der Konflikt** (morgens fest,
  abends existiert ein echtes System). Ein benannter Format-Name macht Folgen zum kumulierenden Asset [AH+CD].
- **Stakes ohne Rivalität [AH]:** Value-Equation — „ein Tag" kollabiert Time Delay, die Relatability des
  Gastes hebt Perceived Likelihood. Offene Schleife = „schafft er's?", nie Negativität.
- **Held vor Begleiter [CD]:** StoryBrand (Gast = Held/Spider-Man, Sebastian = Guide/Uncle Ben). Umgekehrt
  entsteht eine Ich-Show, die Zuschauer und künftige Gäste abstößt.
- **Cold Open = Reaktion, nicht Ergebnis [alle]:** Ergebnis-Open spoilert (Chris: „story delaying"; verletztes
  Whodunit) und hebt die Erwartung auf Max → selbstgemachter Bust (MKBHD: „bust = Erwartung − Realität").
  Statischer Reveal hat keine Stakes. Gast-in-Reaktion + Want/Obstacle zeigt **Existenz, nicht Outcome** =
  100 % Beweis-Emotion, 0 % Spoiler, und ist jede Folge garantiert drehbar.
- **Produktion [MKBHD]:** unter 10 Schnitte/25 s, zwischen Gedanken schneiden, ein bewegtes Element,
  Audio trägt Energie/Bild trägt Ruhe, kein Logo-Sting vorne, KI nie am Gast-Gesicht (nur Hintergrund).

**Dissent.** Kein bestehender Dissens nach Cross-Examination — bemerkenswert, weil beide Anfangs-Konflikte
durch Konzession statt Kompromiss aufgelöst wurden:
- **Chris Do zog seinen eigenen Ergebnis-first-Cold-Open zurück** (verletzt seine eigene Story-Delaying-Doktrin).
- **Hormozi verwarf seine eigene stärkste Zeile** („kenne ihn seit heute Morgen"), nachdem der
  Evidence-Reviewer die Fremder-Behauptung als unwahr (Gäste = Empfehlungen) markierte; er diagnostizierte
  den Sog neu als Repräsentativität + kollabierte Zeit, nicht Fremdheit.
- **MKBHD schwächte Chris' „Gast-voiced payoff"** von Pflicht-Beat zu optionalem, spät gebundenem Slot
  (erzwungene Echt-Reaktion = manufacturierte Kandidaten-Show-Energie). Von allen akzeptiert.

**Assumptions.** (1) HyperFrames-Intro-Template wird einmal gebaut, dann Zwei-Felder-Job. (2) Ein 2-Min-
Weiße-Wand-Reveal-Clip pro Gast ist am Drehtag machbar. (3) Die Community-Mitgliedschaft bietet wirklich den
rohen Volltag als Gegenwert. (4) Voll gesprochen ist das Skript eher ~30 s → ggf. Beats auf VO-über-B-Roll /
Lower-Third verschieben.

**Rejected alternatives.**
- Ergebnis-first Cold Open (Spoiler + Overpromise).
- „Fremder"-Proof-Zeile (bricht Werte-Test/Ehrlichkeit).
- Gameshow-Theatrik: Countdown/Preisrad/Hype-Stings (lesen als der benannte Feind = KI-Hype-Händler).
- KI-Enhance am Gast-Gesicht (Hautton-Drift, Wachsfigur, Vertrauens-Killer).
- „Gast-voiced payoff" als Pflicht-Beat (nicht zuverlässig/echt erzwingbar).

**Risks / next experiment.**
- **Warn-Frame-Risiko:** Beat 2 („keiner sagt dir ehrlich…") ist strukturell nah an den Underperformer-Frames
  beider Kanäle → leicht halten, an echten Folgen messen. Billigster Test: die Adam-Folge damit fahren und
  Retention der ersten 30 s + Kanal-Benchmark ablesen.
- **Opener-Test 70/20/10:** FIXED-Opener als Kontrolle, alle paar Folgen einen neuen testen.
- **Show-Name A/B:** „Ein Tag, ein System" vs. „8 Stunden Vorsprung".

**Affected.** `youtube-engine/docs/concepts/workshop-serie-intro-format.md` (neu, Haupt-Artefakt),
`docs/concepts/videoformat-studio-workshop.md` (Cross-Link + Ganztags-Hinweis), `docs/index.md`,
`videos/wip/2026-07-21-collab-pierre-workshop-tag/drehplan.md` (p1/p2-Ablösung notiert), `docs/log.md`.
