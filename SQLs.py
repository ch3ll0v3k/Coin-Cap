#!/usr/bin/python
# -*- coding: utf-8 -*-

class SQLs(object):

    new_db = '''CREATE TABLE IF NOT EXISTS [TB_NAME] (
        id          INTEGER PRIMARY KEY,
        name        TEXT NOT NULL,
        symbol      TEXT NOT NULL,
        rank        INTEGER,
        price_usd   REAL,
        price_btc   REAL,
        vol24h_usd  REAL,
        cap_usd     REAL,
        avail_supp  REAL,
        total_supp  REAL,
        change_1h   REAL,
        change_24h  REAL,
        change_7d   REAL,
        updated     INTEGER
    )''';

