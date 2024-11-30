import java.util.*;

public class FoldedArea {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int area = sc.nextInt();
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();

        double side = Math.sqrt(area);

        List<Point> originalCorners = new ArrayList<>();
        originalCorners.add(new Point(0, 0));
        originalCorners.add(new Point(side, 0));
        originalCorners.add(new Point(side, side));
        originalCorners.add(new Point(0, side));

        Line foldLine = new Line(x1, y1, x2, y2);

        Set<Point> resultingPoints = new HashSet<>();

        for (Point corner : originalCorners) {
            resultingPoints.add(corner);
            Point reflectedPoint = foldLine.reflect(corner);
            resultingPoints.add(reflectedPoint);
        }

        List<Point> sortedPoints = new ArrayList<>(resultingPoints);
        Collections.sort(sortedPoints, (p1, p2) -> {
            if (p1.x != p2.x) return Double.compare(p1.x, p2.x);
            return Double.compare(p1.y, p2.y);
        });

        for (Point p : sortedPoints) {
            System.out.printf("%.2f %.2f\n", p.x, p.y);
        }

        sc.close();
    }

    static class Point {
        double x, y;
        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Line {
        double a, b, c;

        Line(int x1, int y1, int x2, int y2) {
            this.a = y1 - y2;
            this.b = x2 - x1;
            this.c = x1 * y2 - x2 * y1;
        }

        Point reflect(Point p) {
            double d = (a * p.x + b * p.y + c) / (a * a + b * b);
            double xReflected = p.x - 2 * a * d;
            double yReflected = p.y - 2 * b * d;
            return new Point(xReflected, yReflected);
        }
    }
}