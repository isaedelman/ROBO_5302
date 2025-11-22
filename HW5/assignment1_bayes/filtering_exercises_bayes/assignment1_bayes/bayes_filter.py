from typing import List, Tuple

import numpy as np

from filtering_exercises_bayes.environments import GridWorld


class BayesFilter:
    """
    Bayes Filter implementation for GridWorld localization.
    Maintains and updates a belief state over all possible grid positions.
    """

    def __init__(self, env: GridWorld):
        self.env = env
        self.grid_size = env.size

        # Initialize uniform belief over all free spaces
        self.belief = np.zeros(self.grid_size)
        free_spaces = env.grid == 0
        self.belief[free_spaces] = 1.0 / np.sum(free_spaces)

        # Motion model parameters
        self.motion_noise = 0.2  # Probability of failing to execute action

        # Measurement model parameters
        self.measurement_noise = 0.5  # Probability of incorrect sensor reading
        self.measurement_tolerance = (
            1.0  # Distance tolerance for matching readings
        )

    def predict(self, action: int):
        """
        Implement the Bayes Filter prediction step.

        This method should implement the prediction step of the Bayes filter
        by applying the motion model to update beliefs about the robot's
        position. The motion model should account for uncertainty in the
        robot's heading and possibility of failed actions.

        Implementation steps:
        1. Create a new belief array to store updated beliefs:
           - Initialize with zeros: new_belief = np.zeros_like(self.belief)

        2. For each cell (i,j) in the grid with non-zero belief:
           - If action is forward (action == 0):
             * Consider all possible headings (right, up, left, down)
             * For each heading:
               - Calculate next position based on heading
               - If move is valid (in bounds and not obstacle):
                 * Add probability of successful move to new position
                 * Add probability of failed move to current position
             * Use self.motion_noise for probability of failed move
             * Use (1 - self.motion_noise) for probability of successful move
             * Assume uniform distribution over headings (0.25 each)
           - If action is turn (action != 0):
             * Simply copy current belief (no position change)

        3. Normalize the new belief:
           - If sum is positive, divide by sum
           - Store result in self.belief

        Key variables:
        - self.belief: Current belief state (2D array)
        - self.grid_size: Size of the grid world
        - self.env.grid: Grid world map (0 for free, 1 for obstacle)
        - self.motion_noise: Probability of failing to execute action

        Parameters:
            action (int): 0 (forward), 1 (turn right), 2 (turn left)
        """
        # Initialize new belief array of zeros
        new_belief = np.zeros_like(self.belief)

        # Update beliefs based on action
        # Iterate over each cell in the grid
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):

                # Only consider cells with non-zero belief
                if self.belief[i, j] > 0:

                    # Handle forward action
                    if action == 0:  # Move forward

                        # Consider all possible headings
                        for heading in range(4):

                            # right, up, left, down
                            moves = [
                                (0, 1),
                                (-1, 0),
                                (0, -1),
                                (1, 0),
                            ]

                            # Calculate next position
                            move = moves[heading]
                            next_pos = (i + move[0], j + move[1])

                            # Check if move is valid
                            if (
                                0 <= next_pos[0] < self.grid_size[0]
                                and 0 <= next_pos[1] < self.grid_size[1]
                                and self.env.grid[next_pos[0], next_pos[1]]
                                == 0
                            ):
                                # Successful move to next position
                                new_belief[next_pos] += (
                                    self.belief[i, j]
                                    * (1 - self.motion_noise)
                                    * 0.25
                                )

                                # Failed move stays in the same position
                                new_belief[i, j] += (
                                    self.belief[i, j]
                                    * self.motion_noise
                                    * 0.25
                                )
                            else:
                                # If move is invalid, stay in the same position
                                new_belief[i, j] += (
                                    self.belief[i, j]
                                    * (1 - self.motion_noise)
                                    * 0.25
                                )
                                new_belief[i, j] += (
                                    self.belief[i, j]
                                    * self.motion_noise
                                    * 0.25
                                )
                    # Handle turn actions (no position change)
                    else:
                        new_belief[i, j] += self.belief[i, j]

        # Normalize new belief
        total = np.sum(new_belief)
        # Update belief
        if total > 0:
            # Normalize
            self.belief = new_belief / total
        else:
            # If total is zero, keep the new belief as is
            self.belief = new_belief

    def update(self, readings: np.ndarray):
        """
        Implement the Bayes Filter update step.

        This method should implement the update step of the Bayes filter using
        sensor readings. It should update beliefs based on how well the actual
        readings match the expected readings for each possible position and
        heading.

        Implementation steps:
        1. Create a likelihood array:
           - Initialize with ones: likelihood = np.ones_like(self.belief)

        2. For each free cell (i,j) in the grid:
           - For each possible heading (0-3):
             * Get expected readings using self._get_expected_readings((i,j),
             heading)
             * Compare with actual readings:
               - For each pair of expected and actual readings:
                 * If difference < self.measurement_tolerance:
                   - Multiply by (1 - self.measurement_noise)
                 * Else:
                   - Use scaled noise: self.measurement_noise * (1.0 /
                   (1.0 + |diff|))
             * Average likelihood over all headings (multiply by 0.25)
           - Store final likelihood in likelihood array

        3. Update belief:
           - Multiply current belief by likelihood
           - Normalize if sum is positive

        Key variables:
        - self.belief: Current belief state (2D array)
        - self.grid_size: Size of the grid world
        - self.env.grid: Grid world map (0 for free, 1 for obstacle)
        - self.measurement_noise: Probability of incorrect sensor reading
        - self.measurement_tolerance: Distance tolerance for matching readings

        Parameters:
            readings (np.ndarray): Array of sensor readings (distances) in
            each direction
        """
        # Create likelihood array of ones
        likelihood = np.ones_like(self.belief)

        # Update likelihoods based on sensor readings
        # Iterate over each cell in the grid
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):

                # Only consider free cells
                if self.env.grid[i, j] == 0:

                    # Initialize total likelihood for this cell
                    total_likelihood = 0.0

                    # Consider all possible headings
                    for heading in range(4):

                        # Get expected readings for this position and heading
                        expected_readings = self._get_expected_readings(
                            (i, j), heading
                        )
                        prob = 1.0  # Initialize probability for this heading

                        # Compare expected and actual readings
                        # zip does the pairing
                        for exp, act in zip(expected_readings, readings):
                            diff = abs(exp - act)

                            # Update probability based on measurement model
                            if diff < self.measurement_tolerance:
                                prob *= 1 - self.measurement_noise
                            else:
                                prob *= self.measurement_noise * (
                                    1.0 / (1.0 + diff)
                                )

                        # Average over headings
                        total_likelihood += prob * 0.25

                    # Store final likelihood for this cell
                    likelihood[i, j] = total_likelihood

        # Update belief with likelihood
        self.belief *= likelihood

        # Normalize belief
        total = np.sum(self.belief)
        if total > 0:
            self.belief /= total

    def _get_expected_readings(
        self, pos: Tuple[int, int], heading: int
    ) -> np.ndarray:
        """Get expected sensor readings for a given position and heading."""
        readings = np.zeros(self.env.n_beams)
        moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down

        # For each beam
        for i in range(self.env.n_beams):
            beam_dir = (heading + i) % 4
            move = moves[beam_dir]

            # Cast ray until hitting obstacle or boundary
            curr_pos = list(pos)
            distance = 0

            while True:
                curr_pos[0] += move[0]
                curr_pos[1] += move[1]
                distance += 1

                # Check if out of bounds
                if not (
                    0 <= curr_pos[0] < self.grid_size[0]
                    and 0 <= curr_pos[1] < self.grid_size[1]
                ):
                    break

                # Check if hit obstacle
                if self.env.grid[curr_pos[0], curr_pos[1]] == 1:
                    break

            readings[i] = distance

        return readings

    def get_most_likely_state(self) -> Tuple[int, int]:
        """Return the most likely state (position) based on current belief."""
        idx = np.argmax(self.belief)
        return (idx // self.grid_size[1], idx % self.grid_size[1])

    def get_belief(self) -> np.ndarray:
        """Return the current belief state."""
        return self.belief.copy()
