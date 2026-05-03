import math
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class RocketParams:
    """พารามิเตอร์ของจรวด"""
    mass: float = 1.0  # มวลรวม (kg)
    drag_coefficient: float = 0.75  # ค่าสัมประสิทธิ์แรงต้าน
    cross_sectional_area: float = 0.008  # พื้นที่หน้าตัด (m²) - ขวด 1.5L
    initial_velocity: float = 22.0  # ความเร็วต้น (m/s)
    
@dataclass
class EnvironmentParams:
    """พารามิเตอร์สิ่งแวดล้อม"""
    air_density: float = 1.225  # ความหนาแน่นอากาศ (kg/m³)
    gravity: float = 9.81  # ความเร่งโน้มถ่วง (m/s²)
    wind_speed: float = 0.0  # ความเร็วลม (m/s)
    wind_direction: float = 0.0  # ทิศทางลม (องศา, 0=ตรง, 90=ข้าง)

class WaterRocketCalculator:
    def __init__(self, rocket: RocketParams, environment: EnvironmentParams):
        self.rocket = rocket
        self.env = environment
        
    def calculate_drag_force(self, velocity: float) -> float:
        """คำนวณแรงต้านอากาศ"""
        return 0.5 * self.env.air_density * self.rocket.drag_coefficient * \
               self.rocket.cross_sectional_area * velocity**2
    
    def wind_effect(self, time: float) -> Tuple[float, float]:
        """คำนวณผลกระทบของลม"""
        wind_x = self.env.wind_speed * math.cos(math.radians(self.env.wind_direction)) * time
        wind_y = self.env.wind_speed * math.sin(math.radians(self.env.wind_direction)) * time
        return wind_x, wind_y
    
    def simulate_trajectory(self, launch_angle: float, time_step: float = 0.01) -> Tuple[List[float], List[float], List[float]]:
        """จำลองวิถีการบิน"""
        angle_rad = math.radians(launch_angle)
        
        # ความเร็วเริ่มต้น
        vx = self.rocket.initial_velocity * math.cos(angle_rad)
        vy = self.rocket.initial_velocity * math.sin(angle_rad)
        
        # ตำแหน่งเริ่มต้น
        x, y = 0.0, 0.0
        t = 0.0
        
        # เก็บข้อมูลวิถี
        trajectory_x = [x]
        trajectory_y = [y]
        trajectory_t = [t]
        
        while y >= 0:  # จนกว่าจรวดจะกลับมาถึงพื้น
            # คำนวณความเร็วรวม
            v_total = math.sqrt(vx**2 + vy**2)
            
            # คำนวณแรงต้านอากาศ
            drag = self.calculate_drag_force(v_total)
            
            # แรงต้านในแต่ละทิศทาง
            if v_total > 0:
                drag_x = drag * (vx / v_total) / self.rocket.mass
                drag_y = drag * (vy / v_total) / self.rocket.mass
            else:
                drag_x = drag_y = 0
            
            # อัปเดตความเร็ว (รวมแรงโน้มถ่วงและแรงต้าน)
            vx -= drag_x * time_step
            vy = vy - (self.env.gravity + drag_y) * time_step
            
            # อัปเดตตำแหน่ง
            x += vx * time_step
            y += vy * time_step
            t += time_step
            
            # เก็บข้อมูล
            trajectory_x.append(x)
            trajectory_y.append(y)
            trajectory_t.append(t)
        
        return trajectory_x, trajectory_y, trajectory_t
    
    def calculate_range_with_wind(self, launch_angle: float) -> Tuple[float, float, float]:
        """คำนวณระยะยิงรวมผลกระทบของลม"""
        trajectory_x, trajectory_y, trajectory_t = self.simulate_trajectory(launch_angle)
        
        # หาจุดที่จรวดตกถึงพื้น
        landing_time = trajectory_t[-1]
        landing_x = trajectory_x[-1]
        
        # ผลกระทบของลม
        wind_x, wind_y = self.wind_effect(landing_time)
        
        # ตำแหน่งจริงที่ตกลง
        final_x = landing_x + wind_x
        final_y = wind_y
        
        return final_x, final_y, landing_time
    
    def find_optimal_angle_for_target(self, target_distance: float, tolerance: float = 0.1) -> float:
        """หามุมยิงที่เหมาะสมสำหรับระยะเป้าหมาย"""
        best_angle = 45.0
        best_error = float('inf')
        
        # ค้นหามุมที่ดีที่สุด
        for angle in np.arange(20, 70, 0.5):
            range_x, range_y, _ = self.calculate_range_with_wind(angle)
            actual_distance = math.sqrt(range_x**2 + range_y**2)
            error = abs(actual_distance - target_distance)
            
            if error < best_error:
                best_error = error
                best_angle = angle
                
            if error < tolerance:
                break
        
        return best_angle
    
    def calculate_wind_compensation(self, target_distance: float, target_angle: float = 0) -> Tuple[float, float]:
        """คำนวณการชดเชยทิศทางเพื่อต้านลม"""
        # คำนวณผลกระทบของลมที่ระยะเป้าหมาย
        estimated_time = target_distance / (self.rocket.initial_velocity * 0.7)  # ประมาณการ
        wind_x, wind_y = self.wind_effect(estimated_time)
        
        # คำนวณมุมชดเชย
        compensation_angle = math.degrees(math.atan2(-wind_y, -wind_x))
        compensation_distance = math.sqrt(wind_x**2 + wind_y**2)
        
        return compensation_angle, compensation_distance
    
    def get_shooting_recommendation(self, target_distance: float) -> dict:
        """ให้คำแนะนำการยิง"""
        # หามุมที่เหมาะสม
        optimal_angle = self.find_optimal_angle_for_target(target_distance)
        
        # คำนวณการชดเชยลม
        wind_compensation_angle, wind_compensation_distance = self.calculate_wind_compensation(target_distance)
        
        # คำนวณระยะจริงด้วยมุมที่เหมาะสม
        final_x, final_y, flight_time = self.calculate_range_with_wind(optimal_angle)
        actual_distance = math.sqrt(final_x**2 + final_y**2)
        
        return {
            'optimal_angle': optimal_angle,
            'predicted_distance': actual_distance,
            'landing_x': final_x,
            'landing_y': final_y,
            'flight_time': flight_time,
            'wind_compensation_angle': wind_compensation_angle,
            'wind_compensation_distance': wind_compensation_distance,
            'accuracy_error': abs(actual_distance - target_distance)
        }
    
    def plot_trajectory(self, launch_angle: float, target_distance: float = None):
        """วาดกราฟวิถีการบิน"""
        trajectory_x, trajectory_y, trajectory_t = self.simulate_trajectory(launch_angle)
        
        plt.figure(figsize=(12, 8))
        
        # วิถีการบิน
        plt.subplot(2, 1, 1)
        plt.plot(trajectory_x, trajectory_y, 'b-', linewidth=2, label=f'วิถีการบิน (มุม {launch_angle}°)')
        plt.axhline(y=0, color='brown', linestyle='-', alpha=0.3, label='พื้นดิน')
        
        if target_distance:
            plt.axvline(x=target_distance, color='red', linestyle='--', alpha=0.7, label=f'เป้าหมาย {target_distance}m')
        
        # แสดงจุดตกลง
        final_x, final_y, _ = self.calculate_range_with_wind(launch_angle)
        plt.plot(final_x, final_y, 'ro', markersize=8, label=f'จุดตกลง ({final_x:.1f}m)')
        
        plt.xlabel('ระยะทาง (เมตร)')
        plt.ylabel('ความสูง (เมตร)')
        plt.title('วิถีการบินของจรวดขวดน้ำ')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # กราฟความเร็ว
        plt.subplot(2, 1, 2)
        velocities = []
        for i in range(len(trajectory_x)-1):
            dx = trajectory_x[i+1] - trajectory_x[i]
            dy = trajectory_y[i+1] - trajectory_y[i]
            dt = trajectory_t[i+1] - trajectory_t[i]
            v = math.sqrt((dx/dt)**2 + (dy/dt)**2) if dt > 0 else 0
            velocities.append(v)
        
        plt.plot(trajectory_t[:-1], velocities, 'g-', linewidth=2, label='ความเร็ว')
        plt.xlabel('เวลา (วินาที)')
        plt.ylabel('ความเร็ว (m/s)')
        plt.title('ความเร็วตลอดการบิน')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        plt.show()

# ตัวอย่างการใช้งาน
def main():
    print("🚀 โปรแกรมคำนวณการยิงจรวดขวดน้ำ 🚀")
    print("="*50)
    
    # กำหนดพารามิเตอร์จรวด
    rocket = RocketParams(
        mass=0.8,  # กิโลกรัม (ขวด + น้ำ + ครีบ)
        drag_coefficient=0.75,
        cross_sectional_area=0.008,  # ขวด 1.5L
        initial_velocity=22.0  # m/s
    )
    
    # กำหนดสภาพแวดล้อม
    environment = EnvironmentParams(
        air_density=1.225,
        gravity=9.81,
        wind_speed=2.0,  # ลม 2 m/s
        wind_direction=45  # ลมเฉียง 45 องศา
    )
    
    # สร้างเครื่องคำนวณ
    calculator = WaterRocketCalculator(rocket, environment)
    
    # เป้าหมาย 50 เมตร
    target = 50.0
    
    # คำนวณคำแนะนำ
    recommendation = calculator.get_shooting_recommendation(target)
    
    print(f"เป้าหมาย: {target} เมตร")
    print(f"สภาพลม: {environment.wind_speed} m/s ทิศทาง {environment.wind_direction}°")
    print()
    print("🎯 คำแนะนำการยิง:")
    print(f"   มุมยิงที่เหมาะสม: {recommendation['optimal_angle']:.1f}°")
    print(f"   ระยะที่คาดว่าจะยิงได้: {recommendation['predicted_distance']:.1f} เมตร")
    print(f"   จุดตกลง X: {recommendation['landing_x']:.1f} เมตร")
    print(f"   จุดตกลง Y: {recommendation['landing_y']:.1f} เมตร")
    print(f"   เวลาบิน: {recommendation['flight_time']:.1f} วินาที")
    print(f"   ความคลาดเคลื่อน: {recommendation['accuracy_error']:.1f} เมตร")
    print()
    print("🌪️ การชดเชยลม:")
    print(f"   มุมชดเชย: {recommendation['wind_compensation_angle']:.1f}°")
    print(f"   ระยะชดเชย: {recommendation['wind_compensation_distance']:.1f} เมตร")
    
    # เปรียบเทียบกับกรณีไม่มีลม
    no_wind_env = EnvironmentParams(wind_speed=0, wind_direction=0)
    no_wind_calc = WaterRocketCalculator(rocket, no_wind_env)
    no_wind_rec = no_wind_calc.get_shooting_recommendation(target)
    
    print()
    print("📊 เปรียบเทียบ (ไม่มีลม vs มีลม):")
    print(f"   มุมยิง: {no_wind_rec['optimal_angle']:.1f}° → {recommendation['optimal_angle']:.1f}°")
    print(f"   ระยะยิง: {no_wind_rec['predicted_distance']:.1f}m → {recommendation['predicted_distance']:.1f}m")
    
    # วาดกราฟ
    calculator.plot_trajectory(recommendation['optimal_angle'], target)

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()

# ฟังก์ชันเสริมสำหรับการปรับแต่งพารามิเตอร์
def optimize_rocket_parameters(target_distance: float):
    """หาพารามิเตอร์จรวดที่เหมาะสมสำหรับระยะเป้าหมาย"""
    best_config = None
    best_accuracy = float('inf')
    
    # ทดลองพารามิเตอร์ต่างๆ
    masses = [0.6, 0.8, 1.0, 1.2]  # มวลต่างๆ
    velocities = [18, 20, 22, 24, 26]  # ความเร็วต่างๆ
    
    for mass in masses:
        for velocity in velocities:
            rocket = RocketParams(mass=mass, initial_velocity=velocity)
            env = EnvironmentParams()
            calc = WaterRocketCalculator(rocket, env)
            
            rec = calc.get_shooting_recommendation(target_distance)
            
            if rec['accuracy_error'] < best_accuracy:
                best_accuracy = rec['accuracy_error']
                best_config = {
                    'mass': mass,
                    'velocity': velocity,
                    'angle': rec['optimal_angle'],
                    'accuracy': rec['accuracy_error']
                }
    
    return best_config

# ตัวอย่างการหาพารามิเตอร์ที่เหมาะสม
print("\n" + "="*50)
print("🔧 การหาพารามิเตอร์ที่เหมาะสมสำหรับ 50 เมตร")
best = optimize_rocket_parameters(50.0)
print(f"การกำหนดค่าที่ดีที่สุด:")
print(f"   มวล: {best['mass']} kg")
print(f"   ความเร็วต้น: {best['velocity']} m/s")
print(f"   มุมยิง: {best['angle']:.1f}°")
print(f"   ความแม่นยำ: ±{best['accuracy']:.2f} เมตร")