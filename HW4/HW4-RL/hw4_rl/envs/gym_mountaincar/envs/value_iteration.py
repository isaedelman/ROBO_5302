import numpy as np
import matplotlib.pyplot as plt
import time
from mountain_car import MountainCarEnv


def discretize(value, v_min, v_max, n_bins):
    """
    Map a continuous value to the nearest discrete bin index.
    Args:
        value: continuous value
        v_min: minimum value of the range
        v_max: maximum value of the range
        n_bins: number of discrete bins
    Returns:
        index: discrete bin index
    """
    # Clip value to range
    value = np.clip(value, v_min, v_max)
    return int(round((value - v_min) / (v_max - v_min) * (n_bins - 1)))


def value_iteration(env, n_pos_bins=21, n_vel_bins=21, gamma=0.99, tol=1e-4):
    """
    Standard Value Iteration for MountainCar environment with
    discretized state space.
    Args:
        env: MountainCar environment
        n_pos_bins: number of discretized position bins
        n_vel_bins: number of discretized velocity bins
        gamma: discount factor
        tol: convergence tolerance
    Returns:
        V: value function array [n_pos_bins, n_vel_bins]
        policy: optimal policy array [n_pos_bins, n_vel_bins]
        pos_bins: discretized position bins
        vel_bins: discretized velocity bins
    """
    # Discretized grid
    pos_bins = np.linspace(env.min_position, env.max_position, n_pos_bins)
    vel_bins = np.linspace(-env.max_speed, env.max_speed, n_vel_bins)

    # Initialize value function and policy
    V = np.zeros((n_pos_bins, n_vel_bins))
    policy = np.zeros((n_pos_bins, n_vel_bins), dtype=int)

    iteration = 0
    performance_history = []
    # Value Iteration Loop
    while True:
        delta = 0
        V_new = np.copy(V)
        # Iterate over all discretized states
        for i, pos in enumerate(pos_bins):
            # Iterate over all discretized velocities
            for j, vel in enumerate(vel_bins):

                # Find best action
                best_value = -np.inf
                best_action = 0

                # Iterate over all actions
                for action in range(env.action_space.n):
                    # Simulate step
                    next_pos, next_vel = pos, vel

                    # Update velocity
                    next_vel += (action - 1) * env.force + np.cos(
                        3 * next_pos
                    ) * (-env.gravity)

                    # Clip velcoity
                    next_vel = np.clip(next_vel, -env.max_speed, env.max_speed)

                    # Update position
                    next_pos += next_vel

                    # Clip position
                    next_pos = np.clip(
                        next_pos, env.min_position, env.max_position
                    )

                    # Prevent going left of min position
                    if next_pos == env.min_position and next_vel < 0:
                        next_vel = 0.0

                    # Get reward and done flag
                    reward = -1.0
                    done = next_pos >= env.goal_position

                    # Map to nearest grid
                    i_next = discretize(
                        next_pos,
                        env.min_position,
                        env.max_position,
                        n_pos_bins,
                    )

                    # Map to nearest grid
                    j_next = discretize(
                        next_vel, -env.max_speed, env.max_speed, n_vel_bins
                    )

                    # Compute value
                    value = reward + gamma * (0 if done else V[i_next, j_next])

                    # Update best action
                    if value > best_value:
                        best_value = value
                        best_action = action

                # Update value function and policy
                V_new[i, j] = best_value
                policy[i, j] = best_action
                delta = max(delta, abs(V_new[i, j] - V[i, j]))

        # Update value function
        V = V_new
        iteration += 1
        performance_history.append(np.mean(V))

        # Print progress
        if iteration % 10 == 0:
            print(f"Iteration {iteration}, max delta = {delta:.6f}")
        if delta < tol:
            break

    print(f"Value iteration converged in {iteration} iterations")
    return V, policy, pos_bins, vel_bins, performance_history


def value_iteration_linear(
    env, n_pos_bins=21, n_vel_bins=21, gamma=0.99, tol=1e-4
):
    """
    Value Iteration with n-linear interpolation for MountainCar environment.
    Args:
        env: MountainCar environment
        n_pos_bins: number of discretized position bins
        n_vel_bins: number of discretized velocity bins
        gamma: discount factor
        tol: convergence tolerance
    Returns:
        V: value function array [n_pos_bins, n_vel_bins]
        policy: optimal policy array [n_pos_bins, n_vel_bins]
        pos_bins: discretized position bins
        vel_bins: discretized velocity bins
    """
    # Discretized grid
    pos_bins = np.linspace(env.min_position, env.max_position, n_pos_bins)
    vel_bins = np.linspace(-env.max_speed, env.max_speed, n_vel_bins)

    # Initialize value function and policy
    V = np.zeros((n_pos_bins, n_vel_bins))
    policy = np.zeros((n_pos_bins, n_vel_bins), dtype=int)

    performance_history = []
    iteration = 0
    while True:
        delta = 0
        V_new = np.copy(V)

        # Iterate over all discretized states
        for i, pos in enumerate(pos_bins):
            # Iterate over all discretized velocities
            for j, vel in enumerate(vel_bins):
                # find best action
                best_value = -np.inf
                best_action = 0

                # iterate over all actions to either
                # 0 move left, 1 no move, 2 move right
                for action in range(env.action_space.n):

                    # simulate step
                    next_pos, next_vel = pos, vel
                    # update velocity
                    next_vel += (action - 1) * env.force + np.cos(
                        3 * next_pos
                    ) * (-env.gravity)

                    # clip velcoity to -0.07 and 0.07
                    next_vel = np.clip(next_vel, -env.max_speed, env.max_speed)

                    # update position
                    next_pos += next_vel

                    # clip position to -1.2 and 0.6
                    next_pos = np.clip(
                        next_pos, env.min_position, env.max_position
                    )

                    # prevent going left of min position
                    if next_pos == env.min_position and next_vel < 0:
                        next_vel = 0.0

                    # get reward and done flag
                    reward = -1.0
                    done = next_pos >= env.goal_position

                    # n-linear interpolation
                    value = reward + gamma * (
                        0
                        if done
                        else bilinear_interpolate(
                            V, pos_bins, vel_bins, next_pos, next_vel
                        )
                    )

                    # update best action
                    if value > best_value:
                        best_value = value
                        best_action = action

                # update value function and policy
                V_new[i, j] = best_value
                policy[i, j] = best_action
                delta = max(delta, abs(V_new[i, j] - V[i, j]))

        # update value function
        V = V_new
        iteration += 1
        performance_history.append(np.mean(V))

        # Print progress
        if iteration % 10 == 0:
            print(f"Iteration {iteration}, max delta = {delta:.6f}")
        if delta < tol:
            break

    print(f"Value iteration (n-linear) converged in {iteration} iterations")
    return V, policy, pos_bins, vel_bins, performance_history


def bilinear_interpolate(V, pos_bins, vel_bins, pos, vel):
    """
    Bilinear interpolation for 2D grid.

    Args:
        V: 2D value function array [n_pos, n_vel]
        pos_bins: discretized position bins
        vel_bins: discretized velocity bins
        pos: continuous position
        vel: continuous velocity

    Returns:
        Interpolated value
    """
    # Find surrounding indices
    i = np.searchsorted(pos_bins, pos) - 1
    j = np.searchsorted(vel_bins, vel) - 1
    i = np.clip(i, 0, len(pos_bins) - 2)
    j = np.clip(j, 0, len(vel_bins) - 2)

    # Fraction along each axis
    t = (pos - pos_bins[i]) / (pos_bins[i + 1] - pos_bins[i])
    u = (vel - vel_bins[j]) / (vel_bins[j + 1] - vel_bins[j])

    # Bilinear interpolation formula
    V00 = V[i, j]
    V01 = V[i, j + 1]
    V10 = V[i + 1, j]
    V11 = V[i + 1, j + 1]

    return (
        (1 - t) * (1 - u) * V00
        + (1 - t) * u * V01
        + t * (1 - u) * V10
        + t * u * V11
    )


def plot_heatmap(V, pos_bins, vel_bins, title="Value Function"):
    plt.figure(figsize=(8, 6))
    X, Y = np.meshgrid(vel_bins, pos_bins)
    plt.contourf(X, Y, V, levels=50, cmap="viridis")
    plt.xlabel("Velocity")
    plt.ylabel("Position")
    plt.title(title)
    plt.colorbar(label="Value")
    plt.show()


def plot_policy_curve(reward_history):
    """
    Plot the learning curve showing policy performance over iterations.

    Args:
        reward_history: List of rewards from each policy evaluation
        filename: Optional path to save the plot
    """
    plt.figure()
    plt.plot(range(len(reward_history)), reward_history)
    plt.xlabel("Iteration")
    plt.ylabel("Return")
    plt.title("Policy Iteration Performance")
    plt.show()
    plt.close()


def run_policy(env, policy, pos_bins, vel_bins, render=True):
    """
    Simulate the MountainCar environment using the learned policy.
    Args:
        env: MountainCar environment
        policy: learned policy array [n_pos_bins, n_vel_bins]
        pos_bins: discretized position bins
        vel_bins: discretized velocity bins
        render: whether to render the environment
    Returns:
        total_reward: total reward obtained during the episode
    """
    # Reset environment
    obs, _ = env.reset()
    total_reward = 0
    done = False

    # Run episode
    for step in range(200):
        # Discretize observation
        pos, vel = obs

        # Get action from policy
        i = discretize(pos, env.min_position, env.max_position, len(pos_bins))
        j = discretize(vel, -env.max_speed, env.max_speed, len(vel_bins))
        action = policy[i, j]

        # Take step
        obs, reward, done, truncated, _ = env.step(action)
        total_reward += reward

        # Render environment
        if render:
            env.render()
            time.sleep(0.02)

        # Check for termination
        if done or truncated:
            print(
                f"Goal reached in: {step+1} steps, total reward value at end: {total_reward}"
            )
            break

    return total_reward


if __name__ == "__main__":

    # Create MountainCar environment
    env = MountainCarEnv()

    # Value iteration
    # Do value iteration fpor 21, 51, and 101 bins
    for n_bins in [21, 51, 101]:
        print(f"Running Value Iteration with {n_bins}x{n_bins} bins...")
        (
            V,
            policy,
            pos_bins,
            vel_bins,
            performance_history,
        ) = value_iteration(env, n_bins, n_bins)
        plot_heatmap(
            V,
            pos_bins,
            vel_bins,
            title=f"MountainCar Value Function ({n_bins}x{n_bins})",
        )
        plot_policy_curve(performance_history)
        # Run animation for the final learned policy
        print("Simulating optimal policy...")
        env_sim = MountainCarEnv()  # fresh env for rendering
        run_policy(env_sim, policy, pos_bins, vel_bins)
        env_sim.close()

    # n-linear interpolation
    # Do n-linear value iteration for 12, 51, and 101 bins
    for n_bins in [21, 51, 101]:
        print(
            f"Running n-linear Value Iteration with {n_bins}x{n_bins} bins..."
        )
        V, policy, pos_bins, vel_bins, performance_history = (
            value_iteration_linear(env, n_bins, n_bins)
        )
        plot_heatmap(
            V,
            pos_bins,
            vel_bins,
            title=f"MountainCar Value Function (n-linear, {n_bins}x{n_bins})",
        )
        plot_policy_curve(performance_history)
        # Run animation for the final learned policy
        print("Simulating optimal policy...")
        env_sim = MountainCarEnv()  # fresh env for rendering
        run_policy(env_sim, policy, pos_bins, vel_bins)
        env_sim.close()
