import asyncio
import logging
import sys
from typing import Dict

# [Modules Import] 우리가 만든 모든 레이어 통합!
from galactic_layer.cosmic_async_kernel import CosmicAsyncKernel
from galactic_layer.cosmic_galaxy_db import CosmicGalaxyDB
from transcendence.v15_ultimate_core import CosmicOS_v15_Ultimate_Core

# 로깅 설정
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("Cosmic_Final_v15")

class CosmicOS_v15_Unified_Kernel:
    """
    Cosmic OS v15.0.0: The Infinite Orchestrator
    - Merges v14 Multiverse & v15 Ultimate Core
    """
    def __init__(self):
        logger.info("🌌 [BOOT] Initializing Cosmic OS v15.0.0 'Infinite Orchestrator'...")
        
        # 1. 인프라 레이어 (v13)
        self.db = CosmicGalaxyDB()
        self.scheduler = CosmicAsyncKernel()
        
        # 2. 초월 레이어 (v15 통합 코어 - v14 기능 포함)
        self.ultimate_core = CosmicOS_v15_Ultimate_Core()
        
        self.is_active = True
        logger.info("✅ [BOOT] System v15.0 Unified. Eternal Stability Guaranteed! 🤨")

    async def start_up(self):
        """전 우주적 기능을 동시에 가동"""
        if not self.is_active: return

        print(f"\n" + "═"*70)
        logger.info("🚀 ACTIVATE: ULTIMATE ASCENSION PROTOCOL v15.0")
        print("═"*70 + "\n")

        # 3. 비동기 태스크 통합 실행
        try:
            # 커널 스케줄러와 초월 코어 부팅을 동시에!
            await asyncio.gather(
                self.scheduler.run_kernel(),
                self.ultimate_core.boot_ultimate_core()
            )
        except Exception as e:
            logger.error(f"❌ [CRITICAL] Multiverse Conflict: {e}")

# --- 실행부 ---
if __name__ == "__main__":
    # 인자값 처리 (필요시 사용)
    # mode = sys.argv[1] if len(sys.argv) > 1 else "Transcendence"
    
    kernel = CosmicOS_v15_Unified_Kernel()
    
    try:
        # 19살 연아의 우주, 최종 부팅!
        asyncio.run(kernel.start_up())
    except KeyboardInterrupt:
        logger.info("🌌 [SHUTDOWN] See you in the next Big Bang.")
