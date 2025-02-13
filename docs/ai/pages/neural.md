



## Computational View of a DNN

![DNN](../assets/dnn.png)

### Its Just Matrix Math
In deep neural networks (DNN), matrix math is the foundation for propagating data through layers, as depicted in the diagram. Each layer starts with **input features** (\( \mathbf{x}_1, \mathbf{x}_2, \dots \)) that are combined with a **weight matrix** (\( \mathbf{W} \)) to compute **scores**:

\[
\mathbf{z} = \mathbf{W} \cdot \mathbf{x} + \mathbf{b}
\]

The scores are then passed through an **activation function** \( f(\cdot) \), such as the one shown in the diagram, to introduce non-linearity:

\[
\mathbf{y} = f(\mathbf{z})
\]

The result, \( \mathbf{y} \), represents the output of **hidden units** in each layer, which then serve as inputs to the next layer. This process is repeated across multiple layers, from the **first layer** (weights, scores, and activation functions) through the **hidden layers** to the final layer, which produces the **output units**.

Each hidden layer transforms its inputs into a new representation using the same sequence: weights, scores, activation functions, and outputs. These operations are computationally intensive but highly parallelizable, making GPUs and TPUs essential for efficiently handling the large-scale computations in deep learning.

### Training the DNN
Training is the process of learning the optimal weights and biases for a DNN. It involves:

1. **Forward Pass**: Input features are propagated through the network to compute predictions.
2. **Loss Calculation**: The error between predictions and targets is measured using a loss function.
3. **Backpropagation**: Gradients of the loss with respect to the weights are calculated.
4. **Weight Update**: Weights are adjusted using an optimizer (e.g., SGD) to minimize the error.

This process repeats over many iterations (epochs) until the model converges.

### Executing the DNN (Inference) 
Inference uses the trained weights to make predictions. It involves:

1. **Forward Pass Only**: Input features propagate through the network to compute outputs.
2. **Prediction**: The final output represents the model's decision.

Unlike training, inference is faster and less computationally intensive as it skips backpropagation and weight updates.

**Key Differences**

| **Aspect**       | **Training**                       | **Inference**                    |
|-------------------|-----------------------------------|----------------------------------|
| **Purpose**       | Learn weights.                   | Make predictions.                |
| **Operations**    | Forward pass + backpropagation.  | Forward pass only.               |
| **Resource Needs**| High (GPUs/TPUs).                | Low, optimized for speed.        |
