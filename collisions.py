from circleshape import CircleShape
from triangleshape import TriangleShape


def collision_check(obj1, obj2):
    if isinstance(obj1, CircleShape) and isinstance(obj2, CircleShape):
        return circle_circle_collision(obj1, obj2)
    elif isinstance(obj1, CircleShape) and isinstance(obj2, TriangleShape):
        return circle_triangle_collision(obj1, obj2)
    elif isinstance(obj1, TriangleShape) and isinstance(obj2, CircleShape):
        return circle_triangle_collision(obj2, obj1)
    elif isinstance(obj1, TriangleShape) and isinstance(obj2, TriangleShape):
        pass


def circle_circle_collision(circle1, circle2):
    return (
        circle1.position.distance_to(circle2.position)
        <= circle1.radius + circle2.radius
    )


def circle_triangle_collision(circle, triangle):
    vertices = triangle.calculate_vertices()
    for vertex in vertices:
        if circle.position.distance_to(vertex) <= circle.radius:
            return True

    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]

        ab = b - a
        ap = circle.position - a
        ab_squared = ab.dot(ab)

        if ab_squared == 0:
            t = 0
        else:
            t = max(0, min(1, ap.dot(ab) / ab_squared))

        if circle.position.distance_to(a + ab * t) <= circle.radius:
            return True
