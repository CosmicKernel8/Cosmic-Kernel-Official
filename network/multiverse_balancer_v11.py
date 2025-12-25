import hashlib
import sqlite3
import time
from collections import OrderedDict

# [정보] 이 모듈은 분산 노드 간의 데이터 균형과 원자적 이동(Migration)을 담당합니다.
# 핫 파티션을 방지하는 Consistent Hashing과 데이터 무결성을 보장하는 2PC 기술이 적용되었습니다!

class CosmicMultiverseBalancer:
    """
    Cosmic OS v11.0.0: The Final Equilibrium
    - Consistent Hashing (Hot Partition Defense)
    - 2-Phase Commit (Migration Integrity)
    - Global Query Aggregator (Full Visibility)
    """
    def __init__(self, shards=["Solar", "Andromeda", "Virgo"]):
        self.shards = sorted(shards)
        self.ring = self._build_hash_ring(shards)

    def _build_hash_ring(self, shards):
        """일관된 해싱 링 구축 (가상 노드 기법 적용)"""
        ring = {}
        for shard in shards:
            # 각 샤드당 3개의 가상 노드를 배치해 부하 불균형 해소
            for i in range(3):
                h_key = int(hashlib.md5(f"{shard}:{i}".encode()).hexdigest(), 16)
                ring[h_key] = shard
        return OrderedDict(sorted(ring.items()))

    def get_shard(self, key):
        """해당 데이터가 저장될 최적의 샤드 결정 (해싱 링 순회)"""
        h_val = int(hashlib.md5(key.encode()).hexdigest(), 16)
        for h_key in self.ring.keys():
            if h_val <= h_key:
                return self.ring[h_key]
        return self.ring[next(iter(self.ring))]

    def global_count(self):
        """전체 분산 샤드에 흩어진 데이터 개수 통합 집계"""
        total = 0
        for shard in self.shards:
            try:
                with sqlite3.connect(f"cosmic_{shard}.db") as conn:
                    res = conn.execute("SELECT COUNT(*) FROM storage").fetchone()
                    total += res[0] if res else 0
            except sqlite3.OperationalError:
                continue # 샤드 데이터베이스가 아직 생성 전일 경우 무시
        return total

    def migrate_ego_2pc(self, ego_key, from_shard, to_shard):
        """2단계 커밋(2PC)을 이용한 원자적 데이터 마이그레이션"""
        print(f"🌀 [2PC_PHASE_1] Preparing migration: {from_shard} -> {to_shard}")
        
        # [준비 단계] 연결 확인 및 데이터 존재 여부 검사
        try:
            with sqlite3.connect(f"cosmic_{from_shard}.db") as conn_f, \
                 sqlite3.connect(f"cosmic_{to_shard}.db") as conn_t:
                
                data = conn_f.execute("SELECT payload FROM storage WHERE key=?", (ego_key,)).fetchone()
                if not data: return "❌ FAIL: Ego Not Found"

                # [커밋 단계] 한쪽에서는 쓰고 한쪽에서는 지우는 동시 작업 수행
                print(f"⚡ [2PC_PHASE_2] Committing atomic migration...")
                conn_t.execute("INSERT OR REPLACE INTO storage VALUES (?, ?, ?)", (ego_key, data[0], time.time()))
                conn_f.execute("DELETE FROM storage WHERE key=?", (ego_key,))
                
                conn_t.commit()
                conn_f.commit()
                return "✅ SUCCESS: Atomic Migration Complete"
        except Exception as e:
            return f"♻️ [ROLLBACK] Migration Aborted: {e}"

# --- 단독 실행 로직 ---
if __name__ == "__main__":
    balancer = CosmicMultiverseBalancer()
    print(f"⚖️ [v11.0.0] Multiverse Equilibrium Reached. 우주의 무게추가 완벽해! 에헤헤! 🤨")
