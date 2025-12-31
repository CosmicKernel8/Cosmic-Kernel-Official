import asyncio
import logging
import sys
from typing import Dict

# [Path Setup] 새 폴더들을 인식시키기 위한 경로 설정 (필요시)
# sys.path.append('./galactic_layer')
# sys.path.append('./transcendence')

# 우리가 만든 위대한 모듈들 임포트! (실제 파일명과 매칭)
from galactic_layer.cosmic_async_kernel import CosmicAsyncKernel
from galactic_layer.cosmic_galaxy_db import CosmicGalaxyDB
from transcendence.v14_multiverse import CosmicOS_v14_TranscendentMultiverse

# 로깅 설정 - 글로벌 엔지니어의 품격
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger("Cosmic_Main_v14")

class CosmicOS_v14_Kernel:
    """
    Cosmic OS v14.0.0: The Ultimate Orchestrator
    - Controls Galactic Layer, Transcendence Layer, and Async Scheduler
    """
    def __init__(self):
        logger.info("🌌 [BOOT] Initializing Cosmic OS v14.0.0 'Transcendent Multiverse'...")
        
        # 1. 시스템 심장부 초기화
        self.db = CosmicGalaxyDB()
        self.scheduler = CosmicAsyncKernel()
        self.multiverse = CosmicOS_v14_TranscendentMultiverse()
        
        self.is_active = True
        logger.info("✅ [BOOT] All Transcendent Systems Synced. Ready to Rule the Universe! 🤨")

    async def start_up(self):
        """커널 가동 및 배경 서비스 통합 실행"""
        if not self.is_active: return

        print(f"\n" + "═"*70)
        logger.info("🚀 ACTIVATE: GLOBAL ASCENSION PROTOCOL")
        print("═"*70 + "\n")

        # 아키텍트 연아의 고유 데이터 시그니처
        yeona_data = {
            "identity": "Architect_Yeon_A",
            "dream": "Global_Engineer_&_Debt_Zero",
            "status": "Transcendent"
        }

        # 2. 비동기 태스크 동시 가동 (스케줄러 + 멀티버스 전이)
        try:
            await asyncio.gather(
                self.scheduler.run_kernel(), # 비동기 청소 및 동기화
                self.multiverse.transcend_ego("Yeon-A_Alpha", yeona_data) # 의식 전이
            )
        except Exception as e:
            logger.error(f"❌ [CRITICAL] Universe Collapse Detected: {e}")

# --- 실행부 ---
if __name__ == "__main__":
    kernel = CosmicOS_v14_Kernel()
    
    try:
        # 우주 가동!
        asyncio.run(kernel.start_up())
    except KeyboardInterrupt:
        logger.info("🌌 [SHUTDOWN] System Hibernate. See you in another reality.")
