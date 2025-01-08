# FIFO Page Replacement Technique

This project implements the **FIFO (First In, First Out) Page Replacement Algorithm** using Python to handle multiple reference strings stored in a CSV file. It processes the page replacement technique for different frame sizes and calculates performance metrics like hit and miss ratios.

---

## Features 🚀
- Supports FIFO page replacement for multiple reference strings.
- Handles dynamic frame sizes (default: 3 to 6 frames).
- Calculates:
  - **Hit Count**
  - **Miss Count**
  - **Hit Ratio** (as a percentage)
  - **Miss Ratio** (as a percentage)
  - **Average Statistics** across reference strings.
- Processes input directly from a CSV file.

---

## Requirements 📋
- Python 3.8 or higher.
- **Required Library:** Pandas.
  
Install Pandas using:
```bash
pip install pandas
```

- Example CSV file: `r_strings.csv` containing the reference strings.

### Example CSV Structure
| RS1 | RS2 | RS3 | ... | RS10 |
|-----|-----|-----|-----|-------|
| 7   | 1   | 4   |     | ...   |
| 0   | 0   | 1   |     | ...   |
| 1   | 2   | 0   |     | ...   |

Place the `r_strings.csv` file in the same directory as the Python program.

---

## Algorithm Summary 💡

1. Read the reference strings from the CSV file.
2. Iterate over a configurable range of frame sizes (default: 3 to 6 frames).
3. For each frame size:
   - Simulate FIFO page replacement.
   - Calculate and display:
     - Hits and Misses per reference string.
     - Hit Ratio and Miss Ratio.
     - Average performance metrics.
4. Output results for all frame sizes.

---

## How to Use 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/mohammadsarfarazafzal/fifo.git
cd fifo
```

### 2. Prepare the Input
Ensure the `r_strings.csv` file is available in the same directory. Format it according to the example provided in the **Requirements** section.

### 3. Run the Program
Run the Python script:
```bash
python fifo.py
```

---

## Sample Output 📊
Example results for a CSV file with 10 reference strings and frame sizes 3 to 6:
```plaintext
Hit Count in RS1 for 3 number of frames = 4
Miss Count in RS1 for 3 number of frames = 6
Hit Ratio in RS1 for 3 number of frames = 40.0%
Miss Ratio in RS1 for 3 number of frames = 60.0%
...
Average Hit Count for 6 number of frames = 8.900
Average Hit Ratio for 6 number of frames = 89.000%
Average Miss Count for 6 number of frames = 1.100
Average Miss Ratio for 6 number of frames = 11.000%
```

---

## Quora Post 🌟
Detailed explanation and the context of the project are available in my [Quora post](https://qr.ae/pYttsu).

---

## Contribution 🤝
Contributions are welcome! If you'd like to extend this program to include other page replacement algorithms (e.g., LRU, LFU, Optimal), feel free to fork the repository and submit a pull request.

---

## License 📝
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Author 💡
Created by **Mohammad Sarfaraz Afzal**

- [Portfolio](https://mohammadsarfarazafzal.github.io)
- [GitHub](https://github.com/mohammadsarfarazafzal)
- [Quora Post](https://qr.ae/pYttsu)

---
