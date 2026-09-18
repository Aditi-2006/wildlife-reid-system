# Problem Statement & Project Scope: WildID (wildlife_reid_system)

## 1. Problem Statement
Monitoring endangered animal species like tigers and leopards relies heavily on camera traps placed across forest reserves. These cameras generate thousands of photographs over a few months. Currently, field researchers manually inspect every image, comparing stripe and spot patterns by eye to figure out if a captured animal is a known individual or a new one. 

This manual visual comparison is extremely tedious, slow, and prone to human error—creating a huge delay in tracking population numbers and planning conservation efforts.

## 2. Project Scope
WildID automates this matching process using computer vision. The system accepts camera trap images, identifies the animal, crops out its unique body pattern, turns that pattern into a digital fingerprint (feature vector), and checks it against a database of registered animals. 

### What the project covers:
- Command-line tools for automated batch processing.
- Image preprocessing and central region cropping.
- Extracting visual feature descriptors from stripe patterns.
- Cosine similarity matching to identify specific individuals.
- Logging unknown animals as new registrations automatically.

### Out of scope for this version:
- Live streaming video feeds.
- Full 3D posture reconstruction of animals.

## 3. Target Users
- **Wildlife Researchers:** To analyze camera trap data quickly without manual sorting.
- **Forest Department Staff:** To maintain accurate counts of local tiger/leopard populations.
- **Conservation Biologists:** To track individual movement across different camera locations over time.

## 4. High-Level Features
- **Automatic Crop & Preprocessing:** Cleans and crops the main pattern region from incoming photos.
- **Pattern Representation:** Turns visual stripe details into mathematical vectors.
- **Similarity Matching:** Compares vectors against registered individual profiles.
- **Automated Fallback:** Creates test inputs on the fly if no image argument is given, preventing execution errors.