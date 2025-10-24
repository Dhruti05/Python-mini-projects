# Canoe Portage Conversion

### Overview
This is a beginner-friendly Python program that performs **unit conversions** based on a distance entered in *rods*.  
It’s inspired by the Boundary Waters Canoe Area (BWCA), where distances between lakes are measured in rods — an old unit of length that’s roughly equal to the size of a canoe.

The program helps calculate how far a portage (canoe-carrying route) is in **meters, feet, miles, and furlongs**, and also estimates the **time it would take to walk** that distance at a normal pace.

---

### What the Program Does
1. Prompts the user to enter a distance (in rods).  
2. Converts that distance into:
   - Meters  
   - Feet  
   - Miles  
   - Furlongs  
3. Calculates the **walking time** for that distance based on an average human speed of 3.1 miles per hour.  
4. Displays all results neatly with formatted output.

---

### Conversion Details

| Unit | Conversion Formula | Explanation |
|------|---------------------|--------------|
| Meters | `rods × 5.0292` | 1 rod = 5.0292 meters |
| Feet | `meters ÷ 0.3048` | 1 foot = 0.3048 meters |
| Miles | `meters ÷ 1609.34` | 1 mile = 1609.34 meters |
| Furlongs | `rods ÷ 40` | 1 furlong = 40 rods |
| Time (minutes) | `(miles ÷ 3.1) × 60` | Average speed = 3.1 miles/hour |

---

### Example Run

**Input:**
Enter distance in rods: 10

**Output:**
Rods: 10.000
Meters: 50.292
Feet: 165.000
Miles: 0.03123
Furlongs: 0.250
Time to walk 10.000 rods: 0.60 minutes


---

### 🧠 Learning Focus
This small project reinforces:
- Using `input()` and `float()` to handle user data  
- Performing arithmetic calculations  
- Displaying results using f-strings and formatted output  
- Building confidence with basic Python syntax  

---

### 📄 File Included
proj1.py
