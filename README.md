# 🛠️ Triangle Renderer & 3D Transformations  
**Computer Graphics Project – 2024**

This repository contains the implementation of a three-part Computer Graphics project developed as part of the **Computer Graphics** course (Spring 2024). The project explores the fundamentals of triangle rasterization, shading techniques, 3D transformations, and projection.

---

## 📁 Project Overview

The project is organized into three progressive parts:

---

### 🟦 Part 1: Triangle Rasterization & Shading (2D)

This stage focuses on filling triangles and applying basic shading techniques in 2D.

**Key Features:**
- **Linear Interpolation:** Used for interpolating vertex attributes (colors, positions).
- **Flat Shading:** Assigns a single color per triangle, based on the average of vertex colors.
- **Gouraud Shading:** Computes vertex colors and interpolates them smoothly across the triangle surface using scanlines.

---

### 🧭 Part 2: 3D Transformations & Viewing

Introduces basic 3D graphics concepts, including transformations and camera simulation.

**Key Features:**
- **Affine Transformations:** Translation, scaling, and rotation using matrix operations.
- **Camera System:** Simulates a virtual camera using view and projection matrices.
- **3D-to-2D Projection:** Converts 3D world coordinates to 2D screen space for rasterization.

---

### 💡 Part 3: Phong & Gouraud Shading with Lighting (3D)

Expands the renderer to support **realistic lighting and shading** on 3D objects.

**Key Features:**
- **Input:** 3D object and lighting data loaded from `hw3.npy`.
- **Shading Models:**
  - **Gouraud Shading:** Lighting calculated per vertex, colors interpolated across triangles.
  - **Phong Shading:** Normals interpolated per pixel, lighting computed per fragment.
- **Phong Illumination Model:**
  - **Ambient** – background light
  - **Diffuse** – light reflected in all directions
  - **Specular** – highlights reflecting toward the viewer
- **Vertex Normals:** Computed to simulate smooth surfaces

---

## 🖼️ Output Description

The renderer produces shaded 2D images of 3D models under different lighting and shading conditions. You can switch between **Phong** and **Gouraud** shading modes to observe visual differences, especially in specular highlights and smoothness.

---
