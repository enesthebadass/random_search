# random_search
# Random Search for Function Minimization

This repository contains a Python implementation of a **random search algorithm** to find the minimum value of the function:

g(w) = sin(3w) + 0.3 * w²

## Overview
The script randomly samples values of **w** within a specified range and evaluates the function **g(w)** at each point. It then selects the value of **w** that results in the minimum function value.

## Features
- Uses **random search** to optimize the function
- Plots the function and the identified minimum point
- Customizable number of random samples and range of **w**

## Requirements
The script requires the following Python libraries:

```bash
pip install numpy matplotlib
```

## Usage
Run the script using Python:

```bash
python random_search_g.py
```

### Parameters
You can modify these parameters inside the script:
- **num_points**: Number of random points to evaluate (default: 2000)
- **w_min, w_max**: Search range for **w** (default: -5 to 5)
- **seed**: Random seed for reproducibility (default: 42)

## Example Output
```bash
Random Search Result
--------------------
Best w: -1.23
Best g(w) value: -0.89
```

## Visualization
The script generates a plot showing:
- The function **g(w)** over the given range
- The minimum point found by the random search (marked in red)

## License
This project is open-source and available under the **MIT License**.

## Author
Developed by Enes Yüksel

