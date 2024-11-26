# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Program execution
## Parameters of which shapes can be calculated
- Circle
- Rectangle
- Square
- Triangle

## Functions
### Area
The function calculates the area of a specific shape using the corresponding formula
> Function call example for a circle:
```python
print(area(r))

Input: r = 4
Output: 50.26548245743669
```
> Function call example for a rectangle:
```python
print(area(r))

Input: a = 2; b = 3
Output: 6
```
> Function call example for a square:
```python
print(area(r))

Input: a = 4
Output: 16
```
> Function call example for a triangle:
```python
print(area(r))

Input: a = 4; h = 10
Output: 20
```



### Perimeter
The function calculates the perimeter of a specific shape using the corresponding formula
> Function call example for a circle:
```python
print(perimeter(r))

Input: r = 5
Output: 31.41592653589793
```
> Function call example for a rectangle:
```python
print(perimeter(r))

Input: a = 2; b = 3
Output: 12
```
> Function call example for a square:
```python
print(perimeter(r))

Input: a = 5
Output: 20
```
> Function call example for a triangle:
```python
print(perimeter(r))

Input: a = 4; b = 3; c = 5
Output: 12
```

## Testing

Unit tests have been implemented to verify the accuracy and reliability of the area and perimeter calculations for each shape. Below are descriptions of the tests performed:
### Circle Tests

- Area with radius 0: Verifies that the area function returns 0 when the radius is zero.
- Area with radius -10: Verifies that the area function returns 314.159 when the radius is -10.
- Area with radius 4: Confirms the area calculation is approximately 50.27.
- Perimeter with radius 5: Checks that the perimeter calculation returns approximately 31.42.
- Area with radius 50000000: Verifies that the area function returns 7853981633974482.0 when the radius is 50000000.

### Rectangle Tests

- Area with zero width: Tests that the area is zero when one side length is zero.
- Square area (10x10): Ensures that a rectangle with equal sides calculates an area of 100.
- Perimeter with sides 2 and 5: Checks the perimeter calculation for sides 2 and 5, expecting 14.

### Square Tests

- Area with side 0: Verifies that the area function returns 0 when the side length is zero.
- Area with side 10: Confirms the area calculation returns 100.
- Perimeter with side 5: Ensures the perimeter calculation returns 20.
- Large area calculation: Tests the function’s handling of very large side lengths.
- Negative side for perimeter: Checks perimeter calculation when the side is negative.

### Triangle Tests

- Area with height 0: Verifies that the area is zero when height is zero.
- Area with base 10 and height 6: Confirms that the area calculation returns 30.
- Perimeter with sides 3, 5, and 4: Ensures the perimeter function calculates 12.
- Negative base area calculation: Checks the area function's behavior with a negative base, expecting a negative area.
- Large perimeter calculation: Verifies that the perimeter function handles very large values correctly.

All tests are in `pytests.py`

### Testing Framework

The tests use Python’s built-in unittest module. Each shape has a dedicated test class to group related tests logically. This setup ensures comprehensive coverage for all shape-related calculations and helps detect any unexpected behavior.

## CI/CD Integration
### Workflow Overview

A GitHub Actions workflow automates testing upon every push to the repository. It ensures all tests pass successfully in both Ubuntu and Windows environments.
### Key Features:

Build and Test on Ubuntu:

1. Installs project dependencies (requirements.txt).
2. Executes tests using Python’s unittest and generates a report via pytest.

Build and Test on Windows:

1. Similar process as Ubuntu, with adaptation for the Windows environment.

# Project changelog
> Commits with hashes
``` 
    * commit 2b60a62afe07032fd3756980231221c70936560d (HEAD -> labwork5_ci-cd)
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Tue Nov 26 19:08:29 2024 +0300
    |
    |     added .yml file with ci-cd testing & added testing file pytests.py
    |
    * commit df175a336bb29de5236548566360741ada211b83 (origin/labwork4_unit_tests, labwork4_unit_tests)
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Wed Nov 13 22:18:27 2024 +0300
    |
    |     documentation update
    |
    * commit 9326528a2ca03041b2265740e63a1e16ba515ac4
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Wed Nov 13 21:59:02 2024 +0300
    |
    |     added unit tests
    |
    * commit c4df14ac24f79065e35ee6b0860c2789b5e511f9 (origin/labwork2_docs, labwork2_docs)
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Fri Nov 1 10:23:58 2024 +0300
    |
    |     small commets & ReadMe update
    |
    * commit 49823c104085d443bb88e1059f4437b02401cdb5
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Fri Oct 18 10:48:52 2024 +0300
    |
    |     documentation update
    |
    * commit 510d5bee6cc5d78184d46be305c0231f24fef206
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Thu Oct 17 14:46:03 2024 +0300
    |
    |     updated README file & added func description
    |
    * commit 1ea7cb53b7e77aa8f8c377d8502031509d864b99 (origin/new_features_471752, new_features_471752)
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Wed Oct 2 14:41:48 2024 +0300
    |
    |     changed rectangle.py, added file triangle.py
    |
    * commit 1816cf1b2041bd01636ec3433984ba550f28b15e
    | Author: blumgardt <471752@niuitmo.ru>
    | Date:   Wed Oct 2 14:39:07 2024 +0300
    |
    |     added file rectangle.py
```