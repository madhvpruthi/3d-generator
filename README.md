# Photo/Text to 3D:

This project allows users to **generate 3D models** (`.obj` and `.stl`) using either:
- Images
- Text prompts

# the project is currently supporting these shapes only 
- cone 
- cylinder 
- sphere
- tetrahedron 
- triangle
- rectangle
- cube
- box 

The projectn uses Python, computer vision, and basic 3D geometry to convert visual/text input into downloadable 3D models.

---

# Features

- Generate simple 3D models from text prompts.
- Extract objects from images using background removal.
- Export models as `.obj` and `.stl` formats .
- Preview 3D models in real-time .
- Simple Python-based local interface (CLI) .
- Output folder stores your generated models.

---

# Installation

# 1- Clone

```bash
git clone https://github.com/madhvpruthi/3d-generator
cd 3d-generator
```
# 2- create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3- install dependencies 
pip install -r requirements.txt

# 4- run the main file 
python app.py 

