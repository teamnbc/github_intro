"Draw the names of the team members on a figure and save it."
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def draw_name(name, color="#000000", ax=None, size=10):
    "Draw the provided name at a random location on ax."
    if ax is None:
        ax = plt.gca()
    xlim, ylim = ax.get_xlim(), ax.get_ylim()  # limits of the axes

    # Random coordinates and rotation for the text
    x = np.random.rand() * (xlim[1] - xlim[0]) + xlim[0]
    y = np.random.rand() * (ylim[1] - ylim[0]) + ylim[0]
    rotation = (np.random.rand() - .5) * 360  # degrees

    # Draw the name
    ax.text(x, y, name, color=color, rotation=rotation)
    return ax


if __name__ == "__main__":
    np.random.seed(0)  # for reproducibility

    # Deal with the folder architecture and loads the names
    path_repository = Path(__file__).parent.parent
    team_members = pd.read_csv(path_repository / "team_members.csv")
    print(team_members)

    # Plot and save the figure
    fig, ax = plt.subplots(figsize=(3, 3))
    ax.set_xticks([])
    ax.set_yticks([])
    for _, member in team_members.iterrows():  # loop over the rows of the csv
        draw_name(member.pseudo, color=member.color_hex)
    fig.savefig(path_repository / "output" / "out_python.png")
