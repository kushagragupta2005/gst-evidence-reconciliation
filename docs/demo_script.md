# Narrated demo script

The included MP4 uses these five voiceover sections and custom evidence screens. The opening repeats the exact problem statement shown in the README and pitch deck.

## 1. Problem

A GST officer can’t tell which factories are hiding production or inflating tax credits, because every document she checks is declared by the factory itself, while the independent evidence (power use, goods movement, supplier records, bank flows) sits in separate places and is never compared. If this worked, she would start each week with a short list of units whose paperwork contradicts physical reality, each contradiction spelled out, and honest-but-unusual factories cleared.

## 2. Planted cheat

Here is F zero zero zero zero three nine, a planted dispatch-without-invoice case. The e-way bills show seven hundred sixty-nine units moved; no matching invoice quantity appears. Purchases and power imply eight hundred twenty-seven point two units of output, while five hundred ninety-five were declared. The stock roll-forward shows a two hundred thirty-two point two unit gap in the other direction. Three independent SQL check families place it in the priority queue. The case note restates these evidence values and asks for human review.

## 3. Honest decoy

Now compare F zero zero zero zero zero two, a product-mix-shift decoy. Its mix changes in February, but the independent evidence checks show no material, dispatch, or stock contradiction. It has zero discrepancy signals and the queue clears it. This keeps an unusual change from becoming a fraud accusation.

## 4. Scale

At scale, we loaded one hundred twenty thousand factories, three hundred sixty thousand factory-months, and two point five one million evidence rows into Exasol Personal. The SQL queue caught twenty-four thousand out of twenty-four thousand planted cheats, while zero of twenty-four thousand honest decoys were prioritised. The priority query completed in one point four zero seven seconds. These are seeded synthetic results on one local eight-gigabyte virtual machine, not real-world benchmarks.

## 5. Germany comparison

The same evidence pattern appears in European VAT carousel investigations. In May twenty twenty-six, EPPO reported a suspected Germany-linked case involving missing traders and cross-border invoice chains. This prototype shows how to trace evidence; it does not implement German VAT rules.
