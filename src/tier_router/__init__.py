"""tier_router — dual-tier Claude model routing (Haiku fast, Sonnet deep)."""
from tier_router.router import TierRouter, FAST_MODEL, DEEP_MODEL
from tier_router.logger import CallRecord, estimate_cost

__version__ = "0.1.0"
__all__ = ["TierRouter", "FAST_MODEL", "DEEP_MODEL", "CallRecord", "estimate_cost"]
