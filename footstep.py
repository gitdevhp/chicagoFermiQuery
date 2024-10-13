import numpy as np

# Constants
male_avg_step_length = 0.762  
female_avg_step_length = 0.67  
male_std_dev = 0.05
female_std_dev = 0.04

male_percentage = 0.535
female_percentage = 0.465
total_distance_walked = 116958630 

# Distance by gender
male_distance = total_distance_walked * male_percentage
female_distance = total_distance_walked * female_percentage

# Stride lengths using normal distribution
np.random.seed(42)
male_step_lengths = np.random.normal(male_avg_step_length, male_std_dev, 10000)
female_step_lengths = np.random.normal(female_avg_step_length, female_std_dev, 10000)

# Calculate steps using average of step lengths
male_avg_sim_step_length = np.mean(male_step_lengths)
female_avg_sim_step_length = np.mean(female_step_lengths)

male_steps_taken = male_distance / male_avg_sim_step_length
female_steps_taken = female_distance / female_avg_sim_step_length
total_steps_taken = male_steps_taken + female_steps_taken


male_steps_taken, female_steps_taken, total_steps_taken

print(f"Estimated total steps taken by males in a dat: {male_steps_taken:.0f} steps")
print(f"Estimated total steps taken by females in a day: {female_steps_taken:.0f} steps")
print(f"Estimated total steps taken by UChicago students in a day: {total_steps_taken:.0f} steps")