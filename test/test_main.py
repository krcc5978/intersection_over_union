from project.iou import intersection_over_union


def test_intersection_over_union1():
    a = (100, 100, 300, 300)
    b = (200, 200, 400, 400)
    assert round(intersection_over_union(a, b), 2) == 0.25


def test_intersection_over_union2():
    a = (100, 100, 300, 300)
    b = (100, 100, 300, 300)
    assert round(intersection_over_union(a, b), 2) == 1.00


def test_intersection_over_union3():
    a = (100, 100, 300, 300)
    b = (400, 400, 600, 600)
    assert round(intersection_over_union(a, b), 2) == 0.00


def test_intersection_over_union4():
    a = (100, 100, 300, 300)
    b = (150, 150, 250, 250)
    assert round(intersection_over_union(a, b), 2) == 1