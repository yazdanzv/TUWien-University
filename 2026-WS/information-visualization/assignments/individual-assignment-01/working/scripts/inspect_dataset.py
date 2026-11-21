"""Inspect a preserved Eurostat JSON-stat extract without third-party packages.

Usage: python inspect_dataset.py path/to/ilc_lvho07b_TIMESTAMP.json
Prints coverage, flags, and a small set of source observations for review.
"""

import argparse
import json
from itertools import product
from pathlib import Path


def inspect(source: Path) -> dict:
    dataset = json.loads(source.read_text())
    dimensions = dataset["id"]
    categories = [
        sorted(
            dataset["dimension"][name]["category"]["index"],
            key=dataset["dimension"][name]["category"]["index"].get,
        )
        for name in dimensions
    ]
    assert [len(items) for items in categories] == dataset["size"]
    records = []
    for index, combination in enumerate(product(*categories)):
        position = str(index)
        if position in dataset["value"]:
            record = dict(zip(dimensions, combination))
            record["value"] = dataset["value"][position]
            record["status"] = dataset.get("status", {}).get(position, "")
            assert 0 <= record["value"] <= 100
            records.append(record)
    assert len(records) == len(dataset["value"])
    assert len({tuple(record[name] for name in dimensions) for record in records}) == len(records)

    groups = categories[dimensions.index("quant_inc")]
    years = categories[dimensions.index("time")]
    coverage = {}
    for country in ["AT", "EU27_2020", "DE", "CZ", "IT", "SI", "SK", "HU", "CH"]:
        country_records = [record for record in records if record["geo"] == country]
        available = {(record["quant_inc"], record["time"]) for record in country_records}
        coverage[country] = {
            "years_complete_for_all_income_groups": [
                year for year in years if all((group, year) in available for group in groups)
            ],
            "flagged_records": [record for record in country_records if record["status"]],
        }

    eu_members = {
        "BE", "BG", "CZ", "DK", "DE", "EE", "IE", "EL", "ES", "FR", "HR",
        "IT", "CY", "LV", "LT", "LU", "HU", "MT", "NL", "AT", "PL", "PT",
        "RO", "SI", "SK", "FI", "SE",
    }

    return {
        "source": str(source),
        "label": dataset["label"],
        "source_updated": dataset["updated"],
        "dimensions": dimensions,
        "observed_record_count": len(records),
        "coverage": coverage,
        "austria_eu_2025": [
            record for record in records
            if record["geo"] in {"AT", "EU27_2020"} and record["time"] == "2025"
        ],
        "austria_2015_2025": [
            record for record in records
            if record["geo"] == "AT" and int(record["time"]) >= 2015
        ],
        "eu_members_2025": [
            record for record in records
            if record["geo"] in eu_members and record["time"] == "2025"
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.source), indent=2))
