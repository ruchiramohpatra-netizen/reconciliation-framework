# Reconciliation Framework

A modular, class-based reconciliation framework for comparing Gold and Bronze tables.

## Quick Start

1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install: `pip install -r requirements.txt`
4. Run tests: `pytest tests/`
5. Run notebook: `notebooks/run_reconciliation.ipynb`

## Parameters

Only two parameters change per run:
- `business_date`
- `gold_table_name`

## Output Tables

- recon_run (parent)
- duplicate_check
- column_match
- mismatch_summary
- unique_detail
