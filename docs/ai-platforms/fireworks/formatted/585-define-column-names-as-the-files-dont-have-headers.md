---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define column names as the files don't have headers

COLUMN_NAMES = {
    "airports": ["airport_id", "name", "city", "country", "iata", "icao", "latitude", "longitude", "altitude", "timezone", "dst", "tz_db", "type", "source"],
    "airlines": ["airline_id", "name", "alias", "iata", "icao", "callsign", "country", "active"],
    "routes": ["airline", "airline_id", "source_airport", "source_airport_id", "destination_airport", "destination_airport_id", "codeshare", "stops", "equipment"],
    "countries": ["name", "iso_code", "dafif_code"],
    "planes": ["name", "iata", "icao"]
}

PROD_DB_PATH = "data/prod_openflights.db"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
