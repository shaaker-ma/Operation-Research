# Transportation Problem Solver using Linear Programming

This repository focuses on solving the **Transportation Problem**, a key optimization issue in logistics, using **linear programming** techniques. The project minimizes transportation costs between multiple sources (e.g., power plants) and destinations (e.g., cities) while satisfying supply and demand constraints. 

---

## **Project Overview**

- **Objective:** Minimize transportation costs while meeting supply and demand requirements.
- **Approach:** Use mathematical optimization to model and solve the transportation problem.
- **Real-world Application:** Power distribution planning between power plants and cities.

---

## **Features**

- Selection of cities and power plants using real-world data from Google Maps and OpenInfraMap.
- Distance-based cost calculation between sources and destinations.
- Linear programming-based solution to achieve optimal cost minimization.
- Detailed analysis of results and insights into the transportation problem.

---

## **Project Structure**

1. **`Section A: Cities and Power Plants`**
   - Selection of cities using Google Maps.
   - Identification of power plants using OpenInfraMap.
   - Visualization of locations for better context.

2. **`Section B: Distance Measurement`**
   - Calculation of distances between cities and power plants using geospatial tools.

3. **`Section C: Dataset Generation`**
   - Creation of datasets with supply, demand, and cost matrices for modeling the problem.

4. **`Section D: Cost Definition`**
   - Definition of transportation costs based on calculated distances and fixed rates.

5. **`Section E: Solution & Code`**
   - Python implementation of linear programming to solve the transportation problem.
   - Includes code for finding the initial feasible solution and the optimal solution.

6. **`Section F: Analysis`**
   - Insights and interpretations of the optimization results.

7. **`Section G: Resources`**
   - References and tools used for data collection and modeling.
