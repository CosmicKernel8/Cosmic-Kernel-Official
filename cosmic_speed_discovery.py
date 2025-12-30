import asyncio
import random

class GalacticSpeedDiscoverer:
    """
    Cosmic OS v13.1.0: The Speed of Thought
    - Fastest-Shard Discovery (최단 시간 샤드 감지)
    - Quorum Read Logic (정족수 기반 데이터 검증)
    - Zero-Latency Retrieval (지연 시간 제로 지향)
    """
    def __init__(self, db_instance):
        self.db = db_instance
        self.shards = db_instance.shards

    async def _fetch_from_shard(self, shard, key):
        """개별 은하계에서 데이터를 가져오는 가상의 통신 (지연 발생 시뮬레이션)"""
        latency = random.uniform(0.01, 1.0) # 은하계마다 거리가 다르니까!
        await asyncio.sleep(latency)
        
        data = self.db.data_map[shard].get(key)
        if data:
            return {"shard": shard, "data": data, "latency": latency}
        raise ValueError("Data not found!")

    async def get_fastest_ego(self, key):
        """가장 빨리 응답하는 은하계의 데이터를 즉시 채택! (Race Mode)"""
        print(f"🏁 [RACE] Start! Fetching '{key}' from all Galaxies...")
        
        # 모든 샤드에 동시에 요청을 보냄
        tasks = [asyncio.create_task(self._fetch_from_shard(s, key)) for s in self.shards]
        
        # 가장 먼저 완료되는 태스크가 나올 때까지 대기!
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        
        # 1등으로 도착한 결과 추출
        fastest_result = next(iter(done)).result()
        
        print(f"🏆 [WINNER] {fastest_result['shard']} Galaxy responded in {fastest_result['latency']:.4f}s!")
        
        # 나머지 느림보 태스크들은 취소해서 리소스를 아낌! (차연아의 저비용 철학)
        for task in pending:
            task.cancel()
            
        return fastest_result['data']

    async def quorum_read_ego(self, key, threshold=2):
        """[QUORUM] 과반수 이상의 은하계가 동의한 데이터만 신뢰! (보안 강화)"""
        print(f"🛡️ [QUORUM] Verifying data integrity across {threshold} shards...")
        tasks = [self._fetch_from_shard(s, key) for s in self.shards]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        valid_results = [r['data'] for r in results if isinstance(r, dict)]
        
        if len(valid_results) >= threshold:
            # 데이터가 모두 일치하는지 확인 (자아 안정성 알고리즘의 확장)
            if all(x == valid_results[0] for x in valid_results):
                return valid_results[0]
        
        raise RuntimeError("⚠️ [CRITICAL] Quorum not reached or data mismatch!")
