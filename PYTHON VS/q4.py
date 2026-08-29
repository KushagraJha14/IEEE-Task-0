import numpy as np

hours_studied = np.array([4.5, 6.0, 3.5, 8.0, 5.5])
attendance = np.array([85, 92, 78, 95, 88])
previous_scores = np.array([72, 80, 65, 88, 75])
final_scores = np.array([70, 91, 58, 87, 76])

print(f"Hours Studied: Shape={hours_studied.shape}, Dtype={hours_studied.dtype}")
print(f"Attendance: Shape={attendance.shape}, Dtype={attendance.dtype}")
print(f"Previous Scores: Shape={previous_scores.shape}, Dtype={previous_scores.dtype}")
print(f"Final Scores: Shape={final_scores.shape}, Dtype={final_scores.dtype}")

print(f"Mean Final Score: {np.mean(final_scores)}")
print(f"Max Final Score: {np.max(final_scores)}")
print(f"Min Final Score: {np.min(final_scores)}")
print(f"Std Dev of Final Scores: {np.std(final_scores)}")

bonus_scores = final_scores + 5
print(f"Scores with bonus: {bonus_scores}")

mask = final_scores >= 75
print(f"Boolean array (>= 75): {mask}")

print(f"Scores >= 75: {final_scores[mask]}")