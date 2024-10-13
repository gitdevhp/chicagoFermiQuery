import numpy as np

# Total students at UChicago and distribution by major
total_students = 18000

humanities_students = int(0.20 * total_students)
physical_sciences_students = int(0.21 * total_students)
biological_sciences_students = int(0.18 * total_students)
social_sciences_students = int(0.23 * total_students)
professional_students = int(0.18 * total_students)
others_students = total_students - (humanities_students + physical_sciences_students + 
                                    biological_sciences_students + social_sciences_students + 
                                    professional_students)

# Define student distribution per major
student_distribution = {
    "Humanities": humanities_students,
    "Physical Sciences": physical_sciences_students,
    "Biological Sciences": biological_sciences_students,
    "Social Sciences": social_sciences_students,
    "Professional Schools": professional_students,
    "Others": others_students,
}

print("Student Distribution:", student_distribution)

# approx distances between buildings in meters
distances = {
    ("Rosenwald Hall", "Classics Building"): 200,
    ("Classics Building", "Wieboldt Hall"): 150,
    ("Eckhart Hall", "Jones Laboratory"): 100,
    ("Jones Laboratory", "Kersten Physics Teaching Center"): 120,
    ("Biological Sciences Learning Center", "Knapp Center for Biomedical Discovery"): 80,
    ("Saieh Hall", "Social Sciences Research Building"): 90,
    ("Harper Memorial Library", "Saieh Hall"): 60,
    ("Booth School of Business", "Harris School of Public Policy"): 110,
    ("University of Chicago Law School", "Booth School of Business"): 130,
}

# List all buildings
buildings = [
    "Rosenwald Hall",
    "Classics Building",
    "Wieboldt Hall",
    "Eckhart Hall",
    "Jones Laboratory",
    "Kersten Physics Teaching Center",
    "Biological Sciences Learning Center",
    "Knapp Center for Biomedical Discovery",
    "Saieh Hall",
    "Social Sciences Research Building",
    "Harper Memorial Library",
    "Booth School of Business",
    "Harris School of Public Policy",
    "University of Chicago Law School"
]

# Transition probabilities for each building
transition_matrix = {
    "Rosenwald Hall": [0.2, 0.3, 0.1, 0.1, 0.1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Classics Building": [0.2, 0.4, 0, 0.1, 0.1, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Wieboldt Hall": [0.1, 0.1, 0, 0.1, 0.1, 0.6, 0, 0, 0, 0, 0, 0, 0, 0],
    "Eckhart Hall": [0, 0.3, 0.4, 0, 0.2, 0.1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Jones Laboratory": [0, 0.1, 0.4, 0, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Kersten Physics Teaching Center": [0, 0, 0.5, 0.2, 0.2, 0.1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Biological Sciences Learning Center": [0, 0.2, 0.6, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Knapp Center for Biomedical Discovery": [0, 0, 0.7, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Saieh Hall": [0, 0.1, 0, 0.5, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Social Sciences Research Building": [0, 0, 0, 0.4, 0.2, 0.4, 0, 0, 0, 0, 0, 0, 0, 0],
    "Harper Memorial Library": [0, 0, 0, 0.1, 0.3, 0.6, 0, 0, 0, 0, 0, 0, 0, 0],
    "Booth School of Business": [0.1, 0.2, 0, 0.2, 0.3, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
    "Harris School of Public Policy": [0, 0.1, 0, 0.3, 0.5, 0.1, 0, 0, 0, 0, 0, 0, 0, 0],
    "University of Chicago Law School": [0, 0.1, 0, 0.3, 0.4, 0.2, 0, 0, 0, 0, 0, 0, 0, 0],
}

# Adjust the number of probabilities in each building
for building in buildings:
    if len(transition_matrix[building]) != len(buildings):
        raise ValueError(f"Transition probabilities for {building} doesn't match the number of buildings.")

# Monte Carlo parameters
num_simulations = 100
num_c= 5

# Simulates student movement
def simulate_student_movement(min_moves=5, max_moves=10):  # Allow a student to make multiple moves
    total_distance = 0
    current_building = np.random.choice(buildings)
    num_moves = np.random.randint(min_moves, max_moves + 1)

    for _ in range(num_moves):
        transitions = transition_matrix[current_building]
        building_transit_to = np.random.choice(buildings, p=transitions)
        if building_transit_to != current_building:
            distance_between = distances.get((current_building, building_transit_to), 0)
            if distance_between == 0:
                distance_between = distances.get((building_transit_to, current_building), 0)
            total_distance += distance_between
            current_building = building_transit_to
    return total_distance


total_distances = []
for _ in range(num_simulations):
    total_distance = 0
    print("Simulation:", _)
    for major, count in student_distribution.items():
        for _ in range(count):
            total_distance += simulate_student_movement() * num_c
    total_distances.append(total_distance)

# Calculate the average total distance
average_total_distance = np.mean(total_distances)

print(f"Estimated total distance walked by UChicago students in a day: {average_total_distance:.2f} meters")
