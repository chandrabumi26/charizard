import asyncio
import aiohttp
import json
# from tcgdexsdk import TCGdex, Language, Query
from dacite.exceptions import MissingValueError
import csv

import sys
import os
# Force vendor tcgdexsdk (patched version)
sys.path.insert(0, os.path.abspath("vendor"))

from tcgdexsdk import TCGdex, Language, Query

# async def fetch_raw_card(card_id):
#     url = f"https://api.tcgdex.net/v2/en/cards/?name={card_id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             return await resp.json()

def set_to_dict(s):
    return {
        "id": s.id,
        "name": s.name,
        "logo": s.logo,
        "symbol": s.symbol,
        "tcgOnline": s.tcgOnline,
        "releaseDate": s.releaseDate,
        "cardCount": {
            "total": s.cardCount.total,
            "official": s.cardCount.official,
        },
        "legal": {
            "standard": s.legal.standard,
            "expanded": s.legal.expanded,
        },
        "serie": {
            "id": s.serie.id,
            "name": s.serie.name,
            "logo": s.serie.logo,
        } if s.serie else None,
        "cards": [
            {
                "id": c.id,
                "localId": c.localId,
                "name": c.name,
                "image": c.image,
            }
            for c in (s.cards or [])
        ],
    }

def set_to_dict_simple(s):
    return {
        "id": s.id,
        "name": s.name,
    }

def card_to_dict_simple(card):
    return {
        "id": card.id,
        "localId": card.localId,
        "name": card.name,
        "category": card.category,
        "illustrator": card.illustrator,
        "hp": card.hp,
        "types": card.types,
        "stage": card.stage,
        "image": card.image,
        "set": {
            "id": card.set.id,
            "name": card.set.name,
        } if card.set else None,
    }

def serialize(obj):
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj

    if isinstance(obj, (list, tuple)):
        return [serialize(i) for i in obj]
    
    if hasattr(obj, "__dict__"):
        return {
            key: serialize(value)
            for key, value in obj.__dict__.items()
            if key != "sdk"
        }
    
    return str(obj)

def card_json_to_csv_row(card):
    return {
        "id": card["id"],
        "localId": card["localId"],
        "name": card["name"],
        "category": card["category"],
        "illustrator": card["illustrator"],
        "hp": card["hp"],
        "types": ",".join(card["types"] or []),
        "stage": card["stage"],
        "description": card["description"],
        "regulationMark": card["regulationMark"],
        "set_id": card["set"]["id"],
        "set_name": card["set"]["name"],
        "set_total_cards": card["set"]["cardCount"]["total"],
        "set_official_cards": card["set"]["cardCount"]["official"],
        "variants": json.dumps(card["variants"], ensure_ascii=False),
        "abilities": json.dumps(card["abilities"], ensure_ascii=False),
        "attacks": json.dumps(card["attacks"], ensure_ascii=False),
        "weaknesses": json.dumps(card["weaknesses"], ensure_ascii=False),
        "legal": json.dumps(card["legal"], ensure_ascii=False),
        "retreat": card["retreat"],
        "image": card["image"],
        "boosters": json.dumps(card["boosters"], ensure_ascii=False),
    }


async def main():
    tcgdex = TCGdex(Language.ID)

    card_set = await tcgdex.set.list()

    filtered_cards = [
        card for card in card_set
        if card.name.lower() == "ikatan takdir"
    ]

    set_id = filtered_cards[0].id

    get_card_set_id = await tcgdex.set.get(set_id)

    # sets_json = set_to_dict(get_card_set_id)

    # print(get_card_set_id.cards[0].id)

    # for card in get_card_set_id.cards:
    #     card_single = await tcgdex.card.get(card.id)
    #     print(json.dumps(serialize(card_single), indent=4, ensure_ascii=False))

    csv_file = "ikatan_takdir_cards.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = None

        for card in get_card_set_id.cards:
            card_single = await tcgdex.card.get(card.id)

            row = card_json_to_csv_row(serialize(card_single))

            if writer is None:
                writer = csv.DictWriter(f, fieldnames=row.keys())
                writer.writeheader()

            writer.writerow(row)

    print(f"CSV written to {csv_file}")

asyncio.run(main())
