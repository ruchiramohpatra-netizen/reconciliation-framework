"""Simple tests to verify pytest works"""

def test_pytest_works():
    assert True

def test_import_recon_context():
    from src.core.recon_context import ReconContext
    rc = ReconContext("2025-08-20", "test_gold")
    assert rc.business_date == "2025-08-20"
    assert rc.gold_table_name == "test_gold"

def test_import_orchestrator():
    from src.core.orchestrator import Orchestrator
    from unittest.mock import Mock
    spark = Mock()
    orch = Orchestrator("2025-08-20", "test_gold", spark)
    assert orch is not None
