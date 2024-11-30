def reflect_point(px, py, x1, y1, x2, y2):
    # Reflect point (px, py) across the line defined by points (x1, y1) and (x2, y2)
    # Calculate the line coefficients A, B, C for the line equation Ax + By + C = 0
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    # Calculate the distance from the point to the line
    d = (A * px + B * py + C) / (A**2 + B**2)**0.5
    
    # Calculate the reflection point
    rx = px - 2 * A * d / (A**2 + B**2)**0.5
    ry = py - 2 * B * d / (A**2 + B**2)**0.5
    
    return rx, ry

def main():
    import math
    
    # Read the area of the square
    area = int(input().strip())
    side_length = math.sqrt(area)
    
    # Define the corners of the square
    corners = [
        (0, 0),
        (0, side_length),
        (side_length, side_length),
        (side_length, 0)
    ]
    
    # Read the folding line coordinates
    line_coordinates = list(map(int, input().strip().split()))
    x1, y1, x2, y2 = line_coordinates
    
    # Reflect each corner across the folding line
    reflected_corners = []
    for (px, py) in corners:
        rx, ry = reflect_point(px, py, x1, y1, x2, y2)
        reflected_corners.append((rx, ry))
    
    # Print the reflected corners
    for (rx, ry) in reflected_corners:
        print(f"{rx:.2f} {ry:.2f}")

if __name__ == "__main__":
    main()