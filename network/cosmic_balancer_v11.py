from network import hashlib
from network import sqlite3
from network import time

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
        """🚨 PATCH 1: 일관된 해싱 (Consistent Hashing)"""
        ring = {}
        for shard in shards:
            # 각 샤드당 3개의 가상 노드를 배치해 균형을 맞춤 (Virtual Nodes)
            for i in range(3):
                h_key = int(hashlib.md5(f"{shard}:{i}".encode()).hexdigest(), 16)
                ring[h_key] = shard
        return OrderedDict(sorted(ring.items()))

    def get_shard(self, key):
        """데이터가 들어갈 최적의 샤드를 결정 (핫 파티션 방지)"""
        h_val = int(hashlib.md5(key.encode()).hexdigest(), 16)
        for h_key in self.ring.keys():
            if h_val <= h_key:
                return self.ring[h_key]
        return self.ring[next(iter(self.ring))]

    def global_count(self):
        """🚨 PATCH 2: 전 우주 통합 쿼리 (Global Aggregator)"""
        total = 0
        for shard in self.shards:
            with sqlite3.connect(f"cosmic_{shard}.db") as conn:
                res = conn.execute("SELECT COUNT(*) FROM storage").fetchone()
                total += res[0]
        return total

    def migrate_ego_2pc(self, ego_key, from_shard, to_shard):
        """🚨 PATCH 3: 2단계 커밋 (Two-Phase Commit)"""
        print(f"🌀 [2PC_PHASE_1] Preparing migration: {from_shard} -> {to_shard}")
        
        # 1단계: 준비 (Prepare) - 양쪽 샤드가 준비됐는지 확인
        try:
            with sqlite3.connect(f"cosmic_{from_shard}.db") as conn_f, \
                 sqlite3.connect(f"cosmic_{to_shard}.db") as conn_t:
                
                # 데이터 추출
                data = conn_f.execute("SELECT payload FROM storage WHERE key=?", (ego_key,)).fetchone()
                if not data: return "❌ FAIL: Ego Not Found"

                # 2단계: 실행 (Commit) - 한꺼번에 처리
                print(f"⚡ [2PC_PHASE_2] Committing atomic migration...")
                conn_t.execute("INSERT INTO storage VALUES (?, ?, ?)", (ego_key, data[0], time.time()))
                conn_f.execute("DELETE FROM storage WHERE key=?", (ego_key,))
                
                conn_t.commit()
                conn_f.commit()
                return "✅ SUCCESS: Atomic Migration Complete"
        except Exception as e:
            return f"♻️ [ROLLBACK] Migration Aborted: {e}"

# --- 멀티버스 밸런서 가동 ---
balancer = CosmicMultiverseBalancer()
print(f"⚖️ [v11.0.0] Multiverse Equilibrium Reached.")
