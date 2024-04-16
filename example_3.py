from handwriting_visualizations.handwriting_visualisations import *
from handwriting_sample import HandwritingSample

sample = HandwritingSample.from_svc(path="handaqus_cintiq_data.svc")
# sample = HandwritingSample.from_svc(path="_example_5.svc")

handwriting_visualisations = HandwritingVisualisations(input_data={"x": sample.x,
                                                                   "y": sample.y}, custom_config={"display": True})

myplot = handwriting_visualisations.simple_plots.plot_on_surface(sample=sample)

print(f"type: {myplot}")