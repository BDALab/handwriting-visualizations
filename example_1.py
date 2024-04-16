from visualization_tools import *
from handwriting_sample import HandwritingSample
from handwriting_features.features import HandwritingFeatures

sample = HandwritingSample.from_svc(path="_example_5.svc")
feature_data = HandwritingFeatures.from_sample(sample)

# Preparing config variable
config = {}
config["body"] = \
    [
        [
            {
                "name": "On-surface pohyb",
                "x": feature_data.wrapper.on_surface_data.x,
                "y": feature_data.wrapper.on_surface_data.y,
                "mode": "lines",
                "line": {
                    "color": "blue",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "name": "In-air pohyb",
                "x": feature_data.wrapper.in_air_data.x,
                "y": feature_data.wrapper.in_air_data.y,
                "mode": "lines",
                "line": {
                    "color": "red",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "name": "In-air pohybads",
                "x": feature_data.wrapper.on_surface_data.x,
                "y": feature_data.wrapper.on_surface_data.time,
                "mode": "lines",
                "line": {
                    "color": "red",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "_config": {  # https://plotly.com/python/axes/
                    "update_xaxes": {
                        "title_text": "Souřadnice x [mm]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "scaleanchor": "y"
                    },
                    "update_yaxes": {
                        "title_text": "Souřadnice y [mm]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        }
                    },
                    "update_annotations": {#plotly bug, cannot update by row and col
                        "font": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 28
                        },
                        "text": "Pila",
                        "selector": {"text": "1"}
                    }
                }
            }
        ],
        [
            {
                "name": "Souřadnice x",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.wrapper.on_surface_data.x,
                "mode": "lines",
                "line": {
                    "color": "darkblue",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "name": "Souřadnice y",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.wrapper.on_surface_data.y,
                "mode": "lines",
                "line": {
                    "color": "darkred",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "_config": {  # https://plotly.com/python/axes/
                    "update_xaxes": {
                        "title_text": "Čas [s]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "tickmode": 'linear',
                        "tick0": 0.0,
                        "dtick": 1
                    },
                    "update_yaxes": {
                        "title_text": "Souřadnice x,y [mm]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "tick0": 0.0,
                        "dtick": 25
                    },
                    "update_annotations": {
                        "font": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 28
                        },
                        "selector": {"text": "2"},
                        "text": "Průběh souřadnic x a y v čase"
                    }
                }
            }
        ],
        [
            # {
            #     "name": "Tlak [-]",
            #     "x": feature_data.wrapper.on_surface_data.time,
            #     "y": [x := feature_data.wrapper.on_surface_data.pressure, (x - x.mean()) / x.std()][1],
            #    "mode": "lines",
            #    "line": {
            #        "color": "mediumblue",
            #        "width": 5
            #    },
            #    "opacity": 0.65,
            # },
            {
                "name": "Azimut",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.wrapper.on_surface_data.azimuth,
                "mode": "lines",
                "line": {
                    "color": "mediumseagreen",
                    "width": 4
                },
                "opacity": 0.65
            },
            {
                "name": "Elevace",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.wrapper.on_surface_data.tilt,
                "mode": "lines",
                "line": {
                    "color": "mediumvioletred",
                    "width": 3
                },
                "opacity": 0.65
            },
            {
                "_config": {  # https://plotly.com/python/axes/
                    "update_xaxes": {
                        "title_text": "Čas [s]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "tickmode": 'linear',
                        "tick0": 0.0,
                        "dtick": 1
                    },
                    "update_yaxes": {
                        "title_text": "Azimut, elevace [°]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        }
                    },
                    "update_annotations": {
                        "font": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 28
                        },
                        "selector": {"text": "3"},
                        "text": "Azimut, elevace v čase"
                    }
                }
            }
        ],
        [
            {
                "name": "Horizontální rychlost",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.velocity(axis="x", in_air=False),
                "mode": "lines",
                "line": {
                    "color": "lightseagreen",
                    "width": 3
                },
                "opacity": 0.65,
            },
            {
                "name": "Vertikální rychlost",
                "x": feature_data.wrapper.on_surface_data.time,
                "y": feature_data.velocity(axis="y", in_air=False),
                "mode": "lines",
                "line": {
                    "color": "mediumvioletred",
                    "width": 3
                },
                "opacity": 0.65
            },
            {
                "_config": {  # https://plotly.com/python/axes/
                    "update_xaxes": {
                        "title_text": "Čas [s]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "tickmode": 'linear',
                        "tick0": 0.0,
                        "dtick": 1
                    },
                    "update_yaxes": {
                        "title_text": "Rychlost [mm/s]",
                        "showgrid": True,
                        "title_font": {"size": 28,
                                       "family": 'Georgia',
                                       "color": 'black'},
                        "showticklabels": True,
                        "tickangle": 0,
                        "tickfont": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 20
                        },
                        "tick0": 0.0,
                        "dtick": 25
                    },
                    "update_annotations": {
                        "font": {
                            "family": 'Georgia',
                            "color": 'black',
                            "size": 28
                        },
                        "selector": {"text": "4"},
                        "text": "Rychlost (on-surface)"
                    }
                }
            }
        ]
    ]

config["global_config"] = {
    "subplots": {
        "rows": 2,
        "cols": 2,
        #"column_widths": [0.5, 0.5],
        "vertical_spacing": 0.14,
        "subplot_titles": ["1", "2", "3", "4"]},
    "layout": {  # https://plotly.com/python/reference/layout/
        "showlegend": True,
        # "title": "Časové řady",
        "autosize": True,
        "font": {
            "family": "Georgia",
            "size": 22,
            "color": "black"
        },
        "legend": {
            "orientation": "h",
            "yanchor": "top",
            "xanchor": "center",
            "y": -0.1,
            "x": 0.5}
    },
    "display": True,
    "output": ["fig", "div"],
    "picture": {
        "file": "example_export.png",
        "width": 1920,
        "height": 1080
    }
}
response = vizualize(config)
print(len(response))
