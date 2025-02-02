# Blueprint Analyzer with OpenCV

## 📌 Overview
Blueprint Analyzer is a Python-based tool that processes floor plan images, detects enclosed rooms, and calculates their areas using OpenCV. The program allows users to interactively adjust filter settings (such as dilation size and room area threshold) to refine results. Users can save the final results as a text file.

## ✨ Features
- **Automatic Room Detection**: Identifies enclosed spaces inside a blueprint.
- **Adjustable Filtering**:
  - **Dilation Kernel Size**: Controls how much walls expand to close doorways.
  - **Minimum Room Size Threshold**: Filters out small areas that aren’t rooms.
- **Interactive User Interface**:
  - **Modify settings dynamically** and reprocess the image.
  - **Press 's' to save results** and exit.
- **Handles Invalid Inputs Gracefully**: Ensures robustness by preventing crashes due to incorrect file paths or values.

## 📥 Installation
### Prerequisites
Make sure you have **Python 3.7+** installed on your system.

### Install Required Libraries
Use the following command to install dependencies:
```bash
pip install opencv-python numpy
```

## 🚀 Usage
### 1️⃣ Run the Program
```bash
python3 blueprint_analyzer.py
```
### 2️⃣ Load a Floor Plan Image
- The program will prompt you to **enter the image path**.
- **Supported formats**: JPG, PNG, BMP, TIFF, WEBP.

### 3️⃣ Adjust Filtering Criteria
- The script will process the image and show the detected rooms.
- You can adjust:
  - **Dilation Kernel Size** (Larger value = Closes bigger doorways)
  - **Minimum Room Size** (Higher value = Filters out small areas)
- Enter new values to **reprocess the image** with refined settings.

### 4️⃣ Save Results & Exit
- Once satisfied, **press 's'** to save results in a text file.
- The file will be saved in the same directory as the blueprint image.

## 🖼 Example Output
```
Processing image with:
- Dilation Kernel Size: 10
- Minimum Room Size Threshold: 5000
Total Number of Rooms Detected: 7
```

## 📄 Output File Format
The results will be saved as `<image_name>_results.txt` with the following content:
```
Blueprint Analysis Results
Image: sample_blueprint.png
Total Rooms Detected: 7
Dilation Kernel Size: 10
Minimum Room Size Threshold: 5000
```

## ⚠️ Error Handling
- If an **invalid file path** is entered, the program will prompt the user to **re-enter** the path.
- If an **unsupported image format** is provided, the user will be asked to try again.
- If **no rooms are detected**, a warning will be displayed with guidance to adjust filtering settings.

## 📜 License
This project is released under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! If you'd like to suggest improvements, feel free to fork the repository and submit a PR.

## 📩 Contact
For any issues or questions, feel free to open an issue in the repository.

