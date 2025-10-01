---
title: Digit Recognition App
emoji: 🔢
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
short_description: Interactive digit recognition using CNN
---

# 🎯 Digit Recognition App

A web application that recognizes hand-drawn digits (0-9) using a Convolutional Neural Network trained on the MNIST dataset.

## ✨ Features

- **Interactive Drawing Canvas**: Draw digits using mouse or touch
- **Real-time Prediction**: Get instant predictions with confidence scores
- **Probability Visualization**: See confidence levels for all 10 digits
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface with smooth animations

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask API
- **Machine Learning**: TensorFlow/Keras with CNN model
- **Dataset**: MNIST (Modified National Institute of Standards and Technology)

## 🚀 How to Use

1. **Draw a digit**: Use your mouse or finger to draw a digit (0-9) on the canvas
2. **Click Predict**: Press the "🔮 Predict Digit" button
3. **View Results**: See the predicted digit and confidence score
4. **Clear Canvas**: Use "🗑️ Clear Canvas" to start over

## 🧠 Model Architecture

The CNN model consists of:
- **Input Layer**: 28x28x1 grayscale images
- **Convolutional Layers**: 3 Conv2D layers with ReLU activation
- **Pooling Layers**: MaxPooling2D for dimensionality reduction
- **Dense Layers**: Fully connected layers with dropout
- **Output Layer**: Softmax activation for 10 digit classes

## 🔮 Model Performance

- **Training Accuracy**: ~99% on MNIST test set
- **Inference Time**: <100ms per prediction
- **Model Size**: ~2MB

## 📱 Mobile Support

The app is fully responsive and supports touch drawing on mobile devices.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- MNIST dataset by Yann LeCun
- TensorFlow/Keras for the ML framework
- Flask for the web framework