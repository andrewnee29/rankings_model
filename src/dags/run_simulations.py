import pandas as pd
from ..tasks.run_simulations import (Multi_Simulator,
                                     bracket_keys,
                                     )
from ..configs.run_simulations import (TEAM_RANKING_DATA_PATH,
                                       OPEN_POOLS,
                                       EXPORT_FILENAME,
                                       )


def main():
    # For ease of input I created a csv with the teams and thier ratings as an average of the two player
    open_teams = pd.read_csv(TEAM_RANKING_DATA_PATH)

    # Create a team dictionary out of the teams playing
    team_dict = dict(zip(open_teams["Team"], open_teams["Team Rating"]))

    # Set up simulation
    nationals = Multi_Simulator(OPEN_POOLS, team_dict)

    # Run Simulation
    nationals.sim_n(32, 1000, bracket_keys)

    # Export Results
    nationals.export_results(tag=EXPORT_FILENAME)


if __name__ == "__main__":
    main()
