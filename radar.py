# TODO
# Take stats as inputs and create a radar graph based on six important stats
# Copy the code from the internet, use this as a module so the graph function can just be called in main
from matplotlib.pyplot import polar
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.io as pio

import settings


def plot():
    categories = ['Speed', 'Shooting', 'Passing',
                  'Dribbling', 'Defending', 'Physicality']
    categories = [*categories, categories[0]]

    playerOutline = []
    # Could be automated.
    playerOutline.append(settings.currentPlayer.get("short_name"))
    playerOutline.append(int(settings.currentPlayer.get("pace")))
    playerOutline.append(int(settings.currentPlayer.get("shooting")))
    playerOutline.append(int(settings.currentPlayer.get("passing")))
    playerOutline.append(int(settings.currentPlayer.get("dribbling")))
    playerOutline.append(int(settings.currentPlayer.get("defending")))
    playerOutline.append(int(settings.currentPlayer.get("physic")))
    playerOutline = [*playerOutline, playerOutline[0]]
    settings.currentPlayerOutline = playerOutline

    fig = go.Figure(
        data=[
            go.Scatterpolar(r=playerOutline,
                            fill='toself', name=settings.currentPlayer.get('short_name'), theta=categories, )  # Display the relevant player name
        ],
        layout=go.Layout(
            # Display the relevant player name
            title=go.layout.Title(
                text=settings.currentPlayer.get('short_name')),
            showlegend=True,
            plot_bgcolor='#000000',
            template='plotly_dark',
        )
    )
    fig.update_xaxes(range=[0, 99], fixedrange=True)
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 99]
            )),
        showlegend=False
    )

    pyo.plot(fig)
