# Project 02 – Earthquake Energy Calculator

This project is a simple Python program that calculates the amount of energy released by an earthquake based on its **Richter scale magnitude**.  
It converts that energy into both **joules** and the equivalent **tons of TNT**, helping visualize how powerful different earthquakes are.

---

## Project Overview
The **Richter scale** measures the magnitude of an earthquake.  
Energy released increases exponentially with magnitude — a difference of 1.0 represents roughly **31.6 times more energy**.

The energy released (in joules) is calculated using the formula:

\[
E = 10^{(1.5 \times M + 4.8)}
\]

where:
- `E` = energy released (in joules)  
- `M` = magnitude on the Richter scale  

To convert joules into tons of TNT:
\[
1 \text{ ton of TNT} = 4.184 \times 10^9 \text{ joules}
\]

---

## Features
- Calculates energy released for given Richter scale values.
- Displays energy both in **joules** and **tons of TNT**.
- Includes known historical earthquake magnitudes:
  - 9.1 – Indonesia (2004)  
  - 9.2 – Alaska (1964)  
  - 9.5 – Chile (1960)  
- Accepts custom input from the user.
- Handles invalid input gracefully.

---

##  Example Output

============================
EARTHQUAKE ENERGY CALCULATOR
============================

Richter scale value: 1.0
Energy released: 6.31e+06 joules
Equivalent to: 1.51e-03 tons of TNT

Richter scale value: 9.1
Energy released: 1.99e+18 joules
Equivalent to: 4.76e+08 tons of TNT

Enter a Richter scale value to calculate energy: 5
Richter scale value: 5.0
Energy released: 1.99e+12 joules
Equivalent to: 4.76e+02 tons of TNT

````

---

## Learning Outcomes
Through this project, I practiced:
- Using **functions** in Python for cleaner code.
- Applying **mathematical formulas** in real-world scenarios.
- Handling **user input and exceptions** (`try` / `except`).
- Formatting output for clarity using **f-strings** and **scientific notation**.

---

## File Structure

```
proj01/
│
├── proj1.py       # Main Python script
└── README.md       # Project documentation
```

---
