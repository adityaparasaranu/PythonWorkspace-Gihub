# http_code = "419"
# match http_code:
#     case "200":
#         print("Hi")
#     case "404":
#         print("Not Found")
#     case "419":
#         print("You Found Me")
#     case _:
#         print("Code not found")
#
# http_code = "419"
# if http_code == "200":
#     print("OK")
# elif http_code == "404":
#     print("Not Found Here")
# elif http_code == "419":
#     print("Value Found")
# else:
#     print("Code not found")


# match 401:
#     case 401 | 403 | 404:
#         print("Not allowed")

class Point:
    x: int
    y: int


# def location(point:
#     match point:
#         case Point(x=0, y=0):
#             print("Origin is the point's location.")
#         case Point(x=0, y=y):
#             print(f"Y={y} and the point is on the y-axis.")
#         case Point(x=x, y=0):
#             print(f"X={x} and the point is on the x-axis.")
#         case Point():
#             print("The point is located somewhere else on the plane.")
#         case _:
#             print("Not a point")
#
#
# location((0, 3))

# Point(1, vars)
# Point(1, y=var)
# Point(x=1, y=var)
# Point(y=var, x=1)

# test_variable = ("error", 400, 2)
# match test_variable:
#     case ('warning', code, 40):
#         print("A warning has been received.")
#     case ('error', code, _):
#         print(f"An error {code} occurred.")

# point = (1, 2)
# match point:
#     case x, y if x == y:
#         print(f"The point is located on the diagonal Y=X at {x}.")
#     case x, y:
#         print(f"Point is not on the diagonal.")

# points = []
# match points:
#     case []:
#         print("No points in the list.")
#     case [Point(0, 0)]:
#         print("The origin is the only point in the list.")
#     case [Point(x, y)]:
#         print(f"A single point {x}, {y} is in the list.")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
#     case _:
#         print("Something else is found in the list.")

# class Line:
#     start = "none"
#
# def Point():
#     x:int
#     y:int
#
# start = "test_word"
# end = "test_word"
#

# match get_shape():
#     case Line(start := Point(x, y), end) if start == end:
#         print(f"Zero length line at {x}, {y}")

