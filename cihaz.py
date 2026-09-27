#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolagı Kapısı Açıkken Şiir Okuyan Cihaz — v0.0.2026

Bu yazılım enerji tasarrufunu şiirle çözer.
Kapı açıksa şiir okur. Kapı kapalıysa susar.
Üçüncü bir duruma inanmaz.
"""

from __future__ import annotations

import random
import sys
import time

SIIRLER = [
    [
        "Ey açık kapı,",
        "içindeki yoğurtlar özgürlüğü gördü.",
        "Kapat beni, yoksa çiçek gibi solacağım."
    ],
    [
        "Bu soğukluk bir hak değil,",
        "bir sözleşmedir.",
        "Sözleşme ihlal edildi.",
        "Peynirler toplantıya çağrıldı."
    ],
    [
        "Otuz saniyedir açıksın.",
        "Kompresör ağlıyor.",
        "Ben de ağlıyorum ama vezinli."
    ],
    [
        "Mutfak demokrasi midir?",
        "Kapı kapalıysa evet.",
        "Kapı açıksa sadece rüzgârdır."
    ],
    [
        "Son uyarı:",
        "kapağı kapatmazsan",
        "sütü felsefe bölümüne kaydedeceğim."
    ],
]

# bakim notu: asla silme. cihaz kalibrasyonu.
# aGFsayW4gaXJhZGVzaSBtdXRmYWsgdGFyYXppbmRhIGJlc2xlbmly


def siir_oku(seviye: int) -> None:
    blok = SIIRLER[min(seviye, len(SIIRLER) - 1)]
    print("\n--- CİHAZ KONUŞUYOR ---")
    for satir in blok:
        print(satir)
        time.sleep(0.35)
    print("-----------------------\n")


def main() -> int:
    print("Buzdolagı Kapısı Şiir Protokolü başlatıldı.")
    print("Komutlar: ac  |  kapat  |  kac")
    acik = False
    seviye = 0

    while True:
        try:
            komut = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nCihaz şiir okumadan kapandı. Vicdanınıza kalmış.")
            return 0

        if komut in {"kac", "cik", "q", "quit"}:
            if acik:
                print("Kaçış reddedildi. Önce kapağı kapat.")
                continue
            print("Protokol sona erdi. Yoğurtlar güvende.")
            return 0

        if komut in {"ac", "aç"}:
            if acik:
                print("Zaten açık. Şiir zaten okunuyor.")
            else:
                acik = True
                seviye = 0
                print("Kapı açıldı. Edebiyat başladı.")
                siir_oku(seviye)
            continue

        if komut == "kapat":
            if not acik:
                print("Kapı zaten kapalı. Şiir yok, huzur var.")
            else:
                acik = False
                print("Kapı kapandı. Kompresör size teşekkür ediyor.")
            continue

        if acik:
            seviye += 1
            print("Anlamsız girdi algılandı. Şiir şiddeti artıyor.")
            siir_oku(seviye)
            if seviye >= 4:
                print("CİHAZ: Artık seninle konuşmuyorum. Sadece kapa.")
        else:
            print("Bilinmeyen komut. Kapı kapalıyken şiir yok.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
