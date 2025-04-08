
---

# 🎉 Gender Prediction using Decision Tree Classifier 🎉

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 📖 Description

This project implements a simple gender prediction model using a **Decision Tree Classifier** from the `scikit-learn` library. The model is trained on data extracted from a CSV file and predicts the gender of individuals based on their height, weight, and shoe size.

## ✨ Features

- Reads data from a CSV file (`info.csv`).
- Trains a Decision Tree Classifier on the provided dataset.
- Accepts user input for height, weight, and shoe size to make predictions.
- Outputs the predicted gender for two individuals.

## 📂 Data File

The `info.csv` file has been added to the repository. This file contains the training data required for the model. Ensure that it is present in the same directory as the script when running the program.

## 🚀 Installation

To run this project, you need to have Python installed along with the `scikit-learn` library. You can install the required library using pip:

```bash
pip install scikit-learn
```

## 🛠️ Usage

1. Ensure that the `info.csv` file is in the same directory as your script. The file should have the following structure:
   - The first three columns should contain features (height, weight, shoe size).
   - The fourth column should contain labels (gender).

   **Example of `info.csv`:**
   ```
   1.75, 70, 42, Male
   1.60, 55, 38, Female
   ```

2. Run the script:

```bash
python predict_gender.py
```

3. When prompted, enter the information for two individuals in the following format:
   ```
   height(cm) weight(kg) shoe-size
   ```

   **Example input:**
   ```
   180 80 43
   165 60 39
   ```

4. The script will output the predicted genders for the two individuals.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## 📬 Contact

For questions or feedback, please reach out to [fahime] at [fahime.emlaei@gmail.com].

---

### 🌟 Acknowledgments

- [scikit-learn](https://scikit-learn.org/stable/) for the machine learning library.
- [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) for data handling.

---
