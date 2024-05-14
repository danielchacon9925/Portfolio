# Extraction of polygon coordinates with gdspy library.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Library documentation](#library-documentation)
- [Configuration](#configuration)
- [Author](#author)

## Introduction
The GDS (Graphics Data System) archive contains comprehensive descriptions of polygonal areas associated with logic cells. The extraction of these polygons holds the potential to generate an occupation matrix that effectively represents occupied points within the chip area. The significance of these occupied points lies in their capacity to enable the anticipation of Design Rule Check violations (DLCs) without necessitating the execution of the placement, clock tree synthesis (CTS), and sign-off processes in future stages of development.

## Getting Started
gdspy is a python library use to defined polygons for ASIC development. 

## Library documentation

All the information is available at https://gdspy.readthedocs.io/en/stable/reference.html

## Configuration

#### Cell variables

- **name (string)**: The name of this cell.
- **polygons (list of PolygonSet)**: List of cell polygons.
- **paths (list of RobustPath or FlexPath)**: List of cell paths.
- **labels (list of Label)**: List of cell labels.
- **references (list of CellReference or CellArray)**: List of cell references.


#### Opening the GDS File

Before proceeding with the analysis, it is essential to open the GDS (Graphics Data System) file, which contains crucial information about the polygonal areas associated with logic cells. This step is fundamental for extracting and processing the necessary data.

```python

import gdspy

gds_file = gdspy.GdsLibrary()
gdsii = gds_file.read_gds('picorv32.gds')

```

#### Declare main cell


```python
main_cell = gdsii.top_level()[0] 
```

#### Cell name

```python
main_cell.name
```

#### Polygons in cell

Is a list, use [index] with desire index for polygon.


```python
main_cell.polygons
```

#### Cell labels

Is a list, use [index] with desire index for label.


```python
main_cell.labels
```

#### Area in cell 

Is a dictonary. Use [index] for desire label.

```python
main_cell.area(by_spec=True)
```


## Author

- **Daniel Chacón Mora**
- Student ID: B72018
