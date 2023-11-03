According to the authors of **Maize Tassel Detection** dataset, the timing of flowering profoundly impacts crop productivity in agriculture, as early flowering can lead to premature maturation, and late flowering may result in season-related damage. Maize, in particular, is highly sensitive during its flowering stage. The dataset was created to focus on the development and comparison of two deep learning-based methods for automatic tassel detection using imagery from unmanned aerial vehicles. This approach was applied to 500 genotypes, comprising 750 plots within a 2-hectare breeding field.

The aerial RGB imagery was collected by a UAV (DJI Phantom 3 Pro) over a maize breeding field located in Mead, Nebraska, in late July 2017. The UAV was flying at a low altitude (20 m AGL), capturing images with approximately 90% forward overlap and 85% side overlap. Images were collected in July 2017, fifty-four days after planting, coinciding with the flowering stage of a substantial portion of the research varieties.

The raw images, characterized by a high resolution of 3000 × 4000 pixels, posed challenges in terms of precise labeling and the computational resources required for tassel identification. The authors divided each raw image into non-overlapping sub-images measuring 1000 × 1000 pixels, creating a 3 × 4 grid of smaller images from each original image. These smaller images were subsequently utilized in the labeling process and for training the deep learning models. The maize tassels were later labeled and used to train CNN models to automatically detect the tassels.



