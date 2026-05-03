import logging

logger = logging.getLogger(__name__)


class ReconOutputDB:
    """Persistent layer - independent write methods per table."""
    
    def __init__(self, context, spark):
        self.context = context
        self.spark = spark
    
    def write_recon_run(self):
        logger.info("Writing recon_run table")
    
    def write_duplicate_check(self):
        logger.info("Writing duplicate_check table")
    
    def write_column_match(self):
        logger.info("Writing column_match table")
    
    def write_mismatch_summary(self):
        logger.info("Writing mismatch_summary table")
    
    def write_unique_detail(self):
        logger.info("Writing unique_detail table")
    
    def save_all(self):
        self.write_recon_run()
        self.write_duplicate_check()
        self.write_column_match()
        self.write_mismatch_summary()
        self.write_unique_detail()
