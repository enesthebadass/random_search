import numpy as np
import matplotlib.pyplot as plt

def g(w):
    """
    Function to be minimized.
    g(w) = sin(3w) + 0.3 * w^2
    """
    return np.sin(3*w) + 0.3*(w**2)

def random_search_g(num_points=1000, w_min=-5.0, w_max=5.0, seed=None):
    """
    Performs random search to find the minimum value of g(w).
    
    Parameters:
    num_points:   Number of random points to test.
    w_min, w_max: Lower and upper bounds for w.
    seed:         Random seed (use a fixed value for reproducibility).
    
    Returns:
    best_w:  The w value that minimizes g(w).
    best_val: The corresponding minimum function value.
    """
    if seed is not None:
        np.random.seed(seed)
    
    best_w = None
    best_val = float('inf') # Initialize with a very large value

    for _ in range(num_points):
        # Select a random w in the given range
        w_candidate = np.random.uniform(w_min, w_max)
        # Compute function value
        val = g(w_candidate)

        # Update best values if a new minimum is found
        if val < best_val:
            best_val = val
            best_w = w_candidate

    return best_w, best_val

if __name__ == "__main__":
    num_points = 2000  # Number of random points to sample
    w_min, w_max = -5, 5  # Search space limits
    seed = 42  # Set seed for reproducibility

    # Perform random search optimization
    w_opt, g_opt = random_search_g(num_points=num_points,
                                   w_min=w_min,
                                   w_max=w_max,
                                   seed=seed)
    
    # Print the results
    print("Random Search Result")
    print("--------------------")
    print(f"Best w: {w_opt:.4f}")
    print(f"g(w) value: {g_opt:.4f}")

    # Generate values for plotting the function
    w_vals = np.linspace(w_min, w_max, 400)  # 400 points in range [-5,5]
    g_vals = [g(w) for w in w_vals]  # Compute g(w) for each w

    # Plot the function and the found optimum point
    plt.figure(figsize=(8, 5))
    plt.plot(w_vals, g_vals, label=r"$g(w) = \sin(3w) + 0.3\,w^2$")

    # Mark the best found point on the graph
    plt.plot(w_opt, g_opt, "ro", label=f"Minimum Found (w={w_opt:.2f})")

    # Customize plot appearance
    plt.title("Minimization of g(w) Using Random Search")
    plt.xlabel("w")
    plt.ylabel("g(w)")
    plt.legend()
    plt.grid(True)
    plt.show()
