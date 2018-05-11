# ImageSegmentationUsing_KMeans

- To reduce the number of color points in an image using supervised learning. This application is also referred to as image segmentation or color quantization
- K-means algorithm is used for image segmentaion

### Tools, libraries used

- Language used: Python
- Libraries used: opencv, numpy

### Input

Image segmentation algorithm is run on 3 images which can be found <a href="">here</a>

### Parameters

It is upto you to select the best value of the number of clusters and any other parameters for the algorithm


### Compile and Run Instructions:

**Commands to run:**

```
  ImageSegmentationUsingKMeans.py <Path to Image1> <Path to Image2> <Path to Image3> 
```

**Example command**

```
  python ImageSegmentationUsingKMeans.py image1.jpg image2.jpg image3.jpg
```

### Output

Output is a set of clustered images and stored in a folder named **clusteredImages** which can be found <a href="https://github.com/patilankita79/ImageSegmentationUsing_KMeans/tree/master/ImageSegmentation/clusteredImages">here</a>

### References

- https://docs.opencv.org/3.1.0/d1/d5c/tutorial_py_kmeans_opencv.html#gsc.tab=0
