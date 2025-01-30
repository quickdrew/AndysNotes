# Jetson Nano

The Jetson Nano is a powerful yet compact AI computing platform designed for edge AI projects. It provides the performance and flexibility needed for real-world AI applications while remaining accessible to hobbyists, students, and developers alike. Below, you'll find essential resources to get started with the Jetson Nano:


## Resources

- [Jetson Nano Datasheet](https://components101.com/sites/default/files/component_datasheet/Jetson-Nano-DataSheet.pdf): Comprehensive technical specifications for the Jetson Nano.
- [Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#intro): Official page for setup guides, tutorials, and detailed documentation.
- [NVIDIA Jetson Projects](https://developer.nvidia.com/embedded/community/jetson-projects): Explore a collection of projects built by the Jetson community for inspiration and guidance.
- [YOLO Object Detection](https://docs.ultralytics.com/models/)
---

## SSH into Jetson Nano via Ubuntu WSL

1. **Identify the Jetson Nano's IP Address**  
   On the Jetson Nano, run:  
   ```bash
   hostname -I
   ```  
   Note the IP address.

2. **Check Connection from WSL**  
   Open the Ubuntu WSL terminal on your Windows machine and ping the Jetson Nano to confirm connectivity:  
   ```bash
   ping <Jetson-IP>
   ```  
   Replace `<Jetson-IP>` with the IP address of the Jetson Nano.

3. **SSH into the Jetson Nano**  
   Use the `ssh` command in your WSL terminal:  
   ```bash
   ssh jetson@<Jetson-IP>
   ```  
      - Replace `<Jetson-IP>` with the IP address of the Jetson Nano.  
      - The default password is `jetson`.  

4. **Save SSH Fingerprint**  
   During the first connection, you may be prompted to confirm the SSH fingerprint. Type `yes` and press Enter to save it for future connections.


---

## Image Processing (Hello AI World)

Following notes are based off Jetson Nano's AI introductionary project called [Hello AI world](https://github.com/dusty-nv/jetson-inference).

---

### ImageNet

**ImageNet** is a large-scale dataset containing millions of labeled images across thousands of categories. It is widely used for training and benchmarking computer vision models and was instrumental in the rise of deep learning, starting with the success of convolutional neural networks (CNNs) like AlexNet in 2012.

**Why It Matters to the Jetson Nano:**

The **Jetson Nano**, a low-power AI development board for edge computing, benefits from ImageNet in several ways:

1. **Pretrained Models**: Deploy CNNs like ResNet or MobileNet for tasks such as object detection, image classification, and feature extraction.  
2. **Transfer Learning**: Fine-tune pretrained models on custom datasets with accelerated training and inference.  
3. **Benchmarking**: Use ImageNet to evaluate the Nano’s performance in handling computer vision workloads.  
4. **Edge AI Applications**: Enable real-time object recognition for robotics, IoT devices, and autonomous systems.  

**Learning Material:**
[Jetson ImagNet Project](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md)

---

### TensorRT

**TensorRT** is an NVIDIA library for optimizing and accelerating deep learning inference on GPUs. It supports model optimization (e.g., precision calibration, layer fusion), multiple precisions (FP32, FP16, INT8), and works with models from frameworks like TensorFlow, PyTorch, and ONNX. TensorRT is ideal for high-throughput, low-latency applications in real-time AI tasks such as object detection, NLP, and autonomous systems.

Example project using GoogleNet image recognition netowrk with TensorRT found [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-example-2.md)

---

### Sigmoid and Softmax in Classification


**Softmax** is used for **single-class classification**, where each instance belongs to exactly one class. It converts logits into a probability distribution using the formula:

\[
\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}
\]

This ensures that probabilities across all classes sum to 1. Softmax is suitable for tasks where classes are **mutually exclusive**, like predicting whether an image contains a "cat," "dog," or "bird" (but only one of them).

**Sigmoid** is used for **multi-label classification**, where each instance can belong to multiple classes. It applies the function:

\[
\sigma(x) = \frac{1}{1 + e^{-x}}
\]

to each output independently, producing probabilities between 0 and 1. For example, in an image containing both "cat" and "dog," sigmoid allows both classes to be true since they are **not mutually exclusive**. The probabilities for each class do **not sum to 1**.


Here's a Sigmoid example for printing out the top 5 classifications of a jpg image:

```C
#include <jetson-inference/imageNet.h>
#include <jetson-utils/loadImage.h>
#include <vector>

int main(int argc, char** argv)
{
    // Ensure an image filename is provided as a command line argument
    if (argc < 2)
    {
        printf("my-recognition: expected image filename as argument\n");
        printf("example usage:  ./my-recognition my_image.jpg\n");
        return 0;
    }

    // Retrieve the image filename from command line arguments
    const char* imgFilename = argv[1];

    // Variables for the image data pointer and dimensions
    uchar3* imgPtr = NULL;   // shared CPU/GPU pointer to image
    int imgWidth   = 0;      // width of the image (in pixels)
    int imgHeight  = 0;      // height of the image (in pixels)

    // Load the image from disk as uchar3 RGB (24 bits per pixel)
    if (!loadImage(imgFilename, &imgPtr, &imgWidth, &imgHeight))
    {
        printf("failed to load image '%s'\n", imgFilename);
        return 0;
    }

    // Load the GoogleNet image recognition network with TensorRT
    imageNet* net = imageNet::Create("googlenet");

    // Ensure the network model loaded properly
    if (!net)
    {
        printf("failed to load image recognition network\n");
        return 0;
    }

    // Store classifications and specify the number of top results (topK)
    imageNet::Classifications classifications; // vector of (classID, confidence)
    const int topK = 5; // Modify this for more or fewer top results

    // Classify the image and retrieve multiple results
    if (net->Classify(imgPtr, imgWidth, imgHeight, classifications, topK) < 0)
    {
        printf("failed to classify image\n");
        delete net;
        return 0;
    }

    // Print out the classification results
    printf("Classification results (top %d):\n", topK);
    for (size_t n = 0; n < classifications.size(); n++)
    {
        const uint32_t classID = classifications[n].first;
        const char* classLabel = net->GetClassLabel(classID);
        const float confidence = classifications[n].second * 100.0f;

        printf(" %2.5f%% class #%u (%s)\n", confidence, classID, classLabel);
    }

    // Free the network's resources before shutting down
    delete net;
    return 0;
}
```

example project here: [Multi-Label Classification for Image Tagging](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-tagging.md)


### Object Detection with DetectNet

DetectNet is a deep learning framework designed for object detection tasks, optimized for NVIDIA Jetson devices. It identifies objects in an image and provides their locations using bounding boxes.

**Key Features:**

1. **Input:** Processes an image through a pre-trained neural network (e.g., SSD or Faster R-CNN).
2. **Output:** Returns: Bounding boxes, Object classes, and Confidence scores
3. **Applications:** Pedestrian detection, Vehicle detection, Custom object detection (after fine-tuning)

DetectNet utilizes TensorRT for high-speed inference and supports training on custom datasets to detect specific object classes.

Reference for [images](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-console-2.md)

Reference for [video](https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-tracking.md)

---

### Semantic Segmentation

Semantic segmentation classifies every pixel in an image into categories (e.g., road, car, sky), offering detailed scene understanding. Unlike **object detection**, which provides bounding boxes, semantic segmentation delivers pixel-level precision. Two prominent architectures are **Fully Convolutional Networks (FCNs)** and **SegNet**.

**Fully Convolutional Networks (FCNs)**

- **Architecture:** Replace fully connected layers with convolutional layers to preserve spatial relationships.
- **Upsampling:** Use transposed convolutions (deconvolution) to restore spatial resolution.
- **Skip Connections:** Combine high-level features with low-level details for better accuracy.
- **Use Case:** High-accuracy, detailed segmentation tasks, though computationally intensive.

**SegNet**

- **Encoder-Decoder Structure:**

      1. **Encoder:** Extracts features with convolution and pooling layers, reducing spatial resolution.
      2. **Decoder:** Upsamples using saved pooling indices from the encoder, maintaining spatial accuracy while reducing memory and computation.

- **Optimized for Efficiency:** Designed for lightweight, real-time applications.
- **Use Case:** Real-time tasks on resource-constrained devices, like Jetson Nano.

**Applications**

1. **Urban Environments (Cityscapes)**  
   Segment urban scenes to identify roads, buildings, pedestrians, and vehicles for autonomous driving and smart city systems.  

      - **Dataset**: [Cityscapes](https://www.cityscapes-dataset.com/)  

2. **Off-Road Navigation (DeepScene)**  
   Classify forest trails, vegetation, and off-road elements for robotic path-following in outdoor environments.  

      - **Dataset**: [DeepScene](http://deepscene.cs.uni-freiburg.de/)  

3. **Multi-Human Parsing (MHP)**  
   Segment people into detailed body parts like arms, legs, and clothing for pose estimation or fashion analytics.  

      - **Dataset**: [Multi-Human Parsing](https://lv-mhp.github.io/)  

4. **Object Segmentation (Pascal VOC)**  
   Classify and segment various objects, including people, animals, and vehicles, for general-purpose object recognition.  

      - **Dataset**: [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/)  

5. **Indoor Scene Understanding (SUN RGB-D)**  
   Recognize furniture, appliances, and spaces in office and home environments for robotics and augmented reality.  

      - **Dataset**: [SUN RGB-D](http://rgbd.cs.princeton.edu/)  


[Nividia Reference](https://github.com/dusty-nv/jetson-inference/blob/master/docs/segnet-console-2.md)


---

