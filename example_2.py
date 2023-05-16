from handwriting_visualisations import *
from handwriting_sample import HandwritingSample
from handwriting_features.features import HandwritingFeatures

sample = HandwritingSample.from_svc(path="_examples/_example_5.svc")
feature_data = HandwritingFeatures.from_sample(sample)

handwriting_visualisations = HandwritingVisualisations(input_data={"x": feature_data.wrapper.on_surface_data.x,
                                                                   "y": feature_data.wrapper.on_surface_data.y}, custom_config={"display": True})
myplot = handwriting_visualisations.simple_plots.plot_x_y()
print(f"type: {myplot}")
