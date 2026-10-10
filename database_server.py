import sqlite3
from datetime import datetime

def run_fintech_schema_migration():
    """
    FINTECH CORE DATABASE ORCHESTRATION & SCHEMA MIGRATION NODE:
    Dynamically evaluates table structures to inject advanced tracking metrics
    onto active transaction ledgers with 0% data disruption and zero downtime.
    """
    db_name = "fintech_ledger_core.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    print("⏳ SCANNING ACTIVE TRANSACTION NODES FOR SCHEMA COMPLIANCE...")

    # 1. INITIALIZE BASE TRANSACTION TABLES IF EMPTY
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_transactions (
            tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_ticker TEXT NOT NULL,
            opening_price REAL NOT NULL,
            current_price REAL NOT NULL,
            price_delta_percent REAL NOT NULL,
            timestamp_utc TIMESTAMP NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operational_audit_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            component_source TEXT NOT NULL,
            event_description TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL
        )
    """)

    # 2. SCHEMA EVOLUTION LAYER: Dynamically read existing columns inside the running table
    cursor.execute("PRAGMA table_info(crypto_transactions)")
    columns_matrix = cursor.fetchall()
    existing_column_names = [col[1] for col in columns_matrix]

    # 3. INTERCEPT AND PATCH MATRIX: If the advanced gas fee tracking column is missing, inject it live
    new_column = "network_gas_fee_gwei"

    if new_column not in existing_column_names:
        print(f"🔧 SCHEMA MISMATCH CAPTURED: Migrating Live Ledger Database Structure to v2.0.0...")

        # Inject the advanced transaction parameters instantly into production
        cursor.execute(f"ALTER TABLE crypto_transactions ADD COLUMN {new_column} INTEGER DEFAULT 45")

        # Log the migration footprint safely into the enterprise system journal
        cursor.execute("""
            INSERT INTO operational_audit_logs (component_source, event_description, timestamp)
            VALUES (?, ?, ?)
        """, ("SCHEMA_MIGRATOR", f"Successfully migrated database schema to v2.0.0. Injected '{new_column}' column.", datetime.utcnow()))

        print(f"✅ DATABASE TRANSACTION SCHEMAS UPGRADED TO v2.0.0! [{new_column} Column Active]")
    else:
        print("🎯 MIGRATION MONITOR COMPLETE: Database schema matrix is already synchronized at version v2.0.0.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_fintech_schema_migration()