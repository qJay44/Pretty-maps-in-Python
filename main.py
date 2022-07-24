import json
from prettymaps import plot
from matplotlib import pyplot as plt


def draw(location, radius, width, height):
    with open('layers/layer1.json') as f:
        layer = json.load(f)

    with open('drawing properties/draw1.json') as f:
        draw_properties = json.load(f)
    
    fig, ax = plt.subplots(figsize=(width, height), constrained_layout=True)

    backup = plot(
        location,
        radius=radius,
        ax=ax,
        layers=layer,
        drawing_kwargs=draw_properties,
    )

    ax.autoscale()

    filename = f'imgs/{location}.png'
    plt.savefig(filename)
    plt.show()


if __name__ == "__main__":
    draw('Geneva, Switzerland', 1200, 10, 10)
