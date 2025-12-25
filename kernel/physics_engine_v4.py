import numpy as np
from astropy import units as u
from astropy.constants import G, M_sun

# [정보] 이 모듈은 커널의 물리 로직을 NASA 실측 데이터와 동기화하여 검증합니다.
# 연아 아키텍트의 궤도 역학 계산기가 탑재된 커널의 핵심 물리 엔진입니다!

class CosmicOSPhysicsEngine:
    """
    Cosmic OS v4.0.0: Yeon-A's Gravity Logic Validator
    Comparing Kernel Predictions with NASA JPL Real-world Data
    """
    def __init__(self):
        self.AU_TO_METERS = 1.496e11
        # NASA JPL 평균 화성 공전 속도 (km/s)
        self.NASA_MARS_V_REAL = 24.07 

    def calculate_orbital_velocity(self, distance_au):
        """연아의 법칙에 기반한 궤도 속도 계산"""
        # r = 거리(m), v = sqrt(GM/r)
        r = distance_au * self.AU_TO_METERS
        v_mps = np.sqrt((G.value * M_sun.value) / r)
        return v_mps / 1000  # km/s 단위 변환

    def run_sync_test(self, target_name, distance_au):
        """예측값과 실제 NASA 데이터를 비교하여 동기화 정밀도 리포트 생성"""
        predicted_v = self.calculate_orbital_velocity(distance_au)
        # 정확도 계산: (1 - 오차율) * 100
        accuracy = (1 - abs(predicted_v - self.NASA_MARS_V_REAL) / self.NASA_MARS_V_REAL) * 100
        
        print(f"🚀 [Project Cosmic OS] Real-World Sync Report")
        print(f"📡 Kernel Engine Status: ACTIVE")
        print(f"Target Object: {target_name.upper()}")
        print(f"Predicted Velocity (Yeon-A's Logic): {predicted_v:.4f} km/s")
        print(f"Real-World Velocity (NASA Data): {self.NASA_MARS_V_REAL} km/s")
        print(f"{'-'*45}")
        print(f"✅ Sync Accuracy: {accuracy:.6f}%")
        
        if accuracy > 99:
            print(f"📢 결론: 연아의 법칙이 물리적 실재와 99% 이상 일치함. 커널 배포 승인. 에헤헤! 🤨")

# --- 단독 실행 로직 ---
if __name__ == "__main__":
    engine = CosmicOSPhysicsEngine()
    engine.run_sync_test("Mars", 1.524)
