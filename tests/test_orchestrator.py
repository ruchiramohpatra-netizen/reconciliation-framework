import pytest
from unittest.mock import Mock
from src.core.orchestrator import Orchestrator
from src.core.recon_context import ReconContext


class TestOrchestrator:
    
    def test_orchestrator_initialization(self):
        spark = Mock()
        orch = Orchestrator("2025-08-20", "test_gold", spark)
        assert orch.business_date == "2025-08-20"
        assert orch.gold_table_name == "test_gold"
        assert isinstance(orch.ctx, ReconContext)
    
    def test_orchestrator_run_calls_modules(self):
        spark = Mock()
        orch = Orchestrator("2025-08-20", "test_gold", spark)
        
        orch._load_metadata = Mock()
        orch._map_attributes = Mock()
        orch._build_queries = Mock()
        orch._execute_recon = Mock()
        orch._check_duplicates = Mock()
        orch._persist_outputs = Mock()
        
        orch.run()
        
        orch._load_metadata.assert_called_once()
        orch._map_attributes.assert_called_once()
        orch._build_queries.assert_called_once()
        orch._execute_recon.assert_called_once()
        orch._check_duplicates.assert_called_once()
        orch._persist_outputs.assert_called_once()
